#!/usr/bin/env python3
"""Exact finite base certificate for the A.140 S^2 x S^2 example.

We triangulate the product of two tetrahedron boundaries by ordered
staircases. The general staircase-product proof identifies its PL type.
This program checks the complete finite face data, boundary-square-zero,
mod-two Betti numbers and the homology of every nonmaximal simplex link.
It does not purport to compute a homeomorphism-space homotopy group.
"""
from itertools import combinations
from time import perf_counter
import json

started = perf_counter()
checks = []


def check(name, condition):
    assert condition, name
    checks.append(name)


def face_sets(facets):
    top = max(len(s) for s in facets)-1
    return [sorted({tuple(t) for s in facets for t in combinations(s,d+1)})
            for d in range(top+1)]


def boundaries(faces):
    columns = [[]]
    for d in range(1,len(faces)):
        rows = {s:i for i,s in enumerate(faces[d-1])}
        columns.append([sum(1 << rows[t] for t in combinations(s,d))
                        for s in faces[d]])
    return columns


def binary_rank(columns):
    pivots = {}
    for value in columns:
        while value:
            pivot = value.bit_length()-1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def betti(faces):
    cols = boundaries(faces)
    ranks = [0]+[binary_rank(c) for c in cols[1:]]+[0]
    return [len(faces[d])-ranks[d]-ranks[d+1]
            for d in range(len(faces))]


tetra_facets = list(combinations(range(4),3))
tetra_faces = face_sets(tetra_facets)
check('tetrahedron boundary face vector',list(map(len,tetra_faces))==[4,6,4])
check('tetrahedron boundary mod-two Betti numbers',betti(tetra_faces)==[1,0,1])

# Each pair of ordered 2-simplices has the six monotone (2,2)-paths.
# Vertex (i,j) is encoded as 4*i+j; the finite base has sixteen vertices.
facets = set()
for a in tetra_facets:
    for b in tetra_facets:
        pair_facets = set()
        for horizontal in combinations(range(4),2):
            h = set(horizontal)
            i = j = 0
            path = [4*a[i]+b[j]]
            for step in range(4):
                if step in h:
                    i += 1
                else:
                    j += 1
                path.append(4*a[i]+b[j])
            check(f'staircase {a},{b},{horizontal}: distinct vertices',len(set(path))==5)
            pair_facets.add(tuple(sorted(path)))
        check(f'product cell {a},{b}: six staircases',len(pair_facets)==6)
        facets.update(pair_facets)
facets = sorted(facets)
faces = face_sets(facets)
fvector = list(map(len,faces))
check('product face vector',fvector==[16,84,216,240,96])
check('Euler characteristic four',sum((-1)**d*n for d,n in enumerate(fvector))==4)
check('product mod-two Betti numbers',betti(faces)==[1,0,2,0,1])

cols = boundaries(faces)
for d in range(2,len(faces)):
    for k,column in enumerate(cols[d]):
        product = 0
        bits = column
        while bits:
            low = bits & -bits
            product ^= cols[d-1][low.bit_length()-1]
            bits ^= low
        check(f'boundary squared at dimension {d}, simplex {k}',product==0)

facet_sets = [frozenset(s) for s in facets]
for codim_one in faces[3]:
    sigma = frozenset(codim_one)
    check(f'closed pseudomanifold incidence {codim_one}',
          sum(sigma<=f for f in facet_sets)==2)

link_counts = {}
for d in range(4):
    for simplex in faces[d]:
        sigma = frozenset(simplex)
        link_facets = sorted({tuple(sorted(f-sigma)) for f in facet_sets if sigma<=f})
        lf = face_sets(link_facets)
        ld = 3-d
        expected = [0]*(ld+1)
        expected[0] = 1
        expected[ld] += 1
        check(f'homology sphere link {simplex}',betti(lf)==expected)
    link_counts[str(d)] = len(faces[d])

result = {
    'status':'PASS','checks':len(checks),'failures':0,
    'elapsed_seconds':perf_counter()-started,
    'base':'ordered staircase triangulation of boundary(Delta3) x boundary(Delta3)',
    'vertex_encoding':'(i,j) maps to 4*i+j for 0<=i,j<=3',
    'face_vector':fvector,'betti_mod2':betti(faces),
    'all_facets':facets,'nonmaximal_link_checks_by_simplex_dimension':link_counts,
    'mathematical_scope':'Finite base-complex certificate only. The product triangulation proof establishes PL S2 x S2 and simple connectivity; A140 supplies the infinite homeomorphism-space obstruction theorem.'
}
print(json.dumps(result,indent=2))
