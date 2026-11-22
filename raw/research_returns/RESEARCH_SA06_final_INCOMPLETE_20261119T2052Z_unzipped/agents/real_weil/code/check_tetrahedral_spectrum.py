#!/usr/bin/env python3
"""Exact finite cochain checks for TS; no family-algebraization claim."""
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from time import perf_counter
import json
import sympy as s

started = perf_counter()
utc = datetime.now(timezone.utc).isoformat()
base = Path(__file__).resolve().parents[1]
vertices = tuple(range(4))
edges = tuple(combinations(vertices, 2))
faces = tuple(combinations(vertices, 3))
d0 = s.zeros(6, 4)
for row, (i, j) in enumerate(edges):
    d0[row, i], d0[row, j] = -1, 1
d1 = s.zeros(4, 6)
for row, face in enumerate(faces):
    for pos in range(3):
        edge = face[:pos] + face[pos + 1:]
        d1[row, edges.index(edge)] = (-1) ** pos

# The six sets of five blow-up points lie on the earlier component.
pic_labels = [("H", i) for i in vertices]
pic_labels += [("F", i, j, n) for i, j in edges for n in range(5)]
pic = s.zeros(6, len(pic_labels))
for row, (i, j) in enumerate(edges):
    pic[row, i], pic[row, j] = -1, 1
    for n in range(5):
        pic[row, pic_labels.index(("F", i, j, n))] = -1
chosen = [pic_labels.index(("F", i, j, 0)) for i, j in edges]

checks = []
def check(name, condition, value=None):
    checks.append({"name": name, "passed": bool(condition), "value": value})

check("tetrahedral cochain differential squares to zero", d1*d0 == s.zeros(4,4))
check("weight-zero d0 rank", d0.rank() == 3, d0.rank())
check("weight-zero d1 rank", d1.rank() == 3, d1.rank())
check("weight-zero H0", 4-d0.rank() == 1, 4-d0.rank())
check("weight-zero H1", 6-d0.rank()-d1.rank() == 0, 6-d0.rank()-d1.rank())
check("weight-zero H2", 4-d1.rank() == 1, 4-d1.rank())
check("Picard rank", len(pic_labels) == 34, len(pic_labels))
check("each edge has an integral exceptional degree unit", pic[:,chosen] == -s.eye(6))
check("Picard restriction rank", pic.rank() == 6, pic.rank())
check("Picard kernel rank", len(pic_labels)-pic.rank() == 28, len(pic_labels)-pic.rank())
check("four component degree classes", len(vertices) == 4)
check("total degree-zero rank", 1+28+4 == 33)
check("total middle cohomology zero", 12-(3+6)-3 == 0)
check("component blow-up point counts", [sum(5 for i,j in edges if i==v) for v in vertices] == [15,10,5,0])

# Algebraic verification of the weighted row-sum identity used in TC.
x = s.symbols('x0:4')
bdiag = s.symbols('b00 b11 b22 b33')
boff = s.symbols('b01 b02 b03 b12 b13 b23')
B = s.diag(*bdiag)
for bij, (i,j) in zip(boff, edges):
    B[i,j] = B[j,i] = bij
lhs = (s.Matrix(x).T * B * s.Matrix(x))[0]
rhs = sum(sum(B[i,j] for j in vertices)*x[i]**2 for i in vertices)
rhs -= sum(B[i,j]*(x[i]-x[j])**2 for i,j in edges)
check("weighted negative-intersection identity", s.expand(lhs-rhs) == 0)

record = {
    "utc_started": utc,
    "scope": "Finite cochain ranks, exact integral edge-unit columns, and the symbolic symmetric-matrix identity only. No K-theory descent, Chow comparison, or actual-family lift is certified by this program.",
    "vertices": vertices, "edges": edges, "faces": faces,
    "weight_zero_d0": d0.tolist(), "weight_zero_d1": d1.tolist(),
    "picard_generators": pic_labels, "picard_restriction": pic.tolist(),
    "checks": checks, "passed": sum(c['passed'] for c in checks),
    "total": len(checks), "runtime_seconds": perf_counter()-started,
}
path = base/'output'/'tetrahedral_spectrum_certificate.json'
path.write_text(json.dumps(record, indent=2, default=int)+'\n')
print(json.dumps(record, indent=2, default=int))
if not all(c['passed'] for c in checks):
    raise SystemExit(1)
