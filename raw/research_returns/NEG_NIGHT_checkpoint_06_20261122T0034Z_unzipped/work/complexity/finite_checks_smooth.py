"""Finite arithmetic checks for NN-C024; no claim to verify sheaf theory or E.

Uses independent exact finite-field arithmetic to check the quadratic tower,
semilinear iteration, and the small cubic instances of the Jacobian-minor and
projective point-parity identities. The Macaulay implication over an algebraic
closure is proved in the text, not certified by enumerating finite points.
"""
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import json


@dataclass
class Field:
    degree: int
    sub: object = None
    constant: int = 0

    @property
    def size(self):
        return 1 << self.degree

    def mul(self, x, y):
        if self.degree == 1:
            return x & y
        d = self.sub.degree
        mask = (1 << d) - 1
        x0, x1 = x & mask, x >> d
        y0, y1 = y & mask, y >> d
        t = self.sub.mul(x1, y1)
        lo = self.sub.mul(x0, y0) ^ self.sub.mul(self.constant, t)
        hi = self.sub.mul(x0, y1) ^ self.sub.mul(x1, y0) ^ t
        return lo ^ (hi << d)

    def power(self, x, n):
        ans = 1
        while n:
            if n & 1:
                ans = self.mul(ans, x)
            x = self.mul(x, x)
            n >>= 1
        return ans

    def trace(self, x):
        ans = 0
        for _ in range(self.degree):
            ans ^= x
            x = self.mul(x, x)
        assert ans in (0, 1)
        return ans

    def extend(self):
        a = next(1 << i for i in range(self.degree)
                 if self.trace(1 << i) == 1)
        return Field(2 * self.degree, self, a)


def binary_rank(vectors):
    pivots = {}
    for v in vectors:
        while v:
            i = v.bit_length() - 1
            if i in pivots:
                v ^= pivots[i]
            else:
                pivots[i] = v
                break
    return len(pivots)


def monomials(degree, variables=3):
    if variables == 1:
        yield (degree,)
    else:
        for first in range(degree + 1):
            for rest in monomials(degree-first, variables-1):
                yield (first,) + rest


def evaluate(poly, point, field):
    value = 0
    for exponents, coefficient in poly.items():
        term = coefficient
        for x, exponent in zip(point, exponents):
            term = field.mul(term, field.power(x, exponent))
        value ^= term
    return value


def derivative(poly, i):
    ans = {}
    for exponents, coefficient in poly.items():
        if exponents[i] & 1:
            e = list(exponents)
            e[i] -= 1
            e = tuple(e)
            ans[e] = ans.get(e, 0) ^ coefficient
    return {e: c for e, c in ans.items() if c}


def determinant(matrix, field):
    matrix = [row[:] for row in matrix]
    ans = 1
    for column in range(len(matrix)):
        pivot = next((i for i in range(column, len(matrix))
                      if matrix[i][column]), None)
        if pivot is None:
            return 0
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        entry = matrix[column][column]
        ans = field.mul(ans, entry)
        inv = field.power(entry, field.size - 2)
        for i in range(column + 1, len(matrix)):
            ratio = field.mul(matrix[i][column], inv)
            for j in range(column, len(matrix)):
                matrix[i][j] ^= field.mul(ratio, matrix[column][j])
    return ans


def macaulay_matrix(poly):
    basis = list(monomials(4))
    lookup = {e: i for i, e in enumerate(basis)}
    deriv = [derivative(poly, i) for i in range(3)]
    rows = []
    for e in basis:
        i = next(i for i, exponent in enumerate(e) if exponent >= 2)
        quotient = list(e)
        quotient[i] -= 2
        row = [0] * len(basis)
        for f, coefficient in deriv[i].items():
            target = tuple(x+y for x, y in zip(quotient, f))
            row[lookup[target]] ^= coefficient
        rows.append(row)
    return rows


def projective_points(field):
    for i in range(3):
        for tail in product(range(field.size), repeat=2-i):
            yield (0,) * i + (1,) + tail


def run():
    fields = [Field(1)]
    while fields[-1].degree < 16:
        fields.append(fields[-1].extend())
    totals = {'tower_basis_tests': 0, 'semilinear_iteration_tests': 0,
              'cubic_parameter_tests': 0, 'macaulay_nonzero_tests': 0,
              'projective_points_checked': 0}
    for field in fields:
        for i in range(field.degree):
            assert field.trace(1 << i) in (0, 1)
            totals['tower_basis_tests'] += 1
        assert any(field.trace(1 << i) for i in range(field.degree))
        if field.sub:
            theta = 1 << field.sub.degree
            assert field.mul(theta, theta) ^ theta ^ field.constant == 0
            powers = [field.power(theta, i) for i in range(field.degree)]
            assert binary_rank(powers) == field.degree
            if field.sub.size <= 256:
                assert all(field.sub.mul(y, y) ^ y ^ field.constant
                           for y in range(field.sub.size))
        parameters = range(1, field.size) if field.size <= 256 else range(1, 65)
        for a in parameters:
            for c in (0, 1):
                coefficient = 1
                ac = a if c else 0
                for _ in range(field.degree):
                    coefficient = field.mul(ac, field.mul(coefficient, coefficient))
                assert coefficient == c
                totals['semilinear_iteration_tests'] += 1

    # These include the one-variable clause gadget, the tautological gadget,
    # and both cubic edge-case replacements of C023.
    examples = [
        {(1,1,1): 1},
        {(1,2,0): 1, (1,1,1): 1},
        {(1,2,0): 1, (1,0,2): 1},
        {(0,3,0): 1},
    ]
    for field in (fields[1], fields[2]):  # F4 and F16
        for f in examples:
            c = f.get((1,1,1), 0)
            for a in range(field.size):
                poly = {(3,0,0): 1, (0,3,0): 1, (0,0,3): 1}
                for e, coefficient in f.items():
                    poly[e] = poly.get(e, 0) ^ field.mul(a, coefficient)
                matrix = macaulay_matrix(poly)
                if a == 0:
                    assert matrix == [[int(i == j) for j in range(15)]
                                      for i in range(15)]
                minor = determinant(matrix, field)
                deriv = [derivative(poly, i) for i in range(3)]
                points = 0
                for point in projective_points(field):
                    points += evaluate(poly, point, field) == 0
                    if minor:
                        assert any(evaluate(g, point, field) for g in deriv)
                    totals['projective_points_checked'] += 1
                assert points % 2 == (1 ^ (c if a else 0))
                totals['cubic_parameter_tests'] += 1
                totals['macaulay_nonzero_tests'] += bool(minor)
    out = {'finding': 'NN-C024', 'status': 'all assertions passed',
           'fields_degrees': [f.degree for f in fields], 'totals': totals,
           'limits': 'Finite arithmetic examples only. No sheaf-cohomology, algebraic-closure smoothness, input theorem E, or general complexity-class implication is mechanically verified.'}
    path = Path(__file__).with_name('FINITE_CHECK_SMOOTH_RESULTS.json')
    path.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    run()
