/**
 * Thai national ID, tax ID, phone normalization, and PromptPay QR utilities.
 *
 * Run self-tests:
 *   npx tsx validate.ts
 */

// ---------------------------------------------------------------------------
// Thai National ID / Tax ID
// ---------------------------------------------------------------------------

const WEIGHTS = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2];

export function computeCheckDigit(prefix12: string): number {
  if (prefix12.length !== 12 || !/^\d+$/.test(prefix12)) {
    throw new Error("prefix must be exactly 12 digits");
  }
  let total = 0;
  for (let i = 0; i < 12; i++) total += parseInt(prefix12[i], 10) * WEIGHTS[i];
  return (11 - (total % 11)) % 10;
}

export function isValidThaiId(s: string): boolean {
  if (typeof s !== "string") return false;
  const cleaned = s.replace(/[\s-]/g, "");
  if (!/^\d{13}$/.test(cleaned)) return false;
  return computeCheckDigit(cleaned.slice(0, 12)) === parseInt(cleaned[12], 10);
}

// ---------------------------------------------------------------------------
// Phone normalization
// ---------------------------------------------------------------------------

function digitsOnly(s: string): string {
  return s.replace(/[\s\-()]/g, "");
}

export function normalizePhone(s: string): string {
  if (typeof s !== "string") throw new Error("phone must be a string");
  const raw = digitsOnly(s);
  let rest: string;
  if (raw.startsWith("+66")) rest = raw.slice(3);
  else if (raw.startsWith("66") && (raw.length === 10 || raw.length === 11)) rest = raw.slice(2);
  else if (raw.startsWith("0")) rest = raw.slice(1);
  else throw new Error(`unrecognized phone format: ${JSON.stringify(s)}`);
  if (!/^\d+$/.test(rest) || (rest.length !== 8 && rest.length !== 9)) {
    throw new Error(`phone has wrong digit count: ${JSON.stringify(s)}`);
  }
  return "+66" + rest;
}

export function formatPhoneThai(s: string): string {
  const e164 = normalizePhone(s);
  const domestic = "0" + e164.slice(3);
  if (domestic.length === 10) {
    return `${domestic.slice(0, 3)}-${domestic.slice(3, 6)}-${domestic.slice(6)}`;
  }
  return `${domestic.slice(0, 2)}-${domestic.slice(2, 5)}-${domestic.slice(5)}`;
}

// ---------------------------------------------------------------------------
// PromptPay QR
// ---------------------------------------------------------------------------

function tlv(tag: string, value: string): string {
  const len = value.length.toString().padStart(2, "0");
  return `${tag}${len}${value}`;
}

function crc16CcittFalse(data: string): string {
  let crc = 0xffff;
  for (let i = 0; i < data.length; i++) {
    crc ^= data.charCodeAt(i) << 8;
    for (let b = 0; b < 8; b++) {
      if (crc & 0x8000) crc = ((crc << 1) ^ 0x1021) & 0xffff;
      else crc = (crc << 1) & 0xffff;
    }
  }
  return crc.toString(16).toUpperCase().padStart(4, "0");
}

function promptPayTarget(target: string): { tag: string; value: string } {
  const digits = target.replace(/\D/g, "");
  if (digits.length === 13) return { tag: "02", value: digits };
  const e164 = normalizePhone(target);
  const rest = e164.slice(3);
  const value = ("0066" + rest).padStart(13, "0");
  return { tag: "01", value };
}

export function buildPromptPayPayload(target: string, amount?: number): string {
  const sub = promptPayTarget(target);
  const merchantInfo = tlv("00", "A000000677010111") + tlv(sub.tag, sub.value);
  let payload =
    tlv("00", "01") +
    tlv("01", amount === undefined ? "11" : "12") +
    tlv("29", merchantInfo) +
    tlv("53", "764");
  if (amount !== undefined) payload += tlv("54", amount.toFixed(2));
  payload += tlv("58", "TH");
  payload += "6304";
  payload += crc16CcittFalse(payload);
  return payload;
}

// ---------------------------------------------------------------------------
// Self-tests
// ---------------------------------------------------------------------------

function makeValidId(prefix12: string): string {
  return prefix12 + computeCheckDigit(prefix12).toString();
}

function run() {
  const failures: string[] = [];
  const check = (label: string, actual: unknown, expected: unknown) => {
    const ok = JSON.stringify(actual) === JSON.stringify(expected);
    console.log(
      `[${ok ? "PASS" : "FAIL"}] ${label}: got ${JSON.stringify(actual)}, expected ${JSON.stringify(expected)}`,
    );
    if (!ok) failures.push(label);
  };

  // --- Thai ID ---
  // Synthetic fixtures only — none correspond to a real-issued ID.
  const validIds = ["000000000000", "123456789012", "999999999999", "100000000000", "222222222222"].map(makeValidId);
  for (const vid of validIds) {
    check(`isValidThaiId(${vid})`, isValidThaiId(vid), true);
    const lastDigit = parseInt(vid.slice(-1), 10);
    const bad = vid.slice(0, -1) + ((lastDigit + 1) % 10).toString();
    check(`isValidThaiId(${bad}) corrupted`, isValidThaiId(bad), false);
  }

  const v0 = validIds[0];
  const formatted = `${v0[0]}-${v0.slice(1, 5)}-${v0.slice(5, 10)}-${v0.slice(10, 12)}-${v0[12]}`;
  check("isValidThaiId formatted", isValidThaiId(formatted), true);
  check("isValidThaiId empty", isValidThaiId(""), false);
  check("isValidThaiId 12 digits", isValidThaiId("123456789012"), false);
  check("isValidThaiId letters", isValidThaiId("000000000000A"), false);

  // --- Phone ---
  check("normalize +66", normalizePhone("+66812345678"), "+66812345678");
  check("normalize 0X mobile", normalizePhone("0812345678"), "+66812345678");
  check("normalize with dashes", normalizePhone("081-234-5678"), "+66812345678");
  check("normalize with spaces", normalizePhone("+66 81 234 5678"), "+66812345678");
  check("normalize 66 no plus", normalizePhone("66812345678"), "+66812345678");
  check("normalize landline", normalizePhone("02-880-1234"), "+6628801234");
  check("format mobile", formatPhoneThai("+66812345678"), "081-234-5678");
  check("format landline", formatPhoneThai("028801234"), "02-880-1234");
  check("format raw mobile", formatPhoneThai("0812345678"), "081-234-5678");

  // --- PromptPay ---
  const payloadPhone = buildPromptPayPayload("0812345678", 100.0);
  console.log(`[INFO] PromptPay phone+amount payload: ${payloadPhone}`);
  check("PP starts with 000201", payloadPhone.startsWith("000201"), true);
  check("PP CRC pattern", /.+6304[0-9A-F]{4}$/.test(payloadPhone), true);
  const body = payloadPhone.slice(0, -4);
  check("PP CRC verifies", crc16CcittFalse(body), payloadPhone.slice(-4));
  check("PP contains AID", payloadPhone.includes("A000000677010111"), true);
  check("PP phone tag/value", payloadPhone.includes("01130066812345678"), true);

  const payloadId = buildPromptPayPayload(makeValidId("000000000000"));
  console.log(`[INFO] PromptPay national-id static payload: ${payloadId}`);
  check("PP static POI=11", payloadId.includes("010211"), true);
  check("PP ID tag present", payloadId.includes("0213"), true);

  console.log("");
  if (failures.length) {
    console.log(`FAILED: ${failures.length} case(s)`);
    for (const f of failures) console.log(`  - ${f}`);
    process.exit(1);
  }
  console.log("All tests passed.");
}

run();
