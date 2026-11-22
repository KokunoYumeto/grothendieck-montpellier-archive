"""Exact supporting GF(2) checks for the three-by-b strip proof.

The geometric, infinite-b and group-theoretic assertions are proved in TeX.
This program checks graph quotients, component spans and body projections
in a finite range, plus the universal three-fibre label coinvariants.
"""
from itertools import combinations
from pathlib import Path
from time import perf_counter
import json


def rank(vectors):
    pivots = {}
    for value in vectors:
        while value:
            i = value.bit_length() - 1
            if i in pivots:
                value ^= pivots[i]
            else:
                pivots[i] = value
                break
    return len(pivots)


def quotient_rank(vectors, relations):
    return rank(list(relations) + list(vectors)) - rank(relations)


def body_map(value, b):
    a = sum((value >> j) & 1 for j in range(3)) % 2
    return sum((((value >> j) & 1) ^ a) << (j - 3)
               for j in range(3, b))


started = perf_counter()
rows = []
for b in range(4, 33):
    m = b - 3
    edge = lambda i, j: 1 << (i * b + j)
    cuts = [sum(edge(i, j) for j in range(b)) for i in range(3)]
    cuts += [sum(edge(i, j) for i in range(3)) for j in range(b)]
    assert rank(cuts) == b + 2
    graph_dimension = 3 * b - rank(cuts)
    assert graph_dimension == 2 * b - 2
    columns = [edge(i, j) for j in range(b) for i in range(2)]
    assert quotient_rank(columns, cuts) == graph_dimension
    for j in range(b):
        assert quotient_rank([edge(0, j), edge(1, j)], cuts) == 2

    # All pair vectors occur in some triple; these generate the sum-zero space.
    pairs = [(1 << i) ^ (1 << j) for i, j in combinations(range(b), 2)]
    assert rank(pairs) == b - 1
    diagonal = (1 << b) - 1
    component_span = quotient_rank(pairs, [diagonal])
    assert component_span == b - 1 - (b % 2 == 0)
    for i, j in combinations(range(b), 2):
        third = next(x for x in range(b) if x not in (i, j))
        triple = {i, j, third}
        assert len(triple) == 3
        assert ((1 << i) ^ (1 << j)).bit_count() == 2

    body_span = rank([body_map(v, b) for v in pairs])
    expected_body = m if b % 2 else m - 1
    assert body_span == expected_body
    if b % 2 == 0:
        assert all(body_map(v, b).bit_count() % 2 == 0 for v in pairs)
    assert body_map(diagonal, b) == 0
    generic = 3 * b - 1
    special = graph_dimension + b - 1
    assert special == generic - 2
    recovered = 2 * m + 8 + body_span
    assert recovered == generic - (b % 2 == 0)
    rows.append(dict(b=b, graph=graph_dimension, grid_relative=special,
                     component_span=component_span, body_span=body_span,
                     recovered=recovered))

# The sum-zero subspace of F2^3 has no S3 coinvariants.
heart = [0b011, 0b101]
def permute(v, permutation):
    return sum(((v >> i) & 1) << permutation[i] for i in range(3))
differences = []
for permutation in ((1, 0, 2), (0, 2, 1)):
    differences += [v ^ permute(v, permutation) for v in heart]
assert rank(differences) == 2

result = dict(status="PASS", scope="finite graph and body-projection supplement; not a geometric proof",
              b_range=[4, 32], rows=rows, triple_label_coinvariant_dimension=0,
              runtime_seconds=perf_counter()-started)
destination = Path(__file__).resolve().parents[1] / "outputs" / "mixed_strip_grid_checks.json"
destination.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
