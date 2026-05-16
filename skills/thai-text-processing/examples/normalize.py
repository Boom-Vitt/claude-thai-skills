"""Thai Unicode normalization, grapheme-safe truncation, and romanization.

Install:
    pip install regex pythainlp

References (verify against current docs):
    https://docs.python.org/3/library/unicodedata.html
    https://pypi.org/project/regex/  (provides \\X grapheme cluster matcher)
    https://pythainlp.org/docs/  (transliterate.romanize)
"""

from __future__ import annotations

import unicodedata


# ---------- 1. NFC normalization ----------
def normalize_nfc(s: str) -> str:
    """Canonically compose. Always do this before storing / comparing."""
    return unicodedata.normalize("NFC", s)


def equal_after_normalize(a: str, b: str) -> bool:
    return normalize_nfc(a) == normalize_nfc(b)


# ---------- 2. Grapheme-safe length & truncation ----------
def grapheme_clusters(s: str) -> list[str]:
    """Split into user-perceived characters.

    Uses the `regex` library (not stdlib `re`) for \\X support.
    """
    import regex  # pip install regex

    return regex.findall(r"\X", s)


def grapheme_len(s: str) -> int:
    """How many user-visible characters."""
    return len(grapheme_clusters(s))


def truncate_graphemes(s: str, max_chars: int, ellipsis: str = "…") -> str:
    """Truncate without splitting a grapheme cluster (no orphaned tone marks)."""
    clusters = grapheme_clusters(s)
    if len(clusters) <= max_chars:
        return s
    return "".join(clusters[:max_chars]) + ellipsis


def truncate_at_word_boundary(s: str, max_chars: int, ellipsis: str = "…") -> str:
    """Truncate at a Thai word boundary so we don't cut mid-syllable.

    Strategy: segment, then greedily accumulate words until we'd exceed max_chars
    (measured in graphemes), then add ellipsis.
    """
    # verify against current PyThaiNLP docs
    from pythainlp.tokenize import word_tokenize

    tokens = word_tokenize(s, engine="newmm")
    out: list[str] = []
    running = 0
    for tok in tokens:
        tok_len = grapheme_len(tok)
        if running + tok_len > max_chars:
            break
        out.append(tok)
        running += tok_len
    truncated = "".join(out)
    return truncated + ellipsis if truncated != s else s


# ---------- 3. Romanization (RTGS) ----------
def romanize_rtgs(text: str) -> str:
    """Royal Thai General System of Transcription, via PyThaiNLP `royin` engine.

    Note: drops tone and vowel length. For SEO slugs / passport-style spelling.
    Verify the exact engine name against current PyThaiNLP docs — earlier
    versions used "royin", newer versions also accept "thai2rom" (neural).
    """
    from pythainlp.transliterate import romanize

    return romanize(text, engine="royin")


def slugify_thai(text: str) -> str:
    """Make a URL slug from Thai. RTGS → lowercase → keep [a-z0-9-]."""
    import re

    roman = romanize_rtgs(text).lower()
    # collapse whitespace to hyphen, drop anything else
    roman = re.sub(r"\s+", "-", roman)
    roman = re.sub(r"[^a-z0-9-]", "", roman)
    return re.sub(r"-+", "-", roman).strip("-")


# ---------- self-tests ----------
if __name__ == "__main__":
    # 1. NFC normalization
    print("== NFC normalization ==")
    a = "แสง"  # may be precomposed
    b = unicodedata.normalize("NFD", a)  # explicitly decomposed
    print(f"a == b (raw)            : {a == b}")
    print(f"after NFC normalization : {equal_after_normalize(a, b)}")
    print(f"codepoints a (NFD)      : {[hex(ord(c)) for c in unicodedata.normalize('NFD', a)]}")
    print(f"codepoints a (NFC)      : {[hex(ord(c)) for c in unicodedata.normalize('NFC', a)]}")
    print()

    # 2. Grapheme vs codepoint length
    print("== length: codepoints vs graphemes ==")
    word = "ก่อน"  # base + lower tone? + leading vowel pattern
    print(f"text                : {word!r}")
    print(f"len() (codepoints)  : {len(word)}")
    try:
        print(f"grapheme_len()      : {grapheme_len(word)}")
    except ImportError:
        print("grapheme_len()      : (skipped — pip install regex)")
    print()

    # 3. Grapheme-safe truncation
    print("== grapheme-safe truncation ==")
    long_text = "ฉันกินข้าวที่ร้านอาหารญี่ปุ่นเมื่อวานนี้และมันอร่อยมาก"
    try:
        print(f"truncate_graphemes(20) : {truncate_graphemes(long_text, 20)!r}")
    except ImportError:
        print("(skipped — pip install regex)")
    try:
        print(f"truncate_at_word_boundary(20) : {truncate_at_word_boundary(long_text, 20)!r}")
    except ImportError:
        print("(skipped — pip install regex pythainlp)")
    print()

    # 4. Romanization
    print("== RTGS romanization ==")
    for sample in ["สวัสดี", "ขอบคุณ", "ประเทศไทย", "กรุงเทพมหานคร"]:
        try:
            print(f"{sample!r} → {romanize_rtgs(sample)!r}")
        except ImportError:
            print("(skipped — pip install pythainlp)")
            break
    print()

    # 5. Slug
    print("== slugify ==")
    try:
        print(f"slugify_thai('ประเทศไทย น่าอยู่') → {slugify_thai('ประเทศไทย น่าอยู่')!r}")
    except ImportError:
        print("(skipped — pip install pythainlp)")
