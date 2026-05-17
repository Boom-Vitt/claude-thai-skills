<!--
ขอบคุณที่เปิด PR. กรอกส่วนด้านล่างเท่าที่เกี่ยวข้องกับการเปลี่ยนแปลงของคุณ —
ลบหัวข้อที่ไม่ใช้ออกได้.

Thank you for opening a pull request. Fill in the sections that apply to your
change and delete the headings that do not. Bilingual notes are welcome.
-->

## สรุปการเปลี่ยนแปลง / Summary

<!-- 1-3 ประโยค: เปลี่ยนอะไร และเปลี่ยนเพราะอะไร. หลีกเลี่ยงการลอกข้อความจาก diff. -->
<!-- 1-3 sentences: what changed and why. Avoid restating the diff. -->

## ประเภท / Type of change

<!-- ใส่ x ใน [x] ที่ตรง / Tick the box(es) that apply -->

- [ ] New skill (เพิ่ม skill ใหม่ใน `skills/`)
- [ ] Bug fix in skill code (Python หรือ TypeScript)
- [ ] Content update to an existing skill's `SKILL.md` or templates
- [ ] Legal / regulatory content update (PDPA, Revenue Code, ระเบียบสารบรรณ)
- [ ] Infrastructure (CI, scripts, validator, install)
- [ ] Documentation only (README, CONTRIBUTING, SECURITY, CHANGELOG, AGENTS)
- [ ] Other (please describe):

## Checklist

- [ ] รัน `./scripts/test-all.sh` ในเครื่องและผ่านทุก case / I ran `./scripts/test-all.sh` locally and every case passes.
- [ ] ถ้าเพิ่ม skill ใหม่ — ผ่าน `python3 scripts/validate-skills.py` / If adding a skill, `python3 scripts/validate-skills.py` accepts it.
- [ ] ถ้าเพิ่ม self-test ใหม่ — ลงทะเบียนแล้วใน `scripts/test-all.sh` / If adding a test file, I registered it in `scripts/test-all.sh`.
- [ ] ไม่ได้คอมมิตข้อมูลส่วนตัวจริง (เลขบัตรประชาชน, เบอร์, ที่อยู่, ชื่อบริษัท) — fixture ทั้งหมดเป็น synthetic / I did not commit real personal data; all fixtures are synthetic.
- [ ] ถ้าแก้เนื้อหากฎหมาย — ใส่ลิงก์อ้างอิงต้นทาง (ราชกิจจานุเบกษา, ประกาศกรม, PDPC) ในส่วน "Citations" ด้านล่าง / For legal content edits, I added primary-source citations in the "Citations" section below.
- [ ] อ่าน [CONTRIBUTING.md](../CONTRIBUTING.md) แล้ว / I have read [CONTRIBUTING.md](../CONTRIBUTING.md).

## Citations (สำหรับเนื้อหากฎหมาย / for legal-content changes)

<!--
ใส่ลิงก์/อ้างอิงประกาศที่ใช้ในการเขียน. ใส่วันที่ของประกาศและ section/มาตราที่อ้าง.
ตัวอย่าง:
- ประมวลรัษฎากร มาตรา 86/4 — กรมสรรพากร, ปรับปรุงล่าสุดเดือน xxxx
- ประกาศ PDPC ที่ X/2566 — ราชกิจจานุเบกษา, ออกวันที่ xxxx, https://...
-->

## วิธีทดสอบ / How to test this change

<!--
ขั้นตอนที่ reviewer ทำตามแล้วจะเห็นว่า PR นี้ทำงานถูก.
Steps the reviewer can follow to verify the change works.
-->

```bash
# ตัวอย่าง / example
./scripts/test-all.sh
python3 scripts/validate-skills.py
```

## หมายเหตุเพิ่มเติม / Additional notes

<!--
อะไรที่ reviewer ควรรู้ — trade-off, follow-up ที่ตั้งใจไม่ทำใน PR นี้, ความเสี่ยงที่รู้ตัวดี.
Anything the reviewer should know: trade-offs, intentional follow-ups, known risks.
-->
