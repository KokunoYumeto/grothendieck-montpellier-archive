"""Exact author-side matrix checks for F43; not proof-kernel verification."""
import json
from itertools import product
import sympy as sp

v = sp.symbols("v")
delta = v + v**-1
D = delta**2
h = D - 1
words = list(product((1, 2), repeat=3))
index = {word: i for i, word in enumerate(words)}

def eq(A, B):
    assert A.shape == B.shape
    assert all(sp.cancel(x) == 0 for x in A - B)

E, F = sp.zeros(8), sp.zeros(8)
for word, i in index.items():
    for j in range(3):
        changed = list(word)
        if word[j] == 2:
            changed[j] = 1
            E[i, index[tuple(changed)]] = v**(-sum(1 if a == 1 else -1 for a in word[j+1:]))
        else:
            changed[j] = 2
            F[i, index[tuple(changed)]] = v**sum(1 if a == 1 else -1 for a in word[:j])

B3 = sp.Matrix([[v**2, v, 1], [-1-v**-2, v, 1], [-v**-1, -v**-2, delta]])
C3 = sp.Matrix([[1, 0, 0], [-v**-1, 1, 0], [0, -v**-1, 1]])
eq(B3 * C3.inv(), sp.Matrix([[h, delta, 1], [0, delta, 1], [0, 1, delta]]))
assert sp.cancel(B3.det() - h**2) == 0

T = sp.zeros(8)
T[0, 0] = T[3, 7] = 1
weight_words = [((1,1,2), (1,2,1), (2,1,1)), ((1,2,2), (2,1,2), (2,2,1))]
for target, local_words in [(1, weight_words[0]), (2, weight_words[1])]:
    for j, word in enumerate(local_words):
        T[target, index[word]] = B3[0, j]
for target, local_words, source_rows in [(4, weight_words[0], (1,2)), (6, weight_words[1], (2,1))]:
    for offset, source in enumerate(source_rows):
        for j, word in enumerate(local_words):
            T[target+offset, index[word]] = B3[source, j]
assert sp.cancel(T.det() - h**4) == 0

expected_E, expected_F = sp.zeros(8), sp.zeros(8)
for i, j, coefficient in [(1,0,h), (2,1,delta), (3,2,1), (6,4,1), (7,5,1)]:
    expected_E[i,j] = coefficient
for i, j, coefficient in [(0,1,1), (1,2,delta), (2,3,h), (4,6,1), (5,7,1)]:
    expected_F[i,j] = coefficient
eq(T*E*T.inv(), expected_E)
eq(T*F*T.inv(), expected_F)

c1 = sp.Matrix([[delta, 0], [1, 0]])
c2 = sp.Matrix([[0, 1], [0, delta]])
P = [sp.kronecker_product(c, c) + sp.kronecker_product(c-delta*sp.eye(2), c-delta*sp.eye(2)) for c in (c1,c2)]
B4 = sp.Matrix([[delta,-1,-1,delta], [0,-1,1,0], [2-D,-delta,-delta,D], [-D,delta,delta,D-2]])
assert sp.cancel(B4.det() - 8*h**2) == 0
eq(B4*P[0]*B4.inv(), sp.Matrix([[D,0,0,0], [0,0,0,0], [0,0,D,0], [0,0,D-2,0]]))
eq(B4*P[1]*B4.inv(), sp.Matrix([[D,0,0,0], [0,0,0,0], [0,0,0,D-2], [0,0,0,D]]))
flip = sp.Matrix([[1,0,0,0], [0,0,1,0], [0,1,0,0], [0,0,0,1]])
eq(B4*flip*B4.inv(), sp.diag(1,-1,1,1))

print(json.dumps({
    "status": "PASS",
    "checks": ["source_coproduct_E_F", "actual_bar_coordinates", "ordinary_determinant", "nonstandard_B4_action", "B4_determinant", "actual_factor_swap"],
    "full_determinant_by_tensor_and_blocks": "plus_or_minus 2^12*(D-1)^72",
    "method": "exact rational-function identities, no numerical sampling"
}))
