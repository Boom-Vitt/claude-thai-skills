# ใบเสนอราคา / Quotation

**เลขที่ / Quotation No.:** {{quotation_no}}
**วันที่ / Date:** {{issue_date}}
**ยืนราคาถึง / Valid Until:** {{valid_until}} (ภายใน {{validity_days}} วัน)

---

## ผู้เสนอราคา / From (Seller)
- **ชื่อบริษัท / Company name:** {{seller_name}}
- **ที่อยู่ / Address:** {{seller_address}}
- **เลขประจำตัวผู้เสียภาษี / Tax ID (TIN):** {{seller_tin}}
- **โทรศัพท์ / Tel:** {{seller_phone}}
- **อีเมล / Email:** {{seller_email}}
- **ผู้ติดต่อ / Sales Contact:** {{seller_contact}}

## ลูกค้า / To (Buyer)
- **ชื่อ / Name:** {{buyer_name}}
- **ที่อยู่ / Address:** {{buyer_address}}
- **เลขประจำตัวผู้เสียภาษี / Tax ID (TIN):** {{buyer_tin}}
- **ผู้ติดต่อ / Attention:** {{buyer_contact}}
- **อ้างอิง / Reference (RFQ):** {{rfq_ref}}

---

## รายการสินค้า/บริการที่เสนอ / Quoted Items

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
| **ส่วนลด / Discount ({{discount_pct}}%)** | {{discount}} |
| **มูลค่าก่อนภาษี / Amount before VAT** | {{amount_before_vat}} |
| **ภาษีมูลค่าเพิ่ม 7% / VAT 7%** | {{vat_amount}} |
| **ราคารวมทั้งสิ้น / Grand Total** | **{{grand_total}}** |

**จำนวนเงิน (ตัวอักษร) / Amount in words:** {{amount_in_words}}

---

## เงื่อนไขและข้อตกลง / Terms & Conditions

- **VAT:** [ ] ราคานี้รวมภาษีมูลค่าเพิ่ม 7% แล้ว / Price includes VAT 7%
         [ ] ราคานี้ยังไม่รวมภาษีมูลค่าเพิ่ม 7% / Price excludes VAT 7%
- **เงื่อนไขการชำระเงิน / Payment Terms:** {{payment_terms}}
  ตัวอย่าง: "ชำระเงินภายใน 30 วันนับจากวันที่วางบิล" / "เครดิตเทอม 45 วัน" / "Net 30"
- **กำหนดส่งมอบ / Delivery:** {{delivery_terms}}
- **การรับประกัน / Warranty:** {{warranty_terms}}
- **การยืนราคา / Price Validity:** ราคายืนภายใน {{validity_days}} วันนับจากวันที่ออกใบเสนอราคา
- **หมายเหตุ / Remarks:** {{remarks}}

> *ใบเสนอราคานี้ไม่ใช่ใบกำกับภาษี — ใบกำกับภาษีจะออกเมื่อมีการส่งมอบสินค้า/บริการ*
> *This quotation is not a tax invoice — a tax invoice (ใบกำกับภาษี) will be issued upon delivery.*

---

## ลงนาม / Signatures

| ผู้เสนอราคา / Issued by | ผู้อนุมัติ / Approved by (Customer) |
|---|---|
| ลายเซ็น: ____________________ | ลายเซ็น: ____________________ |
| ชื่อ: {{issuer_name}} | ชื่อ: {{approver_name}} |
| ตำแหน่ง: {{issuer_position}} | ตำแหน่ง: {{approver_position}} |
| วันที่: ______ / ______ / ______ | วันที่: ______ / ______ / ______ |
| (ประทับตราบริษัท / Company seal) | |

---

*ขอบพระคุณที่ให้โอกาสเราเสนอราคา / Thank you for the opportunity to quote.*
