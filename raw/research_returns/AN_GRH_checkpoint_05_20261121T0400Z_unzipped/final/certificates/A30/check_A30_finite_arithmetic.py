#!/usr/bin/env python3
"""Exact finite consistency checks for A30; not a formal proof checker.

Uses only the Python standard library.  The geometric Lang and Euler-factor
proof is read separately; this program checks its displayed small-field
inputs and polynomial consequences by direct finite arithmetic.
"""

import hashlib
import json
from pathlib import Path


class BinaryField:
    def __init__(self, degree, modulus):
        self.degree = degree
        self.modulus = modulus
        self.order = 1 << degree
        assert modulus.bit_length() == degree + 1
        # Exhaustive finite check that this quotient is a field.
        assert all(self.power(a, self.order - 1) == 1
                   for a in range(1, self.order))

    def multiply(self, a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            b >>= 1
            a <<= 1
            if a & self.order:
                a ^= self.modulus
        return result

    def power(self, a, n):
        result = 1
        while n:
            if n & 1:
                result = self.multiply(result, a)
            a = self.multiply(a, a)
            n >>= 1
        return result

    def inverse(self, a):
        assert a
        return self.power(a, self.order - 2)

    def divide(self, a, b):
        return self.multiply(a, self.inverse(b))


F4 = BinaryField(2, 0b111)
O = None


def elliptic_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 != y2:
        return O
    if P == Q:
        slope = F4.power(x1, 2)
    else:
        slope = F4.divide(y1 ^ y2, x1 ^ x2)
    x3 = F4.power(slope, 2) ^ x1 ^ x2
    y3 = F4.multiply(slope, x1 ^ x3) ^ y1 ^ 1
    return x3, y3


def elliptic_scale(P, n):
    result = O
    for _ in range(n):
        result = elliptic_add(result, P)
    return result


points = [O] + [(x, y) for x in range(4) for y in range(4)
                if F4.power(y, 2) ^ y == F4.power(x, 3)]
assert len(points) == 9
assert all(elliptic_scale(P, 3) is O for P in points)
assert all(elliptic_add(elliptic_add(P, Q), R)
           == elliptic_add(P, elliptic_add(Q, R))
           for P in points for Q in points for R in points)

# The tangent at (a,c) gives v^3 after x=a+v, as a polynomial identity.
assert all(F4.power(a, 4) == a for a in range(4))
for a, c in points[1:]:
    # Coefficients of (c+a^2*v)^2 + (c+a^2*v) + (a+v)^3.
    coefficients = [F4.power(c, 2) ^ c ^ F4.power(a, 3),
                    F4.power(a, 2) ^ F4.power(a, 2),
                    F4.power(a, 4) ^ a, 1]
    assert coefficients == [0, 0, 0, 1]

Q = (0, 0)
R = (1, 2)  # 2 denotes omega, omega^2+omega+1=0.
coordinates = {}
for i in range(3):
    for j in range(3):
        P = elliptic_add(elliptic_scale(Q, i), elliptic_scale(R, j))
        assert P not in coordinates
        coordinates[P] = (i, j)
assert set(coordinates) == set(points)
detector = {P: coordinates[P][0] for P in points}
assert detector[Q] == 1
assert all(detector[elliptic_add(P, S)]
           == (detector[P] + detector[S]) % 3
           for P in points for S in points)
minus_Q = elliptic_scale(Q, 2)
assert detector[elliptic_add(minus_Q, minus_Q)] == 1
assert detector[minus_Q] == 2


def translation_cycle_lengths(shift):
    unseen = set(range(3))
    lengths = []
    while unseen:
        start = min(unseen)
        v = start
        length = 0
        while v in unseen:
            unseen.remove(v)
            v = (v + shift) % 3
            length += 1
        assert v == start
        lengths.append(length)
    return lengths


assert translation_cycle_lengths(0) == [1, 1, 1]
assert translation_cycle_lengths(1) == [3]
assert translation_cycle_lengths(2) == [3]


def curve_counts(F):
    E_count = 1
    for x in range(F.order):
        E_count += sum(F.power(y, 2) ^ y == F.power(x, 3)
                       for y in range(F.order))
    # D has one point at each of its poles t=0,1, and two at infinity.
    D_count = 4
    for t in range(F.order):
        denominator = F.power(t, 2) ^ t
        if denominator:
            value = F.inverse(F.power(denominator, 3))
            D_count += sum(F.power(z, 2) ^ z == value
                           for z in range(F.order))
    return E_count, D_count


fields = [F4, BinaryField(4, 0b10011), BinaryField(6, 0b1000011)]
counts = [curve_counts(F) for F in fields]
traces_D = [4**m + 1 - counts[m - 1][1] for m in range(1, 4)]
coefficients_D = [1]
for m in range(1, 4):
    numerator = -sum(coefficients_D[m - i] * traces_D[i - 1]
                     for i in range(1, m + 1))
    assert numerator % m == 0
    coefficients_D.append(numerator // m)
coefficients_D.extend([4 * coefficients_D[2],
                       16 * coefficients_D[1], 64])
assert [c % 2 for c in coefficients_D] == [1, 1, 0, 0, 0, 0, 0]


def polynomial_multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] ^= F4.multiply(a, b)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


one_minus_T = [1, 1]
one_minus_T3 = [1, 0, 0, 1]
chi = polynomial_multiply(one_minus_T, [1, 2])
chi_inverse = polynomial_multiply(one_minus_T, [1, 3])
relative = polynomial_multiply(chi, chi_inverse)
assert chi == [1, 3, 2]
assert chi_inverse == [1, 2, 3]
assert relative == polynomial_multiply(one_minus_T, one_minus_T3)
assert relative == [1, 1, 0, 1, 1]
assert sum(relative) % 2 == 0
upstairs = polynomial_multiply(one_minus_T, relative)
assert upstairs == [1, 0, 1, 1, 0, 1]

source = Path(__file__).with_name("A30_GENUS_THREE_POINTING_COUNTEREXAMPLE.tex")
result = {
    "status": "PASS",
    "scope": "Exact finite arithmetic consistency checks; the geometric proof is separately read, not formally verified.",
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "F4_convention": "omega=2, omega^2=3, omega^2+omega+1=0",
    "elliptic_points": ["O" if P is None else list(P) for P in points],
    "group_structure": "C3 x C3; exhaustive addition and associativity check passed",
    "basis_Q_R": [list(Q), list(R)],
    "a_Q": detector[Q],
    "a_minus_Q_minus_Q": detector[elliptic_add(minus_Q, minus_Q)],
    "a_minus_Q": detector[minus_Q],
    "branch_fibre_closed_degrees": {"Q": [1, 1, 1], "minus_Q": [3]},
    "point_counts_over_F4_power_m": [
        {"m": m, "field_order": 4**m, "E": e, "D": d}
        for m, (e, d) in enumerate(counts, start=1)],
    "H_D_coefficients_ascending": coefficients_D,
    "L_chi_mod2_coefficients_ascending_in_F4": chi,
    "L_chi_inverse_mod2_coefficients_ascending_in_F4": chi_inverse,
    "H_primitive_mod2_coefficients_ascending": relative,
    "H_upstairs_mod2_coefficients_ascending": upstairs,
    "primitive_class_number_parity": 0,
}
target = Path(__file__).with_name("A30_FINITE_ARITHMETIC.json")
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
