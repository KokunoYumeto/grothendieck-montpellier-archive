#!/usr/bin/env python3
"""Exact projective marking for the binary tetrahedral half-character."""
from pathlib import Path
import itertools,json
import numpy as np
HERE=Path(__file__).resolve().parents[1];ROOT=HERE.parents[1]
S=np.array([[0,1],[2,0]],dtype=int);R=np.array([[0,1],[2,1]],dtype=int);I=np.eye(2,dtype=int)
# P1 order infinity,0,1,2. F4 integers 0,1,w,w+1 with w^2=w+1.
def fm(a,b):
 out=0
 for i in range(2):
  if b>>i&1:out^=a<<i
 if out&4:out^=7
 return out
pts=[(1,0),(0,1),(1,1),(2,1)];mark=np.array([3,1,2,0]);lookup={p:i for i,p in enumerate(pts)}
def action(M):
 out=[]
 for p in pts:
  v=M@p%3
  if v[1]:v=v*int(v[1])%3
  else:v=v*int(v[0])%3
  out.append(lookup[tuple(map(int,v))])
 return np.array(out)
assert np.array_equal(mark[action(S)],mark^2)
assert np.array_equal(mark[action(R)],np.array([fm(2,int(t))for t in mark]))
assert np.array_equal(S@S%3,2*I%3)
assert np.array_equal(np.linalg.matrix_power(R,3)%3,2*I%3)
powers=[np.linalg.matrix_power(S,k)%3 for k in range(4)]
pre=[]
for v in itertools.product(range(3),repeat=4):
 M=np.array(v).reshape(2,2)
 if (v[0]*v[3]-v[1]*v[2])%3!=1:continue
 if any(np.array_equal(action(M),action(N))for N in [I,S]):pre.append(M)
assert len(pre)==4 and {m.tobytes()for m in pre}=={m.tobytes()for m in powers}
out={'statement':'D23.C36','projective_point_order':['infinity','0','1','2'],
     'F4_labels':[3,1,2,0],'S_is_translation_by_omega':True,'R_is_multiplication_by_omega':True,
     'cyclic_preimage_order':4,'result':'PASS'}
p=ROOT/'records/sl2_3_gentle_core.npz'
if p.exists():
 d=np.load(p);k=list(d['kernel_ids']).index(1)
 els=np.load(HERE/'records/affine216_marked_pair_kernels.npz')['elements']
 values=[els[int(row[k])][2:].reshape(2,2)for row in d['survivors']]
 theta=[next(i for i,N in enumerate(powers)if np.array_equal(M,N))for M in values]
 out['root_table_theta_values']=theta;assert sorted(theta)==list(range(4))
(HERE/'records/binary_tetrahedral_half_character.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
