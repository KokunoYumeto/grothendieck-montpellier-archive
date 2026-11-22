#!/usr/bin/env python3
"""Exact finite certificates for divisible-nil averaging and reduced fibres.

Checks both averaging homotopies on every basis cochain for C2,C3,S3
acting by conjugation on the endomorphisms of their indicated permutation
representations. Checks the integral polynomial coefficients of the reduced
fibre involutions, sign conjugation, and the first three primary detectors.
"""
from itertools import permutations, product
from pathlib import Path
from time import perf_counter
import json
import numpy as np

START = perf_counter()

def composition(a, b):
    return tuple(a[b[i]] for i in range(len(a)))

def group_certificate(name, elements):
    N, n = len(elements), len(elements[0])
    m = n*n
    pos = {g: i for i, g in enumerate(elements)}
    mul = [[pos[composition(g, h)] for h in elements] for g in elements]
    action = []
    for g in elements:
        matrix = np.zeros((m, m), dtype=np.int64)
        for i, j in product(range(n), repeat=2):
            matrix[g[i]*n+g[j], i*n+j] = 1
        action.append(matrix)
    for g, h in product(range(N), repeat=2):
        assert np.array_equal(action[g] @ action[h], action[mul[g][h]])

    # N*d(g)=S-gS+sum_h (g*d(h)-d(gh)+d(g)) for all 1-cochains.
    one_checks = 0
    for i, a in product(range(N), range(m)):
        d = np.zeros((N, m), dtype=np.int64)
        d[i, a] = 1
        S = d.sum(axis=0)
        for g in range(N):
            dd_sum = sum((action[g] @ d[h] - d[mul[g][h]] + d[g]
                          for h in range(N)), np.zeros(m, dtype=np.int64))
            assert np.array_equal(N*d[g], S-action[g] @ S+dd_sum)
        one_checks += 1

    # N*c(g,h)=S(g)+g*S(h)-S(gh)-sum_l d2(c)(g,h,l).
    two_checks = 0
    for i, j, a in product(range(N), range(N), range(m)):
        c = np.zeros((N, N, m), dtype=np.int64)
        c[i, j, a] = 1
        S = c.sum(axis=1)
        for g, h in product(range(N), repeat=2):
            d2sum = sum((action[g] @ c[h, l] - c[mul[g][h], l]
                         + c[g, mul[h][l]] - c[g, h] for l in range(N)),
                        np.zeros(m, dtype=np.int64))
            actual = S[g] + action[g] @ S[h] - S[mul[g][h]] - d2sum
            assert np.array_equal(N*c[g, h], actual)
        two_checks += 1
    return {'group': name, 'order': N, 'coefficient_module_dimension': m,
            'one_cochain_basis_checked': one_checks,
            'two_cochain_basis_checked': two_checks,
            'identity_arithmetic': 'integer identities before dividing by |G|'}

groups = [group_certificate('C2', [(0, 1), (1, 0)]),
          group_certificate('C3', [(0, 1, 2), (1, 2, 0), (2, 0, 1)]),
          group_certificate('S3', list(permutations(range(3))))]

def eye(n):
    return np.eye(n, dtype=np.int64)

def companion(q):
    d = q.bit_length()-1
    b = np.zeros((d, d), dtype=np.int64)
    for j in range(d-1):
        b[j+1, j] = 1
    b[:, -1] = [(q >> j) & 1 for j in range(d)]
    return b

def rem(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

def irreducible(q):
    d = q.bit_length()-1
    return all(rem(q, f) for e in range(1, d//2+1)
               for f in range(1 << e, 1 << (e+1)))

def mul_poly(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r

def artin_schreier(q):
    r = 0
    for j in range(q.bit_length()-1, -1, -1):
        r = mul_poly(r, 6) ^ ((q >> j) & 1)
    return r

def eval_matrix(q, a):
    r = np.zeros_like(a)
    for j in range(q.bit_length()-1, -1, -1):
        r = (r @ a + ((q >> j) & 1)*eye(len(a))) % 2
    return r

def rank(a):
    pivots = {}
    for j in range(a.shape[1]):
        v = sum((int(x) & 1) << i for i, x in enumerate(a[:, j]))
        while v:
            i = v.bit_length()-1
            if i not in pivots:
                pivots[i] = v
                break
            v ^= pivots[i]
    return len(pivots)

qs = [3, 7, 25]
fs = [artin_schreier(q) for q in qs]
assert all(irreducible(q) for q in qs+fs)
witnesses = []
for q, f in zip(qs, fs):
    b = companion(q)
    d = len(b)
    z = np.zeros_like(b)
    t0 = np.block([[eye(d), z], [z, -eye(d)]])
    U = np.block([[b, b], [b, b]])
    J = np.block([[z, eye(d)], [-eye(d), z]])
    # T=T0+xU; every nonconstant error coefficient divisible by2
    # vanishes in Z_(2)[x]/(2x). Constant coefficients are exact.
    assert np.array_equal(t0 @ t0, eye(2*d))
    assert not np.any((t0 @ U + U @ t0) % 2)
    assert not np.any(U @ U % 2)
    assert not np.any(J @ t0 + t0 @ J)
    assert not np.any((J @ U + U @ J) % 2)
    t4 = (t0 + 2*U) % 4
    assert np.array_equal(t4 @ t4 % 4, eye(2*d))
    assert not np.any((t4-eye(2*d)) % 2)
    N = ((t4-eye(2*d)) % 4) // 2
    assert np.array_equal((N @ N + N) % 2, np.block([[b, z], [z, b]]) % 2)
    assert not np.any(eval_matrix(f, N))
    parities = []
    for fsingle in fs:
        a = eval_matrix(fsingle, N)
        power = eye(2*d)
        for _ in range(2*d):
            power = power @ a % 2
        dim = 2*d-rank(power)
        degree = fsingle.bit_length()-1
        assert dim % degree == 0
        parities.append((dim//degree) % 2)
    assert parities == [int(f == f2) for f2 in fs]
    witnesses.append({'q_bits': q, 'f_bits': f, 'rank': 2*d,
                      'N': N.tolist(), 'parity_vector': parities})

report = {'statement_ids': ['C:divisible_nil_invariance', 'C:reduced_regular_fibres'],
          'averaging_certificates': groups,
          'averaging_scope': 'both homotopy identities on every basis cochain; hence all cochains',
          'reduced_ring': 'Z_(2)[x]_(2,x)/(2x)',
          'reduced_matrix_scope': 'first three trace-one companion witnesses, ranks2,4,8',
          'witnesses': witnesses, 'all_checks_passed': True,
          'runtime_seconds': round(perf_counter()-START, 6)}
out = Path(__file__).resolve().parents[1]/'logs'/'C_finish_nilfibres.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
