#!/usr/bin/env python3
"""Exact finite checks for C:epsilon_Bockstein and C:dualnumber_C2_ring.

Arithmetic uses integers and F2 only. Checks actual two-periodic Tate data
for small integral dual-number involutions and their admissible extensions;
companion witnesses; every invariant subspace lift in the two-cycle quiver
through dimension (2,2); and tensor identities for all irreducibles <=4.
The finite tests support, and do not replace, the general written proof.
"""
from itertools import product
from pathlib import Path
from time import perf_counter
import json
import numpy as np

START = perf_counter()

def eye(n):
    return np.eye(n, dtype=np.int64)

def bits(v):
    return sum((int(a) & 1) << j for j, a in enumerate(v))

def vec(v, n):
    return np.array([(v >> j) & 1 for j in range(n)], dtype=np.int64)

def coords(basis):
    ans = {0: 0}
    for j, v in enumerate(basis):
        ans.update({x ^ v: c | (1 << j) for x, c in tuple(ans.items())})
    return ans

def independent(vectors):
    result, space = [], {0}
    for v in vectors:
        if v not in space:
            result.append(v)
            space |= {x ^ v for x in tuple(space)}
    return result

def rank(a):
    pivots = {}
    for col in range(a.shape[1]):
        v = bits(a[:, col])
        while v:
            p = v.bit_length() - 1
            if p not in pivots:
                pivots[p] = v
                break
            v ^= pivots[p]
    return len(pivots)

def poly_rem(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a

def irreducible(q):
    d = q.bit_length() - 1
    return d > 0 and all(poly_rem(q, f) for e in range(1, d // 2 + 1)
                         for f in range(1 << e, 1 << (e + 1)))

QS = [q for d in range(1, 5) for q in range((1 << d) | 1, 1 << (d + 1), 2)
      if irreducible(q)]

def companion(q):
    d = q.bit_length() - 1
    b = np.zeros((d, d), dtype=np.int64)
    for j in range(d - 1):
        b[j + 1, j] = 1
    b[:, -1] = vec(q, d)
    return b

def matrix_poly(q, a):
    result = np.zeros_like(a)
    for j in range(q.bit_length() - 1, -1, -1):
        result = (result @ a + ((q >> j) & 1) * eye(len(a))) % 2
    return result

def matrix_power(a, e):
    result = eye(len(a))
    while e:
        if e & 1:
            result = result @ a % 2
        a = a @ a % 2
        e >>= 1
    return result

def chi(a, q):
    n = len(a)
    dim = n - rank(matrix_power(matrix_poly(q, a), max(1, n)))
    d = q.bit_length() - 1
    assert dim % d == 0
    return (dim // d) % 2

def h_data(t, u):
    """Recover integral Tate groups from the actual mod4 Bockstein.

    For a 2-torsion-free integral lattice H( T-1 mod2) has its canonical
    N=0 and N=1 summands equal to Hhat^0 and Hhat^1, respectively.
    We construct N by division by 2, and epsilon Bockstein by actual U.
    """
    n = len(t)
    assert np.array_equal(t @ t, eye(n))
    assert not np.any(t @ u + u @ t)
    d = t - eye(n)
    bd = independent(bits(d[:, j]) for j in range(n))
    cycles = [v for v in range(1 << n) if not np.any(d @ vec(v, n) % 2)]
    full = list(bd)
    for v in cycles:
        if v not in coords(full):
            full.append(v)
    hb, co = full[len(bd):], coords(full)
    h = len(hb)
    N, B = np.zeros((h, h), dtype=np.int64), np.zeros((h, h), dtype=np.int64)
    for j, v in enumerate(hb):
        dv = d @ vec(v, n)
        assert not np.any(dv % 2)
        N[:, j] = vec(co[bits(dv // 2)] >> len(bd), h)
        B[:, j] = vec(co[bits(u @ vec(v, n))] >> len(bd), h)
    assert np.array_equal(N @ N % 2, N)
    assert not np.any((N @ B + B @ N + B) % 2)
    vb = independent(v for v in range(1 << h) if not np.any(N @ vec(v, h) % 2))
    wb = independent(v for v in range(1 << h)
                     if not np.any((N + eye(h)) @ vec(v, h) % 2))
    assert len(vb) + len(wb) == h
    vc = coords(vb)
    square = B @ B % 2
    uv = np.zeros((len(vb), len(vb)), dtype=np.int64)
    for j, v in enumerate(vb):
        uv[:, j] = vec(vc[bits(square @ vec(v, h))], len(vb))
    return {'n': n, 'h': h, 'boundary_rank': len(bd), 'basis': hb,
            'coordinates': co, 'N': N, 'B': B, 'u_V': uv,
            'chi': [chi(uv, q) for q in QS]}

def h_map(a, b, x):
    out = np.zeros((a['h'], b['h']), dtype=np.int64)
    for j, v in enumerate(b['basis']):
        w = bits(x @ vec(v, b['n']))
        out[:, j] = vec(a['coordinates'][w] >> a['boundary_rank'], a['h'])
    return out

objects = [(np.array([[1]]), np.array([[0]])),
           (np.array([[-1]]), np.array([[0]])),
           (np.array([[0, 1], [1, 0]]), np.zeros((2, 2), dtype=np.int64))]
for b, c in product(range(2), repeat=2):
    objects.append((np.diag([1, -1]), np.array([[0, b], [c, 0]])))
data = [h_data(t, u) for t, u in objects]
extension_candidates = admissible_extensions = 0
for ia, (ta, ua) in enumerate(objects):
    for ib, (tb, ub) in enumerate(objects):
        a, b = len(ta), len(tb)
        zeros = np.zeros((b, a), dtype=np.int64)
        for vals in product(range(2), repeat=2*a*b):
            extension_candidates += 1
            x0 = np.array(vals[:a*b]).reshape(a, b)
            x1 = np.array(vals[a*b:]).reshape(a, b)
            te = np.block([[ta, x0], [zeros, tb]])
            ue = np.block([[ua, x1], [zeros, ub]])
            if not np.array_equal(te @ te, eye(a+b)) or np.any(te @ ue + ue @ te):
                continue
            admissible_extensions += 1
            da, db, de = data[ia], data[ib], h_data(te, ue)
            inc = np.vstack([eye(a), zeros])
            proj = np.hstack([zeros, eye(b)])
            hi, hp, hd = h_map(de, da, inc), h_map(db, de, proj), h_map(da, db, x0)
            assert not np.any(hp @ hi % 2)
            assert not np.any(hd @ hp % 2)
            assert not np.any(hi @ hd % 2)
            assert rank(hi) + rank(hd) == da['h']
            assert rank(hi) + rank(hp) == de['h']
            assert rank(hp) + rank(hd) == db['h']
            assert not np.any((de['B'] @ hi + hi @ da['B']) % 2)
            assert not np.any((db['B'] @ hp + hp @ de['B']) % 2)
            assert not np.any((da['B'] @ hd + hd @ db['B']) % 2)
            assert de['chi'] == [(x+y) % 2 for x, y in zip(da['chi'], db['chi'])]

def all_subspaces(n):
    spaces = {frozenset({0}): []}
    for v in range(1, 1 << n):
        for sp, basis in tuple(spaces.items()):
            if v not in sp:
                newsp = frozenset(set(sp) | {x ^ v for x in sp})
                spaces.setdefault(newsp, basis + [v])
    return list(spaces.values())

def adapted(basis, n):
    full = list(basis)
    for j in range(n):
        if (1 << j) not in coords(full):
            full.append(1 << j)
    return np.array([vec(v, n) for v in full]).T

def inverse_small(a):
    if len(a) == 1:
        assert a[0, 0] == 1
        return a.copy()
    assert len(a) == 2
    det = int(a[0, 0]*a[1, 1] - a[0, 1]*a[1, 0])
    assert det in (-1, 1)
    return np.array([[a[1, 1], -a[0, 1]], [-a[1, 0], a[0, 0]]]) * det

quiver_pairs = invariant_subspace_lifts = 0
for a, b in product((1, 2), repeat=2):
    for vals in product(range(2), repeat=2*a*b):
        quiver_pairs += 1
        B = np.array(vals[:a*b]).reshape(a, b)
        C = np.array(vals[a*b:]).reshape(b, a)
        for va in all_subspaces(a):
            for wb in all_subspaces(b):
                if any(bits(B @ vec(v, b)) not in coords(va) for v in wb):
                    continue
                if any(bits(C @ vec(v, a)) not in coords(wb) for v in va):
                    continue
                invariant_subspace_lifts += 1
                sa, sb = adapted(va, a), adapted(wb, b)
                bp, cp = inverse_small(sa) @ B @ sb, inverse_small(sb) @ C @ sa
                ra, rb = len(va), len(wb)
                assert not np.any(bp[ra:, :rb] % 2)
                assert not np.any(cp[rb:, :ra] % 2)
                x, y = np.zeros_like(bp), np.zeros_like(cp)
                x[ra:, :rb] = -bp[ra:, :rb] // 2
                y[rb:, :ra] = cp[rb:, :ra] // 2
                assert not np.any((bp + 2*x)[ra:, :rb])
                assert not np.any((cp - 2*y)[rb:, :ra])

witnesses, tensors = [], []
for q in QS:
    b = companion(q)
    d, z = len(b), np.zeros_like(b)
    t0 = np.block([[eye(d), z], [z, -eye(d)]])
    u = np.block([[z, b], [eye(d), z]])
    j = np.block([[z, b], [-eye(d), z]])
    assert not np.any(t0 @ u + u @ t0)
    assert not np.any(j @ t0 + t0 @ j)
    assert not np.any(j @ u + u @ j)
    assert [chi(b, q2) for q2 in QS] == [int(q == q2) for q2 in QS]
    witnesses.append({'q_bits': q, 'dimension': 2*d, 'companion': b.tolist(),
                      'epsilon_parity_vector': [chi(b, q2) for q2 in QS]})
    for r in QS:
        c = companion(r)
        e, zc = len(c), np.zeros_like(c)
        tc = np.block([[eye(e), zc], [zc, -eye(e)]])
        uc = np.block([[zc, c], [eye(e), zc]])
        tt = np.kron(t0, tc)
        ut = np.kron(u, tc) + np.kron(t0, uc)
        assert not np.any(tt @ ut + ut @ tt)
        plus = [i for i, a in enumerate(np.diag(tt)) if a == 1]
        actual = (ut @ ut)[np.ix_(plus, plus)] % 2
        L = (np.kron(b, eye(e)) + np.kron(eye(d), c)) % 2
        zz = np.zeros_like(L)
        assert np.array_equal(actual, np.block([[L, zz], [zz, L]]))
        assert not any(chi(actual, q2) for q2 in QS)
        tensors.append({'q_bits': q, 'r_bits': r, 'rank': len(tt),
                        'two_equal_primary_blocks': True})

report = {'statement_ids': ['C:epsilon_Bockstein', 'C:dualnumber_C2_ring'],
          'arithmetic': 'exact integers and F2; no floating point',
          'extension_scope': '7 explicit endpoint objects, all 0/1 blocks X0,X1',
          'extension_candidates': extension_candidates,
          'admissible_extensions': admissible_extensions,
          'verified_for_extensions': ['actual Tate spaces from mod4 Bockstein',
              'cyclic exactness', 'epsilon Bockstein compatibility',
              'all seven primary parity invariants'],
          'quiver_pair_scope': '(a,b) in {(1,1),(1,2),(2,1),(2,2)} over F2',
          'quiver_pairs': quiver_pairs, 'invariant_subspace_lifts': invariant_subspace_lifts,
          'irreducible_q_bits': QS, 'witnesses': witnesses, 'tensor_products': tensors,
          'trace_zero_witness_q_bits': 11,
          'trace_zero_witness_old_detector': 'q(t^2+t)=(t^3+t+1)(t^3+t^2+1)',
          'runtime_seconds': round(perf_counter() - START, 6), 'all_checks_passed': True}
out = Path(__file__).resolve().parents[1] / 'logs' / 'C_finish_dualnumber_ring.json'
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k not in ('witnesses', 'tensor_products')}, indent=2))
