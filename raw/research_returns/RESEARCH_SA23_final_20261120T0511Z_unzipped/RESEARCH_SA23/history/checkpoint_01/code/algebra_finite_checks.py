"""Exhaustive finite checks for SA23-G-2 and the finite forms of G-4.

Only the four-element algebra F_2[e]/(e^2) is used.  Tensor products
over this algebra are computed as F_2 vector spaces modulo every
balancing relation, rather than inferred from the asserted theorem.
"""
from itertools import product
from time import perf_counter

start = perf_counter()
B = range(4)                    # a + b e encoded as a + 2b

def add(a, b):
    return a ^ b

def mul(a, b):
    return ((a & 1) * (b & 1)) | (((((a >> 1) & 1) * (b & 1)) ^
                                    ((a & 1) * ((b >> 1) & 1))) << 1)

def rank(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                vector ^= pivots[pivot]
            else:
                pivots[pivot] = vector
                break
    return len(pivots)

def tensor_vector(m, n, dm, dn):
    result = 0
    for i in range(dm):
        for j in range(dn):
            if ((m >> i) & 1) and ((n >> j) & 1):
                result ^= 1 << (i * dn + j)
    return result

def balanced_relations(dm, dn, action_m, action_n):
    relations = []
    for b, m, n in product(B, range(1 << dm), range(1 << dn)):
        relations.append(tensor_vector(action_m(b, m), n, dm, dn) ^
                         tensor_vector(m, action_n(b, n), dm, dn))
    return relations

for a, b, c in product(B, repeat=3):
    assert add(add(a, b), c) == add(a, add(b, c))
    assert mul(mul(a, b), c) == mul(a, mul(b, c))
    assert mul(a, add(b, c)) == add(mul(a, b), mul(a, c))
for a, b in product(B, repeat=2):
    assert add(a, b) == add(b, a)
    assert mul(a, b) == mul(b, a)
    assert (mul(a, b) & 1) == ((a & 1) * (b & 1))
for a in B:
    assert add(a, 0) == a and add(a, a) == 0 and mul(a, 1) == a
assert mul(2, 2) == 0 and 2 != 0
print("Ring axioms: 64 triples, 16 pairs, 4 elements; all passed.")

# A=B, C=F_2; v is A tensor_F2 F2 -> A, hence basis matrix identity.
assert rank([1, 2]) == 2
for c in range(2):
    assert (c & 1) == c       # phi(u(c)) = c
for a in B:
    assert mul(a, 1) == a
print("G-2 hypotheses: graded degrees (1,1); split augmentation; v rank 2/2.")

# I=(e), with coordinate m encoding m e, and C=B/I.
action_simple = lambda b, n: (b & 1) * n
relations_source = balanced_relations(1, 1, action_simple, action_simple)
relations_target = balanced_relations(2, 1, mul, action_simple)
source_dim = 1 - rank(relations_source)
target_dim = 2 - rank(relations_target)
assert source_dim == target_dim == 1
# Inclusion maps the source basis e tensor 1 to target vector 2.
assert rank(relations_target + [2]) == rank(relations_target)
assert rank(relations_source + [1]) == rank(relations_source) + 1
print(f"G-2 tensors: {len(relations_source)} source and "
      f"{len(relations_target)} target balancing relations checked.")
print("dim(I tensor_B C)=1; dim(B tensor_B C)=1; induced map rank=0.")
print("Conclusion: C is not B-flat, despite every good and very good hypothesis.")

# G-4 first example: A=B=C=F2[e]/e^2 with identity maps.
multiplication_columns = [mul(1 << i, 1 << j)
                          for i, j in product(range(2), repeat=2)]
assert rank(multiplication_columns) == 2
assert {a for a in B if a == 0} == {0}
assert {mul(2, a) for a in B} == {0, 2}
print("G-4 missing augmentation: multiplication has rank 2/2, "
      "ker(phi)={0}, A_+B={0,e}; asserted equivalence is false.")

# G-4 second example: A=C=F2, B=dual numbers.
hilbert_a, hilbert_b, hilbert_c = [1, 0], [1, 1], [1, 0]
convolution_degree_one = hilbert_a[0]*hilbert_c[1] + hilbert_a[1]*hilbert_c[0]
assert hilbert_b[1] > convolution_degree_one
print("G-4 splitting alone: degree-one ranks B_1=1 and (A tensor C)_1=0; "
      "proposed Hilbert upper bound is false.")
print(f"Elapsed seconds: {perf_counter()-start:.6f}")
