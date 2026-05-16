"""Thai VAT and Withholding-Tax helpers.

All arithmetic uses ``decimal.Decimal`` because Thai accounting documents are
filed to the satang (0.01 THB) and floats lose this precision. Functions
return dictionaries so the caller can format each line item explicitly.

Run ``python calc.py`` for a self-test.
"""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Union

# Two-decimal quantum used everywhere (1 satang).
TWOPLACES = Decimal("0.01")

# Common Thai withholding-tax rates for resident payees.
# Keys mirror the categories in the Revenue Department's ภ.ง.ด.3 / 53 schedule.
WHT_RATES: Dict[str, Decimal] = {
    "service": Decimal("0.03"),        # บริการทั่วไป
    "rent": Decimal("0.05"),           # ค่าเช่าอสังหาริมทรัพย์
    "advertising": Decimal("0.02"),    # ค่าโฆษณา
    "transport": Decimal("0.01"),      # ค่าขนส่ง
    "professional": Decimal("0.03"),   # ค่าวิชาชีพอิสระ
}

Number = Union[Decimal, int, str]


def _to_decimal(value: Number) -> Decimal:
    """Coerce input to Decimal. Reject floats to avoid silent precision loss."""
    if isinstance(value, Decimal):
        return value
    if isinstance(value, int):
        return Decimal(value)
    if isinstance(value, str):
        return Decimal(value)
    raise TypeError(
        f"Use Decimal, int, or str for money values, got {type(value).__name__}. "
        "Floats are rejected because they cannot represent satang exactly."
    )


def _q(value: Decimal) -> Decimal:
    """Quantize to two decimal places (satang), rounding half-up."""
    return value.quantize(TWOPLACES, rounding=ROUND_HALF_UP)


def calculate_vat(
    subtotal: Number,
    rate: Number = Decimal("0.07"),
) -> Dict[str, Decimal]:
    """Add VAT on top of a VAT-exclusive subtotal.

    Example: subtotal 1000, rate 0.07 → vat 70, total 1070.
    """
    sub = _to_decimal(subtotal)
    r = _to_decimal(rate)
    vat = _q(sub * r)
    total = _q(sub + vat)
    return {
        "subtotal": _q(sub),
        "vat": vat,
        "total": total,
    }


def calculate_vat_inclusive(
    total: Number,
    rate: Number = Decimal("0.07"),
) -> Dict[str, Decimal]:
    """Back out VAT from a VAT-inclusive total.

    subtotal = total / (1 + rate); vat = total - subtotal.
    Example: total 1070, rate 0.07 → subtotal 1000, vat 70.
    """
    tot = _to_decimal(total)
    r = _to_decimal(rate)
    subtotal = _q(tot / (Decimal("1") + r))
    vat = _q(tot - subtotal)
    return {
        "subtotal": subtotal,
        "vat": vat,
        "total": _q(tot),
    }


def calculate_wht(
    amount: Number,
    rate: Number,
) -> Dict[str, Decimal]:
    """Compute withholding tax on a pre-VAT amount.

    The Thai Revenue Department always bases WHT on the pre-VAT figure.
    Example: amount 10000, rate 0.03 → wht 300, net_payable 9700.
    """
    amt = _to_decimal(amount)
    r = _to_decimal(rate)
    wht = _q(amt * r)
    net = _q(amt - wht)
    return {
        "amount": _q(amt),
        "wht": wht,
        "net_payable": net,
    }


if __name__ == "__main__":
    # Self-test: prints PASS/FAIL for each expected case and exits non-zero on
    # any failure so CI can rely on the exit code rather than scraping stdout.
    failures: list[str] = []

    def check(label: str, got: Decimal, want: Decimal) -> None:
        ok = got == want
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {label}: got {got}, want {want}")
        if not ok:
            failures.append(label)

    print("calculate_vat(1000) -> 70 VAT, 1070 total")
    v = calculate_vat(Decimal("1000"))
    check("subtotal", v["subtotal"], Decimal("1000.00"))
    check("vat", v["vat"], Decimal("70.00"))
    check("total", v["total"], Decimal("1070.00"))

    print("calculate_vat_inclusive(1070) -> 1000 subtotal, 70 VAT")
    vi = calculate_vat_inclusive(Decimal("1070"))
    check("subtotal", vi["subtotal"], Decimal("1000.00"))
    check("vat", vi["vat"], Decimal("70.00"))
    check("total", vi["total"], Decimal("1070.00"))

    print("calculate_wht(10000, 0.03) -> 300 WHT, 9700 net")
    w = calculate_wht(Decimal("10000"), Decimal("0.03"))
    check("amount", w["amount"], Decimal("10000.00"))
    check("wht", w["wht"], Decimal("300.00"))
    check("net_payable", w["net_payable"], Decimal("9700.00"))

    print("WHT_RATES sanity check")
    check("rent rate", WHT_RATES["rent"], Decimal("0.05"))
    check("advertising rate", WHT_RATES["advertising"], Decimal("0.02"))
    check("transport rate", WHT_RATES["transport"], Decimal("0.01"))
    check("service rate", WHT_RATES["service"], Decimal("0.03"))
    check("professional rate", WHT_RATES["professional"], Decimal("0.03"))

    print()
    if failures:
        print(f"FAILED: {len(failures)} case(s)")
        for f in failures:
            print(f"  - {f}")
        raise SystemExit(1)
    print("All tests passed.")
