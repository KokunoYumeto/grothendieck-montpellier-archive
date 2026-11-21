"""Independent check of the explicit integer witness in F-025.

This script transcribes the pencil and column set from the proof, expands all
six permanent terms, uses exact coefficient differences, and performs its own
fraction-free integer elimination. It does not import the other worker's
certificate, Jacobian, or verification code.
"""
from itertools import permutations, product
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROWS = [
    [-3, 1, 3, -3, 3, -2, 1],
    [4, 3, -4, -2, 1, -2, 0],
    [4, 0, 4, -3, 3, 2, 0],
    [3, 3, 3, -3, 2, -4, 1],
    [3, 0, -4, 3, 4, 3, 2],
    [4, 0, -1, 3, -2, 1, 0],
    [-3, 4, 2, 0, 0, -3, -3],
    [1, -4, 2, 2, 2, -1, -4],
    [4, 3, 1, 2, 1, -2, 4],
]
TARGET = sorted(a for a in product(range(4), repeat=7)
                if sum(a) == 3 and sum(a[2:]) <= 2)
COLS = list(range(40)) + list(range(41, 48)) + [49, 50]
EXPECTED = -333464241200762901244704190454683312552421068381594185434187935121408


def permanent_coefficients(rows):
    result = {}
    for perm in permutations(range(3)):
        factors = [rows[3*i + perm[i]] for i in range(3)]
        for ijk in product(range(7), repeat=3):
            coefficient = factors[0][ijk[0]] * factors[1][ijk[1]] * factors[2][ijk[2]]
            if coefficient:
                exponent = tuple(ijk.count(k) for k in range(7))
                result[exponent] = result.get(exponent, 0) + coefficient
    return result


def bareiss_determinant(matrix):
    a = [row[:] for row in matrix]
    previous, sign = 1, 1
    for k in range(len(a)-1):
        if a[k][k] == 0:
            swap = next(i for i in range(k+1, len(a)) if a[i][k])
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                numerator = pivot*a[i][j] - a[i][k]*a[k][j]
                quotient, remainder = divmod(numerator, previous)
                assert remainder == 0
                a[i][j] = quotient
        for i in range(k+1, len(a)):
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


base = permanent_coefficients(ROWS)
jacobian = [[0]*63 for _ in TARGET]
for source in range(63):
    varied = [row[:] for row in ROWS]
    varied[source//7][source%7] += 1
    coefficients = permanent_coefficients(varied)
    for row, exponent in enumerate(TARGET):
        jacobian[row][source] = coefficients.get(exponent, 0) - base.get(exponent, 0)

assert len(TARGET) == len(COLS) == 49
minor = [[row[col] for col in COLS] for row in jacobian]
determinant = bareiss_determinant(minor)
assert determinant == EXPECTED
assert determinant % 1000003 == 163652

proof = Path(__file__).parents[1] / "jet_review" / "per3_full_transverse_jets.tex"
result = {
    "date_utc": datetime.now(timezone.utc).isoformat(),
    "who_model_effort_run": "/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
    "type": "independent exact computation",
    "method": "Fresh transcription from the proof; all six products expanded as integer coefficient dictionaries; all 63 exact single-coefficient differences computed; independently implemented fraction-free Bareiss elimination on the displayed 49-column minor.",
    "source_proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
    "target_count": len(TARGET),
    "source_count": 63,
    "selected_columns": COLS,
    "integer_determinant": str(determinant),
    "modulus": 1000003,
    "residue": determinant % 1000003,
    "status": "PASS",
}
output = Path(__file__).with_name("per3_transverse_witness_independent_certificate.json")
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
