"""Standalone integer certificate for the seven-matrix U3 Hecke proof.

No input file, symbolic package, search heuristic, or floating arithmetic.
The correspondence with the Hecke operator is proved in u3_hecke_section.tex.
"""
from pathlib import Path
from itertools import permutations, product
from math import isqrt, prod
import json


def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def conj(x):
    return x[0]-x[1], -x[1]


def norm(x):
    return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]


def dot(v, w):
    entries = [mul(conj(x), y) for x, y in zip(v, w)]
    return tuple(sum(x[j] for x in entries) for j in range(2))


PARTITIONS = [(5, 0, 0), (4, 1, 0), (3, 2, 0), (3, 1, 1), (2, 2, 1)]
COEFFICIENTS = [2, -25, 20, 320, -360]
TERMS = {exp: c for p, c in zip(PARTITIONS, COEFFICIENTS)
         for exp in set(permutations(p))}


def f(x):
    return sum(c*prod(t**e for t, e in zip(x, exp)) for exp, c in TERMS.items())


DATA = [
    (7, (3, 1), [
        ((1, 1, 0), 12, [
            [(-2, -2), (-2, -1), (0, 0)],
            [(1, -1), (0, 2), (0, 0)],
            [(0, 0), (0, 0), (-3, -1)]]),
        ((1, 1, 1), 36, [
            [(-2, -1), (-2, -1), (-1, -1)],
            [(-2, -1), (1, 0), (1, 2)],
            [(1, 0), (-2, -1), (1, 2)]])
    ], 157899, {2: 3, 3: 5, 13: 1, 43: 1, 47: 1, 271: 1}),
    (13, (4, 1), [
        ((1, 1, 0), 12, [
            [(-4, -2), (-1, -1), (0, 0)],
            [(0, -1), (-2, 2), (0, 0)],
            [(0, 0), (0, 0), (-4, -1)]]),
        ((1, 2, 0), 12, [
            [(-3, -3), (-2, -2), (0, 0)],
            [(0, 2), (0, -3), (0, 0)],
            [(0, 0), (0, 0), (-4, -1)]]),
        ((1, 1, 1), 36, [
            [(-3, -2), (-2, -1), (-2, -1)],
            [(1, -1), (-2, -1), (1, 3)],
            [(1, -1), (1, 3), (-2, -1)]]),
        ((1, 1, 2), 72, [
            [(-3, -3), (-2, -1), (-1, -1)],
            [(0, 1), (-2, -1), (3, 0)],
            [(1, -1), (-1, 2), (1, 2)]]),
        ((1, 2, 2), 36, [
            [(-3, -1), (-2, -1), (-2, -1)],
            [(-2, -1), (0, -1), (3, 3)],
            [(-2, -1), (3, 3), (0, -1)]])
    ], 6110859, {2: 5, 3: 5, 13: 1, 47: 1, 337: 1, 14551: 1})
]

lap = {}
for exp, coefficient in TERMS.items():
    for i, n in enumerate(exp):
        if n:
            target = list(exp)
            target[i] -= 1
            target = tuple(target)
            lap[target] = lap.get(target, 0)+coefficient*n*n
assert all(v == 0 for v in lap.values()) and f((1, 0, 0)) == 2

reports = []
for p, pi, representatives, scaled, factors in DATA:
    assert norm(pi) == p
    root = (-pi[0]*pow(pi[1], -1, p)) % p
    units = {(a+b*root) % p for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]}
    assert len(units) == 6
    assert units == (set(range(1, p)) if p == 7 else {a*a % p for a in range(1, p)})
    covered = set()
    table = [{'norms': [p, 0, 0], 'multiplicity': p+2, 'f_value': f((p, 0, 0))}]
    total = (p+2)*f((p, 0, 0))
    for ell, multiplicity, matrix in representatives:
        orbit = {(1, ell[1]*a % p, ell[2]*b % p) for a, b in product(units, repeat=2)}
        orbit |= {(1, x[2], x[1]) for x in list(orbit)}
        assert len(orbit) == multiplicity and not (orbit & covered)
        covered |= orbit
        columns = list(zip(*matrix))
        for i, v in enumerate(columns):
            for j, w in enumerate(columns):
                assert dot(v, w) == ((p, 0) if i == j else (0, 0))
        nonzero = False
        for v in columns:
            red = tuple((a+b*root) % p for a, b in v)
            if any(red):
                nonzero = True
                scale = pow(next(a for a in red if a), -1, p)
                assert tuple(a*scale % p for a in red) == ell
        assert nonzero
        norms = sorted([norm(x) for x in matrix[0]], reverse=True)
        value = f(norms)
        total += multiplicity*value
        table.append({'line': ell, 'norms': norms, 'multiplicity': multiplicity, 'f_value': value})
    assert covered == {(1, a, b) for a, b in product(range(p), repeat=2) if a or b}
    assert total == 2*scaled
    difference = p**12+p**6+1-scaled
    assert difference == prod(q**e for q, e in factors.items())
    assert all(all(q % d for d in range(2, isqrt(q)+1)) for q in factors)
    reports.append({'p': p, 'cosets': p*p+p+1, 'table': table,
                    'weighted_sum': total, 'scaled_trace': scaled,
                    'comparison_difference': difference, 'prime_factorization': factors})

output = {'status': 'PASS seven explicit matrices and exhaustive unit orbits', 'results': reports}
Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
