"""Exact finite certificates used in the all-n proof K-020."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json
import numpy as np

root=Path(__file__).resolve().parent
data=json.loads((root/'amplifying_gadget_q8.json').read_text())
support=set(map(tuple,data['support']))
boundary=(4,0,1);output=(7,5,5);n=8
for triple in [boundary,output]:
    for mode in range(3):
        for coordinate in range(n):
            assert any(e[mode]==coordinate and
                       all(e[j]!=triple[j] for j in range(3) if j!=mode)
                       for e in support)
assert all(sum(e[j]==boundary[j] for j in range(3))<=1 for e in support)
lo=F(3,11);hi=F(37,61)
assert (125+43*lo)/256==F(47,88)
assert (125+43*hi)/256==F(36,61)
assert lo<F(47,88)<F(36,61)<hi
weights=[[225,54,113,161,1,72,36,222],
         [0,220,202,192,131,128,125,237],
         [53,0,18,95,238,162,159,220]]
assert sum(weights[a][boundary[a]] for a in range(3))%256==1
assert all(len(set(factor))==8 for factor in weights)
full={edge for edge in product(range(8),repeat=3)
      if sum(weights[a][edge[a]] for a in range(3))%256==0}
assert full==support
pairs=[[(i,j) for i in range(n) for j in range(i+1,n)
        if (factor[i]-factor[j])%256==128] for factor in weights]
assert pairs==[[],[(0,5)],[]]
matrix=np.zeros((n**3,3*n*n),dtype=np.int64)
for row,edge in enumerate(product(range(n),repeat=3)):
    for mode in range(3):
        for source_coordinate in range(n):
            source=list(edge);source[mode]=source_coordinate
            if tuple(source) in support:
                matrix[row,mode*n*n+edge[mode]*n+source_coordinate]=1
rank=0;pivots=[];row_ids=list(range(n**3));prime=10007
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
assert rank==190
result={'scope':'Finite data for the separate all-dimensional proof K-020',
        'boundary_pair_deletion_coverage':True,'output_pair_deletion_coverage':True,
        'no_two_boundary_coordinates':True,'positive_invariant_interval':True,
        'weights':weights,'boundary_character_exponent':1,'full_support_size':len(full),
        'antipodal_pairs':pairs,'GL_lie_rank_mod_10007':rank,'pivots':pivots}
(root/'gadget_stabilizer_checks.json').write_text(json.dumps(result,indent=2))
print('PASS K-020 finite data: both coverage conditions, rank190, spectral freeness, complete support22, unique B pair, invariant interval')
