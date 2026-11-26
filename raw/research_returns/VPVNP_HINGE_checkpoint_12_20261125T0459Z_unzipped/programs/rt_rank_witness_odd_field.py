"""Search Mat_3(F_3) for an isometric rank realization of the SH20 eight points.

This is a finite diagnostic. A success is verified on all64 pair distances;
a failure would concern only the normalized3x3 search, not arbitrary matrices.
"""
from pathlib import Path
from itertools import combinations
import json,time
import numpy as np

W=Path(__file__).resolve().parents[1]
q=3;size=q**9;weights=q**np.arange(9,dtype=np.int64)
digits=(np.arange(size,dtype=np.int64)[:,None]//weights)%q
M=digits.reshape(size,3,3)
det=(M[:,0,0]*(M[:,1,1]*M[:,2,2]-M[:,1,2]*M[:,2,1])
     -M[:,0,1]*(M[:,1,0]*M[:,2,2]-M[:,1,2]*M[:,2,0])
     +M[:,0,2]*(M[:,1,0]*M[:,2,1]-M[:,1,1]*M[:,2,0]))%q
ranks=np.any(digits,axis=1).astype(np.int8)
for rows in combinations(range(3),2):
 for cols in combinations(range(3),2):
  minor=(M[:,rows[0],cols[0]]*M[:,rows[1],cols[1]]-M[:,rows[0],cols[1]]*M[:,rows[1],cols[0]])%q
  ranks=np.maximum(ranks,2*(minor!=0))
ranks[det!=0]=3
rank1=digits[ranks==1]
assert len(rank1)==338
def diff_rank(a,b):return int(ranks[int(((digits[a]-digits[b])%q)@weights)])
A=int(weights[0]);B=int(weights[4]);target=[0,1,1,2,2,3,3,2]
records=[];solution=None
for a in (1,2):
 for b,c in __import__('itertools').product(range(3),repeat=2):
  if (b*c-a*(a-1))%3:continue
  D=int(a*weights[0]+b*weights[1]+c*weights[3]+a*weights[4])
  rA=ranks[((digits-digits[A])%3)@weights]
  rB=ranks[((digits-digits[B])%3)@weights]
  rD=ranks[((digits-digits[D])%3)@weights]
  K=np.flatnonzero((ranks==2)&(rA==3)&(rB==3)&(rD==2))
  L=np.flatnonzero((ranks==3)&(rA==2)&(rB==2)&(rD==3))
  isK=np.zeros(size,dtype=bool);isK[K]=True;pair_first={};edges=0
  for E in L:
   neighbors=((digits[E]-rank1)%3)@weights
   neighbors=neighbors[isK[neighbors]];edges+=len(neighbors)
   for C,G in combinations(sorted(map(int,neighbors)),2):
    if diff_rank(C,G)!=2:continue
    key=(C,G)
    if key in pair_first:
     F=pair_first[key]
     if diff_rank(E,F)==2:
      ids=[0,A,B,D,C,int(E),int(F),G]
      assert all(diff_rank(ids[i],ids[j])==target[i^j] for i in range(8) for j in range(8))
      solution={'ids':ids,'matrices':[M[x].tolist()for x in ids],
                'pair_rank_matrix':[[diff_rank(ids[i],ids[j])for j in range(8)]for i in range(8)],
                'field':'F3','valid_over':'Every extension field of F3, in particularF9',
                'checks':64}
      break
    else:pair_first[key]=int(E)
   if solution:break
  records.append({'lower_square_parameters':[a,b,c],'K':len(K),'L':len(L),
                  'visited_rank_one_edges':edges,'tested_K_pairs':len(pair_first)})
  print(json.dumps(records[-1]),flush=True)
  if solution:break
 if solution:break
out={'status':'FOUND_AND_VERIFIED'if solution else'NO_REALIZATION_IN_SEARCHED_NORMAL_FORMS',
     'records':records,'solution':solution,'rank_one_matrices':338}
(W/'outputs/rt_rank_witness_F3.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out['solution']or{'status':out['status']}),flush=True)
