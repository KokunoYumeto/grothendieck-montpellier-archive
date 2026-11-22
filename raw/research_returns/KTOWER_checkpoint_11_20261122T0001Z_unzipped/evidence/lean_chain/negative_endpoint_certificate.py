"""Small exact certificate: exceptional factors and finite Vandiver inputs.

Only standard-library arithmetic. No O(p) scan and no Vandiver product
evaluation: this certificate alone proves no new component vanishing.
"""
from fractions import Fraction
from math import comb, gcd, isqrt
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

DATA = (
    (34, 2577687858367, 6, {17: 1, 151628697551: 1},
     {2: 1, 5: 2, 11: 1, 17: 1, 16216973: 1}, 7, 12, 6),
    (36, -26315271553053477373, 1919190,
     {26315271553053477373: 1},
     {2: 2, 3: 1, 7: 1, 17: 1, 41: 1, 59: 1, 743: 1,
      8011: 1, 1279877: 1}, 29, 64, 3),
    (38, 2929993913841559, 6, {19: 1, 154210205991661: 1},
     {2: 2, 3: 1, 5: 1, 7: 1, 13: 1, 19: 1, 37: 1,
      367: 1, 109471: 1}, 10, 10, 2),
)


def product_factors(factors):
    value = 1
    for p, exponent in factors.items():
        assert exponent > 0
        value *= p ** exponent
    return value


def trial_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def factor_small(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def lucas_full_factor(n, factors, witness, established_primes):
    # Each prime divisor of n sees a unit of order n-1, hence is >=n.
    assert product_factors(factors) == n - 1
    assert all(q in established_primes for q in factors)
    assert pow(witness, n - 1, n) == 1
    residues = {}
    for q in factors:
        r = pow(witness, (n - 1) // q, n)
        assert gcd(r - 1, n) == 1
        residues[str(q)] = r
    return residues


def bernoulli_through(n):
    b = [Fraction(1)]
    for m in range(1, n + 1):
        b.append(-sum(Fraction(comb(m + 1, j)) * b[j]
                      for j in range(m)) / (m + 1))
    return b


def main():
    b = bernoulli_through(38)
    small_primes = set()
    for _, _, _, numerator_factors, p_factors, _, cofactor, _ in DATA:
        small_primes.update(p_factors)
        small_primes.update(q for q in numerator_factors if q < 2**31)
        small_primes.update(factor_small(cofactor))
    assert all(trial_prime(q) for q in small_primes)
    rows = []
    for n, numerator, denominator, num_factors, p_factors, g, cofactor, h in DATA:
        assert b[n] == Fraction(numerator, denominator)
        assert product_factors(num_factors) == abs(numerator)
        large = [p for p in num_factors if p >= 2**31]
        assert len(large) == 1
        p = large[0]
        p_residues = lucas_full_factor(p, p_factors, g, small_primes)
        q = cofactor * p + 1
        q_factors = factor_small(cofactor)
        q_factors[p] = q_factors.get(p, 0) + 1
        q_residues = lucas_full_factor(q, q_factors, h, small_primes | {p})
        z = pow(h, cofactor, q)
        assert z != 1 and pow(z, p, q) == 1
        assert p > n + 1 and denominator % p != 0
        assert numerator % p == 0 and numerator % (p*p) != 0
        rows.append({
            'negative_endpoint': -n // 2,
            'target_character_exponent': n,
            'mirror_exponent_mod_pminus1': (1-n) % (p-1),
            'bernoulli_index': n,
            'bernoulli_exact': str(b[n]),
            'numerator_factors': {str(r): e for r, e in num_factors.items()},
            'exceptional_prime': p,
            'pminus1_factors': {str(r): e for r, e in p_factors.items()},
            'p_lucas_witness': g,
            'p_lucas_residues': p_residues,
            'sqrt_p_floor': isqrt(p),
            'sqrt_half_floor': isqrt((p-1)//2),
            'order_of_target_character': (p-1)//gcd(n, p-1),
            'vandiver_product_terms': (p-1)//2,
            'auxiliary_prime_q': q,
            'qminus1_factors': {str(r): e for r, e in q_factors.items()},
            'q_lucas_witness': h,
            'q_lucas_residues': q_residues,
            'qminus1_over_p': cofactor,
            'order_p_root_mod_q': z,
            'vandiver_product_evaluated': False,
            'new_class_component_vanishing_proved': False,
        })
    source = Path(__file__).resolve()
    report = {
        'status': 'PASS exact factors, primality and auxiliary test inputs only',
        'checked_utc': datetime.now(timezone.utc).isoformat(),
        'script_sha256': sha256(source.read_bytes()).hexdigest(),
        'trial_proved_small_primes': sorted(small_primes),
        'largest_trial_divisor_bound': max(isqrt(r) for r in small_primes),
        'rows': rows,
        'scope': 'No O(p) scan; no Vandiver product evaluated; no endpoint extension.',
    }
    source.with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')
    print(report['status'])
    for row in rows:
        print(row['negative_endpoint'], row['exceptional_prime'],
              row['auxiliary_prime_q'], row['sqrt_p_floor'])


if __name__ == '__main__':
    main()
