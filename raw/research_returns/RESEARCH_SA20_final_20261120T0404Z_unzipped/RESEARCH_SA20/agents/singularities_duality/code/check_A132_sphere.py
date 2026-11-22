#!/usr/bin/env python3
"""Exact finite-base certificate for A.132.

Checks the boundary of the abstract 4-simplex, including every link,
integral chain matrices, primitive boundary images, and a fundamental
cycle. This certifies the finite PL S^3 used in the counterexample.
It does not construct a TOP family or test the cited TOP(4)/O(4) theorem.
"""
from itertools import combinations
import json
import time

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def main():
    started = time.perf_counter()
    tests = []

    def check(name, value):
        if not value:
            raise AssertionError(name)
        tests.append(name)

    vertices = tuple(range(5))
    faces = {tuple(c) for r in range(5) for c in combinations(vertices, r)}
    by_dim = {k: sorted(f for f in faces if len(f) == k + 1) for k in range(4)}
    check("f-vector", [len(by_dim[k]) for k in range(4)] == [5, 10, 10, 5])
    check("Euler characteristic", sum((-1)**k * len(by_dim[k]) for k in range(4)) == 0)
    for face in sorted(faces - {()}):
        link = {f for f in faces if not set(f).intersection(face)
                and tuple(sorted(f + face)) in faces}
        complement = tuple(v for v in vertices if v not in face)
        expected = {tuple(c) for r in range(len(complement))
                    for c in combinations(complement, r)}
        check("link of " + repr(face), link == expected)

    boundaries = {}
    for degree in range(1, 4):
        rows = by_dim[degree - 1]
        columns = by_dim[degree]
        matrix = sp.zeros(len(rows), len(columns))
        positions = {face: i for i, face in enumerate(rows)}
        for j, simplex in enumerate(columns):
            for i in range(len(simplex)):
                matrix[positions[simplex[:i] + simplex[i+1:]], j] = (-1)**i
        boundaries[degree] = matrix
        smith = smith_normal_form(matrix, domain=ZZ)
        nonzero = [abs(int(smith[i, i])) for i in range(min(smith.shape))
                   if smith[i, i] != 0]
        check(f"primitive integral image of d{degree}", all(x == 1 for x in nonzero))
        check(f"rank of d{degree}", len(nonzero) == {1: 4, 2: 6, 3: 4}[degree])
    for degree in (2, 3):
        check(f"d{degree-1} d{degree}=0",
              boundaries[degree-1] * boundaries[degree] ==
              sp.zeros(len(by_dim[degree-2]), len(by_dim[degree])))
    ranks = {0: 0, 4: 0, **{k: int(v.rank()) for k, v in boundaries.items()}}
    betti = [len(by_dim[k]) - ranks[k] - ranks[k+1] for k in range(4)]
    # Primitive images in the whole chain group remain primitive in its
    # cycle subgroup, so these rank computations determine integral homology.
    check("integral homology ranks", betti == [1, 0, 0, 1])
    oriented_facets = sp.Matrix([(-1)**next(v for v in vertices if v not in f)
                                 for f in by_dim[3]])
    check("oriented fundamental cycle", boundaries[3] * oriented_facets == sp.zeros(10, 1))
    check("primitive fundamental cycle", sp.gcd_list(list(oriented_facets)) == 1)
    for triangle in by_dim[2]:
        containing = [f for f in by_dim[3] if set(triangle).issubset(f)]
        check("two facets around " + repr(triangle), len(containing) == 2)

    result = {
        "statement_id": "A.132",
        "scope": "Finite boundary-of-4-simplex certificate only; no numerical TOP-family claim",
        "checks": len(tests),
        "outcome": "PASS",
        "f_vector": [5, 10, 10, 5],
        "integral_homology": ["Z", "0", "0", "Z"],
        "runtime_seconds": time.perf_counter() - started,
        "tests": tests,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
