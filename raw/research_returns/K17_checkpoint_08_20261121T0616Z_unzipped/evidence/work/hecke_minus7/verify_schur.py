"""Independent, standard-library replay of the complete minus-seven U3 test.

Reconstructs the coefficient space and all actual neighbor frames; recomputes
every saved polynomial evaluation with Python arbitrary-precision integers;
checks the full recovered operator and its determinant.  No C++ code or
prepared row-reduction routines are imported.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, permutations, product
from math import gcd, isqrt, prod
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent
Q = 25078104767246023
K = 15
START = time.monotonic()
model = json.loads((HERE / 'model_k15.json').read_text())
result = json.loads((HERE / 'schur_k15.json').read_text())
frames_record = json.loads((HERE / 'neighbor_frames.json').read_text())


def trial_prime(n):
    return n >= 2 and (n == 2 or n % 2 == 1 and
                      all(n % d for d in range(3, isqrt(n) + 1, 2)))


# Full-order Lucas proof, including primality of every factor of Q-1.
factors = {2: 1, 3: 3, 10487: 1, 44284289839: 1}
assert prod(p ** a for p, a in factors.items()) == Q - 1
assert all(trial_prime(p) for p in factors)
assert pow(3, Q - 1, Q) == 1
assert all(pow(3, (Q - 1) // p, Q) != 1 for p in factors)
assert pow(Q - 7, (Q - 1) // 2, Q) == Q - 1


def mul(x, y):
    a, b = x
    c, d = y
    return ((a*c - 2*b*d) % Q, (a*d + b*c + b*d) % Q)


def add(x, y):
    return ((x[0] + y[0]) % Q, (x[1] + y[1]) % Q)


def sub(x, y):
    return ((x[0] - y[0]) % Q, (x[1] - y[1]) % Q)


def conj(x):
    return ((x[0] + x[1]) % Q, -x[1] % Q)


def scale(x, n):
    return (x[0] * n % Q, x[1] * n % Q)


def inverse(x):
    a, b = x
    n = (a*a + a*b + 2*b*b) % Q
    assert n
    return scale(conj(x), pow(n, -1, Q))


def integral_mul(x, y):
    a, b = x
    c, d = y
    return (a*c - 2*b*d, a*d + b*c + b*d)


def integral_inner(v, w):
    terms = [integral_mul((a+b, -b), y) for (a, b), y in zip(v, w)]
    return tuple(sum(z[i] for z in terms) for i in (0, 1))


def integral_det(columns):
    total = [0, 0]
    for perm in permutations(range(3)):
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(3)
                           for j in range(i+1, 3))
        term = (1, 0)
        for j in range(3):
            term = integral_mul(term, columns[j][perm[j]])
        for i in (0, 1):
            total[i] += sign * term[i]
    return tuple(total)


def frame_signature(frame):
    columns = []
    for column in frame:
        v = tuple(tuple(x) for x in column)
        negative = tuple((-a, -b) for a, b in v)
        columns.append(max(v, negative))
    return tuple(sorted(columns))


# Norm(a+b omega)=(a+b/2)^2+7b^2/4.  For norm <=4, the
# following bounds exhaust all scalars, independently of the producer's [-4,4].
scalars = [(a, b) for b in range(-1, 2) for a in range(-3, 4)
           if a*a+a*b+2*b*b <= 4]
frames = {}
frame_counts = {}
for r, required in ((2, 6), (4, 7)):
    vectors = sorted({max(v, tuple((-a, -b) for a, b in v))
                      for v in product(scalars, repeat=3)
                      if sum(a*a+a*b+2*b*b for a, b in v) == r})
    all_frames = [triple for triple in combinations(vectors, 3)
                  if all(integral_inner(triple[i], triple[j]) == (0, 0)
                         for i, j in ((0, 1), (0, 2), (1, 2)))]
    selected = []
    for frame in all_frames:
        a, b = integral_det(frame)
        if r == 2:
            ok = (a + 2*b) % 4 == 2
        else:
            ok = ((a + 6*b) % 8 == 4 and
                  all(sum(a for a, b in column) % 2 == 0
                      for column in frame))
        if ok:
            selected.append(frame)
    saved = frames_record[str(r)]['selected_frames']
    assert len(selected) == len(saved) == required
    assert {frame_signature(f) for f in selected} == {
        frame_signature(f) for f in saved}
    frames[r] = [[[(a % Q, b % Q) for a, b in col] for col in f]
                 for f in saved]
    frame_counts[r] = [len(vectors), len(all_frames), len(selected)]
print('Prime, coefficient field, and all 13 actual frames: PASS', flush=True)


def complete_orbits(k):
    compositions = [(i, j, k-i-j) for i in range(k+1)
                    for j in range(k-i+1)]
    return sorted({tuple(sorted(zip(a, b)))
                   for a in compositions for b in compositions
                   if all((x-y) % 2 == 0 for x, y in zip(a, b))})


source, target = complete_orbits(K), complete_orbits(K-1)
assert source == [tuple(map(tuple, o)) for o in model['source_orbits']]
assert target == [tuple(map(tuple, o)) for o in model['target_orbits']]
assert (len(source), len(target), model['dimension']) == (795, 624, 171)
orbits = [sorted(set(permutations(o))) for o in source]
target_index = {o: i for i, o in enumerate(target)}
contraction = []
for orbit in orbits:
    polynomial = Counter()
    for monomial in orbit:
        for i, (a, b) in enumerate(monomial):
            if a*b:
                out = list(monomial)
                out[i] = (a-1, b-1)
                polynomial[tuple(out)] += a*b
    column = {}
    for canonical, index in target_index.items():
        coefficient = polynomial[canonical]
        assert all(polynomial[m] == coefficient
                   for m in set(permutations(canonical)))
        if coefficient:
            column[index] = coefficient
    contraction.append(column)

basis = [[(i, c) for i, c in column]
         for column in model['harmonic_basis_sparse_columns']]
free = [i for block in model['blocks'] for i in block['free_columns']]
assert len(basis) == len(free) == len(set(free)) == 171
free_index = {i: j for j, i in enumerate(free)}
for j, column in enumerate(basis):
    image = defaultdict(int)
    for i, c in column:
        assert 0 <= i < len(source) and 0 < c < Q
        if i in free_index:
            assert free_index[i] == j and c == 1
        for row, coefficient in contraction[i].items():
            image[row] += c * coefficient
    assert dict(column)[free[j]] == 1
    assert all(v % Q == 0 for v in image.values())
# The explicit contraction right inverse in the proof works mod Q.  Thus the
# dimension difference, direct kernel check, and independent free coordinates
# prove that these 171 vectors are the entire kernel, without trusting RREF.

# Verify the exact text input consumed by the C++ program against all JSON data.
tokens = iter(map(int, (HERE / 'model_k15.txt').read_text().split()))
assert [next(tokens) for _ in range(4)] == [Q, K, 795, 171]
for orbit in source:
    assert [next(tokens) for _ in range(6)] == [x for pair in orbit for x in pair]
for column in basis:
    assert next(tokens) == len(column)
    assert [next(tokens) for _ in range(2*len(column))] == [x for pair in column for x in pair]
points = model['identifying_and_extra_points']
assert next(tokens) == len(points) == 173
for point in points:
    assert [next(tokens) for _ in range(6)] == [x for row in point for x in row]
for r, count in ((2, 6), (4, 7)):
    assert next(tokens) == count
    for frame in frames_record[str(r)]['selected_frames']:
        assert [next(tokens) for _ in range(18)] == [x for col in frame for pair in col for x in pair]
assert next(tokens, None) is None
print('Complete invariant harmonic basis and input agreement: PASS', flush=True)


def evaluate(z, w):
    pairs = []
    for zi, wi in zip(z, w):
        zp, wp = [(1, 0)], [(1, 0)]
        for _ in range(K):
            zp.append(mul(zp[-1], zi))
            wp.append(mul(wp[-1], wi))
        pairs.append([[mul(x, y) for y in wp] for x in zp])
    values = []
    for orbit in orbits:
        a, b = 0, 0
        for monomial in orbit:
            term = (1, 0)
            for i, (u, v) in enumerate(monomial):
                term = mul(term, pairs[i][u][v])
            a += term[0]
            b += term[1]
        values.append((a % Q, b % Q))
    return [(sum(values[i][0]*c for i, c in column) % Q,
             sum(values[i][1]*c for i, c in column) % Q)
            for column in basis]


def transformed(z, w, frame_list):
    output = [(0, 0)] * len(basis)
    for frame in frame_list:
        zz, ww = [], []
        for column in frame:
            zv = [mul(conj(x), y) for x, y in zip(column, z)]
            wv = [mul(x, y) for x, y in zip(column, w)]
            zz.append((sum(x[0] for x in zv) % Q, sum(x[1] for x in zv) % Q))
            ww.append((sum(x[0] for x in wv) % Q, sum(x[1] for x in wv) % Q))
        output = [add(x, y) for x, y in zip(output, evaluate(zz, ww))]
    return output


d = len(basis)
E = 1 + 2**16 + 2**32
assert E == result['comparison_point'] == 4295032833
saved_names = ('evaluation_matrix', 'norm2_transformed_evaluations',
               'norm4_transformed_evaluations')
saved = [[[tuple(x) for x in row] for row in result[name]] for name in saved_names]
assert all(len(matrix) == 173 and all(len(row) == d for row in matrix)
           for matrix in saved)
operator = [[tuple(x) for x in row] for row in result['schur_operator']]
assert len(operator) == d and all(len(row) == d for row in operator)
schur = []
for r, point in enumerate(points):
    z, w = [[(x, 0) for x in row] for row in point]
    calculated = (evaluate(z, w), transformed(z, w, frames[2]),
                  transformed(z, w, frames[4]))
    assert all(row == matrix[r] for row, matrix in zip(calculated, saved)), r
    a, b2, b4 = calculated
    schur.append([sub(sub(scale(x, E*E), scale(y, E)), zz)
                  for x, y, zz in zip(a, b2, b4)])
    # Full 173 by 171 operator identity, using rational evaluation coefficients.
    assert all(x[1] == 0 for x in a)
    for j in range(d):
        value = (sum(a[i][0]*operator[i][j][0] for i in range(d)) % Q,
                 sum(a[i][0]*operator[i][j][1] for i in range(d)) % Q)
        assert value == schur[-1][j], (r, j)
    if r % 25 == 0:
        print(f'Exact independent evaluation row {r}/173', flush=True)


def determinant(matrix):
    # Column elimination, independent of the producer's row elimination.
    a = [row[:] for row in matrix]
    n = len(a)
    det = (1, 0)
    for i in range(n):
        pivot = next((j for j in range(i, n) if a[i][j] != (0, 0)), None)
        if pivot is None:
            return (0, 0)
        if pivot != i:
            for row in a:
                row[i], row[pivot] = row[pivot], row[i]
            det = scale(det, -1)
        value = a[i][i]
        det = mul(det, value)
        recip = inverse(value)
        for j in range(i+1, n):
            factor = mul(a[i][j], recip)
            for r in range(i+1, n):
                a[r][j] = sub(a[r][j], mul(a[r][i], factor))
            a[i][j] = (0, 0)
    return det


det_a = determinant(saved[0][:d])
det_s = determinant(schur[:d])
det_o = determinant(operator)
assert det_a == tuple(result['det_evaluation']) == (9611653439256081, 0)
assert det_s == tuple(result['det_schur_evaluations']) == (18272413515919144, 0)
assert det_o == tuple(result['det_schur_operator']) == (13187546903051047, 0)
assert mul(det_a, det_o) == det_s
assert det_a != (0, 0) and det_o != (0, 0)
inputs = ['neighbor_frames.py', 'neighbor_frames.json', 'prepare_model.py',
          'model_k15.json', 'model_k15.txt', 'compute_schur.cpp', 'schur_k15.json']
report = {
    'status': 'PASS: complete independent standard-library U3 Schur replay',
    'q': Q, 'k': K, 'dimension': d, 'comparison_point': E,
    'source_dimension': len(source), 'target_dimension': len(target),
    'frame_counts': frame_counts, 'all_recomputed_evaluation_rows': len(points),
    'det_evaluation': det_a, 'det_schur_evaluations': det_s,
    'det_schur_operator': det_o, 'nonzero': True,
    'prime_certificate': {'witness': 3, 'factorization_q_minus_1': factors},
    'sha256': {name: sha256((HERE/name).read_bytes()).hexdigest() for name in inputs},
    'elapsed_seconds': time.monotonic() - START,
    'scope': 'The full two-class coefficient-space test; arithmetic source coverage is separate.'
}
output = HERE / 'verify_schur.json'
output.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report), flush=True)
