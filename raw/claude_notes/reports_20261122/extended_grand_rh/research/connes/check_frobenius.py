"""Exact small-prime and S3 character checks for X^3-269."""
from collections import Counter
from itertools import permutations
from math import isqrt


def primes_up_to(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[:2] = b"\x00\x00"
    for n in range(2, isqrt(limit) + 1):
        if flags[n]:
            flags[n * n::n] = bytes((limit - n * n) // n + 1)
    return (p for p, flag in enumerate(flags) if flag)


def trace(power, permutation):
    result = tuple(range(3))
    for _ in range(power):
        result = tuple(permutation[i] for i in result)
    return sum(i == j for i, j in enumerate(result)) - 1


def conjugacy_check():
    group = list(permutations(range(3)))
    standard = [trace(1, g) for g in group]
    assert sorted(standard) == [-1, -1, 0, 0, 0, 2]
    assert sum(t * t for t in standard) == len(group)
    rows = []
    for r in range(1, 7):
        true = [trace(r, g) for g in group]
        means = {}
        for sign in (1, -1):
            values = [v for v, t in zip(true, standard) if (1 if t else -1) == sign]
            assert sum(values) % len(values) == 0
            means[sign] = sum(values) // len(values)
        residual = [v - means[1 if t else -1] for v, t in zip(true, standard)]
        assert residual == ([0] * len(group) if r % 3 == 0 else standard)
        rows.append((r, means[1], means[-1], sum(x*x for x in residual) // len(group)))
    return rows


def main():
    print("power, even mean, odd mean, mean squared residual", conjugacy_check())
    for p in (13, 37):
        print(p, tuple(x for x in range(p) if x**3 % p == 269 % p))
    counts = Counter()
    for p in primes_up_to(1_000_000):
        if p in (3, 269):
            continue
        if p % 3 == 2:
            t = 0
        else:
            t = 2 if pow(269, (p - 1) // 3, p) == 1 else -1
        counts[t] += 1
        if p < 1500:
            assert t == sum(x**3 % p == 269 % p for x in range(p)) - 1
    print("prime cutoff 1000000: trace counts", sorted(counts.items()))


if __name__ == "__main__":
    main()
