"""Exact common-vector witnesses for the two complete auxiliary operators.

An explicitly verified kernel vector with a unit coordinate makes every
linear-combination determinant zero modulo M, without assuming M prime.
The script does not infer a globally Eisenstein eigensystem or K vanishing.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd
from hashlib import sha256
import json
import sys
sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent


def reduced(raw, modulus):
    result = []
    for row in raw:
        out = []
        for entry in row:
            q = Fraction(entry)
            assert gcd(q.denominator, modulus) == 1
            out.append(q.numerator*pow(q.denominator, -1, modulus) % modulus)
        result.append(out)
    return result


def common_vector(a, b, modulus):
    rows = [row[:] for row in a+b]
    n = len(a)
    pivot_columns = []
    r = 0
    for c in range(n):
        pivot = next((j for j in range(r, len(rows))
                      if gcd(rows[j][c], modulus) == 1), None)
        if pivot is None:
            if any(rows[j][c] for j in range(r, len(rows))):
                return {'status':'nonunit pivot obstruction', 'column':c}
            continue
        rows[pivot], rows[r] = rows[r], rows[pivot]
        inv = pow(rows[r][c], -1, modulus)
        rows[r] = [x*inv % modulus for x in rows[r]]
        assert rows[r][c] == 1
        for j in range(len(rows)):
            if j == r:
                continue
            factor = rows[j][c]
            if factor:
                rows[j] = [(x-factor*y) % modulus for x,y in zip(rows[j],rows[r])]
        pivot_columns.append(c)
        r += 1
        if r == n:
            return {'status':'full column rank by unit pivots'}
    free = next(c for c in range(n) if c not in pivot_columns)
    vector = [0]*n
    vector[free] = 1
    for j,c in enumerate(pivot_columns):
        vector[c] = -rows[j][free] % modulus
    assert vector[free] == 1
    assert all(sum(x*y for x,y in zip(row,vector)) % modulus == 0 for row in a+b)
    return {'status':'verified common vector', 'vector':vector,
            'unit_coordinate':free, 'unit_coordinate_value':1,
            'unit_pivot_count':r,
            'consequence':'Every determinant det(A+cB) equals zero modulo M for every c; adjugate identity and unit coordinate.'}


glpath = HERE/'gl2_higher4_certificate.json'
gl = json.loads(glpath.read_text())
cases = []
for e in (26,28):
    upath = HERE/f'harmonic_hecke_e{e}_exact_data.json'
    spath = HERE/f'residual_support_e{e}.json'
    u = json.loads(upath.read_text())['degrees'][0]
    g = next(r for r in gl['degrees'] if r['e']==e)
    support = next(r for r in json.loads(spath.read_text())['degrees'] if r['e']==e)
    for modulus in support['residual_support_moduli']:
        for name,model,key,point,source in (
                ('U3',u,'rational_real_form_operator','comparison_point',upath),
                ('GL2',g,'matrix','evaluation_point',glpath)):
            records = {r['p']:r for r in model['results']}
            a = reduced(records[7][key],modulus)
            b = reduced(records[13][key],modulus)
            assert len(a)==len(b) and all(len(row)==len(a) for row in a+b)
            for i in range(len(a)):
                a[i][i] = (a[i][i]-records[7][point]) % modulus
                b[i][i] = (b[i][i]-records[13][point]) % modulus
            row = {'e':e,'modulus':modulus,'branch':name,'dimension':len(a),
                   'data_sha256':sha256(source.read_bytes()).hexdigest(),
                   **common_vector(a,b,modulus)}
            cases.append(row)
            print(json.dumps({k:v for k,v in row.items() if k not in ('vector','data_sha256')}),flush=True)
(HERE/'joint_trace_nullvectors.json').write_text(json.dumps({
    'scope':'Full finite-model two-auxiliary obstruction only; no global trace or arithmetic conclusion',
    'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'cases':cases},indent=2)+'\n')
