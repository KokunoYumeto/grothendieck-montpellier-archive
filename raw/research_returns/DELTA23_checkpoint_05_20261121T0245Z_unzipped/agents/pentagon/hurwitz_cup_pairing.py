#!/usr/bin/env python3
"""D23.P19: exact relative cup form in the 112-point Hurwitz block.

This is an algebraic certificate, not a simulation of an unknown GT element.
The naturality assertion is proved separately in hurwitz_cup_pairing.tex.
All arithmetic is in F3. Vectors are columns; cocycles are left cocycles.
"""
from pathlib import Path
import hashlib
import json
import numpy as np

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'characters/records/hurwitz_orthogonal112.json'


def rref(a):
    a = np.array(a, dtype=np.int64, copy=True) % 3
    row, pivots = 0, []
    for col in range(a.shape[1]):
        nz = np.flatnonzero(a[row:, col])
        if not len(nz):
            continue
        j = row + int(nz[0])
        a[[row, j]] = a[[j, row]]
        a[row] = a[row] * int(a[row, col]) % 3
        for k in range(a.shape[0]):
            if k != row and a[k, col]:
                a[k] = (a[k] - a[k, col] * a[row]) % 3
        pivots.append(col)
        row += 1
        if row == a.shape[0]:
            break
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def inverse(a):
    n = len(a)
    r, p = rref(np.c_[a, np.eye(n, dtype=int)])
    assert p[:n] == list(range(n))
    return r[:, n:]


def determinant(a):
    a = np.array(a, dtype=np.int64, copy=True) % 3
    det = 1
    for i in range(len(a)):
        nz = np.flatnonzero(a[i:, i])
        if not len(nz):
            return 0
        j = i + int(nz[0])
        if i != j:
            a[[i, j]] = a[[j, i]]
            det = -det
        det = det * int(a[i, i]) % 3
        a[i] = a[i] * int(a[i, i]) % 3
        for j in range(i + 1, len(a)):
            a[j] = (a[j] - a[j, i] * a[i]) % 3
    return int(det % 3)


source = json.loads(SOURCE.read_text())
linear = [np.array(a, dtype=int) for a in source['base_linear_tuple']]
identity = np.eye(2, dtype=int)
symplectic = np.array([[0, 1], [2, 0]], dtype=int)
product = identity.copy()
for a in linear:
    assert np.array_equal(a.T @ symplectic @ a % 3, symplectic)
    product = product @ a % 3
linear.append(inverse(product))
assert all(determinant(identity - a) != 0 for a in linear)


def cocycle_data(q):
    """q consists of four fixed points; append the determined fifth value."""
    q = [np.array(v, dtype=int) % 3 for v in np.array(q).reshape(4, 2)]
    values = [(identity - a) @ v % 3 for a, v in zip(linear, q)]
    prefix_matrix = identity.copy()
    prefix_value = np.zeros(2, dtype=int)
    for a, c in zip(linear, values):
        prefix_value = (prefix_value + prefix_matrix @ c) % 3
        prefix_matrix = prefix_matrix @ a % 3
    values.append(-inverse(prefix_matrix) @ prefix_value % 3)
    q.append(inverse(identity - linear[4]) @ values[4] % 3)
    check = np.zeros(2, dtype=int)
    p = identity.copy()
    for a, c in zip(linear, values):
        check = (check + p @ c) % 3
        p = p @ a % 3
    assert not check.any() and np.array_equal(p, identity)
    return values, q


def pairing(q, r):
    cs, qs = cocycle_data(q)
    ds, _ = cocycle_data(r)
    prefix_matrix = identity.copy()
    prefix_value = np.zeros(2, dtype=int)
    result = 0
    for a, c, d, fixed in zip(linear, cs, ds, qs):
        result += prefix_value @ symplectic @ prefix_matrix @ d
        result += fixed @ symplectic @ d
        prefix_value = (prefix_value + prefix_matrix @ c) % 3
        prefix_matrix = prefix_matrix @ a % 3
    return int(result % 3)


basis = np.eye(8, dtype=int)
gram8 = np.array([[pairing(u, v) for v in basis] for u in basis])
assert np.array_equal(gram8, gram8.T)
assert rank(gram8) == 6
diagonal_translations = np.tile(np.eye(2, dtype=int), (4, 1))
assert not (gram8 @ diagonal_translations % 3).any()
assert rank(diagonal_translations) == 2
# q4=0 is the canonical representative of the fixed-point-difference quotient.
gram6 = gram8[:6, :6]
assert rank(gram6) == 6 and determinant(gram6) == 1
assert np.array_equal(gram6, np.array(source['quadratic_form']))
matrices = [np.array(a) for a in source['stabilizer_matrices']]
assert all(np.array_equal(a.T @ gram6 @ a % 3, gram6) for a in matrices)

out = {
    'statement': 'D23.P19',
    'source': str(SOURCE.relative_to(HERE.parent.parent)),
    'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'coefficient_field': 'F3',
    'cocycle_convention': 'c(gh)=c(g)+rho(g)c(h); c(t_i)=(I-A_i)q_i',
    'symplectic_coefficient_form': symplectic.tolist(),
    'five_linear_monodromies': [a.tolist() for a in linear],
    'all_five_I_minus_A_invertible': True,
    'eight_dimensional_gram': gram8.tolist(),
    'gram_rank': 6,
    'radical_is_exactly_diagonal_translations': True,
    'six_dimensional_difference_gram': gram6.tolist(),
    'exactly_equals_C23_gram_without_rescaling': True,
    'all_13_stabilizer_matrices_preserve_canonical_gram': True,
    'scope': 'Exact form certificate; GT naturality is the separate relative-cohomology proof.',
    'result': 'PASS',
}
(HERE / 'hurwitz_cup_pairing.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
