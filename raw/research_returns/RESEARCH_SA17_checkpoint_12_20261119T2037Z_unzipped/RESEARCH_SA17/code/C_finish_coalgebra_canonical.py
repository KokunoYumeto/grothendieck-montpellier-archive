#!/usr/bin/env python3
"""Exact finite-coalgebra certificate for O_3 in characteristics 3 and 5.

This constructs the actual coordinate quotient, not the finite group O_3(F_p).
It verifies the degree-two coalgebra and the complete centralizer algebras of
the standard, exterior-square and symmetric-square rational representations.
It is a bounded certificate supporting the symbolic classification construction;
it is not an implementation of the full Belitskii parameter-template algorithm.
"""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
from time import perf_counter
import hashlib
import json
import numpy as np
import sympy as sp


def compositions(d, n):
    if n == 1:
        yield (d,)
    else:
        for i in range(d + 1):
            for tail in compositions(d - i, n - 1):
                yield (i,) + tail


def add_entry(d, key, value, p):
    v = (d.get(key, 0) + int(value)) % p
    if v:
        d[key] = v
    elif key in d:
        del d[key]


def rank_mod(a, p):
    a = np.array(a, dtype=np.int64, copy=True) % p
    if a.ndim == 1:
        a = a.reshape(1, -1)
    row = 0
    for col in range(a.shape[1]):
        ix = np.flatnonzero(a[row:, col])
        if not len(ix):
            continue
        j = row + int(ix[0])
        a[[row, j]] = a[[j, row]]
        a[row] = a[row] * pow(int(a[row, col]), -1, p) % p
        for j in range(row + 1, a.shape[0]):
            if a[j, col]:
                a[j] = (a[j] - a[j, col] * a[row]) % p
        row += 1
        if row == a.shape[0]:
            break
    return row


def inverse_mod(a, p):
    a = np.array(a, dtype=np.int64, copy=True) % p
    n = len(a)
    a = np.concatenate((a, np.eye(n, dtype=np.int64)), axis=1)
    for col in range(n):
        j = col + int(np.flatnonzero(a[col:, col])[0])
        a[[col, j]] = a[[j, col]]
        a[col] = a[col] * pow(int(a[col, col]), -1, p) % p
        for j in range(n):
            if j != col and a[j, col]:
                a[j] = (a[j] - a[j, col] * a[col]) % p
    return a[:, n:]


def centralizer_dimension(mats, p):
    n = mats.shape[1]
    rows = []
    for a in mats:
        for i in range(n):
            for j in range(n):
                row = np.zeros((n, n), dtype=np.int64)
                row[i, :] += a[:, j]
                row[:, j] -= a[i, :]
                if np.any(row % p):
                    rows.append(row.reshape(-1))
    return n * n - rank_mod(rows, p)


def run(p):
    start = perf_counter()
    x = sp.symbols('x0:9')
    X = sp.Matrix(3, 3, x)
    equations = X.T * X - sp.eye(3)
    gb_start = perf_counter()
    gb = sp.groebner([equations[i, j] for i in range(3)
                     for j in range(i, 3)], *x,
                    order='grevlex', modulus=p)
    gb_seconds = perf_counter() - gb_start
    leading = [f.LM(order=gb.order).exponents for f in gb.polys]
    zero = (0,) * 9
    units = [tuple(int(i == j) for i in range(9)) for j in range(9)]

    @lru_cache(None)
    def normal(monomial):
        expression = sp.prod(xi ** a for xi, a in zip(x, monomial))
        nf = gb.reduce(expression)[1]
        return {tuple(a): int(c) % p for a, c in
                sp.Poly(nf, *x, modulus=p).as_dict().items() if int(c) % p}

    def reduced_expr(expression):
        return {tuple(a): int(c) % p for a, c in
                sp.Poly(gb.reduce(expression)[1], *x,
                        modulus=p).as_dict().items() if int(c) % p}

    def standard(d):
        return [a for degree in range(d + 1) for a in compositions(degree, 9)
                if not any(all(ai >= bi for ai, bi in zip(a, lead))
                           for lead in leading)]

    basis = standard(2)
    idx = {a: i for i, a in enumerate(basis)}
    ncoal = len(basis)
    assert [len(standard(d)) for d in range(4)] == [1, 10, 44, 119]
    eps = np.array([int(all(a[j] == 0 for j in (1, 2, 3, 5, 6, 7)))
                    for a in basis], dtype=np.int64)
    coproduct = []
    for monomial in basis:
        raw = {(zero, zero): 1}
        for ij, power in enumerate(monomial):
            i, j = divmod(ij, 3)
            for _ in range(power):
                nxt = {}
                for (a, b), c in raw.items():
                    for k in range(3):
                        aa = tuple(u + v for u, v in zip(a, units[3*i+k]))
                        bb = tuple(u + v for u, v in zip(b, units[3*k+j]))
                        add_entry(nxt, (aa, bb), c, p)
                raw = nxt
        delta = {}
        for (a, b), c in raw.items():
            for aa, ca in normal(a).items():
                for bb, cb in normal(b).items():
                    add_entry(delta, (idx[aa], idx[bb]), c*ca*cb, p)
        coproduct.append(delta)

    antipode = []
    for monomial in basis:
        transposed = tuple(monomial[3*j+i] for i in range(3) for j in range(3))
        antipode.append({idx[a]: c for a, c in normal(transposed).items()})

    for gamma, delta in enumerate(coproduct):
        left, right = {}, {}
        eleft, eright = {}, {}
        sleft, sright = {}, {}
        for (a, b), c in delta.items():
            for (u, v), d in coproduct[a].items():
                add_entry(left, (u, v, b), c*d, p)
            for (u, v), d in coproduct[b].items():
                add_entry(right, (a, u, v), c*d, p)
            add_entry(eleft, b, c*eps[a], p)
            add_entry(eright, a, c*eps[b], p)
            for u, d in antipode[a].items():
                product = tuple(i+j for i, j in zip(basis[u], basis[b]))
                for v, e in normal(product).items():
                    add_entry(sleft, v, c*d*e, p)
            for v, d in antipode[b].items():
                product = tuple(i+j for i, j in zip(basis[a], basis[v]))
                for u, e in normal(product).items():
                    add_entry(sright, u, c*d*e, p)
        assert left == right
        assert eleft == eright == {gamma: 1}
        assert sleft == sright == ({zero: int(eps[gamma])} if eps[gamma] else {})
    for matrix in (X.T * X - sp.eye(3), X * X.T - sp.eye(3)):
        for expression in matrix:
            assert not reduced_expr(expression)

    multiplication = [[{} for _ in basis] for _ in basis]
    for gamma, delta in enumerate(coproduct):
        for (a, b), c in delta.items():
            multiplication[a][b][gamma] = c

    def coefficient_matrices(polynomial_matrix):
        n = polynomial_matrix.rows
        matrices = np.zeros((ncoal, n, n), dtype=np.int64)
        for i in range(n):
            for j in range(n):
                for a, c in reduced_expr(polynomial_matrix[i, j]).items():
                    matrices[idx[a], i, j] = c
        return matrices

    standard_mats = coefficient_matrices(X)
    tensor_mats = coefficient_matrices(sp.kronecker_product(X, X))
    pairs = list(combinations(range(3), 2))
    exterior_polys = sp.Matrix(3, 3, lambda a, b:
        X[pairs[a][0], pairs[b][0]] * X[pairs[a][1], pairs[b][1]] -
        X[pairs[a][0], pairs[b][1]] * X[pairs[a][1], pairs[b][0]])
    exterior_mats = coefficient_matrices(exterior_polys)

    columns = []
    for i in range(3):
        v = np.zeros(9, dtype=np.int64)
        v[3*i+i] = 1
        columns.append(v)
    for i, j in pairs:
        v = np.zeros(9, dtype=np.int64)
        v[3*i+j] = v[3*j+i] = 1
        columns.append(v)
    for i, j in pairs:
        v = np.zeros(9, dtype=np.int64)
        v[3*i+j], v[3*j+i] = 1, -1
        columns.append(v)
    E = np.stack(columns, axis=1) % p
    Einv = inverse_mod(E, p)
    decomposed = np.array([Einv @ a @ E % p for a in tensor_mats])
    assert not np.any(decomposed[:, :6, 6:])
    assert not np.any(decomposed[:, 6:, :6])
    symmetric_mats = decomposed[:, :6, :6]
    assert np.array_equal(decomposed[:, 6:, 6:], exterior_mats)

    algebra_checks = 0
    form_checks = 0
    for name, mats, gram in [
        ('standard', standard_mats, np.eye(3, dtype=np.int64)),
        ('tensor_square', tensor_mats, np.eye(9, dtype=np.int64)),
        ('symmetric_square', symmetric_mats, E[:, :6].T @ E[:, :6] % p),
        ('exterior_square', exterior_mats, np.eye(3, dtype=np.int64))]:
        n = mats.shape[1]
        assert np.array_equal(sum(int(eps[a])*mats[a] for a in range(ncoal)) % p,
                              np.eye(n, dtype=np.int64))
        for a in range(ncoal):
            for b in range(ncoal):
                target = np.zeros((n, n), dtype=np.int64)
                for c, coefficient in multiplication[a][b].items():
                    target += coefficient * mats[c]
                assert np.array_equal(mats[a] @ mats[b] % p, target % p), name
                algebra_checks += 1
        dual_mats = np.zeros_like(mats)
        for a in range(ncoal):
            for b, coefficient in antipode[a].items():
                dual_mats[b] = (dual_mats[b] + coefficient*mats[a].T) % p
        assert rank_mod(gram, p) == n
        for a in range(ncoal):
            assert np.array_equal(gram @ mats[a] % p, dual_mats[a] @ gram % p)
            form_checks += 1

    dimensions = {
        'standard': centralizer_dimension(standard_mats, p),
        'symmetric_square': centralizer_dimension(symmetric_mats, p),
        'exterior_square': centralizer_dimension(exterior_mats, p)}
    assert dimensions == {'standard': 1, 'symmetric_square': 2, 'exterior_square': 1}
    q = np.array([1, 1, 1, 0, 0, 0], dtype=np.int64)
    K = np.outer(q, q) % p
    I = np.eye(6, dtype=np.int64)
    assert rank_mod(np.stack((I.reshape(-1), K.reshape(-1))), p) == 2
    for a in symmetric_mats:
        assert np.array_equal(a @ K % p, K @ a % p)
    assert np.array_equal(K @ K % p, 3*K % p)
    if p == 3:
        assert not np.any(K @ K % p) and np.any(K)
        description = 'End(Sym2 V)=F3[e]/e2; absolutely indecomposable of rank6'
    else:
        projector = K * pow(3, -1, p) % p
        assert np.array_equal(projector @ projector % p, projector)
        assert rank_mod(projector, p) == 1
        assert rank_mod(I-projector, p) == 5
        description = 'End(Sym2 V)=F5 x F5; absolute indecomposable ranks1 and5'

    # Hodge comparison: the ordered basis (01,02,12) corresponds to (2,-1,0).
    hodge = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
    detX = X.det()
    for expression in hodge*exterior_polys - detX*X*hodge:
        assert not reduced_expr(expression)
    assert not reduced_expr(detX*detX - 1)
    basis_serial = json.dumps(basis, separators=(',', ':')).encode()
    return {
        'prime': p,
        'object': 'coordinate Hopf algebra Fp[x_ij]/(X^t X-I), not O3(Fp)',
        'groebner_order': 'grevlex',
        'groebner_basis_size': len(gb.polys),
        'groebner_seconds': gb_seconds,
        'coalgebra_dimensions_d0_to_d3': [1, 10, 44, 119],
        'degree2_basis_sha256': hashlib.sha256(basis_serial).hexdigest(),
        'degree2_coproduct_terms': sum(map(len, coproduct)),
        'coassociativity_checks': ncoal,
        'counit_checks': 2*ncoal,
        'antipode_checks': 2*ncoal,
        'orthogonal_equation_checks': 18,
        'dual_algebra_representation_checks': algebra_checks,
        'unit_representation_checks': 4,
        'invariant_form_coefficient_checks': form_checks,
        'centralizer_dimensions': dimensions,
        'centralizer_algebra_Sym2': 'span(I,K), K=q trace, K^2=3K',
        'absolute_decomposition': description,
        'hodge_and_determinant_checks': 10,
        'normal_form_cache': normal.cache_info()._asdict(),
        'seconds': perf_counter()-start,
        'result': 'PASS'}


def main():
    start = perf_counter()
    rows = [run(p) for p in (3, 5)]
    result = {'scope': __doc__, 'cases': rows, 'seconds': perf_counter()-start,
              'result': 'PASS'}
    target = Path(__file__).resolve().parents[1]/'logs/C_finish_coalgebra_canonical.json'
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
