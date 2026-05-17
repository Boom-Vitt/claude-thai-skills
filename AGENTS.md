# AGENTS.md

This file is the entry point for any AI coding agent — Claude Code, Codex CLI, Cursor, Gemini CLI, OpenCode, Aider, or anything else — that has been pointed at this repository. It is deliberately short. The goal is to tell an agent what this repo is, how to verify changes, and what tone to use when contributing.

ไฟล์นี้เป็นจุดเริ่มต้นสำหรับ AI coding agent ทุกตัวที่ถูกชี้มาที่รีโปนี้ — ไม่ว่าจะเป็น Claude Code, Codex CLI, Cursor, Gemini CLI, OpenCode, Aider หรือเครื่องมืออื่น. เป้าหมายของไฟล์นี้คือบอก agent ว่ารีโปนี้คืออะไร, ตรวจสอบการเปลี่ยนแปลงยังไง, และควรใช้น้ำเสียงไหนเวลา contribute.

---

## What this repository is / รีโปนี้คืออะไร

`claude-thai-skills` is a collection of twelve Claude Code skills focused on Thai-language tasks: tax invoices, government letters, PDPA-compliant privacy notices, Thai national-ID validation, PromptPay QR generation, BE/CE date conversion, postal addresses, social captions, customer-service replies, resumes, festival greetings, and translation.

Each skill lives in `skills/<name>/` and has a `SKILL.md` file with YAML frontmatter (`name`, `description`). Four skills also carry Python and TypeScript code with self-tests.

---

## How to run the test suite / วิธีรันเทสต์

There is one canonical command:

```bash
./scripts/test-all.sh
```

It runs every Python self-test (`python3 skills/<skill>/<file>.py`), every TypeScript self-test (via `npx --yes tsx`), and the SKILL.md frontmatter validator. CI runs the exact same command — so a green run locally means a green run in CI.

Subset flags exist for tighter feedback loops: `--py`, `--ts`, `--validate`.

---

## How to add a new skill / วิธีเพิ่ม skill ใหม่

1. `cp -R template skills/thai-<your-skill>`.
2. Edit the new `SKILL.md` (replace every `REPLACE-…` placeholder).
3. Add the skill path to `.claude-plugin/plugin.json` under `skills`.
4. If shipping code, place it next to `SKILL.md`, write a self-test that exits non-zero on failure, and register the file in `scripts/test-all.sh`.
5. Run `./scripts/test-all.sh` until it prints `All test files passed.` before opening a pull request.

Full prose walkthrough lives in [CONTRIBUTING.md](CONTRIBUTING.md).

---

## How to write a SKILL.md description / เขียน description ของ skill ยังไง

The frontmatter `description` is the single most important field. Claude reads it to decide whether to invoke the skill, so it must be specific and slightly assertive.

Required elements:

* A leading "Use this skill for ..." sentence that names the domain in concrete terms.
* An enumeration of trigger phrases the user might type — **in both Thai and English**. Thai phrases must appear in quotes because Claude pattern-matches against them literally.
* A closing rule of scope: "If the task involves X, use this skill" so the boundary is unambiguous.
* Encourage triggering when in doubt — phrases like "Make sure to use this skill whenever ..." combat under-triggering.

The existing twelve skills are usable templates. Read three of them before drafting a new description.

---

## Tone for contributions / น้ำเสียงในการ contribute

This repository is maintained by one person and the writing style is intentionally conversational. When you commit, edit a README, or write a SKILL.md:

* Prose over bullet-point soup where prose fits.
* Bilingual when the audience needs it. The README and CONTRIBUTING are Thai-first with English follow-ups. Internal scripts and code comments are English.
* No emojis in new content unless the surrounding file already uses them as visual structure (the README's section markers are intentional and pre-date this rule).
* No marketing language. No "production-ready", "battle-tested", "supercharge your workflow". Describe what the thing does and what it does not do.

---

## What not to do / สิ่งที่ห้ามทำ

* Do not commit real Thai personal data as a test fixture. Use synthetic IDs that pass checksum but do not match a real person.
* Do not vendor third-party code into the repo. The skills point to PyThaiNLP and `promptpay-qr` as references; users install them separately. Attribution belongs in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
* Do not remove or weaken the disclaimers in `thai-pdpa`, `thai-invoice`, or `thai-government-form`. These skills are drafting aids, not legal advice; the disclaimers are load-bearing.
* Do not add a new skill without a `SKILL.md` that the validator accepts. CI will reject it.
* Do not push to `main` directly. Open a pull request so CI runs.

---

## Pointers / เอกสารอื่นที่ควรอ่าน

* [README.md](README.md) — what each skill does and why.
* [CONTRIBUTING.md](CONTRIBUTING.md) — full contribution workflow and bilingual prose.
* [SECURITY.md](SECURITY.md) — vulnerability reporting and the legal-content disclaimer.
* [CHANGELOG.md](CHANGELOG.md) — what changed in each release.
* [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) — attribution for libraries and government sources referenced by the skills.
* [template/SKILL.md](template/SKILL.md) — the scaffold for new skills.

If you are an agent and unsure how to proceed, prefer reading these files over inventing conventions. The patterns in this repo are intentional, even when they are quiet.
