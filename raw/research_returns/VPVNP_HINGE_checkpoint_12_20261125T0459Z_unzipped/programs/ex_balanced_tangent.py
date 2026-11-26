#!/usr/bin/env python3
"""Exact modular Jacobian certificate for the K3,3 binary-edge image.

The input is a fixed binary point. Contractions use integer arithmetic;
the retained 155-square minor is verified modulo both2 and101.
"""
import hashlib
import itertools
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
params = json.loads((ROOT / "inputs/ex_balanced_tangent_parameters.json").read_text())
local = [np.asarray(a, dtype=np.int64) for a in params["local_maps"]]
labels = ["aijk", "blmn", "copq", "dilo", "ejmp", "fknq"]
physical = "abcdef"
coordinates = np.arange(4096).reshape((4,)*6)
jacobian = np.zeros((4096, 192), dtype=np.int64)
for site in range(6):
    expression = ",".join(labels[i] for i in range(6) if i != site)
    expression += "->" + "".join(physical[i] for i in range(6) if i != site) + labels[site][1:]
    environment = np.einsum(expression, *[local[i] for i in range(6) if i != site],
                            optimize=True).reshape(1024, 8)
    for output in range(4):
        rows = np.take(coordinates, output, axis=site).ravel()
        columns = range(site*32 + output*8, site*32 + output*8 + 8)
        jacobian[np.ix_(rows, columns)] = environment

def eliminate(matrix, prime, stop=None):
    matrix = np.asarray(matrix, dtype=np.int64).copy() % prime
    row_labels = list(range(matrix.shape[0]))
    selected_rows, selected_columns = [], []
    rank, determinant = 0, 1
    for column in range(matrix.shape[1]):
        candidates = np.flatnonzero(matrix[rank:, column])
        if not len(candidates):
            continue
        pivot = rank + int(candidates[0])
        if pivot != rank:
            matrix[[rank, pivot]] = matrix[[pivot, rank]]
            row_labels[rank], row_labels[pivot] = row_labels[pivot], row_labels[rank]
            determinant = -determinant
        value = int(matrix[rank, column])
        determinant = determinant*value % prime
        matrix[rank] = matrix[rank]*pow(value, -1, prime) % prime
        factors = matrix[rank+1:, column].copy()
        matrix[rank+1:] = (matrix[rank+1:] - factors[:, None]*matrix[rank]) % prime
        selected_rows.append(row_labels[rank])
        selected_columns.append(column)
        rank += 1
        if rank == matrix.shape[0] or rank == stop:
            break
    return rank, determinant % prime, selected_rows, selected_columns

rank2, _, rows, columns = eliminate(jacobian, 2)
rank101, _, _, _ = eliminate(jacobian, 101)
assert rank2 == rank101 == 160
rows, columns = rows[:155], columns[:155]
minor = jacobian[np.ix_(rows, columns)]
minor_checks = {}
for prime in (2, 101):
    rank, determinant, _, _ = eliminate(minor, prime)
    assert rank == 155 and determinant != 0
    minor_checks[str(prime)] = {"rank": rank, "determinant": determinant}

site_rank_checks = {}
for prime in (2, 101):
    single_ranks = []
    omitted_ranks = []
    for site in range(6):
        columns_site = list(range(site*32, (site+1)*32))
        columns_other = [i for i in range(192) if i not in columns_site]
        single_ranks.append(eliminate(jacobian[:, columns_site], prime)[0])
        omitted_ranks.append(eliminate(jacobian[:, columns_other], prime)[0])
    assert single_ranks == [32]*6 and omitted_ranks == [138]*6
    site_rank_checks[str(prime)] = {"single_site_ranks": single_ranks,
                                   "five_site_ranks": omitted_ranks,
                                   "isolated_quotient_ranks": [160-x for x in omitted_ranks]}

# A separate finite combinatorial count of the common orbit tangent.
# Each triangle edge has a fixed-vector line and a 3-dimensional complement.
edges = [(0, 1), (0, 2), (1, 2)]
subsets = []
for mask in range(8):
    selected = [edges[i] for i in range(3) if mask >> i & 1]
    availability = set(range(3))
    for edge in selected:
        availability &= set(edge)
    subsets.append((mask, availability, 3**len(selected)))
intersection_dimension = 0
surviving_components = []
for left, right in itertools.product(subsets, repeat=2):
    mask1, avail1, dim1 = left
    mask2, avail2, dim2 = right
    survives = all({permutation[i] for i in avail1} & avail2
                   for permutation in itertools.permutations(range(3)))
    assert survives == (len(avail1) + len(avail2) > 3)
    if survives:
        intersection_dimension += dim1*dim2
        surviving_components.append([mask1, mask2, dim1*dim2])
assert intersection_dimension == 154

result = {
    "jacobian_shape": [4096, 192],
    "jacobian_integer_min_max": [int(jacobian.min()), int(jacobian.max())],
    "jacobian_sha256_little_endian_int64": hashlib.sha256(jacobian.astype('<i8').tobytes()).hexdigest(),
    "full_jacobian_rank_mod2": rank2,
    "full_jacobian_rank_mod101": rank101,
    "minor_rows": rows,
    "minor_columns": columns,
    "minor_integer_entries": minor.tolist(),
    "minor_checks": minor_checks,
    "site_rank_checks": site_rank_checks,
    "matching_tangent_intersection_dimension": intersection_dimension,
    "surviving_tangent_components": surviving_components,
    "conclusion": "Image dimension at least155 in characteristic0 and2, exceeding the154-dimensional tangent intersection at the two-triangle target."
}
(ROOT / "outputs/ex_balanced_tangent_results.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({key: result[key] for key in (
    "full_jacobian_rank_mod2", "full_jacobian_rank_mod101", "minor_checks",
    "matching_tangent_intersection_dimension", "jacobian_integer_min_max",
    "site_rank_checks")}))
