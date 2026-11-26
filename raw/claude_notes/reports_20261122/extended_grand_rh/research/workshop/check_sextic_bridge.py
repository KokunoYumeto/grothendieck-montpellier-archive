"""Exact checks of the traces in sextic_bridge.tex. Standard library only."""

from collections import Counter
from math import isqrt


def primes_to(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = bytes(2)
    for n in range(2, isqrt(limit) + 1):
        if sieve[n]:
            sieve[n * n :: n] = bytes((limit - n * n) // n + 1)
    return [n for n, prime in enumerate(sieve) if prime]


def lifted_trace(p, d):
    """Coefficients of 1 and sqrt(-3) in the Eisenstein-field induction."""
    omega = ((d - 1) * pow(2, -1, p)) % p
    assert pow(omega, 3, p) == 1 and omega != 1
    phase = pow(269, (p - 1) // 3, p)
    k = [1, omega, omega * omega % p].index(phase)
    quadratic = 1 if pow(2 * d, (p - 1) // 2, p) == 1 else -1
    if p % 4 == 1:
        return quadratic * (2 if k == 0 else -1), 0
    return 0, quadratic * (0, 1, -1)[k]


def verify(limit=6000):
    counts, first, imaginary = Counter(), {}, []
    for p in primes_to(limit):
        if p % 3 != 1 or p == 269:
            continue
        d = next(x for x in range(1, p) if (x * x + 3) % p == 0)
        trace = lifted_trace(p, d)
        assert trace == lifted_trace(p, p - d)
        if p % 4 == 3:
            if trace[1]:
                imaginary.append((p, trace[1]))
            continue
        v = 1 if pow(3, (p - 1) // 4, p) == 1 else -1
        t = sum(pow(x, 3, p) == 269 % p for x in range(p)) - 1
        assert trace == (t * v, 0) and t in {-1, 2}
        s = next(x for x in range(1, p) if (x * x - 3) % p == 0)
        for root in [s, p - s]:
            j = pow(269**2 * 3 * root, (p - 1) // 6, p)
            assert pow(j, 6, p) == 1
            assert (j + pow(j, -1, p) - v * t) % p == 0
        counts[(v, t)] += 1
        first.setdefault((v, t), p)
    assert len(counts) == 4 and len(imaginary) >= 2
    print("First primes and observed counts by (quartic sign, cubic trace)")
    for case in sorted(counts):
        print(case, first[case], counts[case])
    print("First two purely imaginary nonzero traces, in units of sqrt(-3):",
          imaginary[:2])
    print("Their product:", -3 * imaginary[0][1] * imaginary[1][1])


if __name__ == "__main__":
    verify()
