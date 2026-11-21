"""Independent, standard-library replay of the complete minus-seven U3 test.

Reconstructs the coefficient space and all actual neighbor frames; recomputes
every identifying polynomial evaluation with Python arbitrary-precision
integers; checks determinant units over a quadratic algebra modulo an
arbitrary residual integer. No prime or field assertion is assumed.  No C++ code or
prepared row-reduction routines are imported.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, permutations, product
from math import gcd, factorial
from pathlib import Path
import json
import time
import sys

HERE = Path(__file__).resolve().parent
CASE = Path(sys.argv[1]).resolve()
START = time.monotonic()
model = json.loads((CASE / 'model.json').read_text())
frames_record = json.loads((HERE.parent / 'neighbor_frames.json').read_text())
Q, K = model['q'], model['k']
assert Q > 1 and gcd(Q, 336 * factorial(2*K+1)) == 1


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
print('Coefficient ring, denominator units, and all 13 actual frames: PASS', flush=True)


def complete_orbits(k):
    compositions = [(i, j, k-i-j) for i in range(k+1)
                    for j in range(k-i+1)]
    return sorted({tuple(sorted(zip(a, b)))
                   for a in compositions for b in compositions
                   if all((x-y) % 2 == 0 for x, y in zip(a, b))})


source, target = complete_orbits(K), complete_orbits(K-1)
assert source == [tuple(map(tuple, o)) for o in model['source_orbits']]
assert target == [tuple(map(tuple, o)) for o in model['target_orbits']]
assert K >= 1
assert model['source_dimension'] == len(source)
assert model['target_dimension'] == len(target)
assert model['dimension'] == len(source)-len(target)
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
    for canonical in {tuple(sorted(m)) for m in polynomial}:
        coefficient = polynomial[canonical]
        assert all(polynomial[m] == coefficient
                   for m in set(permutations(canonical)))
        if coefficient:
            column[target_index[canonical]] = coefficient
    contraction.append(column)

basis = [[(i, c) for i, c in column]
         for column in model['harmonic_basis_sparse_columns']]
free = [i for block in model['blocks'] for i in block['free_columns']]
assert len(basis) == len(free) == len(set(free)) == model['dimension']
free_index = {i: j for j, i in enumerate(free)}
for j, column in enumerate(basis):
    assert len({i for i, c in column}) == len(column)
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
# dimension difference, direct kernel check, independent identity minor,
# and Nakayama at every maximal ideal of Z/M prove that these vectors are the entire kernel at every residue characteristic, without trusting RREF.

# Verify the exact text input consumed by the C++ program against all JSON data.
tokens = iter(map(int, (CASE / 'model.txt').read_text().split()))
assert [next(tokens) for _ in range(4)] == [Q, K, len(source), len(basis)]
for orbit in source:
    assert [next(tokens) for _ in range(6)] == [x for pair in orbit for x in pair]
for column in basis:
    assert next(tokens) == len(column)
    assert [next(tokens) for _ in range(2*len(column))] == [x for pair in column for x in pair]
points = model['identifying_and_extra_points']
assert next(tokens) == len(points) == len(basis)+2
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
E = (1 + 2**(K+1) + 2**(2*K+2)) % Q
assert gcd(E,Q)==1
# The caller supplies the worker budget after checking the execution environment.
# Fork preserves the complete already-checked model without importing producer code.
from multiprocessing import get_context
workers = int(sys.argv[2])
assert 1 <= workers <= 4


def independent_row(item):
    r, point = item
    z, w = [[(x, 0) for x in row] for row in point]
    a = evaluate(z, w)
    b2 = transformed(z, w, frames[2])
    b4 = transformed(z, w, frames[4])
    s = [sub(sub(scale(x, E*E), scale(y, E)), zz)
         for x, y, zz in zip(a, b2, b4)]
    return r, a, s


evaluations, schur = [None] * d, [None] * d
with get_context('fork').Pool(processes=workers) as pool:
    completed = 0
    for r, a, s in pool.imap_unordered(
            independent_row, enumerate(points[:d]), chunksize=1):
        assert 0 <= r < d
        assert evaluations[r] is None and schur[r] is None
        assert len(a) == len(s) == d
        evaluations[r], schur[r] = a, s
        completed += 1
        if completed % 50 == 0 or completed == d:
            print(f'Exact independent evaluation rows {completed}/{d}', flush=True)
assert completed == d
assert all(row is not None for row in evaluations)
assert all(row is not None for row in schur)


def norm(x):
    a,b=x
    return (a*a+a*b+2*b*b)%Q


def determinant(matrix):
    # Column elimination with certified unit pivots, independent of the
    # producer's row elimination.  A nonunit final entry is never inverted.
    a = [row[:] for row in matrix]
    n = len(a)
    det = (1,0)
    for i in range(n):
        if i==n-1:
            return mul(det,a[i][i])
        pivot = next((j for j in range(i,n) if gcd(norm(a[i][j]),Q)==1),None)
        if pivot is None:
            if all(a[i][j]==(0,0) for j in range(i,n)):
                return (0,0)
            raise ArithmeticError('Unit-pivot verification inconclusive')
        if pivot != i:
            for row in a:
                row[i],row[pivot]=row[pivot],row[i]
            det=scale(det,-1)
        value=a[i][i]
        det=mul(det,value)
        recip=inverse(value)
        for j in range(i+1,n):
            factor=mul(a[i][j],recip)
            for r in range(i+1,n):
                a[r][j]=sub(a[r][j],mul(a[r][i],factor))
            a[i][j]=(0,0)
    return det


det_a=determinant(evaluations)
assert gcd(norm(det_a),Q)==1
det_s=determinant(schur)
det_o=mul(det_s,inverse(det_a))
result = json.loads((CASE / 'schur.json').read_text())
assert result['modulus']==Q and result['k']==K
assert result['comparison_point']==E and result['dimension']==d
assert det_a==tuple(result['det_evaluation'])
assert det_s==tuple(result['det_schur_evaluations'])
assert det_o==tuple(result['det_schur_operator'])
common=gcd(norm(det_o),Q)
assert common==result['gcd_norm_determinant_modulus']==1
report={
 'status':'PASS: full independent exact quadratic-algebra unit certificate',
 'modulus':Q,'k':K,'e':K+1,'dimension':d,
 'source_dimension':len(source),'target_dimension':len(target),
 'comparison_point_modulus':E,'frame_counts':frame_counts,
 'all_recomputed_evaluation_rows':d,
 'parallel_row_workers':workers,
 'verifier_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
 'det_evaluation':det_a,'det_schur_evaluations':det_s,
 'det_schur_operator':det_o,'gcd_norm_determinant_modulus':common,
 'unit':True,'no_primality_assumption':True,
 'sha256':{name:sha256((CASE/name).read_bytes()).hexdigest()
           for name in ['model.json','model.txt','schur.json']},
 'frame_sha256':sha256((HERE.parent/'neighbor_frames.json').read_bytes()).hexdigest(),
 'elapsed_seconds':time.monotonic()-START,
 'scope':'Full two-class U3 coefficient model; source-family coverage separate.'
}
(CASE/'verify_ring_schur_parallel.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report),flush=True)
