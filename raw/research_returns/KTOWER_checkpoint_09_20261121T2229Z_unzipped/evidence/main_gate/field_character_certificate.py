"""Exact small checks of FV.2 by independent finite-sum formulas.

This is a normalization check, not the proof of the general proposition.
Only standard-library exact integers and fractions are used.
"""
from fractions import Fraction
from hashlib import sha256
from math import comb
import json
from pathlib import Path


def bernoulli_numbers(limit):
    values = [Fraction(1)]
    for m in range(1, limit + 1):
        values.append(-sum(Fraction(comb(m + 1, j)) * values[j]
                           for j in range(m)) / (m + 1))
    return values


def quadratic_character(a, conductor):
    # All selected conductors are primes congruent to 3 modulo 4.
    value = pow(a % conductor, (conductor - 1) // 2, conductor)
    return 0 if value == 0 else (1 if value == 1 else -1)


def normalized_bernoulli(k, conductor, values):
    total = Fraction(0)
    for a in range(1, conductor + 1):
        polynomial = sum(Fraction(comb(k, j)) * values[j]
                         * Fraction(a, conductor) ** (k - j)
                         for j in range(k + 1))
        total += quadratic_character(a, conductor) * polynomial
    return total * Fraction(conductor ** (k - 1), k)


def teichmuller_first_residue(p, conductor, exponent):
    modulus = p * p
    numerator = sum(quadratic_character(a, conductor)
                    * pow(pow(a, p, modulus), exponent, modulus) * a
                    for a in range(1, conductor * p + 1) if a % p)
    numerator %= modulus
    assert numerator % p == 0
    return (numerator // p) * pow(conductor, -1, p) % p


def rational_residue(value, p):
    assert value.denominator % p
    return value.numerator * pow(value.denominator, -1, p) % p


def main():
    primes = [5, 7, 11, 13, 17, 19, 23]
    conductors = [3, 7, 11, 19, 43]
    rows = []
    for p in primes:
        values = bernoulli_numbers(p - 2)
        for conductor in conductors:
            if p == conductor:
                continue
            for k in range(3, p - 1, 2):
                lhs = rational_residue(
                    normalized_bernoulli(k, conductor, values), p)
                rhs = teichmuller_first_residue(p, conductor, k - 1)
                assert lhs == rhs, (p, conductor, k, lhs, rhs)
                rows.append([p, conductor, k, lhs, rhs])
    # Explicitly include original weights beyond p and divisible by p.
    values = bernoulli_numbers(21)
    progression = []
    for n in [3, 9, 15, 21]:
        value = normalized_bernoulli(n, 3, values)
        residue = rational_residue(value, 7)
        target = teichmuller_first_residue(7, 3, n - 1)
        assert residue == target
        progression.append({"ell": 7, "conductor": 3, "weight": n,
                            "residue": residue})
    report = {
        "result": "PASS",
        "scope": "Finite normalization checks, not a proof of all cases",
        "ell_values": primes,
        "conductor_values": conductors,
        "finite_character_comparisons": len(rows),
        "rows_sha256": sha256(json.dumps(rows).encode()).hexdigest(),
        "progression": progression,
        "bruinier_example": {"ell": 17, "e": 4,
                              "GD": (2 * 4) % 16 != 0,
                              "second_weight": 9,
                              "exception_exponent": 16},
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
