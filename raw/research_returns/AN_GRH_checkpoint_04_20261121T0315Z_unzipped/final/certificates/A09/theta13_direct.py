#!/usr/bin/env python3
"""Independent exact principal-divisor certificate for rank-one theta 13-torsion.

No Jacobian/Cantor implementation and no third-party packages are used.
K = F_2[z]/(z^4+z+1), integers encode binary polynomials in z.
The curve is Y^2 + X^2 Y = X^5 + X; P is its unique point at infinity.
For R=(z^2+z,z^3), construct F=A(X)+B(X)Y with div(F)=13(R-P).
The finite checks establish the norm identity, vanishing at R, nonvanishing
at its hyperelliptic conjugate, degree bounds, and ord_13(2)=12.
The geometric argument identifying this divisor and the Raynaud theta
bundle is supplied in POSITIVE_RANK_THETA.tex / POSITIVE_RANK_NOTES.md.
"""
from pathlib import Path
import json

MOD = 0b10011


def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 16:
            a ^= MOD
    return out


def power(a, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


def inv(a):
    assert a
    out = power(a, 14)
    assert mul(a, out) == 1
    return out


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) ^
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def pmul(a, b):
    out = [0] * max(0, len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] ^= mul(ai, bj)
    return trim(out)


def ppow(a, n):
    out = [1]
    for _ in range(n):
        out = pmul(out, a)
    return out


def peval(a, x):
    out = 0
    for ai in reversed(a):
        out = mul(out, x) ^ ai
    return out


def translate(a, r):
    """Return a(X+r) in coefficient order increasing in X."""
    out = []
    for ai in reversed(a):
        out = add(pmul(out, [r, 1]), [ai])
    return out


def nullspace_one(matrix):
    a = [row[:] for row in matrix]
    ncols = len(a[0])
    pivots = []
    row = 0
    for col in range(ncols):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = inv(a[row][col])
        a[row] = [mul(scale, x) for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scale = a[i][col]
                a[i] = [x ^ mul(scale, y) for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
    free = [i for i in range(ncols) if i not in pivots]
    assert len(free) == 1
    vector = [0] * ncols
    vector[free[0]] = 1
    for row, col in reversed(list(enumerate(pivots))):
        value = 0
        for j in free:
            value ^= mul(a[row][j], vector[j])
        vector[col] = value
    for row in matrix:
        total = 0
        for aij, vj in zip(row, vector):
            total ^= mul(aij, vj)
        assert total == 0
    assert vector[-1]
    scale = inv(vector[-1])
    return [mul(scale, v) for v in vector], len(pivots)


def main():
    # Irreducibility: no roots in F_2, and not divisible by the only
    # monic irreducible quadratic z^2+z+1; also every nonzero element inverts.
    assert (1 ^ 1 ^ 1) == 1
    for a in range(1, 16):
        inv(a)
    r, s = 6, 8
    h, f = [0, 0, 1], [0, 1, 0, 0, 0, 1]
    assert mul(s, s) ^ mul(mul(r, r), s) ^ peval(f, r) == 0
    assert mul(r, r) ^ r ^ 1 == 0
    coefficients = [s]
    for i in range(1, 13):
        rhs = {1: power(r, 4) ^ 1, 4: r, 5: 1}.get(i, 0)
        if i % 2 == 0:
            rhs ^= mul(coefficients[i // 2], coefficients[i // 2])
        if i >= 2:
            rhs ^= coefficients[i - 2]
        coefficients.append(mul(rhs, inv(mul(r, r))))
    matrix = [[coefficients[i - j] for j in range(5)] for i in range(7, 13)]
    b_taylor, rank = nullspace_one(matrix)
    a_taylor = []
    for i in range(7):
        value = 0
        for j in range(min(i, 4) + 1):
            value ^= mul(b_taylor[j], coefficients[i - j])
        a_taylor.append(value)
    a = translate(a_taylor, r)
    b = translate(b_taylor, r)
    assert len(a) <= 7 and len(b) == 5 and b[-1] == 1
    norm = add(add(pmul(a, a), pmul(pmul(a, b), h)), pmul(pmul(b, b), f))
    target = ppow([r, 1], 13)
    assert norm == target
    value_at_R = peval(a, r) ^ mul(peval(b, r), s)
    conjugate_s = s ^ mul(r, r)
    value_at_conjugate_R = peval(a, r) ^ mul(peval(b, r), conjugate_s)
    assert value_at_R == 0 and value_at_conjugate_R != 0
    powers_two = [pow(2, i, 13) for i in range(12)]
    assert sorted(powers_two) == list(range(1, 13)) and pow(2, 12, 13) == 1
    result = {
        'field_modulus': 'z^4+z+1',
        'encoding': 'integer sum of coefficients times powers of 2; field characteristic two',
        'curve': 'Y^2+X^2*Y=X^5+X',
        'point_R': [r, s], 'point_R_symbolic': ['z^2+z', 'z^3'],
        'A_coefficients_ascending': a, 'B_coefficients_ascending': b,
        'norm_coefficients_ascending': norm,
        'norm_target': '(X+(z^2+z))^13',
        'value_at_R': value_at_R,
        'value_at_hyperelliptic_conjugate_R': value_at_conjugate_R,
        'Taylor_matrix_rank': rank,
        'Taylor_B_coefficients_ascending': b_taylor,
        'Taylor_Y_coefficients_ascending': coefficients,
        'powers_of_2_mod_13': powers_two,
        'pole_orders_at_infinity': {'X': 2, 'Y': 5, 'A': 12, 'B*Y': 13},
        'certified_divisor': 'div(A+B*Y)=13(R-P)',
        'exact_order': 13,
        'exact_order_argument': 'R differs from P; a principal divisor R-P would give a degree-one map from a genus-two curve to P^1.',
        'two_rank_C': 1,
        'two_rank_argument': 'AS model y^2+y=x^3+x^(-1) has two poles of odd orders 3 and 1; p-rank is number of poles minus one.',
        'limitations': 'No universal positive-rank theta incidence theorem or counterexample over finite fields is asserted.'
    }
    target_file = Path(__file__).with_suffix('.json')
    target_file.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
