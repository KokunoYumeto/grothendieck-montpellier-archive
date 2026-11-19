#!/usr/bin/env python3
"""Exact arithmetic and invariant-polynomial checks for B-RD36."""
from math import gcd
from pathlib import Path
import json
import time
import sympy as s


def main():
    start = time.perf_counter()
    rows = []
    for delta in range(24):
        compatible = []
        for m in (1, 2, 3, 4, 6, 12):
            tame = m // 3 if m % 3 == 0 else m
            if m * delta % 12:
                continue
            r = m * delta // 12
            if gcd(r, tame) != 1:
                continue
            assert tame == 4 // gcd(4, delta)
            compatible.append({"m": m, "t": tame, "r": r})
        assert compatible
        rows.append({"delta": delta, "t": 4 // gcd(4, delta),
                     "necessary_scaling_cases": compatible})
    for delta in range(-100, 101):
        for shift in range(-10, 11):
            assert gcd(4, delta) == gcd(4, delta + 12 * shift)

    a2, a4, a6, x = s.symbols("a2 a4 a6 x")
    b2, b4, b6, b8 = 4*a2, 2*a4, 4*a6, 4*a2*a6-a4**2
    c4 = b2**2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    discriminant = -b2**2*b8-8*b4**3-27*b6**2+9*b2*b4*b6
    assert s.expand(c4**3-c6**2-1728*discriminant) == 0
    assert s.Poly(c4-a2**2, a2, a4, a6, modulus=3).is_zero
    assert s.Poly(x**3+a2*x**2+a4*x+a6, x).coeff_monomial(x**2) == a2
    for delta in range(24, 1001):
        lower_c4 = (delta + 2) // 3
        lower_c6 = (delta + 1) // 2
        assert lower_c4 - 2 >= 4
        assert lower_c6 - 6 >= 6

    result = {
        "status": "PASS",
        "discriminant_rows": rows,
        "scaling_invariance_cases": 201 * 21,
        "minimal_discriminant_bound_cases": 977,
        "polynomial_identities": ["c4^3-c6^2=1728Delta", "c4 mod3=a2^2", "Cartier coefficient=a2"],
        "scope": "Necessary tame scaling conditions and coefficient identities; no existence or level27 comparison is asserted",
        "elapsed_seconds": time.perf_counter() - start,
    }
    Path(__file__).with_suffix(".output.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "discriminant_rows"}, indent=2))


if __name__ == "__main__":
    main()
