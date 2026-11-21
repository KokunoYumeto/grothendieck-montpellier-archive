#!/usr/bin/env python3
"""Exact, elementary certificates for small-prime generation of (Z/NZ)^*.

This program verifies individual moduli. It does not check GT equations, identify
a quotient's multiplier modulus, prove GRH, or establish a theorem for all N.
All bound decisions and group computations use integers and fractions. Displayed
decimals are informational. No external packages are needed.

Run from this directory: python verify_gt_units.py
Or give moduli: python verify_gt_units.py 12 101
"""

from collections import deque
import csv
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import sys


# The source-to-modulus inventory is GT_LEVEL_SCOPE.tsv.  It distinguishes
# actual multiplier/cusp moduli from matrix, coefficient, and illustrative
# moduli.  No integer below is being identified with the order of a GT group.
DEFAULT_MODULI = (
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 23, 24, 25, 27, 28, 29, 30, 31, 36, 48, 49, 60, 64,
    72, 81, 96, 101, 108, 120, 121, 144, 169, 192, 202, 288, 289,
    324, 360, 361, 529, 576, 841, 961, 972,
)


def log_interval(n, terms):
    """Return rigorous rational lower and upper bounds for natural log(n)."""
    if n < 1:
        raise ValueError("n must be positive")
    k = n.bit_length() - 1

    def log_rational_interval(a, b):
        # 1 <= a/b <= 2, t=(a-b)/(a+b), log(a/b)=2*atanh(t).
        t = Fraction(a - b, a + b)
        s = Fraction(0)
        power = t
        for j in range(terms):
            s += 2 * power / (2 * j + 1)
            power *= t * t
        # All remaining terms are positive; replacing their denominators by
        # 2*terms+1 gives this geometric-series upper bound.
        tail = 2 * power / ((2 * terms + 1) * (1 - t * t))
        return s, s + tail

    l2, u2 = log_rational_interval(2, 1)
    lr, ur = log_rational_interval(n, 2**k)
    return k * l2 + lr, k * u2 + ur


def strict_log_square_cutoff(n, coefficient):
    """Greatest integer below coefficient*(ln n)^2, proven by intervals."""
    if n == 1:
        return -1, Fraction(0), Fraction(0)
    terms = 16
    while True:
        lo, hi = log_interval(n, terms)
        lo, hi = coefficient * lo * lo, coefficient * hi * hi
        flo, fhi = lo.numerator // lo.denominator, hi.numerator // hi.denominator
        if flo == fhi and lo > flo:
            return flo, lo, hi
        terms *= 2


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def words_for_subgroup(n, generators):
    """BFS gives a literal nonnegative prime word for each generated residue."""
    one = 1 % n
    words = {one: (0,) * len(generators)}
    queue = deque([one])
    while queue:
        r = queue.popleft()
        for i, p in enumerate(generators):
            s = r * p % n
            if s not in words:
                e = list(words[r])
                e[i] += 1
                words[s] = tuple(e)
                queue.append(s)
    return words


def certificate(n):
    if n < 2:
        raise ValueError("Use N>=2; N=1 has a trivial unit group by convention")
    units = {a for a in range(1, n) if gcd(a, n) == 1}
    cut2, lo2, hi2 = strict_log_square_cutoff(n, 2)
    cut3, lo3, hi3 = strict_log_square_cutoff(n, 3)
    primes2 = [p for p in range(2, cut2 + 1) if is_prime(p) and gcd(p, n) == 1]
    primes3 = [p for p in range(2, cut3 + 1) if is_prime(p) and gcd(p, n) == 1]
    basis = []
    generated = {1 % n}
    for p in primes2:
        if p % n not in generated:
            basis.append(p)
            generated = set(words_for_subgroup(n, basis))
    words = words_for_subgroup(n, basis)
    # Independently validate every displayed word and membership.
    for r, exponents in words.items():
        value = 1 % n
        for p, e in zip(basis, exponents):
            value = value * pow(p, e, n) % n
        assert value == r and gcd(r, n) == 1
    assert set(words) == generated
    assert generated <= units
    generated3 = set(words_for_subgroup(n, primes3))
    row = {
        "N": n,
        "phi_N_by_enumeration": len(units),
        "two_log_squared_decimal": f"{float((lo2 + hi2)/2):.12f}",
        "two_log_squared_exact_floor": cut2,
        "primes_below_two_bound_coprime_to_N": ",".join(map(str, primes2)),
        "greedy_prime_basis": ",".join(map(str, basis)),
        "generated_group_order": len(generated),
        "two_bound_generation_verified": str(generated == units),
        "strict_bound_checked_with_rational_intervals": "True",
        "three_log_squared_decimal": f"{float((lo3 + hi3)/2):.12f}",
        "three_log_squared_exact_floor": cut3,
        "three_bound_generation_verified": str(generated3 == units),
        "word_certificate_rows": len(words),
    }
    return row, basis, words


def main():
    moduli = tuple(map(int, sys.argv[1:])) if len(sys.argv) > 1 else DEFAULT_MODULI
    rows = []
    word_rows = []
    for n in moduli:
        row, basis, words = certificate(n)
        rows.append(row)
        for r in sorted(words):
            word_rows.append({
                "N": n,
                "residue": r,
                "prime_basis": ",".join(map(str, basis)),
                "exponents": ",".join(map(str, words[r])),
                "verified_product_mod_N": r,
            })
    destination = Path(__file__).resolve().parent
    for name, data in [("GT_UNIT_CERTIFICATES.tsv", rows), ("GT_UNIT_WORDS.tsv", word_rows)]:
        with (destination / name).open("w", newline="") as f:
            writer = csv.DictWriter(f, delimiter="\t", fieldnames=list(data[0]))
            writer.writeheader()
            writer.writerows(data)
    for r in rows:
        print(f"N={r['N']}: generators [{r['greedy_prime_basis']}], "
              f"order={r['generated_group_order']}, phi={r['phi_N_by_enumeration']}, "
              f"all strictly below 2 log^2 N: {r['two_bound_generation_verified']}")
    if not all(r["two_bound_generation_verified"] == "True" for r in rows):
        raise SystemExit("At least one modulus did not pass the requested two-bound computation")


if __name__ == "__main__":
    main()
