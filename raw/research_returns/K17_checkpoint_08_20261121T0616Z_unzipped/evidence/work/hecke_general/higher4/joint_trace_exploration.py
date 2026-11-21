"""Exploratory joint trace tests on the complete saved level-three models.

This is finite-model arithmetic only. An arithmetic application requires a
separately proved simultaneous residual-congruence source theorem.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd, lcm
from hashlib import sha256
import json
import sys
sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def reduce_matrix(raw, modulus):
    rational = [[Fraction(x) for x in row] for row in raw]
    denominator = lcm(*(x.denominator for row in rational for x in row))
    assert gcd(denominator, modulus) == 1
    return [[x.numerator * pow(x.denominator, -1, modulus) % modulus
             for x in row] for row in rational], denominator


def multiply(a, b, modulus):
    return [[sum(x*y for x, y in zip(row, col)) % modulus
             for col in zip(*b)] for row in a]


def unit_determinant(a, modulus):
    a = [row[:] for row in a]
    value = 1
    pivots = []
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a))
                      if gcd(a[j][i], modulus) == 1), None)
        if pivot is None:
            return {'unit': False, 'unresolved_column': i,
                    'column_ideal_gcd': gcd(modulus, *(a[j][i] for j in range(i, len(a)))),
                    'unit_pivots': pivots}
        if pivot != i:
            a[pivot], a[i] = a[i], a[pivot]
            value = -value
        lead = a[i][i]
        inverse = pow(lead, -1, modulus)
        assert lead*inverse % modulus == 1
        pivots.append(lead)
        value = value*lead % modulus
        for j in range(i+1, len(a)):
            factor = a[j][i]*inverse % modulus
            for k in range(i+1, len(a)):
                a[j][k] = (a[j][k]-factor*a[i][k]) % modulus
            a[j][i] = 0
    value %= modulus
    assert gcd(value, modulus) == 1
    return {'unit': True, 'determinant': value, 'determinant_gcd': 1,
            'unit_pivots': pivots}


gl2_path = HERE/'gl2_higher4_certificate.json'
gl2 = json.loads(gl2_path.read_text())
reports = []
for e in (26, 28):
    u3_path = HERE/f'harmonic_hecke_e{e}_exact_data.json'
    support_path = HERE/f'residual_support_e{e}.json'
    u3 = json.loads(u3_path.read_text())['degrees'][0]
    classical = next(r for r in gl2['degrees'] if r['e'] == e)
    support = next(r for r in json.loads(support_path.read_text())['degrees'] if r['e'] == e)
    for modulus in support['residual_support_moduli']:
        for branch, model, matrix_key, point_key in (
                ('U3', u3, 'rational_real_form_operator', 'comparison_point'),
                ('GL2', classical, 'matrix', 'evaluation_point')):
            records = {r['p']: r for r in model['results']}
            assert set(records) == {7, 13}
            a, da = reduce_matrix(records[7][matrix_key], modulus)
            b, db = reduce_matrix(records[13][matrix_key], modulus)
            assert len(a) == len(b) and all(len(row) == len(a) for row in a+b)
            assert multiply(a, b, modulus) == multiply(b, a, modulus)
            for i in range(len(a)):
                a[i][i] = (a[i][i]-records[7][point_key]) % modulus
                b[i][i] = (b[i][i]-records[13][point_key]) % modulus
            trials = []
            for c in (1, 2, 3, 4):
                matrix = [[(a[i][j]+c*b[i][j]) % modulus for j in range(len(a))]
                          for i in range(len(a))]
                trial = {'coefficient': c, **unit_determinant(matrix, modulus)}
                trials.append(trial)
                if trial['unit']:
                    break
            row = {'e': e, 'modulus': modulus, 'branch': branch,
                   'dimension': len(a), 'commutator_zero_modulus': True,
                   'common_denominators': [da, db], 'trials': trials,
                   'model_sha256': digest(u3_path if branch == 'U3' else gl2_path),
                   'support_sha256': digest(support_path)}
            reports.append(row)
            print(json.dumps({'e': e, 'modulus': modulus, 'branch': branch,
                              'unit_found': any(t['unit'] for t in trials),
                              'last_trial': {k:v for k,v in trials[-1].items() if k!='unit_pivots'}}), flush=True)
out = HERE/'joint_trace_exploration.json'
out.write_text(json.dumps({'scope': 'Exploratory full finite-model arithmetic; no arithmetic source strengthening assumed',
                           'source_sha256': digest(Path(__file__)), 'cases': reports}, indent=2)+'\n')
