#!/usr/bin/env python3
"""Exact integral word-span closure for the explicitly specified string model.

The ambient ring is product_{i=0}^n Mat_{n-i+1}(Z), with one string in
degrees i,i+2,...,2n-i.  L is the unit upward shift.  D lowers v_r by
r(d-r+1), where d=n-i.  Lambda_N is the unit downward shift.

This is an exact finite computation in an expressly chosen ambient order;
it does not identify this order with an automorphic theta-lift lattice.
No floating point arithmetic and no Lean kernel are used.
"""

from pathlib import Path
import csv
import json

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

OUT = Path(__file__).resolve().parent


def data(n, normalized=False):
    coordinates = [
        (i, r, c)
        for i in range(n + 1)
        for r in range(n - i + 1)
        for c in range(n - i + 1)
    ]
    lookup = {key: a for a, key in enumerate(coordinates)}
    dim = len(coordinates)
    unit = sp.zeros(dim, 1)
    up = sp.zeros(dim, 1)
    down = sp.zeros(dim, 1)
    projectors = [sp.zeros(dim, 1) for _ in range(2 * n + 1)]
    for i in range(n + 1):
        d = n - i
        for r in range(d + 1):
            unit[lookup[i, r, r], 0] = 1
            projectors[i + 2 * r][lookup[i, r, r], 0] = 1
            if r < d:
                up[lookup[i, r + 1, r], 0] = 1
            if r > 0:
                down[lookup[i, r - 1, r], 0] = 1 if normalized else r * (d - r + 1)
    generators = [("L", up), ("Lambda_N" if normalized else "D", down)]
    generators.extend((f"pi_{j}", p) for j, p in enumerate(projectors))

    def right_matrix(g):
        action = sp.zeros(dim, dim)
        for column, (i, r, c) in enumerate(coordinates):
            for target_col in range(n - i + 1):
                action[lookup[i, r, target_col], column] = g[lookup[i, c, target_col], 0]
        return action

    return coordinates, unit, generators, [(name, right_matrix(g)) for name, g in generators]


def integral(matrix):
    return all(x.q == 1 for x in matrix)


def calculate(n, normalized=False):
    coords, unit, gens, actions = data(n, normalized)
    basis = unit
    history = []
    for iteration in range(100):
        expanded = sp.Matrix.hstack(basis, *(a * basis for _, a in actions))
        next_basis = hermite_normal_form(expanded)
        index = abs(int(next_basis.det())) if next_basis.cols == next_basis.rows else None
        history.append({"iteration": iteration + 1, "rank": next_basis.cols, "index": index})
        if next_basis == basis:
            break
        basis = next_basis
    else:
        raise RuntimeError("word-span closure did not stabilize")
    assert basis.rows == basis.cols == len(coords)
    inverse = basis.inv()
    assert integral(inverse * unit)
    for name, generator in gens:
        assert integral(inverse * generator), name
    for name, action in actions:
        assert integral(inverse * action * basis), name

    index = abs(int(basis.det()))
    result = {
        "n": n,
        "normalization": "unit_lowering" if normalized else "sl2_lowering",
        "ambient_rank": len(coords),
        "index": index,
        "factorization": {str(p): int(e) for p, e in sp.factorint(index).items()},
        "closure_history": history,
        "coordinates_i_row_col": coords,
        "hnf_basis_columns": [[int(v) for v in row] for row in basis.tolist()],
        "checks": {
            "contains_unit_and_all_generators": True,
            "stable_under_right_multiplication_by_each_generator": True,
            "all_arithmetic_exact": True,
        },
    }
    print(f"n={n}, {result['normalization']}: rank={len(coords)}, index={index}, factors={result['factorization']}, iterations={len(history)}")
    return result


if __name__ == "__main__":
    results = [calculate(n, normalized) for n in (1, 2, 3) for normalized in (False, True)]
    expected = {1: 1, 2: 32, 3: 2**13 * 3**10}
    for result in results:
        assert result["index"] == (1 if result["normalization"] == "unit_lowering" else expected[result["n"]])
    (OUT / "normalized_order_indices_certificate.json").write_text(json.dumps(results, indent=2) + "\n")
    with (OUT / "normalized_order_indices.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["n", "normalization", "ambient_rank", "index", "prime_factorization", "closure_iterations"])
        for result in results:
            writer.writerow([result["n"], result["normalization"], result["ambient_rank"], result["index"],
                             "*".join(f"{p}^{e}" for p, e in result["factorization"].items()) or "1",
                             len(result["closure_history"])])
    with (OUT / "normalized_order_hnf_basis.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["n", "normalization", "basis_vector", "factor_i", "matrix_row", "matrix_column", "coefficient"])
        for result in results:
            for position, (i, r, c) in enumerate(result["coordinates_i_row_col"]):
                for basis_vector, coefficient in enumerate(result["hnf_basis_columns"][position]):
                    if coefficient:
                        writer.writerow([result["n"], result["normalization"], basis_vector, i, r, c, coefficient])
