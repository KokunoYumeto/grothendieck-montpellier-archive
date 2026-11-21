"""Independent small exact Jacobian checks for compressed-tree M-013.

Constructs the actual polynomial matrix, computes its symbolic inverse,
and ranks all linear-entry cofactor perturbations on the full jet space.
"""
from datetime import datetime, timezone
from itertools import product
from math import comb
from pathlib import Path
import json
import sympy as sp


def indices(R, degree):
    return sorted((a for a in product(range(degree + 1), repeat=R)
                   if sum(a) <= degree), key=lambda a: (sum(a), a))


def base_matrix(R, ell, h):
    assert R <= h * h
    z = sp.symbols(f'z0:{R}')
    monomials = indices(R, ell)
    vertices = [(side, a, gamma) for side in ('left', 'right')
                for a in range(h) for gamma in monomials]
    ids = {vertex: i for i, vertex in enumerate(vertices)}
    B = sp.zeros(len(vertices))
    zero = (0,) * R
    for side, a, gamma in vertices:
        if not any(gamma):
            continue
        j = max(i for i, value in enumerate(gamma) if value)
        parent = list(gamma)
        parent[j] -= 1
        parent = tuple(parent)
        origin, target = (side, a, gamma), (side, a, parent)
        if side == 'right':
            origin, target = target, origin
        B[ids[origin], ids[target]] = z[j]
    for j, variable in enumerate(z):
        a, b = divmod(j, h)
        B[ids[('left', a, zero)], ids[('right', b, zero)]] = variable
    return sp.eye(len(vertices)) - B, z


rows = []
for R, ell, h in [(2, 0, 2), (2, 1, 2), (3, 1, 2), (4, 1, 2), (1, 2, 1)]:
    A, z = base_matrix(R, ell, h)
    determinant = A.det(method='domain-ge')
    assert determinant == 1
    inverse = A.inv()
    assert A * inverse == sp.eye(A.rows)
    degree = 2 * ell + 2
    target_monomials = indices(R, degree)
    vectors = set()
    witness = {}
    for i in range(A.rows):
        for j in range(A.cols):
            cofactor = inverse[j, i]
            if cofactor == 0:
                continue
            for multiplier in (sp.Integer(1),) + z:
                polynomial = sp.Poly(sp.expand(cofactor * multiplier), *z)
                coefficients = polynomial.as_dict()
                vector = tuple(coefficients.get(a, 0) for a in target_monomials)
                vectors.add(vector)
                witness.setdefault(vector, (i, j, multiplier))
    J = sp.Matrix(list(vectors)).T
    rank = J.rank()
    expected = comb(R + degree, degree)
    assert rank == expected == len(target_monomials)
    row = {'R': R, 'ell': ell, 'h': h, 'matrix_size': A.rows,
           'jet_degree': degree, 'expected_jet_dimension': expected,
           'distinct_jacobian_columns': len(vectors), 'exact_rank': rank,
           'determinant_at_base': str(determinant)}
    if (R, ell, h) == (1, 2, 1):
        top = tuple(1 if a == (degree,) else 0 for a in target_monomials)
        i, j, multiplier = witness[top]
        eps = sp.Symbol('epsilon')
        perturbation = sp.zeros(A.rows)
        perturbation[i, j] = eps * multiplier
        perturbed_determinant = sp.expand((A + perturbation).det())
        derivative = sp.diff(perturbed_determinant, eps).subs(eps, 0)
        assert derivative == z[0] ** degree
        row['direct_top_degree_perturbation_determinant'] = str(perturbed_determinant)
        row['direct_derivative'] = str(derivative)
    rows.append(row)

result = {'finding': 'M-013 compressed-tree jet construction',
          'date_utc': datetime.now(timezone.utc).isoformat(),
          'reviewer': '/root/positive_formulas; GPT-6 Astra Pro; effort not exposed',
          'run': 'GCT_KRON_20261120', 'checks': rows, 'status': 'PASS',
          'scope': 'Finite exact Jacobian certificates supplement, and do not replace, the all-parameter path and dominance proof.'}
destination = Path(__file__).with_name('jet_jacobian_certificate.json')
destination.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'cases': len(rows),
                  'ranks': [x['exact_rank'] for x in rows], 'certificate': str(destination)}))
