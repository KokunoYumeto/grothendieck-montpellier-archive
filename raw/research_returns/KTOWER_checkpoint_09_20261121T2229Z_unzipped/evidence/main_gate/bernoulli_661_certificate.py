"""Exact, standard-library certificate for the common Eisenstein prime 661.

No floating-point arithmetic, probabilistic primality, or external CAS is used.
It checks generalized Bernoulli residues by both Bernoulli polynomials and
independent finite character power sums modulo p^2, and the rational reflected
Bernoulli component by the defining recurrence modulo p.
"""
from math import comb, gcd, isqrt
from pathlib import Path
import json


def character(f, a):
    r = a % f
    if r == 0:
        return 0
    if f == 3:
        return 1 if r == 1 else -1
    if f == 7:
        return 1 if r in (1, 2, 4) else -1
    raise ValueError("Only the two specified primitive quadratic characters")


def bernoulli_mod(p, limit):
    assert limit + 1 < p
    b = [1]
    for m in range(1, limit + 1):
        numerator = sum(comb(m + 1, j) * b[j] for j in range(m)) % p
        b.append((-numerator * pow(m + 1, -1, p)) % p)
    return b


def main():
    p, e = 661, 268
    n = 2 * e + 1
    assert all(p % d for d in range(2, isqrt(p) + 1))
    assert p > n + 1 and gcd(p, 42 * n) == 1
    b = bernoulli_mod(p, n)
    rows = []
    for f in (3, 7):
        poly = 0
        for a in range(1, f):
            value = sum(comb(n, j) * b[j] * pow(a, n - j, p)
                        * pow(f, j - 1, p) for j in range(n + 1)) % p
            poly = (poly + character(f, a) * value) % p
        divided = poly * pow(n, -1, p) % p
        power_sum = sum(character(f, a) * pow(a, n, p * p)
                        for a in range(1, f * p + 1)) % (p * p)
        assert power_sum % p == 0
        from_sum = (power_sum // p) * pow(f, -1, p) % p
        assert poly == from_sum == divided == 0
        rows.append({"conductor": f, "generalized_B_mod_p": poly,
                     "generalized_B_div_n_mod_p": divided,
                     "character_power_sum_mod_p_squared": power_sum,
                     "generalized_B_from_power_sum_mod_p": from_sum})
    reflected_index = p - 1 - e
    assert reflected_index == 392 and b[reflected_index] == 53
    out = {"status": "PASS", "prime": p, "degree_parameter": e,
           "weight": n, "rows": rows, "reflected_B_index": reflected_index,
           "reflected_B_mod_p": b[reflected_index],
           "rational_K_group": "K_536(Z){661}=0 by carried K17-REFLECTOR"}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()

