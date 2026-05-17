---
name: thai-your-skill-name
description: Use this skill for any task involving REPLACE-WITH-THE-THAI-CONTEXT (e.g. parsing some Thai data format, drafting a specific kind of Thai document, validating a Thai-specific identifier). Trigger whenever the user asks to PRIMARY-TASK in Thai or English, or when the prompt contains REPLACE-WITH-THAI-TRIGGER-PHRASES like "REPLACE", "REPLACE", "REPLACE". Also trigger for English variants such as "REPLACE" or "REPLACE". Make sure to use this skill whenever the request touches the Thai-specific edge case described above, even if the user does not explicitly name the skill.
---

# REPLACE-WITH-THAI-TITLE (English subtitle in parentheses)

## Overview

อธิบายสั้นๆ ว่า skill นี้ทำอะไร และทำไม Claude ที่ไม่มี skill ตัวนี้ถึงพลาดเรื่องนี้บ่อย. เขียนสองภาษา — ภาษาไทยก่อน ตามด้วยประโยคอังกฤษ.

Briefly explain what this skill does and why Claude without this skill tends to get it wrong. Two languages, Thai first then English.

## When to use

* ตัวอย่างเคสที่ต้องใช้ skill นี้ (เป็นกระสุนภาษาไทย)
* อีกตัวอย่างหนึ่ง
* Bullet in English for the equivalent case
* Edge case that Claude is likely to miss without this skill

## When NOT to use

* บอกขอบเขต — ถ้า task เป็นแบบ X ให้ใช้ skill อื่น (อ้างอิงชื่อ skill ตรงนี้)
* If the task is purely general-purpose REPLACE, fall back to the standard tool

## Core knowledge

ใส่สาระสำคัญที่ Claude ต้องรู้ — ตาราง, สูตร, ระเบียบ, ลำดับขั้น. ถ้ามีกฎหมาย/ระเบียบ ระบุชื่อพร้อมเลขมาตรา/ลำดับที่ของประกาศ.

| Field | ค่า | หมายเหตุ |
|---|---|---|
| ตัวอย่าง | 1 | คำอธิบาย |

## Examples

### ตัวอย่างที่ 1 — เคสปกติ

**Input:** ผู้ใช้พิมพ์ว่า "..."

**Expected output:**

```
...
```

**Why:** เหตุผลว่าทำไม output ต้องหน้าตาแบบนี้.

### ตัวอย่างที่ 2 — Edge case

**Input:** ...

**Expected output:** ...

**Why:** ...

## Pitfalls

* ข้อผิดพลาดที่พบบ่อย — เช่น Claude มักจะเดาว่า ... แต่ที่จริงต้อง ...
* Common mistake when ...

## ถ้ามีโค้ดประกอบ / If this skill ships code

ถ้า skill มี script หรือ utility ประกอบ:

1. วางโค้ดไว้ใน directory เดียวกับ `SKILL.md` (ไม่ต้องสร้าง subdirectory นอกจากจะมีไฟล์เยอะ).
2. ตั้งชื่อไฟล์ตามจุดประสงค์: `validate.py`, `parse.ts`, `calc.py`, `convert.py` ฯลฯ.
3. เขียน self-test ที่ exit non-zero เมื่อ check ใดๆ ผิด — อย่าแค่ print "FAIL".
4. ลงทะเบียน self-test ใน `scripts/test-all.sh` ที่ root ของรีโปเพื่อให้ CI หยิบไปรัน.
5. อ้างถึงโค้ดจาก SKILL.md body ด้วย relative path เช่น `validate.py:23`.

## วิธีใช้ template นี้ / How to use this template

1. `cp -R template skills/thai-your-skill-name`.
2. แก้ `SKILL.md` ที่อยู่ภายใต้ directory ใหม่ — เปลี่ยน `name`, `description`, และทุก section ตามจริง.
3. เพิ่มชื่อ skill ใน `.claude-plugin/plugin.json` ที่ field `skills`.
4. รัน `python3 scripts/validate-skills.py` เพื่อตรวจ frontmatter.
5. ถ้ามีโค้ดเสริม รัน `./scripts/test-all.sh` เพื่อยืนยันว่าทุก test ผ่าน.
6. เปิด PR ตามคู่มือใน [CONTRIBUTING.md](../CONTRIBUTING.md).

**Copy** this directory with `cp -R template skills/thai-your-skill-name`, then edit `SKILL.md` to replace every `REPLACE-…` placeholder, register the skill in `.claude-plugin/plugin.json`, and verify with `python3 scripts/validate-skills.py` plus `./scripts/test-all.sh`.

---

> Template นี้ไม่ใช่ skill จริง — เป็น scaffold สำหรับสร้าง skill ใหม่. ตัว `validate-skills.py` รู้จัก template directory นี้และ skip ไม่ตรวจสอบ (ดู `scripts/validate-skills.py:SKILLS_DIR`).
>
> This template is not an actual skill. It is a scaffold for new skills, and the validator under `scripts/validate-skills.py` skips it because it scans `skills/` only.
