"""Exact, standard-library certificate for the level-three seed at e=18.

The large reflected Bernoulli index is NOT recomputed here. Its complete
certificate is the carried K17-BERNOULLI-8361790201 result.
"""
from fractions import Fraction
from math import comb, isqrt
import json


def main():
    prime = 8361790201
    weight = 37
    assert all(prime % d for d in range(2, isqrt(prime) + 1))
    assert prime % 3 == 1 and prime > 2**31
    bernoulli = [Fraction(1)]
    for m in range(1, weight + 1):
        bernoulli.append(
            -sum((comb(m + 1, j) * bernoulli[j] for j in range(m)),
                 Fraction(0)) / (m + 1)
        )
    # chi_{-3}(1)=1, chi_{-3}(2)=-1. Bernoulli-polynomial identity.
    normalized = sum(
        (Fraction(comb(weight, j)) * bernoulli[j]
         * (1 - 2**(weight - j)) * Fraction(3)**(j - 1)
         for j in range(weight + 1)), Fraction(0)
    ) / weight
    expected = Fraction(-1701990248643001964415638362402, 3)
    assert normalized == expected
    assert normalized.numerator % prime == 0
    assert normalized.denominator % prime != 0
    inert_test = (1 - pow(2, weight - 1, prime)) % prime
    assert inert_test == 6536635074 and inert_test != 0
    result = {
        "status": "PASS",
        "prime": prime,
        "primality_method": "trial division through integer square root",
        "trial_division_limit": isqrt(prime),
        "weight": weight,
        "e": 18,
        "coefficient_highest_parameter_a": 17,
        "normalized_generalized_B_numerator": normalized.numerator,
        "normalized_generalized_B_denominator": normalized.denominator,
        "normalized_numerator_quotient_by_prime": normalized.numerator // prime,
        "inert_q2_Eisenstein_residue": inert_test,
        "prime_mod3": prime % 3,
        "exceeds_2_to_31": prime > 2**31,
        "method": "exact Fraction Bernoulli recurrence and polynomial identity",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
