#!/usr/bin/env python3
"""Independent permanent-projection certificate verification.

Uses Ryser's subset formula on integer evaluation points, rather than the
permutation expansion used to construct the coefficient Jacobians. Verifies
the complete evaluation Jacobian and a nonzero selected maximal minor.
"""
from pathlib import Path
from itertools import product
import hashlib
import json


def permanent_ryser(matrix, prime):
    n = len(matrix)
    total = 0
    for bits in product((0, 1), repeat=n):
        term = 1
        for row in matrix:
            term = term * sum(a * b for a, b in zip(row, bits)) % prime
        total = (total + (-1)**(n-sum(bits)) * term) % prime
    return total


def determinant_mod(matrix, prime):
    a = [list(map(lambda x: int(x) % prime, row)) for row in matrix]
    answer = 1
    for j in range(len(a)):
        candidates = [i for i in range(j, len(a)) if a[i][j]]
        if not candidates: return 0
        i = candidates[0]
        if i != j:
            a[i], a[j] = a[j], a[i]; answer *= -1
        p = a[j][j]; answer = answer * p % prime
        inv = pow(p, -1, prime)
        for i in range(j+1, len(a)):
            multiplier = a[i][j] * inv % prime
            a[i] = [(x-multiplier*y) % prime for x, y in zip(a[i], a[j])]
    return answer % prime


def verify(n):
    path = Path(__file__).parents[1] / 'rectangular' / f'permanent_{n}_four_variable_certificate.json'
    data = json.loads(path.read_text()); p = data['prime']
    pencil = data['pencil_coefficients_i_j_k']
    alpha = data['row_monomial_exponents']; params = data['column_parameters_zero_based']
    J = data['jacobian_integer']; selected = data['selected_columns_zero_based']
    evaluation, direct = [], []
    for point in alpha:
        evaluation.append([__import__('math').prod(pow(x, e, p) for x, e in zip(point, a)) % p for a in alpha])
        evaluated = [[sum(c*x for c, x in zip(entry, point)) % p for entry in row] for row in pencil]
        cof = {(i, j): permanent_ryser([[evaluated[a][b] for b in range(n) if b != j]
                                       for a in range(n) if a != i], p)
               for i in range(n) for j in range(n)}
        direct.append([point[k]*cof[i,j] % p for i, j, k in params])
    for i, row in enumerate(evaluation):
        for j in range(len(params)):
            assert sum(row[k]*J[k][j] for k in range(len(alpha))) % p == direct[i][j]
    E_det = determinant_mod(evaluation, p)
    J_det = determinant_mod([[row[j] for j in selected] for row in J], p)
    D_det = determinant_mod([[row[j] for j in selected] for row in direct], p)
    assert E_det and J_det and D_det
    assert E_det*J_det % p == D_det
    assert J_det == data['minor_determinant_mod_prime']
    assert int(data['minor_determinant_integer']) % p == J_det
    return {'n': n, 'rank': len(alpha), 'prime': p, 'evaluation_matrix_determinant': E_det,
            'coefficient_jacobian_minor_determinant': J_det,
            'independent_evaluation_jacobian_minor_determinant': D_det,
            'all_jacobian_entries_verified': len(alpha)*len(params),
            'certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'method': 'Ryser subset permanent; homogeneous-simplex evaluations; exact finite-field elimination',
            'status': 'PASS'}


if __name__ == '__main__':
    results = [verify(4), verify(5)]
    out = Path(__file__).with_name('permanent_projection_independent_results.json')
    out.write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results))
