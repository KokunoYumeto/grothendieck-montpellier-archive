#!/usr/bin/env python3
"""Exact arithmetic checks for C.4n; no geometric existence is simulated."""
from fractions import Fraction
from math import comb, factorial, gcd
from pathlib import Path
import json


def interpolation_coefficients(t):
    return [(-1) ** j * comb(t + j - 1, j) * comb(t + 4, 4 - j)
            for j in range(5)]


def main():
    checks = []
    for t in range(1, 33):
        coeffs = interpolation_coefficients(t)
        for r in range(5):
            # The monomials 1,t,...,t^4 form a basis over Q.
            actual = sum(coeffs[j] * (t + j) ** r for j in range(5))
            expected = 1 if r == 0 else 0
            assert actual == expected, (t, r, actual)
        checks.append({"T": t, "coefficients": coeffs,
                       "all_monomials_through_degree_4": "passed"})

    n = 3 * factorial(4)
    rr_coefficients = [Fraction(n ** r, factorial(r) * factorial(4-r))
                       for r in range(1, 5)]
    assert all(c.denominator == 1 and c.numerator % 3 == 0
               for c in rr_coefficients)
    for m in range(1, 1000):
        if m % 3 == 1:
            assert gcd(6, 2*m) == 2
    data = {
        "status": "passed",
        "scope": "Finite exact arithmetic certificate; geometry proved in LaTeX.",
        "finite_interpolation_checks": checks,
        "N": n,
        "RR_coefficients": [int(c) for c in rr_coefficients],
        "all_RR_coefficients_divisible_by_3": True,
        "gcd_6_2m_for_m_1_mod_3_below_1000": "passed",
    }
    base = Path(__file__).resolve().parents[1] / "output"
    base.mkdir(exist_ok=True)
    (base / "verify_c4_prym_arithmetic.json").write_text(
        json.dumps(data, indent=2) + "\n")
    report = (
        "PASS: exact C.4n arithmetic checks\n"
        "32 shifts x 5 monomial basis elements: interpolation equals evaluation at 0.\n"
        "T=1 coefficients: " + str(checks[0]["coefficients"]) + "\n"
        "N=72 RR coefficients: " + str(data["RR_coefficients"]) + "\n"
        "Every coefficient is an integer divisible by 3.\n"
        "For m=1 mod 3 below 1000, gcd(6,2m)=2.\n"
        "No geometric existence claim rests on this finite check.\n"
    )
    (base / "verify_c4_prym_arithmetic.txt").write_text(report)
    print(report, end="")


if __name__ == "__main__":
    main()
