"""Exact abstract countermodel checks for K17-HOST-GREENBERG-GATE.

These polynomials and groups are not asserted to be arithmetic objects.
No external packages, floating point, or automorphic data are used.
"""
from math import gcd, isqrt, prod
from pathlib import Path
import json


def trial_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


p = 2**31 + 11
assert trial_prime(p)
factors = [2, 3, 149, 2402107]
assert prod(factors) == p - 1
assert all(trial_prime(q) for q in factors)
witness = 2
assert pow(witness, p - 1, p) == 1
residues = {q: pow(witness, (p - 1) // q, p) for q in factors}
assert all(gcd(r - 1, p) == 1 for r in residues.values())

rows = []
for q in (7, 13):
    e = 6
    evaluation_point = q ** (2 * e) + q**e + 1
    constant_term = (-evaluation_point**2) % p
    value = evaluation_point**2 + constant_term
    assert 0 <= constant_term < p < 9 * q ** (2 * e)
    assert value > 0 and value % p == 0
    rows.append({
        "q": q,
        "e": e,
        "E": evaluation_point,
        "F_coefficients_descending": [1, 0, constant_term],
        "F_E": value,
        "F_E_div_p": value // p,
        "root_absolute_value_squared_upper_bound": 9 * q ** (2 * e),
    })

common = gcd(*(r["F_E"] for r in rows))
assert common == 7 * p
result = {
    "scope": "abstract numerical model, not an automorphic certificate",
    "prime": p,
    "trial_division_limit": isqrt(p),
    "p_minus_one_prime_factors": factors,
    "Lucas_witness": witness,
    "Lucas_residues": residues,
    "polynomials": rows,
    "evaluation_gcd": common,
    "evaluation_gcd_div_p": common // p,
}
destination = Path(__file__).with_name("host_strength_model_results.json")
destination.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
