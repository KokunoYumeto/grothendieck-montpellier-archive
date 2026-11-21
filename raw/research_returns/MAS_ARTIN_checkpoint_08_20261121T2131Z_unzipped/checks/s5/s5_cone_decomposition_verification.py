"""Exact integer verification of the reduced S5 Hecke cone.

The input character enumeration is separately audited in
s5_hecke_cone.py.  This program uses no numerical optimization.
The nonnegativity of coordinates c and d is an additional
holomorphy premise for the reduced cone, not a consequence of
the 43 induced-linear tests alone.
"""
from functools import lru_cache
from pathlib import Path
import hashlib
import json

folder = Path(__file__).resolve().parent
source = folder / "s5_hecke_cone.json"
raw = source.read_bytes()
data = json.loads(raw)
patterns = [tuple(item["coefficients"])
            for item in data["induced_linear_patterns"]]
assert len(patterns) == 43 and len(set(patterns)) == 43

names = ["x+y", "b+x", "a+y", "c+x+e", "d+y+e",
         "a+c+x", "b+d+y", "a", "b", "c", "d", "e"]
basis = [
    (0, 0, 0, 0, 1, 1, 0),
    (0, 1, 0, 0, 1, 0, 0),
    (1, 0, 0, 0, 0, 1, 0),
    (0, 0, 1, 0, 1, 0, 1),
    (0, 0, 0, 1, 0, 1, 1),
    (1, 0, 1, 0, 1, 0, 0),
    (0, 1, 0, 1, 0, 1, 0),
    (1, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1),
]
assert all(row in patterns for i, row in enumerate(basis)
           if i not in (9, 10))


@lru_cache(None)
def decompose(index, remainder):
    if index == len(basis):
        return () if not any(remainder) else None
    row = basis[index]
    cap = min(remainder[j] // row[j]
              for j in range(7) if row[j])
    for count in range(cap + 1):
        reduced = tuple(remainder[j] - count * row[j]
                        for j in range(7))
        suffix = decompose(index + 1, reduced)
        if suffix is not None:
            return (count,) + suffix
    return None


certificates = []
for row in patterns:
    coefficients = decompose(0, row)
    assert coefficients is not None
    assert len(coefficients) == 12 and min(coefficients) >= 0
    reconstructed = tuple(sum(coefficients[i] * basis[i][j]
                              for i in range(12)) for j in range(7))
    assert reconstructed == row
    certificates.append({"induced_row": row,
                         "nonnegative_integer_coefficients": coefficients})

relative_order = (0, 0, 4, 4, 5, 5, 6)
total_order = (1, 1, 4, 4, 5, 5, 6)
witnesses = [
    ((0, 1, 1, 0, -1, 1, 0), 4, 5, "general W pole"),
    ((1, 0, 0, 1, 1, -1, 0), 4, 5, "general Wsign pole"),
    ((1, 1, 0, 0, -1, 1, 1), 6, 8, "W pole with c=0"),
    ((1, 1, 0, 0, 1, -1, 1), 6, 8, "Wsign pole with d=0"),
]
verified_witnesses = []
for witness, expected_q, expected_r, label in witnesses:
    pairings = [sum(a * b for a, b in zip(row, witness))
                for row in patterns]
    assert min(pairings) >= 0
    assert all(witness[j] >= 0 for j in (0, 1, 2, 3, 6))
    q = sum(a * b for a, b in zip(relative_order, witness))
    r = sum(a * b for a, b in zip(total_order, witness))
    assert q == expected_q and r == expected_r
    verified_witnesses.append({"description": label,
                               "orders": witness,
                               "all_43_pairings": pairings,
                               "relative_order": q,
                               "total_order": r})

result = {
    "coordinates": ["a", "b", "c", "d", "x", "y", "e"],
    "characters": ["1", "sign", "4", "4sign", "5", "5sign", "6"],
    "input_file": source.name,
    "input_sha256": hashlib.sha256(raw).hexdigest(),
    "additional_premise": "c>=0 and d>=0 from the specified four-dimensional holomorphy input",
    "generator_names": names,
    "generators": basis,
    "integer_decompositions": certificates,
    "sharpness_witnesses": verified_witnesses,
    "scope": "Exact finite cone computation, not a proof-assistant certificate or arithmetic realization of witnesses",
}
target = folder / "s5_cone_decomposition_verification.json"
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"verified_rows": len(certificates),
                  "generators": len(basis),
                  "relative_minimum_witness": 4,
                  "total_minimum_witness": 5,
                  "branch_c_or_d_zero_relative_witness": 6,
                  "branch_c_or_d_zero_total_witness": 8,
                  "output": str(target)}, indent=2))
