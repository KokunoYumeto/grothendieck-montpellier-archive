"""Finite algebra and numerical cross-checks for ALP-LIFT-04.

These computations do not prove the prime number theorem or its asymptotic
consequences.  The complete proof is in lift_accounting.md, Section 5.
All local identities are verified exactly as rational functions by SymPy.
The prime sums use ordinary increasing rational-prime order.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp


PHI = {1, 2, 3}
PSI = {1, 2, 4}


def b(a: int) -> int:
    return sum(a * i % 7 not in PHI for i in PHI) - sum(
        a * i % 7 not in PSI for i in PSI
    )


def primes_to(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (
                (n - p * p) // p + 1
            )
    return [i for i, yes in enumerate(sieve) if yes]


def local_difference(p: int) -> float:
    a = p % 7
    if a in (2, 4):
        return 2 * p * (p + 1) / (p**3 - 1)
    if a in (3, 5):
        return -2 * p * (p - 1) / (p**3 + 1)
    return 0.0


def floor_difference(p: int, n: int) -> int:
    q = p
    total = 0
    while q <= n:
        total += b(q % 7) * (n // q)
        q *= p
    return total


def raw_type_floor(phi: set[int], p: int, n: int) -> int:
    q = p
    total = 0
    while q <= n:
        total += sum((q * i) % 7 not in phi for i in phi) * (n // q)
        q *= p
    return total


def main() -> None:
    x = sp.Symbol("x", positive=True)
    local_checks = []
    for a in range(1, 7):
        f = int(sp.n_order(a, 7))
        expression = sum(b(pow(a, r, 7)) * x ** (f - r) for r in range(1, f + 1)) / (
            x**f - 1
        )
        target = (
            2 * x * (x + 1) / (x**3 - 1)
            if a in (2, 4)
            else -2 * x * (x - 1) / (x**3 + 1)
            if a in (3, 5)
            else sp.Integer(0)
        )
        assert sp.cancel(expression - target) == 0
        local_checks.append(
            {"class_mod_7": a, "order": f, "b": b(a), "delta_S": str(sp.factor(target))}
        )

    for p in (2, 3, 5, 11, 13, 29):
        for n in (0, 1, 2, 3, 10, 31, 100, 1000):
            assert floor_difference(p, n) == raw_type_floor(PHI, p, n) - raw_type_floor(PSI, p, n)

    mp.mp.dps = 60
    delta = (
        mp.loggamma(mp.mpf(2) / 7)
        + 3 * mp.loggamma(mp.mpf(4) / 7)
        - 3 * mp.loggamma(mp.mpf(3) / 7)
        - mp.loggamma(mp.mpf(5) / 7)
    )
    good_delta = delta - mp.mpf(12) / 7 * mp.log(2)
    samples = []
    all_primes = primes_to(1_000_000)
    for n in (100, 1000, 10_000, 100_000, 1_000_000):
        current = [p for p in all_primes if p <= n and p != 7]
        slope_sum = math.fsum(math.log(p) * local_difference(p) for p in current)
        floor_sum = math.fsum(math.log(p) * floor_difference(p, n) for p in current)
        dropped_two = math.log(2) * floor_difference(2, n)
        samples.append(
            {
                "cutoff_and_order": n,
                "prime_slope_sum_including_formal_2": slope_sum,
                "prime_slope_sum_omitting_2_and_7": slope_sum - 12 / 7 * math.log(2),
                "floor_difference_per_n_including_formal_2": floor_sum / n,
                "floor_difference_per_n_omitting_2_and_7": (floor_sum - dropped_two) / n,
            }
        )

    result = {
        "status": "exact local algebra passed; finite numerical asymptotic cross-checks only",
        "exact_local_checks": local_checks,
        "exact_floor_checks": "all 48 comparisons passed",
        "height_gap_delta7": mp.nstr(delta, 60),
        "good_prime_constant_delta7_minus_12log2_over7": mp.nstr(good_delta, 60),
        "samples": samples,
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
