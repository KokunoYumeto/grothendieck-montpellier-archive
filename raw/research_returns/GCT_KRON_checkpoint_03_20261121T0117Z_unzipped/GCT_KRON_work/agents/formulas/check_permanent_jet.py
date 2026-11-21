"""Exact permanent cofactors with the distinguished diagonal held fixed.

This is an independent direct-minor check of F-021, not an inverse-matrix
implementation of the path lemma. Small sparse permanents are expanded by
row recursion with exact SymPy polynomial arithmetic.
"""
from datetime import datetime, timezone
from functools import lru_cache
from itertools import product
from math import comb, isqrt
from pathlib import Path
import json
import sympy as sp


def indices(R, degree):
    return sorted((a for a in product(range(degree + 1), repeat=R)
                   if sum(a) <= degree), key=lambda a: (sum(a), a))


def matrix(R, ell, h):
    assert R <= h*h
    z = sp.symbols(f'z0:{R}')
    zero = (0,)*R
    monomials = indices(R, ell)
    vertices = [(side, a, alpha) for side in ('in', 'out')
                for a in range(h) for alpha in monomials]
    ids = {v: i for i, v in enumerate(vertices)}
    A = sp.eye(len(vertices))
    for side, a, alpha in vertices:
        if alpha == zero:
            continue
        j = max(i for i, entry in enumerate(alpha) if entry)
        parent = list(alpha)
        parent[j] -= 1
        origin, target = (side, a, alpha), (side, a, tuple(parent))
        if side == 'out':
            origin, target = target, origin
        A[ids[origin], ids[target]] = z[j]
    for j, variable in enumerate(z):
        a, c = divmod(j, h)
        A[ids[('in', a, zero)], ids[('out', c, zero)]] = variable
    return A, z


def permanent_engine(A):
    n = A.rows
    all_bits = (1 << n)-1

    @lru_cache(None)
    def per(rows, cols):
        if not rows:
            return sp.Integer(1)
        active_rows = [i for i in range(n) if rows & (1 << i)]
        active_cols = [j for j in range(n) if cols & (1 << j)]
        i = min(active_rows,
                key=lambda u: sum(A[u, j] != 0 for j in active_cols))
        choices = [j for j in active_cols if A[i, j] != 0]
        if not choices:
            return sp.Integer(0)
        return sp.expand(sum(A[i, j]*per(rows ^ (1 << i),
                                        cols ^ (1 << j)) for j in choices))

    return per, all_bits


checks = []
for R, ell, h in [(1, 0, 1), (2, 0, 2), (3, 0, 2),
                  (1, 1, 1), (2, 1, 2), (3, 1, 2), (1, 2, 1)]:
    A, z = matrix(R, ell, h)
    per, full = permanent_engine(A)
    base = per(full, full)
    assert base == 1 and A[0, 0] == 1
    degree = 2*ell+2
    target = indices(R, degree)
    column_vectors = set()
    witness = {}
    tested_cofactors = 0
    for i in range(A.rows):
        for j in range(A.cols):
            if (i, j) == (0, 0):
                continue  # X11 is fixed as the padding form.
            cofactor = per(full ^ (1 << i), full ^ (1 << j))
            tested_cofactors += 1
            if cofactor == 0:
                continue
            for H in (sp.Integer(1),) + z:
                coeffs = sp.Poly(sp.expand(H*cofactor), *z).as_dict()
                vector = tuple(coeffs.get(alpha, 0) for alpha in target)
                column_vectors.add(vector)
                witness.setdefault(vector, (i, j, H))
    jacobian = sp.Matrix(list(column_vectors)).T
    rank = jacobian.rank()
    expected = comb(R+degree, degree)
    assert rank == expected
    # The proof claims a unit minor, not just rational full rank.
    for k in range(expected):
        unit = tuple(int(j == k) for j in range(expected))
        assert unit in column_vectors
    row = {'R': R, 'ell': ell, 'h': h, 'matrix_size': A.rows,
           'jet_order': degree, 'jet_dimension': expected,
           'exact_rank_with_X11_fixed': rank,
           'all_unit_jacobian_columns_present': True,
           'direct_minors_evaluated': tested_cofactors,
           'base_permanent': str(base)}
    if (R, ell, h) == (1, 1, 1):
        x, eps = sp.symbols('x epsilon')
        top = tuple(int(alpha == (degree,)) for alpha in target)
        i, j, H = witness[top]
        assert i != j and (i, j) != (0, 0)
        homogeneous = A + (x-1)*sp.eye(A.rows)
        homogeneous[i, j] += eps*H
        padded_matrix = sp.diag(homogeneous, x)
        direct_per, bits = permanent_engine(padded_matrix)
        m, n = padded_matrix.rows, padded_matrix.rows+2
        internally_padded = sp.expand(padded_matrix[0, 0]**(n-m)
                                      * direct_per(bits, bits))
        assert padded_matrix[0, 0] == x
        assert internally_padded == x**n + eps*x**(n-degree)*z[0]**degree
        row['direct_internal_padding_polynomial'] = str(internally_padded)
        row['m_n'] = [m, n]
    checks.append(row)

star_checks = []
for R in (3, 4):
    z = sp.symbols(f'w0:{R}')
    vertices = [('center',)] + [('core', i) for i in range(R)]
    vertices += [(side, i, j) for side in ('in', 'out')
                 for i in range(R) for j in range(i, R)]
    ids = {v: k for k, v in enumerate(vertices)}
    A = sp.eye(len(vertices))
    center = ids[('center',)]
    sigma = lambda i: (i+1) % R
    inverse_sigma = lambda j: (j-1) % R
    for i in range(R):
        A[ids[('core', i)], center] = z[i]
        A[center, ids[('core', i)]] = z[sigma(i)]
        for j in range(i, R):
            A[ids[('in', i, j)], ids[('core', i)]] = z[j]
            A[ids[('core', inverse_sigma(j))], ids[('out', i, j)]] = z[i]
    fixed = ids[('in', 0, 0)]
    per, full = permanent_engine(A)
    expected_base = 1+sum(z[i]*z[sigma(i)] for i in range(R))
    assert per(full, full) == expected_base
    directions = [(center, center, sp.Integer(1))]
    for k in range(R):
        directions.append((ids[('core', k)], center, z[sigma(k)]))
    for i in range(R):
        for k in range(R):
            if i != k:
                directions.append((ids[('core', k)], ids[('core', i)],
                                   z[i]*z[sigma(k)]))
    for i in range(R):
        for j in range(i, R):
            for a in range(R):
                for b in range(a, R):
                    if i != inverse_sigma(b):
                        directions.append((ids[('out', a, b)], ids[('in', i, j)],
                                           z[i]*z[j]*z[a]*z[b]))
    target = indices(R, 5)
    vectors = set()
    for i, j, expected in directions:
        assert (i, j) != (fixed, fixed)
        cofactor = per(full ^ (1 << i), full ^ (1 << j))
        assert sp.expand(cofactor-expected) == 0
        for H in (sp.Integer(1),)+z:
            coeffs = sp.Poly(sp.expand(H*cofactor), *z).as_dict()
            vectors.add(tuple(coeffs.get(alpha, 0) for alpha in target))
    expected_dimension = comb(R+5, 5)
    for k in range(expected_dimension):
        assert tuple(int(j == k) for j in range(expected_dimension)) in vectors
    rank = sp.Matrix(list(vectors)).T.rank()
    assert rank == expected_dimension
    star_checks.append({'R': R, 'matrix_size': A.rows,
                        'base_permanent': str(expected_base),
                        'fixed_diagonal': list(vertices[fixed]),
                        'pure_cofactors_checked': len(directions),
                        'jet_order': 5, 'exact_rank': rank,
                        'all_unit_jacobian_columns_present': True})

R, r = 1023, 1024
h = isqrt(R)+(isqrt(R)**2 < R)
J = 2*h*comb(R+1, 1)
cover_lower = 1+(R*(R-1)+11)//12
assert (J, cover_lower) == (65536, 87127)
assert J+1 < cover_lower
result = {'finding': 'F-021 internal permanent jet dominance',
          'date_utc': datetime.now(timezone.utc).isoformat(),
          'reviewer': 'GPT-6 Astra Pro; effort not exposed; /root/positive_formulas',
          'run': 'GCT_KRON_20261120', 'status': 'PASS',
          'checks': checks,
          'cyclic_star_checks': star_checks,
          'strict_cover_example': {'r': r, 'm': J, 'n': J+1,
                                   'every_F018_cover_lower_bound': cover_lower},
          'scope': 'Exact finite direct-minor and Jacobian checks supplement the full all-parameter proof.'}
destination = Path(__file__).with_name('permanent_jet_certificate.json')
destination.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'cases': len(checks),
                  'ranks': [row['exact_rank_with_X11_fixed'] for row in checks],
                  'cyclic_star_ranks': [row['exact_rank'] for row in star_checks],
                  'certificate': str(destination)}))
