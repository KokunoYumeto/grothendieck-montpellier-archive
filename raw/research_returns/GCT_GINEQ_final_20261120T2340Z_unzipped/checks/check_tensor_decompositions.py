"""Exact checks for decomposition inputs and the residual quadratic certificate.

No numerical optimization is used.  Arithmetic is integer or Fraction.
Inputs: Derksen arXiv:1308.3860v2, §1.5 equation (5) and §8, p.23,
the unnumbered five-term D_3 display (PDF zero-based page 22).
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product


def outer_sum(terms):
    result = defaultdict(Fraction)
    for scale, factors in terms:
        for choices in product(*(list(v.items()) for v in factors)):
            index = tuple(i for i, _ in choices)
            coefficient = Fraction(scale)
            for _, c in choices:
                coefficient *= c
            result[index] += coefficient
    return {key: value for key, value in result.items() if value}


def v(*pairs):
    return dict(pairs)


# Matrix-unit indexing: 0=E11, 1=E12, 2=E21, 3=E22.
e = [v((i, 1)) for i in range(4)]
strassen = [
    (1, [v((0, 1), (3, 1))] * 3),
    (1, [v((2, 1), (3, -1)), e[0], v((1, 1), (3, 1))]),
    (1, [v((1, 1), (3, 1)), v((2, 1), (3, -1)), e[0]]),
    (1, [v((0, 1), (2, 1)), v((1, 1), (0, -1)), e[3]]),
    (1, [v((1, 1), (0, -1)), e[3], v((0, 1), (2, 1))]),
    (1, [e[3], v((0, 1), (2, 1)), v((1, 1), (0, -1))]),
    (1, [e[0], v((1, 1), (3, 1)), v((2, 1), (3, -1))]),
]
expected_m2 = {(2*i+j, 2*j+k, 2*k+i): Fraction(1)
               for i, j, k in product(range(2), repeat=3)}
actual_m2 = outer_sum(strassen)
assert actual_m2 == expected_m2, (actual_m2, expected_m2)
print("PASS: Derksen (5) equals M_2 exactly; 7 pure terms, 8 nonzero coefficients.")

# Vector indexing here: 0=e1, 1=e2, 2=e3.
det3_terms = [
    (Fraction(1, 2), [v((2, 1), (1, 1)), v((0, 1), (1, -1)), v((0, 1), (1, 1))]),
    (Fraction(1, 2), [v((0, 1), (1, 1)), v((1, 1), (2, -1)), v((1, 1), (2, 1))]),
    (1, [v((1, 1)), v((2, 1), (0, -1)), v((2, 1), (0, 1))]),
    (Fraction(1, 2), [v((2, 1), (1, -1)), v((1, 1), (0, 1)), v((1, 1), (0, -1))]),
    (Fraction(1, 2), [v((0, 1), (1, -1)), v((2, 1), (1, 1)), v((2, 1), (1, -1))]),
]
expected_d3 = {}
for p in permutations(range(3)):
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
    expected_d3[p] = Fraction((-1)**inversions)
actual_d3 = outer_sum(det3_terms)
assert actual_d3 == expected_d3, (actual_d3, expected_d3)
print("PASS: Derksen §8 formula equals row D_3 exactly; 5 pure terms, 6 nonzero coefficients.")

# The lower bound used for the explicit rational rank-two counterexample.
assert Fraction(7500, 3721) > 2
print("PASS: Exact rational margin 7500/3721 - 2 =", Fraction(7500, 3721) - 2)

# F-23: symmetric coefficient matrices for ad-bc and ad+bc.
# Their coordinate order is a,b,c,d. A nonzero residual coefficient c0
# multiplies this principal matrix, so its determinant becomes c0^4/16.
def exact_determinant(matrix):
    size = len(matrix)
    total = Fraction(0)
    for permutation in permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        term = Fraction((-1) ** inversions)
        for i in range(size):
            term *= matrix[i][permutation[i]]
        total += term
    return total


for cross_sign, name in [(-1, "det_2"), (1, "per_2")]:
    matrix = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    matrix[0][3] = matrix[3][0] = Fraction(1, 2)
    matrix[1][2] = matrix[2][1] = Fraction(cross_sign, 2)
    determinant = exact_determinant(matrix)
    assert determinant == Fraction(1, 16)
    print("PASS: F-23", name, "coefficient matrix has determinant", determinant)
