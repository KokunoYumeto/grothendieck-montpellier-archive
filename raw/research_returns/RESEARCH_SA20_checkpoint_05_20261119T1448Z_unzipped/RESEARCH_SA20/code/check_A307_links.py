#!/usr/bin/env python3
"""Exact integral graph-link certificate for the three-page-book example.

Each of q pages contributes a two-edge path between the two axis directions.
Connected graphs have torsion-free first integral homology; Gaussian rank is
computed over Q and a spanning tree is explicitly exhibited.
"""
from fractions import Fraction
import json
import time


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    pivot = 0
    for col in range(len(a[0]) if a else 0):
        row = next((r for r in range(pivot, len(a)) if a[r][col]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        d = a[pivot][col]
        a[pivot] = [x / d for x in a[pivot]]
        for r in range(len(a)):
            if r != pivot and a[r][col]:
                d = a[r][col]
                a[r] = [x - d*y for x, y in zip(a[r], a[pivot])]
        pivot += 1
    return pivot


def certificate(pages):
    vertices = ['u', 'v'] + [f'w{i}' for i in range(pages)]
    edges = [(0, i+2) for i in range(pages)]
    edges += [(i+2, 1) for i in range(pages)]
    boundary = [[(1 if v == b else -1 if v == a else 0)
                 for a, b in edges] for v in range(len(vertices))]
    boundary_rank = rank(boundary)
    tree = edges[:pages] + [edges[pages]]
    reached = {0}
    while True:
        enlarged = reached | {b for a, b in tree if a in reached}
        enlarged |= {a for a, b in tree if b in reached}
        if enlarged == reached:
            break
        reached = enlarged
    assert len(tree) == len(vertices)-1 and len(reached) == len(vertices)
    assert boundary_rank == len(vertices)-1
    h1_rank = len(edges)-boundary_rank
    assert h1_rank == pages-1
    return dict(pages=pages, vertices=vertices, edges=edges,
                boundary_matrix=boundary, boundary_rank=boundary_rank,
                spanning_tree=tree, H1_free_rank=h1_rank,
                H2_local_free_rank=h1_rank)


if __name__ == '__main__':
    start = time.perf_counter()
    records = [certificate(q) for q in (1, 2, 3)]
    print(json.dumps(dict(statement='A.307', records=records,
                         cases=len(records), passed=True,
                         seconds=time.perf_counter()-start), indent=2))
