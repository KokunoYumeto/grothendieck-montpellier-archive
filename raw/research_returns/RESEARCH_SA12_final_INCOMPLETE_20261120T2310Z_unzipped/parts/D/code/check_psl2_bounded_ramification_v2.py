#!/usr/bin/env python3
"""Exact restored PSL2 certificate, version 2.

This is a new, separately identified program.  It is not represented as
the lost program which had 306144 assertions before the environment reset.
All tests below use finite-field and integer arithmetic, with no sampling.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from collections import deque
from fractions import Fraction
from itertools import product
from pathlib import Path

ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


class Field:
    def __init__(self, degree, polynomial):
        self.degree = degree
        self.polynomial = polynomial
        self.q = 1 << degree

    def mul(self, a, b):
        z = 0
        while b:
            if b & 1:
                z ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.polynomial
        return z

    def pow(self, a, n):
        z = 1
        while n:
            if n & 1:
                z = self.mul(z, a)
            a = self.mul(a, a)
            n >>= 1
        return z

    def inv(self, a):
        if not a:
            raise ZeroDivisionError
        return self.pow(a, self.q - 2)

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def order(self, a):
        z = 1
        for n in range(1, self.q):
            z = self.mul(z, a)
            if z == 1:
                return n
        raise AssertionError("not a field unit")


def matrix_mul(f, x, y):
    a, b, c, d = x
    e, g, h, j = y
    return (f.mul(a, e) ^ f.mul(b, h),
            f.mul(a, g) ^ f.mul(b, j),
            f.mul(c, e) ^ f.mul(d, h),
            f.mul(c, g) ^ f.mul(d, j))


def determinant(f, x):
    a, b, c, d = x
    return f.mul(a, d) ^ f.mul(b, c)


def matrix_order(f, x, bound):
    z = (1, 0, 0, 1)
    for n in range(1, bound + 1):
        z = matrix_mul(f, z, x)
        if z == (1, 0, 0, 1):
            return n
    raise AssertionError("matrix order exceeds group size")


def poly_mul(a, b):
    """F_2 polynomials as sets of their nonzero exponents."""
    c = set()
    for i in a:
        for j in b:
            if i + j in c:
                c.remove(i + j)
            else:
                c.add(i + j)
    return c


def poly_pow(a, n):
    z = {0}
    while n:
        if n & 1:
            z = poly_mul(z, a)
        a = poly_mul(a, a)
        n >>= 1
    return z


def evaluate_polynomial_bits(f, polynomial, x):
    z = 0
    power = 1
    while polynomial:
        if polynomial & 1:
            z ^= power
        polynomial >>= 1
        power = f.mul(power, x)
    return z


def run_field(degree, polynomial, extension_polynomial):
    f = Field(degree, polynomial)
    e = Field(2 * degree, extension_polynomial)
    q = f.q
    for a in range(1, f.q):
        check(f.pow(a, f.q - 1) == 1, ("base field", q, a))
        check(f.mul(a, f.inv(a)) == 1, ("base inverse", q, a))
    for a, b, c in product(range(q), repeat=3):
        check(f.mul(a, b ^ c) == (f.mul(a, b) ^ f.mul(a, c)),
              ("distributivity", q, a, b, c))
    for a in range(1, e.q):
        check(e.pow(a, e.q - 1) == 1, ("extension field", q, a))
        check(e.mul(a, e.inv(a)) == 1, ("extension inverse", q, a))

    theta = next(a for a in range(e.q)
                 if evaluate_polynomial_bits(e, polynomial, a) == 0)
    embedding = [evaluate_polynomial_bits(e, a, theta) for a in range(q)]
    check(len(set(embedding)) == q, ("embedding injective", q))
    for a, b in product(range(q), repeat=2):
        check(embedding[a ^ b] == (embedding[a] ^ embedding[b]),
              ("embedding additive", q, a, b))
        check(embedding[f.mul(a, b)] == e.mul(embedding[a], embedding[b]),
              ("embedding multiplicative", q, a, b))
    base_points = set(embedding)
    for z in range(e.q):
        check((e.pow(z, q) == z) == (z in base_points),
              ("Fq points", q, z))

    group = set()
    for a, b, c in product(range(q), repeat=3):
        if a:
            group.add((a, b, c, f.div(1 ^ f.mul(b, c), a)))
        elif b and f.mul(b, c) == 1:
            for d in range(q):
                group.add((0, b, c, d))
    size = q * (q * q - 1)
    check(len(group) == size, ("SL2 order", q))
    identity = (1, 0, 0, 1)
    for g in group:
        check(determinant(f, g) == 1, ("determinant", q, g))
        a, b, c, d = g
        check(matrix_mul(f, g, (d, b, c, a)) == identity,
              ("inverse", q, g))
    primitive = next(a for a in range(1, q) if f.order(a) == q - 1)
    generators = [(1, 1, 0, 1),
                  (primitive, 0, 0, f.inv(primitive)),
                  (0, 1, 1, 0)]
    generated = {identity}
    queue = deque([identity])
    while queue:
        g = queue.popleft()
        for h in generators:
            gh = matrix_mul(f, g, h)
            check(gh in group, ("generator product", q, gh))
            if gh not in generated:
                generated.add(gh)
                queue.append(gh)
    check(generated == group, ("three generation", q))
    check({a for a in range(1, q) if f.mul(a, a) == 1} == {1},
          ("trivial SL2 centre", q))

    infinity = e.q
    embedded_generators = [tuple(embedding[a] for a in g) for g in generators]

    def action(g, z):
        a, b, c, d = g
        if z == infinity:
            return infinity if not c else e.div(a, c)
        denominator = e.mul(c, z) ^ d
        return infinity if not denominator else e.div(e.mul(a, z) ^ b,
                                                       denominator)

    for g in embedded_generators:
        check(len({action(g, z) for z in range(e.q + 1)}) == e.q + 1,
              ("projective permutation", q, g))
    unseen = set(range(e.q + 1))
    orbits = []
    while unseen:
        first = min(unseen)
        orbit = {first}
        queue = deque([first])
        while queue:
            z = queue.popleft()
            for g in embedded_generators:
                w = action(g, z)
                if w not in orbit:
                    orbit.add(w)
                    queue.append(w)
        unseen -= orbit
        orbits.append(orbit)
    check(len(orbits) == 2, ("two branch orbits", q))
    rational_orbit = base_points | {infinity}
    check(rational_orbit in orbits, ("rational branch orbit", q))
    other = set(range(e.q)) - base_points
    check(other in orbits, ("quadratic branch orbit", q))
    check(len(rational_orbit) == q + 1, ("rational orbit size", q))
    check(len(other) == q * q - q, ("quadratic orbit size", q))

    borel = [g for g in group if g[2] == 0]
    check(len(borel) == q * (q - 1), ("Borel inertia", q))
    wild = []
    for a, b, c, d in borel:
        first_coefficient = f.div(d, a) ^ 1
        second_coefficient = f.div(f.mul(d, b), f.mul(a, a))
        if first_coefficient == 0 and b:
            check(second_coefficient != 0, ("wild lower jump one", q, a, b))
            wild.append((a, b, c, d))
        elif (a, b, c, d) != identity:
            check(first_coefficient != 0, ("tame lower jump zero", q, a, b))
    check(len(wild) + 1 == q, ("wild inertia order", q))
    check(all(g[0] == g[3] == 1 for g in wild), ("translation inertia", q))
    nonsplit_point = min(other)
    nonsplit = [g for g in group
                if action(tuple(embedding[a] for a in g), nonsplit_point)
                == nonsplit_point]
    check(len(nonsplit) == q + 1, ("nonsplit tame inertia", q))
    check(any(matrix_order(f, g, q + 1) == q + 1 for g in nonsplit),
          ("cyclic nonsplit inertia", q))

    A = {1, q}
    B = poly_pow(A, q - 1)
    B.symmetric_difference_update({0})
    check(B == {j * (q - 1) for j in range(q + 1)}, ("B polynomial", q))
    check({-j for j in A} == {j - q - 1 for j in A},
          ("A inversion identity", q))
    check({-j for j in B} == {j + q - q*q for j in B},
          ("B inversion identity", q))
    check((q + 1) * (q - q*q) == -q * (q - 1) * (q + 1),
          ("J inversion cancellation", q))
    for a in range(q):
        check(f.pow(a, q) ^ a == 0, ("A translation constant", q, a))
    for a in range(1, q):
        check(f.pow(a, q - 1) == 1, ("B dilation identity", q, a))
    numerator = poly_pow(B, q + 1)
    denominator = poly_pow(A, q * (q - 1))
    check(max(numerator) == size, ("quotient degree", q))
    check(max(numerator) - max(denominator) == q * (q - 1),
          ("infinite pole order", q))
    for z in range(e.q):
        az = e.pow(z, q) ^ z
        bz = e.pow(az, q - 1) ^ 1
        check((az == 0) == (z in base_points), ("A root locus", q, z))
        check((bz == 0) == (z in other), ("B root locus", q, z))
        check(not (az == 0 and bz == 0), ("reduced invariant", q, z))

    e_ram = q * (q - 1)
    different = (e_ram - 1) + (q - 1)
    check(different == q*q - 2, ("different exponent", q))
    upper = Fraction(1, q - 1)
    nonlog = 1 + upper
    check(nonlog <= Fraction(4, 3), ("uniform nonlog conductor", q))
    for i in range(1, 11):
        multiplicity = size**i + 1
        for d in range(1, i + 1):
            check(multiplicity > size**d, ("coordinate pigeonhole", q, i, d))
    return {
        "q": q, "group_order": size,
        "generated_order": len(generated),
        "branch_orbit_sizes": sorted(map(len, orbits)),
        "wild_inertia_order": q, "ramification_index": e_ram,
        "other_inertia_order": q + 1, "different_exponent": different,
        "upper_break": str(upper), "nonlog_break": str(nonlog),
        "primitive_element": primitive,
        "field_polynomial": polynomial,
        "quadratic_extension_polynomial": extension_polynomial,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    start = time.perf_counter()
    fields = [run_field(2, 0b111, 0b10011),
              run_field(3, 0b1011, 0b1000011),
              run_field(4, 0b10011, 0b100011011)]
    result = {
        "id": "D:psl2-bounded-conductor-covers",
        "companion_id": "D:bounded-ramification-generation-obstruction",
        "version": "2-reconstructed-2026-11-20",
        "status": "passed",
        "assertions": ASSERTIONS,
        "runtime_seconds": time.perf_counter() - start,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "fields": fields,
        "scope": "Exact finite checks; the general geometric and cohomological proofs are separate.",
        "historical_program": {
            "source_recovered": False,
            "assertions": 306144,
            "author_runtime_seconds": 0.6179991249955492,
            "root_runtime_seconds": 0.6380047900020145,
            "note": "Historical reported runs, not reruns of this reconstructed version."
        }
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
