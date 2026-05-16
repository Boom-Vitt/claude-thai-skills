---
name: thai-address
description: Use this skill for any task involving Thai postal address parsing, validation, formatting, or province/postcode lookup. Trigger whenever the user asks to: parse a Thai address into fields, validate a 5-digit Thai postcode, look up a province from its postcode, or format an address for a shipping label. Also trigger for requests like "แยกที่อยู่ไทย", "ตรวจรหัสไปรษณีย์", "แปลที่อยู่เป็นภาษาอังกฤษ", "ที่อยู่จัดส่ง", or any variation involving Thai addresses with ตำบล/แขวง/อำเภอ/เขต/จังหวัด.
---

# Thai Address (แยก/ตรวจที่อยู่ไทย)

## Overview
แยกที่อยู่ไทย (บ้านเลขที่ หมู่ ซอย ถนน ตำบล/แขวง อำเภอ/เขต จังหวัด รหัสไปรษณีย์) เป็น structured dict, ตรวจ postcode 5 หลัก, ดูจังหวัดจาก 2 หลักแรกของ postcode, และ map ระหว่างชื่อไทย/อังกฤษของ 77 จังหวัด.

## When to use
- Parse ที่อยู่จากฟอร์ม, e-commerce, PDF
- ตรวจรหัสไปรษณีย์ก่อน submit
- แปลที่อยู่ไทย → English transliteration สำหรับฉลากพัสดุระหว่างประเทศ
- DO NOT use as a delivery-routing source of truth — postcode prefixes are many-to-one (Bangkok metro area shares prefix 10). For exact sub-district resolution, use a Thailand Post sub-district database.

## Example prompts
- "แยกที่อยู่นี้ให้หน่อย: 123/45 ซอยสุขุมวิท 21 ถนนสุขุมวิท แขวงคลองเตยเหนือ เขตวัฒนา กรุงเทพ 10110"
- "รหัส 50200 อยู่จังหวัดอะไร"

## Field ordering (สำคัญ!)

Thai postal addresses go small-to-large — the **reverse** of English convention. Always order fields like this on a shipping label:

```
บ้านเลขที่ → หมู่ → ซอย → ถนน → ตำบล/แขวง → อำเภอ/เขต → จังหวัด → รหัสไปรษณีย์
```

Example:
```
123/45 ซอยสุขุมวิท 21 ถนนสุขุมวิท
แขวงคลองเตยเหนือ เขตวัฒนา
กรุงเทพมหานคร 10110
```

## Bangkok vs provincial vocabulary

| Concept | Bangkok | Province | English |
|---|---|---|---|
| Sub-district | แขวง | ตำบล (ต.) | Sub-district / Tambon / Khwaeng |
| District | เขต | อำเภอ (อ.) | District / Amphoe / Khet |
| Province | กรุงเทพมหานคร | จังหวัด (จ.) | Bangkok / Province / Changwat |

**Never mix these.** A Bangkok address must use แขวง/เขต; a provincial address must use ตำบล/อำเภอ. Mixing them is a strong "this address is wrong" signal.

## Transliteration cheatsheet

| Thai | English / Roman |
|---|---|
| บ้านเลขที่ / เลขที่ | No. |
| หมู่ที่ / หมู่ / ม. | Moo / Mu |
| ซอย / ซ. | Soi |
| ถนน / ถ. | Road / Rd. |
| ตำบล / ต. | Sub-district / Tambon |
| อำเภอ / อ. | District / Amphoe |
| แขวง | Sub-district / Khwaeng |
| เขต | District / Khet |
| จังหวัด / จ. | Province / Changwat |
| รหัสไปรษณีย์ | Postcode |

## Quick reference

| Function | Returns |
|---|---|
| `parse_address(s)` | dict with 8 keys (any may be `None`) |
| `validate_postcode(pc)` | `bool` |
| `province_from_postcode(pc)` | Thai province name or `None` |

### Postcode prefix map (selected)
| Prefix | Region |
|---|---|
| 10 | กรุงเทพมหานคร & ปริมณฑล (sub-districts of Samut Prakan also fall here) |
| 11 | นนทบุรี |
| 12 | ปทุมธานี |
| 20–27 | ภาคตะวันออก |
| 30–49 | ภาคอีสาน |
| 50–58 | ภาคเหนือ |
| 60–67 | ภาคเหนือตอนล่าง |
| 70–77 | ภาคกลาง/ตะวันตก |
| 80–86 | ภาคใต้ตอนบน |
| 90–96 | ภาคใต้ตอนล่าง |

Full 77-province table: [`provinces.json`](provinces.json).

## Implementation
- Python: [`parse.py`](parse.py) — `python parse.py` runs self-tests
- TypeScript: [`parse.ts`](parse.ts) — `npx tsx parse.ts` runs self-tests

## Common mistakes
- **Field reversal.** Writing `Bangkok 10110 Wattana Khwaeng…` in English order on a Thai-side label confuses postmen. Always small-to-large in Thai.
- **Mixing แขวง with อำเภอ.** Bangkok = แขวง/เขต. Everywhere else = ตำบล/อำเภอ. Never mix.
- **Trusting postcode prefix alone.** Prefix 10 spans Bangkok, Samut Prakan, parts of Nonthaburi and Pathum Thani. Use the full 5-digit code for routing.
- **Dropping leading zeros from house numbers.** `123/4` and `123/04` may differ; preserve as the user wrote them.
- **Soi naming.** Soi names are often the same as the parent road (`ซอยสุขุมวิท 21` is off `ถนนสุขุมวิท`). Don't merge them or you'll lose the sub-numbering.
