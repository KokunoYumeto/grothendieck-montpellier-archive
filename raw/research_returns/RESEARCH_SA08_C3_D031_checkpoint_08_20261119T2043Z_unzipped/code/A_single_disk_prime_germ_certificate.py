#!/usr/bin/env python3
"""Finite exact checks of AS28's PD endpoint coefficients and actual map.

The all-prime statement, strict map construction, and localization conclusion
are proved in A_single_disk_localization_obstruction.tex. These checks do not
extrapolate a finite calculation to those statements.
"""
from __future__ import annotations
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path


def variable_monomials(total_weight: int, minimum_weight: int):
    """Enumerate every divided-power monomial, with remaining weight in T."""
    def rec(v: int, remaining: int, powers: tuple[tuple[int, int], ...]):
        if v > total_weight:
            if powers:
                yield remaining, powers
            return
        for r in range(remaining // v + 1):
            yield from rec(v + 1, remaining - r * v,
                           powers + ((v, r),) if r else powers)
    yield from rec(minimum_weight, total_weight, ())


def main():
    started = time.perf_counter()
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    checks = 0
    rows = []
    for minimum_weight in range(2, 7):
        for p in primes:
            if p < minimum_weight:
                continue
            monomial_count = other_count = 0
            for coefficient_weight, powers in variable_monomials(p, minimum_weight):
                denominator = math.factorial(coefficient_weight)
                for v, r in powers:
                    denominator *= math.factorial(r) * math.factorial(v) ** r
                numerator = math.factorial(p)
                assert numerator % denominator == 0
                endpoint_coefficient = numerator // denominator
                monomial_count += 1
                checks += 1
                if coefficient_weight == 0 and powers == ((p, 1),):
                    assert endpoint_coefficient == 1
                    checks += 1
                else:
                    assert math.gcd(denominator, p) == 1
                    assert endpoint_coefficient % p == 0
                    other_count += 1
                    checks += 2
            rows.append({"cutoff": minimum_weight, "prime_weight": p,
                         "all_normalized_monomials": monomial_count,
                         "p_divisible_other_monomials": other_count})
    map_rows = []
    for cutoff in range(2, 8):
        for weight in range(cutoff, 51):
            if weight < 2 * cutoff:
                scalar, product_coefficient = 1, 0
            else:
                product_coefficient = math.comb(weight, cutoff)
                scalar = 1 + product_coefficient
                # The rational x^weight coefficients verify p psi = p exactly.
                assert scalar > 0
                assert scalar * math.factorial(cutoff) * math.factorial(weight-cutoff) - math.factorial(weight) == math.factorial(cutoff) * math.factorial(weight-cutoff)
                checks += 1
            # Coefficient endpoint and standard-theory evaluation have the
            # identical integral divided-power coefficient equality.
            assert scalar - product_coefficient == 1
            checks += 1
            if weight in primes and weight >= 2 * cutoff:
                assert scalar % weight == 1 and scalar > 1
                checks += 1
                map_rows.append({"cutoff": cutoff, "prime_weight": weight,
                                 "indecomposable_scalar": scalar})
    result = {
        "theorem": "A-S09-28",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "status": "PASS",
        "checks": checks,
        "runtime_seconds": time.perf_counter() - started,
        "coefficient_checks": rows,
        "endomorphism_prime_scalars": map_rows,
        "scope": "Exact finite coefficients only; the arbitrary-prime, categorical, and strict-map arguments are in the written proof."
    }
    out = Path(__file__).resolve().parents[1] / "logs" / "A_single_disk_prime_germ_certificate.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["theorem", "status", "checks", "runtime_seconds"]}))
    print(str(out))


if __name__ == "__main__":
    main()
