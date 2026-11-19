#!/usr/bin/env python3
"""Exact exterior-algebra certificates for C.4i and C.4l.

These calculations verify the numerical intersection identities, not the
existence or nonexistence of any unconstructed algebraic curve.
"""
import json
import math
from pathlib import Path

import sympy as sp


def wedge(left, right):
    result = {}
    for a, ca in left.items():
        for b, cb in right.items():
            if a & b:
                continue
            # Count pairs (i,j), i in a, j in b, with i > j.
            crossings = sum(
                (b & ((1 << i) - 1)).bit_count()
                for i in range(a.bit_length())
                if a & (1 << i)
            )
            mask = a | b
            result[mask] = result.get(mask, 0) + (-1) ** crossings * ca * cb
    return {m: sp.expand(c) for m, c in result.items() if sp.expand(c) != 0}


def power(element, exponent):
    answer = {0: sp.Integer(1)}
    for _ in range(exponent):
        answer = wedge(answer, element)
    return answer


def scale(element, scalar):
    return {m: sp.expand(c * scalar) for m, c in element.items()
            if sp.expand(c * scalar) != 0}


def add(left, right):
    answer = dict(left)
    for m, c in right.items():
        answer[m] = answer.get(m, 0) + c
    return {m: sp.expand(c) for m, c in answer.items() if sp.expand(c) != 0}


def cross_part(element, first_rank, degree):
    first_mask = (1 << first_rank) - 1
    return {m: c for m, c in element.items()
            if (m & first_mask).bit_count() == degree
            and (m >> first_rank).bit_count() == degree}


def multiple_of(element, reference):
    if not element:
        return sp.Integer(0)
    first = next(iter(reference))
    coefficient = sp.simplify(element.get(first, 0) / reference[first])
    assert add(element, scale(reference, -coefficient)) == {}
    return coefficient


def bezout(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = bezout(b, a % b)
    return g, y, x - (a // b) * y


def main():
    result = {"scope": "Exact exterior identities; no claim that all curves are divisorial"}
    dimensions = []
    for g in range(1, 5):
        n = 2 * g
        p = {(1 << i) | (1 << (n + i)): sp.Integer(1) for i in range(n)}
        top = power(p, n)
        top_coefficient = int(top[(1 << (2 * n)) - 1])
        assert top_coefficient == (-1) ** g * math.factorial(n)
        curve = power(p, n - 1)
        gamma = scale(curve, sp.Rational(1, math.factorial(n - 1)))
        assert all(c in (1, -1) for c in gamma.values())
        dimensions.append({
            "g": g,
            "P_top_coefficient": top_coefficient,
            "chi_P": top_coefficient // math.factorial(n),
            "uniform_scalar": math.factorial(n - 1),
            "normalized_curve_nonzero_coefficients": len(gamma),
            "normalized_curve_primitive": True,
        })
    result["factorial_certificates"] = dimensions

    d = sp.Symbol("d", integer=True, positive=True)
    p = {(1 << i) | (1 << (4 + i)): sp.Integer(1) for i in range(4)}
    divisor = {(1 << 0) | (1 << 1): sp.Integer(1),
               (1 << 2) | (1 << 3): d}
    dual_divisor = {(1 << 4) | (1 << 5): d,
                    (1 << 6) | (1 << 7): sp.Integer(1)}
    gamma = scale(power(p, 3), sp.Rational(1, 6))
    mixed = wedge(wedge(divisor, dual_divisor), p)
    assert add(mixed, scale(gamma, d)) == {}
    result["surface_symbolic_identity"] = "D * Dhat * P = -d * P^3 / 6"
    monomials = []
    for a in range(4):
        for b in range(4 - a):
            c = 3 - a - b
            product = wedge(wedge(power(divisor, a), power(dual_divisor, b)),
                            power(p, c))
            cross = cross_part(product, 4, 3)
            coefficient = multiple_of(cross, gamma)
            expected = 6 if (a, b, c) == (0, 0, 3) else (
                -d if (a, b, c) == (1, 1, 1) else 0)
            assert sp.expand(coefficient - expected) == 0
            monomials.append({"D_power": a, "Dhat_power": b, "P_power": c,
                              "identity_coefficient": str(coefficient)})
    result["all_surface_divisor_monomials"] = monomials
    result["surface_divisor_subring_image"] = [
        {"d": d0, "positive_generator": math.gcd(6, d0)} for d0 in range(1, 25)
    ]
    result["bezout_examples"] = []
    for a, b in [(6, 5), (120, 7), (2, 3)]:
        g, x, y = bezout(a, b)
        assert x * a + y * b == g == 1
        result["bezout_examples"].append(
            {"n1": a, "n2": b, "coefficient1": x, "coefficient2": y,
             "identity": f"{x}*{a} + {y}*{b} = 1"})
    output = Path(__file__).resolve().parents[1] / "output"
    output.mkdir(exist_ok=True)
    (output / "verify_c4_exterior.json").write_text(
        json.dumps(result, indent=2) + "\n")
    lines = [
        "PASS: P^(2g)/(2g)! has degree (-1)^g for g=1,2,3,4.",
        "PASS: P^(2g-1)/(2g-1)! is primitive integral in the exterior lattice.",
        "PASS: D*Dhat*P = -d*P^3/6 symbolically for a (1,d) surface.",
        "PASS: all ten divisor monomials checked; cross coefficients are 6, -d, or 0.",
        "PASS: Bezout retraction examples checked exactly.",
        "Scope: this does not prove that arbitrary curves lie in the divisor subring.",
    ]
    text = "\n".join(lines) + "\n"
    (output / "verify_c4_exterior.txt").write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
