#!/usr/bin/env python3
"""Exact finite checks for the reconstructed alternating-product obstruction.

The proof covers all ranks and fields. This finite certificate checks the
explicit permutation generators, elementary abelian subgroups, and integer
inequalities used in its concrete examples. It does not replace those proofs.
"""
from collections import deque
from itertools import product
from math import factorial
from pathlib import Path
import hashlib
import json
import time

started = time.perf_counter()
checks = 0

def check(value, message):
    global checks
    checks += 1
    if not value:
        raise AssertionError(message)

def cycle(n, letters):
    a = list(range(n))
    for u, v in zip(letters, letters[1:] + letters[:1]):
        a[u] = v
    return tuple(a)

def mul(a, b):
    return tuple(a[x] for x in b)

def power(a, exponent):
    result = tuple(range(len(a)))
    while exponent:
        if exponent & 1:
            result = mul(result, a)
        a = mul(a, a)
        exponent //= 2
    return result

def even(a):
    return sum(a[i] > a[j] for i in range(len(a))
               for j in range(i + 1, len(a))) % 2 == 0

groups = []
for n in (5, 7, 9):
    ident = tuple(range(n))
    rotation = cycle(n, list(range(n)))
    triple = cycle(n, [0, 1, 2])
    check(even(rotation) and even(triple), ("even generators", n))
    seen = {ident}
    queue = deque([ident])
    while queue:
        a = queue.popleft()
        check(even(a), ("even generated permutation", n, a))
        for g in (rotation, triple):
            b = mul(g, a)
            if b not in seen:
                seen.add(b)
                queue.append(b)
    check(len(seen) == factorial(n) // 2, ("alternating order", n))
    for i in range(n - 2):
        check(cycle(n, [i, i+1, i+2]) in seen, ("adjacent triple", n, i))
    subgroup_records = []
    for ell, block in ((2, 4), (3, 3)):
        generators = []
        for j in range(n // block):
            if ell == 2:
                g = mul(cycle(n, [4*j, 4*j+1]),
                        cycle(n, [4*j+2, 4*j+3]))
            else:
                g = cycle(n, [3*j, 3*j+1, 3*j+2])
            check(g in seen, ("elementary subgroup generator", n, ell, j))
            check(power(g, ell) == ident and g != ident,
                  ("exact generator order", n, ell, j))
            generators.append(g)
        for g in generators:
            for h in generators:
                check(mul(g, h) == mul(h, g), ("commutation", n, ell))
        subgroup = set()
        for exponents in product(range(ell), repeat=len(generators)):
            h = ident
            for g, e in zip(generators, exponents):
                h = mul(h, power(g, e))
            subgroup.add(h)
        check(len(subgroup) == ell ** len(generators),
              ("elementary rank", n, ell))
        subgroup_records.append({"prime": ell, "rank": len(generators),
                                 "order": len(subgroup)})
    groups.append({"n": n, "generated_order": len(seen),
                   "expected_order": factorial(n)//2,
                   "elementary_subgroups": subgroup_records})

for n in range(5, 1002, 2):
    check(n <= 8 * (n // 4), ("uniform dimension bound", n))
    check(n <= 8 * (n // 3), ("characteristic two dimension bound", n))
    check(n ** n <= 2 ** (n*n), ("simple-label bound", n))

dimension_tuples = 0
for length in range(1, 6):
    for dims in product(range(2, 7), repeat=length):
        r = 1
        for d in dims:
            r *= d
        check(sum(d*d for d in dims) <= r*r, ("square budget", dims))
        check(sum((8*d)**2 for d in dims) <= 64*r*r,
              ("support budget", dims))
        dimension_tuples += 1

non_generation = []
for generators in range(1, 17):
    n = 2 * generators * generators + 5
    check(n % 2 == 1, ("odd non-generation test", generators))
    check(2 ** (n*n) > factorial(n) ** generators,
          ("coordinate multiplicity exceeds tuple count", generators, n))
    non_generation.append({"generators": generators, "n": n,
                           "inequality": "2^(n*n) > (n!)^generators"})

# Check the extension-count exponent identity for all positive compositions
# up to rank twelve, using a fixed C >= 1.
composition_count = 0
def compositions(n):
    if n == 0:
        yield ()
    else:
        for first in range(1, n+1):
            for tail in compositions(n-first):
                yield (first,) + tail

for r in range(1, 13):
    local_count = 0
    for dims in compositions(r):
        local_count += 1
        sq = sum(d*d for d in dims)
        cross = 2 * sum(dims[i]*dims[j] for i in range(len(dims))
                        for j in range(i+1, len(dims)))
        check(sq + cross == r*r, ("quadratic extension identity", dims))
        check(7*sq + cross <= 7*r*r, ("extension exponent bound", dims))
    check(local_count == 2**(r-1), ("composition count", r))
    composition_count += local_count

result = {
    "status": "passed",
    "assertions": checks,
    "runtime_seconds": time.perf_counter() - started,
    "exact_arithmetic": True,
    "groups": groups,
    "dimension_tuples": dimension_tuples,
    "composition_count": composition_count,
    "non_generation_tests": non_generation,
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Finite exact checks; the all-rank and all-characteristic claims are proved in the accompanying TeX.",
    "reconstruction": "Fresh certificate after the 2026-11-20 environment replacement; not the lost raw-V8 source."
}
out = Path(__file__).resolve().parents[1] / "output" / "alternating_quadratic_growth_reconstructed.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))

