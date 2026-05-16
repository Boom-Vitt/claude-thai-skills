# ใบกำกับภาษี / Tax Invoice

**[ ] ต้นฉบับ (Original)    [ ] สำเนา (Copy)**

---

## ผู้ขาย / Seller
- **ชื่อบริษัท / Company name:** {{seller_name}}
- **ที่อยู่ / Address:** {{seller_address}}
- **เลขประจำตัวผู้เสียภาษี / Tax ID (TIN):** {{seller_tin}}
- **สาขา / Branch:** {{seller_branch}} (สำนักงานใหญ่ / Head Office หรือ สาขาที่ ____)
- **โทรศัพท์ / Tel:** {{seller_phone}}
- **อีเมล / Email:** {{seller_email}}

## ผู้ซื้อ / Buyer
- **ชื่อ / Name:** {{buyer_name}}
- **ที่อยู่ / Address:** {{buyer_address}}
- **เลขประจำตัวผู้เสียภาษี / Tax ID (TIN):** {{buyer_tin}}
- **สาขา / Branch:** {{buyer_branch}}
- **ผู้ติดต่อ / Contact:** {{buyer_contact}}

## ข้อมูลเอกสาร / Document Info
| ฟิลด์ / Field | ค่า / Value |
|---|---|
| เล่มที่ / Book No. | {{book_no}} |
| เลขที่ / Invoice No. | {{invoice_no}} |
| วันที่ออก / Issue Date | {{issue_date}} |
| อ้างอิงใบสั่งซื้อ / PO Ref. | {{po_ref}} |
| เงื่อนไขการชำระเงิน / Payment Terms | {{payment_terms}} |

---

## รายการสินค้า/บริการ / Line Items

| ลำดับ / No. | รายการ / Description | จำนวน / Qty | หน่วย / Unit | ราคา/หน่วย / Unit Price (THB) | มูลค่า / Amount (THB) |
|:--:|---|:--:|:--:|--:|--:|
| 1 | {{item_1_desc}} | {{item_1_qty}} | {{item_1_unit}} | {{item_1_unit_price}} | {{item_1_amount}} |
| 2 | {{item_2_desc}} | {{item_2_qty}} | {{item_2_unit}} | {{item_2_unit_price}} | {{item_2_amount}} |
| 3 | {{item_3_desc}} | {{item_3_qty}} | {{item_3_unit}} | {{item_3_unit_price}} | {{item_3_amount}} |

---

## สรุปยอด / Summary

| | THB |
|---|--:|
| **รวมเป็นเงิน / Subtotal** | {{subtotal}} |
| **ส่วนลด / Discount** | {{discount}} |
| **มูลค่าก่อนภาษี / Amount before VAT** | {{amount_before_vat}} |
| **ภาษีมูลค่าเพิ่ม 7% / VAT 7%** | {{vat_amount}} |
| **จำนวนเงินรวมทั้งสิ้น / Grand Total** | **{{grand_total}}** |

**จำนวนเงิน (ตัวอักษร) / Amount in words:** {{amount_in_words}}

> ภาษีมูลค่าเพิ่มแสดงแยกตามมาตรา 86/4 แห่งประมวลรัษฎากร
> VAT shown separately as required by Revenue Code §86/4.

---

## หมายเหตุ / Remarks
{{remarks}}

---

## ลงนาม / Signatures

| ผู้รับสินค้า / Received by | ผู้มีอำนาจลงนาม / Authorized Signatory |
|---|---|
| ลายเซ็น: ____________________ | ลายเซ็น: ____________________ |
| ชื่อ: {{receiver_name}} | ชื่อ: {{authorized_name}} |
| วันที่: ______ / ______ / ______ | วันที่: ______ / ______ / ______ |
| | (ตำแหน่ง / Position: {{authorized_position}}) |
| | (ประทับตราบริษัท / Company seal) |

---

*เอกสารนี้ออกตามประมวลรัษฎากร มาตรา 86/4 — This document is issued under Revenue Code §86/4.*
