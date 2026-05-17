# Changelog

ทุกการเปลี่ยนแปลงที่สำคัญของรีโปนี้จะบันทึกในเอกสารนี้. รูปแบบอ้างอิงจาก [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) และเวอร์ชันใช้ [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> All notable changes to this repository are documented here. The format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) and versions follow [Semantic Versioning 2.0](https://semver.org/spec/v2.0.0.html). Entries are written in mixed Thai and English to match the audience of the project.

ประเภทของรายการ / Entry types:

* **Added** — ฟีเจอร์ใหม่ / new functionality
* **Changed** — การแก้ไขฟีเจอร์ที่มีอยู่ / change to existing behavior
* **Deprecated** — ฟีเจอร์ที่จะถูกถอดในเวอร์ชันถัดไป / soon-to-be-removed features
* **Removed** — ฟีเจอร์ที่ถูกถอดแล้ว / features removed in this release
* **Fixed** — แก้บั๊ก / bug fixes
* **Security** — patch ที่เกี่ยวกับช่องโหว่ / vulnerability fixes
* **Docs** — เปลี่ยนแปลงเฉพาะเอกสาร / documentation-only changes

---

## [Unreleased]

### Added

* `THIRD_PARTY_NOTICES.md` ระบุที่มาของไลบรารี (PyThaiNLP, promptpay-qr), สเปกของหน่วยงานราชการไทย (กรมสรรพากร, PDPC, สำนักนายกฯ, DOPA, ITMX, ไปรษณีย์ไทย), และรีโปแรงบันดาลใจ (anthropics/skills, obra/superpowers, mattpocock/skills).
* `CHANGELOG.md` (ไฟล์นี้) เริ่มบันทึก release notes ตาม Keep a Changelog format.
* `template/SKILL.md` สำหรับสร้าง skill ใหม่ ครอบคลุม frontmatter ที่ใช้ trigger ทั้งภาษาไทยและอังกฤษ พร้อมโครงสร้าง body ที่ skill เก่าใช้.
* `AGENTS.md` ที่บอก AI agent ที่ไม่ใช่ Claude (Codex, Cursor, Gemini, OpenCode, ฯลฯ) ว่ารีโปนี้ใช้ฟอร์แมตอะไรและจะเรียกใช้ยังไง — symlink-friendly ตามแบบ obra/superpowers.
* `.github/PULL_REQUEST_TEMPLATE.md` ที่ช่วยให้ผู้ contribute กรอกข้อมูลสำคัญครบ.
* `.github/ISSUE_TEMPLATE/bug_report.yml`, `content_correction.yml`, `feature_request.yml` เพื่อ structure การเปิด issue.

---

## [0.1.0] — 2026-05-16

### Added

* **Skills ทั้ง 12 ตัว** ครอบคลุม:
  * การสื่อสาร: `thai-translate`, `thai-social-caption`, `thai-customer-service`
  * เอกสารทางการ: `thai-resume`, `thai-government-form`, `thai-festival-card`
  * บัญชี/กฎหมาย: `thai-invoice` (Revenue Code §86/4), `thai-pdpa`
  * ข้อมูลและฟอร์แมต: `thai-id-validate` (PromptPay + checksum), `thai-date-format` (พ.ศ./ค.ศ.), `thai-address` (77 จังหวัด), `thai-text-processing` (Thai NLP).
* **Validator skills** (มี code + self-test): `thai-id-validate`, `thai-date-format`, `thai-address`, `thai-invoice` — Python + TypeScript ที่ผ่าน self-test ครบทุกตัว.
* **Continuous integration** ผ่าน GitHub Actions (`.github/workflows/test.yml`) ที่รัน `scripts/test-all.sh` ทุก push สู่ `main` และทุก pull request.
* **Test runner** `scripts/test-all.sh` ที่รัน Python tests, TypeScript tests ผ่าน `npx --yes tsx`, และ SKILL.md validator ในคำสั่งเดียว. รองรับ flag `--py` / `--ts` / `--validate` สำหรับ subset.
* **SKILL.md validator** `scripts/validate-skills.py` ที่ตรวจ frontmatter (name ตรงกับ directory, description ไม่ว่าง, body มี heading) ของทั้ง 12 skill และตรวจ drift ระหว่าง `.claude-plugin/plugin.json` กับ `skills/` directory. ไม่ depend on PyYAML.
* **CONTRIBUTING.md** — คู่มือ contribute สองภาษา ครอบคลุม local setup, project layout, การรันเทสต์, ขั้นตอนเพิ่ม skill ใหม่, และข้อแนะนำสำหรับเนื้อหาที่อ้างอิงกฎหมาย/ระเบียบ.
* **SECURITY.md** — ขั้นตอนรายงานช่องโหว่ผ่าน GitHub Private Vulnerability Reporting, ขอบเขต in-scope/out-of-scope, กฎ "ไม่ paste ข้อมูลส่วนตัวจริงในรายงาน", และ disclaimer ชัดเจนสำหรับ `thai-pdpa` / `thai-invoice` / `thai-government-form`.
* **Plugin marketplace manifests** (`.claude-plugin/plugin.json`, `marketplace.json`) สำหรับติดตั้งผ่าน `/plugin marketplace add Boom-Vitt/claude-thai-skills`.
* **`install.sh`** สำหรับติดตั้ง user-scope ลง `~/.claude/skills/` ทั้งแบบติดตั้งครบและเลือกเฉพาะ skill.
* **README** ที่อธิบายเหตุผล (12 ปัญหาเดิมที่ Claude พลาดซ้ำๆ), ตัวอย่างการใช้งาน, โครงสร้างโปรเจกต์, ข้อจำกัดที่รู้ตัวดี, และวิธีร่วมพัฒนา.

### Fixed

* `skills/thai-invoice/calc.py` — self-test ก่อนหน้านี้ print `PASS`/`FAIL` แต่ไม่ได้ exit non-zero เมื่อ check ผิด ซึ่งทำให้ CI รับ regression แบบเงียบๆ. ตอนนี้ track failure แล้ว `raise SystemExit(1)` ถ้ามีอย่างน้อยหนึ่ง case ผิด.
* `skills/thai-address/parse.py` — tighten regex ของชื่อถนนเป็น single-token เพื่อไม่ให้ greedy-capture กิน keyword `แขวง` ที่อยู่ถัดไป.

### Security

* Test fixture ของเลขบัตรประชาชน และเบอร์โทรในรีโปเป็น synthetic — สร้างให้ผ่าน checksum/รูปแบบ แต่ไม่ตรงกับบุคคลจริงเท่าที่ผู้เขียนทราบ.

### Docs

* README rewrite — humanized prose, 12-grievance opener, banner SVG ที่ใช้ Anthropic-orange accent + Thai script.

---

## ลิงก์เทียบรุ่น / Compare links

ลิงก์เทียบรุ่นจะเพิ่มหลังจากมี git tag ของ release. ปัจจุบัน `0.1.0` คือ initial release จึงยังไม่มี predecessor ให้เทียบ.

* `[Unreleased]`: https://github.com/Boom-Vitt/claude-thai-skills/compare/v0.1.0...HEAD
* `[0.1.0]`: https://github.com/Boom-Vitt/claude-thai-skills/releases/tag/v0.1.0
