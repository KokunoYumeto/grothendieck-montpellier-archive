"""Exact integer checks for the stated theta/plethysm specializations.

No floating point arithmetic, computer algebra database, or theorem-prover claim.
The checks are corroborations of the accompanying proofs, not replacements.
"""
from fractions import Fraction
from math import comb
from pathlib import Path


def weyl_dimension(partition, rank):
    lam = tuple(partition) + (0,) * (rank - len(partition))
    result = Fraction(1)
    for i in range(rank):
        for j in range(i + 1, rank):
            result *= Fraction(lam[i] - lam[j] + j - i, j - i)
    assert result.denominator == 1
    return result.numerator


def binary_weight_multiplicity(outer, inner, weight):
    """Count unordered outer-tuples in [0,inner] summing to weight."""
    if weight < 0:
        return 0
    counts = [[0] * (weight + 1) for _ in range(outer + 1)]
    counts[0][0] = 1
    for part in range(inner + 1):
        for number in range(1, outer + 1):
            for total in range(part, weight + 1):
                counts[number][total] += counts[number - 1][total - part]
    return counts[outer][weight]


def two_row_coefficient(outer, inner, second_row):
    assert 0 <= second_row <= outer * inner // 2
    return (binary_weight_multiplicity(outer, inner, second_row)
            - binary_weight_multiplicity(outer, inner, second_row - 1))


rows = ["statement_id\tcheck\tparameters\tresult"]

for n in range(1, 13):
    for k in range(n + 1):
        actual = two_row_coefficient(2, n, k)
        expected = int(k % 2 == 0)
        assert actual == expected, (n, k, actual, expected)
rows.append("T-006\tbinary weight difference\t1<=n<=12; 0<=k<=n\tPASS")

for n in range(1, 13):
    for rank in range(2, 8):
        inner_dim = comb(n + rank - 1, rank - 1)
        left = comb(inner_dim + 1, 2)
        right = sum(weyl_dimension((2*n-2*j, 2*j), rank)
                    for j in range(n//2 + 1))
        assert left == right, (n, rank, left, right)
rows.append("T-006\tindependent Weyl-dimension total\t1<=n<=12; 2<=rank<=7\tPASS")

periodic = (3, -1, 1, 0, 2, -2)
for s in range(1, 41):
    actual = two_row_coefficient(3, 4*s, 5*s)
    numerator = s + periodic[s % 6]
    assert numerator % 3 == 0
    expected = numerator // 3
    assert actual == expected, (s, actual, expected)
    reverse = two_row_coefficient(4*s, 3, 5*s)
    assert reverse == expected, (s, reverse, expected)
rows.append("T-009\tindependent binary partition counts, both orders\t1<=s<=40\tPASS")

for n in range(1, 13):
    actual = two_row_coefficient(2, n, n)
    assert actual == int(n % 2 == 0)
rows.append("T-005\trectangular parity, rank two\t1<=n<=12\tPASS")

destination = Path(__file__).with_name("COMPUTATION_CERTIFICATES.tsv")
destination.write_text("\n".join(rows) + "\n")
print(destination.read_text(), end="")
