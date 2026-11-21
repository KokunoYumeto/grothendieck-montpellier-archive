"""Exact three-prime U3 comparison; model certificates are separate."""
from pathlib import Path
from math import gcd, isqrt
import hashlib
import json

HERE = Path(__file__).resolve().parent
paths = [HERE.parent / 'harmonic_hecke_exact_data.json',
         HERE / 'harmonic_hecke_exact_data.json']
rows = []
for path in paths:
    data = json.loads(path.read_text())
    degree = next(d for d in data['degrees'] if d['e'] == 10)
    for result in degree['results']:
        p = result['p']
        point = 1 + p**10 + p**20
        value = 0
        for coefficient in result['charpoly_coefficients']:
            value = value * point + coefficient
        assert point == result['comparison_point']
        assert value == result['comparison_value']
        rows.append({'p': p, 'comparison_point': point,
                     'comparison_value': value})
assert sorted(r['p'] for r in rows) == [7, 13, 19]
common = gcd(*(r['comparison_value'] for r in rows))
factors = {2: 28, 3: 26, 241: 1, 1847: 1, 9496386083: 1}
product = 1
for q, exponent in factors.items():
    assert q >= 2 and all(q % d for d in range(2, isqrt(q) + 1))
    product *= q**exponent
assert product == common
assert common == 2884262624361916357406610016104873984
report = {
    'status': 'PASS exact U3 three-prime comparison arithmetic',
    'input_sha256': [hashlib.sha256(p.read_bytes()).hexdigest() for p in paths],
    'results': rows,
    'gcd': common,
    'factorization': factors,
    'scope': 'Full model reconstruction is in the separate harmonic certificates.',
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'status': report['status'], 'gcd': common,
                  'factorization': factors, 'output': str(out)}))
