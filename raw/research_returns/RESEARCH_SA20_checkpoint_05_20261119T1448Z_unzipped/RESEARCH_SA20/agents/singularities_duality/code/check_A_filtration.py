#!/usr/bin/env python3
"""Exact finite checks for A.204; analytical arguments remain in the proof."""
import json
from fractions import Fraction
from pathlib import Path


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    row = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(row, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        factor = a[row][col]
        a[row] = [x / factor for x in a[row]]
        for j in range(len(a)):
            if j != row:
                factor = a[j][col]
                a[j] = [u - factor * v for u, v in zip(a[j], a[row])]
        row += 1
        if row == len(a):
            break
    return row


vertices = ['P0', 'P1', 'P2', 'Q0', 'Q1', 'Q2']
edges = [('P0', 'Q0'), ('P0', 'Q1'), ('P1', 'Q1'),
         ('P2', 'Q1'), ('P2', 'Q2')]
parent = {v: v for v in vertices}


def root(v):
    if parent[v] != v:
        parent[v] = root(parent[v])
    return parent[v]


for a, b in edges:
    parent[root(a)] = root(b)
components = sorted({root(v) for v in vertices})
assert len(components) == 1

link_boundary = [[-1] * 4, [1] * 4]
link_rank = rank(link_boundary)
link_betti1 = 4 - link_rank
assert link_rank == 1
assert link_betti1 == 3
assert 2 - link_rank == 1  # connected link

# A two-vertex, two-edge cell decomposition of the ordinary circle.
circle_boundary = [[-1, -1], [1, 1]]
circle_betti1 = 2 - rank(circle_boundary)
assert circle_betti1 == 1
assert link_betti1 != circle_betti1

result = {
    'statement': 'A.204',
    'partition_incidence_vertices': vertices,
    'partition_incidence_edges': edges,
    'join_atoms': len(components),
    'local_link_vertices': 2,
    'local_link_edges': 4,
    'local_link_boundary_rank_over_Q': link_rank,
    'local_link_first_betti': link_betti1,
    'manifold_circle_first_betti': circle_betti1,
    'assertions_passed': 6,
    'scope': 'Partition join and finite link homology; no numerical claim about regularity.'
}
out = Path(__file__).resolve().parents[1] / 'logs' / 'check_A_filtration_output.json'
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
