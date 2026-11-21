"""Exploratory exact full U3 Hecke matrices in harmonic bidegree (k,k).

The coefficient space is constructed from all mu6^3 and S3 invariant
monomials, including exponent differences +/-6.  Exact evaluation on a
proved full harmonic basis replaces huge dense polynomial expansions.
This script establishes finite algebraic data; arithmetic source coverage
and independent certificate review remain separate obligations.
"""
from pathlib import Path
from itertools import permutations, product
from collections import defaultdict
from math import gcd, lcm
import argparse, hashlib, json, random, time
import sympy as sp

BASE = Path(__file__).resolve().parent
NEIGHBORS = BASE.parent/'hecke_level_one/u3_weight5_exact_exploration.json'


def emul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def eadd(x, y):
    return x[0]+y[0], x[1]+y[1]


def econj(x):
    return x[0]-x[1], -x[1]


def orbits(k):
    compositions = [(a, b, k-a-b) for a in range(k+1) for b in range(k-a+1)]
    return sorted({tuple(sorted(zip(a, b))) for a, b in product(compositions, repeat=2)
                   if all((x-y) % 6 == 0 for x, y in zip(a, b))})


def primitive(v):
    den = lcm(*(int(x.q) for x in v))
    ints = [int(x*den) for x in v]
    common = gcd(*ints)
    ints = [x//common for x in ints]
    if next(x for x in ints if x) < 0:
        ints = [-x for x in ints]
    return sp.Matrix(ints)


def harmonic_data(k):
    source, target = orbits(k), orbits(k-1)
    source_index = {o: i for i, o in enumerate(source)}
    target_index = {o: i for i, o in enumerate(target)}
    expanded = [sorted(set(permutations(o))) for o in source]
    target_sizes = [len(set(permutations(o))) for o in target]
    lap = sp.zeros(len(target), len(source))
    for j, monomials in enumerate(expanded):
        sums = defaultdict(int)
        for mon in monomials:
            for i, (a, b) in enumerate(mon):
                if a and b:
                    out = list(mon)
                    out[i] = (a-1, b-1)
                    sums[tuple(sorted(out))] += a*b
        for out, coefficient in sums.items():
            i = target_index[out]
            assert coefficient % target_sizes[i] == 0
            lap[i, j] = coefficient//target_sizes[i]
    swap = [source_index[tuple(sorted((b, a) for a, b in o))] for o in source]
    sign_spans = {1: [], -1: []}
    for i, j in enumerate(swap):
        if i == j:
            v = sp.zeros(len(source), 1)
            v[i] = 1
            sign_spans[1].append(v)
        elif i < j:
            for sign in (1, -1):
                v = sp.zeros(len(source), 1)
                v[i], v[j] = 1, sign
                sign_spans[sign].append(v)
    basis, signs = [], []
    for sign in (1, -1):
        if not sign_spans[sign]:
            continue
        span = sp.Matrix.hstack(*sign_spans[sign])
        for v in (lap*span).nullspace():
            basis.append(primitive(span*v))
            signs.append(sign)
    H = sp.Matrix.hstack(*basis)
    assert lap.rank() == len(target)
    assert H.rank() == len(source)-len(target) and lap*H == sp.zeros(len(target), H.cols)
    assert all(H[swap[i], j] == signs[j]*H[i, j]
               for i in range(H.rows) for j in range(H.cols))
    return source, target, expanded, lap, H, signs


def eval_orbits_integer(expanded, k, z, w):
    zp = [[x**a for a in range(k+1)] for x in z]
    wp = [[x**a for a in range(k+1)] for x in w]
    return [sum(zp[0][m[0][0]]*wp[0][m[0][1]]*
                zp[1][m[1][0]]*wp[1][m[1][1]]*
                zp[2][m[2][0]]*wp[2][m[2][1]] for m in monomials)
            for monomials in expanded]


def eval_orbits_eisenstein(expanded, k, z, w):
    zp, wp = [], []
    for x in z:
        powers = [(1, 0)]
        for _ in range(k):
            powers.append(emul(powers[-1], x))
        zp.append(powers)
    for x in w:
        powers = [(1, 0)]
        for _ in range(k):
            powers.append(emul(powers[-1], x))
        wp.append(powers)
    answer = []
    for monomials in expanded:
        total = (0, 0)
        for m in monomials:
            value = (1, 0)
            for i, (a, b) in enumerate(m):
                value = emul(value, emul(zp[i][a], wp[i][b]))
            total = eadd(total, value)
        answer.append(total)
    return answer


def choose_points(k, expanded, H):
    generator = random.Random(20261121+k)
    points, rows = [], []
    for attempt in range(1000):
        z = tuple(generator.randrange(-2, 4) for _ in range(3))
        w = tuple(generator.randrange(-2, 4) for _ in range(3))
        values = sp.Matrix(1, len(expanded), eval_orbits_integer(expanded, k, z, w))*H
        row = list(values)
        if sp.Matrix(rows+[row]).rank() > len(rows):
            rows.append(row)
            points.append((z, w))
        if len(points) == H.cols:
            matrix = sp.Matrix(rows)
            assert matrix.det()
            return points, matrix
    raise RuntimeError('did not find an injective evaluation map')


def transformed_evaluation(k, expanded, H, point, neighbors):
    z, w = point
    totals = [(0, 0) for _ in expanded]
    for neighbor in neighbors:
        columns = neighbor['columns']
        zz, ww = [], []
        for column in columns:
            zz.append(tuple(sum(econj(column[i])[j]*z[i] for i in range(3)) for j in range(2)))
            ww.append(tuple(sum(column[i][j]*w[i] for i in range(3)) for j in range(2)))
        values = eval_orbits_eisenstein(expanded, k, zz, ww)
        totals = [eadd(a, b) for a, b in zip(totals, values)]
    return ([sum(int(H[i, j])*totals[i][0] for i in range(H.rows)) for j in range(H.cols)],
            [sum(int(H[i, j])*totals[i][1] for i in range(H.rows)) for j in range(H.cols)])


def matrix_json(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


def calculate(k, prime_records):
    start = time.monotonic()
    source, target, expanded, lap, H, signs = harmonic_data(k)
    points, evaluation = choose_points(k, expanded, H)
    inverse = evaluation.inv()
    print('basis', k, 'source', len(source), 'target', len(target),
          'harmonic', H.cols, 'signs', signs, flush=True)
    output = {'status': 'EXPLORATORY exact full invariant harmonic model; independent review pending',
              'k': k, 'e': k+1, 'highest_weight': [k, 0, -k],
              'source_orbits': source, 'target_orbits': target,
              'laplacian': matrix_json(lap), 'harmonic_basis_columns': matrix_json(H),
              'swap_signs': signs, 'evaluation_points': points,
              'evaluation_matrix': matrix_json(evaluation),
              'evaluation_determinant': str(evaluation.det()), 'results': [],
              'neighbors_sha256': hashlib.sha256(NEIGHBORS.read_bytes()).hexdigest()}
    X = sp.Symbol('X')
    for record in prime_records:
        p = record['p']
        values = [transformed_evaluation(k, expanded, H, point, record['neighbors']) for point in points]
        B0, B1 = sp.Matrix([v[0] for v in values]), sp.Matrix([v[1] for v in values])
        M0, M1 = inverse*B0, inverse*B1
        C = sp.diag(*signs)
        assert C*M0*C == M0-M1 and C*M1*C == -M1
        rational = sp.zeros(H.cols)
        for i in range(H.cols):
            for j in range(H.cols):
                a, b = M0[i, j], M1[i, j]
                if signs[i] == signs[j]:
                    assert b == 0
                    rational[i, j] = a
                else:
                    assert b == 2*a
                    rational[i, j] = -3*a if signs[i] == 1 else a
        polynomial = rational.charpoly(X).as_poly()
        assert all(c.q == 1 for c in polynomial.all_coeffs())
        # Additional evaluation checks resolve implementation errors in the
        # interpolation and the coefficient-field/swap conventions.
        extras = [((1, 2, 4), (3, -1, 2)), ((2, -3, 1), (1, 4, -2))]
        for point in extras:
            b0, b1 = transformed_evaluation(k, expanded, H, point, record['neighbors'])
            row = sp.Matrix(1, len(expanded), eval_orbits_integer(expanded, k, *point))*H
            assert row*M0 == sp.Matrix([b0]) and row*M1 == sp.Matrix([b1])
        comparison = p**(2*(k+1))+p**(k+1)+1
        factors = sp.factor_list(polynomial.as_expr())[1]
        row = {'p': p, 'dimension': H.cols, 'cosets': len(record['neighbors']),
               'scaled_operator': 'p^k times negative minuscule T; same spectrum as positive by swap',
               'transformed_evaluations_0': matrix_json(B0),
               'transformed_evaluations_omega': matrix_json(B1),
               'operator_0': matrix_json(M0), 'operator_omega': matrix_json(M1),
               'rational_real_form_operator': matrix_json(rational),
               'charpoly': str(polynomial.as_expr()),
               'charpoly_coefficients': [int(c) for c in polynomial.all_coeffs()],
               'charpoly_factors': [{'polynomial': str(f), 'multiplicity': int(m),
                                     'coefficients': [int(c) for c in sp.Poly(f, X).all_coeffs()]}
                                    for f, m in factors],
               'comparison_point': comparison,
               'comparison_value': int(polynomial.eval(comparison)),
               'two_extra_evaluation_checks': True,
               'conjugation_similarity_checked': True}
        output['results'].append(row)
        (BASE/f'harmonic_k{k}_exact_exploration.json').write_text(json.dumps(output, indent=2)+'\n')
        print('p', p, 'k', k, 'charpoly', polynomial.as_expr(),
              'factors', factors, 'elapsed', round(time.monotonic()-start, 2), flush=True)
    output['elapsed_seconds'] = time.monotonic()-start
    (BASE/f'harmonic_k{k}_exact_exploration.json').write_text(json.dumps(output, indent=2)+'\n')
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--degrees', nargs='+', type=int, default=[7, 9, 11])
    parser.add_argument('--primes', nargs='+', type=int, default=[7, 13])
    args = parser.parse_args()
    original = json.loads(NEIGHBORS.read_text())
    records = [r for r in original['results'] if r['p'] in args.primes]
    for k in args.degrees:
        calculate(k, records)
