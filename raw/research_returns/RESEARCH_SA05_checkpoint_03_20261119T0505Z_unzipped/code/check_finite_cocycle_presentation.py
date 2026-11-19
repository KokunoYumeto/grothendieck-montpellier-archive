#!/usr/bin/env python3
"""Exact small-group certificates for (B.A5)--(B.A7).

These are synthetic finite-group checks, NOT enumerations of all number
fields in the arithmetic algorithm. Expected answers are derived by the
compact-support H^0/H^1 exact sequence for the displayed cyclic/S3 groups.
No floating-point arithmetic is used.
"""
from itertools import product, permutations
from pathlib import Path
import json
import time


def cyclic(n):
    return list(range(n)), lambda a, b: (a + b) % n


def symmetric3():
    elements = list(permutations(range(3)))
    return elements, lambda a, b: tuple(a[b[i]] for i in range(3))


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))


def compute(name, elements, multiply, action, local, q, expected):
    index = {g: i for i, g in enumerate(elements)}
    table = [[index[multiply(g, h)] for h in elements] for g in elements]
    a = [action(g) % q for g in elements]
    assert all((a[i] * a[j] - a[table[i][j]]) % q == 0
               for i in range(len(a)) for j in range(len(a)))
    local_idx = [index[d] for d in local]
    cocycles = []
    for z in product(range(q), repeat=len(elements)):
        if all((z[table[i][j]] - z[i] - a[i] * z[j]) % q == 0
               for i in range(len(a)) for j in range(len(a))):
            cocycles.append(z)
    pairs = [z + (b,) for z in cocycles for b in range(q)
             if all((z[i] - (a[i] - 1) * b) % q == 0 for i in local_idx)]
    boundaries = [tuple(((x - 1) * c) % q for x in a) + (c,)
                  for c in range(q)]
    pairset = set(pairs)
    assert all(b in pairset for b in boundaries)

    def add(v, w):
        return tuple((x + y) % q for x, y in zip(v, w))

    def canonical(v):
        return min(add(v, b) for b in boundaries)

    reps = sorted({canonical(v) for v in pairs})
    zero = canonical(tuple(0 for _ in range(len(elements) + 1)))
    assert len(reps) == expected
    orders = {}
    for v in reps:
        w = zero
        for k in range(1, q + 1):
            w = canonical(add(w, v))
            if w == zero:
                orders[v] = k
                break
        assert v in orders
    gen = max(reps, key=lambda v: orders[v])
    assert orders[gen] == len(reps)  # all cases here are cyclic
    return dict(name=name, modulus=q, group_order=len(elements),
                local_subgroup_order=len(local), crossed_cocycles=len(cocycles),
                relative_cocycles=len(pairs), boundaries=len(boundaries),
                quotient_order=len(reps), cyclic_generator=list(gen),
                generator_order=orders[gen], expected_order=expected, passed=True)


def main():
    start = time.perf_counter()
    c2, mul2 = cyclic(2)
    c3, mul3 = cyclic(3)
    s3, muls = symmetric3()
    identity = (0, 1, 2)
    transposition = (1, 0, 2)
    a3 = [p for p in s3 if sign(p) == 1]
    cases = [
        ("C2_sign_full_local_q3", c2, mul2, lambda g: (-1)**g, c2, 3, 1),
        ("C2_sign_trivial_local_q3", c2, mul2, lambda g: (-1)**g, [0], 3, 3),
        ("C3_trivial_trivial_local_q3", c3, mul3, lambda g: 1, [0], 3, 3),
        ("S3_sign_C2_local_q3", s3, muls, sign, [identity, transposition], 3, 3),
        ("S3_sign_C3_local_q3", s3, muls, sign, a3, 3, 3),
        ("S3_sign_full_local_q3", s3, muls, sign, s3, 3, 1),
        ("C3_trivial_trivial_local_q9", c3, mul3, lambda g: 1, [0], 9, 3),
        ("C2_sign_trivial_local_q9", c2, mul2, lambda g: (-1)**g, [0], 9, 9),
    ]
    results = [compute(*case) for case in cases]
    output = dict(scope="Synthetic exact finite-group checks; no arithmetic field enumeration",
                  cases=results, all_passed=all(r["passed"] for r in results),
                  wall_seconds=time.perf_counter()-start)
    path = Path(__file__).with_name("check_finite_cocycle_presentation_output.json")
    path.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
