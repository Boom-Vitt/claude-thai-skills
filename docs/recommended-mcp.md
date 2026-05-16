# MCP Servers ที่แนะนำสำหรับคนไทย
## Recommended MCP servers for Thai users

MCP (Model Context Protocol) คือวิธีให้ Claude คุยกับ service ภายนอก — Gmail, Google Drive, Stripe, Supabase ฯลฯ. ในเอกสารนี้รวม MCP server ที่ maintainer ใช้บ่อยและคิดว่าคนไทยจะได้ประโยชน์.

> 🔒 **ไม่มี API key / token / credential ใน document นี้** — ทุกค่า config เป็น placeholder. ให้ใส่ของตัวเอง.

วิธีติดตั้ง MCP: ใส่ใน `~/.claude/settings.json` ที่ field `mcpServers`.

```jsonc
{
  "mcpServers": {
    "<server-name>": {
      "command": "...",
      "args": ["..."],
      "env": { "API_KEY": "..." }
    }
  }
}
```

หรือใช้ `/mcp` ใน Claude Code เพื่อจัดการแบบ interactive.

---

## 🟢 Tier 1 — ใช้บ่อย (highly recommended)

### Gmail MCP
- **ทำอะไร:** อ่าน/เขียน/ค้น email, จัดการ label, ทำ draft
- **เหมาะกับใคร:** ทุกคนที่ใช้ Gmail
- **ทำไมต้องใช้กับคนไทย:** pair กับ `thai-email` skill — ให้ Claude เขียน draft ภาษาไทยให้แล้วส่งเลย
- **ตั้งค่า:** ใช้ official Anthropic Gmail connector ผ่าน [claude.ai/settings/connectors](https://claude.ai/settings/connectors) หรือ third-party MCP server

### Google Calendar MCP
- **ทำอะไร:** สร้าง/แก้ event, list calendars, suggest meeting time
- **เหมาะกับใคร:** ทุกคนที่จัด meeting / appointment
- **ทำไมต้องใช้กับคนไทย:** สั่งภาษาไทยได้ — "ขอ meeting พรุ่งนี้ 14:00 กับทีมขาย ชื่อ Q3 review"

### Google Drive MCP
- **ทำอะไร:** อ่าน/ค้นไฟล์ Drive, copy, get metadata
- **เหมาะกับใคร:** ทีมที่ใช้ Google Workspace
- **Pair กับ:** `docx`, `pptx`, `xlsx` skills (built-in)

---

## 🟡 Tier 2 — สำหรับธุรกิจ / SME

### Stripe MCP
- **ทำอะไร:** สร้าง customer, invoice, payment link, refund, list disputes
- **เหมาะกับใคร:** ธุรกิจรับเงินผ่าน Stripe (international payments)
- **หมายเหตุไทย:** Stripe ยังไม่ support PromptPay ทางตรง — สำหรับชำระเงินในประเทศใช้ Omise/2C2P/SCB API แทน (ยังไม่มี MCP official); ใช้ `thai-id-validate` skill ของรีโปนี้สำหรับ PromptPay QR

### Supabase MCP
- **ทำอะไร:** Manage Supabase projects, run SQL, deploy edge functions, branches, migrations
- **เหมาะกับใคร:** dev ที่ใช้ Supabase เป็น backend
- **ทำไมแนะนำ:** dev ไทยจำนวนมากใช้ Supabase เป็น Firebase แทน — เร็ว, ฟรี tier ดี, มี Thai community ใหญ่บน Discord

### Postiz MCP (จาก postiz skill)
- **ทำอะไร:** Schedule social posts ไป 28+ ช่อง — Facebook, Instagram, TikTok, LINE, Threads, X, LinkedIn, YouTube, Pinterest, Reddit, ฯลฯ
- **เหมาะกับใคร:** content creator, brand, agency ในไทย
- **Pair กับ:** `thai-social-caption` skill ของรีโปนี้ → ให้ Claude เขียนแคปชั่นไทย แล้ว schedule post ผ่าน Postiz

---

## 🔵 Tier 3 — Niche / Creative

### Canva MCP
- **ทำอะไร:** สร้าง design จาก brand template, generate design, comment, export
- **เหมาะกับใคร:** marketing team, social media manager, designer freelancer
- **หมายเหตุ:** ฟอนต์ไทยใน Canva (TH Sarabun, Kanit, Prompt, Athiti) supported

### HeyGen MCP
- **ทำอะไร:** AI avatar video, voice clone, lipsync, video translation
- **เหมาะกับใคร:** content creator ทำ video ภาษาไทย, course creator
- **หมายเหตุ:** Voice clone ภาษาไทยทำได้ — แต่อย่าใช้ผิดศีลธรรม (deepfake)

### Meta/Facebook Ads MCP
- **ทำอะไร:** สร้าง campaign, ad set, creative, custom audience; ดู insights, anomaly signal, benchmark
- **เหมาะกับใคร:** agency, e-commerce ที่ยิงแอด FB/IG เยอะ
- **Pair กับ:** `thai-social-caption` สำหรับ ad copy

### n8n MCP
- **ทำอะไร:** สร้าง/แก้/รัน workflow (automation), search nodes, validate, test
- **เหมาะกับใคร:** dev/automation engineer ที่ใช้ n8n self-hosted
- **ทำไมแนะนำคนไทย:** n8n self-hosted = ฟรีไม่ลิมิต, host บน VPS ไทย (CAT, Bluehost TH) ได้

---

## 🟣 Tier 4 — Dev tools

### Firecrawl MCP (ผ่าน plugin)
- **ทำอะไร:** scrape, crawl, map website, find broken links
- **เหมาะกับใคร:** SEO, data scraping, research
- **Pair กับ:** `claude-seo` plugin's audit skills

### GitHub MCP
- **ทำอะไร:** issue, PR, code search, releases
- **Built-in:** Claude Code มี `gh` CLI integration อยู่แล้ว — แต่ MCP สะดวกกว่าบางที

### Context7 MCP
- **ทำอะไร:** ดึง doc API ของ library/framework ล่าสุด (เหมือนคุยกับ documentation)
- **เหมาะกับใคร:** dev ที่อ่าน doc ของ framework เก่า/มี version conflict
- **ทำไมแนะนำ:** Claude อาจไม่รู้ doc ของ library ที่ release หลัง knowledge cutoff — Context7 ช่วยได้

### Gemini API Docs MCP
- **ทำอะไร:** ค้น Google Gemini API docs โดยเฉพาะ
- **เหมาะกับใคร:** dev ที่ทำ Gemini app

### TradingView MCP
- **ทำอะไร:** ข้อมูล market (หุ้น, crypto, forex)
- **เหมาะกับใคร:** trader, analyst, fintech dev
- **หมายเหตุ:** หุ้นไทย (SET) ก็ดูได้

---

## ⚙️ MCP ที่ผมแนะนำให้เริ่มจาก 3 ตัวก่อน

ถ้าเพิ่งเริ่ม Claude Code อย่ายัด MCP เยอะเกินไป (กิน context window). เริ่มจาก:

1. **Gmail** — งาน email ทุกคนต้องใช้
2. **Google Calendar** — meeting prep / scheduling
3. **GitHub** — ถ้าเป็น dev

แล้วค่อยเพิ่มที่เหลือตามงานจริง.

---

## 🚫 อย่าใส่ใน config เด็ดขาด

- API key, secret token ของจริง — ใช้ env var แทน:
  ```jsonc
  "env": { "STRIPE_API_KEY": "$STRIPE_API_KEY" }
  ```
- credential ที่ commit ไป repo — ใช้ `.env` + `.gitignore`
- production database credentials — ใช้ branch/staging MCP แทน

---

## เพิ่ม MCP ของไทยที่ยังขาด (call for contributions)

ถ้าใครรู้/ทำ MCP server สำหรับ service ไทยเหล่านี้แล้ว เปิด PR เพิ่ม section ได้:

- 🏦 **Thai banking** — SCB, KBank, BBL API (transfer, slip verify)
- 💸 **PromptPay** — generate/validate QR, slip verification (มี endpoint sandbox ของแบงค์)
- 🛒 **Shopee/Lazada Open API** — order, product, message
- 📦 **Flash Express / Kerry / Thailand Post** — tracking, label
- 📱 **LINE Messaging API** — push, broadcast, rich menu
- 🪪 **DBD** (กรมพัฒนาธุรกิจการค้า) — company info lookup
- 📜 **Revenue Department e-Tax** — e-invoice submission
- 🆔 **DOPA** — Thai ID verify (กรมการปกครอง — ต้อง approve)

ถ้าใครทำ MCP server หนึ่งในนี้แล้ว publish public บน GitHub — ติดต่อมา จะ feature ที่นี่.
