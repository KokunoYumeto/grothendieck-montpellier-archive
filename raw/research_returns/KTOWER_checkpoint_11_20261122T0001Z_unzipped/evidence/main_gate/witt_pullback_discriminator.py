"""A finite discriminator for replacing a genus trace by a Witt coefficient.

The two enumeration paths use (1) the exact Schur determinant, and (2)
integer Bareiss determinants of the full Gram matrix.  This is one example,
not a search for auxiliary fields or a uniform nonvanishing certificate.
"""
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

C = ((2, -1, 0), (-1, 2, -1), (0, -1, 2))
B = ((2, -1, 0), (-1, 2, -1), (0, -1, 14))
M = ((3, 2, 1), (2, 4, 2), (1, 2, 3))


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def mv(x):
    return tuple(dot(row, x) for row in M)


def gram(columns):
    R = tuple(zip(*columns))
    return [list(C[i]) + list(R[i]) for i in range(3)] + [
        list(columns[i]) + list(B[i]) for i in range(len(columns))]


def bareiss(A):
    A = [list(row) for row in A]
    n, old, sign = len(A), 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot = next((j for j in range(k + 1, n) if A[j][k]), None)
            if pivot is None:
                return 0
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * A[i][j] - A[i][k] * A[k][j]
                assert numerator % old == 0
                A[i][j] = numerator // old
        for i in range(k + 1, n):
            A[i][k] = 0
        old = pivot
    return sign * A[-1][-1]


def principal(A, n):
    return [row[:n] for row in A[:n]]


def beta(n, f=79):
    vals = [Fraction(1)]
    for m in range(1, n + 1):
        vals.append(-sum(comb(m + 1, j) * vals[j] for j in range(m)) / (m + 1))
    chi = [0] + [1 if pow(a, (f - 1) // 2, f) == 1 else -1
                 for a in range(1, f)]
    return sum(comb(n, j) * vals[j] * Fraction(f ** j, f)
               * sum(chi[a] * a ** (n - j) for a in range(f))
               for j in range(n + 1)) / n


def main():
    assert bareiss(C) == 4 and bareiss(B) == 40
    assert [[dot(C[i], tuple(M[j][k] for j in range(3)))
             for k in range(3)] for i in range(3)] == [
                 [4, 0, 0], [0, 4, 0], [0, 0, 4]]
    # All positive definite Gram matrices satisfy |R_ij|^2<C_ii B_jj.
    first = list(product(range(-1, 2), repeat=3))
    last = list(product(range(-5, 6), repeat=3))
    candidates = [[(x, mv(x), 4 * diagonal - dot(x, mv(x)))
                   for x in points if dot(x, mv(x)) < 4 * diagonal]
                  for diagonal, points in [(2, first), (2, first), (14, last)]]
    schur = set()
    for x, mx, a in candidates[0]:
        for y, my, b in candidates[1]:
            z = -4 - dot(x, my)
            minor = a * b - z * z
            if minor <= 0:
                continue
            for v, m, c in candidates[2]:
                s, t = -dot(x, m), -4 - dot(y, m)
                if minor * c - a * t * t - b * s * s + 2 * z * s * t == 16 * 79:
                    schur.add((x, y, v))
    # A second, exhaustive path uses the full matrix and Sylvester's criterion.
    direct = set()
    direct_six_by_six_calls = 0
    for x in first:
        for y in first:
            stub = gram((x, y, (0, 0, 0)))
            if bareiss(principal(stub, 4)) <= 0 or bareiss(principal(stub, 5)) <= 0:
                continue
            for v in last:
                G = gram((x, y, v))
                direct_six_by_six_calls += 1
                if bareiss(G) == 79:
                    assert all(bareiss(principal(G, j)) > 0 for j in range(1, 7))
                    direct.add((x, y, v))
    assert direct == schur and len(direct) == 56
    b3, b17 = beta(3), beta(17)
    mod = lambda x: x.numerator * pow(x.denominator, -1, 31) % 31
    assert b3 == 992 and mod(b17) == 20
    coefficient = Fraction(-56) * b17
    mass = b3 / 23040
    assert mass == Fraction(31, 720) and mod(coefficient) == 27
    rows = sorted([[list(v) for v in columns] for columns in direct])
    report = {
        'finding_id': 'KT-WITT-PULLBACK-MASS-OBSTRUCTION',
        'p': 31, 'b': 17, 'k': 20, 'D': -79,
        'C': C, 'B': B, 'det_C': 4, 'det_B': 40,
        'coordinate_box_size': len(first) ** 2 * len(last),
        'schur_column_counts': [len(x) for x in candidates],
        'direct_six_by_six_determinants': direct_six_by_six_calls,
        'determinant_79_count': len(rows), 'two_enumerations_agree': True,
        'cross_block_columns': rows,
        'beta3_exact': str(b3), 'beta17_exact': str(b17),
        'beta17_mod31': mod(b17), 'det79_witt_contribution_mod31': mod(coefficient),
        'genus_mass_exact': str(mass), 'genus_trace_mod31': mod(-b17 * mass),
        'scope': 'One determinant-filtered Witt coefficient is a unit although the same-D genus trace and beta3 vanish modulo 31. No general integral functional is ruled out; no auxiliary-field existence follows.',
        'status': 'PASS',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'cross_block_columns'}, indent=2))


if __name__ == '__main__':
    main()
