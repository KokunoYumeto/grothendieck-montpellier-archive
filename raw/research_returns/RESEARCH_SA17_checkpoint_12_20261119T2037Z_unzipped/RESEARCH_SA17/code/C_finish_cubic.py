#!/usr/bin/env python3
"""Exact bounded checks for the cubic curvature invariant and order-three classes.

The independent general proof is in sections/C_finish_cubic.tex.  This script
checks actual Tate groups, maps and primary ranks over F2, and exact matrix
identities over Z[e]/e^3.  Finite coverage is stated explicitly in the output.
"""
from pathlib import Path
from itertools import product
from time import perf_counter
import json
import numpy as np

# Load definitions only: the earlier certificate's test loops are not executed.
exec(Path('code/C_finish_dualnumber_ring.py').read_text().split('\nobjects =')[0])
START = perf_counter()


def pmul(a, b):
    return [sum((a[i] @ b[j] for i in range(3) for j in range(3) if i+j == r),
                np.zeros((a[0].shape[0], b[0].shape[1]), dtype=np.int64))
            for r in range(3)]


def equal(a, b):
    return all(np.array_equal(x, y) for x, y in zip(a, b))


def curvature_data(t):
    t0, t1, t2 = t
    n = len(t0)
    assert np.array_equal(t0 @ t0, eye(n))
    assert not np.any(t0 @ t1 + t1 @ t0)
    assert not np.any(t0 @ t2 + t2 @ t0 + t1 @ t1)
    data = h_data(t0, t1)
    data['C'] = h_map(data, data, t1 @ t2 + t2 @ t1)
    h, N, b, c = data['h'], data['N'], data['B'], data['C']
    assert not np.any(b @ b % 2)
    assert not np.any((N @ c + c @ N) % 2)
    assert not np.any((b @ c + c @ b) % 2)
    values = []
    for q in QS:
        primary = matrix_power(matrix_poly(q, c), max(1, h))
        vb = independent(v for v in range(1 << h)
                         if not np.any(primary @ vec(v, h) % 2)
                         and not np.any(N @ vec(v, h) % 2))
        wb = independent(v for v in range(1 << h)
                         if not np.any(primary @ vec(v, h) % 2)
                         and not np.any((N + eye(h)) @ vec(v, h) % 2))
        r0 = len(independent(bits(b @ vec(v, h)) for v in vb))
        r1 = len(independent(bits(b @ vec(v, h)) for v in wb))
        assert len(vb) == len(wb) == r0+r1
        d = q.bit_length()-1
        assert r0 % d == 0 and r1 % d == 0
        values.append(((r0-r1)//d) % 3)
    data['nu'] = values
    return data


z1, z2 = np.zeros((1, 1), dtype=np.int64), np.zeros((2, 2), dtype=np.int64)
objects = [('plus', [np.array([[1]]), z1, z1]),
           ('minus', [np.array([[-1]]), z1, z1])]
for a, b in [(2, 2), (1, 2), (2, 1)]:
    u1, u2 = z2.copy(), z2.copy()
    (u1 if a == 1 else u2)[0, 1] = 1
    (u1 if b == 1 else u2)[1, 0] = 1
    objects.append((f'M{a}{b}', [np.diag([1, -1]), u1, u2]))
data = [curvature_data(t) for _, t in objects]


def admissible_blocks(ta0, tb0, rhs):
    a, b = rhs.shape
    free, base = [], np.zeros((a, b), dtype=np.int64)
    for i, j in product(range(a), range(b)):
        coefficient = ta0[i, i] + tb0[j, j]
        if coefficient:
            if rhs[i, j] % coefficient:
                return
            base[i, j] = rhs[i, j]//coefficient
        elif rhs[i, j]:
            return
        else:
            free.append((i, j))
    for values in product((-1, 0, 1), repeat=len(free)):
        answer = base.copy()
        for ij, value in zip(free, values):
            answer[ij] = value
        yield answer


admissible = 0
for ia, (name_a, ta) in enumerate(objects):
    for ib, (name_b, tb) in enumerate(objects):
        a, b = len(ta[0]), len(tb[0])
        zero = np.zeros((b, a), dtype=np.int64)
        for x0 in admissible_blocks(ta[0], tb[0], np.zeros((a, b), dtype=np.int64)):
            for x1 in admissible_blocks(ta[0], tb[0], -ta[1] @ x0-x0 @ tb[1]):
                for x2 in admissible_blocks(ta[0], tb[0],
                          -ta[1] @ x1-ta[2] @ x0-x0 @ tb[2]-x1 @ tb[1]):
                    admissible += 1
                    te = [np.block([[ta[i], [x0, x1, x2][i]], [zero, tb[i]]])
                          for i in range(3)]
                    da, db, de = data[ia], data[ib], curvature_data(te)
                    inc = np.vstack([eye(a), zero])
                    proj = np.hstack([zero, eye(b)])
                    hi = h_map(de, da, inc)
                    hp = h_map(db, de, proj)
                    hd = h_map(da, db, x0)
                    assert not np.any(hp @ hi % 2)
                    assert not np.any(hd @ hp % 2)
                    assert not np.any(hi @ hd % 2)
                    assert rank(hi)+rank(hd) == da['h']
                    assert rank(hi)+rank(hp) == de['h']
                    assert rank(hp)+rank(hd) == db['h']
                    for label in ('B', 'C'):
                        assert not np.any((de[label] @ hi-hi @ da[label]) % 2)
                        assert not np.any((db[label] @ hp-hp @ de[label]) % 2)
                        assert not np.any((da[label] @ hd-hd @ db[label]) % 2)
                    assert de['nu'] == [(x+y) % 3 for x, y in zip(da['nu'], db['nu'])]

lift_checks = gauge_checks = 0
for (_, t), original in zip(objects, data):
    n = len(t[0])
    zero = np.zeros((n, n), dtype=np.int64)
    for i, j in product(range(n), repeat=2):
        unit = zero.copy()
        unit[i, j] = 1
        correction = t[0] @ unit+unit @ t[0]
        assert not np.any(h_map(original, original, correction))
        lift_checks += 1
        for degree in (1, 2):
            s = [eye(n), zero.copy(), zero.copy()]
            s[degree] = unit
            sinv = [eye(n), -s[1], s[1] @ s[1]-s[2]]
            transformed = pmul(pmul(sinv, t), s)
            changed = curvature_data(transformed)
            assert np.array_equal(original['C'], changed['C'])
            assert np.array_equal(original['B'], changed['B'])
            assert original['nu'] == changed['nu']
            gauge_checks += 1

witnesses = []
for q in QS:
    B = companion(q)
    d, z = len(B), np.zeros_like(B)
    t = [np.block([[eye(d), z], [z, -eye(d)]]),
         np.block([[z, eye(d)], [z, z]]),
         np.block([[z, z], [B, z]])]
    actual = curvature_data(t)
    assert actual['nu'] == [2*int(q == r) for r in QS]
    x = [np.block([[z, -eye(d)], [z, z]]),
         np.block([[z, z], [-B, z]]),
         np.block([[B, z], [z, -B]])]
    assert all(not np.any(a+b) for a, b in zip(pmul(t, x), pmul(x, t)))
    zz = np.zeros((2*d, 2*d), dtype=np.int64)
    E = [np.block([[t[i], x[i]], [zz, t[i]]]) for i in range(3)]
    assert equal(pmul(E, E), [eye(4*d), np.zeros_like(E[0]), np.zeros_like(E[0])])
    # Columns are v, E v, e3, e2, giving a regular block and the quotient.
    unit = eye(4*d)
    v = unit[:, 3*d:4*d]
    S = [np.hstack([v, E[0] @ v, unit[:, 2*d:3*d], unit[:, d:2*d]]),
         np.hstack([np.zeros_like(v), E[1] @ v, np.zeros_like(v), np.zeros_like(v)]),
         np.hstack([np.zeros_like(v), E[2] @ v, np.zeros_like(v), np.zeros_like(v)])]
    # The constant matrix has a block-permutation inverse with only 0,+/-1.
    Sinv0 = np.zeros_like(S[0])
    Sinv0[0:d, 0:d] = -eye(d)
    Sinv0[0:d, 3*d:4*d] = eye(d)
    Sinv0[d:2*d, 0:d] = -eye(d)
    Sinv0[2*d:3*d, 2*d:3*d] = eye(d)
    Sinv0[3*d:4*d, d:2*d] = eye(d)
    assert np.array_equal(Sinv0 @ S[0], eye(4*d))
    Sinv = [Sinv0, -Sinv0 @ S[1] @ Sinv0,
            Sinv0 @ S[1] @ Sinv0 @ S[1] @ Sinv0-Sinv0 @ S[2] @ Sinv0]
    changed = pmul(pmul(Sinv, E), S)
    for i in range(3):
        assert not np.any(changed[i][2*d:, :2*d])
        assert np.array_equal(changed[i][:2*d, :2*d],
                              np.block([[z, eye(d)], [eye(d), z]]) if i == 0 else zz)
    minus = [t[0], np.block([[z, z], [-B, z]]), np.block([[z, eye(d)], [z, z]])]
    assert equal([a[2*d:, 2*d:] for a in changed], minus)
    g1 = np.block([[z, z], [-B, z]])
    G, Ginv = [eye(2*d), g1, zz], [eye(2*d), -g1, zz]
    plus = [t[0], -minus[1], minus[2]]
    assert equal(pmul(pmul(Ginv, minus), G), plus)
    K = np.block([[z, eye(d)], [-B, z]])
    assert all(np.array_equal(K @ (-a), b @ K) for a, b in zip(t, plus))
    witnesses.append({'q_bits': q, 'rank': 2*d, 'companion': B.tolist(),
                      'nu_vector_mod3': actual['nu'], 'rank4d_extension_verified': True,
                      'regular_submodule_and_free_quotient_verified': True,
                      'quotient_sign_conjugacy_verified': True})

report = {'statement_ids': ['C:three_cycle_length', 'C:cubic_Bockstein',
                            'C:cubic_three_torsion'],
          'arithmetic': 'exact integers and F2; no floating point',
          'scope': 'five endpoints plus/minus/M22/M12/M21; all free opposite-sign '
                   'extension coefficients in {-1,0,1}; other entries solved integrally; '
                   'every nonzero irreducible over F2 through degree4',
          'admissible_extensions': admissible,
          'checks_per_extension': ['T^2=1', 'Tate six-cycle exactness',
              'Bockstein and curvature commute with all three maps',
              'nonzero-primary acyclicity', 'nu additivity modulo3'],
          'lift_change_matrix_units': lift_checks,
          'basis_change_matrix_units_degrees1and2': gauge_checks,
          'witnesses': witnesses,
          'runtime_seconds': round(perf_counter()-START, 6)}
Path('logs/C_finish_cubic.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
