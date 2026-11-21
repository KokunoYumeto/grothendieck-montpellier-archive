"""Full-factor Lucas certificate, independent of trial division of the target."""
from math import gcd, isqrt, prod
from pathlib import Path
import json

N = 697446897311
FACTORS = {2: 1, 5: 1, 31: 1, 1019: 1, 2207879: 1}
WITNESSES = {2: 13, 5: 2, 31: 2, 1019: 2, 2207879: 2}


def trial_prime(q):
    if q < 2:
        return False
    return all(q % d for d in range(2, isqrt(q) + 1))


def certificate():
    assert prod(q ** exponent for q, exponent in FACTORS.items()) == N - 1
    rows = []
    for q, exponent in FACTORS.items():
        assert trial_prime(q)
        a = WITNESSES[q]
        fermat = pow(a, N - 1, N)
        partial = pow(a, (N - 1) // q, N)
        coprime = gcd(partial - 1, N)
        assert fermat == 1
        assert coprime == 1
        rows.append({
            "prime_factor": q,
            "exponent": exponent,
            "prime_factor_checked_by_all_divisors_through": isqrt(q),
            "witness": a,
            "power_N_minus_1_mod_N": fermat,
            "power_N_minus_1_over_q_mod_N": partial,
            "gcd_partial_minus_1_with_N": coprime,
        })
    assert N > 2 ** 31
    return {
        "status": "PASS exact full-factor Lucas primality certificate",
        "prime": N,
        "N_minus_1_factor_product": prod(q ** exponent for q, exponent in FACTORS.items()),
        "above_2_power_31": True,
        "difference_from_2_power_31": N - 2 ** 31,
        "method": (
            "Each q dividing N-1 is prime by exhaustive small trial division. "
            "For every prime divisor p of N the witnesses force the order "
            "modulo p to contain the full q-power in N-1, for every q. "
            "Hence N-1 divides p-1, so p=N."
        ),
        "checks": rows,
    }


if __name__ == "__main__":
    result = certificate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
