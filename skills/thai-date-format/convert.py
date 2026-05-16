"""Thai date conversion utilities: BE↔CE, Thai date formatting, Thai numerals.

Run self-tests:
    python convert.py
"""
from __future__ import annotations

import re
from datetime import date
from typing import Literal


# ---------------------------------------------------------------------------
# BE / CE year conversion
# ---------------------------------------------------------------------------
# BE = CE + 543. The pre-1941 fiscal-year shift (Thai year started 1 April
# before 2484 BE) is documented in SKILL.md but intentionally NOT in code:
# this module assumes the modern Gregorian-aligned calendar.

BE_OFFSET = 543


def be_to_ce(year: int) -> int:
    return year - BE_OFFSET


def ce_to_be(year: int) -> int:
    return year + BE_OFFSET


# ---------------------------------------------------------------------------
# Month tables
# ---------------------------------------------------------------------------

MONTHS_FULL = [
    "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน",
    "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม",
    "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม",
]

MONTHS_ABBR = [
    "ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.",
    "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.",
    "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค.",
]

# month -> 1..12 index for parsing
_MONTH_INDEX: dict[str, int] = {}
for i, m in enumerate(MONTHS_FULL, start=1):
    _MONTH_INDEX[m] = i
for i, m in enumerate(MONTHS_ABBR, start=1):
    _MONTH_INDEX[m] = i


# ---------------------------------------------------------------------------
# Thai numerals
# ---------------------------------------------------------------------------

_ARABIC = "0123456789"
_THAI = "๐๑๒๓๔๕๖๗๘๙"
_A2T = str.maketrans(_ARABIC, _THAI)
_T2A = str.maketrans(_THAI, _ARABIC)


def arabic_to_thai_numerals(s: str) -> str:
    return s.translate(_A2T)


def thai_to_arabic_numerals(s: str) -> str:
    return s.translate(_T2A)


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

Style = Literal["raachakan", "business", "casual", "short"]


def format_thai_date(d: date, style: Style = "business") -> str:
    """Format a Gregorian `date` in Thai with BE year.

    Styles:
        raachakan: "วันที่ 16 พฤษภาคม พ.ศ. 2569"
        business:  "16 พฤษภาคม 2569"
        casual:    "16 พ.ค. 69"
        short:     "16/05/2569"
    """
    be = ce_to_be(d.year)
    if style == "raachakan":
        return f"วันที่ {d.day} {MONTHS_FULL[d.month - 1]} พ.ศ. {be}"
    if style == "business":
        return f"{d.day} {MONTHS_FULL[d.month - 1]} {be}"
    if style == "casual":
        return f"{d.day} {MONTHS_ABBR[d.month - 1]} {be % 100:02d}"
    if style == "short":
        return f"{d.day:02d}/{d.month:02d}/{be:04d}"
    raise ValueError(f"unknown style: {style}")


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

# Matches: optional "วันที่", day, month (full or abbr or 1-2 digit), optional "พ.ศ.", year
_DATE_RE = re.compile(
    r"(?:วันที่\s+)?"                  # optional "วันที่ "
    r"(\d{1,2})\s*"                    # day
    r"(?:/|\s+)?\s*"                   # separator
    r"([^\s/0-9]+|\d{1,2})\s*"         # month (Thai word or numeric)
    r"(?:/|\s+)?\s*"                   # separator
    r"(?:พ\.ศ\.\s*|ค\.ศ\.\s*)?"        # optional era marker
    r"(\d{2,4})"                       # year
)


def parse_thai_date(s: str) -> date:
    """Parse a Thai-formatted date string.

    Accepts full Thai month names (มกราคม), abbreviated forms (ม.ค.), or
    numeric months. Accepts BE or CE year:
      - 4-digit year >= 2400 -> BE
      - 4-digit year < 2400 -> CE
      - 2-digit year -> assumed BE last-two-digits, full BE = 2500 + yy
        (or 2400 + yy if yy >= 70; rough heuristic for casual style)
    Thai numerals are normalized to Arabic first.
    """
    s = thai_to_arabic_numerals(s.strip())
    m = _DATE_RE.search(s)
    if not m:
        raise ValueError(f"cannot parse Thai date: {s!r}")
    day_s, month_s, year_s = m.group(1), m.group(2).strip(), m.group(3)

    # Resolve month
    if month_s.isdigit():
        month = int(month_s)
    else:
        # try exact match; if not, try without trailing dot variations
        normalized = month_s.rstrip(".")
        month = None
        for key, idx in _MONTH_INDEX.items():
            if key.rstrip(".") == normalized:
                month = idx
                break
        if month is None:
            raise ValueError(f"unknown Thai month: {month_s!r}")

    day = int(day_s)

    # Resolve year
    if len(year_s) == 4:
        y = int(year_s)
        ce = be_to_ce(y) if y >= 2400 else y
    elif len(year_s) == 2:
        yy = int(year_s)
        # Heuristic: yy 00-69 -> 2500+yy BE, yy 70-99 -> 2400+yy BE
        be = (2400 if yy >= 70 else 2500) + yy
        ce = be_to_ce(be)
    else:
        raise ValueError(f"bad year length: {year_s!r}")

    return date(ce, month, day)


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

    # BE/CE
    check("be_to_ce(2569)", be_to_ce(2569), 2026)
    check("ce_to_be(2026)", ce_to_be(2026), 2569)
    check("round-trip", be_to_ce(ce_to_be(1999)), 1999)

    # Numerals
    check("arabic_to_thai 2569", arabic_to_thai_numerals("2569"), "๒๕๖๙")
    check("thai_to_arabic ๒๕๖๙", thai_to_arabic_numerals("๒๕๖๙"), "2569")
    check("mixed thai", arabic_to_thai_numerals("16 พ.ค. 2569"), "๑๖ พ.ค. ๒๕๖๙")

    # Formatting
    d = date(2026, 5, 16)
    check("format raachakan", format_thai_date(d, "raachakan"), "วันที่ 16 พฤษภาคม พ.ศ. 2569")
    check("format business",  format_thai_date(d, "business"),  "16 พฤษภาคม 2569")
    check("format casual",    format_thai_date(d, "casual"),    "16 พ.ค. 69")
    check("format short",     format_thai_date(d, "short"),     "16/05/2569")

    # Parsing
    check("parse raachakan",  parse_thai_date("วันที่ 16 พฤษภาคม พ.ศ. 2569"), d)
    check("parse business",   parse_thai_date("16 พฤษภาคม 2569"), d)
    check("parse abbr",       parse_thai_date("16 พ.ค. 2569"), d)
    check("parse short",      parse_thai_date("16/05/2569"), d)
    check("parse casual",     parse_thai_date("16 พ.ค. 69"), d)
    check("parse with CE",    parse_thai_date("16 พ.ค. ค.ศ. 2026"), d)
    check("parse Thai digits", parse_thai_date("๑๖ พฤษภาคม ๒๕๖๙"), d)

    # Round-trip on a variety of dates
    for sample in [date(2024, 1, 1), date(1999, 12, 31), date(2026, 2, 29) if False else date(2024, 2, 29)]:
        s_full = format_thai_date(sample, "business")
        parsed = parse_thai_date(s_full)
        check(f"round-trip {sample}", parsed, sample)

    print()
    if failures:
        print(f"FAILED: {len(failures)} case(s)")
        for f in failures:
            print(f"  - {f}")
        raise SystemExit(1)
    print("All tests passed.")


if __name__ == "__main__":
    _run_tests()
