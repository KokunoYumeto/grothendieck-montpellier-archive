"""Independent exact Q[z]/(z^8+1) verification of the n=5 residue sum.

Uses only Python integers and Fraction; no symbolic algebra or floating point.
The geometric justification for summing is K-010--K-014, not this script.
"""
from fractions import Fraction as F
from itertools import product, permutations
from collections import Counter
from pathlib import Path
import json

root=Path(__file__).resolve().parent
records=json.loads((root/'recursive_n5_m16_result.json').read_text())['feasible']
one=[F(1)]+[F(0)]*7

def multiply(a,b):
    out=[F(0)]*8
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<8:out[i+j]+=x*y
            else:out[i+j-8]-=x*y
    return out

def cyclotomic_product(exponents):
    out=one.copy()
    for exponent in exponents:
        exponent%=16
        if not exponent:continue
        factor=one.copy()
        factor[exponent%8]-=1 if exponent<8 else -1
        out=multiply(out,factor)
    return out

def inverse(a):
    columns=[]
    for j in range(8):
        basis=[F(0)]*8;basis[j]=1;columns.append(multiply(a,basis))
    matrix=[[columns[j][i] for j in range(8)]+[one[i]] for i in range(8)]
    for j in range(8):
        pivot=next(i for i in range(j,8) if matrix[i][j])
        matrix[j],matrix[pivot]=matrix[pivot],matrix[j]
        scale=matrix[j][j];matrix[j]=[v/scale for v in matrix[j]]
        for i in range(8):
            if i==j:continue
            scale=matrix[i][j]
            if scale:matrix[i]=[x-scale*y for x,y in zip(matrix[i],matrix[j])]
    answer=[matrix[i][-1] for i in range(8)]
    assert multiply(a,answer)==one
    return answer

def ordered_canonical(weights):
    return min(tuple(tuple(sorted((a-e[j])%16 for a in factor)) for j,factor in enumerate(weights))
               for e in product(*weights) if sum(e)%16==0)

total=[F(0)]*8;local=[];multiplicities=Counter()
for index,record in enumerate(records,1):
    weights=record['W']
    numerator=cyclotomic_product(a-b for factor in weights for a in factor for b in factor)
    denominator=cyclotomic_product(sum(edge) for edge in product(*weights))
    coefficient=multiply(numerator,inverse(denominator))
    multiplicity=len({ordered_canonical(w) for w in permutations(weights)})
    multiplicities[multiplicity]+=1
    total=[a+multiplicity*b for a,b in zip(total,coefficient)]
    local.append({'index':index,'ordered_factor_multiplicity':multiplicity,
                  'local_coefficient_basis':[str(x) for x in coefficient]})
expected=[F(v,32768) for v in [78,446,-211,-301,-301,-211,446,78]]
assert total==expected
assert multiplicities==Counter({6:65,3:11,1:1})
assert sum(m*k for m,k in multiplicities.items())==424
result={'scope':'Exact local determinant products; global application justified by K-010--K-014',
        'number_of_curves':424,'multiplicities':dict(multiplicities),
        'residue_basis':[str(x) for x in total],
        'primitive_partial_fraction_numerator':[str(x/2) for x in total],
        'locals':local}
(root/'n5_residue_verified.json').write_text(json.dumps(result,indent=2))
print('PASS all77 exact local products and424-component weighted sum')
print('residue basis',result['residue_basis'])
print('partial fraction numerator',result['primitive_partial_fraction_numerator'])
