#!/usr/bin/env python3
"""Exact small counts for the exponent-13 quotient; this does NOT certify Sha.

B: v^2 = 1 - 12t + 52t^2 - 104t^3 + 104t^4 - 52t^5.
The symbolic quotient derivation and the remaining arithmetic gate are
separate mathematical arguments. This script uses only Python integers.
"""
from math import gcd

COEFFICIENTS = (1, -12, 52, -104, 104, -52)


def count(p, degree):
    def character(a):
        value = pow(a % p, (p - 1) // 2, p)
        return value if value < 2 else -1

    if degree == 1:
        return 1 + sum(
            1 + character(sum(c * pow(a, i, p) for i, c in enumerate(COEFFICIENTS)))
            for a in range(p)
        )
    assert degree == 2
    d = next(a for a in range(2, p) if character(a) == -1)

    def multiply(a, b):
        return ((a[0] * b[0] + d * a[1] * b[1]) % p,
                (a[0] * b[1] + a[1] * b[0]) % p)

    total = 1
    for a in range(p):
        for b in range(p):
            value = (0, 0)
            for coefficient in reversed(COEFFICIENTS):
                value = multiply(value, (a, b))
                value = ((value[0] + coefficient) % p, value[1])
            # Quadratic character over F_(p^2) is the character of its norm.
            total += 1 + character(value[0] ** 2 - d * value[1] ** 2)
    return total


if __name__ == '__main__':
    orders = []
    for p, expected in ((3, (7, 11, 27)), (5, (6, 26, 26))):
        first, second = count(p, 1), count(p, 2)
        order = (first * first + second) // 2 - p
        assert (first, second, order) == expected
        orders.append(order)
        print(f'p={p}: #B(F_p)={first}; #B(F_p^2)={second}; #Jac(B)(F_p)={order}')
    assert gcd(*orders) == 1
    print('Coprime good-reduction orders certify trivial rational torsion.')
    print('Finite Sha of the complementary Prym remains unproved.')
