#!/usr/bin/env python3
"""One exact algebra control for HM.4--HM.7; no prime search."""
from fractions import Fraction
from pathlib import Path
import hashlib
import json


def binomial(x, n):
    value = Fraction(1)
    for j in range(n):
        value *= (x - j) / (j + 1)
    return value


def valuation(x, p):
    assert x != 0
    a, b = abs(x.numerator), x.denominator
    value = 0
    while a % p == 0:
        a //= p
        value += 1
    while b % p == 0:
        b //= p
        value -= 1
    return value


def residue(x, p):
    assert x.denominator % p
    return x.numerator * pow(x.denominator, -1, p) % p


def main():
    p = 31
    b = (p + 3) // 2
    rows = []
    for r in range(p):
        c = ((-1) ** r * binomial(Fraction(3 * p, 2), p - 1 - r)
             * binomial(Fraction(p) + Fraction(3, 2), r))
        expected = 2 if b + 1 <= r <= p - 2 else 1
        assert valuation(c, p) == expected
        s = residue(c / p, p)
        assert (s == 0) == (expected == 2)
        rows.append({"r": r, "c_numerator": c.numerator,
                     "c_denominator": c.denominator,
                     "valuation": expected, "s_residue": s})
    assert rows[p - 3]["s_residue"] == rows[p - 2]["s_residue"] == 0
    contradictions = []
    for r in (p - 3, p - 2):
        product = (-1) ** r % p
        diagonal = ((-1) ** r - 1) % p
        beta = diagonal * pow(product, -1, p) % p
        contradictions.append({"r": r, "product_coefficient": product,
                               "diagonal_coefficient": diagonal,
                               "forced_beta": beta})
    assert [x["forced_beta"] for x in contradictions] == [0, 2]
    report = {"status": "PASS", "scope": "single prescribed algebra control",
              "prime": p, "b": b, "rows": rows,
              "incompatible_beta_conditions": contradictions,
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    dest = Path(__file__).with_suffix(".json")
    dest.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "rows": len(rows),
                      "report": str(dest), "report_sha256":
                      hashlib.sha256(dest.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
