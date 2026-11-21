"""R18 exact finite checks, separate from the uniform algebraic proof."""
import json
from pathlib import Path

import sympy as sp

from check_simultaneous_chords import (
    field_for, normal_columns, permanent, product_coefficients,
    rank_columns, submatrix,
)


def families(m, k, p, zeta):
    h = min(m // 2, m - 5)
    roots = [pow(zeta, i, p) for i in range(m)]
    out = []
    for a in range(0, 2 * h, 2):
        block = {(a + i) % m for i in range(k + 1)}
        aa = product_coefficients([(a + 1) % m] +
                                  [i for i in range(m) if i not in block], roots, p)
        bb = product_coefficients([a, (a + 2) % m] +
                                  [(a + i) % m for i in range(2, k)], roots, p)
        out.append([aa[r] * bb[s] % p
                    for r in range(m - k + 1) for s in range(k + 1)])
        block = {(a + i) % m for i in range(k + 2)}
        aa = product_coefficients([(a + 1) % m] * 2 +
                                  [i for i in range(m) if i not in block], roots, p)
        bb = product_coefficients([(a + 2) % m] +
                                  [(a + i) % m for i in range(2, k + 1)], roots, p)
        out.append([aa[r] * bb[s] % p
                    for r in range(m - k + 1) for s in range(k + 1)])
    return out


def local_checks(m, p, zeta):
    h = min(m // 2, m - 5)
    checks = nonzero = 0
    for sample in range(1, 8):
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
        for a in range(0, 2 * h, 2):
            mat[a][(a + 2) % m] = eps * ell[(a + 1) % m] % p
            mat[(a + 1) % m][a] = eps * vv[(a + 2) % m] % p
        for a in range(0, 2 * h, 2):
            b, c = (a + 1) % m, (a + 2) % m
            pp, qq = mat[a][c], mat[b][a]
            for r in range(m):
                if r in (a, b):
                    continue
                cof = [permanent(submatrix(mat, {r}, {j}), p) for j in (a, b, c)]
                rr = permanent(submatrix(mat, {a, b, r}, {a, b, c}), p)
                predicted = [(vv[a] * vv[b] + pp * ell[b]) * rr % p,
                             (ell[a] * vv[b] + pp * qq) * rr % p,
                             (ell[a] * ell[b] + vv[a] * qq) * rr % p]
                assert cof == predicted
                lhs1 = (ell[a] * cof[0] - vv[a] * cof[1] - pp * cof[2]) % p
                lhs2 = (qq * cof[0] + ell[b] * cof[1] - vv[b] * cof[2]) % p
                rhs1, rhs2 = -2 * pp * qq * vv[a] * rr % p, 2 * pp * qq * ell[b] * rr % p
                assert (lhs1, lhs2) == (rhs1, rhs2)
                checks += 2
                nonzero += bool(rhs1) + bool(rhs2)
    return checks, nonzero


# Independent exact rational-function simplification of the displayed
# four-cubic evaluation determinant and coefficient-ratio numerator.
q, K, X, u = sp.symbols('q K X u')
den = (K - 1) * (q * K - 1)
alpha, beta = (K - q) / (K - 1), (q - 1) / (K - 1)
g2, g1, g0 = q * (K - 1) / (q * K - 1), (q - 1) * (K - q) / den, (q - 1) ** 2 / den
uu = lambda z: alpha * X * (z - 1 / q) * (z - q) ** 2 + beta * (z - 1) * (z - q ** 2) * (z - K / q)
vv = lambda z: g2 * X ** 2 * (z - 1) ** 2 * (z - q) + g1 * X * (z - q) ** 2 * (z - K / q) + g0 * (z - q ** 2) * (z - K / q) * (z - K)
det = sp.factor(uu(1) * vv(q) - uu(q) * vv(1))
expected = (q - K) * (q ** 2 - K) * (q - 1) ** 6 * (q + 1) / (q * (K - 1) * (q * K - 1))
assert sp.factor(det - expected) == 0
num = (K * u - 1) * (q * K * u - 1) - 2 * q * (u - 1) * (K * u - 1) + q * (u - 1) * (u - q)
assert sp.factor(num / den - (g2 * u ** 2 + g1 * u + g0)) == 0

results = []
for m in range(6, 13):
    p, zeta = field_for(m)
    h = min(m // 2, m - 5)
    ranks = []
    for k in range(3, m - 2):
        base, _ = normal_columns(m, k, p, zeta)
        extra = families(m, k, p, zeta)
        rb, ra = rank_columns(base, p), rank_columns(base + extra, p)
        assert (rb, ra) == (2 * m, 2 * m + 2 * h), (m, k, p, rb, ra)
        ranks.append({'k': k, 'base_rank': rb, 'augmented_rank': ra})
    result = {'m': m, 'prime': p, 'zeta': zeta, 'blocks': h,
              'independent_normal_columns': 2 * h * (m - 5),
              'bidegree_ranks': ranks}
    if m <= 8:
        checks, nonzero = local_checks(m, p, zeta)
        result.update(cofactor_identity_point_checks=checks,
                      nonzero_rhs_point_checks=nonzero)
    results.append(result)
path = Path(__file__).with_name('two_family_chord_results.json')
path.write_text(json.dumps({'symbolic_evaluation_determinant_verified': True,
                            'symbolic_ratio_numerator_verified': True,
                            'method': 'expanded coefficient products, exact modular row reduction, subset permanent DP, SymPy rational algebra',
                            'scope': 'finite checks; uniform conclusion uses the full R18 proof',
                            'results': results}, indent=2) + '\n')
print(json.dumps({'all_passed': True,
                  'bidegree_matrices_checked': sum(len(r['bidegree_ranks']) for r in results),
                  'cofactor_identity_point_checks': sum(r.get('cofactor_identity_point_checks', 0) for r in results),
                  'output': str(path)}))
