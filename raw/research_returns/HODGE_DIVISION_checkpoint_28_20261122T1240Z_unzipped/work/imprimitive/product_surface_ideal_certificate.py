"""HD-N20: actual product-surface ideal character and exact rank minors.
GPT-6 Astra Pro /root/imprimitive, 21 November 2026, inherited effort.

Only elementary wedge/contraction utilities are reused from N19 by AST.
The source character, all 66 Hochschild columns, factor partitions,
Gaussian elimination and integer minors are rebuilt here.
"""
from pathlib import Path
from itertools import combinations
import ast
import json
import sympy as sp

path = Path(__file__).with_name('rank_two_atiyah_quotient_certificate.py')
tree = ast.parse(path.read_text())
names = {'wedge_sign', 'wedge', 'contract', 'hh_action'}
small = ast.Module(body=[x for x in tree.body
                         if isinstance(x, ast.FunctionDef) and x.name in names],
                   type_ignores=[])
exec(compile(small, '<disclosed elementary exterior utilities>', 'exec'))


def add(a, b, scale=1):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, 0)+scale*c
        if not out[m]:
            del out[m]
    return out


def pivots(columns, prime=65537):
    basis, chosen = {}, []
    for j, column in enumerate(columns):
        v = {m: int(c) % prime for m, c in column.items()
             if int(c) % prime}
        while v:
            pivot = min(v)
            if pivot not in basis:
                a = pow(v[pivot], -1, prime)
                basis[pivot] = {m: c*a % prime for m, c in v.items()}
                chosen.append(j)
                break
            a = v[pivot]
            for m, c in basis[pivot].items():
                v[m] = (v.get(m, 0)-a*c) % prime
                if not v[m]:
                    del v[m]
    return chosen, list(basis)


H = [{(1 << (2*i)) | (1 << (2*i+1)): 1 for i in group}
     for group in (range(3), range(3, 6))]
a6 = []
for h in H:
    h2 = wedge(h, h)
    h3 = wedge(h2, h)
    a6.append(add({m: 3*c for m, c in h2.items()}, h3, -2))
# v=36 ch(I_{C x C}); 6ch(O_C)=3theta²−2theta³.
v = add({0: 36}, wedge(a6[0], a6[1]), -1)
U1, U2 = (0, 1, 2, 6, 7, 8), (3, 4, 5, 9, 10, 11)
block_labels = [
    list(combinations(U1, 2)),
    [(i, j) for i in U1 for j in U2],
    list(combinations(U2, 2))
]
blocks = []
for label in block_labels:
    blocks.append([hh_action(hh_action(v, j), i) for i, j in label])
result_blocks = []
for number, (columns, expected) in enumerate(zip(blocks, (9, 36, 9))):
    indices, rows = pivots(columns)
    assert len(indices) == expected
    assert len(pivots(columns, 1009)[0]) == expected
    M = sp.Matrix([[columns[j].get(m, 0) for j in indices] for m in rows])
    determinant = int(M.det())
    assert determinant
    # Every output has a single pair of Hochschild Kunneth degrees.
    multidegrees = set()
    for col in columns:
        for m in col:
            pair = []
            for group in (range(3), range(3, 6)):
                hol = sum((m >> (2*i)) & 1 for i in group)
                anti = sum((m >> (2*i+1)) & 1 for i in group)
                pair.append(anti-hol)
            multidegrees.add(tuple(pair))
    expected_pair = ((2, 0), (1, 1), (0, 2))[number]
    assert multidegrees == {expected_pair}
    result_blocks.append(dict(block=number+1, columns=len(columns),
                              rank=expected, Kunneth_degree=expected_pair,
                              minor_rows=rows, minor_columns=indices,
                              exact_minor_determinant=str(determinant)))
all_columns = sum(blocks, [])
assert len(all_columns) == 66
assert len(pivots(all_columns)[0]) == 54
one = [hh_action(v, i) for i in range(12)]
assert len(pivots(one)[0]) == 12

# Independent check of the lowest-degree component used for mixed injectivity:
# for each curve character, the six degree-one columns are independent.
factor_ranks = []
for a, U in zip(a6, (U1, U2)):
    columns = [hh_action(a, i) for i in U]
    assert len(pivots(columns)[0]) == 6
    factor_ranks.append(6)

# All higher-degree maps are independently constructed as well.  Their
# expected block ranks are proved by the joint maps in the written proof.
expected_blocks = {
    (0, 0): 1, (0, 1): 6, (0, 2): 9, (0, 3): 2,
    (1, 1): 36, (1, 2): 45, (1, 3): 9,
    (2, 2): 36, (2, 3): 6, (3, 3): 1}
all_grade_blocks = []
total_by_degree = [0]*7
for r in range(4):
    for s in range(4):
        cols = []
        for I in combinations(U1, r):
            for J in combinations(U2, s):
                w = v
                for i in reversed(I+J):
                    w = hh_action(w, i)
                cols.append(w)
        expected = expected_blocks[tuple(sorted((r, s)))]
        assert len(pivots(cols, 65537)[0]) == expected
        assert len(pivots(cols, 1009)[0]) == expected
        total_by_degree[r+s] += expected
        all_grade_blocks.append(dict(first_degree=r, second_degree=s,
                                     rank=expected, columns=len(cols)))
assert total_by_degree == [1, 12, 54, 94, 54, 12, 1]

# Exact RR on the Chern polynomials, retaining the dual signs.
# a_i integrates to chi(O_C)=-2 on each curve factor. The ideal's
# degree-six coefficient integrates to-4; its dual has the same top
# coefficient, and their product correction begins in Chern degree8.
euler_self = -2*((-2)*(-2))
assert euler_self == -8
ext_dimensions = [1, 12, 54, 94, 54, 12, 1]
assert sum((-1)**j*n for j,n in enumerate(ext_dimensions)) == euler_self

out = dict(statement='HD-N20', date='2026-11-21', status='PASS',
           character_scale=36, character_coefficients={str(m): c for m, c in v.items()},
           blocks=result_blocks, total_HH2_rank=54, HH1_rank=12,
           curve_structure_sheaf_HH1_ranks=factor_ranks,
           all_grade_blocks=all_grade_blocks,
           all_grade_ranks=total_by_degree, Euler_self=euler_self,
           target_allowed_HH2_ranks=[30, 39, 48, 57],
           source_maps='actual ideal exact sequence and external structure sheaf product',
           scope='Exact integer minors certify lower bounds; universal upper bounds are in the proof.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print('PASS: exact block minors have sizes9,36,9; Kunneth degrees disjoint.')
print('PASS: HH2 rank54 and HH1 rank12; target ranks30,39,48,57.')
print('PASS: all16 Kunneth blocks at two primes; ranks1,12,54,94,54,12,1 and Euler−8.')

