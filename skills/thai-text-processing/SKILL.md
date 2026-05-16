---
name: thai-text-processing
description: Use this skill for any task involving Thai text in code — word segmentation, Unicode normalization, sorting/collation, search indexing, romanization, truncation, or database/Elasticsearch configuration for Thai. Trigger whenever the user asks to: tokenize / segment Thai (no spaces between words), normalize Thai text (NFC vs decomposed), sort Thai strings correctly, transliterate to roman / Latin, build a Thai search index, fix Thai text that breaks length limits or renders broken glyphs, or pick a Thai NLP library. Also trigger for requests like "ตัดคำภาษาไทย", "Thai word segmentation", "Thai NLP", "ค้นหาภาษาไทย", "Thai romanization", "PyThaiNLP", "Thai sort", "ICU Thai", "Thai collation", "Thai search index", "Thai full text search", or any variation. If the task involves processing Thai text in software, use this skill.
---

# Thai Text Processing (ประมวลผลข้อความภาษาไทยในโค้ด)

## Overview
Thai is written without spaces between words, uses combining tone marks, and does not sort by codepoint. Naive code that works for English silently corrupts Thai: `"ฉันกินข้าว".split(" ")` returns one token, `ORDER BY name` puts vowels in the wrong place, and `LEFT(name, 20)` may chop a syllable mid-character and render `◌`. This skill is the checklist of things to fix.

## When to use
- ตัดคำภาษาไทย (segmentation) สำหรับ search, autocomplete, n-grams
- Unicode normalization (NFC) ก่อนเก็บ / เทียบสตริง
- จัดเรียง (sort / collate) ชื่อภาษาไทยใน DB หรือ list
- ทำ romanization สำหรับ slug, passport-style spelling, academic citation
- ตั้งค่า full-text search index ใน ES / Postgres / MySQL
- ตัดข้อความ (truncate) แบบไม่ทำให้ glyph แตก
- เลือกไลบรารี: PyThaiNLP vs ICU vs nlpO3 vs Lucene Thai analyzer

## 1. The core problem: no spaces

```python
"ฉันกินข้าว".split(" ")  # ["ฉันกินข้าว"]  ← one mega-token
```

This breaks:
- full-text search (`ILIKE '%กิน%'` mostly works, `ILIKE '%ข้าว%'` mostly works, but ranking, stemming, autocomplete all need proper tokens)
- word counting / "how long is this in words"
- text wrap / hyphenation
- n-gram features for ML
- highlight-on-search snippets

You **must** run a segmenter before any token-based operation.

## 2. Word segmentation toolkit

| Tool | Language | Notes |
|---|---|---|
| **PyThaiNLP** `word_tokenize` | Python | De-facto default. Engines: `newmm` (default, dict-based), `longest`, `attacut` (CNN), `deepcut` (LSTM, slow but accurate) |
| **nlpO3** | Python via Rust | Fast newmm-style; permissive license |
| **ICU `BreakIterator`** | C / Java / Python (`pyicu`) | Built into many platforms; decent for word-break |
| **thai-segmenter** | TypeScript | Browser-friendly; dictionary-based |
| **Lucene Thai analyzer** | Java | Use for Elasticsearch / OpenSearch indexing |
| **SentencePiece / BPE** | Any | For ML training; not for human-facing tokens |

Picking rules of thumb:
- **Server Python:** PyThaiNLP `newmm` (good enough, fast, MIT)
- **Need higher recall on OOV / colloquial:** `attacut` or `deepcut` (slower)
- **Frontend JS:** `thai-segmenter` or call ICU via WebAssembly
- **Search index:** dedicated Thai analyzer in ES (`thai` tokenizer) — do not segment client-side and ship tokens to ES
- **Production at scale:** nlpO3 for raw throughput

See `examples/segmentation.py` for runnable code.

## 3. Unicode normalization (NFC)

Thai displays one "visual character" out of up to **3 codepoints**: base consonant + above-vowel + tone mark. The same word can be encoded multiple ways:

```python
import unicodedata
a = "แสง"                              # may be precomposed
b = unicodedata.normalize("NFD", a)    # explicitly decomposed
a == b                                  # False
unicodedata.normalize("NFC", a) == unicodedata.normalize("NFC", b)  # True
```

**Rules:**
- Always normalize to **NFC** before storing or comparing.
- Database column: pre-normalize in application, OR use a generated column / trigger.
- "Length in user-visible characters" = grapheme clusters, not codepoints. Use `regex` library `\X` (Python) or `Intl.Segmenter("th", {granularity: "grapheme"})` (JS).
- `len("ก่")` in Python returns 2 (codepoints) — but the user sees 1 character.

See `examples/normalize.py`.

## 4. Romanization standards

| System | Use case | Lossless? | Example: สวัสดี |
|---|---|---|---|
| **RTGS** (Royal Thai General System) | Signs, passports, SEO slugs | No (drops tone, vowel length) | `sawatdi` |
| **ISO 11940** | Academic, archives | Yes (one-to-one, ugly) | `s̄wạs̄dī` |
| **ISO 11940-2** | Phonetic, prettier | No | `sawatdi` |
| **IPA** | Phonetic transcription | Approximate | `/sā.wàt.dīː/` |

Use **RTGS** for slugs and English-readable transliteration of names. PyThaiNLP exposes `pythainlp.transliterate.romanize(text, engine="royin")` for RTGS-style output. For deterministic batch slugs, also strip non-`[a-z0-9-]` after romanization.

## 5. Sorting / collation

Thai does NOT sort by codepoint. The traditional rule: sort by **base consonant** first, then **vowel**, then **tone mark**. Codepoint sort puts leading vowels (`เ`, `แ`, `โ`, `ใ`, `ไ`) AFTER consonants, which is wrong.

| Place | How |
|---|---|
| PostgreSQL (ICU build) | `name TEXT COLLATE "th-TH-x-icu"` |
| MySQL 8 | `COLLATE utf8mb4_thai_520_w2` (Unicode 5.20, weights v2) |
| Python (no DB) | `pyicu` Collator with `Locale("th_TH")`, or PyThaiNLP's `thai_strftime`/`collate` |
| JavaScript | `Intl.Collator("th", {sensitivity: "base"})` |
| Elasticsearch | `icu_collation_keyword` field with `language: "th"` |

```sql
-- PostgreSQL example
CREATE COLLATION thai_icu (provider = icu, locale = 'th-TH');
SELECT name FROM users ORDER BY name COLLATE "th-TH-x-icu";
```

Default UTF-8 / binary sort is wrong — verify by sorting `["แอน","กิน","โต","ไกล"]` and confirming Thai dictionary order, not codepoint order.

## 6. Truncation safety

Truncating mid-character (codepoint vs grapheme) can leave dangling combining marks rendered as `◌`. Rules:

- **Truncate at grapheme cluster boundary.** Python: `regex` library `\X`. JS: `Intl.Segmenter` with `granularity: "grapheme"`.
- For UI ellipsis (e.g. "show first 30 chars + …"), first segment by word using PyThaiNLP, then count graphemes, then append `…` — don't cut mid-syllable.
- Database `VARCHAR(50)` counts **bytes** in some collations and **characters** in others. Test before assuming "50 chars" matches user perception.

See `examples/normalize.py` for grapheme-safe truncation.

## 7. Database / Elasticsearch indexing

**Elasticsearch / OpenSearch:**
```json
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "thai",
        "search_analyzer": "thai"
      }
    }
  }
}
```

**PostgreSQL full-text:** the bundled `tsvector` configs don't ship a Thai dictionary. Options:
- Segment in application using PyThaiNLP, store space-separated tokens in a `tsvector` column with `simple` config
- Use `pg_search` / `paradedb` with a Thai tokenizer
- Use a sidecar Elasticsearch

**Don't rely on `ILIKE '%term%'`.** Without segmentation it does substring match — works for very short queries, fails for multi-word, misses synonyms, can't rank.

## Common mistakes

- `.split(" ")` to count Thai words → always returns 1 — use a segmenter
- `ORDER BY name` without collation → vowels and tone marks in codepoint order, not dictionary order
- Storing un-normalized text → `WHERE name = 'แสง'` misses rows that were saved decomposed
- `LEFT(text, 20)` for "first 20 chars" → counts bytes or codepoints, not graphemes; renders `◌`
- "Username max 20 chars" enforced by codepoint count → users can submit 60-byte usernames with combining marks
- Using RTGS for accurate phonetic transcription → it drops tone and vowel length; use IPA
- Shipping client-segmented tokens to Elasticsearch → bypasses the analyzer; mismatched query-time tokenization
- Treating "ๆ" (mai-yamok, repetition mark) as a separate word → it's an in-word marker; PyThaiNLP handles it correctly, `.split()` doesn't
- Forgetting that `​` (zero-width space, U+200B) is sometimes injected by CMSs for word break hints — strip on input or normalize
