---
name: thai-id-validate
description: Use this skill for any task involving Thai national ID, tax ID, phone number, or PromptPay QR code validation, normalization, or generation. Trigger whenever the user asks to: validate a Thai citizen ID, check a tax ID checksum, normalize Thai phone numbers between +66 and 0X formats, or build a PromptPay QR payload. Also trigger for requests like "ตรวจเลขบัตรประชาชน", "เช็คเลขผู้เสียภาษี", "แปลงเบอร์โทร +66", "สร้าง PromptPay QR", "ทำคิวอาร์พร้อมเพย์", or any variation involving 13-digit Thai IDs or Thai phone formats.
---

# Thai ID / Phone / PromptPay (ตรวจเลขบัตร เบอร์ พร้อมเพย์)

## Overview
ตรวจสอบ checksum ของเลขบัตรประชาชนไทย / เลขประจำตัวผู้เสียภาษี (13 หลัก), แปลงเบอร์โทรระหว่างรูป `+66` กับ `0X`, และสร้าง payload สำหรับ PromptPay QR (รูปแบบ EMVCo TLV). Algorithm and TLV layout follow the official Thai Revenue Department and ITMX PromptPay specifications.

## When to use
- ตรวจ checksum เลขบัตรประชาชน 13 หลัก (citizen ID / individual tax ID share the same algorithm)
- Normalize เบอร์โทร: ผู้ใช้ป้อน `+66 81 234 5678` แต่ระบบเก็บ `0812345678`
- สร้าง QR สำหรับรับเงิน PromptPay จากเบอร์มือถือหรือเลขบัตรประชาชน
- DO NOT use for company tax IDs that follow non-standard formats, or for verifying that an ID belongs to a real person (checksum only proves format, not existence).

## Example prompts
- "ตรวจเลขบัตร 1-1017-00230-70-X ให้หน่อย"
- "เบอร์ 081-234-5678 แปลงเป็น E.164 ให้ที"
- "สร้าง PromptPay QR เบอร์ 0812345678 จำนวน 250 บาท"

## Quick reference

| Function | ภาษาไทย | Returns |
|---|---|---|
| `is_valid_thai_id(s)` | ตรวจ checksum | `bool` |
| `normalize_phone(s)` | แปลงเป็น `+66XXXXXXXXX` | `str` |
| `format_phone_thai(s)` | แปลงเป็น `0XX-XXX-XXXX` | `str` |
| `build_promptpay_payload(target, amount?)` | สร้าง QR payload | `str` |

### Thai ID checksum algorithm
ให้ตัวเลข 12 หลักแรก คูณด้วยน้ำหนัก `[13,12,11,10,9,8,7,6,5,4,3,2]` แล้วรวมกัน. นำผลรวม mod 11, เอา 11 ลบ, แล้ว mod 10 อีกครั้ง = check digit (หลักที่ 13).

### Phone format rules
- หลังจาก strip เครื่องหมายเว้นวรรค `-` `()` แล้ว
- ขึ้นต้น `+66`, `66`, หรือ `0` ถือว่าเทียบเท่ากัน
- มือถือ: 10 หลักรวม 0 (06, 08, 09 หลังจาก 0)
- บ้าน Bangkok: 9 หลักรวม 0 (เช่น 02-880-1234)

### PromptPay TLV (key tags)
- `00` Payload Format Indicator `01`
- `01` POI Method: `11` static / `12` dynamic (with amount)
- `29` Merchant Account Info → sub-tag `00` AID `A000000677010111`, sub-tag `01` phone (`0066` + เบอร์, pad to 13 chars) **or** `02` national ID (13 digits)
- `53` Currency `764` (THB)
- `54` Amount (optional)
- `58` Country `TH`
- `63` CRC-16/CCITT-FALSE (uppercase 4-hex) over the entire payload **including** the `6304` tag/length prefix

## Implementation
- Python: [`validate.py`](validate.py) — `python validate.py` runs all self-tests
- TypeScript: [`validate.ts`](validate.ts) — `npx tsx validate.ts` runs all self-tests

## เลขหลักแรกของบัตรประชาชน (First-digit prefix)
หลักแรกของเลข 13 หลักบอก *ประเภท* ของผู้ถือบัตรตามที่กรมการปกครอง (DOPA) กำหนด มี 8 ประเภทหลัก:

| หลักแรก | ความหมาย (TH) | Meaning (EN) |
|---|---|---|
| **1** | สัญชาติไทย เกิดและแจ้งเกิดตามกำหนด ตั้งแต่ 1 ม.ค. 2527 | Thai citizen born ≥ 1 Jan 1984 with timely birth registration |
| **2** | สัญชาติไทย เกิดและแจ้งเกิดเกินกำหนด ตั้งแต่ 1 ม.ค. 2527 | Thai citizen born ≥ 1984 with late birth registration |
| **3** | สัญชาติไทย มีชื่อในทะเบียนบ้านก่อน 1 ม.ค. 2527 | Thai citizen already in household registry before 1984 |
| **4** | สัญชาติไทย ไม่มีชื่อในทะเบียนบ้านก่อน 1 ม.ค. 2527 (เพิ่มชื่อช่วงสำรวจ) | Thai citizen not in the initial pre-1984 registry |
| **5** | สัญชาติไทย เพิ่มชื่อเข้าทะเบียนบ้านภายหลัง (รวมแจ้งเกิดเกินกำหนดและกรณีกลับคืนสัญชาติ) | Thai citizen added to registry later (incl. late birth & re-recognition) |
| **6** | บุคคลที่เข้าเมืองโดยชอบด้วยกฎหมายชั่วคราว / ผู้พลัดถิ่น / ชนกลุ่มน้อย | Lawful temporary resident, displaced person, or ethnic minority awaiting status |
| **7** | บุตรของบุคคลประเภท 6 ที่เกิดในประเทศไทย | Children of category-6 persons, born in Thailand |
| **8** | บุคคลต่างด้าวที่ได้รับสัญชาติไทย / มีถิ่นที่อยู่ถาวร | Naturalized Thai citizen or permanent-residence holder |

หมายเหตุ: หลักแรก `0` เคยใช้กับกรณีพิเศษบางอย่างในอดีต แต่พบได้น้อยมากในระบบปัจจุบัน. ใช้สำหรับงาน HR/KYC เพื่อเข้าใจ background ของผู้สมัคร — **ห้าม** ใช้หลักแรกเพียงอย่างเดียวเป็นเกณฑ์เลือกปฏิบัติ (เช่น ปฏิเสธรับสมัครงานเพราะหลักแรกไม่ใช่ 1–5) เพราะผิดทั้งกฎหมายแรงงานและไม่ตรงเจตนาของระบบเลขประจำตัว.

## Slip QR (QR บนสลิปโอนเงิน)
แอปธนาคารไทยยุคใหม่ฝัง QR code ไว้บนสลิปโอนเงินทุกใบ เพื่อให้ผู้รับเงิน *ยืนยันสลิปได้จริง* แทนที่จะเชื่อภาพ JPG ที่อาจถูกตัดต่อ.

**โครงสร้าง payload.** เป็น EMVCo TLV (รูปแบบเดียวกับ PromptPay payment QR) แต่เป็น *คนละ profile* — เก็บข้อมูลธุรกรรมแทนข้อมูลผู้รับเงิน. ฟิลด์ทั่วไปที่อยู่ใน TLV ของสลิป:
- Payload format indicator + POI method (เช่นเดียวกับ PromptPay)
- รหัสธนาคารผู้ส่ง (sending bank ID, 3 หลักตามรหัส BOT)
- รหัสธนาคารผู้รับ (receiving bank ID)
- เลขอ้างอิงธุรกรรม (transaction reference ID — รหัสเฉพาะที่ธนาคารผู้ส่งออกให้)
- จำนวนเงิน, สกุลเงิน (`764`), country (`TH`)
- timestamp ของการโอน
- CRC-16/CCITT-FALSE ปิดท้าย

**การยืนยัน.** เมื่อสแกน QR บนสลิป แอปธนาคารจะดึง `(sending_bank_id, transaction_ref_id)` ออกจาก payload แล้วยิง API ของธนาคารผู้ออกสลิป (เช่น KBank Slip Verification API, SCB Slip Verify) เพื่อขอข้อมูลธุรกรรมจริงกลับมาเทียบ. ถ้าธนาคารตอบกลับว่า "ไม่พบธุรกรรม" หรือจำนวนเงินไม่ตรง = สลิปปลอม.

**เหตุผลที่มี.** กันการปลอมสลิปด้วยการแก้ภาพ — ภาพสลิปปลอมทำได้ง่ายมาก (แค่ Photoshop) แต่ QR ปลอมไม่ได้เพราะข้อมูลถูก **validate ที่ฝั่ง server** ของธนาคารผู้ออกสลิป ไม่ใช่ในตัว QR เอง. ผู้ค้ารายย่อยที่รับโอน PromptPay ควรสแกน QR บนสลิปลูกค้าก่อนปล่อยของ ไม่ใช่ดูแค่ภาพ.

**Known gap.** `validate.py` / `validate.ts` ในสกิลนี้ **ไม่** parse slip QR — รองรับเฉพาะการ *สร้าง* PromptPay payment payload เท่านั้น. ถ้าต้องการ parse/verify สลิปจริง ใช้ไลบรารีเฉพาะทาง (เช่น `slipverify`, `thanakan`) ที่เรียก API ธนาคารผู้ออกสลิปได้.

## Common mistakes
- **Hardcoded fake fixtures.** Don't paste a random 13-digit string and assume it passes. Build fixtures by computing the check digit from a 12-digit prefix.
- **Forgetting the `% 10` step.** When `total % 11 == 0`, `11 - 0 = 11`. Mod 10 yields `1`, not `11`.
- **PromptPay CRC scope.** The CRC is computed over the **entire** payload up to and including the literal `"6304"` tag+length, **not** just the body before tag 63.
- **Phone digit count.** Bangkok landlines are 9 digits (incl. leading 0); mobiles are 10. If you assume 10 always you'll mis-validate landlines.
- **Tax ID vs corporate ID.** Individual tax ID == citizen ID checksum. Juristic-person (company) tax IDs are a different 13-digit allocation but use the **same** checksum, so the same function validates both.
- **Trusting the first digit as proof of nationality.** หลักแรก = 1–5 บ่งบอกว่า *ระบบทะเบียน* จัดเป็นสัญชาติไทย ณ เวลาออกเลข — ไม่ใช่หลักฐานสัญชาติปัจจุบัน. ตรวจกับเอกสารจริง (บัตรประชาชน, ทะเบียนบ้าน) เสมอ. และอย่าใช้หลักแรกเป็นเงื่อนไขกรองผู้สมัคร — ผิดเจตนาและอาจเข้าข่ายเลือกปฏิบัติ.
- **Accepting a slip JPG as payment proof without QR verification.** ภาพสลิปปลอมง่ายมาก. ถ้ารับโอนเงินจริงจัง ต้องสแกน QR บนสลิปแล้วให้แอปธนาคาร verify กับ server ของธนาคารผู้ออก — อย่าเชื่อแค่ตัวเลขในรูป.
