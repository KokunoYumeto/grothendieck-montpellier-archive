#!/usr/bin/env python3
"""Exact finite-ring checks for the matched-norm lemma, not arithmetic norms."""
from pathlib import Path
from math import comb
import hashlib
import json
from datetime import datetime, timezone


def mul(a, b, p):
    c = [0] * p
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < p:
                c[i + j] = (c[i + j] + x * y) % p
    return c


def add(a, b, p):
    return [(x + y) % p for x, y in zip(a, b)]


def monomial(j, p):
    a = [0] * p
    a[j] = 1
    return a


def tau(a, p):
    return [comb(a, j) % p if j <= a else 0 for j in range(p)]


def main():
    records = []
    for p in (5, 7, 11, 13, 17):
        norm = [0] * p
        for a in range(p):
            norm = add(norm, tau(a, p), p)
        assert norm == monomial(p - 1, p)
        assert norm[:3] == [0, 0, 0]

        count = 0
        for n in range(3, p):
            for a in range(p):
                action_minus_one = tau(a, p)
                action_minus_one[0] -= 1
                correction = mul(action_minus_one, monomial(n - 1, p), p)
                expected = [0] * p
                expected[n] = a
                assert correction[:n + 1] == expected[:n + 1]
                assert monomial(n - 1, p)[:2] == [0, 0]
                count += 1

        # In the group basis, D^(1) = -sum_i i sigma^(i-1).
        d1 = [0] * p
        for i in range(p):
            d1[(i - 1) % p] = -i % p
        # I^2 is spanned by sigma^j(1-2sigma+sigma^2).
        for j in range(p):
            v = [0] * p
            for shift, coefficient in ((0, 1), (1, -2), (2, 1)):
                v[(j + shift) % p] = coefficient % p
            assert sum(a * b for a, b in zip(d1, v)) % p == 0

        # An abstract binomial proper f=gamma*x has obstruction chi cup gamma.
        for a in range(p):
            for b in range(p):
                v = [b * x % p for x in monomial(1, p)]
                acted = mul(tau(a, p), v, p)
                d = [(x - y) % p for x, y in zip(acted, v)]
                assert d[:3] == [0, 0, a * b % p]

        records.append({
            'p': p,
            'highest_coefficient_corrections_checked': count,
            'norm_element': norm,
            'D1_annihilates_I2': True,
            'abstract_proper_system_obstruction_checked': True,
        })

    root = Path(__file__).resolve().parent
    script = Path(__file__).resolve()
    report = {
        'utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Exact polynomial and group-ring identities supporting CE.10, the norm-element representative adjustment, and the inversion-pairing annihilator. No ideal, number-field norm, Massey value, or Selmer nonvanishing is computed.',
        'status': 'PASS',
        'records': records,
        'script_sha256': hashlib.sha256(script.read_bytes()).hexdigest(),
    }
    output = root / 'matched_norm_check.json'
    output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'primes': len(records),
                      'correction_cases': sum(r['highest_coefficient_corrections_checked'] for r in records),
                      'report_sha256': hashlib.sha256(output.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()
