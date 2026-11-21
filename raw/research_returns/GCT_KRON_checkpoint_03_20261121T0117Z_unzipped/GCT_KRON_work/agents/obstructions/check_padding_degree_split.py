"""Exact finite checks for O012; the saved proof, not these cases, is universal."""
from __future__ import annotations

import itertools
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp


def indices(k, degree):
    return sorted((a for a in itertools.product(range(degree + 1), repeat=k)
                   if sum(a) <= degree), key=lambda a: (sum(a), a))


def split(a, first_limit):
    remaining = min(sum(a), first_limit)
    left = []
    for value in a:
        take = min(value, remaining)
        left.append(take)
        remaining -= take
    return tuple(left), tuple(x - y for x, y in zip(a, left))


def matrix_for(b, r, L, z, coefficients, caps=None):
    u, v = (b - 1) // 2, b // 2
    zero = (0,) * (r - 1)
    prefix, suffix = indices(r - 1, u), indices(r - 1, v)
    if caps is not None:
        prefix = [a for a in prefix if all(x <= c for x, c in zip(a, caps))]
        suffix = [a for a in suffix if all(x <= c for x, c in zip(a, caps))]
    locations = {("p", zero): 0, ("s", zero): 0}
    cursor = 1
    for side, entries in (("p", prefix), ("s", suffix)):
        for a in entries:
            if a != zero:
                locations[side, a] = cursor
                cursor += 1
    matrix = sp.zeros(cursor)
    for index in range(1, cursor):
        matrix[index, index] = L
    for side, entries in (("p", prefix), ("s", suffix)):
        for a in entries:
            if a == zero:
                continue
            j = max(i for i, x in enumerate(a) if x)
            parent = tuple(x - (i == j) for i, x in enumerate(a))
            source, target = locations[side, parent], locations[side, a]
            if side == "s":
                source, target = target, source
            matrix[source, target] -= z[j]
    form = 0
    for gamma, coefficient in coefficients.items():
        monomial = coefficient * L ** (b - sum(gamma))
        for variable, power in zip(z, gamma):
            monomial *= variable ** power
        form += monomial
        remaining = gamma
        edge_label = coefficient * L
        if sum(gamma) == b:
            j = next(i for i, x in enumerate(gamma) if x)
            remaining = tuple(x - (i == j) for i, x in enumerate(gamma))
            edge_label = coefficient * z[j]
        alpha, beta = split(remaining, u)
        matrix[locations["p", alpha], locations["s", beta]] += edge_label
    expected_size = len(prefix) + len(suffix) - 1
    assert cursor == expected_size
    return matrix, form


symbolic_results = []
for b, r in [(1, 3), (2, 2), (2, 3), (3, 2)]:
    L = sp.Symbol("L")
    z = sp.symbols(f"z0:{r - 1}")
    all_indices = indices(r - 1, b)
    coefficients = dict(zip(all_indices, sp.symbols(f"c0:{len(all_indices)}")))
    matrix, form = matrix_for(b, r, L, z, coefficients)
    residual = sp.expand(matrix.det() - L ** (matrix.rows - b) * form)
    assert residual == 0
    symbolic_results.append({"b": b, "r": r, "size": matrix.rows,
                             "universal_coefficient_residual": str(residual)})

integer_results = []
for b, r in [(1, 5), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
             (3, 4), (4, 4), (5, 4), (2, 8), (4, 5)]:
    for L in (1, 2):
        z = tuple((i + 1) * (-1 if i % 2 else 1) for i in range(r - 1))
        coefficients = {a: ((j * 7 + 3) % 19) - 9
                        for j, a in enumerate(indices(r - 1, b))}
        matrix, form = matrix_for(b, r, L, z, coefficients)
        determinant = matrix.det(method="domain-ge")
        expected = L ** (matrix.rows - b) * form
        assert determinant == expected
        integer_results.append({"b": b, "r": r, "L": L,
                                "size": matrix.rows, "determinant": str(determinant),
                                "expected": str(expected)})

padding_results = []
for b, r, p, d in [(1, 2, 1, 2), (2, 3, 3, 2), (3, 2, 2, 3)]:
    factors = [math.factorial(a[0] + p) // math.factorial(a[0])
               for a in indices(r, b) if sum(a) == b]
    symmetric_factors = [math.prod(factors[i] for i in multiset)
                         for multiset in itertools.combinations_with_replacement(
                             range(len(factors)), d)]
    assert min(symmetric_factors) > 0
    padding_results.append({"b": b, "r": r, "p": p, "d": d,
                            "RT_diagonal": factors,
                            "symmetric_power_dimension": len(symmetric_factors),
                            "minimum_symmetric_diagonal": min(symmetric_factors)})

assert 2 * math.comb(2 * 2 + 11, 12) - 1 == 909
assert 2 * 3 ** 12 < math.factorial(12)

certificate = {
    "finding": "O-012.a/b",
    "date_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro",
    "effort": "not exposed",
    "run": "GCT_KRON_20261120",
    "scope": "Exact finite checks; universal statements established in the accompanying proofs.",
    "symbolic_graph_identities": symbolic_results,
    "integer_graph_identities": integer_results,
    "padding_pairing_diagonals": padding_results,
    "uniform_bound_checks": {"B_25_4": 909,
                              "two_times_three_to_twelve": 2 * 3 ** 12,
                              "factorial_twelve": math.factorial(12)},
    "status": "PASS",
}
destination = Path(__file__).with_name("padding_degree_split_certificate.json")
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print(json.dumps({"status": "PASS", "symbolic_identities": len(symbolic_results),
                  "integer_identities": len(integer_results),
                  "padding_cases": len(padding_results), "certificate": str(destination)}))
