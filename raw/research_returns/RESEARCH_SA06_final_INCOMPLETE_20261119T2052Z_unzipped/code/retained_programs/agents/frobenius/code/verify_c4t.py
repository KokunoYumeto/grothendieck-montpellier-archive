"""Exact matrix checks and a bounded binary-form reduction certificate for C.4t.

The bounded enumeration supplements, and does not replace, the proof that every
positive definite integral unimodular binary form is equivalent to the identity.
"""
import math
import time
from pathlib import Path
import sympy as s

started = time.perf_counter()
ell, a, b, c, u, v, w, z = s.symbols("ell a b c u v w z", nonzero=True)
H = s.Matrix([[ell, 1], [1, 2 / ell]])
Hinv = s.Matrix([[2 / ell, -1], [-1, ell]])
R = s.Matrix([[1, 2 / ell], [0, -1]])
j = s.diag(1, ell)
M0 = s.Matrix([[1, 1], [1, 2]])
Hab = s.Matrix([[a * ell, b], [b, 2 * c / ell]])
M = s.Matrix([[a, b], [b, 2 * c]])
G = s.Matrix([[u, 2 * v], [w, z]])
U = s.Matrix([[u, 2 * v / ell], [w * ell, z]])

def zero(mat):
    return all(s.simplify(entry) == 0 for entry in mat)

assert zero(H * Hinv - s.eye(2))
assert zero(R * R - s.eye(2))
assert zero(R.T * H * R - H)
assert zero(j.T * H * j - ell * M0)
for column in (s.Matrix([1, 0]), s.Matrix([-1, ell])):
    assert s.simplify((column.T * H * column)[0] - ell) == 0
assert zero(j.T * Hab * j - ell * M)
assert zero(U * j - j * G)
assert s.simplify(U.det() - (u * z - 2 * v * w)) == 0
assert zero(U * U.adjugate() - (u * z - 2 * v * w) * s.eye(2))
assert s.expand(16 * M.det()**4 - 4**2 * (2*a*c-b*b)**4) == 0
print("PASS: polarization inverse, involution, both eigenspace restrictions,")
print("      pullback matrices, Uj=jG, adjugate inverse, and degree identity.")

def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def gram(A, B):
    return mul(mul(transpose(B), A), B)

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def inverse_unimodular(A):
    d = det(A)
    assert abs(d) == 1
    return [[A[1][1]//d, -A[0][1]//d], [-A[1][0]//d, A[0][0]//d]]

def reduce_form(original):
    current = [row[:] for row in original]
    basis = [[1, 0], [0, 1]]
    steps = 0
    while True:
        aa, bb, cc = current[0][0], current[0][1], current[1][1]
        if cc < aa:
            change = [[0, 1], [1, 0]]
        else:
            shift = (2*bb+aa)//(2*aa)
            if shift == 0:
                assert 2*abs(bb) <= aa <= cc
                assert current == [[1, 0], [0, 1]]
                assert gram(original, basis) == current
                return basis, steps
            change = [[1, -shift], [0, 1]]
        current = gram(current, change)
        basis = mul(basis, change)
        steps += 1
        assert steps < 1000

limit = 250
base = [[1, 1], [1, 2]]
base_to_identity, _ = reduce_form(base)
count = 0
max_steps = 0
max_entry = 0
examples = []
for aa in range(1, limit+1):
    for cc in range(1, limit+1):
        sq = 2*aa*cc-1
        root = math.isqrt(sq)
        if root*root != sq:
            continue
        for bb in (-root, root):
            form = [[aa, bb], [bb, 2*cc]]
            to_identity, steps = reduce_form(form)
            isometry = mul(to_identity, inverse_unimodular(base_to_identity))
            assert gram(form, isometry) == base
            assert isometry[0][1] % 2 == 0
            assert aa % 2 == bb % 2 == cc % 2 == 1
            assert abs(det(isometry)) == 1
            count += 1
            max_steps = max(max_steps, steps)
            max_entry = max(max_entry, *(abs(x) for row in isometry for x in row))
            if aa in (1, 17, 113, 233) and len(examples) < 8:
                examples.append((aa, bb, cc, isometry))
print(f"PASS: all {count} forms with 1<=a,c<={limit} and 2ac-b^2=1.")
print(f"Maximum reduction steps: {max_steps}; maximum isometry entry: {max_entry}.")
for aa, bb, cc, isometry in examples:
    print(f"  (a,b,c)=({aa},{bb},{cc}), G={isometry}")
print("Every recorded G has even upper-right entry and determinant +/-1.")
print("Bounded verification only; unrestricted proof is in C4_jacobian_exclusion.tex.")
print(f"Runtime seconds: {time.perf_counter()-started:.6f}")
