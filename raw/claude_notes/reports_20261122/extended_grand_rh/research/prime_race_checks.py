"""Finite checks for the S3 trace, the twists at 12, and the prime-square bias."""
from itertools import permutations
from math import gcd, isqrt

def primes_through(limit):
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n

def parity(g):
    return sum(g[i] > g[j] for i in range(3) for j in range(i + 1, 3)) % 2

def trace(g):
    return sum(g[i] == i for i in range(3)) - 1

def square(g):
    return tuple(g[g[i]] for i in range(3))

perms = list(permutations(range(3)))
checked = 0
for p in primes_through(1000):
    if 3 * 269 % p == 0:
        continue
    actual = sum(pow(x, 3, p) == 269 % p for x in range(p)) - 1
    expected = 3 * (pow(269, (p - 1) // 3, p) == 1) - 1 if p % 3 == 1 else 0
    assert actual == expected
    for k in range(isqrt(p), isqrt(p) + 5):
        assert sum(p <= j*j for j in range(1,k+1)) == max(0,k-isqrt(p))
    checked += 1
for m in range(3, 181, 3):
    units = [a for a in range(1, m) if gcd(a, m) == 1]
    G = [(g,a) for g in perms for a in units if parity(g) == (a % 3 == 2)]
    assert len(G) == 3 * len(units)
    square_sum = sum(trace(square(g)) * len(units) for g,a in G if a*a % m == 1)
    involutions = sum(a*a % m == 1 for a in units)
    assert square_sum == len(G) * involutions
    if m == 12:
        for g,a in G:
            eisenstein = 1 if a % 3 == 1 else -1
            gaussian = 1 if a % 4 == 1 else -1
            regular = len(units) if a == 1 else 0
            assert trace(g) * eisenstein == trace(g)
            assert trace(g) * regular == 2 * trace(g) * (1 + gaussian)
print(f"{checked} unramified prime traces, their square-sample counts, and 60 finite-group biases agree.")
