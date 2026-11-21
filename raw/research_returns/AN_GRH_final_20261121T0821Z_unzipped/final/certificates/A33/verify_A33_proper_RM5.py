#!/usr/bin/env python3
"""Exact small certificate for the proper ordinary RM5 restriction in A33.

Uses only Python integers. Point counts use explicit F16 arithmetic and
F4's embedded subfield; the ratio resultant is a 4 by 4 companion-matrix
determinant computed by the complete permutation formula. No CAS or
Jacobian package is imported. This is not formal verification.
"""
from pathlib import Path
from itertools import permutations
from functools import reduce
from math import gcd
import hashlib
import json


def field_product(a, b):
    result = 0
    for i in range(4):
        if b >> i & 1:
            result ^= a << i
    for j in range(6, 3, -1):
        if result >> j & 1:
            result ^= 0x13 << (j-4)
    return result


M = [[field_product(a, b) for b in range(16)] for a in range(16)]
inverse = [0] + [next(b for b in range(1, 16) if M[a][b] == 1)
                 for a in range(1, 16)]


def field_power(a, n):
    result = 1
    for unused in range(n):
        result = M[result][a]
    return result


def trace(a, degree):
    result = 0
    for unused in range(degree):
        result ^= a
        a = M[a][a]
    assert result in (0, 1)
    return result


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def plus(a, b):
    result = list(a)+[0]*max(0, len(b)-len(a))
    for i, coefficient in enumerate(b):
        result[i] += coefficient
    return trim(result)


def product(a, b):
    result = [0]*max(0, len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i+j] += ai*bj
    return trim(result)


def power(a, n):
    result = [1]
    for unused in range(n):
        result = product(result, a)
    return result


def matrix_product(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


def main():
    f4 = [a for a in range(16) if field_power(a, 4) == a]
    assert f4 == [0, 1, 6, 7]
    u = 6
    assert M[u][u] == 7 and M[u][u] ^ u ^ 1 == 0
    rows, points16 = [], []
    counts = {}
    for size, degree, elements in ((4, 2, f4), (16, 4, range(16))):
        count = 3  # one totally ramified rational point at 0,1,infinity
        for x in elements:
            if x in (0, 1):
                continue
            rhs = x ^ M[u][inverse[x]] ^ M[7][inverse[x ^ 1]]
            tr = trace(rhs, degree)
            ys = [y for y in elements if M[y][y] ^ y == rhs]
            assert len(ys) == 2*(1-tr)
            count += len(ys)
            if size == 16:
                rows.append([x, rhs, tr])
                points16.extend([[x, y] for y in ys])
        counts[str(size)] = count
    assert counts == {'4': 3, '16': 15}
    a1 = counts['4'] - 5
    numerator = a1*a1 - (17-counts['16'])
    assert numerator % 2 == 0
    a2 = numerator//2
    P = [16, 4*a1, a2, a1, 1]
    assert P == [16, -8, 1, -2, 1]
    # Multiplication by X in Z[X]/P(X), basis 1,X,X^2,X^3.
    C = [[0, 0, 0, -16], [1, 0, 0, 8],
         [0, 1, 0, -1], [0, 0, 1, 2]]
    identity = [[int(i == j) for j in range(4)] for i in range(4)]
    powers = [identity]
    for unused in range(4):
        powers.append(matrix_product(powers[-1], C))
    assert all(sum(P[k]*powers[k][i][j] for k in range(5)) == 0
               for i in range(4) for j in range(4))
    # det(P(t C)) is Res_X(P(X),P(tX)).
    matrix = [[trim([P[k]*powers[k][i][j] for k in range(5)])
               for j in range(4)] for i in range(4)]
    resultant = []
    for perm in permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4)
                         for j in range(i+1, 4))
        term = [(-1)**inversions]
        for i in range(4):
            term = product(term, matrix[i][perm[i]])
        resultant = plus(resultant, term)
    A = [4, 7, 10, 7, 4]
    B = [16, -8, 1, -8, 16]
    factored = product([256], product(power([-1, 1], 4),
                                     product(power(A, 2), B)))
    assert resultant == factored
    for poly in (P, A, B):
        assert reduce(gcd, (abs(c) for c in poly)) == 1
        assert [c % 3 for c in poly] == [1]*5
    assert [pow(3, d, 5) for d in (1, 2, 4)] == [3, 4, 1]
    # X^2 ((X+4/X)^2 -2(X+4/X)-7) equals P(X).
    real_polynomial = [-7, -2, 1]
    expanded = [16, -8, 8-7, -2, 1]
    assert expanded == P
    result = {
        'curve': 'y^2+y=x+u/x+u^2/(x+1), u^2+u+1=0 over F4',
        'field16_modulus': 0x13, 'u_encoding': 6,
        'encoding': 'binary polynomial coefficients, low degrees first',
        'embedded_F4': f4, 'point_counts': counts,
        'F16_trace_table_x_rhs_trace': rows,
        'F16_unramified_affine_points': points16,
        'branch_points': ['0', '1', 'infinity'],
        'Weil_polynomial_low_to_high': P,
        'ratio_resultant_low_to_high': resultant,
        'ratio_factors_low_to_high': {'scalar': 256,
                                     'factor1': [-1, 1], 'multiplicity1': 4,
                                     'factor2': A, 'multiplicity2': 2,
                                     'factor3': B, 'multiplicity3': 1},
        'irreducibility_certificate': 'P,A,B primitive and reduce to Phi5 mod3; ord5(3)=4',
        'real_Frobenius_polynomial_low_to_high': real_polynomial,
        'real_discriminant': 32,
        'scope': 'Exact arithmetic certificate; the accompanying proof derives absolute simplicity and absence of Rosati-fixed O5. No formal verification claim.',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    Path(__file__).with_suffix('.json').write_text(
        json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({k: result[k] for k in ('point_counts',
        'Weil_polynomial_low_to_high', 'ratio_factors_low_to_high',
        'real_discriminant', 'source_sha256')}, indent=2))


if __name__ == '__main__':
    main()
