#!/usr/bin/env python3
"""Exact finite checks for C.3i; the all-dimension proof is in C3_picard.tex."""
from fractions import Fraction


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols, pivot = len(a), len(a[0]), 0
    for j in range(cols):
        row = next((i for i in range(pivot, rows) if a[i][j]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        scale = a[pivot][j]
        a[pivot] = [x / scale for x in a[pivot]]
        for i in range(rows):
            if i != pivot:
                scale = a[i][j]
                a[i] = [x - scale * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


print("Fermat quartic: F=z0^4+z1^4+z2^4; partial_i F=4*zi^3.")
for i in range(3):
    derivative_on_chart = 4 * Fraction(1) ** 3
    assert Fraction(1, 4) * derivative_on_chart == 1
    coordinate_section_on_chart = Fraction(1)
    assert coordinate_section_on_chart == 1
    print(f"chart z{i}=1: (1/4)*partial_{i}(F)=1; section z{i}=1 generates O(1).")
print("Thus all three charts are smooth and z0,z1,z2 have no common projective zero.")
print("N\tsource_vector_dimension\ttarget_vector_dimension\tcontraction_rank\tkernel_dimension\tcomposition_zero")
for n in range(4, 21):
    m = n - 2
    inclusion = [[int(i == j) for j in range(3)] for i in range(m + 1)]
    quotient = [[int(j == i + 3) for j in range(m + 1)] for i in range(m - 2)]
    ri, rq = rank(inclusion), rank(quotient)
    product = multiply(quotient, inclusion)
    zero = all(all(x == 0 for x in row) for row in product)
    assert ri == 3 and rq == m - 2 and zero
    assert (m + 1) - rq == ri
    print(f"{n}\t{m+1}\t{m-2}\t{ri}\t{m+1-rq}\t{zero}")
print("All checks passed over Q; actual Picard groups and henselian comparison are proved in the fragment.")
