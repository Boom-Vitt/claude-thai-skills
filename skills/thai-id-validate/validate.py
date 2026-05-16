"""Thai national ID, tax ID, phone normalization, and PromptPay QR utilities.

Run self-tests:
    python validate.py
"""
from __future__ import annotations

import re
from typing import Optional


# ---------------------------------------------------------------------------
# Thai National ID / Tax ID (13-digit, position-weighted checksum)
# ---------------------------------------------------------------------------

_WEIGHTS = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]


def _compute_check_digit(prefix12: str) -> int:
    """Compute the 13th check digit from the first 12 digits."""
    if len(prefix12) != 12 or not prefix12.isdigit():
        raise ValueError("prefix must be exactly 12 digits")
    total = sum(int(d) * w for d, w in zip(prefix12, _WEIGHTS))
    return (11 - (total % 11)) % 10


def is_valid_thai_id(s: str) -> bool:
    """Validate a 13-digit Thai national ID or individual tax ID.

    Strips dashes/spaces. Returns False on any non-conforming input.
    Algorithm: digits[0..11] * weights[13..2], sum mod 11, 11 minus that,
    mod 10, must equal digits[12].
    """
    if not isinstance(s, str):
        return False
    s = re.sub(r"[\s\-]", "", s)
    if len(s) != 13 or not s.isdigit():
        return False
    return _compute_check_digit(s[:12]) == int(s[12])


# ---------------------------------------------------------------------------
# Phone normalization
# ---------------------------------------------------------------------------


def _digits_only(s: str) -> str:
    return re.sub(r"[\s\-\(\)]", "", s)


def normalize_phone(s: str) -> str:
    """Normalize a Thai phone number to E.164 +66XXXXXXXXX form.

    Accepts: '0812345678', '081-234-5678', '+66 81 234 5678', '66812345678'.
    Mobile (10 digits starting 0) becomes +66 + 9 digits.
    Landline (9 digits starting 0, e.g. Bangkok 02-880-1234) becomes +66 + 8 digits.
    Raises ValueError on invalid input.
    """
    if not isinstance(s, str):
        raise ValueError("phone must be a string")
    raw = _digits_only(s)
    if raw.startswith("+66"):
        rest = raw[3:]
    elif raw.startswith("66") and len(raw) in (10, 11):
        rest = raw[2:]
    elif raw.startswith("0"):
        rest = raw[1:]
    else:
        raise ValueError(f"unrecognized phone format: {s!r}")
    if not rest.isdigit() or len(rest) not in (8, 9):
        raise ValueError(f"phone has wrong digit count: {s!r}")
    return "+66" + rest


def format_phone_thai(s: str) -> str:
    """Format any Thai phone number in domestic display style.

    Mobile (10 digits): 0XX-XXX-XXXX (e.g. 081-234-5678)
    Landline (9 digits): 0X-XXX-XXXX (e.g. 02-880-1234)
    """
    e164 = normalize_phone(s)
    rest = e164[3:]  # without +66
    domestic = "0" + rest
    if len(domestic) == 10:  # mobile: 0XX-XXX-XXXX
        return f"{domestic[:3]}-{domestic[3:6]}-{domestic[6:]}"
    # landline: 0X-XXX-XXXX
    return f"{domestic[:2]}-{domestic[2:5]}-{domestic[5:]}"


# ---------------------------------------------------------------------------
# PromptPay QR (EMVCo TLV)
# ---------------------------------------------------------------------------
# Reference: https://github.com/dtinth/promptpay-qr
# Top-level tags used:
#   00 Payload Format Indicator      "01"
#   01 Point of Initiation Method    "11" static / "12" dynamic
#   29 Merchant Account Info (PromptPay)
#      00 AID  "A000000677010111"
#      01 Mobile (0066 + 9 digits, total 13 chars) OR
#      02 National ID (13 digits) OR
#      03 e-Wallet ID
#   53 Currency  "764" (THB)
#   54 Amount    e.g. "100.00"  (omit for static, no amount)
#   58 Country   "TH"
#   63 CRC-16/CCITT-FALSE (uppercase, 4 hex chars over everything including "6304")


def _tlv(tag: str, value: str) -> str:
    return f"{tag}{len(value):02d}{value}"


def _crc16_ccitt_false(data: str) -> str:
    """CRC-16/CCITT-FALSE: poly 0x1021, init 0xFFFF, no reflection, no xor-out."""
    crc = 0xFFFF
    for ch in data.encode("ascii"):
        crc ^= ch << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ 0x1021) & 0xFFFF
            else:
                crc = (crc << 1) & 0xFFFF
    return f"{crc:04X}"


def _promptpay_target(target: str) -> tuple[str, str]:
    """Detect whether `target` is a phone or a national ID; return (tag, value)."""
    digits = re.sub(r"\D", "", target)
    if len(digits) == 13:
        # National ID — tag 02
        return ("02", digits)
    # Phone: normalize to 0066 + 9-digit mobile (or 8-digit landline) prefix
    e164 = normalize_phone(target)  # "+66XXXXXXXXX"
    rest = e164[3:]  # 9 or 8 digits
    # PromptPay phone format: "0066" + rest, padded with leading zeros to 13 chars
    value = ("0066" + rest).zfill(13)
    return ("01", value)


def build_promptpay_payload(target: str, amount: Optional[float] = None) -> str:
    """Build a PromptPay QR string for the given phone or national ID.

    Args:
        target: phone (any Thai format) or 13-digit national ID
        amount: THB amount; if None, generates a static (no-amount) QR
    """
    sub_tag, sub_value = _promptpay_target(target)
    merchant_info = _tlv("00", "A000000677010111") + _tlv(sub_tag, sub_value)
    payload = (
        _tlv("00", "01")
        + _tlv("01", "12" if amount is not None else "11")
        + _tlv("29", merchant_info)
        + _tlv("53", "764")
    )
    if amount is not None:
        payload += _tlv("54", f"{amount:.2f}")
    payload += _tlv("58", "TH")
    # CRC is computed over the payload PLUS the literal "6304"
    payload += "6304"
    payload += _crc16_ccitt_false(payload)
    return payload


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------


def _make_valid_id(prefix12: str) -> str:
    return prefix12 + str(_compute_check_digit(prefix12))


def _run_tests() -> None:
    failures: list[str] = []

    def check(label: str, actual, expected):
        ok = actual == expected
        print(f"[{'PASS' if ok else 'FAIL'}] {label}: got {actual!r}, expected {expected!r}")
        if not ok:
            failures.append(label)

    # --- Thai ID checksum ---
    # Synthetic fixtures only — none correspond to a real-issued ID.
    # Real Thai IDs are issued by DOPA; these are constructed test inputs.
    valid_ids = [_make_valid_id(p) for p in [
        "000000000000",
        "123456789012",
        "999999999999",
        "100000000000",
        "222222222222",
    ]]
    for vid in valid_ids:
        check(f"is_valid_thai_id({vid})", is_valid_thai_id(vid), True)
        # corrupt last digit -> must be invalid
        bad = vid[:-1] + str((int(vid[-1]) + 1) % 10)
        check(f"is_valid_thai_id({bad}) corrupted", is_valid_thai_id(bad), False)

    # Whitespace / dash tolerance
    vid0 = valid_ids[0]
    formatted = f"{vid0[0]}-{vid0[1:5]}-{vid0[5:10]}-{vid0[10:12]}-{vid0[12]}"
    check(f"is_valid_thai_id formatted", is_valid_thai_id(formatted), True)

    # Garbage inputs
    check("is_valid_thai_id empty", is_valid_thai_id(""), False)
    check("is_valid_thai_id 12 digits", is_valid_thai_id("123456789012"), False)
    check("is_valid_thai_id letters", is_valid_thai_id("000000000000A"), False)

    # --- Phone normalization ---
    check("normalize +66", normalize_phone("+66812345678"), "+66812345678")
    check("normalize 0X mobile", normalize_phone("0812345678"), "+66812345678")
    check("normalize with dashes", normalize_phone("081-234-5678"), "+66812345678")
    check("normalize with spaces", normalize_phone("+66 81 234 5678"), "+66812345678")
    check("normalize 66 no plus", normalize_phone("66812345678"), "+66812345678")
    check("normalize landline 02", normalize_phone("02-880-1234"), "+6628801234")

    check("format mobile", format_phone_thai("+66812345678"), "081-234-5678")
    check("format landline", format_phone_thai("0628801234"[:0] + "028801234"), "02-880-1234")
    check("format from raw", format_phone_thai("0812345678"), "081-234-5678")

    # --- PromptPay payload ---
    payload_phone = build_promptpay_payload("0812345678", 100.00)
    print(f"[INFO] PromptPay phone+amount payload: {payload_phone}")
    # Must start with payload format indicator and end with CRC
    check("PP starts with 00", payload_phone.startswith("000201"), True)
    check("PP ends with 4-hex CRC", bool(re.fullmatch(r".+6304[0-9A-F]{4}", payload_phone)), True)
    # CRC must validate
    body = payload_phone[:-4]
    check("PP CRC verifies", _crc16_ccitt_false(body), payload_phone[-4:])
    # Contains AID
    check("PP contains AID", "A000000677010111" in payload_phone, True)
    # Phone tag 01 with value 0066812345678
    check("PP phone formatted", "01130066812345678" in payload_phone, True)

    payload_id = build_promptpay_payload(_make_valid_id("000000000000"), None)
    print(f"[INFO] PromptPay national-id static payload: {payload_id}")
    # Static QR: point-of-init = 11
    check("PP static POI=11", "010211" in payload_id, True)
    # National ID tag 02
    check("PP ID tag present", "0213" in payload_id, True)

    print()
    if failures:
        print(f"FAILED: {len(failures)} case(s)")
        for f in failures:
            print(f"  - {f}")
        raise SystemExit(1)
    print(f"All tests passed.")


if __name__ == "__main__":
    _run_tests()
