#!/usr/bin/env python3
"""Exact bounded exterior-algebra certificate for the five-point Kummer test.

All calculations are over Z, followed by explicit Gaussian elimination over F2.
Geometry and the support-localization argument are proved in the research note;
this program checks the entire degree-four vectors and the indicated ranks.
"""
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from math import gcd
from functools import reduce
import hashlib
import json
import time


def add(*polys):
    out = {}
    for poly in polys:
        for mask, coefficient in poly.items():
            out[mask] = out.get(mask, 0) + coefficient
    return {mask: coefficient for mask, coefficient in out.items() if coefficient}


def scale(coefficient, poly):
    return {mask: coefficient * value for mask, value in poly.items()
            if coefficient * value}


def multiply(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            if a & b:
                continue
            inversions = sum((b & ((1 << i) - 1)).bit_count()
                             for i in range(a.bit_length()) if (a >> i) & 1)
            mask = a | b
            out[mask] = out.get(mask, 0) + (-1 if inversions % 2 else 1) * ca * cb
    return {mask: coefficient for mask, coefficient in out.items() if coefficient}


def generator(site, alpha):
    return {1 << (4 * site + alpha): 1}


def linear(row, alpha):
    return add(*(scale(value, generator(site, alpha))
                 for site, value in enumerate(row)))


def incidence(number_of_sites, alpha, beta):
    row = [1] * number_of_sites
    return add(*(multiply(generator(site, alpha), generator(site, beta))
                 for site in range(number_of_sites)),
               multiply(linear(row, alpha), linear(row, beta)))


def casimir(number_of_sites):
    mu = lambda a, b: incidence(number_of_sites, a, b)
    return add(multiply(mu(0, 1), mu(2, 3)),
               multiply(mu(0, 2), mu(3, 1)),
               multiply(mu(0, 3), mu(1, 2)))


def collision_class(row):
    result = {0: 1}
    for alpha in range(4):
        result = multiply(result, linear(row, alpha))
    return result


def mod_two_rank(polys, basis):
    pivots = {}
    for poly in polys:
        vector = sum((poly.get(mask, 0) % 2) << i
                     for i, mask in enumerate(basis))
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = vector
                break
            vector ^= pivots[pivot]
    return len(pivots)


def sparse_output(poly):
    return [
        {"generators": [f"x{j // 4 + 1}{j % 4 + 1}"
                         for j in range(16) if (mask >> j) & 1],
         "coefficient": coefficient}
        for mask, coefficient in sorted(poly.items())
    ]


started_utc = datetime.now(timezone.utc).isoformat()
started = time.perf_counter()
basis = [sum(1 << j for j in indices) for indices in combinations(range(16), 4)]
assert len(basis) == 1820
q = casimir(4)
detector = sum(1 << j for j in (0, 5, 10, 15))
assert q[detector] == 3

rows = []
for i, j in combinations(range(4), 2):
    row = [0] * 4
    row[i], row[j] = 1, -1
    rows.append((f"D{i + 1}{j + 1}", row))
for i in range(4):
    row = [1] * 4
    row[i] = 2
    rows.append((f"D{i + 1}5", row))

classes = [collision_class(row) for _, row in rows]
detected = [poly.get(detector, 0) for poly in classes]
assert detected == [0] * 6 + [2] * 4
assert all(reduce(gcd, row) == 1 for _, row in rows)
pair_minor_gcds = []
for (name_a, a), (name_b, b) in combinations(rows, 2):
    minors = [a[i] * b[j] - a[j] * b[i]
              for i, j in combinations(range(4), 2)]
    value = reduce(gcd, minors)
    assert value == 1
    pair_minor_gcds.append({"pair": [name_a, name_b], "minor_gcd": value})

rank = mod_two_rank(classes, basis)
augmented_rank = mod_two_rank(classes + [q], basis)
assert rank == 10
assert augmented_rank == 11

# A normalization control: for three points, the same ordered pullback has
# all coefficients divisible by six. This is not a geometric saturation proof.
q_three = casimir(2)
q_three_content = reduce(gcd, q_three.values())
assert q_three_content == 6
assert reduce(gcd, q.values()) == 1

elapsed = time.perf_counter() - started
result = {
    "started_utc": started_utc,
    "finished_utc": datetime.now(timezone.utc).isoformat(),
    "seconds": elapsed,
    "arithmetic": "exact integer exterior algebra, then Gaussian elimination over F2",
    "ambient_generator_count": 16,
    "complete_degree_four_basis_dimension": len(basis),
    "detector_monomial": ["x11", "x22", "x33", "x44"],
    "casimir_detector_value": q[detector],
    "collision_detector_values": dict(zip((name for name, _ in rows), detected)),
    "collision_rank_mod_two": rank,
    "augmented_rank_mod_two": augmented_rank,
    "five_point_casimir_content": 1,
    "three_point_control_content": q_three_content,
    "all_45_pairwise_minor_gcds": pair_minor_gcds,
    "collision_rows": dict(rows),
    "complete_casimir_sparse_vector": sparse_output(q),
    "complete_collision_sparse_vectors": {
        name: sparse_output(poly) for (name, _), poly in zip(rows, classes)
    },
    "geometric_claims_not_checked_by_program": [
        "the ordered collision complement covers the distinct-support Kummer locus",
        "support duality and the integral localization exact sequence",
        "the absence of 2-torsion follows from the proved support geometry and verified rank",
        "no integral Hodge or algebraic surface with odd scalar is constructed"
    ]
}
output_directory = Path(__file__).resolve().parents[1] / "output"
output_directory.mkdir(parents=True, exist_ok=True)
full_path = output_directory / "kummer_five_point_detector.json"
full_path.write_text(json.dumps(result, indent=2) + "\n")
summary = {key: value for key, value in result.items()
           if key not in {"complete_casimir_sparse_vector", "complete_collision_sparse_vectors",
                          "all_45_pairwise_minor_gcds"}}
summary["full_certificate_sha256"] = hashlib.sha256(full_path.read_bytes()).hexdigest()
summary["all_45_pairwise_minor_gcds_equal_one"] = True
summary["result"] = "PASS"
summary_text = json.dumps(summary, indent=2) + "\n"
(output_directory / "kummer_five_point_detector.out").write_text(summary_text)
print(summary_text, end="")
