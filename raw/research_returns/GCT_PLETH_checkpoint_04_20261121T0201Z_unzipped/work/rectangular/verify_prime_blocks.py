#!/usr/bin/env python3
"""Exact finite checks of the normalized prime rectangular contraction.

No source-paper code is imported. For each case, expand determinant^b
and permanent^b together by independent monomial multiplication. Their
Fischer pairing gives the actual tensor contraction:
 q = sum_E C_E D_E prod(E_ij!) / ((a!)^b (b!)^a).
The derivation is recorded in boundary_and_prime_blocks.md.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import factorial
from pathlib import Path
import csv

HERE = Path(__file__).resolve().parent


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p))
                       for j in range(i + 1, len(p)))


def expansion(a, b):
    terms = []
    for p in permutations(range(a)):
        t = tuple(int(j == p[i]) for i in range(a) for j in range(a))
        terms.append((t, sign(p)))
    # Each state stores determinant and permanent coefficients.
    d = {(0,) * (a * a): (1, 1)}
    for _ in range(b):
        nd = defaultdict(lambda: [0, 0])
        for e, (c_det, c_per) in d.items():
            for t, sg in terms:
                z = tuple(x + y for x, y in zip(e, t))
                nd[z][0] += sg * c_det
                nd[z][1] += c_per
        d = {e: tuple(cd) for e, cd in nd.items()}
    assert sum(cp for cd, cp in d.values()) == factorial(a) ** b
    return d


def residue(q, p):
    assert q.denominator % p != 0
    return (q.numerator % p) * pow(q.denominator, -1, p) % p


def check(a, p):
    b = p - 1
    coeffs = expansion(a, b)
    numerator = 0
    for e, (cd, cp) in coeffs.items():
        ef = 1
        for x in e:
            ef *= factorial(x)
        # Check Glynn's coefficient congruence separately at every monomial.
        assert (cd * ef - (-1) ** a) % p == 0, (a, p, e, cd)
        numerator += cd * cp * ef
    q = Fraction(numerator, factorial(a) ** b * factorial(b) ** a)
    assert residue(q, p) == 1
    # Independently enumerated Latin scalars in verify_rectangular.py.
    square = {2: Fraction(-1, 2), 4: Fraction(1, 576)}
    if a == b and a in square:
        assert q == square[a] ** 2
    return {
        "a": a, "b": b, "prime": p,
        "exponent_matrices": len(coeffs),
        "pairing_integer_numerator": numerator,
        "q_numerator": q.numerator, "q_denominator": q.denominator,
        "q_mod_p": residue(q, p),
        "all_coefficient_congruences": "PASS",
    }


def main():
    cases = [(2, 3), (2, 5), (3, 5), (3, 7), (4, 5), (3, 11), (3, 13)]
    rows = [check(a, p) for a, p in cases]
    with (HERE / "PRIME_BLOCK_CHECKS.tsv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
