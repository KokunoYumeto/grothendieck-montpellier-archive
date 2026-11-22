"""Exact modular Lie and complete weight-count replay for K-019."""
from pathlib import Path
from itertools import product
from collections import Counter
import json
import numpy as np

root=Path(__file__).resolve().parent
data=json.loads((root/'n9_period512_counterexample.json').read_text())
n=9;support=set(map(tuple,data['support']));weights=data['W'];prime=10007
matrix=np.zeros((n**3,3*n*n),dtype=np.int64)
for row,edge in enumerate(product(range(n),repeat=3)):
    for mode in range(3):
        for source_coordinate in range(n):
            source=list(edge);source[mode]=source_coordinate
            if tuple(source) in support:
                matrix[row,mode*n*n+edge[mode]*n+source_coordinate]=1
rank=0;pivots=[];row_ids=list(range(n**3))
for col in range(3*n*n):
    pivot=next((i for i in range(rank,n**3) if matrix[i,col]%prime),None)
    if pivot is None:continue
    matrix[[rank,pivot]]=matrix[[pivot,rank]]
    row_ids[rank],row_ids[pivot]=row_ids[pivot],row_ids[rank]
    pivots.append([row_ids[rank],col])
    matrix[rank]=matrix[rank]*pow(int(matrix[rank,col]),-1,prime)%prime
    indices=np.nonzero(matrix[rank+1:,col])[0]+rank+1
    if len(indices):
        matrix[indices]=(matrix[indices]-matrix[indices,col,None]*matrix[rank,None,:])%prime
    rank+=1
assert rank==241 and pivots==data['GL_lie_minor_pivots_mod_10007']
pairs=[[(i,j) for i in range(n) for j in range(i+1,n)
        if (factor[i]-factor[j])%512==256] for factor in weights]
assert pairs==[[],[(0,6)],[]]
counts=[]
for modulus,expected in [(512,(25,24,1)),(256,(30,26,4))]:
    fixed_v=sum(sum(edge)%modulus==0 for edge in product(*weights))
    fixed_sl=sum(sum(m*m for m in Counter(a%modulus for a in factor).values())
                 for factor in weights)-3
    assert (fixed_v,fixed_sl,fixed_v-fixed_sl)==expected
    counts.append({'modulus':modulus,'fixed_tensor_dimension':fixed_v,
                   'fixed_SL_lie_dimension':fixed_sl,'fixed_quotient_tangent_dimension':fixed_v-fixed_sl})
(root/'n9_stabilizer_checks.json').write_text(json.dumps({
    'GL_lie_rank_mod_10007':rank,'antipodal_pairs':pairs,'counts':counts},indent=2))
print('PASS K-019: Lie rank241, simple spectra, antipodal-free factors, complete fixed dimensions1 and4')
