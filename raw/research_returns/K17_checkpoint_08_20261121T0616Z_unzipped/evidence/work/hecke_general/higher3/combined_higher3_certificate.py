"""Exact complete E=-3 comparison gcds, without large primality claims."""
from pathlib import Path
from hashlib import sha256
from math import gcd, isqrt, prod
import json

HERE = Path(__file__).resolve().parent
UP = HERE/'harmonic_hecke_exact_data.json'
GP = HERE/'gl2_higher3_certificate.json'
SMALL = {
    20: {2:213, 3:257, 5:6, 61:2, 241:1, 175427911:3},
    22: {2:298, 3:299, 5:29, 19:2, 53:3, 67:1},
    24: {2:298, 3:372, 5:8, 7:1, 13:9, 37:1, 97:1,
         28447:1, 300455201:1},
}
RESIDUAL = {
    20: {9496386083:1, 552972895573825165951583191:3},
    22: {80348736972167:1,
         2789260013036301774436972122687974510453:3},
    24: {3369865772726176603506574274451733385689247:3},
}
U3_DIMS = {20:39, 22:52, 24:64}


def evaluate(poly, point):
    value = 0
    for coefficient in poly:
        value = value*point+coefficient
    return value


def trial_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


unitary = {r['e']:r for r in json.loads(UP.read_text())['degrees']}
classical = {r['e']:r for r in json.loads(GP.read_text())['degrees']}
assert set(unitary) == set(classical) == set(SMALL) == set(RESIDUAL)
rows = []
for e in SMALL:
    us = {r['p']:r for r in unitary[e]['results']}
    gs = {r['p']:r for r in classical[e]['results']}
    assert set(us) == set(gs) == {7, 13}
    details, combined_values = [], []
    for p in (7, 13):
        up, gp = us[p]['charpoly_coefficients'], gs[p]['charpoly_coefficients']
        assert up[0] == gp[0] == 1
        assert all(isinstance(a, int) for a in up+gp)
        assert len(up)-1 == U3_DIMS[e] == us[p]['dimension']
        assert len(gp)-1 == (2*e-5)//3+1 == classical[e]['dimension']
        ue, ge = 1+p**e+p**(2*e), 1+p**(2*e)
        uv, gv = evaluate(up, ue), evaluate(gp, ge)
        assert ue == us[p]['comparison_point']
        assert ge == gs[p]['evaluation_point']
        assert uv == us[p]['comparison_value'] != 0
        assert gv == gs[p]['evaluation'] != 0
        combined_values.append(uv*gv)
        details.append({'p':p, 'unitary_point':ue, 'classical_point':ge,
                        'unitary_value':uv, 'classical_value':gv,
                        'combined_value':uv*gv})
    common = gcd(*combined_values)
    assert all(q < 2**31 and trial_prime(q) for q in SMALL[e])
    assert all(m >= 2**31 and a > 0 for m, a in RESIDUAL[e].items())
    assert all(gcd(m, 42) == 1 for m in RESIDUAL[e])
    product_value = prod(q**a for q, a in SMALL[e].items())
    product_value *= prod(m**a for m, a in RESIDUAL[e].items())
    assert common == product_value
    rows.append({
        'e':e, 'conditional_K_degree':2*e,
        'unitary_dimension':U3_DIMS[e],
        'classical_dimension':classical[e]['dimension'],
        'results':details, 'comparison_gcd':common,
        'proved_primes_below_2pow31':SMALL[e],
        'residual_integers_with_multiplicities':RESIDUAL[e],
        'residual_primality_assumed':False,
        'exact_factor_product_verified':True,
    })
report = {
    'status':'PASS: complete comparison gcds and exact residual decomposition',
    'unitary_data_sha256':sha256(UP.read_bytes()).hexdigest(),
    'classical_data_sha256':sha256(GP.read_bytes()).hexdigest(),
    'small_factor_primality':'exact trial division through the integer square root',
    'residual_integers_are_not_asserted_prime':True,
    'degrees':rows,
    'scope':'Finite comparisons only; full model replay and arithmetic coverage separate.',
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'status':report['status'], 'output':str(out),
                  'summary':[{k:r[k] for k in
                              ('e','unitary_dimension','classical_dimension',
                               'proved_primes_below_2pow31',
                               'residual_integers_with_multiplicities')} for r in rows]},
                 indent=2))
