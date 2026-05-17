# Security Policy
## นโยบายความปลอดภัย

เอกสารฉบับนี้บอกว่าจะรายงานช่องโหว่ของรีโปนี้ได้อย่างไร, รีโปนี้รองรับเวอร์ชันใดบ้าง, และข้อจำกัดสำคัญที่ผู้ใช้ควรเข้าใจก่อนพึ่งพา skill ในงานจริง — โดยเฉพาะ skill ที่เกี่ยวข้องกับกฎหมาย, ภาษี, และเอกสารราชการ.

> This document describes how to report a security vulnerability in this repository, which versions receive fixes, and the limitations users should understand before relying on these skills in production, particularly the skills that touch Thai law, taxation, and government documentation.

---

## เวอร์ชันที่ยังได้รับการ patch / Supported versions

รีโปนี้ใช้ semantic versioning อย่างหลวมๆ. ตอนเวอร์ชัน `0.x.y` (ปัจจุบัน) จะ patch เฉพาะ minor ล่าสุดเท่านั้น — เพราะรีโปยังเป็น preview ใช้เองอยู่. หลังจาก `1.0.0` แล้วถึงจะมีข้อผูกพันชัดเจนว่าจะ backport ไปยัง major เก่ากี่ตัว.

| Version | สถานะ |
|---------|---------------|
| `0.1.x` | กำลัง patch — bug fix และ security fix จะลงที่นี่ |
| `< 0.1` | ไม่มี (รีโปยังไม่เคยเผยแพร่เวอร์ชันก่อนหน้านี้) |

This repository follows semantic versioning loosely. While the project is in its `0.x` series, only the latest minor version receives security patches. After `1.0.0` is released a clearer back-porting policy will be published here.

---

## วิธีรายงานช่องโหว่ / How to report a vulnerability

**อย่าเปิด public GitHub issue** สำหรับ vulnerability — เพราะ issue จะเห็นได้ทั่วโลกก่อนที่จะ fix.

ช่องทางที่แนะนำเรียงตามลำดับ:

1. **GitHub Private Vulnerability Reporting** — เปิดที่หน้า [Security tab](https://github.com/Boom-Vitt/claude-thai-skills/security/advisories/new) ของรีโปนี้. นี่เป็นช่องทางที่ดีที่สุดเพราะ GitHub จะแจ้งเตือนและ track ให้.

2. **อีเมล** ถึงผู้ดูแลรีโปโดยตรง — ดูที่อยู่อีเมลของ commit author ในประวัติ git (`git log --format='%aE' | head -1`).

ในรายงาน โปรดระบุ:

* **ชนิดของช่องโหว่** — code execution, data leak, supply-chain, validation bypass, ฯลฯ.
* **ขั้นตอนทำซ้ำ** ที่ผมเปิดเครื่องตามได้ทันที.
* **ผลกระทบที่คาดว่าจะเกิด** ถ้ามีใครใช้ช่องโหว่นี้.
* **เวอร์ชัน** ของรีโป (commit hash) และของ Python/Node/OS.
* **suggested fix** ถ้ามีไอเดีย — ไม่บังคับ แต่ช่วยเร่งการแก้ได้มาก.

ผมจะตอบกลับภายใน 7 วัน เพื่อยืนยันว่าได้รับและจัดลำดับความสำคัญแล้ว. ถ้าจำเป็นต้อง release patch ผมจะ coordinate disclosure กับคุณก่อนเปิดเผยรายละเอียดสาธารณะ.

Please do **not** open a public GitHub issue for a vulnerability. Use the private reporting channels listed above. In your report, include the class of vulnerability, reproduction steps, expected impact, the repository version (commit hash), and your environment versions. A suggested fix is helpful but not required. I aim to acknowledge reports within seven days and will coordinate disclosure with you before publishing details.

---

## ขอบเขตของรายงาน / Scope

ช่องโหว่ที่อยู่ในขอบเขต ได้แก่:

* **ปัญหาด้าน safety ของโค้ด** ที่รันบนเครื่องผู้ใช้ — เช่น path traversal ใน `install.sh`, code injection ผ่าน input ที่ไม่ได้ sanitize ใน `parse.py`, dependency ที่ดึงโค้ดอื่นเข้ามาโดยไม่ได้ตั้งใจ.
* **Test fixture ที่หลุดเป็นข้อมูลส่วนตัวจริง** — เช่น ถ้าใครเผลอ commit เลขบัตรประชาชนของจริงเข้ามา ผมต้องการรู้ทันทีเพื่อ rewrite history.
* **ปัญหา supply-chain** — เช่น link ใน README ที่ชี้ไปยัง package ที่ถูก typosquat, npm package ที่ skill อ้างถึงแต่ตัวจริงถูก takeover.
* **Logic bug ที่นำไปสู่การ bypass safety** — เช่น `is_valid_thai_id()` ที่ return `True` ให้ ID ที่จริงไม่ valid และเปิดทาง social engineering.

ช่องโหว่ที่ **อยู่นอกขอบเขต**:

* **ความถูกต้องของเนื้อหากฎหมาย** — เช่น "PDPA template ของคุณไม่ครอบคลุม use case X". อันนี้เป็นเรื่องสำคัญและรับรายงานเช่นกัน แต่เปิดเป็น public issue ปกติได้.
* **ปัญหาของ Claude เอง** — เช่น hallucination, refusal, การจัดการ context. รายงานที่ Anthropic แทน.
* **ข้อจำกัดของ skill ที่ documented อยู่แล้วใน README** (`Known limitations` section).

In-scope: code safety in scripts that run on a user's machine (path traversal, injection, unintended dependency execution), accidental check-in of real personal data as a test fixture, supply-chain issues such as typosquatted links or package takeovers, and logic bugs that bypass a safety check. Out of scope: legal correctness of skill content (file a normal issue), bugs in Claude itself (report to Anthropic), and limitations already documented in the README.

---

## สิ่งที่อย่า paste ลงในรายงาน / What not to include in reports

ถ้าตัวอย่างของช่องโหว่ใช้ข้อมูลจริง โปรดทดแทนด้วยข้อมูลปลอมก่อนส่งเข้ามา:

* **เลขบัตรประชาชน** ของบุคคลจริง — แปลงเป็นค่าทดสอบที่ผ่าน checksum.
* **เบอร์โทรของคนรู้จัก** — ใช้ `0812345678` หรือ `0899999999`.
* **ที่อยู่บ้านจริง** — ใช้ที่อยู่สำนักงานหรือ landmark สาธารณะ.
* **ชื่อบริษัทลูกค้า** ที่ยังไม่ได้รับความยินยอม — ใช้ "บริษัท X จำกัด".
* **API key, token, credential** — ขออะไรก็ตามที่เริ่มต้นด้วย `sk-`, `pk_`, `eyJ`, ตัด/ปกปิดทุกตัว.

ถ้ารายงานติด private data ไปแล้ว แจ้งผมทันที — ผมจะช่วย rewrite git history และลบ artifact ที่เกี่ยวข้องออก.

If your proof-of-concept references real personal data, replace it with synthetic equivalents before sending the report: substitute test national IDs that pass checksum, generic phone numbers, public landmark addresses, placeholder company names, and redacted API tokens. If you accidentally include real data in a report, let me know immediately and I will help rewrite the relevant history.

---

## ขอบเขตเกี่ยวกับเนื้อหากฎหมายและภาษี / Legal and tax content disclaimer

Skill ในรีโปนี้ที่อ้างอิงกฎหมายหรือระเบียบไทย — `thai-pdpa`, `thai-invoice`, `thai-government-form` และ template ภายในนั้น — เขียนขึ้นเป็น **เครื่องมือร่างเอกสาร**, ไม่ใช่คำปรึกษากฎหมายหรือคำปรึกษาด้านภาษี.

* **ไม่มีความสัมพันธ์ทนาย-ลูกความ.** การใช้ skill หรือ template ในรีโปนี้ไม่ก่อให้เกิด attorney-client relationship กับผู้ดูแลรีโปหรือผู้ contribute ใดๆ.
* **กฎหมายไทยเปลี่ยนได้.** ประกาศของกรมสรรพากร, PDPC, สำนักนายกฯ ออกใหม่เป็นระยะ. เนื้อหาใน skill เป็นภาพ ณ วันที่ commit ล่าสุด ไม่ได้ track real-time. ก่อนใช้กับงานที่มีความเสี่ยงสูงให้ตรวจกับแหล่งทางการอีกครั้ง.
* **ตรวจกับมืออาชีพ.** สำหรับเอกสารที่ส่งให้ราชการ, ลูกค้าใหญ่, หรือคดีความ ควรให้ทนาย, นักบัญชี CPA, หรือ DPO มืออาชีพรีวิวก่อนใช้จริง.
* **ผู้ดูแลรีโปและผู้ contribute ไม่รับผิดชอบ** ต่อความเสียหายที่เกิดจากการพึ่งพาเนื้อหาเหล่านี้ — ดูเงื่อนไขใน [LICENSE](LICENSE).

ถ้าพบว่าเนื้อหาส่วนใดของ skill เหล่านี้ขัดต่อประกาศ/ระเบียบล่าสุด **โปรดเปิด issue ปกติ** พร้อมลิงก์อ้างอิงต้นทาง (ราชกิจจานุเบกษา, ประกาศของหน่วยงาน). กรณีนี้ไม่ถือเป็น security vulnerability ตามนิยามข้างต้น แต่ก็เป็นสิ่งสำคัญที่ต้องรีบแก้.

The skills that touch Thai law or taxation — `thai-pdpa`, `thai-invoice`, `thai-government-form`, and their templates — are drafting aids, not legal or tax advice. Using them does not create any attorney-client relationship. Thai law changes; treat the content as a snapshot at the time of the latest commit and verify against official sources before relying on it. For high-stakes documents, have a qualified Thai lawyer, certified accountant, or DPO review the draft. The maintainers and contributors disclaim liability for damages arising from reliance on this content (see [LICENSE](LICENSE)). If you find content that conflicts with a current regulation, please open a standard issue with citations — this is important to fix, but it is not a security vulnerability under this policy.

---

## ความเป็นส่วนตัวของข้อมูลผู้ใช้ / Privacy of user data

รีโปนี้ไม่เก็บข้อมูลของผู้ใช้. ไม่มี telemetry, ไม่มี analytics, ไม่มี call-home. Skill ทำงานในเครื่องคุณทั้งหมด.

ทดสอบทุกตัวที่เห็นในรีโป (เลขบัตรประชาชน, เบอร์โทร, ที่อยู่, ชื่อบริษัท) เป็น **synthetic fixtures** — สร้างให้ผ่าน checksum, สอดคล้องกับ pattern, แต่ไม่ตรงกับบุคคล/องค์กรจริงตามที่ผู้เขียนทราบ. ถ้าพบว่าค่าใดบังเอิญตรงกับของจริง โปรดรายงานทันทีตามช่องทางข้างต้น เพื่อให้สลับเป็นค่าใหม่.

This repository does not collect user data: no telemetry, no analytics, no remote calls. All test fixtures committed to the repository (national IDs, phone numbers, addresses, company names) are synthetic — constructed to pass checksums and match expected patterns but, to the best of the maintainer's knowledge, not corresponding to any real person or organisation. If you discover a fixture that coincidentally matches a real identifier, please report it via the channels above so it can be replaced.

---

## ขอบคุณ / Acknowledgements

ขอบคุณทุกคนที่รายงาน vulnerability อย่างมีความรับผิดชอบ. ถ้าต้องการให้ credit ใน advisory ก็แจ้งได้.

Thank you to everyone who reports vulnerabilities responsibly. If you would like credit in the resulting advisory, please indicate so when you report.
