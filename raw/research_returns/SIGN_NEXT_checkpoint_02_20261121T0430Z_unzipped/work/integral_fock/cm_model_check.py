#!/usr/bin/env python3
"""Exact checks for IF-10's CM signs, primitive lattices, and matrix units.

This checks the cohomological matrices, not rational equivalence of cycles
and not a Lean proof. Algebraic correspondences are constructed in the paper.
"""
from pathlib import Path
from itertools import combinations, product
import json
import sympy as S

ROOT = Path(__file__).resolve().parent
I = S.I
J = S.Matrix([[0, 1], [-1, 0]])
u = S.Matrix([1, I])
psi = S.Matrix([[0, 1], [-1, 0]])
p = (S.eye(2) - I * J) / 2
kappa = (u.T * psi * S.conjugate(u))[0]
assert J * u == I * u
assert p * p == p and p * u == u
assert p == u * S.conjugate(u).T / 2
assert (S.conjugate(u).T * u)[0] == 2
assert (u.T * u)[0] == 0
assert kappa == -2 * I
assert (u.row_join(S.Matrix([0, 1]))).det() == 1
assert S.expand(-(1 + I) ** 2) == kappa

tests = []
for r in range(1, 4):
    for h in range(r + 1):
        basis = list(combinations(range(2 * r), h))
        ix = {s: j for j, s in enumerate(basis)}
        subsets = list(combinations(range(r), h))
        V = S.zeros(len(basis), len(subsets))
        unit_rows = []
        for c, chosen in enumerate(subsets):
            unit_rows.append(ix[tuple(2 * a for a in chosen)])
            for bits in product(range(2), repeat=h):
                positions = tuple(2 * a + b for a, b in zip(chosen, bits))
                V[ix[positions], c] = I ** sum(bits)
        assert V.extract(unit_rows, range(V.cols)) == S.eye(V.cols)
        gram = S.conjugate(V).T * V
        assert gram == 2 ** h * S.eye(V.cols)
        dual = S.conjugate(V).T / 2 ** h
        projector = V * dual
        assert projector * projector == projector
        # Every E_JI is represented on the actual H^h exterior basis.
        units = {
            (a, b): V[:, a] * dual[b, :]
            for a in range(V.cols) for b in range(V.cols)
        }
        for (a, b), Eab in units.items():
            for c in range(V.cols):
                assert Eab * V[:, c] == (V[:, a] if b == c else S.zeros(V.rows, 1))
            for (c, d), Ecd in units.items():
                assert Eab * Ecd == (units[a, d] if b == c else S.zeros(V.rows))
        tests.append({
            'r': r, 'h': h, 'ambient_betti_rank': V.rows,
            'coefficient_rank': V.cols, 'primitive_unit_minor': True,
            'ambient_hermitian_scale': 2 ** h, 'matrix_units_pass': True,
        })

data = json.loads((ROOT / 'kernel_model_check.json').read_text())
weight_tests = {}
for name in ['actual_numEx_w0', 'numBig_distinguished_real_place_w0']:
    v = data[name]
    ds = [sum(a) for a in v['polynomial_parts']]
    ws = [sum(a) for a in v['true_weights']]
    assert ws == [d + len(a) * s for d, a, s in zip(ds, v['polynomial_parts'], v['det_shifts'])]
    assert [ws[1] - ws[0], ws[2] - ws[1]] == [-1600, -1888]
    weight_tests[name] = {
        'polynomial_degrees': ds, 'CM_exponents_per_embedding': ws,
        'native_collapsed_pair_lengths_at_1_plus_i': [2 * abs(w) for w in ws],
        'abstract_dual_unit_evaluation': True,
    }
assert weight_tests['actual_numEx_w0']['polynomial_degrees'] == [113, 841, 889]
assert weight_tests['actual_numEx_w0']['CM_exponents_per_embedding'] == [137, -1463, -3351]
assert weight_tests['numBig_distinguished_real_place_w0']['CM_exponents_per_embedding'] == [134, -1466, -3354]

out = {
    'kind': 'exact Python/SymPy cohomological computation; not a Lean check',
    'kappa': str(kappa), 'v_1_plus_i_kappa': 2,
    'native_pair_absolute_index': 4,
    'eigenline_basis_primitive': True,
    'projector_denominator_2_retained': True,
    'cohomological_matrix_unit_checks': tests,
    'actual_weight_checks': weight_tests,
}
(ROOT / 'cm_model_check.json').write_text(json.dumps(out, indent=2))
print(json.dumps({'passed': True, 'matrix_models': len(tests), 'weights': weight_tests}, indent=2))
