"""Exact single-example discriminator; no range or asymptotic claim."""
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
import json


def bernoulli(limit):
    ans = [Fraction(1)]
    for n in range(1, limit + 1):
        ans.append(-sum(Fraction(comb(n + 1, j)) * ans[j]
                        for j in range(n)) / (n + 1))
    return ans


def main():
    p, f, b = 31, 79, 17
    assert all(p % q for q in range(2, isqrt(p) + 1))
    assert all(f % q for q in range(2, isqrt(f) + 1))
    chi = [0] + [1 if pow(a, (f - 1) // 2, f) == 1 else -1
                 for a in range(1, f)]
    assert sum(chi) == 0 and all(chi[-a] == -chi[a] for a in range(1, f))
    values = bernoulli(b)

    def beta(n):
        return sum(Fraction(comb(n, j)) * values[j] * Fraction(f ** j, f)
                   * sum(chi[a] * a ** (n - j) for a in range(f))
                   for j in range(n + 1)) / n

    def residue(x):
        assert x.denominator % p
        return x.numerator * pow(x.denominator, -1, p) % p

    b1, b3, bb = beta(1), beta(3), beta(b)
    # Independent defining conductor-f*p sum, keeping precision p^2.
    mod = p * p
    omega = [0] + [pow(a, p, mod) for a in range(1, p)]
    numerator = sum(a * chi[a % f] * pow(omega[a % p], b - 1, mod)
                    for a in range(1, f * p + 1)) % mod
    assert numerator % p == 0
    teich = numerator // p * pow(f, -1, p) % p
    assert b1 == -5 and b3 == 992 and residue(bb) == teich == 20
    assert 4 * 20 - 1 == f and (f * (-residue(bb))) % p == 1
    report = {
        "finding_id": "KT-JACOBI-THIRD-UNIT-NONIMPLICATION",
        "p": p, "D": -f, "b": b, "e": b - 1,
        "B1_exact": str(b1), "class_number": int(-b1),
        "beta3_exact": str(b3), "beta3_mod_p": residue(b3),
        "beta17_exact": str(bb), "beta17_mod_p": residue(bb),
        "independent_teichmuller_mod_p": teich,
        "heat_coefficient_n_r": [20, 1], "heat_coefficient_mod_p": 1,
        "discriminant_bound": 3 * p + 6,
        "scope": "One valid field selected by a unit heat coefficient need not have the third unit; does not disprove existence of a different field with all three units.",
        "status": "PASS",
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
