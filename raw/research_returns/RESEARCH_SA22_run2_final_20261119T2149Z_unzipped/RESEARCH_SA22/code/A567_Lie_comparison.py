#!/usr/bin/env python3
"""Finite arithmetic certificate for the PS118 characteristic-two example.

The all-degree simplicial construction and its homotopy calculation are proved
in notes/A567_Lie_comparison_counterexample.tex.  This program checks only the
four rational points, their orders, and the derivative law over dual numbers.
"""
import itertools
import json
import time

started = time.perf_counter()
checks_count = 0
points = list(itertools.product(range(2), repeat=2))
zero = (0, 0)


def check(condition):
    global checks_count
    checks_count += 1
    if not condition:
        raise AssertionError(f"check {checks_count} failed")


def add(x, y):
    return ((x[0] + y[0]) % 2,
            (x[1] + y[1] + x[0] * y[0]) % 2)


def vector_add(x, y):
    return tuple((u + v) % 2 for u, v in zip(x, y))


def order(x, law):
    value = zero
    for n in range(1, 5):
        value = law(value, x)
        if value == zero:
            return n
    raise AssertionError("element order exceeded 4")


def dual_add(x, y):
    return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)


def dual_mul(x, y):
    return ((x[0] * y[0]) % 2,
            (x[0] * y[1] + x[1] * y[0]) % 2)


def tangent_law(x, y):
    a, b = (0, x[0]), (0, x[1])
    c, d = (0, y[0]), (0, y[1])
    return dual_add(a, c), dual_add(dual_add(b, d), dual_mul(a, c))


for x in points:
    check(add(x, zero) == x)
    check(add(zero, x) == x)
for x, y in itertools.product(points, repeat=2):
    check(add(x, y) == add(y, x))
for x, y, z in itertools.product(points, repeat=3):
    check(add(add(x, y), z) == add(x, add(y, z)))
for a, b in points:
    check(add((a, b), (a, (b + a * a) % 2)) == zero)

group_orders = [order(x, add) for x in points]
expected_group_orders = [1, 2, 4, 4]
for actual, expected in zip(group_orders, expected_group_orders):
    check(actual == expected)

for x, y in itertools.product(points, repeat=2):
    expected = tuple((0, u) for u in vector_add(x, y))
    check(tangent_law(x, y) == expected)

tangent_orders = [order(x, vector_add) for x in points]
for actual, expected in zip(tangent_orders, [1, 2, 2, 2]):
    check(actual == expected)
check(sorted(group_orders) != sorted(tangent_orders))

result = {
    "status": "PASS",
    "field": "F_2",
    "scope": "All 4 rational points; all 64 associativity triples; all 16 dual-number derivative pairs. No finite truncation is used to claim the all-degree homotopy theorem.",
    "checks_count": checks_count,
    "elapsed_seconds": time.perf_counter() - started,
    "run_note": "First timed run of this certificate",
    "points": points,
    "group_orders": group_orders,
    "tangent_orders": tangent_orders,
    "group_Cayley_table": [[points.index(add(x, y)) for y in points] for x in points],
    "tangent_Cayley_table": [[points.index(vector_add(x, y)) for y in points] for x in points],
    "conclusion": "G(F_2) is cyclic of order 4; Lie(G)(F_2) is elementary abelian of order 4; they are not isomorphic as groups."
}
print(json.dumps(result, indent=2))
