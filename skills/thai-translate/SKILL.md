---
name: thai-translate
description: Use this skill for any task involving English-Thai or Thai-English translation, localization, or rewording. Trigger whenever the user asks to: translate text between Thai and English, localize content for a Thai audience, render English idioms in Thai (or vice versa), pick the right pronouns and register, choose between keeping a term in English vs ทับศัพท์, or fix awkward translations. Also trigger for requests like "แปลเป็นไทย", "แปลอังกฤษเป็นไทย", "ช่วยแปลหน่อย", "localize Thai", "translate this", "Thai version", or any variation. If the task involves moving meaning between Thai and English at any level — word, sentence, document — use this skill.
---

# แปลไทย-อังกฤษ (Thai ⇄ English Translation)

## Overview
แปลภาษาไม่ใช่แค่เปลี่ยนคำ แต่ต้องเลือกระดับภาษา สรรพนาม และคำทับศัพท์ให้เหมาะกับผู้อ่าน. Translation is register selection first, word selection second — Thai forces you to commit to a social relationship before you finish the sentence.

## When to use
- แปลเอกสาร อีเมล โพสต์ บทความ ระหว่างไทย-อังกฤษ
- Localizing UI, marketing copy, contracts for a Thai audience
- เลือกสรรพนาม "I/you" ที่เหมาะกับบริบท
- ตัดสินใจว่าจะทับศัพท์ คำไหน หรือเก็บภาษาอังกฤษไว้
- แก้คำแปลที่ "อ่านแล้วรู้ว่าแปลมา" ให้เป็นธรรมชาติ

## Core conventions

### 1. Register matrix — pick BEFORE translating

| Register | When to use | Example greeting | I / you |
|---|---|---|---|
| ราชการ / royal | govt letters, ทรงพระเจริญ, ราชสำนัก | กราบเรียน | กระผม·ดิฉัน → ท่าน |
| สุภาพทางการ business | external emails, contracts, press | เรียนคุณ… | ผม·ดิฉัน → คุณ·ท่าน |
| กึ่งทางการ workplace | colleagues, Slack, internal docs | สวัสดีครับ·ค่ะ | ผม·เรา → คุณ·พี่·น้อง |
| ลำลอง casual | friends, social posts | หวัดดี | เรา → นาย·เธอ·ชื่อ |
| กันเอง intimate | close friends only | ดิ้·เฮ้ย | กู → มึง or first names |

Rule: when in doubt, go ONE step more formal than English source. English "Hi" → Thai "สวัสดีครับ", not "หวัดดี", unless context says otherwise.

### 2. Keep-in-English vs ทับศัพท์
- **Keep English:** tech (API, deploy, server, KPI, deadline, email, meeting), brands (Apple, Shopee), units (GB, USD), proper nouns, acronyms.
- **ทับศัพท์ established:** คอมพิวเตอร์, อินเทอร์เน็ต, อีเมล, โน้ตบุ๊ก, แอป, เว็บไซต์, ไลน์, เฟซบุ๊ก. Use these in mainstream/consumer copy.
- **Translate:** abstract concepts (freedom → เสรีภาพ), institutional terms (board of directors → คณะกรรมการ), legal terms (use Royal Institute glossary).
- Audience test: government/elderly → translate or use Royal Institute spelling. Tech/youth → keep English or short ทับศัพท์.

### 3. Pronouns (no 1:1 mapping with I/you)

| Thai "I" | Speaker | Context |
|---|---|---|
| ผม | male | default polite |
| ดิฉัน | female | formal business, written |
| ฉัน | female (or neutral) | semi-formal, song lyrics |
| หนู | female younger → senior | family, school, junior staff |
| เรา | any | casual, also plural |
| กระผม | male | very formal, to superiors |
| กู | any | rough/intimate only |

| Thai "you" | Use when |
|---|---|
| คุณ | safe default, polite |
| ท่าน | very formal, to elders/officials |
| พี่ | addressee is older/senior |
| น้อง | addressee is younger/junior |
| เธอ | casual, romantic, female-to-anyone |
| นาย | casual male, or "you" in light tone |
| first name + พี่·น้อง | most natural in workplace |

Pitfall: defaulting "you" → "คุณ" in casual contexts sounds cold. Use พี่·ชื่อ instead.

### 4. ครับ / ค่ะ particles
- Per-utterance, NOT per-sentence. In writing, ~1 ครับ·ค่ะ per paragraph is normal.
- Spoken/chat: end most turns with ครับ·ค่ะ.
- Written articles, news, captions: usually drop entirely.
- ครับ (male), ค่ะ (female), คะ (female questions: "จริงหรอคะ").

### 5. Idiom equivalents (don't translate literally)
| Thai | English equivalent |
|---|---|
| น้ำขึ้นให้รีบตัก | strike while the iron is hot |
| กบในกะลา | frog in a well / narrow worldview |
| ขี่ช้างจับตั๊กแตน | sledgehammer to crack a nut |
| น้ำท่วมปาก | tongue-tied / can't speak up |
| ไก่เห็นตีนงู งูเห็นนมไก่ | they know each other's secrets |
| ปิดทองหลังพระ | doing good unseen / unsung hero |
| ชักแม่น้ำทั้งห้า | beat around the bush |
| หนีเสือปะจระเข้ | out of the frying pan into the fire |

## Examples

**INPUT:** "Hi team, just a quick reminder our deadline is Friday EOD."
**OUTPUT (กึ่งทางการ workplace):** "สวัสดีทีม แจ้งย้ำอีกครั้งนะครับ deadline ของเราคือวันศุกร์ก่อนเลิกงานครับ"

**INPUT:** "We regret to inform you that your application was unsuccessful."
**OUTPUT (สุภาพทางการ):** "ทางบริษัทขอแจ้งด้วยความเสียใจว่า ใบสมัครของท่านยังไม่ผ่านการพิจารณาในครั้งนี้"

**INPUT:** "555 มาช้าอีกแล้ว เดี๋ยวกูไปก่อนนะ"
**OUTPUT (casual EN):** "Lol late again — I'm heading out first."

**INPUT:** "She always plays it safe — total frog-in-a-well thinking."
**OUTPUT:** "เธอเซฟตัวเองตลอด คิดแบบกบในกะลาเลย"

## Common mistakes
- Translating "the / a" — Thai has no articles. Drop them.
- Pluralizing nouns Thai keeps singular: "หนังสือ 3 เล่ม" not "หนังสือs".
- Auto-using "คุณ" for every "you" → sounds stiff in chat/social.
- Ending every Thai sentence with ครับ·ค่ะ in written articles → over-polite.
- Translating "We are excited to announce…" → "พวกเราตื่นเต้นที่จะประกาศ…" (literal/awkward). Use "ทางเราขอประกาศ…" or "ยินดีอย่างยิ่งที่จะแจ้งว่า…"
- Using ดิฉัน in casual chat → sounds like 1980s newscaster. Use ฉัน·เรา.
- Mixing registers within one paragraph (กระผม + นาย together).
- Using common ใช้ / ให้ / กิน / พูด when translating royal context → must shift to ราชาศัพท์ (พระราชทาน / เสวย / ตรัส). See royal vocabulary section.
- Accepting a sworn-translation, medical-label, or patent request without referring to a certified specialist → high-stakes domains require certified providers, not general LLM translation.

## ราชาศัพท์ minimum (Royal vocabulary basics)

Use when translating content involving the Thai royal family, royal news, royal events, or formal references to His Majesty / Her Majesty / สมเด็จพระบรมวงศ์. Wrong register or familiar vocabulary in royal context is legally and culturally serious in Thailand — when in doubt, escalate.

| English | Thai (common) | ราชาศัพท์ (royal) |
|---|---|---|
| to go | ไป | เสด็จ / เสด็จพระราชดำเนิน |
| to say / speak | พูด | ตรัส / รับสั่ง / มีพระราชดำรัส |
| to think | คิด | ทรงพระราชดำริ / มีพระราชดำริ |
| to give / grant | ให้ | พระราชทาน |
| to eat | กิน | เสวย / ทรงเสวย |
| to sleep | นอน | บรรทม |
| to be born | เกิด | พระราชสมภพ (king/queen) / ประสูติ (princes·princesses) |
| to bestow a gift | มอบให้ | พระราชทาน / โปรดเกล้าฯ พระราชทาน |
| hand | มือ | พระหัตถ์ |
| head | หัว | พระเศียร |
| hair | ผม | พระเกศา |
| face | หน้า | พระพักตร์ |
| speech / royal address | คำพูด·สุนทรพจน์ | พระราชดำรัส / พระบรมราโชวาท |
| photograph / portrait | รูป·ภาพถ่าย | พระบรมฉายาลักษณ์ (king·queen) / พระฉายาลักษณ์ (royals) |
| birthday | วันเกิด | วันคล้ายวันพระราชสมภพ (king·queen) / วันคล้ายวันประสูติ (princes·princesses) |
| to do (auxiliary) | — | ทรง + verb (e.g., ทรงงาน, ทรงดนตรี, ทรงม้า) |

The auxiliary **ทรง** prefixes many ordinary verbs to lift them into royal register (ทรงงาน = "works", ทรงพระอักษร = "writes/studies"). Do not stack ทรง with a verb that already has a royal form (write ตรัส, not ทรงตรัส).

**Tiered system — important caveat.** ราชาศัพท์ is not one vocabulary set but several tiers used for different ranks: พระมหากษัตริย์·สมเด็จพระราชินี (highest) → สมเด็จเจ้าฟ้า → พระองค์เจ้า → หม่อมเจ้า (lower royal). Vocabulary differs across tiers (e.g., พระราชสมภพ vs. ประสูติ above). This skill provides a *working minimum* for journalistic / informational translation. For ceremonial, state, palace, or official royal-household content, consult the **Royal Institute (สำนักงานราชบัณฑิตยสภา, orst.go.th)** reference or an experienced specialist translator. Do not improvise.

## Scope note — when NOT to use this skill

This skill covers general EN↔TH translation, localization, and register selection. Bow out and recommend a specialist for:

- **Legal contracts & sworn translation** — Thai courts, immigration, and government agencies often require sworn / NAATI-equivalent / **Department of Consular Affairs–certified** translation (consular.mfa.go.th). General LLM output is not admissible.
- **Medical records, prescriptions, drug labels, clinical trial documents** — patient safety risk; use a qualified medical translator.
- **Patent filings, technical specifications, regulatory submissions** — highly domain-specific terminology; mistranslation has legal/financial consequences.
- **Royal / state ceremonial content** — beyond the ราชาศัพท์ minimum above; consult the Royal Institute (orst.go.th) or an experienced palace-affairs specialist.
- **Pali / Sanskrit / Buddhist scripture (พระไตรปิฎก, บทสวดมนต์)** — language outside everyday Thai; requires a scholar of Buddhist canonical languages.
- **Northern / Northeastern / Southern dialects (คำเมือง, อีสาน, ปักษ์ใต้)** and Pak Tai variants — this skill covers Central Thai (ภาษากลาง) only. Dialectal work needs a native speaker of that region.
- **Old Thai / Sukhothai-era scripts, jindamani, ancient inscriptions** — academic specialty.

When the user asks for any of the above, name the limitation explicitly, then point them to: **Royal Institute (orst.go.th)** for vocabulary/style, **Department of Consular Affairs (consular.mfa.go.th)** for sworn certification, or a relevant domain expert. Declining gracefully beats shipping an inaccurate translation in a high-stakes domain.
