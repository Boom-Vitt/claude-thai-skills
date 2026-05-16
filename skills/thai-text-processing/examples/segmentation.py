"""Thai word segmentation — runnable examples.

Install:
    pip install pythainlp

References (verify against current PyThaiNLP docs):
    https://pythainlp.org/docs/
    pythainlp.tokenize.word_tokenize(text, engine="newmm", custom_dict=None, keep_whitespace=True)
"""

from __future__ import annotations


def naive_split(text: str) -> list[str]:
    """The wrong way. Returns one mega-token because Thai has no spaces."""
    return text.split(" ")


def segment_newmm(text: str) -> list[str]:
    """Dictionary-based segmentation. Fast, good default."""
    # verify against current PyThaiNLP docs
    from pythainlp.tokenize import word_tokenize

    return word_tokenize(text, engine="newmm")


def segment_attacut(text: str) -> list[str]:
    """CNN-based segmentation. Slower, higher recall on out-of-vocabulary words.

    Requires `pip install pythainlp[attacut]` or `pip install attacut`.
    """
    from pythainlp.tokenize import word_tokenize

    return word_tokenize(text, engine="attacut")


def segment_with_custom_dict(text: str, extra_words: list[str]) -> list[str]:
    """Add domain-specific words (product names, jargon) to the dictionary.

    Useful when the default dict over-segments brand names, e.g. "แกร็บฟู้ด" → "แกร็บ" + "ฟู้ด".
    """
    # verify against current PyThaiNLP docs — Trie import path occasionally changes
    from pythainlp.tokenize import word_tokenize
    from pythainlp.util import Trie
    from pythainlp.corpus.common import thai_words

    custom = set(thai_words()) | set(extra_words)
    trie = Trie(custom)
    return word_tokenize(text, engine="newmm", custom_dict=trie)


def count_words(text: str) -> int:
    """Word count that actually works for Thai."""
    return len([t for t in segment_newmm(text) if t.strip()])


# ---------- self-tests ----------
if __name__ == "__main__":
    sample = "ฉันกินข้าวที่ร้านอาหารญี่ปุ่นเมื่อวานนี้"

    print("== Input ==")
    print(sample)
    print()

    print("== naive .split(' ') ==")
    naive = naive_split(sample)
    print(f"tokens: {naive}")
    print(f"count : {len(naive)}  ← wrong, always 1 for unspaced Thai")
    print()

    print("== PyThaiNLP newmm ==")
    try:
        tokens = segment_newmm(sample)
        print(f"tokens: {tokens}")
        print(f"count : {count_words(sample)}")
    except ImportError:
        print("(skipped — pip install pythainlp)")
    print()

    print("== custom dictionary (adds 'ร้านอาหารญี่ปุ่น' as single token) ==")
    try:
        tokens = segment_with_custom_dict(sample, ["ร้านอาหารญี่ปุ่น"])
        print(f"tokens: {tokens}")
    except ImportError:
        print("(skipped — pip install pythainlp)")
    print()

    print("== brand-name example (attacut handles novel words better than newmm) ==")
    brand_sample = "สั่งแกร็บฟู้ดจากแอปได้เลย"
    try:
        print(f"newmm   : {segment_newmm(brand_sample)}")
        print(f"attacut : {segment_attacut(brand_sample)}")
    except ImportError as e:
        print(f"(skipped — {e})")
