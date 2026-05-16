/**
 * Thai date conversion utilities: BE↔CE, Thai date formatting, Thai numerals.
 *
 * Run self-tests:
 *   npx tsx convert.ts
 */

export const BE_OFFSET = 543;

export function beToCe(year: number): number {
  return year - BE_OFFSET;
}

export function ceToBe(year: number): number {
  return year + BE_OFFSET;
}

export const MONTHS_FULL = [
  "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน",
  "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม",
  "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม",
];

export const MONTHS_ABBR = [
  "ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.",
  "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.",
  "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค.",
];

const MONTH_INDEX = new Map<string, number>();
MONTHS_FULL.forEach((m, i) => MONTH_INDEX.set(m, i + 1));
MONTHS_ABBR.forEach((m, i) => MONTH_INDEX.set(m, i + 1));

const A2T: Record<string, string> = {
  "0": "๐", "1": "๑", "2": "๒", "3": "๓", "4": "๔",
  "5": "๕", "6": "๖", "7": "๗", "8": "๘", "9": "๙",
};
const T2A: Record<string, string> = Object.fromEntries(
  Object.entries(A2T).map(([k, v]) => [v, k]),
);

export function arabicToThaiNumerals(s: string): string {
  return s.replace(/[0-9]/g, (c) => A2T[c]);
}

export function thaiToArabicNumerals(s: string): string {
  return s.replace(/[๐-๙]/g, (c) => T2A[c]);
}

export type Style = "raachakan" | "business" | "casual" | "short";

export function formatThaiDate(d: Date, style: Style = "business"): string {
  const day = d.getDate();
  const monthIdx = d.getMonth();
  const be = ceToBe(d.getFullYear());
  const pad2 = (n: number) => n.toString().padStart(2, "0");
  switch (style) {
    case "raachakan":
      return `วันที่ ${day} ${MONTHS_FULL[monthIdx]} พ.ศ. ${be}`;
    case "business":
      return `${day} ${MONTHS_FULL[monthIdx]} ${be}`;
    case "casual":
      return `${day} ${MONTHS_ABBR[monthIdx]} ${pad2(be % 100)}`;
    case "short":
      return `${pad2(day)}/${pad2(monthIdx + 1)}/${be.toString().padStart(4, "0")}`;
    default: {
      const _exhaustive: never = style;
      throw new Error(`unknown style: ${_exhaustive}`);
    }
  }
}

const DATE_RE =
  /(?:วันที่\s+)?(\d{1,2})\s*(?:\/|\s+)?\s*([^\s/0-9]+|\d{1,2})\s*(?:\/|\s+)?\s*(?:พ\.ศ\.\s*|ค\.ศ\.\s*)?(\d{2,4})/;

export function parseThaiDate(s: string): Date {
  const norm = thaiToArabicNumerals(s.trim());
  const m = norm.match(DATE_RE);
  if (!m) throw new Error(`cannot parse Thai date: ${JSON.stringify(s)}`);
  const dayS = m[1];
  const monthS = m[2].trim();
  const yearS = m[3];

  let month: number;
  if (/^\d+$/.test(monthS)) {
    month = parseInt(monthS, 10);
  } else {
    const normalized = monthS.replace(/\.+$/, "");
    let found: number | undefined;
    for (const [key, idx] of MONTH_INDEX.entries()) {
      if (key.replace(/\.+$/, "") === normalized) {
        found = idx;
        break;
      }
    }
    if (found === undefined) throw new Error(`unknown Thai month: ${JSON.stringify(monthS)}`);
    month = found;
  }

  const day = parseInt(dayS, 10);

  let ce: number;
  if (yearS.length === 4) {
    const y = parseInt(yearS, 10);
    ce = y >= 2400 ? beToCe(y) : y;
  } else if (yearS.length === 2) {
    const yy = parseInt(yearS, 10);
    const be = (yy >= 70 ? 2400 : 2500) + yy;
    ce = beToCe(be);
  } else {
    throw new Error(`bad year length: ${JSON.stringify(yearS)}`);
  }

  return new Date(ce, month - 1, day);
}

// ---------------------------------------------------------------------------
// Self-tests
// ---------------------------------------------------------------------------

function run() {
  const failures: string[] = [];
  const check = (label: string, actual: unknown, expected: unknown) => {
    const a = actual instanceof Date ? actual.toISOString().slice(0, 10) : JSON.stringify(actual);
    const e = expected instanceof Date ? expected.toISOString().slice(0, 10) : JSON.stringify(expected);
    const ok = a === e;
    console.log(`[${ok ? "PASS" : "FAIL"}] ${label}: got ${a}, expected ${e}`);
    if (!ok) failures.push(label);
  };

  check("beToCe(2569)", beToCe(2569), 2026);
  check("ceToBe(2026)", ceToBe(2026), 2569);

  check("arabicToThai 2569", arabicToThaiNumerals("2569"), "๒๕๖๙");
  check("thaiToArabic", thaiToArabicNumerals("๒๕๖๙"), "2569");
  check("mixed thai", arabicToThaiNumerals("16 พ.ค. 2569"), "๑๖ พ.ค. ๒๕๖๙");

  const d = new Date(2026, 4, 16); // May 16, 2026
  check("format raachakan", formatThaiDate(d, "raachakan"), "วันที่ 16 พฤษภาคม พ.ศ. 2569");
  check("format business", formatThaiDate(d, "business"), "16 พฤษภาคม 2569");
  check("format casual", formatThaiDate(d, "casual"), "16 พ.ค. 69");
  check("format short", formatThaiDate(d, "short"), "16/05/2569");

  check("parse raachakan", parseThaiDate("วันที่ 16 พฤษภาคม พ.ศ. 2569"), d);
  check("parse business", parseThaiDate("16 พฤษภาคม 2569"), d);
  check("parse abbr", parseThaiDate("16 พ.ค. 2569"), d);
  check("parse short", parseThaiDate("16/05/2569"), d);
  check("parse casual", parseThaiDate("16 พ.ค. 69"), d);
  check("parse CE", parseThaiDate("16 พ.ค. ค.ศ. 2026"), d);
  check("parse Thai digits", parseThaiDate("๑๖ พฤษภาคม ๒๕๖๙"), d);

  // Round-trip several dates
  for (const sample of [new Date(2024, 0, 1), new Date(1999, 11, 31), new Date(2024, 1, 29)]) {
    const s = formatThaiDate(sample, "business");
    const parsed = parseThaiDate(s);
    check(`round-trip ${sample.toISOString().slice(0, 10)}`, parsed, sample);
  }

  console.log("");
  if (failures.length) {
    console.log(`FAILED: ${failures.length} case(s)`);
    for (const f of failures) console.log(`  - ${f}`);
    process.exit(1);
  }
  console.log("All tests passed.");
}

run();
