"""Exact fixed local-cost diagnostic for AM-DO-034; no theta nonvanishing test."""
from fractions import Fraction
from pathlib import Path
import json


def valuation(n, p):
    assert n != 0
    ans = 0
    while n % p == 0:
        ans += 1
        n //= p
    return ans


def order_mod(q, p):
    return next(h for h in range(1, p) if pow(q, h, p) == 1)


a = 42
records = []
for q in [29, 4615409, 5276377]:
    h = order_mod(q, 11)
    c = valuation(q**h - 1, 11)
    terms = [valuation(q**i - 1, 11) for i in range(1, a + 1)]
    assert h == 10 and c == 1
    assert [(i+1, v) for i, v in enumerate(terms) if v] == [
        (10, 1), (20, 1), (30, 1), (40, 1)]
    records.append(dict(q=q, order_mod_11=h, first_valuation=c,
                        terms=terms, sum=sum(terms)))

index_v = 6 * records[0]['sum']
gamma_v = 42 * sum(r['sum'] for r in records[1:])
assert index_v == 24 and gamma_v == 336
result = dict(
    finding='AM-DO-034',
    rank=a,
    absolute_real_degree=42,
    primes_over_29=6,
    ramification_degree_over_29=7,
    rational_level_index_exponent=42*a*a,
    index_residue_factor_exponent=6,
    g_primes_selected_places_each=42,
    q_records=records,
    index_11_valuation=index_v,
    raw_finite_gamma_11_valuation=gamma_v,
    unit_finite_scalar_cost_11=gamma_v//2,
    standard_coordinate_scalar_29_slope=str(Fraction(-3, 7)),
    ordinary_derivative_coefficient_29_lower_slope=str(Fraction(-6, 7)),
    scope='Exact local arithmetic diagnostic. Primality/splitting are K031 inputs; '
          'no full source record or numerical theta coefficient is verified.'
)
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print('PASS: rank42 index valuation24, finite Gamma valuation336, unit scalar cost168; '
      'six residue places and absolute ramification7 kept distinct.')
