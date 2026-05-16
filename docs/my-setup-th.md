# การตั้งค่า Claude Code ส่วนตัว — ทัวร์แบบลบข้อมูลลับแล้ว
## My Claude Code setup — sanitized tour

เอกสารนี้บอกว่า maintainer (@Boom-Vitt) ตั้งค่า Claude Code ยังไงให้ทำงานคล่องที่สุด เผื่อคนอื่นจะเอาไปประยุกต์ใช้.
This document shows how the maintainer configures Claude Code daily, in case others want to adopt parts of it.

> ⚠️ **ไม่มี secrets / no secrets** — ค่าทุกอย่างในนี้ปลอดภัยจะแชร์ (ไม่มี API key, token, MCP credential ของจริง). ถ้าใครจะเอาไปใช้ ให้ใส่ค่าของตัวเอง.

---

## 1. โครงสร้างโฟลเดอร์ `~/.claude/`

```
~/.claude/
├── settings.json            # Settings หลัก (ดูข้อ 2)
├── settings.local.json      # Settings เฉพาะเครื่อง (sandbox, permission overrides)
├── CLAUDE.md                # (optional) memory ระดับ user — ของผมว่าง, ใช้ project-level แทน
├── skills/                  # Skills ที่ติดตั้ง user-scope
├── agents/                  # Custom subagents (.md ไฟล์ละ 1 agent)
├── commands/                # Custom slash commands (ของผมว่าง)
├── hooks/                   # Hook scripts (.sh)
├── plugins/                 # Plugin marketplace data (managed)
└── projects/<project>/memory/   # Memory per-project
```

---

## 2. `settings.json` — ค่าหลักที่แนะนำ

ตัวอย่าง (ของจริง maintainer เป็นแบบนี้ พร้อมคำอธิบาย):

```jsonc
{
  // ใช้ Opus 4.7 พร้อม 1M context — โมเดลเก่ง + context กว้าง
  "model": "opus[1m]",

  // permission mode: "auto" = แค่ classifier auto-allow read-only/safe;
  // ลด popup permission ไปได้เยอะ
  "permissions": {
    "defaultMode": "auto"
  },

  // เปิด max effort + ให้ advisor ใช้ opus เหมือนกัน (ที่ปรึกษาที่ฉลาดที่สุด)
  "effortLevel": "max",
  "advisorModel": "opus",
  "skipAutoPermissionPrompt": true,

  // Plugin ที่เปิดใช้ user-scope
  "enabledPlugins": {
    "commit-commands@claude-plugins-official": true,
    "superpowers@claude-plugins-official": true,
    "claude-seo@agricidaniel-seo": true
  },

  // Extra marketplace (นอก official)
  "extraKnownMarketplaces": {
    "agricidaniel-seo": {
      "type": "github",
      "repo": "AgriciDaniel/claude-seo"
    }
  },

  // MCP servers — ใส่ของตัวเอง ห้าม commit token จริง!
  "mcpServers": {
    "gemini-api-docs": {
      "command": "npx",
      "args": ["-y", "gemini-api-docs-mcp"]
    }
    // เพิ่มอื่นๆ ตามต้องการ
  },

  // Hooks — ดูข้อ 4
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          { "type": "command", "command": "...architect-mode prompt..." },
          { "type": "command", "command": "~/.claude/hooks/check-token-usage.sh" }
        ]
      }
    ],
    "PreCompact": [
      {
        "matcher": "",
        "hooks": [
          { "type": "command", "command": "..." }
        ]
      }
    ]
  }
}
```

**`settings.local.json`** (per-machine):
```json
{
  "sandbox": { "enabled": true },
  "autoAllowBashIfSandboxed": true
}
```

ทำไม sandbox: เปิด `auto` permission แล้ว ปลอดภัยกว่าเดิมเพราะ command อันตรายโดน sandbox ดักไว้.

---

## 3. Plugin ที่ใช้ทุกวัน

| Plugin | ทำอะไร | ทำไมใช้ |
|---|---|---|
| `superpowers` (claude-plugins-official) | TDD, brainstorming, debugging, parallel-agents, writing-skills | ระเบียบวินัยในการเขียนโค้ด |
| `commit-commands` | `/commit`, `/commit-push-pr`, `/clean_gone` | จัด git workflow เร็วขึ้น |
| `claude-seo` (agricidaniel-seo) | SEO suite — 28 skills ครอบคลุม technical, content, GEO, local | ทำ SEO ลูกค้า/เว็บตัวเอง |
| `ralph-loop` (prp-marketplace) | recurring loops | task ทำซ้ำตามรอบ |

ติดตั้ง:
```
/plugin marketplace add anthropics/claude-plugins-official
/plugin install superpowers@claude-plugins-official
/plugin install commit-commands@claude-plugins-official
```

---

## 4. Hooks — ของจริงผมมี 2 ตัว

### `check-token-usage.sh` (UserPromptSubmit)

อยู่ที่ `~/.claude/hooks/check-token-usage.sh`. มันอ่าน transcript JSONL ของ session นั้น รวม `cache_read + cache_creation + input_tokens` จาก usage block ล่าสุด และเตือนใน systemMessage ถ้าเกิน 60% ของ 400k context window — แนะนำ `/compact`.

ตัวอย่าง skeleton:

```bash
#!/usr/bin/env bash
TRANSCRIPT="$CLAUDE_TRANSCRIPT_PATH"   # Claude injects path
LIMIT=400000
THRESHOLD=$(( LIMIT * 60 / 100 ))

USED=$(tail -n 50 "$TRANSCRIPT" | jq -s '
  map(select(.usage)) | last | .usage
  | (.input_tokens // 0) + (.cache_read_input_tokens // 0) + (.cache_creation_input_tokens // 0)
' 2>/dev/null)

if [ "${USED:-0}" -gt "$THRESHOLD" ]; then
  PCT=$(( USED * 100 / LIMIT ))
  echo "⚠️ ใช้ context ไปแล้ว ${PCT}% (${USED}/${LIMIT}) — พิจารณา /compact"
fi
```

### Architect mode prompt (inline)

`UserPromptSubmit` hook ตัวที่ 2 inject ข้อความเข้า additional context ทุกครั้งที่ user ส่ง prompt: บอก Claude ให้ auto-invoke matching skills/agents โดยไม่ต้องรอ user พิมพ์ `/` เอง, ใช้ Explore สำหรับโค้ด, Plan สำหรับ design, Agent สำหรับ parallel work, และเรียก `advisor()` ก่อนเริ่มทำงานหนัก. ตัวอย่าง:

```bash
printf '%s' '{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"Architect mode: when a task matches an installed skill or agent description, invoke it via the Skill or Agent tool without waiting for the user to type a slash command. Use Explore for codebase questions, Plan for design, Agent subagents for independent parallel work, and call advisor() before committing to substantive approaches."}}'
```

---

## 5. Custom subagents

ผมมี subagent 21 ตัวใน `~/.claude/agents/`. ส่วนใหญ่เป็น SEO specialist 17 ตัว (auto-spawn จาก `claude-seo` plugin) + 4 ตัวทั่วไป:
- `api-research-test-schema` — research API → write tests → update schema (workflow เดียวจบ)
- `backend-design` — REST/GraphQL/RPC, data modeling, queue/worker design
- `frontend-design` — UI, components, design tokens
- `unit-test-writer` — เขียน unit test หลังโค้ดเปลี่ยน

วิธีสร้าง subagent เอง: เขียนไฟล์ `.md` ใน `~/.claude/agents/` ที่มี frontmatter:

```markdown
---
name: my-agent
description: Use when ... (third person, when-to-use)
tools: [Read, Write, Bash, Grep]  # หรือ "All tools"
model: sonnet  # หรือ opus / haiku / inherit
---

# System prompt ของ agent ตรงนี้...
```

---

## 6. Memory pattern ที่ผมใช้

- `~/.claude/CLAUDE.md` — ของผม **ว่าง** ตั้งใจ; เพราะรวมจะใช้กับโปรเจกต์เดียวเท่านั้นแย่
- `~/.claude/projects/<project-path-encoded>/memory/MEMORY.md` — index list, 1 บรรทัดต่อ memory
- `~/.claude/projects/<project-path-encoded>/memory/<topic>.md` — memory file จริง

Memory แบ่งเป็น 4 type ตาม system prompt: `user`, `feedback`, `project`, `reference`. รายละเอียดอยู่ใน auto-memory section ของ Claude Code system prompt — ไม่ต้องตั้งเอง.

---

## 7. Workflow ประจำวัน

1. เริ่ม session: บอก Claude สั้นๆ ว่าจะทำอะไร — architect mode hook จะแนะให้ Claude เลือก skill/agent เอง
2. งาน parallel: Claude spawn subagent แบบ `run_in_background: true` แล้วทำต่ออย่างอื่น
3. ทุกครั้งก่อน commit ใช้ `/commit` (จาก commit-commands plugin) — มันจะรัน lint + diff + draft message
4. ก่อน push: `/commit-push-pr` ถ้ามี GitHub remote
5. ถ้า context เกิน 60%: hook เตือน → `/compact`
6. ถ้าติดงานยาก: invoke `advisor()` — reviewer ที่เห็น transcript ทั้งหมด

---

## 8. ของที่ผมจงใจไม่ใช้

- `--no-verify` (skip hooks) — ห้าม, แก้ root cause แทน
- `git push --force` to main — ห้ามเด็ดขาด
- `rm -rf` แบบเสี่ยง — ใช้ git stash / git restore ก่อน
- ตอบ "ใช่ ๆ" ให้ advisor ทุกครั้งโดยไม่อ่าน — รับมัน, ไม่งั้นเสียประโยชน์
- เปิด `bypassPermissions` mode — น่ากลัวเกินไป, ใช้ `auto` + sandbox พอ

---

## 9. ต่อยอด

อ่านเพิ่ม:
- [recommended-mcp.md](recommended-mcp.md) — MCP servers ที่ผมแนะนำสำหรับคนไทย
- [Claude Code docs](https://docs.claude.com/en/docs/claude-code)
- [Anthropic skill specification](https://agentskills.io/specification)

ถ้ามีคำถาม — เปิด issue ได้.
