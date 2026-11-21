"""Exact incidence and independent cofactor checks for the refined O020."""
from __future__ import annotations

import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def incidence_matrix(R, n):
    assert R >= 1 and n >= R + 1
    pairs = [(a, b) for a in range(R) for b in range(a, R)]
    positions = {pair: i for i, pair in enumerate(pairs)}
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)
             if i < R]
    # Delete the last residue coordinate; it is minus the sum of the others.
    matrix = sp.zeros((n - 1) * len(pairs), R * len(edges))
    for edge_index, (i, j) in enumerate(edges):
        coefficients = [int(a == i) - int(a == j) for a in range(R)]
        for b in range(R):
            for a, coefficient in enumerate(coefficients):
                if not coefficient:
                    continue
                position = positions[tuple(sorted((a, b)))]
                if i < n - 1:
                    matrix[i * len(pairs) + position, edge_index * R + b] += coefficient
                if j < n - 1:
                    matrix[j * len(pairs) + position, edge_index * R + b] -= coefficient
    return matrix


incidence_cases = []
for R in range(1, 9):
    for extra in (0, 1, 3):
        n = R + 1 + extra
        matrix = incidence_matrix(R, n)
        rank = matrix.to_DM().rank()
        assert rank == matrix.rows
        if extra == 0:
            assert matrix.rows == matrix.cols
        incidence_cases.append({
            "R": R, "n": n, "rows": matrix.rows, "columns": matrix.cols,
            "exact_rank": rank, "extra_vertices": extra,
        })

smith_cases = []
for R in range(1, 7):
    matrix = incidence_matrix(R, R + 1)
    smith = smith_normal_form(matrix, domain=sp.ZZ)
    diagonal = [abs(int(smith[i, i])) for i in range(smith.rows)]
    torsion_rank = R * (R - 1) * (R - 2) // 6
    assert diagonal.count(2) == torsion_rank
    assert diagonal.count(1) == matrix.rows - torsion_rank
    assert set(diagonal) <= {1, 2}
    smith_cases.append({
        "R": R, "rank": matrix.rows,
        "unit_invariant_factors": diagonal.count(1),
        "two_invariant_factors": diagonal.count(2),
        "predicted_two_torsion_rank": torsion_rank,
    })

rank_cases = []
for R, n in [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]:
    t = sp.Symbol("t")
    z = sp.symbols(f"z0:{R}")
    zeta = list(z) + [sp.Integer(0)] * (n - R)
    matrix = sp.diag(*(t - (i + 1) for i in range(n)))
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i, j] = -(zeta[i] - zeta[j])
            if matrix[i, j] != 0:
                edges.append((i, j))
    assert sp.expand(matrix.det() - sp.prod(t - (i + 1) for i in range(n))) == 0
    gammas = sorted(
        (gamma for gamma in itertools.product(range(3), repeat=R)
         if sum(gamma) <= 2), key=lambda gamma: (sum(gamma), gamma),
    )
    basis = [(power,) + gamma for gamma in gammas
             for power in range(n - sum(gamma) + 1)]
    positions = {monomial: i for i, monomial in enumerate(basis)}

    def vector(polynomial):
        result = [sp.Integer(0)] * len(basis)
        for exponents, coefficient in sp.Poly(sp.expand(polynomial), t, *z).terms():
            if sum(exponents[1:]) <= 2:
                assert exponents in positions
                result[positions[exponents]] += coefficient
        return sp.Matrix(result)

    columns = []
    for i in range(n):
        cofactor = matrix.cofactor(i, i)
        for linear_form in (sp.Integer(1), t, *z):
            columns.append(vector(linear_form * cofactor))
    for i, j in edges:
        # Actual minors are independent of the inverse/path proof.
        cofactor = matrix.cofactor(j, i)
        for linear_form in z:
            columns.append(vector(linear_form * cofactor))
    jacobian = sp.Matrix.hstack(*columns)
    rank = jacobian.to_DM().rank()
    expected = n + 1 + R * n + R * (R + 1) // 2 * (n - 1)
    assert jacobian.rows == expected and rank == expected
    rank_cases.append({
        "R": R, "n": n, "target_dimension": expected,
        "selected_parameter_directions": jacobian.cols, "exact_rank": rank,
        "method": "direct symbolic cofactors, truncation, exact DomainMatrix rank",
    })

record = {
    "finding": "O-020 refined n>=r-1",
    "date_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro", "effort": "not exposed", "run": "GCT_KRON_20261120",
    "incidence_rank_checks": incidence_cases, "integral_smith_checks": smith_cases,
    "Jacobian_rank_checks": rank_cases,
    "scope": "Finite exact checks; universal incidence proof and all-copy theorem are in the text.",
    "status": "PASS",
}
destination = Path(__file__).with_name("binary_difference_jet_certificate.json")
destination.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({
    "status": "PASS", "incidence_cases": len(incidence_cases),
    "integral_smith_cases": len(smith_cases),
    "cofactor_ranks": [case["exact_rank"] for case in rank_cases],
    "certificate": str(destination),
}))
