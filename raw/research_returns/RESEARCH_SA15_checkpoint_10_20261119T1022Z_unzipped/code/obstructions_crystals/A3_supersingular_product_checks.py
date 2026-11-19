#!/usr/bin/env python3
"""Exact supplementary certificate for the geometric all-degree rank proof.

The finite computations certify the stated algebraic examples and retained
Cartier witnesses.  The unbounded degree theorem is proved in the TeX file.
Only Python's standard library is used.
"""
import hashlib
import itertools
import json
import math
import time
from pathlib import Path

started = time.perf_counter()

# F4 = F2[w]/(w^2+w+1), represented by two bits.
def fm(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return r

def pa(a, b):
    r = dict(a)
    for t, c in b.items():
        r[t] = r.get(t, 0) ^ c
        if not r[t]:
            del r[t]
    return r

def pm(a, b):
    r = {}
    for (i, j), c in a.items():
        for (u, v), d in b.items():
            r = pa(r, {(i+u, j+v): fm(c, d)})
    return r

def ps(c, a):
    return {t: fm(c, d) for t, d in a.items() if fm(c, d)}

one, x, y = {(0, 0): 1}, {(1, 0): 1}, {(0, 1): 1}
equation = pa(pa(pm(y, y), y), pm(pm(x, x), x))

def affine(a, c):
    return pa(x, ps(a, one)), pa(pa(y, ps(fm(a, a), x)), ps(c, one))

def subst(p, xy):
    r = {}
    for (i, j), c in p.items():
        t = ps(c, one)
        for _ in range(i):
            t = pm(t, xy[0])
        for _ in range(j):
            t = pm(t, xy[1])
        r = pa(r, t)
    return r

def compose(f, g):
    return tuple(subst(p, g) for p in f)

I, J = affine(1, 2), affine(2, 2)
negative = (x, pa(y, one))
assert subst(equation, I) == equation
assert subst(equation, J) == equation
assert compose(I, I) == compose(J, J) == negative
assert compose(I, J) == compose(negative, compose(J, I))

# Hamilton basis multiplication: (coefficient sign, basis index).
table = [[(1, j) for j in range(4)]]
table += [[(1, 1), (-1, 0), (1, 3), (-1, 2)],
          [(1, 2), (-1, 3), (-1, 0), (1, 1)],
          [(1, 3), (1, 2), (-1, 1), (-1, 0)]]
for a, b, c in itertools.product(range(4), repeat=3):
    s, q = table[a][b]
    t, r = table[q][c]
    u, v = table[b][c]
    w, z = table[a][v]
    assert (s*t, r) == (u*w, z)

# Symbolic coefficients of bar(q)*q and q*bar(q), with commuting variables.
def symbolic_norm(reverse=False):
    out = [dict() for _ in range(4)]
    for a, b in itertools.product(range(4), repeat=2):
        sign, component = table[a][b]
        sign *= (1 if (b if reverse else a) == 0 else -1)
        powers = tuple(int(i == a)+int(i == b) for i in range(4))
        out[component][powers] = out[component].get(powers, 0)+sign
    return [{e:c for e,c in v.items() if c} for v in out]

expected = [{tuple(2*int(i == j) for i in range(4)): 1 for j in range(4)}, {}, {}, {}]
assert symbolic_norm() == expected == symbolic_norm(True)

# Deterministic nonnegative four-square witnesses, independently finite-checked.
bound = 4096
pairs = {}
for a in range(math.isqrt(bound)+1):
    for b in range(math.isqrt(bound-a*a)+1):
        pairs.setdefault(a*a+b*b, (a, b))
four_squares = []
for n in range(1, bound+1):
    witness = None
    for a in range(math.isqrt(n)+1):
        for b in range(math.isqrt(n-a*a)+1):
            rem = n-a*a-b*b
            if rem in pairs:
                witness = (a, b)+pairs[rem]
                break
        if witness is not None:
            break
    assert witness is not None and sum(c*c for c in witness) == n
    four_squares.append(witness)

degree_data = []
for d in range(1, 10001):
    m = 3*d
    genus = m*m+1
    if d % 2:
        nodes = m*m
        graph_rank = nodes-1
        assert graph_rank == genus-2
    else:
        a, b = 3, m-3
        assert a >= 3 and b >= 3 and a % 2 and b % 2
        nodes = 2*a*b
        genus_union = (a*a+1)+(b*b+1)+nodes-1
        graph_rank = (a*a-1)+(b*b-1)+nodes-1
        assert genus_union == genus and graph_rank == genus-4
    expected_rank = m*m-(1 if d % 2 else 3)
    assert graph_rank == expected_rank > 0
    if d <= 20:
        degree_data.append({'d':d, 'm':m, 'genus':genus, 'relative_dimension':m*m-1,
                            'generic_stable_rank':expected_rank})

# Independently re-evaluate all six retained exact F2 matrix witnesses.
def rank(columns):
    pivots = {}
    for c in columns:
        while c:
            r = c.bit_length()-1
            if r in pivots:
                c ^= pivots[r]
            else:
                pivots[r] = c
                break
    return len(pivots)

def apply(columns, v):
    out = 0
    while v:
        bit = v & -v
        v ^= bit
        out ^= columns[bit.bit_length()-1]
    return out

probe_path = Path(__file__).with_name('A3_supersingular_product_probe_output.json')
probe = json.loads(probe_path.read_text())
matrix_checks = []
for r in probe['results']:
    columns = r['certificate']['columns']
    section = r['certificate']['section_bits']
    assert apply(columns, section) == 0
    power = columns[:]
    seq = [len(columns)]
    for _ in range(len(columns)+1):
        seq.append(rank(power))
        if seq[-1] == seq[-2]:
            break
        power = [apply(columns, v) for v in power]
    assert seq == r['certificate']['rank_sequence']
    assert seq[-1] == r['best_stable_rank']
    assert seq[-1] == 9*r['degree']**2-(1 if r['degree'] % 2 else 3)
    matrix_checks.append({'degree':r['degree'], 'rank_sequence':seq})

result = {
    'status':'PASS',
    'scope':'Exact Q8, norm, finite four-square and degeneration arithmetic checks; six retained Cartier matrix witnesses. Infinite theorem proved geometrically in TeX.',
    'automorphism_field':'F2[w]/(w^2+w+1)',
    'automorphisms':{'i':['x+1','y+x+w'], 'j':['x+w','y+w^2*x+w']},
    'automorphism_checks':['curve equation preserved','i^2=j^2=[-1]','ij=[-1]ji'],
    'quaternion_associativity_cases':64,
    'symbolic_norm_identities_checked':2,
    'four_square_integer_bound':bound,
    'four_square_witnesses':four_squares,
    'degree_arithmetic_bound':10000,
    'first_twenty_degrees':degree_data,
    'retained_matrix_witnesses':matrix_checks,
    'probe_sha256':hashlib.sha256(probe_path.read_bytes()).hexdigest(),
    'elapsed_seconds':time.perf_counter()-started,
}
destination = Path(__file__).with_name('A3_supersingular_product_checks_output.json')
destination.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in {'four_square_witnesses','first_twenty_degrees'}},indent=2))
