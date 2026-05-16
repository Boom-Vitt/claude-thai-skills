# Claude Thai Skills · ทักษะ Claude Code สำหรับคนไทย

> 12 skills ภาษาไทยพร้อมใช้ — แปล, แคปชั่นโซเชียล, เรซูเม่, จดหมายราชการ, PDPA, ใบกำกับภาษี, PromptPay, เลขบัตรประชาชน, วันที่ พ.ศ., ที่อยู่ไทย, ตอบลูกค้า, ตัดคำภาษาไทย.
>
> 12 production-ready Claude Code skills for Thai users — translation, social captions, resumes, government letters, PDPA, tax invoices, PromptPay, Thai national ID, BE dates, Thai addresses, customer-service replies, Thai NLP.

## ติดตั้ง / Install

**วิธีที่ 1 — ผ่าน Claude Code plugin marketplace (แนะนำ / recommended):**

```
/plugin marketplace add Boom-Vitt/claude-thai-skills
/plugin install claude-thai-skills
```

**วิธีที่ 2 — ติดตั้งทั้งหมดด้วยสคริปต์ (clone แล้วรัน):**

```bash
git clone https://github.com/Boom-Vitt/claude-thai-skills.git
cd claude-thai-skills
./install.sh                  # ติดตั้งทุก skill
./install.sh thai-resume      # ติดตั้งเฉพาะตัวที่ต้องการ
```

**วิธีที่ 3 — คัดลอกเฉพาะ skill ที่ต้องการ:**

```bash
cp -r skills/thai-resume ~/.claude/skills/
```

หลังติดตั้ง: เปิด session ใหม่ของ Claude Code แล้วลองพิมพ์ตัวอย่างด้านล่าง ✨

---

## ทำไมต้องมี skills ภาษาไทย? / Why Thai-specific skills?

Claude เก่งภาษาไทยอยู่แล้ว แต่ยังพลาดเรื่องเฉพาะของไทยได้บ่อย — เช่น:

- 🗓 ฟอร์แมตวันที่สลับ พ.ศ./ค.ศ. หรือใช้ชื่อเดือนผิด
- ✉️ ขึ้นต้นจดหมายราชการด้วย "เรียน" แทน "กราบเรียน" กับบุคคลที่ต้องใช้
- 🧾 ออกใบกำกับภาษีโดยลืมแยก VAT 7% ตามมาตรา 86/4
- 📱 เขียนแคปชั่น TikTok ภาษาไทยเหมือนแปลจาก Google
- 🔐 ใช้ template GDPR แทน PDPA (ผิด — ห้าม pre-check, ต้อง opt-in)
- 🆔 ตรวจเลขบัตรประชาชนด้วย regex 13 หลักเฉยๆ (ไม่ได้เช็ค checksum)
- 🏛 แปล "you" เป็น "คุณ" หมดทุกที่ (ควรเป็น พี่/น้อง/ท่าน ตาม context)

ทุก skill ในรีโปนี้ถูกออกแบบมาแก้ปัญหาเฉพาะเหล่านี้ — concrete, copy-pasteable, ใช้ได้ทันที.

---

## Skills ที่มี / Available skills

### ✍️ การเขียน & การสื่อสาร / Writing & Communication

- **[thai-translate](skills/thai-translate)** — แปล EN ⇄ TH โดยรักษา register, สรรพนาม, idioms / EN ⇄ TH translation with register-aware pronouns and idiom matching.
- **[thai-social-caption](skills/thai-social-caption)** — แคปชั่น Facebook, TikTok, IG, Threads, X, Pantip / Captions for Thai audience on Facebook, TikTok, IG, Threads, X, Pantip.
- **[thai-customer-service](skills/thai-customer-service)** — ตอบลูกค้า LINE OA, Shopee, Lazada, IG DM, TikTok Shop / Customer-service replies for LINE OA, Shopee, Lazada, IG DM, TikTok Shop.

### 🏛 เอกสารทางการ / Formal Documents

- **[thai-resume](skills/thai-resume)** — เรซูเม่ภาษาไทย + bilingual (JobsDB, JobThai, LinkedIn TH) / Thai resume and TH/EN bilingual CV for JobsDB, JobThai, LinkedIn TH.
- **[thai-government-form](skills/thai-government-form)** — หนังสือราชการ, คำร้อง, ใบลา, หนังสือมอบอำนาจ / Official Thai government letters, petitions, leave requests, POA.
- **[thai-festival-card](skills/thai-festival-card)** — อวยพรปีใหม่, สงกรานต์, ลอยกระทง, แต่งงาน, ไว้อาลัย / Festival greetings, royal occasions, weddings, condolences.

### 🧾 บัญชี & กฎหมาย / Accounting & Legal

- **[thai-invoice](skills/thai-invoice)** — ใบกำกับภาษี, ใบเสร็จ, ใบเสนอราคา, ภ.ง.ด.3/53 / Tax invoices, receipts, quotations, WHT certificates (Revenue Code §86/4).
- **[thai-pdpa](skills/thai-pdpa)** — Privacy notice, consent banner, breach notification ตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล / PDPA-compliant privacy notice, consent banner, breach notification.

### 🔢 ข้อมูลและฟอร์แมต / Data & Format

- **[thai-id-validate](skills/thai-id-validate)** — เช็คเลขบัตร ปชช. 13 หลัก, เบอร์โทรไทย, PromptPay QR / Thai national ID checksum, phone normalization, PromptPay QR payload.
- **[thai-date-format](skills/thai-date-format)** — แปลง พ.ศ. ↔ ค.ศ., ชื่อเดือนไทย, เลขไทย ๐๑๒๓ / BE ↔ CE conversion, Thai month names, Thai numerals.
- **[thai-address](skills/thai-address)** — แยกที่อยู่ไทย, รหัสไปรษณีย์ → จังหวัด / Thai postal address parsing, postcode lookup, 77-province table.
- **[thai-text-processing](skills/thai-text-processing)** — ตัดคำภาษาไทย, NFC normalize, Thai sort, romanize / Thai word segmentation, Unicode normalization, sorting, romanization.

---

## ตัวอย่างการใช้งาน / Example prompts

หลังติดตั้งแล้ว ลองพิมพ์ใน Claude Code:

```
"ช่วยเขียนแคปชั่น TikTok โปรโมตคาเฟ่ใหม่ที่ทองหล่อ ราคา ๑๒๐ บาท"
"แปลงเลข ๒๕๖๘ เป็น ค.ศ. และเขียนวันที่ ๑๖ พ.ค. แบบราชการ"
"ออกใบกำกับภาษี ค่าบริการ design 30,000 บาท ลูกค้า บริษัท X จำกัด"
"เขียนหนังสือลาป่วยถึงผู้อำนวยการ 3 วัน เพราะไข้หวัดใหญ่"
"ตรวจเลขบัตรประชาชน 9999999999994 ว่า checksum ผ่านไหม (เลขทดสอบ ไม่ใช่ของจริง)"
"เขียน privacy policy สำหรับเว็บขายของ ต้อง compliance PDPA"
"ตัดคำประโยค 'ฉันรักการเขียนโค้ดภาษาไทยมาก' ด้วย PyThaiNLP"
"reply ลูกค้า LINE OA ที่บ่นว่าของเสีย ขอเงินคืน"
```

Claude จะเลือก skill ที่เหมาะสมให้อัตโนมัติ — ไม่ต้องระบุชื่อ skill เอง.

---

## โครงสร้างไฟล์ / Repo layout

```
claude-thai-skills/
├── .claude-plugin/
│   ├── plugin.json          # Plugin metadata
│   └── marketplace.json     # Marketplace listing
├── skills/
│   ├── thai-translate/SKILL.md
│   ├── thai-resume/
│   │   ├── SKILL.md
│   │   └── template-bilingual.md
│   ├── thai-id-validate/
│   │   ├── SKILL.md
│   │   ├── validate.py      # Working checksum
│   │   └── validate.ts
│   └── ... (12 skills total)
├── docs/
│   ├── my-setup-th.md       # ทัวร์ config ส่วนตัว (sanitized)
│   └── recommended-mcp.md   # MCP servers ที่แนะนำ
├── install.sh
├── LICENSE                  # MIT
└── README.md
```

---

## คุณภาพ / Quality

| Tier | Skills | สถานะ |
|---|---|---|
| **Validator (มี code)** | `thai-id-validate`, `thai-date-format`, `thai-address`, `thai-invoice` | Python + TypeScript พร้อม self-test ที่ผ่านทั้งหมด |
| **Prose / Reference** | อีก 8 skills | v0.1 — ครบเนื้อหา, ยังไม่ผ่าน adversarial testing |

PR ที่ช่วย harden ด้วย test scenario เพิ่มเติม ยินดีต้อนรับ ✨

> 🛡 **ความปลอดภัยของข้อมูล:** ตัวอย่างทุกอย่างในรีโปนี้ (เลขบัตรประชาชน, เบอร์โทร, ที่อยู่, ชื่อบริษัท) เป็น **synthetic test fixtures** — ไม่ตรงกับบุคคล/องค์กรจริง. Test ID ทั้งหมดสร้างขึ้นใหม่เพื่อให้ checksum ผ่าน, ไม่ใช่ ID ที่ออกโดยกรมการปกครอง.
>
> **Privacy notice:** All examples in this repo (national IDs, phone numbers, addresses, company names) are **synthetic test fixtures** — they do not correspond to real people or organizations. Test IDs are constructed to pass the checksum, not issued by DOPA.

## ปัญหาที่รู้แล้ว / Known issues (v0.1)

- `thai-address/parse.py` แยกชื่อถนนแบบคำเดียวเท่านั้น — ถ้าเป็นถนนหลายคำ (เช่น "พระราม 9") อาจตัดเฉพาะคำแรก. PR แก้ regex ยินดีต้อนรับ.
- `thai-pdpa` SKILL.md อ้างอิงเลขมาตราของ พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 ตามฉบับล่าสุดที่ maintainer ตรวจสอบ. ถ้ามีประกาศ PDPC ใหม่ที่กระทบ เปิด issue แจ้งได้
- `thai-invoice` อัตรา WHT และ VAT 7% อิงตามอัตราปัจจุบัน — ถ้ารัฐบาลเปลี่ยน rate (เช่น VAT กลับเป็น 10%) ต้องอัปเดต `calc.py` และ template
- Prose skills (8 ตัว) ยังไม่ได้ผ่าน adversarial test scenarios ตามแนวทาง `superpowers:writing-skills`. ใครอยากช่วย harden เปิด PR ได้

---

## ร่วมพัฒนา / Contributing

ภาษาที่ใช้: เขียน issue/PR ได้ทั้งภาษาไทยและภาษาอังกฤษ

1. Fork → branch ใหม่ → commit → PR
2. ถ้าจะเพิ่ม skill ใหม่: อ่าน skill อื่นเป็น reference ก่อน, ตั้งชื่อ `thai-<topic>`, frontmatter ใส่ trigger ภาษาไทยในเครื่องหมายคำพูด
3. ถ้าเจอเนื้อหาผิด (โดยเฉพาะส่วน legal/PDPA/Revenue Code): เปิด issue พร้อมแหล่งอ้างอิง — เนื้อหา legal เปลี่ยนได้ตาม พ.ร.บ. ใหม่ๆ

---

## License

[MIT](LICENSE) — ใช้ฟรี, แก้ฟรี, แจกฟรี

---

## ขอบคุณ / Credits

- ได้รับแรงบันดาลใจจาก [mattpocock/skills](https://github.com/mattpocock/skills), [obra/superpowers](https://github.com/obra/superpowers), [anthropics/skills](https://github.com/anthropics/skills)
- ทักษะหลายตัวอ้างอิงจาก [PyThaiNLP](https://github.com/PyThaiNLP/pythainlp), [Revenue Department Thailand](https://www.rd.go.th/), [PDPC Thailand](https://www.pdpc.or.th/)
- Maintained by [@Boom-Vitt](https://github.com/Boom-Vitt) · vittawat.soo@boombignose.org
