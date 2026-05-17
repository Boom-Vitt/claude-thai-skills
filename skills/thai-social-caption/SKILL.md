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
| LINE VOOM | 100–300 chars | warm, plain-spoken | 3–5 |
| Live (pre) | 150–400 chars | hype + info-packed | 2–5 |

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

## LINE VOOM (LINE Timeline rebranded 2022)

LINE Voom = LINE's in-app social feed. คนละอย่างกับ LINE OA broadcast (ที่เด้งเข้าแชท). Voom เป็นฟีดที่คนเลื่อนดูเอง โทนต้องเป็นมิตรเหมือนเพื่อนบ้านคุยกัน ไม่ใช่โฆษณายัดเยียด.

**Audience profile:** Thai mass-market, อายุเฉลี่ยสูงกว่า TikTok เล็กน้อย (25–55), ครอบครัว, ต่างจังหวัดเยอะ, ใช้ LINE เป็นช่องทางหลักอยู่แล้ว. เข้าฟีดเพื่อดูข่าวบ้าน ดูร้านใกล้บ้าน ดูดวง ดูสาระน่ารู้.

**Caption length:** 100–300 ตัวอักษร ยาวกว่า TikTok สั้นกว่า Facebook ยาว ๆ. มีรูป/วิดีโอประกอบเสมอ — caption ไม่ใช่พระเอก แต่ต้องอธิบายให้ครบ.

**Tone:** สุภาพ เป็นกันเอง ภาษาบ้าน ๆ. ห้ามใช้ภาษาวัยรุ่นจัด ห้ามใช้ irony แบบ Gen Z ห้ามอังกฤษล้วน. เน้น "ค่ะ/ครับ" ลงท้าย, ใช้ น้า/นะคะ ได้.

**Hashtags:** มีระบบ # อยู่จริงแต่ไม่เด่นเท่า IG. ใส่ 3–5 พอ เน้น discovery tag ภาษาไทย: #สาระน่ารู้ #ของกินอร่อย #ร้านใกล้บ้าน #โปรโมชั่นวันนี้.

**What works:** ความอบอุ่น, รูปอาหาร, ครอบครัว, วันพระ/วันสำคัญทางศาสนา, โปรโมชั่นท้องถิ่น, สาระน่ารู้สั้น ๆ (เคล็ดลับครัว, สุขภาพ, การเงินพื้นฐาน), เลขเด็ด/ดูดวง, ข่าวร้านใหม่ในจังหวัด.

**What flops:** ภาษาอังกฤษเยอะ, มุก Gen Z แบบ ironic/sarcastic, CTA ดุดัน ("รีบสั่งเดี๋ยวนี้!!!"), trendy slang ของ TikTok (ตำ/มู ใช้ได้แต่อย่ายัด), ภาพแต่งจัดเกินจริง.

**Example 1 — product promo (ร้านขนมเปี๊ยะ):**
"ขนมเปี๊ยะไส้ถั่วกวนสูตรโบราณ อบใหม่ทุกเช้าค่ะ 🥮 / แป้งบางไส้แน่น หวานกำลังพอดี ทานคู่ชาร้อน ๆ อร่อยที่สุด / สั่งล่วงหน้า 1 วัน รับได้ที่ร้าน หรือส่ง Grab ในตัวเมืองค่ะ / กล่อง 6 ชิ้น 120 บาท / ทักไลน์ @banpiahome ได้เลยน้า
#ขนมเปี๊ยะ #ของฝากเชียงใหม่ #ขนมโบราณ #สาระน่ารู้"

**Example 2 — engagement/lifestyle (เคล็ดลับ):**
"เคล็ดลับลดค่าไฟหน้าร้อนแบบง่าย ๆ ที่บ้านทำได้เลยค่ะ ☀️ / 1) ตั้งแอร์ 26 องศา เปิดพัดลมช่วย / 2) ปิดเครื่องใช้ไฟฟ้าที่ standby / 3) ซักผ้ารวมรอบใหญ่ไม่ซักทีละนิด / ใครมีเคล็ดลับอื่นมาแชร์กันในคอมเมนต์ได้น้า ลองเอาไปปรับใช้กันนะคะ 🙏
#สาระน่ารู้ #ประหยัดค่าไฟ #เคล็ดลับในบ้าน"

## Live-stream captions (FB Live / TikTok Live / Shopee Live / IG Live)

Live commerce ในไทยใหญ่มาก — แม่ค้าไลฟ์ขายของได้หลักแสนต่อรอบ. แคปชั่นมี 2 จังหวะ: **pre-live announcement** (โพสต์ก่อนเริ่ม 1–24 ชม.) กับ **during-live updates** (โพสต์สั้น ๆ ระหว่างไลฟ์เพื่อดึงคนเข้า).

### Pre-live caption components
ต้องมีครบ 5 อย่าง อย่าขาด:
1. **วันเวลา** — ระบุชัด ๆ "วันนี้ 2 ทุ่ม" / "พรุ่งนี้ 20:00 น." (ไทยใช้ 24 ชม. ได้ แต่ภาษาพูดนิยม "2 ทุ่ม / 3 ทุ่ม")
2. **แม่ค้า/แขกรับเชิญ** — เรียก "แม่ค้า", "พี่ + ชื่อเล่น", "น้อง + ชื่อเล่น" เช่น "พี่แนน", "น้องมิ้น", "แม่ค้าก้อย"
3. **สินค้า/หมวด** — "เสื้อผ้าแฟชั่นเกาหลี", "ครีมหน้าใส", "ปลาทูเค็มสูตรแม่"
4. **Hook** — "โปรเด็ด / ลดสุดในไลฟ์ / ของแถมเพียบ / ราคาไลฟ์เท่านั้น / ลดเพิ่ม 50% ในไลฟ์"
5. **CTA** — "กดติดตาม / เปิดแจ้งเตือน / set notification / กดกระดิ่ง / รอเจอกันนะคะ"

### During-live updates
สั้น เร่งด่วน เน้น scarcity + urgency:
- "เหลือ 5 ตัวสุดท้าย!! 🔥"
- "Code ลดเพิ่ม 50.- รับช่วงไลฟ์เท่านั้น พิมพ์ในแชทเลยค่ะ"
- "พี่แนนแถมให้อีก 1 ชิ้น เฉพาะ 10 คนแรก! 🎁"
- "ตัวนี้หมดแล้วค่า ไปดูตัวต่อไปกัน"

### Platform differences

| Platform | Audience | Pace | Caption style |
|---|---|---|---|
| **Shopee Live** | ช้อปปิ้งมินเดด, อายุ 20–40 | ปานกลาง | เน้น product card, pin โค้ดในแชท, รหัสสินค้าชัด |
| **TikTok Live** | วัยรุ่น–วัยทำงานต้น, urban | เร็วมาก | trendy slang OK (ตำ/ปัง/จัดเลย), gamified |
| **FB Live** | อายุ 30+, ต่างจังหวัด, แม่บ้าน | ช้ากว่า | อธิบายสินค้าละเอียด, รีวิวเชิงลึก, comment-driven |
| **IG Live** | urban young, แฟชั่น/บิวตี้ | ปานกลาง | TH-EN mix, aesthetic, brand-led |

**Example 1 — pre-live Shopee Live (เสื้อผ้า):**
"📣 ไลฟ์ใหญ่คืนนี้!! 2 ทุ่มตรง 🛍️ / พี่แนนยกคลังเสื้อผ้าเกาหลีมาไลฟ์ ลดสุดในรอบเดือน / เดรส เสื้อ กางเกง เริ่ม 99.- เท่านั้น / โค้ดลดเพิ่ม 50.- เฉพาะในไลฟ์ พิมพ์ NANLIVE / ของแถมเพียบ มีลุ้นรับกระเป๋าฟรี 5 ใบ / กดติดตามร้าน + เปิดแจ้งเตือน รอเจอกันนะคะ 🔔
#ShopeeLive #เสื้อผ้าเกาหลี #ไลฟ์สดShopee"

**Example 2 — pre-live TikTok Live (อาหารทะเลแห้ง):**
"ไลฟ์คืนนี้ 3 ทุ่ม จัดเต็ม! 🦐🔥 / แม่ค้าก้อยยกกุ้งแห้งสด ๆ จากระนองมาไลฟ์ / ราคาไลฟ์ลดสุด ถูกกว่าตลาด 30% / ของแถมจัดเต็ม สั่งครบ 500 แถมปลาหมึกแห้ง 1 ขีด / กดติดตาม + กดกระดิ่งรอเลยจ้าาาา ตำกันให้หนัก!
#tiktoklive #ของกินมาแรง #กุ้งแห้งระนอง #fyp"

## Common mistakes
- Literal translation of marketing English: "พวกเราตื่นเต้นที่จะประกาศ" → use "ขอประกาศ" หรือ "มาแล้วจ้า"
- Too many CTAs in one post (pick ONE action).
- Wrong register for platform: Facebook caption written in TikTok tone reads juvenile; TikTok caption written like Facebook reads boring.
- Hashtag spam on Facebook (kills reach).
- Brand account using กู/มึง without clear meme-account positioning.
- Forgetting platform character limits (X clips at 280; Threads at 500).
- Using only English hashtags for a Thai-only audience product.
- Emoji overload (>5 emojis per short caption looks desperate).
- Posting TikTok-style captions on LINE Voom — wrong audience (Voom skews older/family, slang and ironic humor flop).
- Pre-live captions without a clear วันเวลา / countdown — viewers won't know when to come back; always pin time + ทุ่ม format.
- Calling it "LINE Timeline" — rebranded to LINE Voom in 2022; using the old name signals outdated knowledge.
- Forgetting CTA to "เปิดแจ้งเตือน / กดกระดิ่ง" on pre-live posts — follow alone doesn't push notifications when the stream starts.
