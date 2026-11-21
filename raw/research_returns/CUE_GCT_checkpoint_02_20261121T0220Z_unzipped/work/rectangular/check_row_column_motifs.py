"""Exact finite checks for the uniform R19 proof, without extrapolation."""
import json
from pathlib import Path
import sympy as sp
from check_simultaneous_chords import (
    field_for, normal_columns, permanent, product_coefficients,
    rank_columns, submatrix,
)


def coefficient_column(ai, bi, m, k, roots, p):
    aa = product_coefficients([i % m for i in ai], roots, p)
    bb = product_coefficients([i % m for i in bi], roots, p)
    assert len(aa) == m - k + 1 and len(bb) == k + 1
    return [aa[r] * bb[s] % p for r in range(m - k + 1) for s in range(k + 1)]


def four_families(m, k, p, zeta):
    h = min(m // 3, m - 9)
    roots = [pow(zeta, i, p) for i in range(m)]
    cols = []
    for a in range(1, 3 * h, 3):
        def outside(start, stop):
            inside = {i % m for i in range(start, stop + 1)}
            return [i for i in range(m) if i not in inside]
        cols.append(coefficient_column([a + 1] + outside(a, a + k),
                                        [a, a + 2] + list(range(a + 2, a + k)),
                                        m, k, roots, p))
        cols.append(coefficient_column([a + 1, a + 1] + outside(a, a + k + 1),
                                        [a + 2] + list(range(a + 2, a + k + 1)),
                                        m, k, roots, p))
        cols.append(coefficient_column([a, a] + outside(a - k, a + 1),
                                        [a + 2] + list(range(a - k, a - 1)),
                                        m, k, roots, p))
        cols.append(coefficient_column([a] + outside(a - k + 1, a + 1),
                                        [a, a + 2] + list(range(a - k + 1, a - 1)),
                                        m, k, roots, p))
    return cols


def local_checks(m, samples, selected_centers=None, selected_k=None):
    p, zeta = field_for(m)
    h = min(m // 3, m - 9)
    starts = list(range(1, 3 * h, 3))
    checked = nonzero = 0
    for sample in samples:
        x, y, z, w, eps = [v % p for v in
                          (sample + 1, sample ** 2 + 2,
                           sample ** 3 + 3, 2 * sample + 1, sample)]
        if not eps:
            eps = 1
        ell = [(x - pow(zeta, i, p) * y) % p for i in range(m)]
        vv = [(z - pow(zeta, i, p) * w) % p for i in range(m)]
        mat = [[0] * m for _ in range(m)]
        for i in range(m):
            mat[i][i] = ell[i]
            mat[i][(i + 1) % m] = vv[i]
        for a in starts:
            mat[a][(a + 2) % m] = eps * ell[(a + 1) % m] % p
            mat[(a + 1) % m][a] = eps * vv[(a + 2) % m] % p
            mat[(a - 1) % m][(a + 1) % m] = eps * ell[a] % p
        for a in (selected_centers if selected_centers is not None else starts):
            prev, b, c = (a - 1) % m, (a + 1) % m, (a + 2) % m
            pp, qq, rr = mat[a][c], mat[b][a], mat[prev][b]
            for k in (selected_k if selected_k is not None else range(5, m - 4)):
                for r in ((a + k) % m, (a + k + 1) % m):
                    cof = [permanent(submatrix(mat, {r}, {j}), p) for j in (a, b, c)]
                    comp = permanent(submatrix(mat, {a, b, r}, {a, b, c}), p)
                    pred = [(vv[a] * vv[b] + pp * ell[b]) * comp % p,
                            (ell[a] * vv[b] + pp * qq) * comp % p,
                            (ell[a] * ell[b] + vv[a] * qq) * comp % p]
                    assert cof == pred
                    lhs = [(ell[a] * cof[0] - vv[a] * cof[1] - pp * cof[2]) % p,
                           (qq * cof[0] + ell[b] * cof[1] - vv[b] * cof[2]) % p]
                    rhs = [-2 * pp * qq * vv[a] * comp % p,
                           2 * pp * qq * ell[b] * comp % p]
                    assert lhs == rhs
                    checked += 2; nonzero += sum(bool(x) for x in rhs)
                for col in ((a - k) % m, (a - k + 1) % m):
                    cof = [permanent(submatrix(mat, {i}, {col}), p) for i in (prev, a, b)]
                    comp = permanent(submatrix(mat, {prev, a, b}, {a, b, col}), p)
                    pred = [(ell[a] * ell[b] + vv[a] * qq) * comp % p,
                            (vv[prev] * ell[b] + qq * rr) * comp % p,
                            (vv[prev] * vv[a] + ell[a] * rr) * comp % p]
                    assert cof == pred
                    lhs = [(vv[prev] * cof[0] - ell[a] * cof[1] - qq * cof[2]) % p,
                           (rr * cof[0] + vv[a] * cof[1] - ell[b] * cof[2]) % p]
                    rhs = [-2 * qq * rr * ell[a] * comp % p,
                           2 * qq * rr * vv[a] * comp % p]
                    assert lhs == rhs
                    checked += 2; nonzero += sum(bool(x) for x in rhs)
    return {'m': m, 'prime': p, 'identity_point_checks': checked,
            'nonzero_rhs_checks': nonzero, 'centers': selected_centers or starts}


q, K, X, z, x, y = sp.symbols('q K X z x y')
den = (K - 1) * (q * K - 1)
d0, d1 = K * (q - 1) / (q * (K - 1)), (K - q) / (q * (K - 1))
e0 = K ** 2 * (q - 1) ** 2 / (q * den)
e1 = K * (K - q) * (q - 1) / (q * den)
e2 = (K - 1) / (q * K - 1)
assert sp.factor(d0 * (x - q / K * y) + d1 * (x - q * y) - (x - y)) == 0
assert sp.factor(e0 * (x - y / K) * (x - q * y / K)
                 + e1 * (x - q * y) * (x - y / K)
                 + e2 * (x - y) * (x - q * y) - (x - y) ** 2) == 0
cc = lambda z: (z - 1) * (z - q) * (
    e0 * (z - q ** -2) * (z - q ** -1) * (z - K)
    + e1 / X * (z - q ** -1) * (z - K / q ** 3) * (z - q * K)
    + e2 / X ** 2 * (z - K / q ** 3) * (z - K / q ** 2) * (z - q ** 2 * K))
dd = lambda z: (z - 1) * (z - q) * (
    d0 * (z - q ** -1) * (z - K / q ** 2) * (z - K)
    + d1 / X * (z - K / q ** 3) * (z - K / q) * (z - q * K))
det = sp.factor(cc(K / q ** 3) * dd(K / q ** 2) - dd(K / q ** 3) * cc(K / q ** 2))
expected = K ** 6 * (q - K) * (q ** 2 - K) ** 2 * (q ** 3 - K) ** 2 * (q ** 4 - K) * (q - 1) ** 6 * (q + 1) * (q ** 2 + q + 1) / (q ** 27 * (K - 1) * (q * K - 1))
assert sp.factor(det - expected) == 0

results = []
for m in range(10, 17):
    p, zeta = field_for(m)
    h = min(m // 3, m - 9)
    ranks = []
    for k in range(5, m - 4):
        base, _ = normal_columns(m, k, p, zeta)
        extra = four_families(m, k, p, zeta)
        rb, ra = rank_columns(base, p), rank_columns(base + extra, p)
        assert (rb, ra) == (2 * m, 2 * m + 4 * h), (m, k, rb, ra)
        ranks.append({'k': k, 'base_rank': rb, 'augmented_rank': ra})
    results.append({'m': m, 'prime': p, 'zeta': zeta, 'motifs': h,
                    'normal_columns': 4 * h * (m - 9), 'bidegree_ranks': ranks})
local = [local_checks(11, [1, 2, 3, 4]),
         local_checks(15, [2], selected_centers=[1, 13], selected_k=[5, 10])]
path = Path(__file__).with_name('row_column_motif_results.json')
path.write_text(json.dumps({'symbolic_shift_identities_verified': True,
                            'symbolic_quintic_determinant_verified': True,
                            'scope': 'finite checks only; R19 has a uniform proof',
                            'results': results, 'local_checks': local}, indent=2) + '\n')
print(json.dumps({'all_passed': True,
                  'bidegree_matrices_checked': sum(len(r['bidegree_ranks']) for r in results),
                  'identity_point_checks': sum(r['identity_point_checks'] for r in local),
                  'output': str(path)}))
