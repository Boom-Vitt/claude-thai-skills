"""Thai postal-address parsing and validation.

Run self-tests:
    python parse.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Optional


_HERE = Path(__file__).parent
_PROVINCES_PATH = _HERE / "provinces.json"


def _load_provinces() -> list[dict]:
    with _PROVINCES_PATH.open(encoding="utf-8") as f:
        return json.load(f)["provinces"]


PROVINCES = _load_provinces()


# Postcode-prefix → list of province names. Bangkok metro shares prefix 10
# with Samut Prakan and Nonthaburi (some sub-districts), so this is many-to-one.
_PREFIX_TO_PROVINCE: dict[str, str] = {}
for p in PROVINCES:
    pref = p["postcode_prefix"]
    # Keep the first-listed province for each prefix; user can disambiguate
    # by looking at the full 5-digit postcode against a finer table.
    _PREFIX_TO_PROVINCE.setdefault(pref, p["name_th"])


_PROVINCE_NAMES_TH = {p["name_th"] for p in PROVINCES}
_PROVINCE_NAMES_EN = {p["name_en"] for p in PROVINCES}


# ---------------------------------------------------------------------------
# Address parsing
# ---------------------------------------------------------------------------

# Tokens we look for, ordered roughly by usual occurrence in a Thai address.
# Each pattern captures the value following the keyword up to the next keyword
# or postcode/end-of-string.
#
# For `road` and `building`, we capture greedily up to the next recognized
# keyword (or postcode / end-of-string) so multi-token names work:
#   ถนนพระราม 9 แขวงห้วยขวาง   → road = "พระราม 9"
#   อาคารชาญอิสสระ ทาวเวอร์ 2  → building = "ชาญอิสสระ ทาวเวอร์ 2"
_ROAD_STOP = (
    r"(?=\s+(?:แขวง|ตำบล|ต\.|เขต|อำเภอ|อ\.|จังหวัด|จ\.|รหัสไปรษณีย์|ซอย|ซ\.|"
    r"อาคาร|ตึก|คอนโด|ชั้น|ห้อง|บ้านเลขที่|เลขที่|หมู่ที่|หมู่|ม\.)"
    r"|\s+\d{5}\b|\s*,|$)"
)
_BUILDING_STOP = (
    r"(?=\s+(?:แขวง|ตำบล|ต\.|เขต|อำเภอ|อ\.|จังหวัด|จ\.|รหัสไปรษณีย์|ซอย|ซ\.|"
    r"ถนน|ถ\.|ชั้น|ห้อง|บ้านเลขที่|เลขที่|หมู่ที่|หมู่|ม\.)"
    r"|\s+\d{5}\b|\s*,|$)"
)

_FIELD_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("house_no",    re.compile(r"(?:บ้านเลขที่|เลขที่)\s*([^\s,]+)")),
    ("moo",         re.compile(r"(?:หมู่ที่|หมู่|ม\.)\s*([0-9๐-๙]+)")),
    ("soi",         re.compile(r"(?:ซอย|ซ\.)\s*([^\s,]+)")),
    ("road",        re.compile(r"(?:ถนน|ถ\.)\s*(.+?)" + _ROAD_STOP)),
    ("building",    re.compile(r"(?:อาคาร|ตึก|คอนโด)\s*(.+?)" + _BUILDING_STOP)),
    ("floor",       re.compile(r"ชั้น\s*([^\s,]+)")),
    ("unit",        re.compile(r"ห้อง\s*([^\s,]+)")),
    ("subdistrict", re.compile(r"(?:แขวง|ตำบล|ต\.)\s*([^\s,]+)")),
    ("district",    re.compile(r"(?:เขต|อำเภอ|อ\.)\s*([^\s,]+)")),
    ("province",    re.compile(r"(?:จังหวัด|จ\.)\s*([^\s,]+)")),
    ("postcode",    re.compile(r"(?:รหัสไปรษณีย์\s*)?(\b\d{5}\b)")),
]


def parse_address(s: str) -> dict:
    """Parse a Thai postal address into a dict.

    Returns a dict with keys: house_no, moo, soi, road, building, floor, unit,
    subdistrict, district, province, postcode. Missing fields are None.

    The parser is keyword-anchored — it relies on Thai labels like บ้านเลขที่,
    หมู่, ซอย, ถนน, แขวง/ตำบล, เขต/อำเภอ, จังหวัด, รหัสไปรษณีย์ (or their abbrev forms).
    Multi-token road names (e.g. ถนนพระราม 9, ถนนเลียบทางด่วน) are captured up to
    the next address keyword. Condo/apartment fields อาคาร/ตึก/คอนโด → building,
    ชั้น → floor, ห้อง → unit are also extracted when present.
    """
    if not isinstance(s, str):
        raise ValueError("address must be a string")
    # Normalize whitespace; preserve commas
    cleaned = re.sub(r"\s+", " ", s).strip()

    result: dict[str, Optional[str]] = {
        "house_no": None,
        "moo": None,
        "soi": None,
        "road": None,
        "building": None,
        "floor": None,
        "unit": None,
        "subdistrict": None,
        "district": None,
        "province": None,
        "postcode": None,
    }

    for field, pattern in _FIELD_PATTERNS:
        m = pattern.search(cleaned)
        if m:
            result[field] = m.group(1).strip().rstrip(",")

    # Special case: if no explicit "จังหวัด"/"จ." token but a known province name appears
    if not result["province"]:
        for name in _PROVINCE_NAMES_TH:
            if name in cleaned:
                result["province"] = name
                break

    # If no "บ้านเลขที่" keyword, fall back: pick the first token that looks like
    # a house-number pattern (digits, optional slash) — but only if not later
    # claimed by another field.
    if not result["house_no"]:
        m = re.match(r"\s*([0-9๐-๙]+(?:/[0-9๐-๙]+)?)\b", cleaned)
        if m:
            result["house_no"] = m.group(1)

    return result


# ---------------------------------------------------------------------------
# Postcode validation
# ---------------------------------------------------------------------------


def validate_postcode(pc: str) -> bool:
    """Return True if `pc` is a syntactically valid Thai postcode.

    A valid postcode is 5 digits whose 2-digit prefix matches at least one
    known province. (Special service codes outside this range will fail; this
    is intentional for everyday use.)
    """
    if not isinstance(pc, str):
        return False
    pc = pc.strip()
    if not re.fullmatch(r"\d{5}", pc):
        return False
    return pc[:2] in _PREFIX_TO_PROVINCE


def province_from_postcode(pc: str) -> Optional[str]:
    """Return the Thai province name guessed from the postcode's first 2 digits.

    NOTE: postcode prefixes are many-to-one — prefix 10 covers Bangkok, Samut
    Prakan, Nonthaburi, Pathum Thani. This function returns ONE canonical
    answer (the first-listed province for that prefix). For precise resolution
    use the full 5-digit postcode and a sub-district database.
    """
    if not validate_postcode(pc):
        return None
    return _PREFIX_TO_PROVINCE.get(pc[:2])


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------


def _run_tests() -> None:
    failures: list[str] = []

    def check(label: str, actual, expected):
        ok = actual == expected
        print(f"[{'PASS' if ok else 'FAIL'}] {label}: got {actual!r}, expected {expected!r}")
        if not ok:
            failures.append(label)

    # Province table
    check("province count", len(PROVINCES), 77)

    # Postcode validation
    check("validate 10110", validate_postcode("10110"), True)
    check("validate 50200", validate_postcode("50200"), True)
    check("validate 99999", validate_postcode("99999"), False)
    check("validate 4 digits", validate_postcode("1011"), False)
    check("validate letters", validate_postcode("10A10"), False)

    # Province from postcode
    check("prefix 10 -> Bangkok", province_from_postcode("10110"), "กรุงเทพมหานคร")
    check("prefix 50 -> Chiang Mai", province_from_postcode("50200"), "เชียงใหม่")
    check("prefix 83 -> Phuket", province_from_postcode("83000"), "ภูเก็ต")
    check("invalid prefix returns None", province_from_postcode("99999"), None)

    # Address parsing — Bangkok style with แขวง/เขต
    bkk = parse_address(
        "บ้านเลขที่ 123/45 ซอยสุขุมวิท 21 ถนนสุขุมวิท แขวงคลองเตยเหนือ เขตวัฒนา กรุงเทพมหานคร 10110"
    )
    check("BKK house_no", bkk["house_no"], "123/45")
    check("BKK soi", bkk["soi"], "สุขุมวิท")
    check("BKK road", bkk["road"], "สุขุมวิท")
    check("BKK subdistrict", bkk["subdistrict"], "คลองเตยเหนือ")
    check("BKK district", bkk["district"], "วัฒนา")
    check("BKK province", bkk["province"], "กรุงเทพมหานคร")
    check("BKK postcode", bkk["postcode"], "10110")

    # Provincial style with ตำบล/อำเภอ
    prov = parse_address(
        "99 หมู่ 5 ตำบลสันทราย อำเภอเมืองเชียงใหม่ จังหวัดเชียงใหม่ 50200"
    )
    check("Prov house_no", prov["house_no"], "99")
    check("Prov moo", prov["moo"], "5")
    check("Prov subdistrict", prov["subdistrict"], "สันทราย")
    check("Prov district", prov["district"], "เมืองเชียงใหม่")
    check("Prov province", prov["province"], "เชียงใหม่")
    check("Prov postcode", prov["postcode"], "50200")

    # Abbreviated form
    abbr = parse_address("12 ม.3 ต.บ้านใหม่ อ.ปากเกร็ด จ.นนทบุรี 11120")
    check("Abbr moo", abbr["moo"], "3")
    check("Abbr subdistrict", abbr["subdistrict"], "บ้านใหม่")
    check("Abbr district", abbr["district"], "ปากเกร็ด")
    check("Abbr province", abbr["province"], "นนทบุรี")
    check("Abbr postcode", abbr["postcode"], "11120")

    # Multi-token road: พระราม 9 (Arabic numeral)
    rama9 = parse_address(
        "บ้านเลขที่ 99 ถนนพระราม 9 แขวงห้วยขวาง เขตห้วยขวาง กรุงเทพมหานคร 10310"
    )
    check("Rama9 road", rama9["road"], "พระราม 9")
    check("Rama9 subdistrict", rama9["subdistrict"], "ห้วยขวาง")
    check("Rama9 postcode", rama9["postcode"], "10310")

    # Multi-token road: สุขุมวิท 21 used as road name (not soi)
    suk21 = parse_address(
        "1 ถนนสุขุมวิท 21 แขวงคลองเตยเหนือ เขตวัฒนา กรุงเทพมหานคร 10110"
    )
    check("Suk21 road", suk21["road"], "สุขุมวิท 21")
    check("Suk21 subdistrict", suk21["subdistrict"], "คลองเตยเหนือ")

    # Multi-token road: ศรีนครินทร์ ๓๔ (Thai numerals)
    srin = parse_address(
        "10 ถนนศรีนครินทร์ ๓๔ แขวงหนองบอน เขตประเวศ กรุงเทพมหานคร 10250"
    )
    check("Srin road", srin["road"], "ศรีนครินทร์ ๓๔")

    # Multi-token compound road, no number: เลียบทางด่วน
    leab = parse_address(
        "55 ถนนเลียบทางด่วน แขวงคลองจั่น เขตบางกะปิ กรุงเทพมหานคร 10240"
    )
    check("Leab road", leab["road"], "เลียบทางด่วน")

    # Road at end-of-string (no trailing keyword)
    eol = parse_address("ถนนพระราม 4")
    check("EOL road", eol["road"], "พระราม 4")

    # Road immediately before bare 5-digit postcode
    bare = parse_address("ถนนพระราม 9 10310")
    check("Bare-postcode road", bare["road"], "พระราม 9")
    check("Bare-postcode postcode", bare["postcode"], "10310")

    # Condo / building / floor / unit
    condo = parse_address(
        "อาคารชาญอิสสระ ชั้น 12 ห้อง 1203 บ้านเลขที่ 99 ถนนพระราม 4 "
        "แขวงสีลม เขตบางรัก กรุงเทพมหานคร 10500"
    )
    check("Condo building", condo["building"], "ชาญอิสสระ")
    check("Condo floor", condo["floor"], "12")
    check("Condo unit", condo["unit"], "1203")
    check("Condo house_no", condo["house_no"], "99")
    check("Condo road", condo["road"], "พระราม 4")
    check("Condo subdistrict", condo["subdistrict"], "สีลม")
    check("Condo district", condo["district"], "บางรัก")
    check("Condo postcode", condo["postcode"], "10500")

    # ตึก variant + alphanumeric unit code
    tuek = parse_address(
        "ตึกเอ ชั้น 5 ห้อง A-15 บ้านเลขที่ 1 ถนนสีลม แขวงสีลม เขตบางรัก กรุงเทพมหานคร 10500"
    )
    check("Tuek building", tuek["building"], "เอ")
    check("Tuek floor", tuek["floor"], "5")
    check("Tuek unit", tuek["unit"], "A-15")

    # คอนโด variant
    condo2 = parse_address(
        "คอนโดเดอะนิช ห้อง 88 บ้านเลขที่ 8 ถนนรัชดาภิเษก แขวงดินแดง เขตดินแดง กรุงเทพมหานคร 10400"
    )
    check("Condo2 building", condo2["building"], "เดอะนิช")
    check("Condo2 unit", condo2["unit"], "88")

    # Backwards-compat: building/floor/unit are None when absent
    plain = parse_address("12 ม.3 ต.บ้านใหม่ อ.ปากเกร็ด จ.นนทบุรี 11120")
    check("Plain building None", plain["building"], None)
    check("Plain floor None", plain["floor"], None)
    check("Plain unit None", plain["unit"], None)

    print()
    if failures:
        print(f"FAILED: {len(failures)} case(s)")
        for f in failures:
            print(f"  - {f}")
        raise SystemExit(1)
    print("All tests passed.")


if __name__ == "__main__":
    _run_tests()
