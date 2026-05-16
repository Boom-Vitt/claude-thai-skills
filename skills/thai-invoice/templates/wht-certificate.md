# หนังสือรับรองการหักภาษี ณ ที่จ่าย
# Certificate of Withholding Tax

**ฉบับที่ / Sheet No.:**
[ ] 1. สำหรับผู้ถูกหักภาษี ณ ที่จ่าย ใช้แนบพร้อมกับแบบแสดงรายการภาษี (For payee to attach to tax return)
[ ] 2. สำหรับผู้ถูกหักภาษี ณ ที่จ่าย เก็บไว้เป็นหลักฐาน (For payee's records)

**ประเภทแบบยื่นภาษี / WHT Form Type:**
- [ ] **ภ.ง.ด.1ก** (เงินเดือน ค่าจ้าง — Salary)
- [ ] **ภ.ง.ด.2** (ดอกเบี้ย เงินปันผล — Interest, Dividends)
- [ ] **ภ.ง.ด.3** (บุคคลธรรมดา — Individual payee)
- [ ] **ภ.ง.ด.53** (นิติบุคคล — Juristic person payee)

**เลขที่ / Certificate No.:** {{cert_no}}

---

## ผู้มีหน้าที่หักภาษี ณ ที่จ่าย / Withholding Agent (Payer)
- **ชื่อ / Name:** {{payer_name}}
- **ที่อยู่ / Address:** {{payer_address}}
- **เลขประจำตัวผู้เสียภาษี / Tax ID (TIN):** {{payer_tin}}
- **สาขา / Branch:** {{payer_branch}}

## ผู้ถูกหักภาษี ณ ที่จ่าย / Payee
- **ชื่อ / Name:** {{payee_name}}
- **ที่อยู่ / Address:** {{payee_address}}
- **เลขประจำตัวผู้เสียภาษี / Tax ID (TIN):** {{payee_tin}}
- **สาขา / Branch:** {{payee_branch}}

---

## รายละเอียดการจ่ายเงิน / Payment Details

**เดือน / Tax Month:** {{tax_month}} **ปีภาษี / Tax Year:** {{tax_year}}

| ประเภทเงินได้พึงประเมินที่จ่าย (Category, ม.40 แห่งประมวลรัษฎากร) | วันที่จ่าย / Date Paid | จำนวนเงินที่จ่าย / Amount Paid (THB) | ภาษีที่หักและนำส่งไว้ / WHT Withheld (THB) |
|---|:--:|--:|--:|
| (1) เงินเดือน ค่าจ้าง เบี้ยเลี้ยง โบนัส ฯลฯ — Salary, wages, bonus (ม.40(1)) | {{m40_1_date}} | {{m40_1_amount}} | {{m40_1_wht}} |
| (2) ค่าธรรมเนียม ค่านายหน้า — Fees, commission (ม.40(2)) | {{m40_2_date}} | {{m40_2_amount}} | {{m40_2_wht}} |
| (3) ค่าแห่งกู๊ดวิลล์ ค่าลิขสิทธิ์ — Royalty, goodwill (ม.40(3)) | {{m40_3_date}} | {{m40_3_amount}} | {{m40_3_wht}} |
| (4) ดอกเบี้ย เงินปันผล — Interest, dividends (ม.40(4)) | {{m40_4_date}} | {{m40_4_amount}} | {{m40_4_wht}} |
| (5) ค่าเช่าทรัพย์สิน — Rent (ม.40(5)) — **5%** | {{m40_5_date}} | {{m40_5_amount}} | {{m40_5_wht}} |
| (6) ค่าวิชาชีพอิสระ — Professional fees (ม.40(6)) — **3%** | {{m40_6_date}} | {{m40_6_amount}} | {{m40_6_wht}} |
| (7) ค่ารับเหมา — Contractor (ม.40(7)) — **3%** | {{m40_7_date}} | {{m40_7_amount}} | {{m40_7_wht}} |
| (8) ค่าบริการอื่น ๆ — Other services (ม.40(8)) — **3%** | {{m40_8_date}} | {{m40_8_amount}} | {{m40_8_wht}} |
| (8.1) ค่าโฆษณา — Advertising — **2%** | {{adv_date}} | {{adv_amount}} | {{adv_wht}} |
| (8.2) ค่าขนส่ง — Transport — **1%** | {{transport_date}} | {{transport_amount}} | {{transport_wht}} |
| **รวม / Total** | | **{{total_amount}}** | **{{total_wht}}** |

**จำนวนเงินภาษีที่หักและนำส่งทั้งสิ้น (ตัวอักษร) / Total WHT in words:**
{{total_wht_in_words}} บาท

---

## เงื่อนไขการนำส่ง / Filing Notes
- ผู้จ่ายเงินต้องนำส่งภาษีให้กรมสรรพากรภายในวันที่ 7 ของเดือนถัดไป (วันที่ 15 หากยื่นออนไลน์)
- ผู้จ่ายเงินต้องออกหนังสือรับรองให้ผู้ถูกหักภาษีภายใน 7 วันนับจากวันที่นำส่งภาษี
- *Payer must remit WHT to the Revenue Department by the 7th of the following month (15th if filed online), and issue this certificate to the payee within 7 days of remittance.*

---

## ผู้จ่ายเงิน / Payer's Declaration

ขอรับรองว่ารายการที่กล่าวข้างต้นเป็นจริงและถูกต้อง
*I/We certify that the above particulars are true and correct.*

| ลงชื่อ / Signature: ____________________________ |
|---|
| ชื่อ / Name: {{payer_signatory_name}} |
| ตำแหน่ง / Position: {{payer_signatory_position}} |
| วันที่ / Date: ______ / ______ / ______ |
| (ประทับตรา / Company seal) |

---

> **สำหรับผู้ถูกหักภาษีนำไปใช้เป็นหลักฐาน**
> *For the payee to use as evidence of tax withheld.*
