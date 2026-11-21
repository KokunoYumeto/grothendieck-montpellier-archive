"""Exact finite discriminator for the projected theta scalar identity."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json


def bernoulli(limit):
    values = [Fraction(1)]
    for n in range(1, limit + 1):
        values.append(-sum(Fraction(comb(n + 1, j)) * values[j]
                           for j in range(n)) / (n + 1))
    return values


def theta_power(m, limit):
    ans = [1] + [0] * limit
    for _ in range(m):
        nxt = ans.copy()
        a = 1
        while a * a <= limit:
            for n in range(a * a, limit + 1):
                nxt[n] += 2 * ans[n - a * a]
            a += 1
        ans = nxt
    return ans


def main():
    p, b, m = 31, 17, 35
    B = bernoulli(b)
    rows = []
    rm, r4 = theta_power(m, 7), theta_power(4, 7)
    for d in (3, 7):
        chi = [0] + [1 if pow(a, (d - 1) // 2, d) == 1 else -1
                     for a in range(1, d)]
        beta = sum(Fraction(comb(b, j)) * B[j] * Fraction(d ** j, d)
                   * sum(chi[a] * a ** (b - j) for a in range(d))
                   for j in range(b + 1)) / b
        assert beta.denominator % p
        residue = beta.numerator * pow(beta.denominator, -1, p) % p
        mod = p * p
        omega = [0] + [pow(a, p, mod) for a in range(1, p)]
        numerator = sum(a * chi[a % d]
                        * pow(omega[a % p], b - 1, mod)
                        for a in range(1, d * p + 1)) % mod
        assert numerator % p == 0
        independent = numerator // p * pow(d, -1, p) % p
        assert independent == residue
        assert rm[d] % p == r4[d] % p
        rows.append({"D": -d, "beta17_exact": str(beta),
                     "beta17_mod_p": residue,
                     "independent_teichmuller_mod_p": independent,
                     "cohen_coefficient_mod_p": (-residue) % p,
                     "theta35_coefficient_exact": rm[d],
                     "theta4_coefficient_exact": r4[d],
                     "normalized_plus_coefficient_mod_p": rm[d] % p})
    determinant = (rows[0]["normalized_plus_coefficient_mod_p"]
                   * rows[1]["cohen_coefficient_mod_p"]
                   - rows[1]["normalized_plus_coefficient_mod_p"]
                   * rows[0]["cohen_coefficient_mod_p"]) % p
    assert [r["cohen_coefficient_mod_p"] for r in rows] == [26, 16]
    assert [r["normalized_plus_coefficient_mod_p"] for r in rows] == [1, 2]
    assert determinant == 26
    report = {"finding_id": "KT-KOHNEN-THETA-NONCONGRUENCE", "p": p,
              "weight_twice": m, "rows": rows,
              "determinant_mod_p": determinant, "status": "PASS",
              "scope": "Finite scalar-congruence discriminator only; the plus-coefficient formula is proved in the accompanying text, not by this computation."}
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
