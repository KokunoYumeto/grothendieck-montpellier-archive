"""Exact affine-line necessary conditions for a full-support Moore parameter.

No universal nine-variable determinant is reconstructed here.  The symbolic
identity is the three-by-three block identity.  The independent finite-field
matrix witness tests whether the resulting necessary conditions suffice.
"""
from datetime import datetime, timezone
from itertools import product, permutations
from pathlib import Path
import json, time

start = time.perf_counter()
G = list(product(range(3), repeat=2))
index = {g: i for i, g in enumerate(G)}
normals = [(1, 0), (0, 1), (1, 1), (1, 2)]
add = lambda a, b: ((a[0]+b[0]) % 3, (a[1]+b[1]) % 3)
neg = lambda a: ((-a[0]) % 3, (-a[1]) % 3)
scale = lambda a, n: ((n*a[0]) % 3, (n*a[1]) % 3)
lines = [[frozenset(g for g in G if (n[0]*g[0]+n[1]*g[1]) % 3 == t)
          for t in range(3)] for n in normals]
choices = {tuple(c): frozenset(lines[i][c[i]] for i in range(4))
           for c in product(range(3), repeat=4)}
assert len(choices) == 81

def rref(rows):
    rows = list(rows)
    k = 0
    pivots = []
    for col in range(9):
        pivot = next((i for i in range(k, len(rows)) if rows[i] >> col & 1), None)
        if pivot is None:
            continue
        rows[k], rows[pivot] = rows[pivot], rows[k]
        for i in range(len(rows)):
            if i != k and rows[i] >> col & 1:
                rows[i] ^= rows[k]
        pivots.append(col)
        k += 1
    return rows[:k], pivots

choice_records = []
for constants, selected in choices.items():
    multiplicities = {g: sum(g in line for line in selected) for g in G}
    maximum = max(multiplicities.values())
    assert maximum in (3, 4)
    centres = [g for g, value in multiplicities.items() if value == maximum]
    assert len(centres) == 1
    rows = [sum(1 << index[g] for g in lines[i][constants[i]]) for i in range(4)]
    reduced, pivots = rref(rows)
    assert len(pivots) == 4
    choice_records.append({'constants': constants, 'type': 'concurrent' if maximum == 4 else 'triple-plus-one',
                           'unique_centre': centres[0], 'rank_over_F2': 4,
                           'line_row_masks': rows, 'rref_row_masks': reduced, 'pivot_columns': pivots})
assert sum(r['type'] == 'concurrent' for r in choice_records) == 9
assert sum(r['type'] == 'triple-plus-one' for r in choice_records) == 72

linear = [m for m in product(range(3), repeat=4) if (m[0]*m[3]-m[1]*m[2]) % 3]
assert len(linear) == 48
def transform_point(g, m, t):
    return ((m[0]*g[0]+m[1]*g[1]+t[0]) % 3,
            (m[2]*g[0]+m[3]*g[1]+t[1]) % 3)
def orbit(selected):
    return {frozenset(frozenset(transform_point(g, m, t) for g in line) for line in selected)
            for m in linear for t in G}
concurrent = orbit(choices[(0, 0, 0, 0)])
triple = orbit(choices[(0, 0, 0, 1)])
assert len(concurrent) == 9 and len(triple) == 72 and concurrent.isdisjoint(triple)
assert concurrent | triple == set(choices.values())

# Cubes z_ij are linear expressions in five formal free variables.  An
# expression is represented by its F2 coefficient bitmask.
concurrent_forms = [1, 2, 1 ^ 2, 4, 8, 16, 1 ^ 4, 1 ^ 16, 1 ^ 8]
triple_forms = [1, 2, 1 ^ 2, 4, 8, 2 ^ 4, 1 ^ 4, 1 ^ 2 ^ 4, 16]
def xor_sum(xs):
    value = 0
    for x in xs:
        value ^= x
    return value
for constants, forms in [((0,0,0,0), concurrent_forms), ((0,0,0,1), triple_forms)]:
    for i in range(4):
        assert xor_sum(forms[index[g]] for g in lines[i][constants[i]]) == 0
assert xor_sum(concurrent_forms) == 1
assert xor_sum(triple_forms) == 8 ^ 16

# The exact 3x3 Moore determinant in characteristic two.
det3 = set()
for perm in permutations(range(3)):
    mon = [0] * 6
    for a, b in enumerate(perm):
        mon[(a-b) % 3] += 1
        mon[3+(a+b) % 3] += 1
    mon = tuple(mon)
    if mon in det3:
        det3.remove(mon)
    else:
        det3.add(mon)
expected = set()
for a in range(3):
    mon = [0]*6
    mon[a] = 3
    mon[3:] = [1,1,1]
    expected.add(tuple(mon))
    mon = [1,1,1,0,0,0]
    mon[3+a] = 3
    expected.add(tuple(mon))
assert det3 == expected

# Check the actual row/column block typing for every line direction.
block_entries = 0
for n in normals:
    H = next(line for line in lines[normals.index(n)] if (0,0) in line)
    v = min(g for g in H if g != (0,0))
    reps = []
    covered = set()
    for r in G:
        if r not in covered:
            reps.append(r)
            covered.update(add(r, h) for h in H)
    assert len(reps) == 3
    assert {add(r, scale(v,a)) for r in reps for a in range(3)} == set(G)
    assert {add(neg(r), scale(v,b)) for r in reps for b in range(3)} == set(G)
    for r in reps:
        for a, b in product(range(3), repeat=2):
            row = add(r, scale(v,a))
            col = add(neg(r), scale(v,b))
            assert add(row,col) == scale(v,(a+b)%3)
            assert add(row,neg(col)) == add(scale(r,2), scale(v,(a-b)%3))
            block_entries += 1
    for r, s in product(reps, repeat=2):
        if r != s:
            assert add(r,neg(s)) not in H
assert block_entries == 108

# A literal full-support finite-field counterexample to sufficiency of the
# affine-line conditions, with an actual F=0 test vector and nonzero matrix.
def mul(a,b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011
    return result
def power(a,n):
    result = 1
    while n:
        if n & 1:
            result = mul(result,a)
        a = mul(a,a)
        n >>= 1
    return result
for a in range(1,8):
    assert power(a,7) == 1 and power(power(a,3),5) == a
def determinant(matrix):
    a = [row[:] for row in matrix]
    result = 1
    for j in range(len(a)):
        pivot = next((i for i in range(j,len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        a[j], a[pivot] = a[pivot], a[j]
        pivot_value = a[j][j]
        result = mul(result,pivot_value)
        inverse = power(pivot_value,6)
        for i in range(j+1,len(a)):
            factor = mul(a[i][j],inverse)
            for k in range(j,len(a)):
                a[i][k] ^= mul(factor,a[j][k])
    return result

z = [1,2,3,2,2,2,3,3,3]
c = [power(a,5) for a in z]
assert all(c) and [power(a,3) for a in c] == z
assert all(xor_sum(z[index[g]] for g in lines[i][0]) == 0 for i in range(4))
assert xor_sum(z) == 1
witness = None
Hindices = [0,1,2]
for coeff in product(range(8), repeat=3):
    x = [0]*9
    for j,value in zip(Hindices,coeff):
        x[j] = value
    x[3] = power(xor_sum(power(value,3) for value in coeff),5)
    assert xor_sum(power(value,3) for value in x) == 0
    matrix = [[mul(c[index[add(a,neg(b))]], x[index[add(a,b)]]) for b in G] for a in G]
    d = determinant(matrix)
    if d:
        witness = {'field':'F2[a]/(a^3+a+1)', 'encoding':'binary coefficient bits',
                   'c':c, 'c_cubes':z, 'x':x, 'F_x':0, 'F_c':1,
                   'Moore_matrix':matrix, 'determinant':d,
                   'meaning':'All four concurrent affine-line necessary conditions hold on full support, but F does not divide the determinant.'}
        break
assert witness is not None
out = {
    'status':'PASS', 'actual_utc':datetime.now(timezone.utc).isoformat(),
    'runtime_seconds':time.perf_counter()-start,
    'counts':{'affine_line_choices':81,'concurrent_choices':9,'triple_plus_one_choices':72,
              'affine_transformations':432,'rank_four_systems':81,'typed_block_entries':block_entries,
              'three_by_three_determinant_terms':len(det3)},
    'point_order':G,'normal_order':normals,'choice_records':choice_records,
    'normal_forms':{
        'concurrent':{'constants':[0,0,0,0],'free_z':['z00','z01','z10','z11','z12'],
                      'expression_masks':concurrent_forms,'total_cube_sum':'z00'},
        'triple_plus_one':{'constants':[0,0,0,1],'free_z':['z00','z01','z10','z11','z22'],
                           'expression_masks':triple_forms,'total_cube_sum':'z11+z22'}},
    'counterexample_to_sufficiency':witness,
    'scope':'Exact necessary affine-line reduction only. The two normal forms are not a classification of Fermat-divisible parameters. An exact counterexample disproves sufficiency of the line conditions. No actual theta/Cartier parameter or wall conclusion is asserted.'
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'actual_utc':out['actual_utc'],'runtime_seconds':out['runtime_seconds'],
                  'counts':out['counts'],'counterexample_to_sufficiency':witness},indent=2))
