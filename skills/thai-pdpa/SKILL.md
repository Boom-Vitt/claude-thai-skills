---
name: thai-pdpa
description: Use this skill for tasks involving Thailand's PDPA (พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562). Trigger whenever the user asks to: draft a Thai privacy notice, write a PDPA consent banner, prepare a data subject rights notice, draft a 72-hour breach notification to the PDPC, decide if a DPO is required, list lawful bases, handle cross-border transfers, or audit a notice against PDPA. Also trigger for "เขียน privacy policy", "PDPA", "ขอความยินยอม", "นโยบายความเป็นส่วนตัว", "consent banner ไทย", "Thai privacy notice", "PDPA compliance", "DPO Thailand", "ประกาศการละเมิดข้อมูล", or any variation. If the task involves Thai personal data law, consent, or notice drafting, use this skill.
---

# PDPA ไทย (Thailand Personal Data Protection Act drafting)

## Overview
พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA, effective 1 June 2022) ใกล้เคียงกับ GDPR แต่ไม่เหมือนกัน. Copy-pasting a GDPR notice into Thai is the #1 reason notices fail audits — references to "Article 6 GDPR" make the notice non-compliant on its face. Always re-anchor citations to PDPA sections.

## When to use
- ร่างนโยบายความเป็นส่วนตัว (privacy notice) สำหรับเว็บไซต์ / แอป
- ออกแบบ cookie / consent banner ที่ผ่านเกณฑ์ PDPA
- ร่างหนังสือแจ้งสิทธิ์เจ้าของข้อมูล (data subject rights notice)
- แจ้งเหตุการละเมิดข้อมูล (data breach notification) ภายใน 72 ชั่วโมงต่อ PDPC
- ประเมินว่าต้องแต่งตั้ง DPO หรือไม่
- ตรวจสอบ template ที่แปลมาจาก GDPR ว่าใช้ได้กับ PDPA หรือไม่

## PDPA vs GDPR — what changes when drafting

| Topic | GDPR | PDPA (พ.ร.บ.) |
|---|---|---|
| Consent | Opt-in, freely given | Opt-in, freely given (Sec 19); no pre-checked boxes |
| Reject button | Recommended | **Required equal-weight** under PDPC consent guidance |
| Breach notice to regulator | 72h to DPA | **72h to PDPC** (Sec 37) |
| Subject rights | 8 rights | Same 8 rights (Sec 30–36): access, rectify, erase, restrict, port, object, withdraw, complain |
| DPO trigger | Large-scale systematic monitoring or special-category data | Same trigger + state agencies (Sec 41) |
| Cross-border | Adequacy or safeguards | Adequacy or safeguards; PDPC keeps adequacy list (Sec 28) |
| Sensitive data | Art 9 categories | Sec 26: race, ethnicity, political opinion, religion/philosophy, sexual behavior, criminal record, health, disability, trade union, genetic, biometric, others as prescribed |
| Penalties | Up to 4% global turnover | Admin fines up to ฿5M; criminal up to ฿1M + 1 yr imprisonment; civil punitive up to 2x damages |

## Required elements of a privacy notice (Section 23)
A compliant Thai notice must state, in plain Thai:
1. **วัตถุประสงค์** — Purpose for each item collected (itemized, not lumped)
2. **ฐานทางกฎหมาย** — Lawful basis (consent / contract / legal obligation / vital interest / public task / legitimate interest)
3. **ประเภทข้อมูล** — Categories of personal data processed
4. **ระยะเวลาเก็บรักษา** — Retention period (or criteria to determine it)
5. **ผู้รับข้อมูล** — Recipients / categories (including processors, group companies, third parties)
6. **การส่งข้อมูลข้ามประเทศ** — Cross-border transfer info: destination countries, safeguards (SCC-equivalent, BCR, adequacy)
7. **สิทธิ์ของเจ้าของข้อมูล** — All 8 data subject rights + how to exercise
8. **ผู้ควบคุมข้อมูล / DPO** — Controller identity, address, DPO contact
9. **สิทธิ์ในการร้องเรียน** — Right to complain to PDPC (สำนักงานคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล)
10. **ผลของการไม่ให้ข้อมูล** — Consequences of refusing (where data is required by contract or law)

See `templates/privacy-notice-th.md` for the full bilingual skeleton.

## Consent banner rules (Section 19 + PDPC consent guidance)
- **Pre-checked boxes are invalid** — every non-essential category starts off
- **"ยอมรับทั้งหมด" and "ปฏิเสธทั้งหมด" must be equally prominent** — same colour, same size, same depth in navigation. "Reject all" cannot be hidden behind a "Manage preferences" wall.
- **Granular consent** — at minimum: necessary / analytics / marketing / personalization. Necessary cookies don't need consent but must still be disclosed.
- **Withdrawal as easy as giving** — provide a "Cookie preferences" link in the footer that re-opens the banner.
- **No "implied consent by continuing to use the site"** — explicitly invalid under PDPA.

See `templates/consent-banner.md` for the HTML mockup and Thai copy.

## Breach notification (Section 37)
Notify the PDPC within **72 hours** of becoming aware, unless the breach is unlikely to result in risk to rights and freedoms. Notify affected data subjects **without undue delay** if high risk. Include:
- Nature of the breach (what happened, when, attack vector)
- Categories and approximate number of subjects + records
- Categories of personal data affected
- Likely consequences for subjects
- Measures taken and proposed (containment, remediation, notification plan)
- DPO / contact point

## DPO appointment triggers (Section 41)
Required when:
- Core activity = regular and systematic monitoring of data subjects on a large scale (e.g. ad-tech, ride-hailing, loyalty program at scale)
- Core activity = large-scale processing of sensitive data under Sec 26 (e.g. hospitals, HR for tens of thousands of employees)
- The controller / processor is a state agency
- Other criteria prescribed by PDPC sub-notification (check current PDPC notifications)

The DPO must report directly to top management, cannot have a conflict of interest, and their contact must be published in the notice.

## Penalties cheat sheet
- Administrative fines: up to ฿5,000,000 per violation for serious breaches (no-consent processing, unlawful sensitive-data processing, illegal cross-border transfer)
- Criminal: up to ฿1,000,000 and/or 1 year imprisonment for unauthorized disclosure of sensitive data for personal benefit
- Civil: actual damages + punitive damages up to 2× actual damages

## Common mistakes
- **Translated GDPR template** — leaves "Art. 6 / Art. 9 GDPR" references; re-cite to Sec 24 / Sec 26 PDPA
- **"By continuing to browse, you consent..."** — invalid; PDPA needs explicit affirmative action
- **Hiding "Reject all"** — direct Sec 19 violation
- **English-only notice on a Thai-targeted site** — PDPC guidance: Thai must be primary; English may be secondary
- **Missing cross-border disclosure** when using Cloudflare / AWS us-east / GCP — these are transfers outside Thailand and must be listed with safeguards
- **"We keep data forever"** — must specify period or determining criteria
- **Treating IP / cookie ID / device ID as non-personal** — PDPA includes them as personal data (Sec 6)
- **No DPO contact in notice** even when DPO is required — Sec 41(3) requires publication
- **Bundling marketing consent with terms acceptance** — Sec 19(4) bars bundled consent for unrelated purposes
- **Forgetting children's data special treatment** — under 10 needs parental consent (Sec 20); 10–20 depends on capacity
