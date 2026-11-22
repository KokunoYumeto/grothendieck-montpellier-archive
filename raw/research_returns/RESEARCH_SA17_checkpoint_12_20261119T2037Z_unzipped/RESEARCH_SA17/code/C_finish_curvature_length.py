"""Finite certificate for curvature Fitting parts, lengths, and torsion heights."""
from pathlib import Path
from itertools import product
from functools import lru_cache
from time import perf_counter
import json
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

# Reuse only the explicit finite-field row-reduction helpers, not that run.
exec(Path('code/C_finish_modp2_Bockstein.py').read_text().split('def homology(')[0])
start = perf_counter()
z = sp.symbols('z')

def inv_local(B, p, mod):
    n = B.shape[0]
    U = np.column_stack((B.copy() % mod, np.eye(n, dtype=np.int64)))
    for j in range(n):
        i = next(i for i in range(j, n) if U[i, j] % p)
        U[[i, j]] = U[[j, i]]
        U[j] = U[j] * pow(int(U[j, j]), -1, mod) % mod
        for i in range(n):
            if i != j:
                U[i] = (U[i]-U[i, j]*U[j]) % mod
    assert np.array_equal(U[:, :n], np.eye(n, dtype=np.int64))
    return U[:, n:]

@lru_cache(None)
def primary_polynomial(c0, c1, n0, n1, p):
    C0 = sp.Matrix(n0, n0, c0)
    C1 = sp.Matrix(n1, n1, c1)
    f = sp.Poly(C0.charpoly(z).as_expr()*C1.charpoly(z).as_expr(), z, modulus=p)
    lin = sp.Poly(z-1, z, modulus=p)
    g, a = f, 0
    while g.degree() > 0 and int(g.eval(1)) % p == 0:
        g = g.exquo(lin)
        a += 1
    if not a:
        return (0,)
    if g.degree() == 0:
        return (1,)
    f0 = lin**a
    e = (g*sp.invert(g, f0)).rem(f)
    return tuple(int(c) % p for c in reversed(e.all_coeffs()))

def evaluate(coeff, C, mod):
    n = C.shape[0]
    E = np.zeros((n, n), dtype=np.int64)
    for c in reversed(coeff):
        E = (E @ C + c*np.eye(n, dtype=np.int64)) % mod
    return E

def image_basis(E, p, mod):
    cols = rr(E % p, p)[1]
    B = E[:, cols] % mod
    if not cols:
        return B, np.zeros((0, E.shape[0]), dtype=np.int64)
    rows = rr(B.T % p, p)[1]
    P = np.zeros((len(cols), E.shape[0]), dtype=np.int64)
    P[:, rows] = inv_local(B[rows, :], p, mod)
    assert np.array_equal(P @ B % mod, np.eye(len(cols), dtype=np.int64))
    return B, P

def cokernel_length(D, p, m):
    if not D.shape[0]:
        return 0
    S = smith_normal_form(sp.Matrix(D.tolist()), domain=sp.ZZ)
    ans = 0
    for i in range(D.shape[0]):
        a, v = abs(int(S[i, i])), 0
        if not a:
            ans += m
            continue
        while a % p == 0 and v < m:
            a //= p
            v += 1
        ans += v
    return ans

def invariant(d0, d1, p, m):
    mod = p**m
    prod0, prod1 = d1 @ d0, d0 @ d1
    assert not np.any(prod0 % mod) and not np.any(prod1 % mod)
    C0, C1 = prod0 // mod, prod1 // mod
    assert not np.any(C1 @ d0-d0 @ C0)
    assert not np.any(C0 @ d1-d1 @ C1)
    coeff = primary_polynomial(tuple(int(x) for x in (C0 % p).flat),
                               tuple(int(x) for x in (C1 % p).flat),
                               C0.shape[0], C1.shape[0], p)
    Es = [evaluate(coeff, C0 % mod, mod), evaluate(coeff, C1 % mod, mod)]
    for i in range(m.bit_length()+1):
        Es = [(3*E@E-2*(E@E % mod)@E) % mod for E in Es]
    assert all(not np.any((E@E-E) % mod) for E in Es)
    assert not np.any((d0 @ Es[0]-Es[1] @ d0) % mod)
    assert not np.any((d1 @ Es[1]-Es[0] @ d1) % mod)
    B0, P0 = image_basis(Es[0], p, mod)
    B1, P1 = image_basis(Es[1], p, mod)
    assert B0.shape[1] == B1.shape[1]
    D0, D1 = P1 @ d0 @ B0 % mod, P0 @ d1 @ B1 % mod
    assert not np.any((B1@D0-d0@B0) % mod)
    assert not np.any((B0@D1-d1@B1) % mod)
    l0, l1 = cokernel_length(D0, p, m), cokernel_length(D1, p, m)
    assert l0+l1 == m*B0.shape[1]
    return l0 % m

counts = {'extension_candidates': 0, 'admissible_extensions': 0,
          'lift_changes': 0, 'basis_changes': 0}
examples = []
extension_runs = []
for p, m in ((3, 2), (3, 3), (3, 4)):
    mod = p**m
    cs = (1, 2) if m < 4 else (1,)
    endpoints = [(np.array([[p**a]], dtype=np.int64),
                  np.array([[c*p**(m-a)]], dtype=np.int64),
                  a % m if c == 1 else 0)
                 for a in range(1, m) for c in cs]
    if m < 4:
        endpoints.append((np.array([[0]], dtype=np.int64), np.array([[p]], dtype=np.int64), 0))
    for d0, d1, expected in endpoints:
        assert invariant(d0, d1, p, m) == expected
        examples.append((d0, d1, p, m))
    candidates = admissible = 0
    for (a0, a1, av), (b0, b1, bv) in product(endpoints, repeat=2):
        for x0, x1 in product(range(mod), repeat=2):
            candidates += 1
            if (int(a1[0, 0])*x0+x1*int(b0[0, 0])) % mod:
                continue
            if (int(a0[0, 0])*x1+x0*int(b1[0, 0])) % mod:
                continue
            d0 = np.array([[a0[0, 0], x0], [0, b0[0, 0]]], dtype=np.int64)
            d1 = np.array([[a1[0, 0], x1], [0, b1[0, 0]]], dtype=np.int64)
            assert invariant(d0, d1, p, m) == (av+bv) % m
            admissible += 1
            if x0 and x1 and len(examples) < 24:
                examples.append((d0, d1, p, m))
    counts['extension_candidates'] += candidates
    counts['admissible_extensions'] += admissible
    extension_runs.append({'p': p, 'm': m, 'endpoints': len(endpoints),
                           'candidates': candidates, 'admissible': admissible})

for d0, d1, p, m in examples:
    mod, n = p**m, d0.shape[0]
    expected = invariant(d0, d1, p, m)
    old0, old1 = d1@d0//mod, d0@d1//mod
    for parity, i, j, sign in product(range(2), range(n), range(n), (-1, 1)):
        h = np.zeros((n, n), dtype=np.int64)
        h[i, j] = sign
        e0, e1 = d0.copy(), d1.copy()
        if parity == 0:
            e0 += mod*h
            assert not np.any((e1@e0//mod-old0-d1@h) % mod)
            assert not np.any((e0@e1//mod-old1-h@d1) % mod)
        else:
            e1 += mod*h
            assert not np.any((e1@e0//mod-old0-h@d0) % mod)
            assert not np.any((e0@e1//mod-old1-d0@h) % mod)
        assert invariant(e0, e1, p, m) == expected
        counts['lift_changes'] += 1
    gauges = []
    for i in range(n):
        P = np.eye(n, dtype=np.int64)
        P[i, i] = 2
        gauges.append(P)
    for i, j in product(range(n), repeat=2):
        if i != j:
            P = np.eye(n, dtype=np.int64)
            P[i, j] = 1
            gauges.append(P)
    for parity, P in product(range(2), gauges):
        Pinv = inv_local(P, p, mod)
        if parity == 0:
            e0, e1 = d0@P % mod, Pinv@d1 % mod
        else:
            e0, e1 = Pinv@d0 % mod, d1@P % mod
        assert invariant(e0, e1, p, m) == expected
        counts['basis_changes'] += 1

scalar_runs = []
twists = 0
for p, r in product((3, 5, 7), range(1, 5)):
    m, mod = 2*r, p**(2*r)
    row = []
    for a in range(1, p):
        T = pow(1+p**(m-1), a, mod)
        norm = sum(pow(T, i, mod) for i in range(p)) % mod
        d0, d1 = np.array([[T-1]], dtype=np.int64), np.array([[norm]], dtype=np.int64)
        value = invariant(d0, d1, p, m)
        assert value == (m-1 if a == 1 else 0)
        row.append(value)
        twists += 1
    assert sum(row) % m == m-1
    assert (p**r)**2 % mod == 0
    assert p**(r-1)*p**r == p**(2*r-1)
    scalar_runs.append({'p': p, 'torsion_height_length': r,
                        'target_exponent_m': m, 'twisted_invariants': row,
                        'induced_invariant': m-1})

report = {'status': 'PASS',
          'scope': 'Actual polynomial Fitting projectors over Z/p^m, lifted idempotent refinement, free image bases and integer Smith cokernel lengths; complete stated scalar-factorization extension ranges, matrix-unit lift changes, two-sided basis changes, and higher-height scalar Tate witnesses.',
          'draft_ids': ['C:curvature_length', 'C:odd_torsion_allheights',
                        'C:allprime_squarezero_criterion'],
          'counts': counts, 'extension_runs': extension_runs,
          'scalar_torsion_runs': scalar_runs, 'normalizer_twists': twists,
          'runtime_seconds': round(perf_counter()-start, 6)}
root = Path(__file__).resolve().parents[1]
(root/'logs/C_finish_curvature_length.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
