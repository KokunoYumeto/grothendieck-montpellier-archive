#!/usr/bin/env python3
"""Exact finite checks for D:superperfect-quadratic-obstruction.

This checks the explicit permutation and numerical ingredients of the
infinite-family proof. It does NOT compute Schur multipliers or rerun the
small-degree cohomology computations cited by GKKL.
"""
from collections import deque
from fractions import Fraction
from itertools import product
from math import factorial, prod
from pathlib import Path
import hashlib
import json
import time

start = time.perf_counter()
checks = 0
def check(condition):
    global checks
    checks += 1
    assert condition

def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))
def inverse(a):
    b = [0] * len(a)
    for i, j in enumerate(a):
        b[j] = i
    return tuple(b)
def cycle(n, entries):
    a = list(range(n))
    for i, j in zip(entries, entries[1:] + entries[:1]):
        a[i] = j
    return tuple(a)
def parity(a):
    return sum(a[i] > a[j] for i in range(len(a))
               for j in range(i + 1, len(a))) % 2
def power(a, exponent):
    out = tuple(range(len(a)))
    while exponent:
        if exponent & 1:
            out = compose(out, a)
        a = compose(a, a)
        exponent >>= 1
    return out

# Exact quotient-generator checks in two small groups. The proof covers
# every odd n by the consecutive-three-cycle induction.
orders = []
for n in (5, 7):
    identity = tuple(range(n))
    generators = [cycle(n, list(range(n))), cycle(n, [0, 1, 2])]
    seen = {identity}
    queue = deque([identity])
    while queue:
        a = queue.popleft()
        for g in generators:
            b = compose(a, g)
            check(parity(b) == 0)
            if b not in seen:
                seen.add(b)
                queue.append(b)
    check(len(seen) == factorial(n) // 2)
    orders.append({"n": n, "generated_order": len(seen)})

# Odd-cycle elementary abelian subgroups in the actual degree range.
for n in range(31, 152, 2):
    identity = tuple(range(n))
    long_cycle = cycle(n, list(range(n)))
    three = cycle(n, [0, 1, 2])
    check(parity(long_cycle) == 0)
    check(6 * (n // 5) >= n)
    for i in range(n - 2):
        conjugator = power(long_cycle, i)
        check(compose(compose(conjugator, three), inverse(conjugator))
              == cycle(n, [i, i + 1, i + 2]))
    for prime in (3, 5):
        blocks = [cycle(n, list(range(prime * j, prime * (j + 1))))
                  for j in range(n // prime)]
        check(len(blocks) == n // prime)
        supports = []
        for a in blocks:
            check(parity(a) == 0)
            check(power(a, prime) == identity)
            check(a != identity)
            supports.append({i for i in range(n) if a[i] != i})
        for j in range(len(blocks)):
            for h in range(j):
                check(supports[j].isdisjoint(supports[h]))
                check(compose(blocks[j], blocks[h])
                      == compose(blocks[h], blocks[j]))

# Support-square and finite counting inequalities, all by integer arithmetic.
for length in range(1, 5):
    for dims in product(range(2, 9), repeat=length):
        rank = prod(dims)
        check(sum(d * d for d in dims) <= rank * rank)
        check(2 ** length <= rank)
        check(sum((6 * d) ** 2 for d in dims) <= 36 * rank * rank)
for rank in range(2, 129):
    floor_log = rank.bit_length() - 1
    check((6 * rank) ** (1 + floor_log) <= 2 ** (2 * rank * rank))
    check(rank <= 2 ** (rank * rank))
    check(74 * rank * rank + rank * rank == 75 * rank * rank)
    check(2 ** (rank - 1) <= 2 ** (rank * rank))

# Truncated degree-two Kunneth coefficients with the proven single-factor
# upper bounds, including inactive (trivial) factors.
for length in range(7):
    for active in product((False, True), repeat=length):
        for dim in (2, 3, 5):
            coefficients = [1, 0, 0]
            rank = 1
            for flag in active:
                local = [0, 2 * dim, 5 * dim] if flag else [1, 0, 0]
                if flag:
                    rank *= dim
                coefficients = [
                    sum(coefficients[j] * local[i - j] for j in range(i + 1))
                    for i in range(3)
                ]
            check(coefficients[1] <= 2 * rank)
            check(coefficients[2] <= 5 * rank)
            if sum(active) >= 3:
                check(coefficients[1:] == [0, 0])
            if sum(active) == 0:
                check(coefficients == [1, 0, 0])
check(Fraction(35, 12) + 2 < 5)
check(2 * 2 <= 5)

# Explicit finite witnesses to the generator-count contradiction.
growth_witnesses = []
for generators in range(1, 33):
    n = max(31, (2 * generators + 1) ** 2)
    if n % 2 == 0:
        n += 1
    check(2 ** n > n ** generators)
    check(factorial(n) <= n ** n)
    growth_witnesses.append({"generators": generators, "odd_degree": n})

result = {
    "statement": "D:superperfect-quadratic-obstruction",
    "version": 1,
    "status": "PASS",
    "assertions": checks,
    "runtime_seconds": time.perf_counter() - start,
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "small_quotient_generation": orders,
    "family_odd_degrees": [31, 151],
    "counting_ranks": [2, 128],
    "growth_witnesses": growth_witnesses,
    "scope": ("Exact permutation, support, counting, and low-degree tensor "
              "coefficient checks. The Schur-multiplier computation and the "
              "GKKL cohomology estimates are cited literature inputs, not "
              "computed by this program.")
}
target = Path(__file__).resolve().parents[1] / "output" / "superperfect_product.json"
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
