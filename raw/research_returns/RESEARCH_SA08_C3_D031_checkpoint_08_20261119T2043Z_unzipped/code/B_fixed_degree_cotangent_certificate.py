#!/usr/bin/env python3
"""Finite checks of the exact Fu--Nuiten degree/weight inequalities.

This verifies a bounded collection of actual admissible operation indices,
including p=2.  It does not replace the all-index proof of A-L10 or the
two filtrations of the cotangent complex.
"""
import json
from pathlib import Path
from time import perf_counter


def compositions_at_most(length, budget):
    if length == 0:
        yield ()
        return
    for a in range(budget + 1):
        for tail in compositions_at_most(length - 1, budget - a):
            yield (a,) + tail


def bound(p, n):
    return max([n + 1] + [
        (n + 2 - 2 * r) * p ** r
        for r in range(1, (n + 1) // 2 + 1)
    ])


def main():
    started = perf_counter()
    primes = (2, 3, 5, 7, 11, 13)
    max_degree = 16
    checks = 0
    accepted = 0
    per_prime = {}
    witnesses = {}
    for p in primes:
        count = 0
        for length in range(1, max_degree + 2):
            epsilon = int(p > 2 and length % 2 == 1)
            for e in range(epsilon + 1):
                effective = (1 + e) * length
                for r in range(max_degree - effective + 2):
                    budget = max_degree - effective + 1 - r
                    for a in compositions_at_most(r, budget):
                        if r:
                            modulus = 2 * (p - 1)
                            if any(x % modulus not in (0, 1) for x in a):
                                continue
                            if a[-1] > (p - 1) * (1 + e) * (length - 1) + epsilon:
                                continue
                            if any(a[j] >= p * a[j + 1] for j in range(r - 1)):
                                continue
                        n = effective - 1 + sum(a) + r
                        assert 0 <= n <= max_degree
                        checks += 1
                        accepted += 1
                        count += 1
                        if r:
                            assert sum(a) >= r - 1
                            assert n >= effective + 2 * r - 2
                            assert r <= (n + 1) // 2
                            checks += 3
                        else:
                            assert n == effective - 1
                            checks += 1
                        envelope = effective * p ** r
                        assert envelope <= bound(p, n)
                        checks += 1
                        for truncation in (2, 3, 4, 7, 13):
                            maximal_letter_weight = (truncation - 1) * length
                            total_weight = (1 + e) * p ** r * maximal_letter_weight
                            assert total_weight <= (truncation - 1) * bound(p, n)
                            assert (truncation - 1) * (1 + bound(p, n)) >= truncation
                            checks += 2
                        key = (p, n)
                        if envelope > witnesses.get(key, {}).get("weight_envelope", -1):
                            witnesses[key] = {
                                "length": length,
                                "e": e,
                                "indices": [-x for x in a],
                                "weight_envelope": envelope,
                            }
        per_prime[str(p)] = count
    result = {
        "statement": "A-L10",
        "purpose": "Supplementary finite checks of operation-degree and weight inequalities",
        "all_assertions_passed": True,
        "exact_checks": checks,
        "accepted_sequences": accepted,
        "per_prime": per_prime,
        "max_bar_degree": max_degree,
        "bounds": {str(p): [bound(p, n) for n in range(max_degree + 1)] for p in primes},
        "extremal_envelopes": {
            f"p={p},n={n}": value for (p, n), value in witnesses.items()
        },
        "limitations": [
            "The enumeration is bounded in homological degree.",
            "Length envelopes do not assert existence of a Lyndon word of every extremal weight.",
            "The all-index proof and the two actual chain filtrations are in B_fixed_degree_cotangent.tex.",
        ],
        "runtime_seconds": perf_counter() - started,
    }
    destination = Path(__file__).resolve().parents[1] / "logs" / "B_fixed_degree_cotangent_certificate.json"
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in (
        "statement", "all_assertions_passed", "exact_checks", "accepted_sequences", "runtime_seconds"
    )}))


if __name__ == "__main__":
    main()
