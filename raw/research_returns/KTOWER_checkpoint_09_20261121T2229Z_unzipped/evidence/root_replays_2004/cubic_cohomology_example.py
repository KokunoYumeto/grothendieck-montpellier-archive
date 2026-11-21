"""Exact tiny example separating raw H2 from auxiliary-unit vanishings.

No class-group computation or Massey nonvanishing is asserted.  The
cohomological consequence is the separately proved local quotient (CC.3).
"""
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
import hashlib
import json


def bernoulli_numbers(n):
    out = [Fraction(1)]
    for j in range(1, n + 1):
        out.append(-sum(Fraction(comb(j + 1, i)) * out[i]
                        for i in range(j)) / (j + 1))
    return out


def main():
    p, conductor, e = 7, 43, 2
    assert all(conductor % q for q in range(2, isqrt(conductor) + 1))
    assert conductor % 4 == 3 and p > 3 and (2 * e) % (p - 1)

    def character(x):
        if x % conductor == 0:
            return 0
        value = pow(x, (conductor - 1) // 2, conductor)
        assert value in (1, conductor - 1)
        return 1 if value == 1 else -1

    first = sum(character(x) * x for x in range(1, conductor + 1))
    first = Fraction(first, conductor)
    assert first == -1
    numbers = bernoulli_numbers(5)
    rows = []
    for a, expected in ((e, 5), (2 * e, 3)):
        total = 0
        for x in range(1, conductor * p + 1):
            if x % p == 0:
                continue
            # x^p is the Teichmuller lift of x mod p, modulo p^2.
            teich = pow(x, p, p * p)
            assert pow(teich, p - 1, p * p) == 1
            total += character(x) * x * pow(teich, a, p * p)
        numerator = total % (p * p)
        assert numerator % p == 0
        residue = (numerator // p) * pow(conductor, -1, p) % p

        n = a + 1
        beta = sum(Fraction(comb(n, j)) * numbers[j]
                   * Fraction(conductor) ** (j - 1)
                   * sum(character(x) * x ** (n - j)
                         for x in range(1, conductor + 1))
                   for j in range(n + 1)) / n
        assert beta.denominator % p
        beta_residue = beta.numerator * pow(beta.denominator, -1, p) % p
        assert residue == beta_residue == expected
        rows.append({'twist_exponent': a,
                     'complete_conductor': conductor * p,
                     'numerator_mod_p_squared': numerator,
                     'B1_residue': residue,
                     'ordinary_index': n,
                     'normalized_generalized_Bernoulli': str(beta),
                     'exact_rational_residue': beta_residue})
    assert pow(conductor, e - 1, p) == 1
    report = {'status': 'PASS', 'p': p, 'e': e, 'D': -conductor,
              'B1_eta': str(first), 'three_units': True, 'rows': rows,
              'local_H2_quotient_prime': conductor,
              'local_H2_condition': 'q^(e-1)=1 mod p',
              'scope': 'Exact Bernoulli units and local quotient condition; no specific Massey-class nonvanishing',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
