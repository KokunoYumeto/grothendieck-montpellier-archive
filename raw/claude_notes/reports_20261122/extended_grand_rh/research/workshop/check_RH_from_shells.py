"""Check the two raw integer counts and the residue class 1 modulo 840."""
from collections import Counter
from math import gcd, isqrt, prod


def divisors(n):
    small = [k for k in range(1, isqrt(n) + 1) if n % k == 0]
    return small + [n // k for k in reversed(small) if k * k != n]


def raw_opposition(a):
    counts = Counter()
    for d in divisors(a):
        counts[d % 3] += 1
        counts[(4 * a * d) % 3] += 1
    return 2 * counts[1] * counts[2]


def prime(n):
    return n > 1 and all(n % k for k in range(2, isqrt(n) + 1))


def check():
    cases = 0
    for m in range(1, 4000, 6):
        if gcd(m, 210) != 1:
            continue
        ds = divisors(m)
        tau = len(ds)
        b = sum(1 if d % 3 == 1 else -1 for d in ds)
        assert raw_opposition(m) == 2 * (tau**2 - b**2)
        assert raw_opposition(25 * m) == 18 * tau**2 - 2 * b**2
        assert (4 * 25 * m - 3) % 24 == 1
        cases += 1
    units = [r for r in range(1, 210) if gcd(r, 210) == 1]
    markers = {}
    for r in units:
        start = pow(11 * r, -1, 210)
        q = start
        while q == 11 or not prime(q):
            q += 210
        markers[r] = q
    excluded = 210 * 11 * prod(markers.values())
    exact = 0
    for m in range(1, 2501):
        if gcd(m, excluded) != 1:
            continue
        a = 11 * markers[m % 210] * m
        assert (4 * a - 3) % 840 == 1
        assert raw_opposition(a) == 32 * len(divisors(m))**2
        exact += 1
    print(f"Verified {cases} pairs of counts at m and 25m.")
    print(f"Verified {exact} marked counts in class 1 modulo 840, "
          f"using {len(markers)} primes through {max(markers.values())}.")


if __name__ == "__main__":
    check()
