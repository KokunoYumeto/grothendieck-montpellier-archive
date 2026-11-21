"""Independent permanent minors and exact example checks for O021."""
from __future__ import annotations

import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp


def permanent(matrix):
    result = sp.Integer(0)
    for permutation in itertools.permutations(range(matrix.rows)):
        product = sp.Integer(1)
        for row, column in enumerate(permutation):
            product *= matrix[row, column]
            if product == 0:
                break
        result += product
    return sp.expand(result)


cases = []
for R, s in [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]:
    t = sp.Symbol("t")
    z = sp.symbols(f"z0:{R}")
    zeta = list(z) + [sp.Integer(0)] * (s - R)
    matrix = sp.diag(*(t - (i + 1) for i in range(s)))
    edges = []
    for i in range(s):
        for j in range(i + 1, s):
            matrix[i, j] = zeta[i] - zeta[j]
            if matrix[i, j] != 0:
                edges.append((i, j))
    assert permanent(matrix) == sp.expand(sp.prod(t - (i + 1) for i in range(s)))
    gammas = sorted(
        (gamma for gamma in itertools.product(range(3), repeat=R)
         if sum(gamma) <= 2), key=lambda gamma: (sum(gamma), gamma),
    )
    basis = [(power,) + gamma for gamma in gammas
             for power in range(s - sum(gamma) + 1)]
    positions = {monomial: i for i, monomial in enumerate(basis)}

    def vector(polynomial):
        result = [sp.Integer(0)] * len(basis)
        for exponents, coefficient in sp.Poly(sp.expand(polynomial), t, *z).terms():
            if sum(exponents[1:]) <= 2:
                assert exponents in positions
                result[positions[exponents]] += coefficient
        return sp.Matrix(result)

    columns = []
    for i in range(s):
        minor = permanent(matrix.minor_submatrix(i, i))
        for linear_form in (sp.Integer(1), t, *z):
            columns.append(vector(linear_form * minor))
    for i, j in edges:
        minor = permanent(matrix.minor_submatrix(j, i))
        for linear_form in z:
            columns.append(vector(linear_form * minor))
    jacobian = sp.Matrix.hstack(*columns)
    rank = jacobian.to_DM().rank()
    expected = s + 1 + R * s + R * (R + 1) // 2 * (s - 1)
    assert rank == expected == jacobian.rows
    cases.append({
        "R": R, "s": s, "exact_rank": rank, "target_dimension": expected,
        "method": "direct permutation-sum permanent minors and exact DomainMatrix rank",
    })


def restricted_partition_count(total, width, height):
    # Independent recursion over weakly decreasing positive parts.
    def count(left, largest, rows):
        if left == 0:
            return 1
        if rows == 0:
            return 0
        return sum(count(left - part, part, rows - 1)
                   for part in range(1, min(left, largest) + 1))
    return count(total, width, height)


m, n, d, r, b = 9, 10, 6, 6, 8
partition = (44, 8, 2, 2, 2, 2)
assert sum(partition) == n * d
assert m >= max(r, b + 1) and n >= m
p6 = restricted_partition_count(6, d, n - 2)
p5 = restricted_partition_count(5, d, n - 2)
assert (p6, p5, p6 - p5) == (11, 7, 4)
assert b + r - 2 == 12 > n > m
s = m - 1
padding_diagonal = [sp.factorial(a + n - s) // sp.factorial(a) for a in range(s + 1)]
assert all(value > 0 for value in padding_diagonal)
target_dimension = s + 1 + (r - 2) * s + (r - 2) * (r - 1) // 2 * (s - 1)
assert target_dimension == 111

record = {
    "finding": "O-021",
    "date_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro", "effort": "not exposed", "run": "GCT_KRON_20261120",
    "permanent_minor_checks": cases,
    "strict_example": {
        "m": m, "n": n, "d": d, "r": r, "partition": partition,
        "base_degree": s, "transverse_target_dimension": target_dimension,
        "padding_diagonal": list(map(int, padding_diagonal)),
        "ambient_partition_counts": [p6, p5], "exact_multiplicity_by_proved_formula": p6 - p5,
        "universal_two_tree_lower_bound": b + r - 2,
    },
    "scope": "Finite independent minor checks; the arbitrary-rank padding and universal dominance proofs are in the text.",
    "status": "PASS",
}
destination = Path(__file__).with_name("permanent_transverse_jet_certificate.json")
destination.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({
    "status": "PASS", "permanent_minor_cases": len(cases),
    "exact_ranks": [case["exact_rank"] for case in cases],
    "strict_example_multiplicity": p6 - p5, "certificate": str(destination),
}))
