"""Check the central Frobenius sign and both fixed-denominator counts."""
from fractions import Fraction
from itertools import product
from math import prod


def factor(value):
    result = {}
    prime = 2
    while prime * prime <= value:
        while value % prime == 0:
            result[prime] = result.get(prime, 0) + 1
            value //= prime
        prime += 1
    if value > 1:
        result[value] = 1
    return result


def divisors(factors):
    result = [1]
    for prime, exponent in factors.items():
        result = [d * prime**e for d in result for e in range(exponent + 1)]
    return sorted(result)


def quartic(r, s):
    return r**4 - r*r*s*s + s**4


assert quartic(3, 5) == 481 == 13 * 37
assert pow(3, 3, 13) == 1 and pow(3, 9, 37) == 36
unit_vectors = {(r, s) for r, s in product(range(-3, 4), repeat=2) if quartic(r, s) == 1}
assert unit_vectors == set(product((-1, 0, 1), repeat=2)) - {(0, 0)}
assert all(quartic(r, s) == quartic(-s, r) == quartic(s, r)
           for r, s in product(range(-4, 5), repeat=2))

for p, sign, opposition, denominators in [
    (1009, -1, 32, 12), (2689, -1, 0, 0),
    (3529, 1, 0, 0), (32089, 1, 32, 12),
]:
    assert p % 840 == 169 and factor(p) == {p: 1}
    assert pow(3, (p - 1) // 4, p) == sign % p
    a = (p + 3) // 4
    s = p * a
    factors = factor(s)
    ds = divisors(factors)
    assert sum((d + e) % 3 == 0 for d in ds for e in ds) == opposition
    fsq = {prime: 2 * e for prime, e in factors.items()}
    actual = []
    for d in divisors(fsq):
        if d % 3 == 2:
            x = (s + d) // 3
            y = (s + s * s // d) // 3
            assert Fraction(4, p) == Fraction(1, a) + Fraction(1, x) + Fraction(1, y)
            actual.append((x, y))
    assert len(set(actual)) == len(actual) == denominators
    parity = prod(2 * e + 1 for prime, e in factors.items() if prime % 3 == 1)
    assert (prod(2 * e + 1 for e in factors.values()) - parity) // 2 == denominators
    print(p, sign, opposition, denominators, sep="\t")
