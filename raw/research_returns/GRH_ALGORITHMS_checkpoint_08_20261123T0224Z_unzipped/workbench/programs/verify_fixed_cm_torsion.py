#!/usr/bin/env python3
"""Exact, dependency-free checks in F_3[lambda]/(lambda^6).

Run from the worktree root:
  python delivery/workbench/research/kummer/verify_fixed_cm_torsion.py
The output must equal verify_fixed_cm_torsion_expected.json.
These are finite algebra checks, not a Frobenius-distribution experiment.
"""
from collections import Counter
import json

P, H = 3, 6
ZERO = (0,) * H
ONE = (1,) + (0,) * (H - 1)

def digits(n):
    a = []
    for _ in range(H):
        a.append(n % P)
        n //= P
    return tuple(a)

def add(a, b):
    return tuple((x + y) % P for x, y in zip(a, b))

def neg(a):
    return tuple(-x % P for x in a)

def mul(a, b):
    return tuple(sum(a[i] * b[j - i] for i in range(j + 1)) % P
                 for j in range(H))

def power(a, n):
    z = ONE
    while n:
        if n & 1:
            z = mul(z, a)
        a = mul(a, a)
        n //= 2
    return z

def conjugate(a):
    return tuple(x * (-1 if i & 1 else 1) % P
                 for i, x in enumerate(a))

def depth(a):
    for i, x in enumerate(add(a, neg(ONE))):
        if x:
            return i
    return H

ring = {digits(n) for n in range(P ** H)}
units = {u for u in ring if u[0]}
norm_one = {u for u in units if mul(u, conjugate(u)) == ONE}
cubes = {power(u, 3) for u in units}
assert cubes <= norm_one

def orbit_counts(u):
    todo = set(ring)
    counts = Counter()
    while todo:
        x = start = min(todo)
        length = 0
        while True:
            assert x in todo
            todo.remove(x)
            x = mul(u, x)
            length += 1
            if x == start:
                break
        counts[length] += 1
    assert sum(n * count for n, count in counts.items()) == P ** H
    return {str(n): counts[n] for n in sorted(counts)}

examples = []
for s in (1, 3, 5):
    lam_s = tuple(int(i == s) for i in range(H))
    numerator = add(ONE, lam_s)
    denominator = add(ONE, neg(lam_s))
    # The unit group has order 486; inversion is exact exponentiation.
    u = mul(numerator, power(denominator, len(units) - 1))
    assert mul(u, conjugate(u)) == ONE
    assert depth(u) == s
    examples.append({"depth": s, "positive": orbit_counts(u),
                     "negative": orbit_counts(neg(u))})

result = {
    "ring_size": len(ring),
    "unit_group_size": len(units),
    "norm_one_unit_count": len(norm_one),
    "cube_subgroup_size": len(cubes),
    "norm_one_noncubes": len(norm_one - cubes),
    "norm_one_positive_depth_counts": dict(sorted(Counter(
        depth(u if u[0] == 1 else neg(u)) for u in norm_one).items())),
    "examples": examples,
    "scope": "Exact finite ring arithmetic only; no assertion about the distribution of CM Frobenius units."
}
assert result["unit_group_size"] == 486
assert result["norm_one_unit_count"] == 54
assert result["cube_subgroup_size"] == 6
assert result["norm_one_noncubes"] == 48
assert examples == [
    {"depth": 1, "positive": {"1": 3, "3": 8, "9": 78},
     "negative": {"1": 1, "2": 1, "6": 4, "18": 39}},
    {"depth": 3, "positive": {"1": 27, "3": 234},
     "negative": {"1": 1, "2": 13, "6": 117}},
    {"depth": 5, "positive": {"1": 243, "3": 162},
     "negative": {"1": 1, "2": 121, "6": 81}},
]
print(json.dumps(result, indent=2, sort_keys=True))
