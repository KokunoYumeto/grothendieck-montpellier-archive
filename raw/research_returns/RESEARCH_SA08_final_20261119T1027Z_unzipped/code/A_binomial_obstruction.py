"""Finite certificate for the weight-two strict simplicial DGA obstruction.

Every bilinear map F_2^2 x F_2^2 -> F_2^2 is determined by eight bits.
Check naturality for the three faces a, b, a+b against b_1(s,t)=st.
No candidate exists. This finite check supplements the symbolic proof.
"""
from itertools import product
from time import perf_counter
import json

start = perf_counter()
vectors = list(product(range(2), repeat=2))
face_vectors = [(1, 0), (0, 1), (1, 1)]

def dot(x, y):
    return sum(a*b for a, b in zip(x, y)) % 2

def value(coeff, u, v):
    return tuple(sum(coeff[4*r+2*i+j]*u[i]*v[j]
                     for i in range(2) for j in range(2)) % 2
                 for r in range(2))

survivors = [0, 0, 0]
checks = 0
examples = []
for coeff in product(range(2), repeat=8):
    okay = True
    for step, face in enumerate(face_vectors):
        for u, v in product(vectors, repeat=2):
            checks += 1
            if dot(face, value(coeff, u, v)) != dot(face, u)*dot(face, v):
                okay = False
                break
        if not okay:
            break
        survivors[step] += 1
    if okay:
        examples.append(coeff)
assert survivors == [16, 1, 0], survivors
assert not examples
print(json.dumps({
    "statement": "A-016", "field": "F_2", "bilinear_candidates": 256,
    "survivors_after_successive_faces": survivors,
    "individual_naturality_checks": checks,
    "explicit_failed_pair": [[1, 0], [0, 1]],
    "expected_third_face": 1, "actual_third_face": 0,
    "elapsed_seconds": perf_counter()-start,
    "result": "no simplicial bilinear map with b_1(1,1)=1"
}, indent=2))
