#!/usr/bin/env python3
"""Independently certify a nonzero maximal minor of the C.3ae matrix."""
from pathlib import Path
from itertools import product
import hashlib
import json
import time
import sympy as sp
from sympy.polys.matrices import DomainMatrix

started = time.perf_counter()
root = Path(__file__).resolve().parents[1]
source = root / "agents/cycles/output/test_quartic_obstruction_rank.json"
record = json.loads(source.read_text())
coefficients = record["trials"][0]["coefficients_i_j_k"]
basis3 = sorted(e for e in product(range(3), repeat=4) if sum(e) == 3)
basis4 = sorted(e for e in product(range(3), repeat=4) if sum(e) == 4)
index4 = {e: n for n, e in enumerate(basis4)}
matrix = sp.zeros(4 * len(basis3), 3 * len(basis4))
for section, coeff in enumerate(coefficients):
    for row, monomial in enumerate(basis3):
        for variable in range(4):
            target = list(monomial)
            target[variable] += 1
            if max(target) > 2:
                continue
            column = index4[tuple(target)]
            for curve_coordinate in range(3):
                matrix[section * 16 + row, curve_coordinate * 19 + column] += coeff[variable][curve_coordinate]
field_matrix = DomainMatrix.from_Matrix(matrix).convert_to(sp.GF(101))
_, independent_rows = field_matrix.transpose().rref()
assert len(independent_rows) == 57
minor = matrix.extract(list(independent_rows), list(range(57)))
determinant = int(DomainMatrix.from_Matrix(minor).convert_to(sp.GF(101)).det()) % 101
assert determinant != 0
result = {
    "statement": "C.3ae candidate; only its finite obstruction matrix is certified here",
    "matrix_shape": list(matrix.shape),
    "coefficient_input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "independent_row_indices_zero_based": list(independent_rows),
    "minor_determinant_mod_101": determinant,
    "rank_over_Q": 57,
    "independent_method": "SymPy DomainMatrix finite-field row reduction on the transpose, followed by a square determinant",
    "runtime_seconds": time.perf_counter() - started,
    "scope": "A nonzero integer maximal minor modulo101 proves full column rank over Q and C; geometry and actual cycle-family arguments require separate proofs."
}
output = root / "code/check_quartic_obstruction_independent_output.json"
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
