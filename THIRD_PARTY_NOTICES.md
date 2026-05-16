# Third-Party Notices
## ที่มาของแหล่งอ้างอิงและไลบรารีที่เกี่ยวข้อง

เอกสารฉบับนี้ระบุชื่อ ผู้สร้าง ใบอนุญาต และลักษณะการอ้างอิงของไลบรารี, สเปก, และเอกสารทางการที่ปรากฏใน skill ของรีโปนี้. ตัว `claude-thai-skills` เอง license แบบ MIT (ดู [LICENSE](LICENSE)) และไม่ได้นำโค้ดของบุคคลที่สามมาบรรจุไว้ในรีโป — รายการด้านล่างคือสิ่งที่ skill **ชี้ไปหา** หรือ **อ้างอิงเป็นที่มาทางเทคนิค**, ไม่ใช่สิ่งที่ vendor มาในรีโป.

> This document lists the libraries, specifications, and authoritative sources referenced by the skills in this repository. `claude-thai-skills` itself is MIT-licensed (see [LICENSE](LICENSE)) and does not vendor any third-party code. The entries below are upstream references or recommended pairings — they are not bundled.

---

## ไลบรารีที่ skill อ้างอิงให้ผู้ใช้ติดตั้งเอง / Libraries skills recommend the user install separately

### PyThaiNLP

* **Project**: https://github.com/PyThaiNLP/pythainlp
* **License**: Apache License 2.0
* **Used by**: `skills/thai-text-processing` — แนะนำ PyThaiNLP สำหรับ word segmentation, normalization, romanize (RTGS) และ Thai NLP ทั่วไป.
* **ลักษณะการใช้**: skill ระบุชื่อ function ของ PyThaiNLP เป็นตัวอย่าง (เช่น `pythainlp.tokenize.word_tokenize`) แต่ไม่ได้คัดลอกโค้ดมาในรีโป. ผู้ใช้ต้อง `pip install pythainlp` เอง.

### promptpay-qr (dtinth)

* **Project**: https://github.com/dtinth/promptpay-qr
* **License**: MIT License
* **Used by**: `skills/thai-id-validate` — ใช้เป็น reference สำหรับโครงสร้าง EMVCo TLV ของ PromptPay QR. โค้ดของ `validate.py` และ `validate.ts` ในรีโปนี้เขียนใหม่จากการอ่านสเปก EMVCo + การตรวจสอบ payload ด้วย QR scanner ของแอปธนาคารจริง ไม่ใช่การ port มาตรงๆ. การกล่าวถึง project นี้ใน comment คือเครดิตให้คนแรกที่ทำให้สเปกอ่านง่ายต่อ dev ไทย.

### Anthropic Agent Skills specification

* **Reference**: https://agentskills.io/specification
* **License**: Documentation copyright Anthropic.
* **Used by**: ทุก SKILL.md ในรีโป — โครงสร้าง frontmatter (`name`, `description`) และ semantic ที่ Claude Code ใช้ load skill มาจากสเปกฉบับนี้.

---

## ข้อมูลและสเปกของหน่วยงานรัฐไทย / Thai government data and specifications

Skill ที่อ้างอิงกฎหมาย, ระเบียบ, หรือสเปกจากหน่วยงานราชการไทย ใช้เอกสารต้นทางต่อไปนี้เป็นแหล่งความจริง. เอกสารพวกนี้เป็น public domain ในฐานะ official government works แต่การตีความเชิงปฏิบัติในรีโปนี้เป็นมุมมองของผู้เขียน ไม่ใช่ของหน่วยงานเจ้าของเอกสาร.

### กรมสรรพากร / Revenue Department of Thailand

* **Source**: https://www.rd.go.th/
* **Used by**: `skills/thai-invoice`
* **อ้างอิงอะไร**: ประมวลรัษฎากร มาตรา 86/4 (โครงสร้างใบกำกับภาษี), อัตรา VAT 7% ปัจจุบัน, อัตราภาษีหัก ณ ที่จ่าย (WHT) ตามแบบ ภ.ง.ด.3/53, แบบฟอร์มใบกำกับภาษี/ใบเสร็จ/ใบเสนอราคา.
* **Status**: เนื้อหาในรีโปคือ "human-readable distillation" ของระเบียบ ไม่ใช่ official authority. ตรวจกับประกาศล่าสุดของกรมก่อนใช้กับงานจริง.

### คณะกรรมการคุ้มครองข้อมูลส่วนบุคคล (PDPC)

* **Source**: https://www.pdpc.or.th/
* **Used by**: `skills/thai-pdpa`
* **อ้างอิงอะไร**: พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562, ประกาศ PDPC ที่ออกตามมาตราต่างๆ (consent, breach notification, DPO, cross-border transfer).
* **Status**: skill เขียนเป็นเครื่องมือร่าง ไม่ใช่คำปรึกษากฎหมาย. ดู [SECURITY.md](SECURITY.md) section "Legal and tax content disclaimer".

### สำนักนายกรัฐมนตรี — ระเบียบสำนักนายกรัฐมนตรีว่าด้วยงานสารบรรณ พ.ศ. 2526

* **Source**: ราชกิจจานุเบกษา (Royal Thai Government Gazette)
* **Used by**: `skills/thai-government-form`
* **อ้างอิงอะไร**: รูปแบบหนังสือราชการ (ภายนอก / ภายใน / ประทับตรา), คำขึ้นต้น/ลงท้ายตามชั้นยศ, โครงสร้างคำสั่ง/ประกาศ.

### กรมการปกครอง (DOPA)

* **Source**: https://www.dopa.go.th/
* **Used by**: `skills/thai-id-validate`
* **อ้างอิงอะไร**: position-weighted checksum สำหรับเลขประจำตัวประชาชน 13 หลัก. Algorithm สาธารณะ (ระบุในเอกสารของ DOPA และในวิชาการต่อเนื่องตั้งแต่ปี 1996), ไม่ใช่ trade secret.

### ITMX — National ITMX Co., Ltd.

* **Source**: https://www.itmx.co.th/
* **Used by**: `skills/thai-id-validate` (PromptPay payload)
* **อ้างอิงอะไร**: EMVCo Merchant Presented Mode QR Code Specification สำหรับ PromptPay (Application ID `A000000677010111` และ tag layout).

### Thailand Post / ไปรษณีย์ไทย

* **Source**: https://www.thailandpost.com/
* **Used by**: `skills/thai-address` (`provinces.json` postal-code prefix table)
* **อ้างอิงอะไร**: 5-digit postcode → จังหวัด, prefix mapping ของ 77 จังหวัด.
* **Status**: ข้อมูล postcode prefix เป็น public reference ที่หลายแหล่งเผยแพร่. ตาราง `provinces.json` ในรีโปสร้างจาก cross-reference ระหว่าง Thailand Post และ Wikipedia (CC BY-SA 4.0).

---

## แรงบันดาลใจ / Inspiration

Skill ในรีโปนี้ได้รับแรงบันดาลใจจากโครงสร้างและแนวคิดของรีโปต่อไปนี้. ไม่ได้คัดลอกโค้ดหรือเนื้อหามาตรงๆ แต่อยากเครดิตให้ชัด:

| Project | Author | License | สิ่งที่ได้แรงบันดาลใจ |
|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic | Apache 2.0 (skills) | โครงสร้าง `skills/<name>/SKILL.md`, ฟอร์แมต frontmatter, แนวคิด `template/` scaffold |
| [obra/superpowers](https://github.com/obra/superpowers) | Jesse Vincent (obra) | MIT | แนวการเขียน `AGENTS.md`, การ release-note ตามเวอร์ชัน, ระเบียบ contribution |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock | MIT | สไตล์ description ที่ระบุ "trigger when ..." อย่างชัดเจน, การใช้ em-dash ใน bullet |

---

## หากพบ attribution ที่ขาดหายไป / Reporting missing attribution

ถ้าคุณเป็นเจ้าของผลงานที่รีโปนี้ควรจะเครดิตให้แต่ยังไม่มีรายชื่อด้านบน, หรือเห็นว่ามีการอ้างอิงที่ไม่ถูกต้อง โปรดเปิด issue หรือ pull request เพื่อแก้ไข. เป้าหมายของเอกสารฉบับนี้คือให้เครดิตครบถ้วนและถูกต้อง — ไม่ใช่เอาผ่านไป.

If you maintain a project or document that this repository should credit but does not, or you find an inaccurate attribution above, please open an issue or pull request. The goal of this notice is complete and accurate attribution, not lip service.
