"""Independent exact input/lattice and norm-determinant checks for the U3 model.

The full transformed evaluations are independently replayed from the C++ source;
this verifier separately reconstructs the invariant orbit spaces and contraction,
checks every matrix equation, and checks determinants using only F_q arithmetic.
"""
from itertools import permutations
from pathlib import Path
from collections import defaultdict
import hashlib
import json

HERE = Path(__file__).resolve().parent
model = json.loads((HERE/'model_k15.json').read_text())
result = json.loads((HERE/'schur_k15_archive_replay.json').read_text())
frames = json.loads((HERE/'neighbor_frames.json').read_text())
P = model['q']
k = model['k']
assert P == 25078104767246023 and k == 15


def all_orbits(n):
    compositions = [(i, j, n-i-j) for i in range(n+1)
                    for j in range(n-i+1)]
    answer = set()
    for a in compositions:
        for b in compositions:
            if any((a[i]+b[i]) % 2 for i in range(3)):
                continue
            answer.add(tuple(sorted(zip(a, b))))
    return sorted(answer)


source = all_orbits(k)
target = all_orbits(k-1)
assert source == [tuple(map(tuple, o)) for o in model['source_orbits']]
assert target == [tuple(map(tuple, o)) for o in model['target_orbits']]
assert (len(source), len(target)) == (795, 624)
target_index = {o:i for i, o in enumerate(target)}
contraction = []
for orbit in source:
    coefficients = defaultdict(int)
    for monomial in set(permutations(orbit)):
        for i, (a, b) in enumerate(monomial):
            if a*b:
                m = list(monomial)
                m[i] = (a-1, b-1)
                coefficients[tuple(m)] += a*b
    # Invariance means every monomial in a target orbit has equal coefficient.
    for m, c in coefficients.items():
        canonical = tuple(sorted(m))
        assert coefficients[canonical] == c
    contraction.append({target_index[o]:coefficients[o] for o in target
                        if coefficients[o]})
basis = model['harmonic_basis_sparse_columns']
assert len(basis) == 171
free = [j for block in model['blocks'] for j in block['free_columns']]
assert len(set(free)) == 171
for b in basis:
    totals = defaultdict(int)
    for i, c in b:
        for row, a in contraction[i].items():
            totals[row] = (totals[row]+a*c) % P
    assert all(v == 0 for v in totals.values())
coordinates = [{i:c for i, c in b} for b in basis]
assert [[b.get(i, 0) for b in coordinates] for i in free] == [
       [int(i == j) for j in range(171)] for i in range(171)]

# Decode the exact compiled-program input independently and compare every item.
tokens = iter(map(int, (HERE/'model_k15.txt').read_text().split()))
def take(n):
    return [next(tokens) for _ in range(n)]
assert take(4) == [P, k, 795, 171]
for orbit in source:
    assert take(6) == [x for pair in orbit for x in pair]
for column in basis:
    assert next(tokens) == len(column)
    assert take(2*len(column)) == [x for pair in column for x in pair]
points = model['identifying_and_extra_points']
assert next(tokens) == len(points) == 173
for point in points:
    assert take(6) == [x for row in point for x in row]
for norm in ('2', '4'):
    fs = frames[norm]['selected_frames']
    assert next(tokens) == len(fs)
    for frame in fs:
        assert take(18) == [x for col in frame for scalar in col for x in scalar]
assert next(tokens, None) is None


def determinant(matrix):
    a = [r[:] for r in matrix]
    value = 1
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            value = -value
        entry = a[i][i]
        value = value*entry % P
        reciprocal = pow(entry, -1, P)
        for j in range(i+1, len(a)):
            c = a[j][i]*reciprocal % P
            a[j][i] = 0
            for h in range(i+1, len(a)):
                a[j][h] = (a[j][h]-c*a[i][h]) % P
    return value % P


evaluation = result['evaluation_matrix']
norm2 = result['norm2_transformed_evaluations']
norm4 = result['norm4_transformed_evaluations']
operator = result['schur_operator']
assert all(len(a) == 173 and all(len(row) == 171 for row in a)
           for a in (evaluation, norm2, norm4))
assert len(operator) == 171 and all(len(row) == 171 for row in operator)
assert all(v[1] == 0 for row in evaluation for v in row)
a = [[v[0] for v in row] for row in evaluation]
E = 1+2**16+2**32
assert E == result['comparison_point']
opcolumns = list(zip(*operator))
for r in range(173):
    for j in range(171):
        derived_a = sum(x*y[0] for x, y in zip(a[r], opcolumns[j])) % P
        derived_b = sum(x*y[1] for x, y in zip(a[r], opcolumns[j])) % P
        direct_a = (E*E*a[r][j]-E*norm2[r][j][0]-norm4[r][j][0]) % P
        direct_b = (-E*norm2[r][j][1]-norm4[r][j][1]) % P
        assert (derived_a, derived_b) == (direct_a, direct_b)
da = determinant(a[:171])
assert [da, 0] == result['det_evaluation']

# Restriction of scalars: multiplication by A+B*omega is the block matrix
# [[A,-2B],[B,A+B]], since omega^2=omega-2.
aa = [[v[0] for v in row] for row in operator]
bb = [[v[1] for v in row] for row in operator]
norm_matrix = [aa[i] + [(-2*x) % P for x in bb[i]] for i in range(171)]
norm_matrix += [bb[i] + [(x+y) % P for x, y in zip(aa[i], bb[i])]
                for i in range(171)]
norm_det = determinant(norm_matrix)
ds, imaginary = result['det_schur_operator']
assert imaginary == 0 and norm_det == ds*ds % P and norm_det != 0
assert result['det_schur_evaluations'] == [da*ds % P, 0]
report = {
    'status':'PASS independent exact U3 input/lattice/matrix/norm verification',
    'q':P, 'source_count':795, 'target_count':624, 'harmonic_dimension':171,
    'kernel_columns_checked':171, 'matrix_equation_rows_checked':173,
    'identifying_determinant':da, 'schur_determinant':ds,
    'restriction_of_scalars_dimension':342, 'norm_determinant':norm_det,
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope':'Finite model only; full frame evaluation is separately recompiled and replayed.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report))
