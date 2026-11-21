#!/usr/bin/env python3
"""Independent dictionary/convolution verification of the G19 cubic certificate.

No SymPy, root construction routine, or root elimination routine is imported.
The explicit pencil is entered independently from its displayed formula.
"""
from collections import defaultdict
from datetime import datetime, timezone
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parents[2]
CERT = BASE / "work/root/g19_cubic/certificate.json"
RAW = BASE / "work/root/g19_cubic/macaulay_degree6.u8"
OUT = BASE / "work/isolation/G19_cubic_independent_checks.json"
certificate = json.loads(CERT.read_text())

def add_exponents(a, b):
    return tuple(x + y for x, y in zip(a, b))

def multiply(a, b):
    result = defaultdict(int)
    for ea, ca in a.items():
        for eb, cb in b.items():
            result[add_exponents(ea, eb)] += ca * cb
    return dict(result)

units = [tuple(int(i == j) for i in range(5)) for j in range(5)]
def linear(indices):
    return {units[i]: 1 for i in indices}

# [[x1+x2,x3,x4],[x4,x0,x1],[x2+x3,x1,x0+x2]]
pencil_indices = [[[1, 2], [3], [4]], [[4], [0], [1]], [[2, 3], [1], [0, 2]]]
pencil = [[linear(a) for a in row] for row in pencil_indices]
assert certificate["pencil_coefficients_i_j_k"] == [
    [[int(k in entry) for k in range(5)] for entry in row]
    for row in pencil_indices
]

polynomial = defaultdict(int)
for sigma in permutations(range(3)):
    term = {(0, 0, 0, 0, 0): 1}
    for i in range(3):
        term = multiply(term, pencil[i][sigma[i]])
    for monomial, coefficient in term.items():
        polynomial[monomial] += coefficient
polynomial = dict(polynomial)
expected = {
    (2, 1, 0, 0, 0): 1,
    (2, 0, 1, 0, 0): 1,
    (1, 1, 1, 0, 0): 1,
    (1, 0, 2, 0, 0): 1,
    (1, 0, 1, 0, 1): 1,
    (1, 0, 0, 1, 1): 2,
    (0, 3, 0, 0, 0): 1,
    (0, 2, 1, 0, 0): 1,
    (0, 1, 1, 1, 0): 1,
    (0, 1, 0, 2, 0): 1,
    (0, 1, 0, 0, 2): 1,
    (0, 0, 1, 1, 1): 1,
}
assert polynomial == expected

gradients = []
for j in range(5):
    derivative = {}
    for a, coefficient in polynomial.items():
        if a[j]:
            b = list(a)
            b[j] -= 1
            derivative[tuple(b)] = coefficient * a[j]
    gradients.append(derivative)

# Independent Cartesian-product enumeration, not recursive compositions.
rows = sorted((a for a in product(range(7), repeat=5) if sum(a) == 6), reverse=True)
multipliers = sorted((a for a in product(range(5), repeat=5) if sum(a) == 4), reverse=True)
assert len(rows) == 210 and len(multipliers) == 70
assert rows == [tuple(a) for a in certificate["degree6_row_monomials"]]
assert multipliers == [tuple(a) for a in certificate["degree4_multiplier_monomials"]]
row_index = {a: i for i, a in enumerate(rows)}
prime = 101
matrix = [[0 for _ in range(350)] for _ in range(210)]
for j, derivative in enumerate(gradients):
    for k, multiplier in enumerate(multipliers):
        for a, coefficient in derivative.items():
            matrix[row_index[add_exponents(a, multiplier)]][70*j+k] += coefficient
matrix = [[a % prime for a in row] for row in matrix]
raw = bytes(a for row in matrix for a in row)
assert len(raw) == 73500
assert raw == RAW.read_bytes()
assert hashlib.sha256(raw).hexdigest() == certificate["matrix_sha256"]

columns = certificate["selected_columns_zero_based"]
assert len(columns) == len(set(columns)) == 210
square = [[row[j] for j in columns] for row in matrix]
determinant = 1
for col in range(210):
    pivot_row = next((i for i in range(col, 210) if square[i][col]), None)
    assert pivot_row is not None
    if pivot_row != col:
        square[col], square[pivot_row] = square[pivot_row], square[col]
        determinant = -determinant
    pivot = square[col][col]
    determinant = determinant * pivot % prime
    inverse = pow(pivot, prime-2, prime)
    for i in range(col+1, 210):
        multiplier = square[i][col] * inverse % prime
        if multiplier:
            for j in range(col+1, 210):
                square[i][j] = (square[i][j] - multiplier*square[col][j]) % prime
            square[i][col] = 0
assert determinant == certificate["selected_minor_determinant_mod101"] == 94

result = {
    "checked_utc": datetime.now(timezone.utc).isoformat(),
    "who": "GPT-6 Astra Pro; effort not exposed; agent=/root/isolation; run=CUE-GCT-20261121-I",
    "status": "PASS",
    "method": "six-permutation dictionary multiplication; integer dictionary derivatives; independent Cartesian monomials and convolution; pure-Python selected-minor elimination",
    "polynomial_term_count": len(polynomial),
    "matrix_shape": [210, 350],
    "all_matrix_bytes_rebuilt": len(raw),
    "matrix_sha256": hashlib.sha256(raw).hexdigest(),
    "certificate_sha256": hashlib.sha256(CERT.read_bytes()).hexdigest(),
    "selected_minor_determinant_mod101": determinant,
    "rank_mod101": 210,
    "conclusion": "The selected integer minor is nonzero. The five quadratic derivatives span all degree-six forms after degree-four multiplication over Q; hence their common affine zero set is the origin, so this explicit cubic hypersurface is smooth over C.",
    "scope": "One exact finite cubic example, not a general-size extrapolation or computation of the degree80 discriminant.",
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
