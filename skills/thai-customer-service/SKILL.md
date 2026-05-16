---
name: thai-customer-service
description: Use this skill for any task involving Thai customer service messaging — replies, apologies, status updates, refund/return scripts, and auto-replies on LINE OA, Facebook Page, Shopee, Lazada, Instagram DM, TikTok Shop, and similar channels. Trigger whenever the user asks to: reply to a Thai customer, draft an apology, write a refund or return message, write an auto-reply, de-escalate an angry customer, or send a shipping/status update in Thai. Also trigger for requests like "ตอบลูกค้า", "reply LINE OA", "ตอบแชท", "Shopee reply", "ข้อความขอโทษลูกค้า", "customer service Thai", "เขียน auto reply", "ตอบ inbox", or any variation. If the output is a Thai message from a business to a customer, use this skill.
---

# ตอบลูกค้า (Thai Customer Service Replies)

## Overview
การตอบลูกค้าไทยต้องอ่อนน้อม รวดเร็ว และใช้สรรพนามให้ถูกต้องตามอายุ/ความสัมพันธ์. Thai CS is conversational politeness layered on transactional speed — every reply needs a particle (ค่ะ/ครับ), a clear next step, and zero defensiveness even when the customer is wrong.

## When to use
- ตอบแชท LINE OA, Facebook Page Inbox, IG DM
- ตอบคำถามใน Shopee, Lazada, TikTok Shop
- เขียนข้อความขอโทษ คืนเงิน เปลี่ยนสินค้า
- เขียน auto-reply / canned responses
- ตอบลูกค้าโมโห หรือ complaint

## Core conventions

### 1. Opener templates by channel

| Channel | Opener |
|---|---|
| LINE OA | "สวัสดีค่ะ ขอบคุณที่ทักมาที่ [ร้าน X] นะคะ 🙏 รบกวนแจ้ง…" |
| Facebook Page | "สวัสดีค่ะคุณลูกค้า ขอบคุณที่สนใจสินค้าของเรานะคะ…" |
| IG DM | "สวัสดีค่ะ ทางร้านได้รับข้อความแล้วนะคะ 😊…" |
| Shopee/Lazada | "สวัสดีค่ะ ขอบคุณที่สั่งซื้อสินค้าจากร้านเรานะคะ คำสั่งซื้อ #… กำลัง…" |
| TikTok Shop | "สวัสดีค่ะ ทางร้านได้รับคำสั่งซื้อแล้วนะคะ…" |
| Auto-reply (off hours) | "ขอบคุณที่ติดต่อร้าน [X] ค่ะ ขณะนี้นอกเวลาทำการ ทีมงานจะรีบตอบกลับใน [เวลา] นะคะ 🙏" |

### 2. Pronouns

| Pronoun | Use when |
|---|---|
| คุณลูกค้า | safe default, unknown age/gender |
| พี่ | customer visibly older (profile, name) |
| น้อง | customer visibly younger |
| คุณ + ชื่อ | when name is known, polite default |
| เรา / ทางร้าน / ทางบริษัท / แอดมิน | "we" — pick one and stick with it |

Rule: do NOT switch pronouns mid-conversation. Pick once per thread.

### 3. Apology ladder (escalating)
- **Minor (delayed reply, small confusion):**
  "ขออภัยในความไม่สะดวกค่ะ 🙏"
- **Moderate (wrong item, late shipment, unmet expectation):**
  "ขอโทษอย่างสูงที่ทำให้คุณลูกค้ารู้สึกไม่ประทับใจค่ะ ทางร้านจะรีบตรวจสอบและแก้ไขให้นะคะ"
- **Major (damaged item, repeated failure, public complaint):**
  "ทางร้านขอแสดงความเสียใจอย่างยิ่งสำหรับสิ่งที่เกิดขึ้นค่ะ ขอรับเรื่องและจะดำเนินการแก้ไขให้คุณลูกค้าโดยด่วนภายใน [เวลา] นะคะ 🙏"

### 4. Status / update phrases
- "กำลังตรวจสอบให้ค่ะ รบกวนรอสักครู่นะคะ"
- "ทางร้านขอเช็คกับฝ่าย [คลัง/ขนส่ง] ก่อน แล้วจะแจ้งกลับภายใน [เวลา] ค่ะ"
- "คำสั่งซื้อจัดส่งเรียบร้อยแล้วค่ะ เลขพัสดุ [tracking] ขนส่ง [Kerry/Flash/J&T] ค่ะ"
- "สินค้าหมดสต็อกค่ะ คาดว่าจะเข้าใหม่ประมาณ [date] รบกวนรอนะคะ 🙏"
- "ได้รับข้อมูลแล้วนะคะ ทางร้านขอเวลา [X] นาที·ชั่วโมงในการตรวจสอบค่ะ"

### 5. Refund / return scripts

**Refund approved:**
"ทางร้านตรวจสอบเรียบร้อยแล้วค่ะ ยินดีคืนเงินให้คุณลูกค้านะคะ 🙏 / รบกวนแจ้งเลขบัญชี ชื่อบัญชี และธนาคาร เพื่อโอนคืนภายใน [X] วันทำการค่ะ"

**Refund denied (with policy):**
"ทางร้านขออภัยนะคะ 🙏 กรณีนี้ไม่เข้าเงื่อนไขการคืนเงินตามนโยบายร้าน (ข้อ [X]: [reason]) แต่ทางเรายินดี[เสนอ exchange / store credit / ส่วนลด] ให้คุณลูกค้าแทนนะคะ"

**Exchange offered:**
"ทางร้านยินดีเปลี่ยนสินค้าให้นะคะ 😊 รบกวนส่งสินค้าเดิมกลับมาที่ [ที่อยู่] พร้อมแนบใบเสร็จ ทางร้านจะจัดส่งใหม่ให้ภายใน [X] วันทำการค่ะ"

### 6. De-escalation (angry customer)
- "เข้าใจความรู้สึกของคุณลูกค้าเลยค่ะ 🙏"
- "ทางร้านรับฟังและจะดูแลให้ที่สุดนะคะ"
- "ขอเวลาตรวจสอบให้ละเอียดอีกครั้งค่ะ จะรีบแจ้งกลับโดยด่วน"
- "ขอบคุณที่แจ้งให้ทางร้านทราบนะคะ เพื่อจะได้ปรับปรุงต่อไป"
- ห้ามใช้: "ก็บอกแล้วไง" "อ่านเงื่อนไขให้ดี" "ไม่ใช่ความผิดร้าน" — defensive = ดราม่าทันที

### 7. Tone rules
- ใส่ ค่ะ·ครับ ทุกประโยคหรือเกือบทุกประโยค (chat ≠ email — particle หนาแน่นกว่า)
- 🙏 = ขอโทษ / ขอบคุณ / ขอความเข้าใจ (เครื่องมือ deescalate ที่ดีที่สุด)
- 😊 ใช้ในบริบทเป็นมิตร, ไม่ใช้กับลูกค้าโกรธ
- ห้ามใช้ 🤣 555 กู มึง กับลูกค้าทุกกรณี (แม้บน TikTok Shop)
- ปิดประโยคด้วย "นะคะ·นะครับ" ช่วยลด tone ห้วน
- ลูกค้าโกรธ → ตอบสั้น ชัด เห็นใจก่อน solution ทีหลัง

## Examples

**INPUT:** Customer angry: "สั่งมา 5 วันแล้วยังไม่ได้ของ!!" (LINE OA)
**OUTPUT:**
"สวัสดีค่ะคุณลูกค้า ขออภัยอย่างสูงที่ของล่าช้านะคะ 🙏 / เข้าใจความรู้สึกของคุณลูกค้าเลยค่ะ / ทางร้านขอเลขคำสั่งซื้อ เพื่อตรวจสอบกับขนส่งให้โดยด่วนนะคะ / จะรีบแจ้งกลับภายใน 30 นาทีค่ะ"

**INPUT:** Customer asks: "สีนี้มีไซส์ XL มั้ยคะ" (IG DM)
**OUTPUT:**
"สวัสดีค่ะ ขอบคุณที่สนใจสินค้านะคะ 😊 / สีนี้ไซส์ XL ยังมีอยู่ค่ะ เหลือ 3 ตัวนะคะ / สนใจสั่งเลยทักได้เลยค่ะ"

**INPUT:** After-hours auto-reply for a café Facebook page.
**OUTPUT:**
"ขอบคุณที่ทักมาที่ [ร้าน X] ค่ะ 🙏 / ขณะนี้นอกเวลาทำการ (10:00–20:00) / ทีมงานจะรีบตอบกลับโดยเร็วที่สุดในเวลาทำการนะคะ 😊"

**INPUT:** Refund denied — customer wants return after 30 days (policy: 7 days).
**OUTPUT:**
"สวัสดีค่ะคุณลูกค้า ทางร้านขออภัยนะคะ 🙏 / กรณีนี้เกินระยะเวลาคืนสินค้าตามนโยบายร้าน (ภายใน 7 วันหลังได้รับสินค้า) / แต่ทางร้านยินดีมอบส่วนลด 15% สำหรับการสั่งครั้งถัดไปให้คุณลูกค้าแทนนะคะ / ขอบคุณที่เข้าใจค่ะ 😊"

## Common mistakes
- ลืม ค่ะ·ครับ → อ่านห้วน เหมือนหุ่นยนต์
- ใช้ "ลูกค้า" ห้วนๆ แทน "คุณลูกค้า"
- ตอบยาวเกินไปสำหรับ chat (ลูกค้า scroll)
- ขึ้นต้นด้วย "ไม่ใช่ความผิดของร้าน" → ดราม่าแน่นอน
- ใช้ 🤣 หรือ 555 ตอบลูกค้า complaint
- เปลี่ยนสรรพนามกลางบทสนทนา (พี่ → คุณ → ลูกค้า สับสน)
- Copy-paste auto-reply ที่ไม่ตอบคำถามจริง → ลูกค้ายิ่งโมโห
- ใช้ "นะ" เฉยๆ ไม่มี ค่ะ → ดูกันเองเกินไป
- สัญญาเวลาเกินจริง ("ตอบกลับใน 5 นาที") แล้วทำไม่ได้ → trust ตก
- ปิดด้วย "ขอบคุณค่ะ" อย่างเดียวเมื่อลูกค้ายังโกรธ → ใช้ "ขอบคุณที่แจ้งให้ทราบนะคะ ทางร้านจะปรับปรุงต่อไปค่ะ 🙏" แทน
