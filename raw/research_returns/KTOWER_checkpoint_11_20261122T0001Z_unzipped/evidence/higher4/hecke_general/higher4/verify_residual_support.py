"""Independent exact check of the higher4 comparison-support certificates.

This verifies complete polynomial evaluations and the displayed remaining
prime support. It does not replace the full-model arithmetic replays.
"""
from pathlib import Path
from math import gcd, isqrt, prod
from hashlib import sha256
import json
import sys
sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
B = 2**31

def prime_small(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))

def evaluate_direct(coefficients, value):
    # Independent of the collector's Horner evaluation.
    return sum(c*value**j for j,c in enumerate(reversed(coefficients)))

classical_path = HERE/'gl2_higher4_certificate.json'
classical = {r['e']:r for r in json.loads(classical_path.read_text())['degrees']}
checked = []
for e in (26,28,30):
    support_path = HERE/f'residual_support_e{e}.json'
    if not support_path.exists():
        continue
    support = json.loads(support_path.read_text())
    assert len(support['degrees']) == 1
    row = support['degrees'][0]
    assert row['e'] == e
    discovery_path = HERE/'fast'/f'harmonic_k{e-1}_exact_exploration.json'
    discovery = json.loads(discovery_path.read_text())
    assert sha256(discovery_path.read_bytes()).hexdigest() == row['discovery_data_sha256']
    assert sha256(classical_path.read_bytes()).hexdigest() == support['classical_data_sha256']
    assert discovery['e'] == e and discovery['k'] == e-1
    unitary_results = {r['p']:r for r in discovery['results']}
    classical_results = {r['p']:r for r in classical[e]['results']}
    details = {r['p']:r for r in row['results']}
    assert set(unitary_results) == set(classical_results) == set(details) == {7,13}
    values = []
    for p in (7,13):
        up = unitary_results[p]['charpoly_coefficients']
        gp = classical_results[p]['charpoly_coefficients']
        assert up[0] == gp[0] == 1
        uv = evaluate_direct(up, 1+p**e+p**(2*e))
        gv = evaluate_direct(gp, 1+p**(2*e))
        assert uv == unitary_results[p]['comparison_value'] == details[p]['unitary_value'] != 0
        assert gv == classical_results[p]['evaluation'] == details[p]['classical_value'] != 0
        assert uv*gv == details[p]['combined_value']
        values.append(uv*gv)
    common = gcd(values[0],values[1])
    assert common == row['combined_gcd']
    small = {int(p):a for p,a in row['proved_small_prime_factors'].items()}
    assert all(0 < a and p <= row['small_prime_bound'] < B and prime_small(p)
               for p,a in small.items())
    bounded = row['removed_bounded_integer_factors']
    assert all(isinstance(n,int) and 1 < n < B for n in bounded)
    initial = row['exact_remaining_integer']
    assert common == prod(p**a for p,a in small.items())*prod(bounded)*initial
    assert common == prod(p**a for p,a in small.items())*row['exact_remainder_after_small_prime_sieve']
    moduli = row['residual_support_moduli']
    assert all(isinstance(m,int) and m >= B and common % m == 0 for m in moduli)
    assert all(gcd(a,b)==1 for i,a in enumerate(moduli) for b in moduli[i+1:])
    product = prod(moduli)
    remainder, divisors = initial, []
    while remainder > 1:
        divisor = gcd(remainder,product)
        assert divisor > 1
        divisors.append(divisor)
        remainder //= divisor
    assert divisors == row['residual_support_divisions']
    assert len(up)-1 == row['unitary_dimension']
    assert classical[e]['dimension'] == row['classical_dimension']
    result = {
        'e':e, 'status':'PASS', 'combined_gcd':common,
        'proved_small_prime_factors':small,
        'removed_bounded_integer_factors':bounded,
        'residual_support_moduli':moduli,
        'residual_support_divisions':divisors,
        'large_primality_assumed':False,
        'support_sha256':sha256(support_path.read_bytes()).hexdigest(),
        'discovery_sha256':sha256(discovery_path.read_bytes()).hexdigest(),
        'classical_sha256':sha256(classical_path.read_bytes()).hexdigest(),
    }
    checked.append(result)
    print(json.dumps({k:result[k] for k in ('e','status','residual_support_moduli','large_primality_assumed')}),flush=True)
report = {'status':'PASS for every present degree', 'degrees':checked,
          'all_three_degrees_present':len(checked)==3,
          'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope':'Complete exact comparison and support arithmetic; full-model replays remain separate.'}
(HERE/'residual_support_independent_check.json').write_text(json.dumps(report,indent=2)+'\n')
