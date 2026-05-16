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

## Common mistakes
- **Adding 543 to a parsed BE year.** If the input already says `พ.ศ. 2569`, don't add 543 again — that gives 3112. Always know whether the year you hold is BE or CE.
- **Mixing scripts in one date.** `๑๖ May 2569` looks weird; either go full Thai (`๑๖ พฤษภาคม ๒๕๖๙`) or full Arabic.
- **Two-digit year ambiguity.** `๖๙` could be 2469 or 2569 BE. This skill uses a heuristic (`yy >= 70` → 2400s, else 2500s); for legal documents, prefer 4-digit years.
- **Hard-coding day/month separators.** Thai dates commonly use spaces, not slashes. Slash-form `dd/mm/yyyy` exists but is informal.
- **Month abbreviation dots.** Always include trailing dot: `ม.ค.` not `มค`. The parser handles either, but the formatter emits the canonical dotted form.
