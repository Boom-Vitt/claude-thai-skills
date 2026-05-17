/**
 * Thai postal-address parsing and validation.
 *
 * Run self-tests:
 *   npx tsx parse.ts
 */
import { readFileSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

interface Province {
  code: string;
  name_th: string;
  name_en: string;
  postcode_prefix: string;
}

const provincesData = JSON.parse(
  readFileSync(join(__dirname, "provinces.json"), "utf-8"),
);
export const PROVINCES: Province[] = provincesData.provinces;

const PREFIX_TO_PROVINCE = new Map<string, string>();
for (const p of PROVINCES) {
  if (!PREFIX_TO_PROVINCE.has(p.postcode_prefix)) {
    PREFIX_TO_PROVINCE.set(p.postcode_prefix, p.name_th);
  }
}

const PROVINCE_NAMES_TH = new Set(PROVINCES.map((p) => p.name_th));

export interface ParsedAddress {
  house_no: string | null;
  moo: string | null;
  soi: string | null;
  road: string | null;
  building: string | null;
  floor: string | null;
  unit: string | null;
  subdistrict: string | null;
  district: string | null;
  province: string | null;
  postcode: string | null;
}

// For `road` and `building`, capture greedily up to the next recognized
// keyword (or 5-digit postcode / end-of-string) so multi-token names work:
//   ถนนพระราม 9 แขวงห้วยขวาง  → road = "พระราม 9"
//   อาคารชาญอิสสระ ทาวเวอร์   → building = "ชาญอิสสระ ทาวเวอร์"
const ROAD_STOP =
  "(?=\\s+(?:แขวง|ตำบล|ต\\.|เขต|อำเภอ|อ\\.|จังหวัด|จ\\.|รหัสไปรษณีย์|ซอย|ซ\\.|" +
  "อาคาร|ตึก|คอนโด|ชั้น|ห้อง|บ้านเลขที่|เลขที่|หมู่ที่|หมู่|ม\\.)" +
  "|\\s+\\d{5}\\b|\\s*,|$)";

const BUILDING_STOP =
  "(?=\\s+(?:แขวง|ตำบล|ต\\.|เขต|อำเภอ|อ\\.|จังหวัด|จ\\.|รหัสไปรษณีย์|ซอย|ซ\\.|" +
  "ถนน|ถ\\.|ชั้น|ห้อง|บ้านเลขที่|เลขที่|หมู่ที่|หมู่|ม\\.)" +
  "|\\s+\\d{5}\\b|\\s*,|$)";

const FIELD_PATTERNS: Array<{ field: keyof ParsedAddress; pattern: RegExp }> = [
  { field: "house_no", pattern: /(?:บ้านเลขที่|เลขที่)\s*([^\s,]+)/ },
  { field: "moo", pattern: /(?:หมู่ที่|หมู่|ม\.)\s*([0-9๐-๙]+)/ },
  { field: "soi", pattern: /(?:ซอย|ซ\.)\s*([^\s,]+)/ },
  { field: "road", pattern: new RegExp("(?:ถนน|ถ\\.)\\s*(.+?)" + ROAD_STOP) },
  { field: "building", pattern: new RegExp("(?:อาคาร|ตึก|คอนโด)\\s*(.+?)" + BUILDING_STOP) },
  { field: "floor", pattern: /ชั้น\s*([^\s,]+)/ },
  { field: "unit", pattern: /ห้อง\s*([^\s,]+)/ },
  { field: "subdistrict", pattern: /(?:แขวง|ตำบล|ต\.)\s*([^\s,]+)/ },
  { field: "district", pattern: /(?:เขต|อำเภอ|อ\.)\s*([^\s,]+)/ },
  { field: "province", pattern: /(?:จังหวัด|จ\.)\s*([^\s,]+)/ },
  { field: "postcode", pattern: /(?:รหัสไปรษณีย์\s*)?(\b\d{5}\b)/ },
];

export function parseAddress(s: string): ParsedAddress {
  if (typeof s !== "string") throw new Error("address must be a string");
  const cleaned = s.replace(/\s+/g, " ").trim();

  const result: ParsedAddress = {
    house_no: null, moo: null, soi: null, road: null,
    building: null, floor: null, unit: null,
    subdistrict: null, district: null, province: null, postcode: null,
  };

  for (const { field, pattern } of FIELD_PATTERNS) {
    const m = cleaned.match(pattern);
    if (m) result[field] = m[1].trim().replace(/,+$/, "");
  }

  if (!result.province) {
    for (const name of PROVINCE_NAMES_TH) {
      if (cleaned.includes(name)) {
        result.province = name;
        break;
      }
    }
  }

  if (!result.house_no) {
    const m = cleaned.match(/^\s*([0-9๐-๙]+(?:\/[0-9๐-๙]+)?)\b/);
    if (m) result.house_no = m[1];
  }

  return result;
}

export function validatePostcode(pc: string): boolean {
  if (typeof pc !== "string") return false;
  const trimmed = pc.trim();
  if (!/^\d{5}$/.test(trimmed)) return false;
  return PREFIX_TO_PROVINCE.has(trimmed.slice(0, 2));
}

export function provinceFromPostcode(pc: string): string | null {
  if (!validatePostcode(pc)) return null;
  return PREFIX_TO_PROVINCE.get(pc.slice(0, 2)) ?? null;
}

// ---------------------------------------------------------------------------
// Self-tests
// ---------------------------------------------------------------------------

function run() {
  const failures: string[] = [];
  const check = (label: string, actual: unknown, expected: unknown) => {
    const ok = JSON.stringify(actual) === JSON.stringify(expected);
    console.log(`[${ok ? "PASS" : "FAIL"}] ${label}: got ${JSON.stringify(actual)}, expected ${JSON.stringify(expected)}`);
    if (!ok) failures.push(label);
  };

  check("province count", PROVINCES.length, 77);

  check("validate 10110", validatePostcode("10110"), true);
  check("validate 50200", validatePostcode("50200"), true);
  check("validate 99999", validatePostcode("99999"), false);
  check("validate 4 digits", validatePostcode("1011"), false);
  check("validate letters", validatePostcode("10A10"), false);

  check("prefix 10 -> Bangkok", provinceFromPostcode("10110"), "กรุงเทพมหานคร");
  check("prefix 50 -> Chiang Mai", provinceFromPostcode("50200"), "เชียงใหม่");
  check("prefix 83 -> Phuket", provinceFromPostcode("83000"), "ภูเก็ต");
  check("invalid -> null", provinceFromPostcode("99999"), null);

  const bkk = parseAddress(
    "บ้านเลขที่ 123/45 ซอยสุขุมวิท 21 ถนนสุขุมวิท แขวงคลองเตยเหนือ เขตวัฒนา กรุงเทพมหานคร 10110",
  );
  check("BKK house_no", bkk.house_no, "123/45");
  check("BKK soi", bkk.soi, "สุขุมวิท");
  check("BKK road", bkk.road, "สุขุมวิท");
  check("BKK subdistrict", bkk.subdistrict, "คลองเตยเหนือ");
  check("BKK district", bkk.district, "วัฒนา");
  check("BKK province", bkk.province, "กรุงเทพมหานคร");
  check("BKK postcode", bkk.postcode, "10110");

  const prov = parseAddress("99 หมู่ 5 ตำบลสันทราย อำเภอเมืองเชียงใหม่ จังหวัดเชียงใหม่ 50200");
  check("Prov house_no", prov.house_no, "99");
  check("Prov moo", prov.moo, "5");
  check("Prov subdistrict", prov.subdistrict, "สันทราย");
  check("Prov district", prov.district, "เมืองเชียงใหม่");
  check("Prov province", prov.province, "เชียงใหม่");
  check("Prov postcode", prov.postcode, "50200");

  const abbr = parseAddress("12 ม.3 ต.บ้านใหม่ อ.ปากเกร็ด จ.นนทบุรี 11120");
  check("Abbr moo", abbr.moo, "3");
  check("Abbr subdistrict", abbr.subdistrict, "บ้านใหม่");
  check("Abbr district", abbr.district, "ปากเกร็ด");
  check("Abbr province", abbr.province, "นนทบุรี");
  check("Abbr postcode", abbr.postcode, "11120");

  // Multi-token road: พระราม 9 (Arabic numeral)
  const rama9 = parseAddress(
    "บ้านเลขที่ 99 ถนนพระราม 9 แขวงห้วยขวาง เขตห้วยขวาง กรุงเทพมหานคร 10310",
  );
  check("Rama9 road", rama9.road, "พระราม 9");
  check("Rama9 subdistrict", rama9.subdistrict, "ห้วยขวาง");
  check("Rama9 postcode", rama9.postcode, "10310");

  // Multi-token road: สุขุมวิท 21 used as road name (not soi)
  const suk21 = parseAddress(
    "1 ถนนสุขุมวิท 21 แขวงคลองเตยเหนือ เขตวัฒนา กรุงเทพมหานคร 10110",
  );
  check("Suk21 road", suk21.road, "สุขุมวิท 21");
  check("Suk21 subdistrict", suk21.subdistrict, "คลองเตยเหนือ");

  // Multi-token road: ศรีนครินทร์ ๓๔ (Thai numerals)
  const srin = parseAddress(
    "10 ถนนศรีนครินทร์ ๓๔ แขวงหนองบอน เขตประเวศ กรุงเทพมหานคร 10250",
  );
  check("Srin road", srin.road, "ศรีนครินทร์ ๓๔");

  // Multi-token compound road, no number: เลียบทางด่วน
  const leab = parseAddress(
    "55 ถนนเลียบทางด่วน แขวงคลองจั่น เขตบางกะปิ กรุงเทพมหานคร 10240",
  );
  check("Leab road", leab.road, "เลียบทางด่วน");

  // Road at end-of-string (no trailing keyword)
  const eol = parseAddress("ถนนพระราม 4");
  check("EOL road", eol.road, "พระราม 4");

  // Road immediately before bare 5-digit postcode
  const bare = parseAddress("ถนนพระราม 9 10310");
  check("Bare-postcode road", bare.road, "พระราม 9");
  check("Bare-postcode postcode", bare.postcode, "10310");

  // Condo / building / floor / unit
  const condo = parseAddress(
    "อาคารชาญอิสสระ ชั้น 12 ห้อง 1203 บ้านเลขที่ 99 ถนนพระราม 4 " +
      "แขวงสีลม เขตบางรัก กรุงเทพมหานคร 10500",
  );
  check("Condo building", condo.building, "ชาญอิสสระ");
  check("Condo floor", condo.floor, "12");
  check("Condo unit", condo.unit, "1203");
  check("Condo house_no", condo.house_no, "99");
  check("Condo road", condo.road, "พระราม 4");
  check("Condo subdistrict", condo.subdistrict, "สีลม");
  check("Condo district", condo.district, "บางรัก");
  check("Condo postcode", condo.postcode, "10500");

  // ตึก variant + alphanumeric unit code
  const tuek = parseAddress(
    "ตึกเอ ชั้น 5 ห้อง A-15 บ้านเลขที่ 1 ถนนสีลม แขวงสีลม เขตบางรัก กรุงเทพมหานคร 10500",
  );
  check("Tuek building", tuek.building, "เอ");
  check("Tuek floor", tuek.floor, "5");
  check("Tuek unit", tuek.unit, "A-15");

  // คอนโด variant
  const condo2 = parseAddress(
    "คอนโดเดอะนิช ห้อง 88 บ้านเลขที่ 8 ถนนรัชดาภิเษก แขวงดินแดง เขตดินแดง กรุงเทพมหานคร 10400",
  );
  check("Condo2 building", condo2.building, "เดอะนิช");
  check("Condo2 unit", condo2.unit, "88");

  // Backwards-compat: building/floor/unit are null when absent
  const plain = parseAddress("12 ม.3 ต.บ้านใหม่ อ.ปากเกร็ด จ.นนทบุรี 11120");
  check("Plain building null", plain.building, null);
  check("Plain floor null", plain.floor, null);
  check("Plain unit null", plain.unit, null);

  console.log("");
  if (failures.length) {
    console.log(`FAILED: ${failures.length} case(s)`);
    for (const f of failures) console.log(`  - ${f}`);
    process.exit(1);
  }
  console.log("All tests passed.");
}

run();
