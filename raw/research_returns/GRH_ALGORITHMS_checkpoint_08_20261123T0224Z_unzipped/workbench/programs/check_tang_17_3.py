#!/usr/bin/env python3
"""Exact finite arithmetic for the two constructions of F_(17^3).

Run from the workbench root: python3 programs/check_tang_17_3.py
No external dependencies; this is a finite computation, not a formal proof.
All polynomial coefficient lists are in increasing degree order.
"""
import json

P = 17


class Quotient:
    def __init__(self, modulus):
        assert modulus[-1] == 1
        self.modulus = [x % P for x in modulus]
        self.degree = len(modulus) - 1
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)
        self.x = self.reduce([0, 1])

    def reduce(self, a):
        a = [x % P for x in a]
        a += [0] * max(0, self.degree - len(a))
        for i in range(len(a) - 1, self.degree - 1, -1):
            for j in range(self.degree):
                a[i - self.degree + j] = (
                    a[i - self.degree + j] - a[i] * self.modulus[j]
                ) % P
        return tuple(a[: self.degree])

    def add(self, a, b):
        return tuple((x + y) % P for x, y in zip(a, b))

    def scale(self, c, a):
        return tuple(c * x % P for x in a)

    def mul(self, a, b):
        c = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i + j] += x * y
        return self.reduce(c)

    def pow(self, a, e):
        b = self.one
        while e:
            if e & 1:
                b = self.mul(b, a)
            a = self.mul(a, a)
            e //= 2
        return b

    def evaluate(self, coefficients, a):
        value = self.zero
        for c in reversed(coefficients):
            value = self.add(self.mul(value, a), self.scale(c, self.one))
        return value


def roots_over_prime(coefficients):
    return [
        x for x in range(P)
        if sum(c * pow(x, i, P) for i, c in enumerate(coefficients)) % P == 0
    ]


assert pow(P, 1, 3) == 2 and pow(P, 2, 3) == 1
assert (P**2 - 1) % 9 == 0 and (P**2 - 1) % 27 != 0

# The older auxiliary-prime construction.
assert pow(P, 2, 7) == 2
assert all(pow(P, k, 7) != 1 for k in range(1, 6))
assert pow(P, 6, 7) == 1
cyclotomic = Quotient([1] * 7)
zeta = cyclotomic.x
eta = cyclotomic.add(zeta, cyclotomic.pow(zeta, 6))
old_cubic = [16, 15, 1, 1]
assert cyclotomic.evaluate(old_cubic, eta) == cyclotomic.zero
assert cyclotomic.pow(eta, P**3) == eta
assert cyclotomic.pow(eta, P) != eta
assert roots_over_prime(old_cubic) == []

# Tang's root chain in E=F_17[u]/(u^2+u+1).
E = Quotient([1, 1, 1])
u = E.x
assert roots_over_prime([1, 1, 1]) == []
c = (2, 8)
assert E.pow(c, 3) == u
assert E.pow(c, 9) == E.one and E.pow(c, 3) != E.one
c_inverse = E.pow(c, 8)
assert c_inverse == (11, 9)
assert E.add(c, c_inverse) == (13, 0)
cube_roots = [
    (a, b) for a in range(P) for b in range(P)
    if E.pow((a, b), 3) == u
]
assert cube_roots == [(2, 8), (6, 15), (9, 11)]
trace_roots = [E.add(z, E.pow(z, P))[0] for z in cube_roots]
assert trace_roots == [13, 14, 7]
prime_query = [1, 14, 0, 1]
assert roots_over_prime(prime_query) == [7, 13, 14]

# The tower E[v]/(v^3-c) is represented over F_17 by
# v^6-13v^3+1=0, with u=4+15v^3.
T = Quotient([1, 0, 0, 4, 0, 0, 1])
v = T.x
assert T.pow(v, 27) == T.one and T.pow(v, 9) != T.one
assert all(pow(P, k, 27) != 1 for k in range(1, 6))
assert pow(P, 6, 27) == 1
embedded_u = T.add(T.scale(4, T.one), T.scale(15, T.pow(v, 3)))
assert T.evaluate([1, 1, 1], embedded_u) == T.zero
assert T.pow(v, 9) == embedded_u
alpha = T.add(v, T.pow(v, 26))
tang_cubic = [4, 14, 0, 1]
assert T.evaluate(tang_cubic, alpha) == T.zero
assert T.pow(alpha, P**3) == alpha
assert T.pow(alpha, P) != alpha
assert roots_over_prime(tang_cubic) == []

# Optional prime meeting Tang's stronger auxiliary congruence.
assert 37 % 36 == 1 and pow(P, 12, 37) == 26

print(json.dumps({
    "characteristic": P,
    "extension_degree": 3,
    "ord_3_17": 2,
    "v_3_17_squared_minus_1": 2,
    "older_route": {
        "auxiliary_prime": 7,
        "17_squared_mod_7": 2,
        "ord_7_17": 6,
        "cubic_coefficients": old_cubic,
        "roots_in_F17": roots_over_prime(old_cubic),
        "generator_coordinates_mod_Phi7": eta,
    },
    "tang_route": {
        "E_modulus": [1, 1, 1],
        "cube_roots_of_u": cube_roots,
        "selected_c": c,
        "inverse_c": c_inverse,
        "order_c": 9,
        "prime_field_query_coefficients": prime_query,
        "prime_field_query_roots": [7, 13, 14],
        "tower_modulus_over_F17": T.modulus,
        "order_v": 27,
        "alpha_coordinates_in_tower": alpha,
        "cubic_coefficients": tang_cubic,
        "roots_in_F17": roots_over_prime(tang_cubic),
        "auxiliary_table_required": False,
        "optional_auxiliary_prime": 37,
        "17_power_12_mod_37": 26,
    },
    "all_assertions_passed": True,
}, indent=2))
