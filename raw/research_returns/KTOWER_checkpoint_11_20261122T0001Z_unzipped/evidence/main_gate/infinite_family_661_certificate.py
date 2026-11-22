"""Small exact residue checks used in KT-TWOFIELD-FAMILY.

This does not recompute the two generalized Bernoulli seed residues;
those are certified by bernoulli_661_certificate.py.
"""
from math import comb
import json


def main():
    p = 661
    bernoulli = [1]
    for m in range(1, 63):
        # Every denominator m+1 is less than p and invertible modulo p.
        bernoulli.append(
            -sum(comb(m + 1, j) * bernoulli[j] for j in range(m))
            * pow(m + 1, -1, p) % p
        )
    inert_residue = (1 - pow(3, 536, p)) % p
    assert bernoulli[62] == 511
    assert inert_residue == 50
    assert 268 % 3 == 1 and 330 % 3 == 0
    assert (268 + 330) % 660 == 598
    assert (268 + 2 * 330) % 660 == 268
    result = {
        "status": "PASS",
        "prime": p,
        "B62_mod661": bernoulli[62],
        "one_minus_3_to_536_mod661": inert_residue,
        "family_e": "268 + 330*t",
        "family_K_degree": "536 + 660*t",
        "e_residue_even_t": 268,
        "e_residue_odd_t": 598,
        "method": "standard-library Bernoulli recurrence modulo 661",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
