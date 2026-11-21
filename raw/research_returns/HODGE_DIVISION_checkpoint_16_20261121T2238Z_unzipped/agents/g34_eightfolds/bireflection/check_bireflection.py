#!/usr/bin/env python3
"""Exact finite checks accompanying D-BI-01--04.

The group classification, Hurwitz factorization and universal dimension
inequalities are mathematical proofs, not conclusions from this checker.
The ATLAS matrices are retained numerical data with explicit provenance.
"""
from pathlib import Path
import json,time
import sympy as S

HERE=Path(__file__).resolve().parent
start=time.monotonic()
def zero(A): return all(S.expand(z)==0 for z in A)
data=json.loads((HERE/'u52_witness.json').read_text())
M={k:S.Matrix([[a+S.I*b for a,b in row] for row in v])
   for k,v in data['matrices'].items()}
x,y,B,H=(M[k] for k in ['x','y','B1','B2'])
I=S.eye(10)
assert zero(B+B.T) and S.simplify(B.det())==1
assert zero(H-H.conjugate().T) and S.simplify(H.det())==32
assert zero(x*x-I) and zero(y**5-I) and zero((x*y)**11-I)
for A in [x,y]:
    # The original ATLAS matrices act on row vectors.
    assert zero(A*B*A.T-B)
    assert zero(A*H*A.conjugate().T-H)
leading=[S.simplify(H[:k,:k].det()) for k in range(1,11)]
assert all(z.is_positive for z in leading)
C=S.Matrix.vstack(*[S.kronecker_product(I,A)-S.kronecker_product(A.T,I)
                     for A in [x,y]])
rank=C.to_DM().convert_to(S.QQ_I).rank()
assert rank==99

permutation=[]
for m in range(9,15):
    q=m-(m+1)//3
    assert 20+2*q>2*m+6
    permutation.append({'m':m,'total_moving_budget':2*m+6,
                        'nonreal_scalar_rank_lower_bound':q,
                        'two_nonreal_scalars_total_lower_bound':20+2*q})
blocks=[]
for m in range(9,15):
    for d in range(3,m):
        if m%d: continue
        t=m//d
        if 2*t+d>=11:
            blocks.append({'m':m,'t':t,'d':d,'2t_plus_d':2*t+d})
assert blocks==[{'m':12,'t':4,'d':3,'2t_plus_d':11},
                {'m':14,'t':2,'d':7,'2t_plus_d':11}]
for m in [10,12,14]:
    assert 3*m//2+18>2*m+6

out={'status':'PASS','atlas_source_sha256':data['source_sha256'],
     'row_action_invariant_alternating_determinant':1,
     'row_action_invariant_hermitian_determinant':32,
     'hermitian_leading_principal_minors':[int(z) for z in leading],
     'centralizer_dimension_over_Qi':100-rank,
     'generator_orders_and_product_order':[2,5,11],
     'permutation_scalar_budget':permutation,
     'remaining_imprimitive_block_sizes':blocks,
     'scope':'Exact retained-matrix invariance, positivity and commutant; arithmetic budget tables. The published classification and family-level rank proof are separate inputs/proofs.',
     'elapsed_seconds':time.monotonic()-start}
(HERE/'check_bireflection.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
