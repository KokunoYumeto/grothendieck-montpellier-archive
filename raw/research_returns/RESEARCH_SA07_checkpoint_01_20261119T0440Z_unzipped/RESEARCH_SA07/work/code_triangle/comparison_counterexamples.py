#!/usr/bin/env python3
"""Exact finite checks for Part B; no numerical transcendence inference.

Input: C2 written additively; H={+1,-1}; E=H x C2.
Also F4=F2[a]/(a^2+a+1), and the Hensel root of x^2-6,
congruent to 1 modulo 5, through modulus 5^12.
All arithmetic is exact Python integer arithmetic.  No external package.
"""
from itertools import product
from fractions import Fraction


def mul(x, y):
    return (x[0] * y[0], (x[1] + y[1]) % 2)


def inverse(x):
    return x  # both factors have exponent two


def section_test(f):
    return all(f((g + h) % 2) == mul(f(g), f(h))
               for g, h in product(range(2), repeat=2))


def check_example(chi, u, sigma2, compatibility_expected):
    sigma1 = lambda g: (1, g)
    phi = lambda g: mul(inverse(sigma1(g)), sigma2(g))[0]
    assert section_test(sigma1) and section_test(sigma2)
    modified1 = lambda g: mul(sigma1(g), (u(g), 0))
    modified2 = lambda g: mul(sigma2(g), (chi(g), 0))
    assert section_test(modified1) and section_test(modified2)
    compatible = all(modified1(g) == modified2(g) for g in range(2))
    assert compatible == compatibility_expected
    for g, h in product(range(2), repeat=2):
        # H is central, so the right-cocycle law is multiplicative here.
        assert phi((g + h) % 2) == phi(g) * phi(h)
    kernels = {
        "u": [g for g in range(2) if u(g) == 1],
        "chi": [g for g in range(2) if chi(g) == 1],
        "phi": [g for g in range(2) if phi(g) == 1],
    }
    if compatible:
        assert all(phi(g) == u(g) / chi(g) for g in range(2))
        assert set(kernels["chi"]) & set(kernels["phi"]) == (
            set(kernels["chi"]) & set(kernels["u"]))
    return compatible, kernels


print("Part B exact checks; arithmetic precision: exact, except stated finite residue modulus")
one = lambda g: 1
sign = lambda g: (-1)**g
ex1 = check_example(one, one, lambda g: (sign(g), g), False)
print("C2 example 1: compatibility, kernels =", ex1)
ex2 = check_example(sign, one, lambda g: (sign(g), g), True)
assert set(ex2[1]["u"]) != set(ex2[1]["chi"]) & set(ex2[1]["phi"])
print("C2 example 2: compatibility, kernels =", ex2)


def f4mul(a, b):
    c = 0
    for i in range(2):
        for j in range(2):
            if ((a >> i) & 1) and ((b >> j) & 1):
                c ^= 1 << (i + j)
    if c & 4:
        c ^= 7  # a^2+a+1=0
    return c


cubes = {a: f4mul(f4mul(a, a), a) for a in range(4)}
assert cubes == {0: 0, 1: 1, 2: 1, 3: 1}
assert f4mul(2, 2) == 3  # a^2=a+1
assert 2 not in cubes.values()  # no z^3=a
print("F4 elements: 0=0, 1=1, 2=a, 3=a+1; cubes =", cubes)

tH, tN = 1, 0
assert tH != tN
print("Rank-one filtered phi counterexample: t_H=1, t_N=0; not weakly admissible")
for p in (2, 3, 5, 7, 11):
    s = Fraction(1, p + 1)
    assert s.denominator != 1
    assert (p + 1) * s == 1
print("Character exponents tested p=2,3,5,7,11: 1/(p+1) not integral; proof in text works every prime")

# Hensel lifting by the unique next base-5 digit.  This illustrates existence
# only; irrationality follows from the elementary fact that 6 is not a
# rational square, not from these digits.
r, modulus = 1, 5
for n in range(1, 12):
    candidates = [r + digit * modulus for digit in range(5)
                  if ((r + digit * modulus)**2 - 6) % (modulus * 5) == 0]
    assert len(candidates) == 1
    r = candidates[0]
    modulus *= 5
assert modulus == 5**12 and (r*r-6) % modulus == 0 and r % 5 == 1
print("Hensel illustration: sqrt(6) congruent to", r, "mod", modulus)
print("Hensel residual (r^2-6) mod 5^12 =", (r*r-6) % modulus)
print("All finite assertions passed.")
