#!/usr/bin/env python3
"""Exact finite certificates for the local fierce extensions in characteristic p.

The proof for all prime powers is algebraic.  These calculations independently
check the finite-field actions and Jacobian identities for six concrete q.
"""
import json
import time
from collections import deque
from pathlib import Path

from sympy.polys.domains import GF
from sympy.polys.fields import field

started = time.perf_counter()
assertions = 0


def check(condition):
    global assertions
    assertions += 1
    assert condition


class FiniteField:
    def __init__(self, p, modulus):
        self.p = p
        self.modulus = modulus
        self.m = len(modulus) - 1
        self.q = p ** self.m
        self.digits = [self.decode(a) for a in range(self.q)]
        self.add = [[self.encode([(x + y) % p for x, y in zip(
            self.digits[a], self.digits[b])]) for b in range(self.q)]
            for a in range(self.q)]
        self.mul = [[self.multiply(a, b) for b in range(self.q)]
                    for a in range(self.q)]

    def decode(self, a):
        result = []
        for _ in range(self.m):
            result.append(a % self.p)
            a //= self.p
        return result

    def encode(self, coefficients):
        return sum(a * self.p ** i for i, a in enumerate(coefficients))

    def multiply(self, a, b):
        p, m = self.p, self.m
        coefficients = [0] * (2 * m - 1)
        for i, x in enumerate(self.digits[a]):
            for j, y in enumerate(self.digits[b]):
                coefficients[i + j] = (coefficients[i + j] + x * y) % p
        for degree in range(2 * m - 2, m - 1, -1):
            leading = coefficients[degree]
            for i in range(m):
                coefficients[degree - m + i] = (
                    coefficients[degree - m + i] - leading * self.modulus[i]
                ) % p
        return self.encode(coefficients[:m])

    def power(self, a, n):
        result = 1
        while n:
            if n & 1:
                result = self.mul[result][a]
            a = self.mul[a][a]
            n >>= 1
        return result


cases = [(2, [0, 1]), (3, [0, 1]), (2, [1, 1, 1]),
         (5, [0, 1]), (2, [1, 1, 0, 1]), (3, [1, 0, 1])]
results = []
for p, modulus in cases:
    ff = FiniteField(p, modulus)
    q, add, mul = ff.q, ff.add, ff.mul
    begin_count = assertions
    for a in range(q):
        check(ff.power(a, q) == a)
        check(add[a][0] == a and mul[a][1] == a)
        if a:
            check(ff.power(a, q - 1) == 1)
        for b in range(q):
            check(add[a][b] == add[b][a] and mul[a][b] == mul[b][a])
            for c in range(q):
                check(add[add[a][b]][c] == add[a][add[b][c]])
                check(mul[mul[a][b]][c] == mul[a][mul[b][c]])
                check(mul[a][add[b][c]] == add[mul[a][b]][mul[a][c]])

    # g=(a,b,c) acts on an affine plane by (w,y) -> (cw+a,cy+b).
    group = [(a, b, c) for a in range(q) for b in range(q)
             for c in range(1, q)]
    identity = (0, 0, 1)

    def product(g, h):
        a, b, c = g
        x, y, z = h
        return (add[a][mul[c][x]], add[b][mul[c][y]], mul[c][z])

    def action(g, point):
        a, b, c = g
        w, y = point
        return (add[mul[c][w]][a], add[mul[c][y]][b])

    check(len({tuple(action(g, point) for point in [(0, 0), (1, 0), (0, 1)])
               for g in group}) == len(group))
    basis = [p ** i for i in range(ff.m)]
    generators = [(a, 0, 1) for a in basis] + [(0, b, 1) for b in basis]
    generators += [(0, 0, c) for c in range(1, q)]
    reached = {identity}
    queue = deque([identity])
    while queue:
        g = queue.popleft()
        for h in generators:
            gh = product(g, h)
            if gh not in reached:
                reached.add(gh)
                queue.append(gh)
    check(len(reached) == q * q * (q - 1))
    for g in group:
        a, b, c = g
        ci = ff.power(c, q - 2)
        neg_a = ff.encode([(-x) % p for x in ff.digits[a]])
        neg_b = ff.encode([(-x) % p for x in ff.digits[b]])
        gi = (mul[ci][neg_a], mul[ci][neg_b], ci)
        check(product(g, gi) == identity and product(gi, g) == identity)
        for h in generators:
            gh = product(g, h)
            for w in range(q):
                for y in range(q):
                    check(action(gh, (w, y)) == action(g, action(h, (w, y))))

    # Rational identities over the prime field; all q-power formulas persist
    # over its algebraic closure and contain the chosen finite field F_q.
    fraction_field, pi, u = field('pi,u', GF(p))
    denominator = 1 - pi ** (q - 1)
    s = pi ** q / denominator
    z = (u ** q - pi ** (q - 1) * u) / denominator
    t = s ** (q - 1)
    w, y = 1 / pi, u / pi
    check(not (w ** q - w - 1 / s))
    check(not (y ** q - y - z / s))
    check(not (s.diff(pi) + pi ** (2 * q - 2) / denominator ** 2))
    check(not (t.diff(pi) - pi ** (q * q - 2) / denominator ** q))
    check(not (z.diff(u) + pi ** (q - 1) / denominator))
    jacobian = t.diff(pi) * z.diff(u) - t.diff(u) * z.diff(pi)
    delta = q * q + q - 3
    check(not (jacobian + pi ** delta / denominator ** (q + 1)))
    check(min(exponents[0] for exponents in jacobian.numer.monoms()) == delta)
    check(min(exponents[0] for exponents in jacobian.denom.monoms()) == 0)
    e = q * (q - 1)
    check(delta - e + 1 == 2 * (q - 1))
    results.append({'p': p, 'q': q, 'finite_field_modulus': modulus,
                    'galois_group_order': q * q * (q - 1),
                    'ramification_index': e,
                    'inseparable_residue_degree': q,
                    'different_exponent': delta,
                    'normalized_excess': f'2/{q}',
                    'assertions': assertions - begin_count})

output = {'status': 'passed', 'assertions': assertions,
          'elapsed_seconds': time.perf_counter() - started, 'cases': results,
          'scope': 'Exact finite-field actions and rational Jacobian identities; '
                   'the local extension and all-prime-power assertions are '
                   'proved separately in the accompanying TeX fragment.'}
destination = Path(__file__).resolve().parents[1] / 'output' / 'fierce_different_certificate.json'
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
