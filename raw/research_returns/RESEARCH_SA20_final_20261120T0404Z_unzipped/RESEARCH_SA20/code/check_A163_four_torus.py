#!/usr/bin/env python3
"""Exact finite T4 certificate for A.163; no surgery or isotopy decision.

We triangulate the product of four oriented triangular circles by the
staircase triangulation of each product of four edges. We retain every
vertex and maximal simplex, check the oriented fundamental cycle and
the integer boundary-square identities, and compute F2 boundary ranks.
The separate product argument identifies the PL manifold as T4.
"""
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import time

started = time.perf_counter()
root = Path(__file__).resolve().parents[1]
checks = Counter()


def check(name, truth):
    checks[name] += 1
    if not truth:
        raise AssertionError(name)


def sign_of_order(seq):
    return -1 if sum(a > b for i, a in enumerate(seq) for b in seq[i+1:]) % 2 else 1


grid_vertices = list(product(range(3), repeat=4))
vertex_index = {v: i for i, v in enumerate(grid_vertices)}
circle_coordinates = ((0, 0), (1, 0), (0, 1))
coordinates = [sum((circle_coordinates[a] for a in v), ()) for v in grid_vertices]
facets = {}
for origin in grid_vertices:
    for axes in permutations(range(4)):
        vertex = list(origin)
        ordered = [vertex_index[tuple(vertex)]]
        for axis in axes:
            vertex[axis] = (vertex[axis] + 1) % 3
            ordered.append(vertex_index[tuple(vertex)])
        facet = tuple(sorted(ordered))
        check('distinct_vertices_per_facet', len(set(facet)) == 5)
        check('unique_maximal_simplex', facet not in facets)
        facets[facet] = sign_of_order(axes) * sign_of_order(ordered)

simplices = [set() for _ in range(5)]
for facet in facets:
    for size in range(1, 6):
        simplices[size-1].update(combinations(facet, size))
simplices = [sorted(faces) for faces in simplices]
indices = [{face: i for i, face in enumerate(faces)} for faces in simplices]
f_vector = [len(faces) for faces in simplices]
check('f_vector', f_vector == [81, 1215, 4050, 4860, 1944])
check('euler_characteristic', sum((-1)**i * n for i, n in enumerate(f_vector)) == 0)

integer_boundaries = [[]]
binary_columns = [[]]
for degree in range(1, 5):
    boundaries = []
    columns = []
    for face in simplices[degree]:
        boundary = {}
        column = 0
        for deleted in range(len(face)):
            lower = face[:deleted] + face[deleted+1:]
            row = indices[degree-1][lower]
            boundary[row] = (-1)**deleted
            column ^= 1 << row
        boundaries.append(boundary)
        columns.append(column)
    integer_boundaries.append(boundaries)
    binary_columns.append(columns)

for degree in range(2, 5):
    for boundary in integer_boundaries[degree]:
        square = Counter()
        for middle, coefficient in boundary.items():
            for lower, other in integer_boundaries[degree-1][middle].items():
                square[lower] += coefficient * other
        check('integer_boundary_square_zero', all(value == 0 for value in square.values()))

incidences = Counter()
fundamental_boundary = Counter()
for facet, orientation in facets.items():
    for deleted in range(5):
        face = facet[:deleted] + facet[deleted+1:]
        incidences[face] += 1
        fundamental_boundary[face] += orientation * (-1)**deleted
for face in simplices[3]:
    check('two_facets_per_codimension_one_face', incidences[face] == 2)
    check('oriented_fundamental_cycle', fundamental_boundary[face] == 0)


def rank_mod_two(columns):
    pivots = {}
    for value in columns:
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


ranks = [0] + [rank_mod_two(binary_columns[d]) for d in range(1, 5)] + [0]
betti = [f_vector[d] - ranks[d] - ranks[d+1] for d in range(5)]
check('mod_two_boundary_ranks', ranks[1:5] == [80, 1131, 2913, 1943])
check('mod_two_betti_numbers', betti == [1, 4, 6, 4, 1])

# The product CW structure has one vertex, four oriented loops, and the
# six coordinate-square attaching commutators. Higher cells do not alter pi1.
generators = ['a1', 'a2', 'a3', 'a4']
relations = []
for first, second in combinations(range(1, 5), 2):
    relation = [first, second, -first, -second]
    relations.append(relation)
    exponent_sums = [sum((1 if a > 0 else -1) for a in relation if abs(a) == k)
                     for k in range(1, 5)]
    check('commutator_abelianization', exponent_sums == [0, 0, 0, 0])
check('all_coordinate_square_relations', len(relations) == 6)

result = {
    'statement': 'A.163 finite standard T4 certificate only',
    'utc': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS',
    'scope': ('Exact product triangulation, integer chain identities, oriented '
              'codimension-one incidences, F2 homology, and explicit product '
              'CW pi1 presentation. The proof identifies the PL product and '
              'its universal cover; no assembly, TOP class, or isotopy '
              'comparison is inferred by this program.'),
    'vertex_grid_labels': grid_vertices,
    'vertices_in_R8': coordinates,
    'oriented_maximal_simplices': [[list(face), orientation]
                                 for face, orientation in sorted(facets.items())],
    'f_vector': f_vector,
    'mod_two_boundary_ranks_d1_through_d4': ranks[1:5],
    'mod_two_betti_numbers': betti,
    'product_CW_cell_counts': [1, 4, 6, 4, 1],
    'pi1_presentation': {'generators': generators,
                         'relators_as_signed_generator_indices': relations,
                         'interpretation': 'All pairwise commutators; hence Z^4.'},
    'checks_by_kind': dict(checks),
    'checks_passed': sum(checks.values()),
    'checks_failed': 0,
    'elapsed_seconds': time.perf_counter() - started,
    'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
target = root / 'logs/check_A163_four_torus.json'
target.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({key: result[key] for key in
                 ('status', 'f_vector', 'mod_two_boundary_ranks_d1_through_d4',
                  'mod_two_betti_numbers', 'checks_by_kind', 'checks_passed',
                  'checks_failed', 'elapsed_seconds', 'program_sha256')}, indent=2))
