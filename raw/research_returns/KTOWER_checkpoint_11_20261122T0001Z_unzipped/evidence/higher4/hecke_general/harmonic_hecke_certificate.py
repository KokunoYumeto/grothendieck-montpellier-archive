"""Independent standard-library certificate for full invariant U3 Hecke data.

Reconstructs all orbit bases and Laplacians, proves the saved kernel bases
complete by exact ranks, checks injective evaluations and all transformed
values, and verifies characteristic polynomials without Sympy.  Global
automorphic/source coverage is not a claim of this certificate.
"""
from pathlib import Path
from itertools import permutations, product
from collections import defaultdict
from fractions import Fraction as F
from math import gcd, isqrt
import argparse, hashlib, json

BASE = Path(__file__).resolve().parent
DATA = BASE/'harmonic_hecke_exact_data.json'
NEIGHBORS = BASE.parent/'hecke_level_one/u3_weight5_exact_exploration.json'
parser = argparse.ArgumentParser()
parser.add_argument('--data', type=Path, default=DATA)
parser.add_argument('--neighbors', type=Path, default=NEIGHBORS)
parser.add_argument('--report', type=Path, default=Path(__file__).with_suffix('.json'))
args = parser.parse_args()
DATA, NEIGHBORS = args.data, args.neighbors


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def conjugate(x):
    return x[0]-x[1], -x[1]


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def integer_rank(matrix):
    a = [list(map(int, row)) for row in matrix]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(rank+1, len(a)):
            if a[i][col]:
                x, y = a[rank][col], a[i][col]
                a[i] = [x*t-y*s for t, s in zip(a[i], a[rank])]
                common = gcd(*a[i])
                if common:
                    a[i] = [v//common for v in a[i]]
        rank += 1
        if rank == len(a):
            break
    return rank


def determinant(matrix):
    a = [list(map(F, row)) for row in matrix]
    det = F(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            det = -det
        value = a[j][j]
        det *= value
        for i in range(j+1, len(a)):
            ratio = a[i][j]/value
            for k in range(j+1, len(a)):
                a[i][k] -= ratio*a[j][k]
            a[i][j] = F(0)
    return det


def orbit_basis(k):
    exponents = [(a, b, k-a-b) for a in range(k+1) for b in range(k-a+1)]
    answer = set()
    for a in exponents:
        for b in exponents:
            if all((x-y) % 6 == 0 for x, y in zip(a, b)):
                answer.add(tuple(sorted(zip(a, b))))
    return sorted(answer)


def expand(orbits):
    return [sorted(set(permutations(o))) for o in orbits]


def laplacian_direct(source, target):
    columns = []
    for orbit in source:
        polynomial = defaultdict(int)
        for monomial in set(permutations(orbit)):
            for i, (a, b) in enumerate(monomial):
                if a and b:
                    out = list(monomial)
                    out[i] = (a-1, b-1)
                    polynomial[tuple(out)] += a*b
        column = []
        for orbit_out in target:
            coefficient = polynomial[orbit_out]
            assert all(polynomial[m] == coefficient for m in set(permutations(orbit_out)))
            column.append(coefficient)
        columns.append(column)
    return [list(row) for row in zip(*columns)]


def orbit_values(expanded, k, z, w):
    zp, wp = [], []
    for x in z:
        row = [(1, 0)]
        for _ in range(k):
            row.append(mul(row[-1], x))
        zp.append(row)
    for x in w:
        row = [(1, 0)]
        for _ in range(k):
            row.append(mul(row[-1], x))
        wp.append(row)
    values = []
    for orbit in expanded:
        total = (0, 0)
        for monomial in orbit:
            term = (1, 0)
            for i, (a, b) in enumerate(monomial):
                term = mul(term, mul(zp[i][a], wp[i][b]))
            total = add(total, term)
        values.append(total)
    return values


def harmonic_evaluate(expanded, k, H, z, w):
    values = orbit_values(expanded, k, z, w)
    return ([sum(H[i][j]*values[i][0] for i in range(len(H))) for j in range(len(H[0]))],
            [sum(H[i][j]*values[i][1] for i in range(len(H))) for j in range(len(H[0]))])


def transform_sum(expanded, k, H, point, neighbors):
    z, w = point
    d = len(H[0])
    zero, one = [0]*d, [0]*d
    for neighbor in neighbors:
        zz, ww = [], []
        for column in neighbor['columns']:
            zz.append(tuple(sum(conjugate(column[i])[j]*z[i] for i in range(3)) for j in range(2)))
            ww.append(tuple(sum(column[i][j]*w[i] for i in range(3)) for j in range(2)))
        a, b = harmonic_evaluate(expanded, k, H, zz, ww)
        zero = [x+y for x, y in zip(zero, a)]
        one = [x+y for x, y in zip(one, b)]
    return zero, one


def characteristic_polynomial(a):
    # Faddeev--LeVerrier with exact rational arithmetic.
    n = len(a)
    b = identity(n)
    coefficients = [F(1)]
    for k in range(1, n+1):
        b = matmul(a, b)
        c = -sum(b[i][i] for i in range(n))/F(k)
        coefficients.append(c)
        for i in range(n):
            b[i][i] += c
    assert all(x == 0 for row in b for x in row)
    return coefficients


def polynomial_product(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def evaluate(poly, x):
    value = 0
    for coefficient in poly:
        value = value*x+coefficient
    return value


data = json.loads(DATA.read_text())
neighbors = json.loads(NEIGHBORS.read_text())
neighbor_hash = hashlib.sha256(NEIGHBORS.read_bytes()).hexdigest()
for record in neighbors['results']:
    p, pi = record['p'], record['pi']
    assert p >= 2 and all(p % d for d in range(2, isqrt(p)+1))
    assert pi[0]**2-pi[0]*pi[1]+pi[1]**2 == p
    root = -pi[0]*pow(pi[1], -1, p) % p
    assert (root*root+root+1) % p == 0
    lines = set()
    for item in record['neighbors']:
        ell = tuple(item['line'])
        assert ell not in lines
        lines.add(ell)
        columns = item['columns']
        assert len(columns) == 3 and all(len(v) == 3 for v in columns)
        nonzero = False
        for i, column in enumerate(columns):
            red = tuple((a+b*root) % p for a, b in column)
            if any(red):
                nonzero = True
                c = pow(next(a for a in red if a), -1, p)
                assert tuple(a*c % p for a in red) == ell
            for j, other in enumerate(columns):
                products = [mul(conjugate(x), y) for x, y in zip(column, other)]
                value = tuple(sum(x[k] for x in products) for k in range(2))
                assert value == ((p, 0) if i == j else (0, 0))
        assert nonzero
    assert lines == ({(1, a, b) for a, b in product(range(p), repeat=2)} |
                     {(0, 1, a) for a in range(p)} | {(0, 0, 1)})

reports = []
for degree in data['degrees']:
    k, e = degree['k'], degree['e']
    assert e == k+1 and degree['highest_weight'] == [k, 0, -k]
    assert degree['neighbors_sha256'] == neighbor_hash
    source, target = orbit_basis(k), orbit_basis(k-1)
    assert source == [tuple(map(tuple, o)) for o in degree['source_orbits']]
    assert target == [tuple(map(tuple, o)) for o in degree['target_orbits']]
    lap = laplacian_direct(source, target)
    assert lap == [list(map(int, row)) for row in degree['laplacian']]
    H = [list(map(int, row)) for row in degree['harmonic_basis_columns']]
    d = len(H[0])
    assert integer_rank(lap) == len(target)
    assert d == len(source)-len(target) and integer_rank(H) == d
    assert all(x == 0 for row in matmul(lap, H) for x in row)
    signs = degree['swap_signs']
    index = {o: i for i, o in enumerate(source)}
    for i, orbit in enumerate(source):
        swapped = index[tuple(sorted((b, a) for a, b in orbit))]
        assert all(H[swapped][j] == signs[j]*H[i][j] for j in range(d))
    expanded = expand(source)
    points = degree['evaluation_points']
    A = []
    for z, w in points:
        a, b = harmonic_evaluate(expanded, k, H, [(x, 0) for x in z], [(x, 0) for x in w])
        assert not any(b)
        A.append(a)
    assert A == [list(map(int, row)) for row in degree['evaluation_matrix']]
    det = determinant(A)
    assert det and str(det) == degree['evaluation_determinant']
    values = []
    for record in degree['results']:
        p = record['p']
        ns = next(r['neighbors'] for r in neighbors['results'] if r['p'] == p)
        assert record['dimension'] == d and record['cosets'] == len(ns)
        B = [transform_sum(expanded, k, H, point, ns) for point in points]
        B0, B1 = [r[0] for r in B], [r[1] for r in B]
        assert B0 == [list(map(int, row)) for row in record['transformed_evaluations_0']]
        assert B1 == [list(map(int, row)) for row in record['transformed_evaluations_omega']]
        M0 = [list(map(F, row)) for row in record['operator_0']]
        M1 = [list(map(F, row)) for row in record['operator_omega']]
        assert matmul(A, M0) == B0 and matmul(A, M1) == B1
        rational = []
        for i in range(d):
            row = []
            for j in range(d):
                a, b = M0[i][j], M1[i][j]
                s = signs[i]*signs[j]
                assert s*a == a-b and s*b == -b
                if s == 1:
                    assert b == 0
                    row.append(a)
                else:
                    assert b == 2*a
                    row.append(-3*a if signs[i] == 1 else a)
            rational.append(row)
        assert rational == [list(map(F, row)) for row in record['rational_real_form_operator']]
        poly = characteristic_polynomial(rational)
        assert all(x.denominator == 1 for x in poly)
        poly = list(map(int, poly))
        assert poly == record['charpoly_coefficients']
        factor_product = [1]
        for factor in record['charpoly_factors']:
            for _ in range(factor['multiplicity']):
                factor_product = polynomial_product(factor_product, factor['coefficients'])
        assert factor_product == poly
        E = p**(2*e)+p**e+1
        value = evaluate(poly, E)
        assert E == record['comparison_point'] and value == record['comparison_value']
        values.append(value)
        for point in [((1, 2, 4), (3, -1, 2)), ((2, -3, 1), (1, 4, -2))]:
            actual0, actual1 = transform_sum(expanded, k, H, point, ns)
            z, w = point
            row, imag = harmonic_evaluate(expanded, k, H, [(x, 0) for x in z], [(x, 0) for x in w])
            assert not any(imag)
            assert matmul([row], M0) == [actual0] and matmul([row], M1) == [actual1]
    gcd_value = gcd(*values)
    gcd_factors = None
    saved = next((r for r in data['comparison_gcds'] if r['k'] == k), None)
    if saved is not None:
        assert saved['values'] == values and saved['gcd'] == gcd_value
        product_value = 1
        for prime_text, exponent in saved['factorization'].items():
            q = int(prime_text)
            assert q >= 2 and exponent > 0
            assert all(q % t for t in range(2, isqrt(q)+1))
            product_value *= q**exponent
        assert product_value == gcd_value
        gcd_factors = saved['factorization']
    reports.append({'k': k, 'e': e, 'invariant_source_dimension': len(source),
                    'invariant_target_dimension': len(target), 'harmonic_dimension': d,
                    'swap_signs': signs, 'all_neighbor_evaluations': True,
                    'exact_characteristic_polynomials': True, 'two_extra_points_each_prime': True,
                    'comparison_gcd': gcd_value, 'gcd_prime_factorization': gcd_factors})

output = {'status': 'PASS exact full invariant-harmonic linear algebra and Hecke data',
          'data_sha256': hashlib.sha256(DATA.read_bytes()).hexdigest(),
          'neighbor_sha256': neighbor_hash, 'results': reports,
          'scope': 'Finite algebraic model only; no arithmetic source coverage or K-group conclusion.'}
args.report.write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
