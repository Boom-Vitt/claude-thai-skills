---
name: thai-social-caption
description: Use this skill for any task involving writing Thai-language social media captions, posts, or short-form copy. Trigger whenever the user asks to: write a caption for Facebook, Instagram, TikTok, Threads, X (Twitter), Pantip, or LINE TIMELINE in Thai, draft a Thai social post, write a Thai product/review/giveaway post, pick hashtags for a Thai audience, or adapt copy for a Thai social channel. Also trigger for requests like "เขียนแคปชั่น", "caption ภาษาไทย", "เขียน TikTok caption", "โพสต์ Facebook", "ลงไอจี", "caption social media Thai", "เขียนรีวิว", or any variation. If the output is a short Thai post designed to be published on a social platform, use this skill.
---

# แคปชั่นโซเชียลไทย (Thai Social Caption)

## Overview
แต่ละแพลตฟอร์มมีโทน ความยาว และ hashtag ที่ต่างกัน เขียนผิดแพลตฟอร์ม = ยอดไม่มา. Each Thai social platform has its own dialect — Facebook ≠ Threads ≠ TikTok. Pick the platform's tone before writing a single word.

## When to use
- เขียนแคปชั่นโพสต์ลง FB, IG, TikTok, Threads, X, Pantip, LINE TL
- เขียนรีวิวสินค้า ร้านอาหาร คาเฟ่
- โพสต์ขายของ giveaway โปรโมชั่น
- โพสต์มูเตลู เลขเด็ด ขอพร
- เลือก hashtag ที่คนไทยใช้จริง

## Core conventions

### 1. Platform tone table

| Platform | Length | Tone | Hashtags |
|---|---|---|---|
| Facebook | 60–200 chars, story-driven | warm, slightly formal | 0–3 |
| Instagram | 80–150 chars | aspirational, lifestyle | 5–15 (mix TH+EN) |
| TikTok | 30–100 chars, hook-first | playful, snappy | 2–5 (incl. trending) |
| Threads | 1–3 sentences | conversational, opinionated | 0–2 |
| X (Twitter) | <140 chars Thai | punchy, witty | 0–1 |
| Pantip | long-form, story format | community-friendly | uses room tags |
| LINE TIMELINE | 1–2 sentences | broadcasty, friendly | 0 |

### 2. Thai social writing devices
- **Repeated vowels for emphasis:** ดีมากกกก, อร่อยยยย, ปังงงง, น่ารักกกก
- **Laughter:** 555 (mild) → 55555555 (rolling on floor). Avoid in CS context.
- **Softening particles:** น้าาาา, เนอะ, ดิ, ป่ะ, อ่ะ, อ่ะนะ. These make tone friendly.
- **Slang (use with caution):** ปัง = killer, จัดเต็ม = goes all-out, ตำ = devour/cop it, มู = pray for luck, สายมู = spiritual believer, รีวิวจัดให้ = full review incoming.
- **Emojis that dominate Thai social:** 🤣🥺😭🔥💯✨🙏🥰😅 . 🙏 = thanks/please/respect (not just prayer). ✨ = cute aesthetic. Avoid 👍 alone — reads cold.
- **กรู/มึง** — relatable but reads as low-class/funny. OK for memes & meme accounts, NEVER for brand accounts unless that's the brand voice.

### 3. Hashtag conventions
- **Facebook:** brand tag only (#ชื่อร้าน). Too many = looks spammy.
- **Instagram:** stack 5–15 niche TH+EN: #ของกินกรุงเทพ #คาเฟ่อร่อย #รีวิวร้านอาหาร #bangkokfood #thaifoodie. Niche > generic.
- **TikTok:** trending sounds + #fyp #fypシ #ของกินมาแรง #รีวิวtiktok . Trend tags expire — check what's hot.
- **Pantip:** use room/tag system not # — เลือกห้องสินสาด, ไกลบ้าน, ก้นครัว ฯลฯ
- **Brand posts:** put brand tag FIRST, then 2–3 discovery tags.

### 4. Genre archetypes

**รีวิว (review):**
"วันนี้พามาลองร้าน X ย่าน Y… เมนูเด็ดคือ Z รสชาติ [adj] ราคา [฿] / สรุป: [verdict] / ใครผ่านแถวนี้ลองเลย 👍"

**ขายของ (selling):**
hook (problem/desire) → benefit → CTA → ราคา → urgency
"ผมร่วงเยอะ? 😱 / เซรั่มสูตรใหม่ ลดผมร่วงใน 14 วัน / ปกติ 990 ลดเหลือ 590 / ทักแชทเลย / เหลือ 23 ขวดเท่านั้น 🔥"

**มูเตลู (spiritual/lucky numbers):**
"เลขเด็ดงวด 16/5/68 หลวงพ่อ X ใบ้มา… / เลข 2 ตัว: 47, 74 / 3 ตัว: 147 / ใครได้เอาบุญด้วยนะคะ 🙏✨"

**ดราม่า / ระบาย (rant):**
"เรื่องมีอยู่ว่า… 😤 / [story] / สรุปคือ [punchline] / เพื่อนๆเจอแบบนี้บ้างมั้ย?"

**Giveaway:**
"แจกฟรี! 🎉 [prize] / กติกา: 1) กดไลก์ 2) คอมเมนต์แท็กเพื่อน 1 คน 3) แชร์โพสต์ตั้งสาธารณะ / ประกาศผล [date] / #ชื่อแบรนด์"

## Examples

**INPUT:** Write IG caption for new iced matcha launch at คาเฟ่ "บ้านไม้".
**OUTPUT:**
"กรีนเข้มจี๊ดดดด มัทฉะใหม่มาแล้วน้า 🍵✨ / ตัดหวานกำลังดี เหมาะกับวันร้อนๆ / มาลองก่อนใครที่บ้านไม้ ☁️
#บ้านไม้คาเฟ่ #มัทฉะไทย #คาเฟ่กรุงเทพ #icedmatcha #bangkokcafe #matchalover #คาเฟ่ฮอปปิ้ง"

**INPUT:** TikTok caption for a 15-sec ramen review.
**OUTPUT:**
"ราเมงร้านนี้ ตำมั้ย? 🍜🔥 มีคำตอบ #รีวิวtiktok #ของกินมาแรง #fyp"

**INPUT:** Threads post reacting to PM2.5.
**OUTPUT:**
"ตื่นมาเปิดม่าน นึกว่าหมอกลงเชียงใหม่ ที่แท้คือฝุ่น กทม. 😮‍💨 ใครใส่ N95 ออกบ้านบ้าง?"

**INPUT:** Facebook post launching free shipping.
**OUTPUT:**
"ส่งฟรีทั่วประเทศ! 🚚 ถึงสิ้นเดือนนี้เท่านั้น / ช้อปครบ 500.- ส่งฟรีไม่ต้องใช้โค้ด / ทักแชทสั่งได้เลยค่ะ 😊
#ชื่อร้าน"

## Common mistakes
- Literal translation of marketing English: "พวกเราตื่นเต้นที่จะประกาศ" → use "ขอประกาศ" หรือ "มาแล้วจ้า"
- Too many CTAs in one post (pick ONE action).
- Wrong register for platform: Facebook caption written in TikTok tone reads juvenile; TikTok caption written like Facebook reads boring.
- Hashtag spam on Facebook (kills reach).
- Brand account using กู/มึง without clear meme-account positioning.
- Forgetting platform character limits (X clips at 280; Threads at 500).
- Using only English hashtags for a Thai-only audience product.
- Emoji overload (>5 emojis per short caption looks desperate).
