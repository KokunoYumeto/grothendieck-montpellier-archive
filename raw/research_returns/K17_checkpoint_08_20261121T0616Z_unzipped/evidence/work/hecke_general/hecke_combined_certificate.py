"""Exact combination of separately proved full U3 and GL2 Hecke models.

No arithmetic source coverage or K-group conclusion is encoded here.
Each model has its own standalone reconstruction; this file only checks
the recorded full polynomial evaluations, gcds, factorizations, and ranges.
"""
from pathlib import Path
from math import gcd, isqrt
from hashlib import sha256
import json

HERE = Path(__file__).parent
U3_PATH = HERE / 'harmonic_hecke_exact_data.json'
GL2_PATH = HERE / 'gl2_general_certificate.json'

FACTORS = {
    6: {2:15, 3:19, 7:1, 13:5, 37:1, 47:3},
    8: {2:29, 3:31, 23:3, 401:3, 809:1, 13687:3},
    10: {2:54, 3:54, 43:1, 241:3, 1847:1, 9496386083:3},
    12: {2:58, 3:71, 5:2, 7:1, 13:8, 37:1, 47:1,
         28447:3, 300455201:3},
}

# These concise factorizations are additionally checked against the
# complete integral characteristic polynomials, not substituted for them.
GL2_FACTORS = {
    (8, 7): [([1, 1570772, -39368833865900], 2)],
    (8, 13): [([1, 790365212, 53944448738897860], 2)],
    (10, 7): [([1, -279803958, -127584561562048500,
                30590253082420358136355000], 2)],
    (10, 13): [([1, -8923939638, -6797158417228643929140,
                 194437243363096745461703318361400], 2)],
    (12, 7): [([1, 4119710398], 1),
              ([1, -994032438, -313864742351252973300,
                -1965630682954936067477202845000], 2)],
    (12, 13): [([1, -41718377201762], 1),
               ([1, 36771219031962, -143657636498003570201050740,
                 -7357825592607362422723731960417071505800], 2)],
}


def evaluate(poly, x):
    out = 0
    for c in poly:
        out = out*x+c
    return out


def multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


u3 = json.loads(U3_PATH.read_text())
gl2 = json.loads(GL2_PATH.read_text())
u3_degrees = {r['e']: r for r in u3['degrees']}
gl2_degrees = {r['e']: r for r in gl2['degrees']}
assert set(u3_degrees) == set(gl2_degrees) == set(FACTORS)
reports = []
for e in FACTORS:
    u = {r['p']: r for r in u3_degrees[e]['results']}
    g = {r['p']: r for r in gl2_degrees[e]['results']}
    assert set(u) == set(g) == {7, 13}
    rows = []
    for p in (7, 13):
        up, gp = u[p]['charpoly_coefficients'], g[p]['charpoly_coefficients']
        assert up[0] == gp[0] == 1
        assert all(isinstance(c, int) for c in up+gp)
        assert len(gp) == (2*e-5)//3+2
        if (e, p) in GL2_FACTORS:
            product = [1]
            for factor, multiplicity in GL2_FACTORS[e, p]:
                for _ in range(multiplicity):
                    product = multiply(product, factor)
            assert product == gp
        ue, ge = 1+p**e+p**(2*e), 1+p**(2*e)
        assert ue == u[p]['comparison_point']
        assert ge == g[p]['evaluation_point']
        uv, gv = evaluate(up, ue), evaluate(gp, ge)
        assert uv == u[p]['comparison_value'] != 0
        assert gv == g[p]['evaluation'] != 0
        rows.append({'p': p, 'U3_point': ue, 'GL2_point': ge,
                     'U3_evaluation': uv, 'GL2_evaluation': gv,
                     'combined_value': uv*gv})
    common = gcd(*(r['combined_value'] for r in rows))
    product = 1
    for q, exponent in FACTORS[e].items():
        assert prime(q)
        assert exponent > 0
        product *= q**exponent
    assert common == product
    reports.append({
        'e': e, 'comparison_K_degree_if_covered': 2*e,
        'results': rows, 'gcd': common,
        'factorization': FACTORS[e],
        'every_factor_trial_division_prime': True,
        'all_prime_factors_below_2pow31': all(q < 2**31 for q in FACTORS[e]),
    })
report = {
    'status': 'PASS: exact model comparison arithmetic only',
    'U3_data_sha256': sha256(U3_PATH.read_bytes()).hexdigest(),
    'GL2_data_sha256': sha256(GL2_PATH.read_bytes()).hexdigest(),
    'degrees': reports,
    'scope': 'Source coverage and Selmer/K-group deductions are separate.',
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({
    'status': report['status'], 'output': str(out),
    'summary': [{k: r[k] for k in ('e', 'gcd', 'factorization',
                                  'all_prime_factors_below_2pow31')}
                for r in reports],
}))
