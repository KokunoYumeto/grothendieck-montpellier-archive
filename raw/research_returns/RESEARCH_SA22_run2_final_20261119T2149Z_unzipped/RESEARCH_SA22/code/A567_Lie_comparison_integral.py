#!/usr/bin/env python3
"""Exact symbolic and Smith-form certificate for the integral PS118 example.

No bounded sample of integers is used to assert a universal identity.  The
source proof supplies Dold--Kan in every degree and all geometric assertions.
"""
import json
import time
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

started = time.perf_counter()
checks_count = 0


def check(condition):
    global checks_count
    checks_count += 1
    if not condition:
        raise AssertionError(f"check {checks_count} failed")


a, b, c, d, t, u = s.symbols("a b c d t u", integer=True)


def law(x, y):
    return s.Matrix([x[0] + y[0], x[1] + y[1] + x[0] * y[0]])


def differential(x):
    return s.Matrix([2 * x, 2 * x**2])


def theta(x):
    return s.Matrix([x[0], x[1] - x[0] * (x[0] - 1) / 2])


zero = s.zeros(2, 1)
check(s.simplify(law(differential(t), differential(u)) - differential(t + u)) == zero)
check(s.simplify(theta(law(s.Matrix([a, b]), s.Matrix([c, d])))
                 - theta(s.Matrix([a, b])) - theta(s.Matrix([c, d]))) == zero)
check(s.simplify(theta(differential(t)) - s.Matrix([2 * t, t])) == zero)
check(differential(t).diff(t).subs(t, 0) == s.Matrix([2, 0]))

points_matrix = s.Matrix([[2], [1]])
tangent_matrix = s.Matrix([[2], [0]])
points_smith = smith_normal_form(points_matrix, domain=s.ZZ)
tangent_smith = smith_normal_form(tangent_matrix, domain=s.ZZ)
check(points_smith == s.Matrix([[1], [0]]))
check(tangent_smith == s.Matrix([[2], [0]]))
check(abs(int(points_smith[0, 0])) != abs(int(tangent_smith[0, 0])))

print(json.dumps({
    "status": "PASS",
    "base_ring": "Z",
    "checks_count": checks_count,
    "elapsed_seconds": time.perf_counter() - started,
    "run_note": "First timed run of this certificate",
    "scope": "Exact polynomial identities over Q with integer-valued theta, derivative, and Smith normal forms over Z; no finite-range integer extrapolation.",
    "point_differential": [[2], [1]],
    "tangent_differential": [[2], [0]],
    "point_Smith_form": [[int(v) for v in row] for row in points_smith.tolist()],
    "tangent_Smith_form": [[int(v) for v in row] for row in tangent_smith.tolist()],
    "point_cokernel": "Z",
    "tangent_cokernel": "Z direct_sum Z/2",
    "proof_boundary": "Integer-valuedness of a(a-1)/2, representability, all-degree Dold-Kan, smoothness and Kan are established in the written proof."
}, indent=2))
