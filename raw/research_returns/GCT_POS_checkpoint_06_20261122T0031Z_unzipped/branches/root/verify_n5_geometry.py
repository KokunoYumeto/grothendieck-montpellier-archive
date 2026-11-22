"""Independent finite geometry arithmetic for K-010--K-014.

Rebuilds the infinitesimal action, uses a different prime, evaluates
maximal incidence minors, and enumerates every scalar shift for factor
orbit multiplicities. No import of the classification/analysis engines.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import json
import sympy as sp

BASE = Path(__file__).resolve().parents[2]
K = BASE / 'branches' / 'kronecker'
records = json.loads((K / 'n5_type_analysis.json').read_text())
residue = json.loads((K / 'n5_residue_verified.json').read_text())
assert len(records) == len(residue['locals']) == 77
P = 10007

def rank_mod(matrix):
    rows = [[int(x) % P for x in row] for row in matrix]
    rank = 0
    for j in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        factor = pow(rows[rank][j], -1, P)
        rows[rank] = [x * factor % P for x in rows[rank]]
        for i in range(rank + 1, len(rows)):
            factor = rows[i][j]
            if factor:
                rows[i] = [(x - factor*y) % P for x,y in zip(rows[i],rows[rank])]
        rank += 1
    return rank

def canonical_all_shifts(weights):
    candidates = []
    for a,b in product(range(16), repeat=2):
        shifts = a,b,(-a-b)%16
        candidates.append(tuple(tuple(sorted((v+s)%16 for v in w))
                                for w,s in zip(weights,shifts)))
    return min(candidates)

z = sp.Symbol('z')
profiles = Counter()
mults = Counter()
checks = []
total = [Fraction(0)]*8
for record,local in zip(records,residue['locals']):
    weights = record['W']
    support = {tuple(e) for e in record['chosen_support']}
    assert len(support) == 13
    assert all(sum(weights[a][e[a]] for a in range(3))%16 == 0 for e in support)
    for a in range(3):
        assert {e[a] for e in support} == set(range(5))
    outputs = list(product(range(5), repeat=3))
    output_index = {e:i for i,e in enumerate(outputs)}
    columns = []
    for factor,i,j in product(range(3),range(5),range(5)):
        column = [0]*125
        for e in support:
            if e[factor] == j:
                image = list(e); image[factor] = i
                column[output_index[tuple(image)]] += 1
        columns.append(column)
    lie_rank = rank_mod(list(zip(*columns)))
    assert lie_rank == 73
    # Delete one row in each of the second and third coordinate blocks.
    row_labels = [(a,i) for a in range(3) for i in range(5)
                  if not (a in (1,2) and i == 4)]
    incidence = sp.Matrix([[int(e[a] == i) for e in sorted(support)]
                           for a,i in row_labels])
    determinant = int(incidence.det(method='domain-ge'))
    assert abs(determinant) == 16
    multiplicity = len({canonical_all_shifts(w) for w in permutations(weights)})
    assert multiplicity == local['ordered_factor_multiplicity']
    mults[multiplicity] += 1
    symbolic = sp.Poly(sp.sympify(record['normal_determinant_reciprocal_before_finite_quotient']),z)
    coefficients = [Fraction(str(symbolic.nth(j))) for j in range(8)]
    assert coefficients == [Fraction(x) for x in local['local_coefficient_basis']]
    total = [x+multiplicity*y for x,y in zip(total,coefficients)]
    profile = []
    paired = []
    for factor in weights:
        values = [v for v in range(8) if v in factor and v+8 in factor]
        assert len(values) <= 1
        if values:
            v = values[0]
            assert factor.count(v) == factor.count(v+8) == 1
            paired.append({factor.index(v),factor.index(v+8)})
        else:
            paired.append(set())
        profile.append(len(values))
    profiles[tuple(sorted(profile))] += 1
    if all(profile):
        assert any(sum(e[a] in paired[a] for a in range(3)) == 1 for e in support)
    checks.append({'index':record['index'],'lie_rank_mod_10007':lie_rank,
                   'incidence_minor':determinant,'factor_multiplicity':multiplicity})
assert mults == Counter({6:65,3:11,1:1})
assert total == [Fraction(v,32768) for v in (78,446,-211,-301,-301,-211,446,78)]
result = {'status':'PASS','types':77,'curves':424,'prime':P,
          'multiplicities':dict(mults),'residue':[str(x) for x in total],
          'scope':'Independent infinitesimal matrices, incidence minors, full scalar-shift orbits; comparison of two cyclotomic arithmetic methods.',
          'checks':checks}
(BASE/'reviews'/'n5_geometry_root_verification.json').write_text(json.dumps(result,indent=2))
print('PASS: all 77 infinitesimal ranks/minors, all factor orbits, and all exact local coefficients')
