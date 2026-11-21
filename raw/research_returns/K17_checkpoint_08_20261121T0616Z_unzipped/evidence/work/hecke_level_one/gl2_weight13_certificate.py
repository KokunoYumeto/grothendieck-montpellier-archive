"""Exact standard-library certificate for the proved weight-13 level-3 basis.

The modularity/basis proof is in gl2_weight13_section.tex.  This program
reconstructs all series, Hecke matrices, determinants and factorizations.
It does not use the exploratory report or any unitary-group computation.
"""
from pathlib import Path
from math import comb, isqrt
import json

N = 55

def mul(a, b):
    out = [0] * (N + 1)
    for i, x in enumerate(a):
        if x:
            for j in range(min(len(b), N + 1 - i)):
                out[i+j] += x * b[j]
    return out

def power(a, n):
    out = [1] + [0] * N
    for _ in range(n):
        out = mul(out, a)
    return out

def eta_product(factors, shift):
    out = [0] * shift + [1] + [0] * (N - shift)
    for scale, exponent in factors:
        for t in range(scale, N + 1, scale):
            factor = [0] * (N + 1)
            for k in range(N // t + 1):
                if exponent >= 0:
                    if k > exponent:
                        break
                    c = (-1)**k * comb(exponent, k)
                else:
                    c = comb(-exponent+k-1, k)
                factor[t*k] = c
            out = mul(out, factor)
    return out

def chi(d):
    return 0 if d % 3 == 0 else 1 if d % 3 == 1 else -1

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def charpoly(m):
    tr = sum(m[i][i] for i in range(3))
    minors = sum(m[i][i]*m[j][j]-m[i][j]*m[j][i]
                 for i in range(3) for j in range(i+1, 3))
    return [1, -tr, minors, -det3(m)]

def evaluate(poly, x):
    out = 0
    for c in poly:
        out = out*x + c
    return out

def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

a = [1] + [6*sum(chi(d) for d in range(1, n+1) if n % d == 0)
           for n in range(1, N+1)]
b = eta_product([(3, 9), (1, -3)], 1)
D = eta_product([(1, 6), (3, 6)], 1)
basis = [mul(D, power(a, 7)), mul(D, mul(power(a, 4), b)),
         mul(D, mul(a, power(b, 2)))]
leading = [[f[n] for f in basis] for n in (1, 2, 3)]
assert leading == [[1, 0, 0], [36, 1, 0], [513, 21, 1]]
assert det3(leading) == 1

expected = {
    7: {
        'roots': [40250, 40250, -153502],
        'factors': {2:12, 3:14, 7:1, 13:4, 37:1, 43:2, 47:2, 61:1, 271:2},
        'evaluation': 2651744832098840875904898134016,
    },
    13: {
        'roots': [1284050, 1284050, -9397582],
        'factors': {2:18, 3:14, 7:2, 13:4, 19:1, 37:1, 47:2,
                    193:1, 337:2, 14551:2},
        'evaluation': 12646222259779542583967104682915874471936,
    },
}
results = []
for p, e in expected.items():
    columns = []
    raw = [[f[p*n] for f in basis] for n in (1, 2, 3)]
    for f in basis:
        v = [f[p*n] for n in (1, 2, 3)]
        c0 = v[0]
        c1 = v[1] - 36*c0
        c2 = v[2] - 513*c0 - 21*c1
        c = [c0, c1, c2]
        for n in range(1, N//p+1):
            target = f[p*n] + (chi(p)*p**12*f[n//p] if n % p == 0 else 0)
            assert target == sum(c[i]*basis[i][n] for i in range(3))
        columns.append(c)
    matrix = [[columns[j][i] for j in range(3)] for i in range(3)]
    poly = charpoly(matrix)
    r, s, t = e['roots']
    assert poly == [1, -(r+s+t), r*s+r*t+s*t, -r*s*t]
    E = p**12+1
    value = evaluate(poly, E)
    assert value == e['evaluation'] == (E-r)*(E-s)*(E-t)
    product = 1
    for prime, exponent in e['factors'].items():
        assert is_prime(prime)
        product *= prime**exponent
    assert product == value
    results.append({'p': p, 'initial_hecke_coefficient_rows': raw,
                    'matrix': matrix, 'charpoly_coefficients': poly,
                    'roots_with_multiplicity': e['roots'],
                    'evaluation_point': E, 'evaluation': value,
                    'prime_factorization': e['factors'],
                    'additional_coefficients_checked_through': N//p})

report = {'status': 'PASS: exact arithmetic for independently proved modular-form model',
          'precision': N, 'leading_coefficient_matrix': leading,
          'basis_coefficients_through_21': [f[:22] for f in basis],
          'results': results,
          'scope': 'No source-conductor, unitary transfer, or K-group assertion.'}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'status': report['status'], 'output': str(out), 'results': results}))
