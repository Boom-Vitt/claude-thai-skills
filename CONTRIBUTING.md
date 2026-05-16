# Contributing to claude-thai-skills
## คู่มือสำหรับคนที่อยากช่วยพัฒนา

ขอบคุณที่อยากช่วยปรับปรุงรีโปนี้ครับ. โปรเจกต์นี้เป็น skill ภาษาไทยที่ผมเขียนไว้ใช้เอง — ยินดีรับ contribution ทุกขนาด ตั้งแต่แก้คำผิดในเอกสาร, แต่งประโยคให้อ่านง่ายขึ้น, รายงานบั๊ก, ไปจนถึงการเพิ่ม skill ใหม่. เอกสารฉบับนี้เขียนไว้ให้ผู้ contribute มีจุดเริ่มที่ชัดเจน และเพื่อให้ทุกคนรู้ว่าผมจะรีวิวอะไรบ้างก่อน merge.

> Thank you for considering a contribution. This repository is a personal toolkit of Thai-language skills, and contributions of any size are welcome — fixing a typo, rewording an awkward sentence, reporting a bug, or proposing a new skill. This document explains the moving parts so you can submit changes with confidence, and outlines what I look for during review.

---

## ก่อนเริ่ม / Before you start

### ภาษาที่ใช้สื่อสาร

เปิด issue, PR หรือคอมเมนต์ได้ทั้งภาษาไทยและภาษาอังกฤษ. ไม่ต้องสลับโทน — เลือกภาษาที่ถนัด. ถ้าเขียนเป็นภาษาไทยแล้วบอกบริบทเกี่ยวกับกฎหมาย, เอกสารราชการ, หรือธุรกิจในไทยให้ละเอียดหน่อยจะดีมาก เพราะรายละเอียดเล็กๆ พวกนี้คือสิ่งที่ Claude เดาเองไม่ได้.

You can open issues, pull requests, and review comments in either Thai or English. Pick whichever language you are more comfortable in. Detailed context about Thai law, government practice, or local business conventions is especially valuable, because that is exactly the kind of nuance the skills are designed to capture.

### ขอบเขตของรีโป

รีโปนี้รวบรวม skill ที่ตอบโจทย์เฉพาะของคนใช้ภาษาไทยกับ Claude Code. ถ้าสิ่งที่อยากจะเพิ่มเป็น skill ทั่วไปที่ไม่ได้ผูกกับบริบทไทย (เช่น utility ทั่วไป, framework specific, API กลางๆ) อาจจะเหมาะกับรีโปอื่นมากกว่า. เกณฑ์คร่าวๆ ของผมคือ: ถ้าทำ skill นี้แล้ว Claude ทำงานเรื่องไทยให้ถูกต้องมากขึ้นอย่างมีนัยสำคัญ skill นี้เหมาะที่จะอยู่ที่นี่.

This repository focuses on skills that are specifically useful when working in Thai language, business, legal, or cultural contexts. General-purpose utilities or framework-specific skills are usually a better fit elsewhere. A rough test: if your proposed skill measurably improves the quality of Claude's output on Thai-language tasks, it belongs here.

---

## ตั้งค่าเครื่องมือในเครื่อง / Local setup

คุณต้องมี:

* **Git** สำหรับ clone และส่ง pull request.
* **Python 3.10 ขึ้นไป** — ใช้ Python ที่ติดมากับเครื่อง (`python3 --version` เพื่อตรวจ).
* **Node.js 18 ขึ้นไป** สำหรับ TypeScript tests. คำสั่ง `npx --yes tsx` ของ test runner จะดาวน์โหลด `tsx` ให้อัตโนมัติ ไม่ต้อง `npm install` ก่อน.

ขั้นตอน:

```bash
git clone https://github.com/Boom-Vitt/claude-thai-skills.git
cd claude-thai-skills
./scripts/test-all.sh
```

ถ้า output ลงท้ายด้วย `All test files passed.` แสดงว่าเครื่องคุณพร้อมแล้ว. ถ้าไม่ผ่าน อ่าน error message — ส่วนใหญ่จะบอกว่าขาด `python3` หรือ `npx`.

You need Git, Python 3.10 or newer, and Node.js 18 or newer. After cloning, run `./scripts/test-all.sh` from the repository root. The script downloads `tsx` on first run via `npx --yes`, so you do not need to install Node dependencies manually.

---

## โครงสร้างโปรเจกต์ / Project layout

โครงสร้างหลักของรีโปเป็นแบบนี้:

```
claude-thai-skills/
├── .claude-plugin/          ตัว manifest ของ Claude Code plugin
├── .github/workflows/       GitHub Actions (ตอนนี้มี test.yml ตัวเดียว)
├── assets/                  รูป banner และ asset ที่ใช้ใน README
├── docs/                    เอกสารยาวที่อยู่นอก README
├── scripts/
│   ├── test-all.sh          รัน self-test ทุกตัว (CI ก็เรียกตัวนี้)
│   └── validate-skills.py   ตรวจ SKILL.md ทุกตัวให้ frontmatter ถูกต้อง
├── skills/<skill-name>/     หนึ่งโฟลเดอร์ต่อหนึ่ง skill — SKILL.md อยู่ที่นี่
├── install.sh               สคริปต์ติดตั้ง user-scope ลง ~/.claude/skills/
├── CONTRIBUTING.md          ไฟล์นี้
├── SECURITY.md              ขั้นตอนรายงานช่องโหว่ + disclaimer เนื้อหากฎหมาย
└── README.md
```

แต่ละ skill ต้องมีไฟล์ `SKILL.md` ที่ root ของโฟลเดอร์ skill นั้น. `SKILL.md` จะมี YAML frontmatter ที่ระบุ `name` (ตรงกับชื่อโฟลเดอร์) และ `description` (สิ่งที่ Claude อ่านเพื่อตัดสินใจว่าจะหยิบ skill นี้ขึ้นมาใช้เมื่อใด). ที่เหลือคือ Markdown body ที่อธิบาย skill กับยกตัวอย่าง.

Each skill lives in its own directory under `skills/`, and must contain a `SKILL.md` file with YAML frontmatter declaring `name` (matching the directory name) and `description` (the text Claude reads when deciding whether to activate the skill). The body is plain Markdown.

---

## วิธีรันเทสต์ / Running the tests

มีสามวิธีในการรัน:

1. **รันทุกอย่าง** (เหมือนที่ CI รัน):

   ```bash
   ./scripts/test-all.sh
   ```

2. **รันเฉพาะส่วน** ถ้าอยากเร่งความเร็วตอนพัฒนา:

   ```bash
   ./scripts/test-all.sh --py        # เฉพาะ Python
   ./scripts/test-all.sh --ts        # เฉพาะ TypeScript
   ./scripts/test-all.sh --validate  # เฉพาะตัว validator
   ```

3. **รันไฟล์เดียว** ระหว่าง debug:

   ```bash
   python3 skills/thai-invoice/calc.py
   npx --yes tsx skills/thai-date-format/convert.ts
   ```

ถ้าเพิ่ม self-test ให้ skill ใหม่ อย่าลืมไป register ที่ส่วนล่างของ `scripts/test-all.sh` ด้วย เพราะ CI ดู script ตัวนี้เป็นต้นทาง.

To run the entire suite the way CI does, use `./scripts/test-all.sh`. The flags `--py`, `--ts`, and `--validate` run subsets when you want a faster feedback loop. If you add a new test file, register it at the bottom of `scripts/test-all.sh` so CI picks it up.

---

## เพิ่ม skill ใหม่ / Adding a new skill

ก่อนเริ่มเขียน skill ใหม่ แนะนำให้เปิด issue ก่อนเพื่อคุยกันว่า skill นั้นเหมาะกับรีโปนี้ไหม. หลายครั้ง skill ที่ดูคล้ายของเดิมจริงๆ ควรเป็นการ extend skill ที่มีอยู่ ไม่ใช่สร้างใหม่.

ขั้นตอนเมื่อเริ่มเขียน:

1. **ตั้งชื่อโฟลเดอร์** ขึ้นต้นด้วย `thai-` แล้วตามด้วย topic แบบ kebab-case. เช่น `thai-banking`, `thai-vehicle-tax`. ชื่อนี้จะเป็นค่า `name` ใน frontmatter ด้วย.

2. **เขียน `SKILL.md`** ที่มี frontmatter:

   ```markdown
   ---
   name: thai-banking
   description: Use this skill for tasks involving Thai banking — transfer slips, account number validation, BIC/SWIFT lookups for Thai banks, and reading common bank statement formats. Trigger when the user asks to ... Also trigger for "...", "...", "..." in Thai.
   ---

   # หัวข้อ skill (English subtitle)

   ## Overview
   ...
   ```

   `description` คือสิ่งที่ Claude อ่านเพื่อตัดสินใจ — เขียนให้ระบุชัดว่า "trigger when ... " มี keyword ไทยจริงๆ ที่คนจะพิมพ์, และมีตัวอย่าง phrasing ทั้งไทยและอังกฤษ. ยิ่ง concrete ยิ่งดี เพราะ Claude เลือก skill จาก description.

3. **เพิ่มชื่อ skill ใน `.claude-plugin/plugin.json`** ที่ field `skills`. ถ้าลืม validator จะร้องเมื่อ CI รัน.

4. **ถ้ามีโค้ด** (Python หรือ TypeScript) ใส่ไว้ในโฟลเดอร์ skill เดียวกันกับ `SKILL.md`. ตั้งชื่อไฟล์ตามจุดประสงค์ (`validate.py`, `parse.ts`, `calc.py` ฯลฯ) แล้ว register self-test ใน `scripts/test-all.sh`.

5. **เขียน self-test ที่ exit non-zero ถ้าผิด** เพราะ CI ดูจาก exit code. ห้ามแค่ `print("FAIL")` แล้วจบ — ต้อง `raise SystemExit(1)` หรือ `process.exit(1)`.

6. **รัน `./scripts/test-all.sh`** ก่อนเปิด PR — ถ้าไม่ผ่าน CI ก็จะไม่ผ่าน.

When proposing a new skill, please open an issue first to discuss whether it fits this repository or whether your idea is better implemented by extending an existing skill. Each new skill needs a directory named `thai-<topic>`, a `SKILL.md` whose `name` matches the directory and whose `description` is concrete enough for Claude to match against user prompts, an entry in `.claude-plugin/plugin.json`, and any executable test files registered at the bottom of `scripts/test-all.sh`. Test files must exit non-zero on failure; printing the word "FAIL" without setting an exit code makes CI dangerously misleading.

### เขียน description ให้ดี / Writing a good description

`description` ของ skill มีคนอ่านอยู่สองกลุ่ม: Claude ตอน routing และคนอ่านใน marketplace. เขียนยาวพอที่จะระบุ trigger ไทยและอังกฤษได้ครบ แต่ก็ไม่ต้องยาวเกินจำเป็น. ดู skill ที่มีอยู่เป็นตัวอย่าง — ทุก description เริ่มด้วย "Use this skill for ...", ระบุว่า trigger เมื่อใด, ให้ตัวอย่าง phrasing ภาษาไทยและอังกฤษ, และจบด้วยกฎจำง่ายๆ ของ scope ("if the task involves X, use this skill").

A skill description is read both by Claude during routing and by humans browsing the marketplace. It should be long enough to enumerate Thai and English trigger phrases but no longer than necessary. The existing skills follow a consistent template: a leading "Use this skill for ..." sentence, an enumeration of triggers, concrete example phrasings in both languages, and a closing rule of scope. Mirror that shape unless you have a reason not to.

---

## แก้ skill ที่มีอยู่ / Modifying existing skills

### เนื้อหาทั่วไป

PR ที่ปรับปรุงตัวอย่าง, แก้ภาษา, เพิ่ม edge case ที่ skill ยังไม่ได้พูดถึง — ส่งได้เลย. ขอแค่ลองดูว่า diff ที่ทำให้ test ที่มีอยู่ไม่ผ่านไหม.

Improvements to examples, language, and additional edge cases are very welcome. Just make sure existing tests still pass.

### เนื้อหาที่เกี่ยวกับกฎหมาย / ราชการ / ภาษี

`thai-pdpa`, `thai-invoice`, และ `thai-government-form` มีเนื้อหาที่อ้างอิงกฎหมายและระเบียบไทย. กฎหมายเปลี่ยนได้, ระเบียบใหม่ออกมาเรื่อยๆ. ถ้าจะ PR เนื้อหากลุ่มนี้:

* **อ้างอิงต้นทางทุกครั้ง.** ใส่ลิงก์ไปยังประกาศของกรมสรรพากร, ราชกิจจานุเบกษา, PDPC, หรือสำนักนายกฯ ใน PR description.
* **ระบุวันที่ของแหล่งอ้างอิง.** ถ้าอ้างประกาศที่ออกเดือนใด เขียนไว้ใน PR เลย ผมจะใช้ตรวจสอบเร็วขึ้น.
* **อย่าลบ disclaimer ใน skill body.** ทุก skill กลุ่มนี้บอกชัดเจนว่าไม่ใช่คำปรึกษากฎหมาย และเป็นความรับผิดชอบของผู้ใช้ที่จะตรวจสอบกับ professional. รักษาประโยคพวกนี้ไว้.

For skills that touch Thai law, government procedure, or tax — `thai-pdpa`, `thai-invoice`, and `thai-government-form` in particular — please cite primary sources (Revenue Department announcements, the Royal Gazette, PDPC notices, the Prime Minister's Office regulations) directly in the pull request. Include the date of the source so the reviewer can verify quickly. Disclaimers in the skill body must remain intact: these skills are drafting aids, not legal advice, and a removed disclaimer materially changes the risk profile.

---

## ขั้นตอน Pull Request / Pull request process

1. **Fork แล้ว clone** หรือทำงานบน branch ใน fork ของคุณ.
2. **เขียน commit message ที่บอกเหตุผล** — เน้น "why" มากกว่า "what". diff บอก what ได้ดีอยู่แล้ว.
3. **รัน `./scripts/test-all.sh` ในเครื่อง** ให้ผ่านก่อนเปิด PR.
4. **เปิด PR ไปที่ `main`** พร้อมคำอธิบายสั้นๆ ของสิ่งที่เปลี่ยน. ถ้าเป็นเนื้อหาเกี่ยวกับกฎหมาย/ราชการ ใส่ลิงก์อ้างอิงด้วย.
5. **CI จะรันอัตโนมัติ.** ถ้า CI ไม่ผ่าน ดู log แล้วแก้ก่อน — ถ้าไม่แน่ใจว่าเกิดจากอะไร comment ใน PR ได้.
6. **ผมจะรีวิวภายใน 1-2 สัปดาห์.** ถ้าเงียบไปกว่านั้น mention ใน PR ได้ (อาจลืม notification).

Open a pull request against `main` once the local test suite passes. Keep commits focused — one logical change per commit if you can. CI will run automatically. I review PRs within a week or two; if you have not heard back after that, feel free to mention me in the PR. For legally sensitive content, please cite primary sources in the PR description.

---

## รายงานบั๊ก / Reporting bugs

เปิด GitHub issue พร้อมข้อมูล:

* **สิ่งที่คุณทำ** (prompt ที่ส่งให้ Claude, คำสั่งที่รัน).
* **สิ่งที่ Claude หรือสคริปต์ตอบกลับมา** (paste output).
* **สิ่งที่คุณคาดว่าจะเกิด.**
* **เวอร์ชัน:** ของรีโป (commit hash), Python, Node, OS.

ถ้าเป็น bug ที่เกี่ยวกับเลขบัตรประชาชน, เบอร์โทร, ที่อยู่ — **อย่า paste ของจริง.** ใช้ค่าทดสอบที่ผ่าน checksum (เลขเริ่มต้นด้วย 0 หลายตัวก็พอ) หรือ generic placeholder. รีโปนี้ไม่อยากเก็บข้อมูลส่วนบุคคลของจริงไว้ใน issue history.

When filing a bug, please include the prompt or command you ran, the output you received, what you expected to happen, and your environment versions (repo commit, Python, Node, operating system). If the bug involves Thai national IDs, phone numbers, addresses, or other personal identifiers, **do not paste real values**: use synthetic test fixtures or generic placeholders. The repository should not accumulate real personal data in its issue history.

---

## รายงานช่องโหว่ความปลอดภัย / Reporting security issues

อ่าน [SECURITY.md](SECURITY.md). ห้ามเปิดเป็น public issue.

For security issues, see [SECURITY.md](SECURITY.md). Do not file a public issue.

---

## License

การ contribute ใดๆ จะถูก license แบบเดียวกับ project นี้ ([MIT](LICENSE)). ส่ง PR เท่ากับยินยอมว่าโค้ดของคุณจะถูกแจกจ่ายในเงื่อนไข MIT.

All contributions are licensed under the same [MIT license](LICENSE) as the rest of the project. By opening a pull request you agree that your code can be distributed under those terms.

---

## ขอบคุณ / Thank you

ทุก contribution มีคุณค่าหมด แม้กระทั่งการ report ว่า "skill นี้ดูไม่ครอบคลุมกรณี ABC". การที่คนช่วยกันสะสมความรู้เฉพาะของบริบทไทยไว้ในที่เดียวคือเป้าหมายของรีโปนี้ — ทำคนเดียวจะไม่ครอบคลุมแน่นอน.

Every contribution matters, including ones that simply note "this skill misses case ABC". The point of this repository is to collect Thailand-specific knowledge in one place; that goal is only reachable with collaboration.
