"""Exact finite-field sanity checks for R16; not a proof by extrapolation.

The normal-space ranks are computed from expanded binary coefficient
products, with no Fourier decomposition or Schur determinant in the
algorithm.  Additional-block cofactor identities are checked at exact
finite-field points using subset permanent DP.
"""
from __future__ import annotations

import json
from pathlib import Path

from sympy import isprime, primitive_root


def field_for(m):
    p = m + 1
    while not isprime(p):
        p += m
    zeta = pow(int(primitive_root(p)), (p - 1) // m, p)
    assert pow(zeta, m, p) == 1
    assert all(pow(zeta, i, p) != 1 for i in range(1, m))
    return p, zeta


def product_coefficients(indices, roots, p):
    coefficients = [1]
    for i in indices:
        out = [0] * (len(coefficients) + 1)
        for r, coefficient in enumerate(coefficients):
            out[r] = (out[r] + coefficient) % p
            out[r + 1] = (out[r + 1] - roots[i] * coefficient) % p
        coefficients = out
    return coefficients


def rank_columns(columns, p):
    matrix = [list(row) for row in zip(*columns)]
    rows, cols = len(matrix), len(columns)
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inv = pow(matrix[rank][col], -1, p)
        matrix[rank] = [(x * inv) % p for x in matrix[rank]]
        for i in range(rank + 1, rows):
            factor = matrix[i][col]
            if factor:
                matrix[i] = [(x - factor * y) % p
                             for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def normal_columns(m, k, p, zeta):
    roots = [pow(zeta, i, p) for i in range(m)]
    base, extra = [], []
    h = min(m // 2, m - 3)
    for a in range(m):
        interval = {(a + j) % m for j in range(k)}
        aa = product_coefficients([i for i in range(m) if i not in interval], roots, p)
        bb = product_coefficients([(a + j) % m for j in range(k - 1)], roots, p)
        base.append([(aa[r] * (bb[s] if s < len(bb) else 0)) % p
                     for r in range(m - k + 1) for s in range(k + 1)])
        base.append([(aa[r] * (bb[s - 1] if 1 <= s <= len(bb) else 0)) % p
                     for r in range(m - k + 1) for s in range(k + 1)])
    for a in range(0, 2 * h, 2):
        interval = {(a + j) % m for j in range(k + 1)}
        ai = [a] + [i for i in range(m) if i not in interval]
        bi = [a, (a + 2) % m] + [(a + j) % m for j in range(2, k)]
        aa = product_coefficients(ai, roots, p)
        bb = product_coefficients(bi, roots, p)
        extra.append([(aa[r] * bb[s]) % p
                      for r in range(m - k + 1) for s in range(k + 1)])
    return base, extra


def permanent(matrix, p):
    n = len(matrix)
    dp = [0] * (1 << n)
    dp[0] = 1
    for mask in range(1, 1 << n):
        row = mask.bit_count() - 1
        dp[mask] = sum(matrix[row][j] * dp[mask ^ (1 << j)]
                       for j in range(n) if mask & (1 << j)) % p
    return dp[-1]


def submatrix(matrix, deleted_rows, deleted_columns):
    return [[v for j, v in enumerate(row) if j not in deleted_columns]
            for i, row in enumerate(matrix) if i not in deleted_rows]


def check_cofactors(m, p, zeta):
    h = min(m // 2, m - 3)
    starts = list(range(0, 2 * h, 2))
    checked = nonzero_rhs = 0
    for sample in range(1, 8):
        x, y, z, w, epsilon = [v % p for v in
                              (sample + 1, sample ** 2 + 2,
                               sample ** 3 + 3, 2 * sample + 1, sample)]
        if not epsilon:
            epsilon = 1
        ell = [(x - pow(zeta, i, p) * y) % p for i in range(m)]
        vv = [(z - pow(zeta, i, p) * w) % p for i in range(m)]
        matrix = [[0] * m for _ in range(m)]
        for i in range(m):
            matrix[i][i] = ell[i]
            matrix[i][(i + 1) % m] = vv[i]
        for a in starts:
            matrix[a][(a + 2) % m] = epsilon * ell[a] % p
            matrix[(a + 1) % m][a] = epsilon * vv[(a + 2) % m] % p
        for a in starts:
            b, c = (a + 1) % m, (a + 2) % m
            pp, qq = matrix[a][c], matrix[b][a]
            for k in range(2, m - 1):
                r = (a + k) % m
                cof = [permanent(submatrix(matrix, {r}, {j}), p)
                       for j in (a, b, c)]
                rr = permanent(submatrix(matrix, {a, b, r}, {a, b, c}), p)
                predicted = [((vv[a] * vv[b] + pp * ell[b]) * rr) % p,
                             ((ell[a] * vv[b] + pp * qq) * rr) % p,
                             ((ell[a] * ell[b] + vv[a] * qq) * rr) % p]
                assert cof == predicted, (m, sample, a, k, cof, predicted)
                lhs = (ell[a] * cof[0] - vv[a] * cof[1] - pp * cof[2]) % p
                rhs = (-2 * epsilon ** 2 * ell[a] * vv[a] * vv[c] * rr) % p
                assert lhs == rhs, (m, sample, a, k, lhs, rhs)
                checked += 1
                nonzero_rhs += bool(rhs)
    return checked, nonzero_rhs


results = []
for m in range(4, 13):
    p, zeta = field_for(m)
    h = min(m // 2, m - 3)
    ranks = []
    for k in range(2, m - 1):
        base, extra = normal_columns(m, k, p, zeta)
        rb = rank_columns(base, p)
        ra = rank_columns(base + extra, p)
        assert (rb, ra) == (2 * m, 2 * m + h), (m, k, p, rb, ra)
        ranks.append({"k": k, "base_rank": rb, "augmented_rank": ra})
    entry = {"m": m, "prime": p, "zeta": zeta, "blocks": h,
             "normal_columns_independent_mod_base": h * (m - 3),
             "proved_rank_bound": 2 * m * m + 2 + h * (m - 3),
             "bidegree_ranks": ranks}
    if m <= 8:
        checked, nonzero = check_cofactors(m, p, zeta)
        entry.update(cofactor_identity_point_checks=checked,
                     nonzero_rhs_point_checks=nonzero)
    results.append(entry)

path = Path(__file__).with_name("simultaneous_chord_results.json")
path.write_text(json.dumps({"method": "expanded coefficient products and modular row reduction; subset permanent DP",
                            "scope": "finite sanity checks only; R16 proof is uniform",
                            "results": results}, indent=2) + "\n")
print(json.dumps({"bidegree_matrices_checked": sum(len(x["bidegree_ranks"]) for x in results),
                  "cofactor_identity_point_checks": sum(x.get("cofactor_identity_point_checks", 0) for x in results),
                  "all_passed": True,
                  "output": str(path)}))
