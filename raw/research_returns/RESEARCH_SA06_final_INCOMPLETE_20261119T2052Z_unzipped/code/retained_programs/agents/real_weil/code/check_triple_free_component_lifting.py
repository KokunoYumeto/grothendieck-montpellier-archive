#!/usr/bin/env python3
"""Exact finite algebra checks for C.3br; no geometric theorem is delegated here."""
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
import json
import sympy as s

started_at = datetime.now(timezone.utc).isoformat()
started = perf_counter()
base = Path(__file__).resolve().parents[1]
checks = []

def keep(name, passed, **data):
    checks.append({"name": name, "passed": bool(passed), **data})

def matrix_data(M):
    return [[str(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]

x = s.symbols('x')
surface = (x - 1) * (x - 2) / 6
threefold = -(x - 1) * (x - 2) * (x - 8) / 24
for weight in range(3):
    value = surface.subs(x, 2**weight)
    keep(f"surface weight-two projector on weight {weight}", value == int(weight == 2), value=str(value))
for weight in range(4):
    value = threefold.subs(x, 2**weight)
    keep(f"threefold weight-two projector on weight {weight}", value == int(weight == 2), value=str(value))
keep("edge polynomial removes weight one and preserves weight two",
     ((x - 2) / 2).subs(x, 2) == 0 and ((x - 2) / 2).subs(x, 4) == 1)

graphs = [
    ("single", 2, [(0, 1)]),
    ("path", 4, [(0, 1), (1, 2), (2, 3)]),
    ("cycle", 4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
    ("parallel", 3, [(0, 1), (0, 1), (1, 2)]),
    ("disconnected", 5, [(0, 1), (2, 3)]),
]
for name, c, edges in graphs:
    for seed in range(4):
        a = s.Matrix([1 + (i + seed) % 4 for i in range(c)])
        restriction = s.zeros(len(edges), 2 * len(edges))
        right_inverse = s.zeros(2 * len(edges), len(edges))
        normals = []
        for e, (i, j) in enumerate(edges):
            # Include both choices of one zero self-intersection, and negative pairs.
            if (seed + e) % 3 == 0:
                ni, nj = 0, -1 - seed - e
            elif (seed + e) % 3 == 1:
                ni, nj = -2 - seed - e, 0
            else:
                ni, nj = -1 - seed, -2 - e
            restriction[e, 2 * e] = ni
            restriction[e, 2 * e + 1] = -nj
            if ni:
                right_inverse[2 * e, e] = s.Rational(1, ni)
            else:
                right_inverse[2 * e + 1, e] = -s.Rational(1, nj)
            normals.append({"edge": [i, j], "normal_i": ni, "normal_j": nj,
                            "D_degree": str(a[i] * nj + a[j] * ni)})
        good = restriction * right_inverse == s.eye(len(edges))
        good = good and all(s.Rational(row["D_degree"]) < 0 for row in normals)
        keep(f"explicit edge right inverse: {name}, seed {seed}", good,
             positive_weights=[int(v) for v in a], normals=normals,
             restriction=matrix_data(restriction), right_inverse=matrix_data(right_inverse))

    # Separate formal weighted intersection matrices: the entries are not claimed
    # to be realized by the above self-intersections on actual surfaces.
    a = s.Matrix([i + 1 for i in range(c)])
    M = s.zeros(c)
    for i, j in edges:
        M[i, j] += 1
        M[j, i] += 1
    for i in range(c):
        M[i, i] = (-1 - sum(M[i, j] * a[j] for j in range(c) if j != i)) / a[i]
    A = s.diag(*a)
    B = A * M * A
    variables = s.symbols(f'x0:{c}')
    vector = s.Matrix(variables)
    left = (vector.T * B * vector)[0]
    right = sum(sum(B[i, j] for j in range(c)) * variables[i]**2 for i in range(c))
    right -= sum(B[i, j] * (variables[i] - variables[j])**2
                 for i in range(c) for j in range(i + 1, c))
    minors = [(-1)**j * B[:j, :j].det() for j in range(1, c + 1)]
    good = (M * a == -s.ones(c, 1) and s.expand(left - right) == 0
            and all(value > 0 for value in minors))
    keep(f"weighted negative identity: {name}", good, matrix=matrix_data(M),
         signed_leading_minors=[str(value) for value in minors],
         determinant=str(M.det()))

record = {
    "statement": "C.3br",
    "started_utc": started_at,
    "completed_utc": datetime.now(timezone.utc).isoformat(),
    "runtime_seconds": perf_counter() - started,
    "scope": "Finite exact rational projector, graph right-inverse, and weighted quadratic-form identities. No realization, Bertini, K-descent, or universal geometric assertion is inferred from these samples.",
    "checks": checks,
    "summary": {"passed": sum(item['passed'] for item in checks),
                "failed": sum(not item['passed'] for item in checks),
                "total": len(checks)},
}
path = base / 'output' / 'triple_free_component_lifting_certificate.json'
path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
if record['summary']['failed']:
    raise SystemExit(1)
