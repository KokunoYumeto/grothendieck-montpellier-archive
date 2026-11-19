#!/usr/bin/env python3
"""Independent exact arithmetic checks for the B.3 audit.

The cohomological conclusions are proved in the manuscript.  This certificate
checks the finite polynomial identities entering the characteristic-7 and
characteristic-3 counterexamples, without numerical approximation.
"""
from pathlib import Path
import json


def multiply(left, right, modulus=None):
    answer = {}
    for e, a in left.items():
        for f, b in right.items():
            key = tuple(x + y for x, y in zip(e, f))
            answer[key] = answer.get(key, 0) + a * b
    if modulus:
        answer = {e: a % modulus for e, a in answer.items()}
    return {e: a for e, a in answer.items() if a}


def power(poly, exponent, modulus=None):
    answer = {(0,) * len(next(iter(poly))): 1}
    for _ in range(exponent):
        answer = multiply(answer, poly, modulus)
    return answer


# Variables x,a,b.  Coefficient of x^6 in (x^3+a*x+b)^3.
cube = power({(3, 0, 0): 1, (1, 1, 0): 1, (0, 0, 1): 1}, 3)
coefficient = {e[1:]: a for e, a in cube.items() if e[0] == 6}
assert coefficient == {(0, 1): 3}

char7 = []
for a, b, expected_discriminant, expected_cartier in [
    (-1, 0, 3, 0), (-1, 1, 2, 3)
]:
    disc_factor = (4 * a**3 + 27 * b**2) % 7
    cartier = (3 * b) % 7
    assert disc_factor == expected_discriminant != 0
    assert cartier == expected_cartier
    char7.append({
        "a": a, "b": b,
        "4a^3+27b^2_mod_7": disc_factor,
        "coefficient_x^6_mod_7": cartier,
        "smooth": True,
    })

# Variables x,t; lambda=2+t, characteristic 3.
legendre = multiply(
    multiply({(1, 0): 1}, {(1, 0): 1, (0, 0): -1}, 3),
    {(1, 0): 1, (0, 0): -2, (0, 1): -1}, 3,
)
x2 = {e[1]: a for e, a in legendre.items() if e[0] == 2}
assert x2 == {1: 2}  # -t in F_3[t]
disc_at_zero = (16 * 2**2 * (1 - 2)**2) % 3
assert disc_at_zero == 1

report = {
    "status": "passed",
    "characteristic_7_coefficient_identity": "[x^6](x^3+a*x+b)^3 = 3*b over Z",
    "characteristic_7_examples": char7,
    "characteristic_3_legendre": {
        "lambda": "2+t",
        "coefficient_x^2": "-t",
        "discriminant_constant_term_mod_3": disc_at_zero,
        "special_Cartier_zero": True,
        "generic_Cartier_nonzero": True,
    },
    "scope": "Exact algebraic hypotheses only; cohomology and specialization are proved in sections/part_b.tex.",
}
out = Path(__file__).with_name("part_c_b3_audit_output.json")
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
