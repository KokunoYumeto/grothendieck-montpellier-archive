"""Exact checks of the shell histograms and character zeros (Python 3)."""
from fractions import Fraction
from math import gcd, isqrt


def sieve(limit):
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for q in range(2, isqrt(limit) + 1):
        if flags[q]:
            flags[q * q::q] = bytes(1 + (limit - q * q) // q)
    return [q for q in range(2, limit + 1) if flags[q]]


def factor(n):
    ans = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            ans[q] = ans.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1:
        ans[n] = 1
    return ans


def divisors(factors):
    values = [1]
    for q, e in factors.items():
        values = [d * q**j for d in values for j in range(e + 1)]
    return values


def shell7(p):
    a = (p + 7) // 4
    factors = factor(a)
    assert p not in factors
    factors[p] = 1
    ds = divisors(factors)
    hist = [sum(d % 7 == g for d in ds) for g in range(1, 7)]
    # Each table entry follows directly from the defining double sum.
    pairs = sum((d + e) % 7 == 0 for d in ds for e in ds)
    assert pairs == sum(i * j for i, j in zip(hist, reversed(hist)))

    # Character index j relative to generator 3 modulo 7. A local sum is zero
    # exactly when its nontrivial order divides the number of summands.
    exponents = {pow(3, i, 7): i for i in range(6)}
    killed = []
    for j in range(1, 6):
        orders = [(6 // gcd(6, j * exponents[q % 7]), e) for q, e in factors.items()]
        killed.append(any(h > 1 and (e + 1) % h == 0 for h, e in orders))
    assert all(killed) == (len(set(hist)) == 1)
    odd_order_kill = any(q % 7 in (2, 3, 4, 5) and e % 3 == 2 for q, e in factors.items())
    assert killed[1] == killed[3] == odd_order_kill
    for q, e in factors.items():
        if q % 7 == 6 and e % 2:
            assert hist == hist[::-1]
    return a, hist, pairs


if __name__ == "__main__":
    # Primitive shifted-form certificates, one per residual class modulo 840.
    witnesses = [(1, 5792641, -377, 89), (121, 565441, -183, 11),
                 (169, 2662129, -409, 10), (289, 1703809, -311, 23),
                 (361, 884881, -167, 32), (529, 3039649, -334, 55)]
    for residue, p, u, v in witnesses:
        assert gcd(u, v) == 1 and 16 * (u*u + u*v + 32*v*v) - 127 == p
        assert factor(p) == {p: 1} and p % 840 == residue and p % 121 == 8
        a = (p + 127) // 4
        assert all(pow(q, 63, 127) == 1 for q in factor(p * a))
        assert len({d % 127 for d in divisors(factor(p * a))} &
                   {-d % 127 for d in divisors(factor(p * a))}) == 0
        aa, bb, cc = (p + 3) // 4, p * (p + 3) // 11, p * (p + 3)
        assert Fraction(4, p) == Fraction(1, aa) + Fraction(1, bb) + Fraction(1, cc)
    print("Certified cross-shell prime witnesses in all six residual classes.")
    primes = sieve(60000)
    checks = [p for p in primes if p % 24 == 1]
    for p in checks:
        shell7(p)
    print("Exact prime-shell character and pairing checks:", len(checks))
    for p in (2521, 9241, 14281, 42841):
        print(p, shell7(p))
    # Outward integer rounding at every multiplication bounds the finite product.
    # The omitted product differs from 1 by at most sum_{n>Y} 2/n^2 <= 2/Y.
    Y = 50000
    scale = 10**30
    lo, hi = scale, scale
    for q in primes:
        if not (5 <= q <= Y and q % 7 in (2, 3, 4, 5)):
            continue
        den = q**3 - 1
        num = den - q
        lo = (lo * num) // den
        hi = (hi * num + den - 1) // den
    lower = 1 - Fraction(5 * hi, 7 * scale)
    upper = 1 - Fraction(5 * lo, 7 * scale) * (1 - Fraction(2, Y))
    print("Outward decimal bounds on limiting exact-uniformity density:",
          (lower * 10**6).__floor__() / 10**6, (upper * 10**6).__ceil__() / 10**6)
