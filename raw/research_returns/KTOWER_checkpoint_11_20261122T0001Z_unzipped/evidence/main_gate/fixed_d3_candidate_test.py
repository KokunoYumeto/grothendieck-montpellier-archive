"""Modest, fixed-bound discriminator for one proposed universal field.

No hit is not a proof of uniform nonvanishing.  Stop at the first hit;
the bound is deliberately fixed at 10000 rather than extended as a census.
"""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import hashlib
import json


def main():
    bound = 10000
    flags = bytearray(b'\1') * (bound + 1)
    flags[:2] = b'\0\0'
    for r in range(2, isqrt(bound) + 1):
        if flags[r]:
            flags[r * r:bound + 1:r] = b'\0' * ((bound - r * r) // r + 1)
    rows = []
    first_hit = None
    for p in range(31, bound + 1, 4):
        if not flags[p]:
            continue
        legendre = [-1] * p
        legendre[0] = 0
        for a in range(1, (p + 1) // 2):
            legendre[a * a % p] = 1
        character, prefix = (0, 1, -1), (0, 0, 1)
        ip = pow(p, -1, 3)
        residue = character[p % 3] * sum(
            a * legendre[a] * prefix[a * ip % 3] for a in range(1, p)) % p
        weighted = sum(a * legendre[a] for a in range(1, p // 3 + 1))
        # Independent exact rational B_2(chi_(3p))/2 at conductor 3p.
        beta2 = Fraction(sum(a * a * character[a % 3] * legendre[a % p]
                             for a in range(1, 3 * p)), 6 * p)
        assert beta2.denominator % p
        beta2_mod = beta2.numerator * pow(beta2.denominator, -1, p) % p
        assert residue == 6 * weighted % p == beta2_mod
        rows.append({'p': p, 'b': (p + 3) // 2, 'residue': residue,
                     'weighted_excess': weighted, 'beta2_exact': str(beta2)})
        if residue == 0:
            first_hit = p
            break
    report = {'finding_id': 'KT-FIXED-D3-CANDIDATE-TEST',
              'scope': 'Finite discriminator only, not an all-prime theorem or a new auxiliary-field existence claim.',
              'lower_bound': 31, 'upper_bound': bound, 'prime_condition': 'p == 3 mod 4',
              'tested_primes': len(rows), 'first_hit': first_hit,
              'two_normalizations_and_weighted_sum_agree': True,
              'rows': rows, 'status': 'PASS',
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'rows'}, indent=2))


if __name__ == '__main__':
    main()
