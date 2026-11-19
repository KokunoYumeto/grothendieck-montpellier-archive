"""Finite exact checks accompanying E7--E9; not substitutes for the proofs.

E7: multiplication by the acting uniformizer in
  F_p[x,y]/(x^(p+1), y^(p+1)) cannot hit y^p.
E8: Jacobi's complementary principal minor identity for explicit SL matrices.
E9: exterior-algebra expansion, including both Cech and reordering signs.
All inputs and outputs are retained. No floating point operations are used.
"""
import itertools
import json
from fractions import Fraction
from pathlib import Path


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a)
    out = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        value = a[j][j]
        out *= value
        for i in range(j + 1, n):
            ratio = a[i][j] / value
            for k in range(j + 1, n):
                a[i][k] -= ratio * a[j][k]
            a[i][j] = 0
    return out


def inverse(matrix):
    n = len(matrix)
    a = [[Fraction(matrix[i][j]) for j in range(n)] +
         [Fraction(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        i = next(i for i in range(j, n) if a[i][j])
        a[i], a[j] = a[j], a[i]
        v = a[j][j]
        a[j] = [x / v for x in a[j]]
        for i in range(n):
            if i != j:
                v = a[i][j]
                a[i] = [x - v * y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def modular_rank(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        unit = pow(a[rank][col], -1, p)
        a[rank] = [x * unit % p for x in a[rank]]
        for i in range(len(a)):
            if i != rank:
                v = a[i][col]
                a[i] = [(x - v * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def wedge_sign(sequence):
    if len(set(sequence)) < len(sequence):
        return 0
    inversions = sum(sequence[i] > sequence[j]
                     for i in range(len(sequence))
                     for j in range(i + 1, len(sequence)))
    return (-1) ** inversions


results = {"E7": [], "E8": [], "E9": [], "E9_product_rule": []}
for p in (2, 3, 5, 7):
    e = p + 1
    basis = list(itertools.product(range(e), repeat=2))
    index = {m: i for i, m in enumerate(basis)}
    matrix = [[0] * (e * e) for _ in basis]
    for j, (a, b) in enumerate(basis):
        if a + 1 < e:
            matrix[index[(a + 1, b)]][j] = 1
    target = [int(m == (0, p)) for m in basis]
    rank = modular_rank(matrix, p)
    augmented_rank = modular_rank([row + [v] for row, v in zip(matrix, target)], p)
    assert augmented_rank == rank + 1
    results["E7"].append({"p": p, "e": e, "basis": "x^a y^b, lexicographic",
                          "target": f"y^{p}", "multiplication_x_rank": rank,
                          "augmented_rank": augmented_rank,
                          "tail_integral_inequality": p * p > e})

for g in (1, 2, 3, 4):
    n = 2 * g
    C = [[int(i == j) for j in range(n)] for i in range(n)]
    for t in range(3 * n):
        i, j = t % n, (t + 1 + t // n) % n
        if i == j:
            j = (j + 1) % n
        a = (-1) ** t * (t % 4 + 1)
        C[i] = [x + a * y for x, y in zip(C[i], C[j])]
    assert determinant(C) == 1
    Cinv = inverse(C)
    left = determinant([row[:g] for row in Cinv[:g]])
    right = determinant([row[g:] for row in C[g:]])
    assert left == right
    results["E8"].append({"g": g, "C": C, "det_C": 1,
                          "det_inverse_upper_left": str(left),
                          "det_lower_right": str(right),
                          "equal_mod_primes": {str(p): (left.numerator-right.numerator) % p == 0
                                               for p in (2, 3, 5, 7)}})

for g in range(1, 7):
    B = [[((i + 1) * (j + 2) + int(i == j)) for j in range(g)]
         for i in range(g)]
    coefficient = 0
    for perm in itertools.permutations(range(g)):
        sequence = []
        term = (-1) ** g
        for i, j in enumerate(perm):
            sequence.extend([i, g + j])
            term *= B[i][j]
        coefficient += term * wedge_sign(sequence)
    epsilon = (-1) ** (g * (g + 1) // 2)
    det_B = determinant(B)
    assert coefficient == epsilon * det_B
    results["E9"].append({"g": g, "B": B, "det_B": str(det_B),
                          "expanded_divided_power_coefficient": coefficient,
                          "epsilon": epsilon})

for g in range(1, 7):
    for h in range(1, 7):
        eps = lambda n: (-1) ** (n * (n + 1) // 2)
        ratio = eps(g + h) * eps(g) * eps(h)
        assert ratio == (-1) ** (g * h)
        if (g, h) in ((1, 1), (1, 2), (2, 2)):
            results["E9_product_rule"].append({"g": g, "h": h, "ratio": ratio})

path = Path(__file__).with_name("lattice_sign_output.json")
path.write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps({"all_exact_checks_passed": True,
                  "E7_primes": [2, 3, 5, 7],
                  "E8_dimensions": [1, 2, 3, 4],
                  "E9_dimensions": list(range(1, 7)),
                  "g1_g1_product_correction": -1,
                  "output": str(path)}))
