#!/usr/bin/env python3
"""Exact connected-partition expansion through order six.

Run: python checks/rook_cumulants.py
Expected: all rational identities PASS; writes checks/rook_cumulants.json.
Only Python's standard library is needed. No floating-point arithmetic is used.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import factorial
from pathlib import Path
import json
import random


def partitions(n):
    if n == 0:
        yield ()
        return
    for p in partitions(n - 1):
        yield p + ((n - 1,),)
        for j in range(len(p)):
            yield p[:j] + (p[j] + (n - 1,),) + p[j + 1:]


def mobius(p):
    r = 1
    for b in p:
        r *= (-1) ** (len(b) - 1) * factorial(len(b) - 1)
    return r


def connected(a):
    nr, nc = len(a), len(a[0])
    reached = {0}
    todo = [0]
    while todo:
        u = todo.pop()
        neighbors = ([nr + j for j in range(nc) if a[u][j]] if u < nr
                     else [i for i in range(nr) if a[i][u - nr]])
        for v in neighbors:
            if v not in reached:
                reached.add(v)
                todo.append(v)
    return len(reached) == nr + nc


def canonical(a):
    return min(tuple(tuple(a[i][j] for j in c) for i in r)
               for r in permutations(range(len(a)))
               for c in permutations(range(len(a[0]))))


def terms(k):
    ps = [p for p in partitions(k) if all(len(b) >= 2 for b in p)]
    out = defaultdict(Fraction)
    pairs = 0
    for p in ps:
        for q in ps:
            a = tuple(tuple(len(set(b) & set(c)) for c in q) for b in p)
            if connected(a):
                out[canonical(a)] += Fraction(mobius(p) * mobius(q), factorial(k))
                pairs += 1
    return dict(sorted(out.items(), key=lambda x: (len(x[0]), len(x[0][0]), x[0]))), len(ps), pairs


def contraction(t, a):
    nr, nc = len(t), len(t[0])
    # Sum over column labels first: each column vertex is independent.
    total = 0
    for rows in product(range(nr), repeat=len(a)):
        v = 1
        for j in range(len(a[0])):
            v *= sum(__import__('functools').reduce(
                lambda x, y: x * y,
                (t[rows[i]][c] ** a[i][j] for i in range(len(a))), 1)
                for c in range(nc))
        total += v
    return total


def rook_coefficients(t, degree=6):
    # Dynamic program: process rows, tracking occupied columns.
    d = {0: 1}
    for row in t:
        nxt = dict(d)
        for mask, v in d.items():
            if mask.bit_count() >= degree:
                continue
            for j, x in enumerate(row):
                if not mask & (1 << j):
                    nm = mask | (1 << j)
                    nxt[nm] = nxt.get(nm, 0) + v * x
        d = nxt
    s = [0] * (degree + 1)
    for mask, v in d.items():
        s[mask.bit_count()] += v
    return s


def log_coefficients(s):
    # R' = R (log R)' is an independent exact calculation.
    c = [Fraction(0)] * len(s)
    for k in range(1, len(s)):
        c[k] = Fraction(s[k]) - sum(Fraction(j, k) * c[j] * s[k-j]
                                    for j in range(1, k))
    return c


def dc_matrix(nr, nc, rng):
    t = [[rng.randrange(-3, 4) for _ in range(nc-1)] for _ in range(nr-1)]
    for row in t:
        row.append(-sum(row))
    t.append([-sum(t[i][j] for i in range(nr-1)) for j in range(nc)])
    return t


def main():
    data = {}
    expansions = {}
    for k in range(2, 7):
        a, count, pairs = terms(k)
        expansions[k] = a
        data[str(k)] = {'singleton_free_partitions': count, 'connected_pairs': pairs,
                        'terms': [{'matrix': m, 'coefficient': str(v)} for m, v in a.items()]}
        print('c_%d: %d graph types, %d connected partition pairs' % (k, len(a), pairs))
        for m, v in a.items():
            print(' ', str(v), m)
    rng = random.Random(20261125)
    tests = []
    for nr, nc in [(3, 3), (4, 5), (5, 6), (6, 6)]:
        for repeat in range(3):
            t = dc_matrix(nr, nc, rng)
            s = rook_coefficients(t)
            c = log_coefficients(s)
            for k, a in expansions.items():
                value = sum(v * contraction(t, m) for m, v in a.items())
                assert value == c[k], (nr, nc, k, value, c[k])
            tests.append({'shape': [nr, nc], 'matrix': t,
                          'rook': s, 'cumulants': [str(v) for v in c], 'result': 'PASS'})
    data['checks'] = tests
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(data, indent=2) + '\n')
    print('PASS: 60 exact rational comparisons on 12 doubly centred matrices.')


if __name__ == '__main__':
    main()
