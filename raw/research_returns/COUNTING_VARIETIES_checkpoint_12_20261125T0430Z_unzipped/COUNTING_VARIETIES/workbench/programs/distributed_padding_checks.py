#!/usr/bin/env python3
"""Exact finite tests of the distributed-padding support refinement.

Run: python3 distributed_padding_checks.py
Expected: 111 coefficient tests pass, plus the ternary cone counts printed.
This checks finite coefficients and counts, not geometric smoothness.
"""
import itertools
import json
import math
import random
from core_checks import add, mul, hasse


def permanent(matrix, p):
    n = len(matrix)
    return sum(math.prod(matrix[i][s[i]] for i in range(n))
               for s in itertools.permutations(range(n))) % p


def make_form(matrix, p, q):
    r = len(matrix)
    m, d = q - 1, q + 1
    assert r > 0 and r % (p - 1) == 0
    assert m > r + p - 1 and (m - r - p + 1) % (p - 1) == 0
    a = (m - r - p + 1) // (p - 1)
    row_product = {(0,) * r: 1}
    for row in matrix:
        factor = {}
        for j, c in enumerate(row):
            e = [0] * r
            e[j] = 1
            if c % p:
                factor[tuple(e)] = c % p
        row_product = mul(row_product, factor, p)
    f = {}
    for tag in range(p - 1):
        base = row_product if tag == 0 else {(1,) * r: 1}
        for e, c in base.items():
            ex = list(e) + [0] * (d - r)
            ex[r + tag] = p - 1
            for j in range(a):
                ex[r + p - 1 + tag * a + j] = p - 1
            ex[-2] = ex[-1] = 1
            f = add(f, {tuple(ex): -c if tag == 0 else c}, p)
    ex = [0] * d
    ex[0], ex[-2], ex[-1] = m, 1, 1
    f = add(f, {tuple(ex): 1}, p)
    for j in range(m + 1):
        ex = [0] * d
        ex[j] = d
        f = add(f, {tuple(ex): 1}, p)
    ex = [0] * d
    ex[0], ex[-1] = 1, q
    f = add(f, {tuple(ex): -1}, p)
    displayed_support = r + a + 3
    assert (p - 1) * displayed_support - d == (p - 2) * (r + 2)
    return f, displayed_support


def ternary_count(matrix):
    # r=2,Q=9: internal x=(a,b,t1,t2,v1,v2,v3,v4).
    p = 3
    slope_nonzero = slope_and_offset_zero = only_slope_zero = 0
    for x in itertools.product(range(p), repeat=8):
        a, b, t1, t2, v1, v2, v3, v4 = x
        row_product = math.prod((row[0] * a + row[1] * b) % p for row in matrix)
        A = (-t1 * t1 * v1 * v1 * v2 * v2 * row_product
             + t2 * t2 * v3 * v3 * v4 * v4 * a * b + pow(a, 8, p)) % p
        xsum = sum(z * z for z in x) % p
        for y in range(p):
            slope = (y * A - a) % p
            offset = (y * y + xsum) % p
            if slope:
                slope_nonzero += 1
            elif not offset:
                slope_and_offset_zero += 1
            else:
                only_slope_zero += 1
    cone = slope_nonzero + p * slope_and_offset_zero
    projective = (cone - 1) // (p - 1)
    assert projective % p == (1 + permanent(matrix, p)) % p
    return {'matrix': matrix, 'scalar': permanent(matrix, p),
            'slope_nonzero': slope_nonzero,
            'slope_and_offset_zero': slope_and_offset_zero,
            'only_slope_zero': only_slope_zero,
            'cone': cone, 'projective': projective}


def main():
    tests = 0
    for entries in itertools.product(range(3), repeat=4):
        matrix = [list(entries[:2]), list(entries[2:])]
        f, sigma = make_form(matrix, 3, 9)
        assert hasse(f, 3, 10) == permanent(matrix, 3)
        assert sigma == 7
        tests += 1
    rng = random.Random(20261124)
    for _ in range(24):
        matrix = [[rng.randrange(5) for _ in range(4)] for _ in range(4)]
        f, sigma = make_form(matrix, 5, 25)
        assert hasse(f, 5, 26) == permanent(matrix, 5)
        assert sigma == 11
        tests += 1
    for _ in range(6):
        matrix = [[rng.randrange(3) for _ in range(2)] for _ in range(2)]
        f, sigma = make_form(matrix, 3, 27)
        assert hasse(f, 3, 28) == permanent(matrix, 3)
        assert sigma == 16
        tests += 1
    counts = [ternary_count(m) for m in (
        [[1, 0], [0, 1]], [[1, 1], [1, 1]], [[1, 1], [1, 2]],
        [[0, 0], [1, 1]])]
    print(json.dumps({'coefficient_tests': tests,
                      'support_excess_identity': 'K=(p-2)(r+2)',
                      'ternary_counts': counts}, indent=2))


if __name__ == '__main__':
    main()
