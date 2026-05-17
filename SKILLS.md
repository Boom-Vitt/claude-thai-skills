# Skills Catalog — ภาพรวม + วิธีติดตั้งทีละตัว

ทั้ง 12 skills ในรีโปนี้สามารถติดตั้งทีละตัวได้ — ไม่จำเป็นต้องเอาทั้งชุด.

> [!TIP]
> ถ้าต้องการแค่ตัวเดียว ใช้ `./install.sh thai-X` เร็วที่สุด.
> ถ้าต้องการทั้งชุด ใช้ `/plugin install claude-thai-skills` (Claude Code plugin marketplace).

---

## Categories — เลือกตามหมวด

| หมวด | Skills |
|---|---|
| ✍️ การเขียน & การสื่อสาร | thai-translate, thai-social-caption, thai-customer-service |
| 🏛 เอกสารทางการ | thai-resume, thai-government-form, thai-festival-card |
| 🧾 บัญชี & กฎหมาย | thai-invoice, thai-pdpa |
| 🔢 ข้อมูล & ฟอร์แมต | thai-date-format, thai-id-validate, thai-address, thai-text-processing |

---

## 1. thai-invoice — ใบกำกับภาษี / WHT (Thai tax invoice & withholding)
**ใช้เมื่อ:** ออกใบกำกับภาษี (Revenue Code §86/4), ใบเสร็จ, ใบเสนอราคา, ใบลดหนี้/เพิ่มหนี้, ภ.ง.ด.3/53, คำนวณ VAT 7% / WHT ด้วย `Decimal`
**Install:**
```bash
./install.sh thai-invoice                   # script
cp -r skills/thai-invoice ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `ออกใบกำกับภาษี ค่าบริการ design 30,000 บาท ลูกค้า บริษัท X จำกัด`

---

## 2. thai-date-format — แปลง พ.ศ. ↔ ค.ศ. (Thai date format / BE↔CE)
**ใช้เมื่อ:** แปลง พ.ศ. ↔ ค.ศ. (`BE = CE + 543`), จัดรูปแบบวันที่ราชการ/business/casual, parse ชื่อเดือนเต็ม/ย่อ (มกราคม / ม.ค.), สลับเลขอารบิก ↔ เลขไทย ๐๑๒๓
**Install:**
```bash
./install.sh thai-date-format                   # script
cp -r skills/thai-date-format ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `แปลงปี 2568 เป็น ค.ศ. และเขียนวันที่ 16 พ.ค. แบบราชการให้ที`

---

## 3. thai-customer-service — ตอบลูกค้า LINE OA / Shopee / Lazada
**ใช้เมื่อ:** reply LINE OA, Facebook Page, IG DM, Shopee, Lazada, TikTok Shop, เขียน apology / refund / return, auto-reply, de-escalate ลูกค้าโมโห
**Install:**
```bash
./install.sh thai-customer-service                   # script
cp -r skills/thai-customer-service ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `reply ลูกค้า LINE OA ที่บ่นว่าของเสีย ขอเงินคืน`

---

## 4. thai-id-validate — เลขบัตร ปชช. / เบอร์โทร / PromptPay QR
**ใช้เมื่อ:** ตรวจ checksum เลขบัตร 13 หลัก (citizen ID / tax ID), normalize เบอร์ระหว่าง `+66` กับ `0X`, สร้าง PromptPay QR payload (EMVCo TLV) ที่ scan ผ่านจริง
**Install:**
```bash
./install.sh thai-id-validate                   # script
cp -r skills/thai-id-validate ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `ตรวจเลขบัตรประชาชน 9999999999994 ว่า checksum ผ่านไหม`

---

## 5. thai-translate — แปล EN ⇄ TH รักษา register
**ใช้เมื่อ:** แปลเอกสาร/อีเมล/โพสต์/บทความ EN ⇄ TH, เลือกสรรพนาม "I/you" ตาม context (`พี่/น้อง/ท่าน/คุณ`), ตัดสินใจทับศัพท์ vs เก็บอังกฤษ, แก้คำแปลที่ "อ่านแล้วรู้ว่าแปลมา"
**Install:**
```bash
./install.sh thai-translate                   # script
cp -r skills/thai-translate ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `ช่วยแปลอีเมลภาษาอังกฤษนี้เป็นไทยให้สุภาพแบบส่งหาลูกค้า`

---

## 6. thai-government-form — หนังสือราชการตามระเบียบสารบรรณ 2526
**ใช้เมื่อ:** เขียนหนังสือราชการ (ภายนอก/ภายใน), คำร้อง, ใบลา, หนังสือมอบอำนาจ, เลือกคำขึ้นต้น (`เรียน` / `กราบเรียน` / `กราบบังคมทูล`) ตามยศ/ตำแหน่งผู้รับ
**Install:**
```bash
./install.sh thai-government-form                   # script
cp -r skills/thai-government-form ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `เขียนหนังสือลาป่วยถึงผู้อำนวยการ 3 วัน เพราะไข้หวัดใหญ่`

---

## 7. thai-pdpa — privacy notice / consent banner (PDPA 2562)
**ใช้เมื่อ:** ร่าง privacy notice, cookie/consent banner ที่ผ่าน PDPA, หนังสือแจ้งสิทธิ์เจ้าของข้อมูล, แจ้งเหตุละเมิดข้อมูลภายใน 72 ชม., audit template ที่แปลมาจาก GDPR
**Install:**
```bash
./install.sh thai-pdpa                   # script
cp -r skills/thai-pdpa ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `เขียน privacy policy สำหรับเว็บขายของ ต้อง compliance PDPA`

---

## 8. thai-social-caption — แคปชั่น FB / IG / TikTok / Threads / X
**ใช้เมื่อ:** เขียนแคปชั่นโพสต์ลง FB, IG, TikTok, Threads, X, Pantip, LINE TL, รีวิวสินค้า/ร้าน/คาเฟ่, โพสต์ giveaway / โปรโมชั่น, เลือก hashtag ที่คนไทยใช้จริง
**Install:**
```bash
./install.sh thai-social-caption                   # script
cp -r skills/thai-social-caption ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `เขียนแคปชั่น TikTok โปรโมตคาเฟ่ใหม่ที่ทองหล่อ ราคา 120 บาท`

---

## 9. thai-resume — เรซูเม่ภาษาไทย / bilingual TH-EN
**ใช้เมื่อ:** เขียน/แก้/แปลเรซูเม่หรือ CV เป็นไทยหรือสองภาษา, สมัครงานในไทย (ราชการ / MNC / startup), เลือกระหว่าง พ.ศ./ค.ศ., รูปถ่าย/ไม่มี, คำนำหน้าชื่อ
**Install:**
```bash
./install.sh thai-resume                   # script
cp -r skills/thai-resume ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `เขียนเรซูเม่ภาษาไทยสองภาษา สมัคร software engineer ที่ SCB`

---

## 10. thai-address — แยกที่อยู่ไทย / รหัสไปรษณีย์ → จังหวัด
**ใช้เมื่อ:** parse ที่อยู่จากฟอร์ม / e-commerce / PDF, ตรวจรหัสไปรษณีย์ 5 หลัก, lookup จังหวัดจาก postcode, transliterate ที่อยู่ไทย → English สำหรับฉลากพัสดุระหว่างประเทศ
**Install:**
```bash
./install.sh thai-address                   # script
cp -r skills/thai-address ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `แยกที่อยู่นี้ให้หน่อย: 123/45 ซอยสุขุมวิท 21 ถนนสุขุมวิท แขวงคลองเตยเหนือ เขตวัฒนา กรุงเทพ 10110`

---

## 11. thai-festival-card — อวยพร / คำไว้อาลัย / การ์ดงานพิธี
**ใช้เมื่อ:** อวยพรปีใหม่ / สงกรานต์ / ลอยกระทง / ตรุษจีน / วันแม่ / วันพ่อ, คำไว้อาลัย, การ์ดแต่งงาน / ขึ้นบ้านใหม่ / รับปริญญา, ข้อความเกี่ยวกับสถาบันพระมหากษัตริย์ (รวม taboo เลข ๔ / สี / ของห้ามให้)
**Install:**
```bash
./install.sh thai-festival-card                   # script
cp -r skills/thai-festival-card ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `เขียนคำอวยพรปีใหม่ส่งหาเจ้านาย แบบทางการแต่ไม่แข็ง`

---

## 12. thai-text-processing — ตัดคำ / NFC / collation / romanization
**ใช้เมื่อ:** ตัดคำ (segmentation) สำหรับ search/autocomplete, NFC normalization ก่อนเก็บ DB, จัดเรียงชื่อไทยให้ถูก, romanize RTGS สำหรับ slug, ตั้ง full-text index (ES/Postgres/MySQL), เลือก lib (PyThaiNLP vs ICU vs nlpO3)
**Install:**
```bash
./install.sh thai-text-processing                   # script
cp -r skills/thai-text-processing ~/.claude/skills/ # manual
```
**ลองพิมพ์:** `ตัดคำประโยค "ฉันรักการเขียนโค้ดภาษาไทยมาก" ด้วย PyThaiNLP`

---

## ต้องการครบทุก skill?

```bash
./install.sh                          # ครบ 12 ตัว
# หรือ
/plugin install claude-thai-skills    # ผ่าน Claude Code marketplace
```
