"""Actual mod-p Tate homology/Bockstein checks over Z/p^2."""
from itertools import product
from pathlib import Path
from time import perf_counter
import json
import numpy as np

start = perf_counter()

def rr(A, p):
    A = np.array(A, dtype=np.int64, copy=True) % p
    row, piv = 0, []
    for col in range(A.shape[1]):
        nz = next((i for i in range(row, A.shape[0]) if A[i, col]), None)
        if nz is None:
            continue
        A[[row, nz]] = A[[nz, row]]
        A[row] = A[row] * pow(int(A[row, col]), -1, p) % p
        for i in range(A.shape[0]):
            if i != row and A[i, col]:
                A[i] = (A[i] - A[i, col]*A[row]) % p
        piv.append(col)
        row += 1
        if row == A.shape[0]:
            break
    return A, piv

def rank(A, p):
    return len(rr(A, p)[1])

def ker(A, p):
    R, piv = rr(A, p)
    free = [j for j in range(A.shape[1]) if j not in piv]
    K = np.zeros((A.shape[1], len(free)), dtype=np.int64)
    for j, col in enumerate(free):
        K[col, j] = 1
        for i, pc in enumerate(piv):
            K[pc, j] = -R[i, col] % p
    return K

def homology(d, prev, p):
    n = d.shape[1]
    K = ker(d, p)
    im = prev[:, rr(prev, p)[1]] % p
    B, hs = im.copy(), []
    for j in range(K.shape[1]):
        v = K[:, j:j+1]
        if rank(np.column_stack((B, v)), p) > B.shape[1]:
            B = np.column_stack((B, v))
            hs.append(v)
    H = np.column_stack(hs) if hs else np.zeros((n, 0), dtype=np.int64)
    P = np.zeros((H.shape[1], n), dtype=np.int64)
    if B.shape[1]:
        rows = rr(B.T, p)[1]
        square = B[rows, :]
        inv = rr(np.column_stack((square, np.eye(len(rows), dtype=np.int64))), p)[0][:, len(rows):]
        full = np.zeros((len(rows), n), dtype=np.int64)
        full[:, rows] = inv
        P = full[im.shape[1]:]
    assert not np.any(d @ H % p)
    return H, P

def powm(T, r, mod):
    A = np.eye(T.shape[0], dtype=np.int64)
    for i in range(r):
        A = A @ T % mod
    return A

def data(T, p):
    mod, n = p*p, T.shape[0]
    I = np.eye(n, dtype=np.int64)
    assert np.array_equal(powm(T, p, mod), I)
    N, power = np.zeros((n, n), dtype=np.int64), I
    for i in range(p):
        N = (N + power) % mod
        power = power @ T % mod
    ds = [(T-I) % mod, N]
    assert not np.any(ds[0] @ ds[1] % mod)
    H, P = [], []
    for i in range(2):
        h, proj = homology(ds[i] % p, ds[1-i] % p, p)
        H.append(h)
        P.append(proj)
    bs = []
    for i in range(2):
        dv = ds[i] @ H[i] % mod
        assert not np.any(dv % p)
        w = dv // p
        assert not np.any(ds[1-i] @ w % p)
        bs.append(P[1-i] @ w % p)
    us = [bs[1] @ bs[0] % p, bs[0] @ bs[1] % p]
    h = H[0].shape[1]
    q = (us[0] - np.eye(h, dtype=np.int64)) % p
    qpow = np.eye(h, dtype=np.int64)
    for i in range(max(1, h)):
        qpow = qpow @ q % p
    chi = (h-rank(qpow, p)) % 2
    return {'T': T, 'd': ds, 'H': H, 'P': P, 'b': bs, 'u': us, 'chi': chi}

def check_extension(A, B, X, p):
    n, m = A['T'].shape[0], B['T'].shape[0]
    E = np.block([[A['T'], X], [np.zeros((m, n), dtype=np.int64), B['T']]])
    if not np.array_equal(powm(E, p, p*p), np.eye(n+m, dtype=np.int64)):
        return False
    C = data(E, p)
    inc = np.vstack((np.eye(n, dtype=np.int64), np.zeros((m, n), dtype=np.int64)))
    pr = np.column_stack((np.zeros((m, n), dtype=np.int64), np.eye(m, dtype=np.int64)))
    maps = []
    for i in range(2):
        j = 1-i
        f = C['P'][i] @ inc @ A['H'][i] % p
        g = B['P'][i] @ pr @ C['H'][i] % p
        delta = A['P'][j] @ C['d'][i][:n, n:] @ B['H'][i] % p
        maps.append((f, g, delta))
    for i in range(2):
        j = 1-i
        f, g, delta = maps[i]
        fj, gj, dj = maps[j]
        assert not np.any((C['b'][i] @ f - fj @ A['b'][i]) % p)
        assert not np.any((B['b'][i] @ g - gj @ C['b'][i]) % p)
        assert not np.any((A['b'][j] @ delta + dj @ B['b'][i]) % p)
        assert rank(dj, p)+rank(f, p) == A['H'][i].shape[1]
        assert rank(f, p)+rank(g, p) == C['H'][i].shape[1]
        assert rank(g, p)+rank(delta, p) == B['H'][i].shape[1]
    assert C['chi'] == (A['chi']+B['chi']) % 2
    return True

reports = []
total_candidates = total_extensions = 0
for p in (3, 5, 7):
    mod = p*p
    lines = [data(np.array([[1+p*r]], dtype=np.int64) % mod, p) for r in range(p)]
    assert [d['chi'] for d in lines] == [0, 1]+[0]*(p-2)
    candidates = extensions = 0
    for A, B in product(lines, repeat=2):
        for x in range(mod):
            candidates += 1
            extensions += check_extension(A, B, np.array([[x]], dtype=np.int64), p)
    if p == 3:
        extra = [np.array([[0, -1], [1, -1]], dtype=np.int64) % mod,
                 np.diag([1+p, 1-p]) % mod,
                 np.array([[1, p], [0, 1]], dtype=np.int64) % mod,
                 (np.eye(2, dtype=np.int64)+p*np.array([[0, -1], [1, 0]])) % mod]
        extras = [data(T, p) for T in extra]
        assert not np.any(extras[0]['u'][0]) and not np.any(extras[0]['u'][1])
        for A, B in list(product(lines, extras))+list(product(extras, lines)):
            shape = (A['T'].shape[0], B['T'].shape[0])
            for entries in product(range(mod), repeat=shape[0]*shape[1]):
                candidates += 1
                extensions += check_extension(A, B, np.array(entries, dtype=np.int64).reshape(shape), p)
    total_candidates += candidates
    total_extensions += extensions
    reports.append({'p': p, 'scalar_twists': p-1,
                    'twisted_primary_parities': [d['chi'] for d in lines[1:]],
                    'extension_candidates': candidates,
                    'admissible_extensions_checked': extensions})

report = {'status': 'PASS', 'scope': 'Actual two-periodic Tate homology over Fp, division-by-p Bocksteins, six-cycle exactness, naturality/anticommutation and z−1-primary parity; p3,5,7 scalar endpoints and selected p3 rank2 endpoints.',
          'draft_ids': ['C:modp2_Tate_Bockstein', 'C:odd_torsion_heightzero'],
          'prime_tests': reports, 'total_extension_candidates': total_candidates,
          'total_admissible_extensions': total_extensions,
          'runtime_seconds': round(perf_counter()-start, 6)}
root = Path(__file__).resolve().parents[1]
(root/'logs/C_finish_modp2_Bockstein.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
