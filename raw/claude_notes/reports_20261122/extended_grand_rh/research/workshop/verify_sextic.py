"""Enumerate the mixed Galois group, central Frobenius sectors and fixed ES shell."""
from fractions import Fraction
from itertools import product
from math import isqrt


def mult(x, y):
    j, t, a, b = x
    k, u, c, d = y
    return ((j + (-1)**t * k) % 3, (t + u) % 2,
            (a + (-1)**b * c) % 4, (b + d) % 2)


group = [(j, (a+b) % 2, a, b) for j, a, b in product(range(3), range(4), range(2))]
identity = (0, 0, 0, 0)
inverse = {x: next(y for y in group if mult(x, y) == identity) for x in group}
relative = {x for x in group if x[2] % 2 == x[3] == 0}
commutators = {
    mult(mult(mult(x, y), inverse[x]), inverse[y]) for x, y in product(group, repeat=2)
}
assert len(group) == 24 and len(relative) == 6 and relative == commutators
classes = {
    frozenset(mult(mult(g, x), inverse[g]) for g in group) for x in relative
}
assert sorted(map(len, classes)) == [1, 1, 2, 2]


def divisors_square(n):
    factors = []
    q = 2
    while q * q <= n:
        exponent = 0
        while n % q == 0:
            n //= q
            exponent += 1
        if exponent:
            factors.append((q, 2 * exponent))
        q += 1
    if n > 1:
        factors.append((n, 2))
    result = [1]
    for q, exponent in factors:
        result = [d * q**j for d in result for j in range(exponent + 1)]
    return result


for sign, trace, empty, occupied in [
    (-1, -1, 2689, 1009), (-1, 2, 15289, 19489),
    (1, -1, 3529, 32089), (1, 2, 31249, 80809),
]:
    for p, count in [(empty, 0), (occupied, 12)]:
        assert p % 840 == 169 and all(p % q for q in range(2, isqrt(p) + 1))
        assert pow(3, (p - 1) // 4, p) == sign % p
        assert (pow(269, (p - 1) // 3, p) == 1) == (trace == 2)
        a = (p + 3) // 4
        s = p * a
        solutions = set()
        for d in divisors_square(s):
            if d % 3 == 2:
                x, y = (d + s) // 3, (s*s//d + s) // 3
                assert Fraction(1, a) + Fraction(1, x) + Fraction(1, y) == Fraction(4, p)
                solutions.add((x, y))
        assert len(solutions) == count
        print(p, sign, trace, 2 * sign * trace, count, sep="\t")
