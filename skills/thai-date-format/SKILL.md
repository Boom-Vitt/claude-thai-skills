---
name: thai-date-format
description: Use this skill for any task involving Thai date formatting, Buddhist Era (พ.ศ.) ↔ Gregorian (ค.ศ.) year conversion, or Arabic ↔ Thai numeral conversion. Trigger whenever the user asks to: convert พ.ศ. to ค.ศ. or vice versa, format a date in Thai government / business / casual style, parse a Thai date string with full or abbreviated month names, or convert digits between 0123456789 and ๐๑๒๓๔๕๖๗๘๙. Also trigger for requests like "แปลง พ.ศ. เป็น ค.ศ.", "จัดรูปแบบวันที่ไทย", "วันที่แบบราชการ", "เปลี่ยนเป็นเลขไทย", or any variation involving Thai calendar dates.
---

# Thai Date Format (แปลงวันที่ไทย พ.ศ./ค.ศ.)

## Overview
แปลงระหว่าง พ.ศ. กับ ค.ศ. (`BE = CE + 543`), จัดรูปแบบวันที่ไทยตามสไตล์ราชการ / ธุรกิจ / กันเอง / สั้น, และสลับเลขอารบิก ↔ เลขไทย. Handles full month names (มกราคม) and abbreviations (ม.ค.).

## When to use
- รายงาน/หนังสือราชการที่ต้องการ พ.ศ.
- Parse วันที่จากเอกสาร PDF/Excel ที่ใช้ภาษาไทย
- แสดงผลในแอปสำหรับผู้ใช้ไทย (ทั้งเลขไทยและ พ.ศ.)
- DO NOT use for pre-1941 historical documents where the Thai fiscal year started 1 April; this module assumes Gregorian-aligned years.

## Example prompts
- "แปลง วันที่ 16 พฤษภาคม พ.ศ. 2569 เป็น ISO date"
- "Format วันนี้แบบราชการพร้อมเลขไทย"
- "Parse '๑๖ พ.ค. ๖๙' ให้เป็น Date object"

## Quick reference

### Year conversion
`BE = CE + 543` (e.g., 2026 → 2569). Pre-1941 documents may use a 1 April fiscal-year start — not handled here; convert manually if needed.

### Month tables

| # | Full (เต็ม) | Abbreviated (ย่อ) |
|---|---|---|
| 1 | มกราคม | ม.ค. |
| 2 | กุมภาพันธ์ | ก.พ. |
| 3 | มีนาคม | มี.ค. |
| 4 | เมษายน | เม.ย. |
| 5 | พฤษภาคม | พ.ค. |
| 6 | มิถุนายน | มิ.ย. |
| 7 | กรกฎาคม | ก.ค. |
| 8 | สิงหาคม | ส.ค. |
| 9 | กันยายน | ก.ย. |
| 10 | ตุลาคม | ต.ค. |
| 11 | พฤศจิกายน | พ.ย. |
| 12 | ธันวาคม | ธ.ค. |

### Numerals
| Arabic | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Thai | ๐ | ๑ | ๒ | ๓ | ๔ | ๕ | ๖ | ๗ | ๘ | ๙ |

### Format styles

| Style | Output example | Use case |
|---|---|---|
| `raachakan` | `วันที่ 16 พฤษภาคม พ.ศ. 2569` | หนังสือราชการ |
| `business` | `16 พฤษภาคม 2569` | จดหมายธุรกิจ ใบกำกับภาษี |
| `casual` | `16 พ.ค. 69` | SMS, chat |
| `short` | `16/05/2569` | ตาราง, spreadsheet |

## Implementation
- Python: [`convert.py`](convert.py) — `python convert.py` runs self-tests
- TypeScript: [`convert.ts`](convert.ts) — `npx tsx convert.ts` runs self-tests

## ปฏิทินจันทรคติ (Lunar calendar — ขึ้น/แรม)
Thai Buddhist lunar dates use **ขึ้น N ค่ำ** (waxing, days 1–15 as moon grows) and **แรม N ค่ำ** (waning, days 1–14 or 1–15 as moon shrinks), tied to lunar months written either as เดือนอ้าย, เดือนยี่, เดือนสาม … เดือนสิบสอง or simply เดือน ๑–๑๒ / เดือน 1–12.

### When this format is used
- พิธีกรรมทางศาสนา (Buddhist religious ceremonies, ordinations, ทอดกฐิน, ทอดผ้าป่า)
- วันพระ (every ขึ้น ๘ ค่ำ, ขึ้น ๑๕ ค่ำ, แรม ๘ ค่ำ, แรม ๑๔/๑๕ ค่ำ)
- วันสำคัญทางพุทธศาสนา — วิสาขบูชา (ขึ้น ๑๕ ค่ำ เดือน ๖), มาฆบูชา (ขึ้น ๑๕ ค่ำ เดือน ๓), อาสาฬหบูชา (ขึ้น ๑๕ ค่ำ เดือน ๘), วันเข้าพรรษา (แรม ๑ ค่ำ เดือน ๘), วันออกพรรษา (ขึ้น ๑๕ ค่ำ เดือน ๑๑)
- Official Buddhist event invitations typically write the lunar date first, then the Gregorian/BE date in parentheses: `วันขึ้น ๑๕ ค่ำ เดือน ๖ (ตรงกับวันอังคารที่ ๑๙ พฤษภาคม พ.ศ. ๒๕๖๙)`

### Basic structure
- A lunar month = waxing half (ขึ้น ๑–๑๕ ค่ำ, 15 days) + waning half (แรม ๑ ค่ำ to แรม ๑๔ or ๑๕ ค่ำ).
- เดือนคี่ (odd months) usually have แรม ๑๔ ค่ำ as the last day; เดือนคู่ (even months) usually have แรม ๑๕ ค่ำ. Adhikamāsa (อธิกมาส) leap-month years add an extra เดือน ๘ (called เดือน ๘-๘).
- DO NOT attempt manual conversion to Gregorian — alignment shifts every year. If conversion is needed, point the user at **PyThaiNLP** (`pythainlp.util` has lunar helpers) or the **thai-calendar-converter** npm package.

### Formatting rules
- Always use Thai numerals when written formally: `ขึ้น ๑๕ ค่ำ เดือน ๖`, not `ขึ้น 15 ค่ำ เดือน 6`.
- Space between each token: `ขึ้น` + space + numeral + space + `ค่ำ` + space + `เดือน` + space + numeral.
- For the first two months, ordinal names อ้าย (1) and ยี่ (2) are preferred in traditional contexts; numeric เดือน ๑ / เดือน ๒ is acceptable in modern writing.

## รูปแบบเวลา (Thai time format)
Thai uses a **dot** as the hour/minute separator (NOT colon) and ends with **น.** (abbreviation of นาฬิกา). Business and official writing always uses the **24-hour clock + น.**

### Canonical form
- `08.30 น.` (8:30 AM)
- `13.45 น.` (1:45 PM)
- `00.05 น.` (just after midnight)
- `23.59 น.` (one minute before midnight)

### Rules
- Always two-digit hour with leading zero: `08.30 น.` not `8.30 น.`.
- Always two-digit minute: `13.05 น.` not `13.5 น.`.
- Dot separator, not colon: `08.30` not `08:30`.
- Space before `น.` and keep the trailing dot.
- For time ranges use เวลา prefix and ถึง / `–`: `เวลา 09.00 – 12.00 น.` or `เวลา 09.00 ถึง 12.00 น.`.

### Traditional 6-period system (โมง / บ่าย / เย็น / ทุ่ม / ตี)
Still common in speech and casual chat, but **do not use in official documents, contracts, invoices, or formal invitations**:
- ตี ๑–ตี ๕ = 01.00–05.00 น.
- ๖ โมงเช้า–๑๑ โมงเช้า = 06.00–11.00 น.
- เที่ยง / เที่ยงวัน = 12.00 น.
- บ่ายโมง–บ่าย ๓ โมง = 13.00–15.00 น.
- ๔ โมงเย็น–๖ โมงเย็น = 16.00–18.00 น.
- ๑ ทุ่ม–๕ ทุ่ม = 19.00–23.00 น.
- เที่ยงคืน = 00.00 น.

## Common mistakes
- **Adding 543 to a parsed BE year.** If the input already says `พ.ศ. 2569`, don't add 543 again — that gives 3112. Always know whether the year you hold is BE or CE.
- **Mixing scripts in one date.** `๑๖ May 2569` looks weird; either go full Thai (`๑๖ พฤษภาคม ๒๕๖๙`) or full Arabic.
- **Two-digit year ambiguity.** `๖๙` could be 2469 or 2569 BE. This skill uses a heuristic (`yy >= 70` → 2400s, else 2500s); for legal documents, prefer 4-digit years.
- **Hard-coding day/month separators.** Thai dates commonly use spaces, not slashes. Slash-form `dd/mm/yyyy` exists but is informal.
- **Month abbreviation dots.** Always include trailing dot: `ม.ค.` not `มค`. The parser handles either, but the formatter emits the canonical dotted form.
- **Colon in Thai time.** `08:30 AM` or `08:30 น.` is wrong for Thai writing — use dot: `08.30 น.`. The `AM`/`PM` suffix is also wrong; switch to 24-hour + `น.`
- **Missing leading zero in time.** `8.30 น.` or `9.5 น.` on an official document looks unprofessional. Always pad to `08.30 น.` and `09.05 น.`
- **Trying to hand-convert lunar dates.** Do not guess the Gregorian equivalent of `ขึ้น ๑๕ ค่ำ เดือน ๖` — the mapping shifts each year and adhikamāsa years insert an extra เดือน ๘. Use PyThaiNLP or thai-calendar-converter, or quote the lunar date verbatim alongside the official Gregorian date supplied by the issuer.
