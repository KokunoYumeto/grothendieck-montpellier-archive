"""Independent finite arithmetic checks for the PN reconstruction.

Methods: direct projective-point enumeration, sparse polynomial multiplication,
semilinear matrix composition over F_4, and Euclidean gcd of Deuring polynomials.
No authored/source program has been opened.  Finite checks do not prove the
unresolved full-group statements, and no smoothness certification is attempted.
"""
import json
from itertools import product
from math import comb
from random import Random


class Field:
    def __init__(self, q):
        self.q = q
        self.p = 2 if q == 4 else q
        self.r = 2 if q == 4 else 1

    def add(self, a, b):
        return a ^ b if self.q in (2, 4) else (a + b) % self.q

    def neg(self, a):
        return a if self.q in (2, 4) else (-a) % self.q

    def mul(self, a, b):
        if self.q != 4:
            return (a * b) % self.q
        out = 0
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 7  # F_2[t]/(t^2+t+1)
        return out

    def power(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def total(self, values):
        out = 0
        for a in values:
            out = self.add(out, a)
        return out


def compositions(d, r, positive=False):
    if positive:
        return [tuple(z + 1 for z in a) for a in compositions(d - r, r)] if d >= r else []
    if r == 1:
        return [(d,)]
    return [(i,) + a for i in range(d + 1) for a in compositions(d - i, r - 1)]


def poly_mul(f, g, field):
    out = {}
    for a, u in f.items():
        for b, v in g.items():
            exponent = tuple(x + y for x, y in zip(a, b))
            out[exponent] = field.add(out.get(exponent, 0), field.mul(u, v))
    return {a: u for a, u in out.items() if u}


def poly_power(f, power, variables, field):
    out = {(0,) * variables: 1}
    for _ in range(power):
        out = poly_mul(out, f, field)
    return out


def poly_eval(f, point, field):
    out = 0
    for exponent, coefficient in f.items():
        value = coefficient
        for x, power in zip(point, exponent):
            value = field.mul(value, field.power(x, power))
        out = field.add(out, value)
    return out


def projective_points(n, q):
    for first in range(n + 1):
        for tail in product(range(q), repeat=n - first):
            yield (0,) * first + (1,) + tail


def matrix_for(power_poly, exponent_power, indices):
    return [[power_poly.get(tuple(exponent_power * x - y for x, y in zip(a, b)), 0)
             for a in indices] for b in indices]


def matrix_mul(a, b, field):
    h = len(a)
    return [[field.total(field.mul(a[i][k], b[k][j]) for k in range(h))
             for j in range(h)] for i in range(h)]


def matrix_rank(a, field):
    a = [row[:] for row in a]
    h = len(a)
    row = 0
    for column in range(h):
        pivot = next((i for i in range(row, h) if a[i][column]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inverse = field.power(a[row][column], field.q - 2)
        a[row] = [field.mul(x, inverse) for x in a[row]]
        for i in range(row + 1, h):
            factor = a[i][column]
            a[i] = [field.add(x, field.neg(field.mul(factor, y)))
                    for x, y in zip(a[i], a[row])]
        row += 1
    return row


def check_covector(f, n, d, field):
    indices = compositions(d, n + 1, True)
    matrix = matrix_for(f, 2, indices)
    xi = [f.get(a, 0) if all(x % 2 for x in a) else 0 for a in indices]
    left = [field.total(field.mul(matrix[b][a], xi[b]) for b in range(len(indices)))
            for a in range(len(indices))]
    assert left == [field.power(x, 2) for x in xi]
    ordinary = matrix_rank(matrix, field) == len(indices)
    assert not ordinary or any(xi)
    return ordinary


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def remainder(a, b, p):
    a = a[:]
    while len(a) >= len(b) and a:
        factor = a[-1] * pow(b[-1], -1, p) % p
        shift = len(a) - len(b)
        for i, coefficient in enumerate(b):
            a[shift + i] = (a[shift + i] - factor * coefficient) % p
        trim(a)
    return a


def main():
    rng = Random(202611230828)
    cases = ([(2, 2, d, 16) for d in range(2, 8)]
             + [(3, 2, d, 12) for d in range(2, 6)]
             + [(4, 2, d, 12) for d in range(2, 6)]
             + [(5, 2, d, 8) for d in range(2, 5)]
             + [(2, 3, d, 12) for d in range(2, 6)]
             + [(4, 3, d, 8) for d in range(3, 5)])
    records = []
    point_checks = iteration_checks = covector_checks = 0
    for q, n, d, samples in cases:
        field = Field(q)
        monomials = compositions(d, n + 1)
        indices = compositions(d, n + 1, True)
        points = list(projective_points(n, q))
        for _ in range(samples):
            f = {a: rng.randrange(q) for a in monomials}
            f = {a: u for a, u in f.items() if u}
            count = sum(poly_eval(f, x, field) == 0 for x in points)
            polynomial = poly_power(f, q - 1, n + 1, field)
            matrix_q = matrix_for(polynomial, q, indices)
            trace = field.total(matrix_q[i][i] for i in range(len(indices)))
            sign_trace = trace if (n - 1) % 2 == 0 else field.neg(trace)
            residue = field.add(1, sign_trace)
            assert residue == count % field.p
            point_checks += 1
            matrix_p = matrix_for(poly_power(f, field.p - 1, n + 1, field), field.p, indices)
            composed = matrix_p
            for step in range(1, field.r):
                twist = [[field.power(x, field.p ** step) for x in row] for row in matrix_p]
                composed = matrix_mul(composed, twist, field)
            assert composed == matrix_q
            iteration_checks += 1
            if field.p == 2 and d >= n + 1 and (d - n - 1) % 2 == 0:
                check_covector(f, n, d, field)
                covector_checks += 1
        records.append({"q": q, "n": n, "d": d, "samples": samples})

    extra_covectors = []
    for n, d in [(2, 7), (3, 6), (4, 7)]:
        field = Field(4)
        monomials = compositions(d, n + 1)
        ordinary = 0
        for _ in range(32):
            f = {a: rng.randrange(4) for a in monomials}
            ordinary += check_covector(f, n, d, field)
            covector_checks += 1
        extra_covectors.append({"q": 4, "n": n, "d": d, "samples": 32,
                                 "ordinary": ordinary})

    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
              47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    deuring = []
    for p in primes:
        m = (p - 1) // 2
        coefficients = [comb(m, i) ** 2 % p for i in range(m + 1)]
        derivative = [i * coefficients[i] % p for i in range(1, m + 1)]
        a, b = coefficients[:], trim(derivative)
        while b:
            a, b = b, remainder(a, b, p)
        assert len(a) == 1
        assert coefficients[0] and sum(coefficients) % p
        deuring.append({"p": p, "degree": m, "gcd_with_derivative_degree": 0})

    distinct_locations = []
    for n in range(2, 17):
        d = n + 2
        indices = compositions(d, n + 1, True)
        locations = [tuple(2 * x - y for x, y in zip(a, b))
                     for b in indices for a in indices]
        assert len(set(locations)) == (n + 1) ** 2
        assert all(min(a) >= 0 and sum(a) == d for a in locations)
        assert (d,) + (0,) * n not in locations
        distinct_locations.append({"n": n, "d": d, "distinct_entries": len(locations)})

    print(json.dumps({"seed": 202611230828,
                      "scope": "Formula checks only; no smoothness or full-monodromy certification",
                      "projective_point_checks": point_checks,
                      "semilinear_iteration_checks": iteration_checks,
                      "covector_identity_checks": covector_checks,
                      "point_cases": records, "extra_covector_cases": extra_covectors,
                      "deuring_gcd_checks": deuring,
                      "minimal_matrix_location_checks": distinct_locations}, indent=2))


if __name__ == "__main__":
    main()
