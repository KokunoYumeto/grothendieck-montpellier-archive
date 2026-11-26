#!/usr/bin/env python3
"""Independent rational-series audit of the decorated determinant entropies.

No generator or floating logarithm is imported. Logarithms use an exact
atanh series with a positive rational geometric tail bound. This checks
the entropy inequality independently of the generator's large powers.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parents[1]
TERMS = 64

def reduced_log_bounds(x):
    assert F(1) <= x <= F(2)
    z = (x - 1) / (x + 1)
    partial = 2 * sum((z ** (2*j+1) / (2*j+1) for j in range(TERMS)), F(0))
    tail = 2*z**(2*TERMS+1) / ((2*TERMS+1)*(1-z*z))
    return partial, partial + tail

L2, U2 = reduced_log_bounds(F(2))

def integer_log_bounds(x):
    k = x.bit_length()-1
    lo, hi = reduced_log_bounds(F(x, 1 << k))
    return k*L2+lo, k*U2+hi

rows = []
for N in range(1, 8):
    q = 2**N
    n = 64*q*q
    shape = [21*(q*q+1)+22*q] + [21+22*q]*(q-1) + [21]*(q*q-q)
    assert len(shape) == q*q and sum(shape) == n
    assert all(shape[i] >= shape[i+1] for i in range(len(shape)-1))
    from collections import Counter
    multiplicities = Counter(shape)
    coefficient = F(6) + F(3*N, 4)
    lower, upper = coefficient*L2, coefficient*U2
    for value, count in multiplicities.items():
        lo, hi = integer_log_bounds(value)
        weight = F(count*value, n)
        lower -= weight*hi
        upper -= weight*lo
    assert lower <= upper
    status = 'above' if lower > 0 else 'below' if upper < 0 else 'unresolved'
    assert status == ('above' if N <= 6 else 'below')
    bounds = {'lower': str(lower), 'upper': str(upper)}
    rows.append({
        'q': q, 'degree': n, 'status': status,
        'natural_log_entropy_margin_bounds': bounds,
        'bounds_sha256': sha256(json.dumps(bounds, sort_keys=True).encode()).hexdigest(),
        'shape': [[v, c] for v, c in multiplicities.items()],
    })

result = {
    'status': 'PASS', 'method': 'Exact rational logarithm bounds from 64 atanh terms',
    'generator_imported': False, 'floating_point_used': False,
    'scope': 'The proved dominance bound passes q2..64 and fails q128; no system inconsistency inferred.',
    'rows': rows,
}
out = ROOT/'outputs/rt_decorated_entropy_verified.json'
tmp = out.with_suffix('.tmp')
tmp.write_text(json.dumps(result, indent=2)+'\n')
tmp.replace(out)
print(json.dumps({'status': 'PASS', 'comparisons': [{'q': r['q'], 'status': r['status']} for r in rows]}))
