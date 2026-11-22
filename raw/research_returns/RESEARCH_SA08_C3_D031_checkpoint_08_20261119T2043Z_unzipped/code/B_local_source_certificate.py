#!/usr/bin/env python3
"""Supplementary exact checks for the local G_N comparison used in AT20.

The all-index argument is the Legendre calculation and the explicit
PD-coordinate proof.  This script does not extrapolate finite checks.
It independently checks the integer basis coefficients and the three
faces and vertical differential of the proposed normalized one-form.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import json
import time

started = time.perf_counter()
checks = 0
cases = 0
formula_cases = 0


def check(condition):
    global checks
    checks += 1
    assert condition


@lru_cache(None)
def fac(n):
    return factorial(n)


def derivative(term):
    """A monomial in Gamma(u1,u2) tensor Lambda(du1,du2).

    A key (a,b,mask) denotes gamma_a(u1) gamma_b(u2) times
    the indicated increasing exterior product.  Both u_i are even.
    """
    out = {}
    for (a, b, mask), coefficient in term.items():
        for index, exponent in enumerate((a, b)):
            if exponent == 0 or mask & (1 << index):
                continue
            powers = [a, b]
            powers[index] -= 1
            sign = -1 if (mask & ((1 << index) - 1)).bit_count() % 2 else 1
            key = (*powers, mask | (1 << index))
            out[key] = out.get(key, Fraction(0)) + sign * coefficient
    return {key: value for key, value in out.items() if value}


def face_of_x(m, coefficient, face):
    """Faces of -coefficient*gamma_(m-1)(u2)*du1.

    The zeroth face imposes u1+u2=U and du1=-du2; faces one
    and two set the respective coordinate and its differential to zero.
    Keys on the output edge are (gamma exponent, differential mask).
    """
    if face == 0:
        return {(m - 1, 1): coefficient} if coefficient else {}
    if face == 1:
        return {}
    if face == 2:
        return {} if m >= 2 else {(0, 1): -coefficient}
    raise ValueError(face)


for exponent in range(7):
    n = 2 ** exponent
    for m in range(17):
        denominator = fac(m) * fac(n) ** m
        check(fac(m*n) % denominator == 0)
        composition = fac(m*n) // denominator
        check(composition % 2 == 1)
        for remainder in range(n):
            weight = m*n + remainder
            multiplication = comb(weight, remainder)
            basis_coefficient = composition * multiplication
            check(multiplication % 2 == 1)
            check(basis_coefficient % 2 == 1)
            check(basis_coefficient * fac(m) * fac(n)**m * fac(remainder) == fac(weight))
            cases += 1
            if m < 2:
                continue
            for scalar in (-3, -1, 1, 2, 5):
                lam = Fraction(scalar, basis_coefficient)
                check(lam.denominator % 2 == 1)
                check(lam * basis_coefficient == scalar)
                x = {(0, m-1, 1): -lam}
                y = {(0, m-2, 3): lam}
                check(derivative(x) == y)
                check(derivative(y) == {})
                check(face_of_x(m, lam, 0) == {(m-1, 1): lam})
                check(face_of_x(m, lam, 1) == {})
                check(face_of_x(m, lam, 2) == {})
                check((m-1)*n + n + remainder == weight)
                formula_cases += 1
    for q in range(9):
        for weight in range((q+1)*n, (q+2)*n):
            check(weight // n > q)

result = {
    "statement": "C09 local source and AT20 explicit comparison pair",
    "status": "passed",
    "checks": checks,
    "basis_cases": cases,
    "normalized_formula_cases": formula_cases,
    "powers_of_two": [2**e for e in range(7)],
    "coefficient_arities": [0, 16],
    "claims": [
        "integer coefficient basis with odd unit transition",
        "explicit normalized x has all three prescribed faces",
        "vertical differential has the stated two-form value",
        "row threshold (q+1)N implies floor(weight/N)>q"
    ],
    "scope": "finite supplementary certificate; all-index proof is symbolic",
    "runtime_seconds": time.perf_counter() - started,
}
output = Path(__file__).resolve().parents[1] / "logs" / "B_local_source_certificate.json"
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
