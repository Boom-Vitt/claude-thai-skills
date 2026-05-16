---
name: thai-invoice
description: Use this skill for any task involving Thai tax invoices, receipts, quotations, or withholding-tax certificates. Trigger whenever the user asks to: draft a Thai tax invoice (ใบกำกับภาษี), receipt (ใบเสร็จ), quotation (ใบเสนอราคา), credit/debit note (ใบลดหนี้/ใบเพิ่มหนี้), or WHT certificate (ภ.ง.ด.3/53). Also trigger for requests like "ออกใบกำกับภาษี", "ใบเสร็จ", "ใบเสนอราคา", "Thai tax invoice", "VAT 7%", "ภาษีหัก ณ ที่จ่าย", or any variation. If the context involves Thai accounting documents under Revenue Code §86/4, use this skill.
---

# Thai Tax Documents (ใบกำกับภาษี / ใบเสร็จ / ใบเสนอราคา / WHT)

## Overview
This skill drafts Thai tax invoices compliant with Revenue Code §86/4, plus quotations, receipts, credit/debit notes, and withholding-tax certificates (ภ.ง.ด.3/53). It applies the correct VAT 7% and WHT rates per category and matches Revenue Department wording. Use it whenever you need bookkeeping-grade Thai accounting documents — never improvise the legal phrasing or VAT/WHT math; pull from this skill.

## When to use
- ออกใบกำกับภาษีให้ลูกค้านิติบุคคล / individual buyers
- บันทึก ภ.ง.ด.3 (หัก ณ ที่จ่ายบุคคลธรรมดา) or ภ.ง.ด.53 (นิติบุคคล)
- เขียนใบเสนอราคา / ใบลดหนี้ / ใบเพิ่มหนี้
- Drafting English-Thai bilingual invoices for foreign buyers
- Calculating VAT-inclusive vs VAT-exclusive totals
- Computing withholding tax to deduct from a supplier payment

## Required fields — full tax invoice (Revenue Code §86/4)
A full ใบกำกับภาษี MUST contain all seven elements. Quote the Thai exactly:

1. คำว่า "ใบกำกับภาษี" ในที่ที่เห็นได้ชัดเจน
2. ชื่อ ที่อยู่ และเลขประจำตัวผู้เสียภาษีอากรของผู้ออก
3. ชื่อ ที่อยู่ ของผู้ซื้อ (+TIN ถ้ามี)
4. หมายเลขลำดับและเล่ม (ถ้ามี)
5. ชื่อ ชนิด ประเภท ปริมาณ และมูลค่าของสินค้า/บริการ
6. จำนวนภาษีมูลค่าเพิ่มที่คำนวณจากมูลค่าของสินค้าหรือบริการ แยกออกจากมูลค่าให้ชัดเจน
7. วัน เดือน ปี ที่ออกใบกำกับภาษี

Note: a short-form (อย่างย่อ) invoice can omit buyer TIN and address when issued by a retailer at the point of sale — but the seller must be approved by Revenue.

## VAT
- Standard rate: 7% (statutory rate 10%, reduced by Royal Decree — make rate a parameter; don't hardcode forever)
- VAT-exempt items (Sec 81): basic agricultural products, education, healthcare, books, public transport — DO NOT add VAT, and DO NOT issue ใบกำกับภาษี for these (use ใบส่งของ instead)
- Only VAT-registered sellers (ผู้ประกอบการจดทะเบียน VAT) may issue ใบกำกับภาษี

## Withholding tax (ภาษีหัก ณ ที่จ่าย)

| Service | Form | Rate (resident) |
|---|---|---|
| บริการทั่วไป (services) | ภ.ง.ด.3 / 53 | 3% |
| ค่าเช่าอสังหาริมทรัพย์ | ภ.ง.ด.3 / 53 | 5% |
| ค่าโฆษณา | ภ.ง.ด.3 / 53 | 2% |
| ค่าขนส่ง | ภ.ง.ด.3 / 53 | 1% |
| ค่าวิชาชีพอิสระ (lawyer, accountant, etc.) | ภ.ง.ด.3 | 3% |
| ดอกเบี้ย/เงินปันผล | ภ.ง.ด.2 | 10%/15% |

ภ.ง.ด.3 = WHT cert for individuals receiving payment. ภ.ง.ด.53 = WHT cert for juristic entities (บริษัท/ห้างหุ้นส่วน). WHT base = pre-VAT amount.

## Numbering, credit/debit notes, quotation
- Sequential invoice numbers required; reset annually optional (e.g. `INV-2026-0001`)
- ใบลดหนี้ (credit note): reference original invoice number, show reduction reason
- ใบเพิ่มหนี้ (debit note): same but for upward adjustment
- ใบเสนอราคา: not a tax document; include "ราคานี้ไม่รวมภาษีมูลค่าเพิ่ม" or "ราคารวม VAT 7% แล้ว" clearly; specify validity period (ยืนราคา 30 วัน)
- Common payment terms: "ชำระเงินภายใน 30 วันนับจากวันที่วางบิล" / "Net 30" / "เครดิตเทอม 45 วัน"
- Combined form "ใบเสร็จรับเงิน/ใบกำกับภาษี" is allowed for cash sales by VAT-registered sellers

## Common mistakes
1. Forgetting to separate VAT line ("ราคารวม 1,070 บาท (รวม VAT)") — Revenue Code requires showing VAT amount distinctly on a full tax invoice.
2. Using "ใบเสร็จ/ใบกำกับภาษี" combined form when seller is not VAT-registered — only VAT-registered sellers can issue ใบกำกับภาษี.
3. Issuing ใบกำกับภาษี for VAT-exempt goods (books, fresh agricultural products) — use ใบส่งของ/บิลเงินสด instead.
4. Wrong WHT rate (e.g., 3% on rent — should be 5%; 2% on advertising — frequently confused).
5. Not issuing WHT certificate to payee within 7 days of submitting ภ.ง.ด.3/53.
6. Missing TIN on buyer side for B2B — Revenue may reject input-VAT claim.
7. Bilingual invoices that translate "Tax Invoice" but omit the Thai "ใบกำกับภาษี" — Thai law requires the Thai phrase explicitly.
8. Computing WHT on the VAT-inclusive amount — base must be pre-VAT.

## Templates
See:
- `templates/tax-invoice-full.md` — full ใบกำกับภาษี (Tax Invoice)
- `templates/quotation.md` — ใบเสนอราคา (Quotation)
- `templates/wht-certificate.md` — หนังสือรับรองการหักภาษี ณ ที่จ่าย (ภ.ง.ด.3/53)

## Calculator
`calc.py` — Decimal-based helpers:
- `calculate_vat(subtotal, rate=Decimal("0.07"))` → `{subtotal, vat, total}`
- `calculate_vat_inclusive(total, rate=Decimal("0.07"))` → backs out VAT from a VAT-inclusive total
- `calculate_wht(amount, rate)` → `{amount, wht, net_payable}`
- `WHT_RATES` constant for the common categories
- Run `python calc.py` for a self-test
