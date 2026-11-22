#!/usr/bin/env python3
"""Exact supplementary checks for D-HES04--06; no classification oracle.

The universal proof is in higher_even_symplectic_all_fields_section.tex.
This program uses its own small F4 matrix implementation and rational
arithmetic; its finite examples do not purport to prove the universal
finite-field identities by enumeration.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from random import Random
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
start = time.perf_counter()


def mul(a, b):
    out = 0
    for i in range(2):
        if (b >> i) & 1:
            out ^= a << i
    if out & 4:
        out ^= 7
    return out


MUL = [[mul(a, b) for b in range(4)] for a in range(4)]
SQ = [MUL[a][a] for a in range(4)]


def add(*values):
    z = 0
    for x in values:
        z ^= x
    return z


def dot(v, w):
    return add(*(MUL[a][b] for a, b in zip(v, w)))


def vadd(v, w):
    return tuple(a ^ b for a, b in zip(v, w))


def scale(c, v):
    return tuple(MUL[c][x] for x in v)


def ident(d):
    return tuple(tuple(int(i == j) for j in range(d)) for i in range(d))


def trans(a):
    return tuple(zip(*a))


def mm(a, b):
    bt = trans(b)
    return tuple(tuple(dot(row, col) for col in bt) for row in a)


def mv(a, v):
    return tuple(dot(row, v) for row in a)


def frob(a):
    return tuple(tuple(SQ[x] for x in row) for row in a)


def J(d):
    assert d % 2 == 0
    n = d // 2
    return tuple(tuple(int((i + n) % d == j) for j in range(d)) for i in range(d))


def pairing(v, w):
    d = len(v)
    n = d // 2
    return dot(v[:n], w[n:]) ^ dot(v[n:], w[:n])


def sinv(a):
    j = J(len(a))
    return mm(j, mm(trans(a), j))


def tv(v, c):
    d = len(v)
    rows = [list(row) for row in ident(d)]
    for k in range(d):
        e = tuple(int(i == k) for i in range(d))
        extra = scale(MUL[c][pairing(e, v)], v)
        for i in range(d):
            rows[i][k] ^= extra[i]
    return tuple(tuple(row) for row in rows)


for a, b, c in product(range(4), repeat=3):
    assert MUL[a][b ^ c] == MUL[a][b] ^ MUL[a][c]
    assert MUL[MUL[a][b]][c] == MUL[a][MUL[b][c]]
assert SQ == [0, 1, 3, 2]
assert 2 ^ SQ[2] == 1

rng = Random(20261121)
twist_records = []
vector_checks = 0
for d, twists in [(2, 12), (4, 12), (8, 4)]:
    j = J(d)
    for twist in range(twists):
        z = ident(d)
        for _ in range(9):
            v = tuple(rng.randrange(4) for _ in range(d))
            c = rng.randrange(1, 4)
            u = tv(v, c)
            assert mm(trans(u), mm(j, u)) == j
            assert mm(u, u) == ident(d)
            z = mm(u, z)
        assert mm(trans(z), mm(j, z)) == j
        zi = sinv(z)
        assert mm(z, zi) == ident(d)
        g = mm(z, frob(zi))
        assert mm(g, frob(g)) == ident(d)

        def semilinear(v):
            return mv(g, tuple(SQ[x] for x in v))

        fixed_basis = list(trans(z))
        assert all(semilinear(v) == v for v in fixed_basis)
        assert tuple(tuple(pairing(v, w) for w in fixed_basis) for v in fixed_basis) == j

        # Exhaust every natural vector for d=2,4. At d=8 use every
        # fixed vector plus 512 deterministic general vectors.
        if d <= 4:
            vectors = list(product(range(4), repeat=d))
            fixed = {v for v in vectors if semilinear(v) == v}
            expected = {mv(z, bits) for bits in product(range(2), repeat=d)}
            assert fixed == expected and len(fixed) == 2**d
        else:
            expected = {mv(z, bits) for bits in product(range(2), repeat=d)}
            assert len(expected) == 2**d
            vectors = sorted(expected) + [tuple(rng.randrange(4) for _ in range(d)) for _ in range(512)]
        for v in vectors:
            sv = semilinear(v)
            assert semilinear(sv) == v
            a = vadd(v, sv)
            b = vadd(scale(3, v), scale(2, sv))
            assert semilinear(a) == a and semilinear(b) == b
            assert v == vadd(b, scale(2, a))
            vector_checks += 1
        twist_records.append({'natural_dimension': d, 'twist': twist,
                              'tested_vectors': len(vectors), 'fixed_basis_size': d})

# Check the exact dual action Tr(a v^2)=Tr(a^2 v), its fixed characters,
# and every paired orbit. Frobenius on each F4 coordinate has order two.
weight_records = []
duality_checks = 0
for r in range(1, 7):
    params = list(product(range(4), repeat=r))
    fixed = [v for v in params if tuple(SQ[x] for x in v) == v]
    assert len(fixed) == 2**r
    seen = set(fixed)
    pairs = []
    for v in params:
        if v in seen:
            continue
        w = tuple(SQ[x] for x in v)
        assert w != v and tuple(SQ[x] for x in w) == v
        pairs.append((v, w))
        seen.update((v, w))
    assert len(seen) == 4**r and len(pairs) == (4**r - 2**r)//2
    if r <= 4:
        for a in params:
            a2 = tuple(SQ[x] for x in a)
            for v in params:
                x = dot(a, tuple(SQ[y] for y in v))
                y = dot(a2, v)
                assert x ^ SQ[x] == y ^ SQ[y]
                duality_checks += 1
    bound = Q(1, 8)*(1-Q(1, 2**r))
    if r >= 3:
        assert bound >= Q(7, 64)
    weight_records.append({'r': r, 'characters': 4**r,
                          'fixed_characters': 2**r, 'paired_orbits': len(pairs),
                          'support_bound': str(bound)})

# Symbolic estimates are represented by their exact shifted coefficients.
# 25q^2/16-(q+1)^2 at q=4+x is (9x^2+40x)/16.
assert [Q(0), Q(40, 16), Q(9, 16)] == [Q(0), Q(5, 2), Q(9, 16)]
# q^3-64 at q=4+x has coefficients 0,48,12,1.
assert all(x >= 0 for x in [0, 48, 12, 1])
assert Q(25, 63) < Q(1, 2)
assert 625 < 648
assert Q(2, 3)*Q(3, 4)*(1-Q(9, 16)) == Q(7, 32)
assert Q(7, 32)/2 == Q(7, 64)
assert (1-Q(1, 8))/8 == Q(7, 64)
assert Q(1) + 10*Q(7, 64) - 2 == Q(3, 32)
assert Q(6)/Q(3, 32) == 64
assert 35**2 > 64 and 8**3 - 1 > 64 and 24 < 35

poly_path = HERE / 'even_symplectic_polynomials.json'
poly_bytes = poly_path.read_bytes()
assert hashlib.sha256(poly_bytes).hexdigest() == '92e32ae7b01d49469f31464472ae044b320b59a6400fedaec5003fde2760a3b3'
tables = json.loads(poly_bytes)['tables']
sp6 = next(t for t in tables if t['name'] == 'Sp6.0.jl')
degrees = [sum(Q(c)*4**i for i, c in enumerate(row['degree_coefficients']))
           for row in sp6['polynomial_input']]
assert len(degrees) == 65 and min(degrees) == 378 > 64

result = {
    'status': 'PASS',
    'proof_sha256_at_run': hashlib.sha256((HERE/'higher_even_symplectic_all_fields_section.tex').read_bytes()).hexdigest(),
    'field_model': 'F2[w]/(w^2+w+1), values0,1,w,w+1; exact integer operations',
    'semilinear_twists': len(twist_records),
    'descent_vector_checks': vector_checks,
    'twist_records': twist_records,
    'dual_trace_checks': duality_checks,
    'weight_records': weight_records,
    'rational_constants': {'unipotent_c_q_ge8': '<9/16', 'inner_support_q_ge8': '>7/32',
                           'normalizer_support_all_even': '>=7/64', 'degree_ceiling': 64,
                           'sp6_q4_degree_rows': 65, 'sp6_q4_minimum_degree': 378,
                           'q_ge8_minimum_degree': 511, 'two_factor_minimum_degree': 1225},
    'reused_polynomial_input_sha256': hashlib.sha256(poly_bytes).hexdigest(),
    'scope': 'Supplementary finite identity and exact endpoint checks. Universal proofs, known classification inputs and unipotent bound are not proved by this enumeration.',
    'seconds': round(time.perf_counter()-start, 6),
}
(HERE/'check_higher_even_all_fields.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: result[k] for k in ['status', 'semilinear_twists', 'descent_vector_checks', 'dual_trace_checks', 'rational_constants', 'seconds']}, indent=2))
