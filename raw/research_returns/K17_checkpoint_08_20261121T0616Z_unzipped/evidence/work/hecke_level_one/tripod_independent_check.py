"""Independent exact checks of the saved U3 and GL2 Hecke data.

Only the JSON outputs are read. No code from either discovery script and no
symbolic-algebra package is imported. The mathematical coverage/normalization
argument is in hecke_model_tripod_audit.md.
"""
from pathlib import Path
from itertools import permutations, product
from math import gcd, isqrt, prod
import json

BASE = Path(__file__).resolve().parent


def emul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c-b*d)


def econj(x):
    return (x[0]-x[1], -x[1])


def enorm(x):
    return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]


def edot(v, w):
    terms = [emul(econj(x), y) for x, y in zip(v, w)]
    return tuple(sum(t[j] for t in terms) for j in range(2))


def det3(a):
    return sum((1 if s in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1)
               * prod(a[i][s[i]] for i in range(3))
               for s in permutations(range(3)))


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def factor_product(fac):
    assert all(prime(int(p)) and e > 0 for p, e in fac.items())
    return prod(int(p)**e for p, e in fac.items())


# The invariant polynomial is rebuilt from the five partition coefficients.
u3 = json.loads((BASE/'u3_weight5_exact_exploration.json').read_text())
assert u3['weight'] == [5, 0, -5] and [r['p'] for r in u3['results']] == [7, 13]
terms = {}
for partition, coefficient in u3['coefficients']:
    assert sum(partition) == 5
    for exp in set(permutations(partition)):
        assert exp not in terms
        terms[exp] = coefficient
assert len(terms) == 21
partitions5 = [tuple(p) for p, _ in u3['coefficients']]
partitions4 = [(4, 0, 0), (3, 1, 0), (2, 2, 0), (2, 1, 1)]
lap_matrix = []
for target in partitions4:
    row = []
    for partition in partitions5:
        coefficient = 0
        for exp in set(permutations(partition)):
            for j, degree in enumerate(exp):
                output = list(exp)
                output[j] -= 1
                if degree and tuple(output) == target:
                    coefficient += degree*degree
        row.append(coefficient)
    lap_matrix.append(row)
def permutation_sign(s):
    return (-1)**sum(s[i] > s[j] for i in range(len(s)) for j in range(i+1, len(s)))
minor = sum(permutation_sign(s)*prod(lap_matrix[i][s[i]] for i in range(4))
            for s in permutations(range(4)))
assert minor != 0  # image has dimension four, so invariant harmonic kernel has dimension one.
lap = {}
for exp, coefficient in terms.items():
    for j, degree in enumerate(exp):
        if degree:
            out = list(exp)
            out[j] -= 1
            out = tuple(out)
            lap[out] = lap.get(out, 0) + coefficient*degree*degree
assert not any(lap.values())


def feval(x):
    return sum(c*prod(t**e for t, e in zip(x, exp))
               for exp, c in terms.items())


assert feval((1, 0, 0)) == u3['f_at_100'] == 2
points = [((1, 0), (1, 0), (0, 0)),
          ((1, 0), (1, 0), (1, 0)),
          ((1, 0), (0, 1), (2, 0)),
          ((2, 1), (-1, 0), (1, -1)),
          ((3, 0), (2, -1), (-1, 2))]
u3_reports = []
for record in u3['results']:
    p, pi = record['p'], record['pi']
    assert enorm(pi) == p and prime(p) and p % 3 == 1
    root = (-pi[0]*pow(pi[1], -1, p)) % p
    assert (root*root+root+1) % p == 0
    all_lines = {(1, a, b) for a, b in product(range(p), repeat=2)}
    all_lines |= {(0, 1, a) for a in range(p)} | {(0, 0, 1)}
    found = set()
    total = 0
    totals = [0]*len(points)
    for neighbor in record['neighbors']:
        ell = tuple(neighbor['line'])
        assert ell in all_lines and ell not in found
        found.add(ell)
        cols = neighbor['columns']
        assert len(cols) == 3
        for i, v in enumerate(cols):
            for j, w in enumerate(cols):
                assert edot(v, w) == ((p, 0) if i == j else (0, 0))
        nonzero = False
        for v in cols:
            reduction = tuple((a+b*root) % p for a, b in v)
            if any(reduction):
                nonzero = True
                scale = pow(next(x for x in reduction if x), -1, p)
                assert tuple(x*scale % p for x in reduction) == ell
        assert nonzero
        norms = [enorm(v[0]) for v in cols]
        assert norms == neighbor['first_row_norms'] and sum(norms) == p
        value = feval(norms)
        assert value == neighbor['polynomial_value']
        total += value
        for j, z in enumerate(points):
            totals[j] += feval([enorm(edot(v, z)) for v in cols])
    assert found == all_lines and len(found) == p*p+p+1
    assert total == 2*record['scaled_trace']
    for z, value in zip(points, totals):
        assert value == record['scaled_trace']*feval([enorm(t) for t in z])
    assert record['evaluation_difference'] == p**12+p**6+1-record['scaled_trace']
    u3_reports.append({'p': p, 'neighbors': len(found),
                       'scaled_trace': total//2,
                       'exact_additional_vector_checks': len(points)})


# Independent series construction by logarithmic derivatives, not binomial
# multiplication. If F=prod(1-q^d)^r_d then n*[q^n]F is the convolution with
# -sum_{d|k} d*r_d. The leading q-power is inserted only after this recurrence.
gl2 = json.loads((BASE/'gl2_weight13_exact_exploration.json').read_text())
assert gl2['weight'] == 13 and gl2['level'] == 3 and gl2['character'] == 'chi_minus3'
assert [r['p'] for r in gl2['results']] == [7, 13]
N = gl2['series_precision']


def eta_series(exponents, shift):
    r = [0]*(N+1)
    for scale, exponent in exponents:
        for d in range(scale, N+1, scale):
            r[d] += exponent
    logder = [0]*(N+1)
    for d in range(1, N+1):
        for k in range(d, N+1, d):
            logder[k] -= d*r[d]
    a = [1]+[0]*N
    for n in range(1, N+1):
        value = sum(logder[k]*a[n-k] for k in range(1, n+1))
        assert value % n == 0
        a[n] = value//n
    return [0]*shift+a[:N+1-shift]


def convolution(a, b):
    return [sum(a[i]*b[n-i] for i in range(n+1)) for n in range(N+1)]


def series_power(a, n):
    result = [1]+[0]*N
    for _ in range(n):
        result = convolution(result, a)
    return result


theta = [0]*(N+1)
bound = isqrt(4*N//3)+2
for a, b in product(range(-bound, bound+1), repeat=2):
    norm = enorm((a, b))
    if norm <= N:
        theta[norm] += 1
assert theta[0] == 1
for n in range(1, N+1):
    assert theta[n] == 6*sum(0 if d % 3 == 0 else 1 if d % 3 == 1 else -1
                             for d in range(1, n+1) if n % d == 0)
b = eta_series([(3, 9), (1, -3)], 1)
delta = eta_series([(1, 6), (3, 6)], 1)
basis = [convolution(delta, series_power(theta, 7)),
         convolution(delta, convolution(series_power(theta, 4), b)),
         convolution(delta, convolution(theta, series_power(b, 2)))]
assert [f[:16] for f in basis] == gl2['basis_first_terms']
assert [[f[i] for f in basis] for i in (1, 2, 3)] == [[1, 0, 0], [36, 1, 0], [513, 21, 1]]
gl2_reports = []
for record in gl2['results']:
    p = record['p']
    columns = []
    for f in basis:
        c0 = f[p]
        c1 = f[2*p]-36*c0
        c2 = f[3*p]-513*c0-21*c1
        c = [c0, c1, c2]
        for n in range(1, N//p+1):
            hecke = f[p*n] + (p**12*f[n//p] if n % p == 0 else 0)
            assert hecke == sum(c[j]*basis[j][n] for j in range(3))
        columns.append(c)
    matrix = [[columns[j][i] for j in range(3)] for i in range(3)]
    assert matrix == record['matrix']
    trace = sum(matrix[i][i] for i in range(3))
    second = sum(matrix[i][i]*matrix[j][j]-matrix[i][j]*matrix[j][i]
                 for i in range(3) for j in range(i+1, 3))
    coefficients = [1, -trace, second, -det3(matrix)]
    assert coefficients == record['charpoly_coefficients']
    x = p**12+1
    value = sum(c*x**(3-i) for i, c in enumerate(coefficients))
    assert value == record['evaluation']
    u = next(row for row in u3['results'] if row['p'] == p)
    combined = value*u['evaluation_difference']
    assert combined == record['combined_evaluation'] == factor_product(record['factorization'])
    gl2_reports.append({'p': p, 'matrix': matrix, 'charpoly': coefficients,
                       'verified_hecke_coefficients': N//p,
                       'combined_prime_factors': sorted(map(int, record['factorization']))})
assert factor_product(gl2['gcd_factorization']) == gl2['combined_gcd']
assert gcd(*(r['combined_evaluation'] for r in gl2['results'])) == gl2['combined_gcd']
result = {'status': 'PASS independent exact JSON-only verification',
          'harmonic_laplacian_rank_four_minor': minor,
          'u3': u3_reports, 'gl2': gl2_reports,
          'coverage': 'local and coefficient-model checks only; see audit for mathematical scope'}
(BASE/'tripod_independent_check.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
