"""Exact finite certificate for the prime-weight PD ideal in C15.

The proof is symbolic; this records independent integer arithmetic at
finite primes and cutoffs. It does not test or assert global C3.
"""
from pathlib import Path
from collections import Counter
from math import comb, factorial, prod
import json
import time

ROOT = Path(__file__).resolve().parents[1]


def primes_through(bound):
    return [
        n for n in range(2, bound + 1)
        if all(n % d for d in range(2, int(n**0.5) + 1))
    ]


def partitions(total, minimum):
    """All nondecreasing partitions, with every part at least minimum."""
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


start = time.monotonic()
rows = []
total_products = 0
total_pd_terms = 0
for prime in primes_through(43):
    for cutoff in range(2, min(8, prime - 1) + 1):
        product_checks = 0
        for left in range(cutoff, prime):
            coefficient = comb(prime, left)
            assert coefficient % prime == 0, (prime, cutoff, left)
            product_checks += 1
        pd_checks = 0
        examples = []
        for parts in partitions(prime, cutoff):
            if len(parts) < 2:
                continue
            multiplicities = Counter(parts)
            denominator = prod(
                factorial(weight)**multiplicity * factorial(multiplicity)
                for weight, multiplicity in multiplicities.items()
            )
            numerator = factorial(prime)
            assert numerator % denominator == 0
            coefficient = numerator // denominator
            assert coefficient % prime == 0, (prime, cutoff, parts, coefficient)
            assert all(weight < prime for weight in parts)
            assert all(multiplicity < prime for multiplicity in multiplicities.values())
            pd_checks += 1
            if len(examples) < 2:
                examples.append({"partition": parts, "coefficient": coefficient})
        total_products += product_checks
        total_pd_terms += pd_checks
        rows.append({
            "N": cutoff,
            "p": prime,
            "product_checks": product_checks,
            "pd_partition_checks": pd_checks,
            "examples": examples,
        })

result = {
    "claim": (
        "The only unremoved weight in the tail quotient is the prime p. "
        "Every product from J_p and every higher PD term built from tail "
        "weights landing in weight p has coefficient divisible by p."
    ),
    "scope": "Finite exact arithmetic certificate; symbolic proof is B_C3_replacements.md.",
    "prime_bound": 43,
    "cutoffs": "2 <= N <= min(8,p-1)",
    "pairs": len(rows),
    "product_checks": total_products,
    "pd_partition_checks": total_pd_terms,
    "checks_passed": True,
    "seconds": time.monotonic() - start,
    "rows": rows,
}
path = ROOT / "logs/B_prime_pd_ideal_checks.json"
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({key: value for key, value in result.items() if key != "rows"}, indent=2))
