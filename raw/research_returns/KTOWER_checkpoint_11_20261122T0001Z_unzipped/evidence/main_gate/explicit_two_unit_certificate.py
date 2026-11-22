"""KT-EXPLICIT-TWO-UNIT-CODE: exact finite tests, not an all-prime proof.

The O(f+p) character-prefix identity is proved in bernoulli_prefix_formula.tex.
Two independent finite formulas reconcile it at small primes.  The scan
records, but does not assume, the third unit for each of the two fields.
Only Python's standard library and exact integers/fractions are used.
"""
from fractions import Fraction
from hashlib import sha256
from math import comb, gcd, isqrt
from pathlib import Path
import json


def primes_three_mod_four(bound):
    flags = bytearray(b"\1") * (bound + 1)
    flags[:2] = b"\0\0"
    for p in range(2, isqrt(bound) + 1):
        if flags[p]:
            flags[p * p:bound + 1:p] = b"\0" * ((bound - p * p) // p + 1)
    return [p for p in range(7, bound + 1, 4) if flags[p]]


def squarefree_part(n):
    result = 1
    for q in range(2, isqrt(n) + 1):
        parity = 0
        while n % q == 0:
            n //= q
            parity ^= 1
        if parity:
            result *= q
    return result * n


def jacobi(a, n):
    """Jacobi symbol for positive odd n, including n=1."""
    assert n > 0 and n % 2
    a %= n
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        a, n = n, a
        if a % 4 == n % 4 == 3:
            sign = -sign
        a %= n
    return sign if n == 1 else 0


def character_data(m):
    """chi_{-4m}; m is positive square-free and 1 modulo 4."""
    assert m % 4 == 1
    f = 4 * m
    symbols = [jacobi(a, m) for a in range(m)]
    character = [0 if a % 2 == 0 else
                 (1 if a % 4 == 1 else -1) * symbols[a % m]
                 for a in range(f)]
    prefix = [0]
    for value in character:
        prefix.append(prefix[-1] + value)
    assert prefix[-1] == 0
    assert all(character[-a % f] == -character[a] for a in range(f))
    return character, prefix


def weights(p):
    inverses = [0] * p
    inverses[1] = 1
    for a in range(2, p):
        inverses[a] = -(p // a) * inverses[p % a] % p
    legendre = [-1] * p
    legendre[0] = 0
    for a in range(1, (p + 1) // 2):
        legendre[a * a % p] = 1
    first = [legendre[a] * inverses[a] % p for a in range(p)]
    third = [inverses[a] ** 2 % p for a in range(p)]
    return first, third


def prefix_residue(p, character, prefix, weight):
    f = len(character)
    inverse_p = pow(p, -1, f)
    return character[p % f] * sum(
        weight[r] * prefix[r * inverse_p % f] for r in range(1, p)) % p


def direct_teichmuller_residue(p, character, exponent):
    """Definition at conductor f*p, retaining precision p^2 before division."""
    f = len(character)
    modulus = p * p
    lifted = [0] + [pow(pow(a, p, modulus), exponent, modulus)
                    for a in range(1, p)]
    numerator = sum(a * character[a % f] * lifted[a % p]
                    for a in range(1, f * p + 1)) % modulus
    assert numerator % p == 0
    return numerator // p * pow(f, -1, p) % p


def bernoulli_numbers(limit):
    values = [Fraction(1)]
    for n in range(1, limit + 1):
        values.append(-sum(Fraction(comb(n + 1, j)) * values[j]
                           for j in range(n)) / (n + 1))
    return values


def normalized_bernoulli(n, character, values):
    f = len(character)
    total = Fraction(0)
    for a in range(1, f + 1):
        polynomial = sum(Fraction(comb(n, j)) * values[j]
                         * Fraction(a, f) ** (n - j)
                         for j in range(n + 1))
        total += character[a % f] * polynomial
    return total * Fraction(f ** (n - 1), n)


def rational_residue(value, p):
    assert value.denominator % p
    return value.numerator * pow(value.denominator, -1, p) % p


def main():
    bound = 20000
    rows = []
    direct_checks = []
    polynomial_checks = []
    individual_failures = []
    both_failures = []
    primes = primes_three_mod_four(bound)
    for p in primes:
        first_weight, third_weight = weights(p)
        pair_third = []
        for sign in (1, -1):
            m = squarefree_part(p + 2 * sign)
            assert (p + 2 * sign) % m == 0
            assert isqrt((p + 2 * sign) // m) ** 2 == (p + 2 * sign) // m
            assert m % 4 == 1 and gcd(p, m) == 1
            character, prefix = character_data(m)
            f = 4 * m
            w = 4 if m == 1 else 2
            b1 = Fraction(sum(a * character[a] for a in range(f)), f)
            h = -Fraction(w, 2) * b1
            assert h.denominator == 1 and 0 < h < p
            assert h == Fraction(w, 4) * sum(character[1:f // 2 + 1])
            e0 = (p - 3) // 2
            assert e0 % 2 == 0 and (2 * e0) % (p - 1) != 0
            first = prefix_residue(p, character, prefix, first_weight)
            third = prefix_residue(p, character, prefix, third_weight)
            zeroth = rational_residue(b1, p)
            assert zeroth and first
            expected_splitting = -sign * jacobi(2, p)
            assert character[p % f] == expected_splitting
            if third == 0:
                individual_failures.append([p, sign, -f])
            pair_third.append(third)
            rows.append([p, sign, -f, e0, int(h), expected_splitting,
                         zeroth, first, third])
            if p <= 151:
                for exponent, expected in ((e0, first), (2 * e0, third)):
                    got = direct_teichmuller_residue(p, character, exponent)
                    assert got == expected, (p, sign, exponent, got, expected)
                    direct_checks.append([p, sign, exponent, got])
            if p in (7, 11, 19):
                values = bernoulli_numbers(p - 2)
                for n, expected in (((p - 1) // 2, first), (p - 2, third)):
                    value = normalized_bernoulli(n, character, values)
                    got = rational_residue(value, p)
                    assert got == expected, (p, sign, n, got, expected)
                    polynomial_checks.append({"p": p, "sign": sign, "D": -f,
                                              "weight": n, "value": str(value),
                                              "residue": got})
        if pair_third == [0, 0]:
            both_failures.append(p)
    report = {
        "result": "PASS",
        "scope": "Finite exact checks; no all-prime assertion for the third unit",
        "prime_bound": bound,
        "prime_count": len(primes),
        "field_count": len(rows),
        "row_columns": ["ell", "sign", "D", "e0", "class_number",
                        "ell_splitting_symbol", "B1_residue",
                        "first_twist_residue", "third_twist_residue"],
        "rows_sha256": sha256(json.dumps(rows).encode()).hexdigest(),
        "direct_mod_p_squared_comparisons": len(direct_checks),
        "direct_checks_sha256": sha256(json.dumps(direct_checks).encode()).hexdigest(),
        "exact_bernoulli_polynomial_comparisons": polynomial_checks,
        "individual_third_failures": individual_failures,
        "both_third_failures": both_failures,
        "rows": rows,
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    compact = {key: value for key, value in report.items() if key != "rows"}
    print(json.dumps(compact, indent=2))


if __name__ == "__main__":
    main()
