"""Standard-library exact U3/combined gcds and recursive Lucas primality.

For each n>2 the complete prime factorization of n-1 and one witness a
are checked. For every prime r|n, these checks make the order of a mod r
equal to n-1, so n-1 divides r-1. Thus r>=n and n is prime.
No probable-prime test or external symbolic package is used.
"""
from pathlib import Path
from math import gcd
import hashlib
import json

HERE = Path(__file__).resolve().parent
names = ('harmonic_hecke_exact_data.json', 'gl2_higher2_certificate.json',
         'u3_comparison_gcd_exploration.json', 'combined_exploration.json',
         'prime_certificates.json')
sources = {n: json.loads((HERE/n).read_text()) for n in names}
cert = sources['prime_certificates.json']
proved = set()
for node in cert['nodes']:
    n = node['n']
    assert n not in proved and isinstance(n, int)
    factors = {int(q): a for q, a in node['factors_n_minus_1'].items()}
    if n == 2:
        assert not factors and node['witness'] is None
        proved.add(2)
        continue
    assert n > 2
    product = 1
    for q, a in factors.items():
        assert q in proved and 0 < a and isinstance(a, int)
        product *= q**a
    assert product == n-1
    a = node['witness']
    assert isinstance(a, int) and 1 < a < n
    assert pow(a, n-1, n) == 1
    assert all(gcd(pow(a, (n-1)//q, n)-1, n) == 1 for q in factors)
    proved.add(n)
assert set(cert['targets']) <= proved


def evaluate(polynomial, point):
    value = 0
    for c in polynomial:
        assert isinstance(c, int)
        value = value*point+c
    return value


def check_factorization(value, factors):
    product = 1
    for qtext, a in factors.items():
        q = int(qtext)
        assert q in proved and isinstance(a, int) and a > 0
        product *= q**a
    assert product == value


u3 = {d['e']: d for d in sources['harmonic_hecke_exact_data.json']['degrees']}
gl2 = {d['e']: d for d in sources['gl2_higher2_certificate.json']['degrees']}
ur = {d['e']: d for d in sources['u3_comparison_gcd_exploration.json']}
cr = {d['e']: d for d in sources['combined_exploration.json']}
assert set(u3) == set(gl2) == set(ur) == set(cr) == {14, 16, 18}
reports = []
for e in sorted(u3):
    degree = u3[e]
    d = len(degree['swap_signs'])
    assert len(degree['evaluation_points']) == d
    assert len(degree['evaluation_matrix']) == d
    assert all(len(row) == d for row in degree['evaluation_matrix'])
    assert len(degree['harmonic_basis_columns']) == len(degree['source_orbits'])
    assert all(len(row) == d for row in degree['harmonic_basis_columns'])
    u = {r['p']: r for r in u3[e]['results']}
    g = {r['p']: r for r in gl2[e]['results']}
    assert set(u) == set(g) == {7, 13}
    unitary_values, combined_values = [], []
    for p in (7, 13):
        for name in ('operator_0', 'operator_omega', 'rational_real_form_operator',
                     'transformed_evaluations_0', 'transformed_evaluations_omega'):
            assert len(u[p][name]) == d
            assert all(len(row) == d for row in u[p][name])
        assert len(u[p]['charpoly_coefficients']) == d+1
        upoint, gpoint = 1+p**e+p**(2*e), 1+p**(2*e)
        uv = evaluate(u[p]['charpoly_coefficients'], upoint)
        gv = evaluate(g[p]['charpoly_coefficients'], gpoint)
        assert upoint == u[p]['comparison_point'] and uv == u[p]['comparison_value']
        assert gpoint == g[p]['evaluation_point'] and gv == g[p]['evaluation']
        unitary_values.append(uv)
        combined_values.append(uv*gv)
    ug, cg = gcd(*unitary_values), gcd(*combined_values)
    assert unitary_values == ur[e]['values'] and ug == ur[e]['gcd']
    assert combined_values == cr[e]['combined_values'] and cg == cr[e]['gcd']
    check_factorization(ug, ur[e]['factorization'])
    check_factorization(cg, cr[e]['factorization'])
    reports.append({'e': e, 'U3_dimension': len(u3[e]['swap_signs']),
                    'GL2_dimension': gl2[e]['dimension'],
                    'U3_gcd': ug, 'U3_factorization': ur[e]['factorization'],
                    'combined_gcd': cg, 'combined_factorization': cr[e]['factorization'],
                    'large_combined_primes': sorted(int(q) for q in cr[e]['factorization']
                                                    if int(q) >= 2**31)})
report = {'status': 'PASS exact comparisons and recursive Lucas prime certificates',
          'model_replays_required_separately': True,
          'input_sha256': {n: hashlib.sha256((HERE/n).read_bytes()).hexdigest()
                          for n in names},
          'prime_nodes_checked': len(proved), 'degrees': reports}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'status': report['status'], 'prime_nodes_checked': len(proved),
                  'summary': [{'e': r['e'], 'U3_dimension': r['U3_dimension'],
                               'combined_factorization': r['combined_factorization'],
                               'large_combined_primes': r['large_combined_primes']}
                              for r in reports]}))
