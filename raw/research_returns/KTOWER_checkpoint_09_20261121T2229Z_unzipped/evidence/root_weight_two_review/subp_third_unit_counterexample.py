"""One exact counterexample to automatic third units from a sub-p seed."""
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
import hashlib
import json


def main():
    p, f, b = 83, 43, 43
    for q in (p, f):
        assert all(q % r for r in range(2, isqrt(q) + 1))
    chi = [0] + [1 if pow(a, (f - 1) // 2, f) == 1 else -1
                 for a in range(1, f)]
    B = [Fraction(1)]
    for n in range(1, b + 1):
        B.append(-sum(comb(n + 1, j) * B[j] for j in range(n)) / (n + 1))

    def beta(n):
        return sum(comb(n, j) * B[j] * Fraction(f ** j, f)
                   * sum(chi[a] * a ** (n - j) for a in range(f))
                   for j in range(n + 1)) / n

    mod = lambda x: x.numerator * pow(x.denominator, -1, p) % p
    b1, b3, bb = beta(1), beta(3), beta(b)
    # Independent conductor-f*p sum with Teichmuller lifts modulo p^2.
    modulus = p * p
    lifted = [0] + [pow(pow(a, p, modulus), b - 1, modulus)
                     for a in range(1, p)]
    numerator = sum(a * chi[a % f] * lifted[a % p]
                    for a in range(1, f * p + 1)) % modulus
    assert numerator % p == 0
    direct = numerator // p * pow(f, -1, p) % p
    assert b1 == -1 and b3 == 166 and mod(bb) == direct == 76
    assert p % 4 == f % 4 == 3 and f <= p - 4 and (2 * (b - 1)) % (p - 1)
    report = {'finding_id': 'KT-SUBP-SEED-THIRD-UNIT-NONIMPLICATION',
              'p': p, 'D': -f, 'b': b, 'e': b - 1,
              'B1_exact': str(b1), 'class_number': int(-b1),
              'beta3_exact': str(b3), 'beta3_mod_p': mod(b3),
              'beta43_exact': str(bb), 'beta43_mod_p': mod(bb),
              'independent_teichmuller_mod_p': direct,
              'bound_p_minus4': p - 4,
              'scope': 'A field below p with the first two units can fail the third unit. Does not disprove existence of another field, and gives no new rational Selmer vanishing.',
              'status': 'PASS',
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
