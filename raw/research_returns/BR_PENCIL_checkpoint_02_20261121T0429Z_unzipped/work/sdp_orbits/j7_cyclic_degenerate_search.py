"""Search exact-support monomial degenerations of cyclic convolution rank13.
A successful rational cone will be converted to an exact integer certificate.
"""
from itertools import combinations
from pathlib import Path
import numpy as np,json,time
from scipy.optimize import linprog

p=13
vars_=[(i,j) for i in range(4) for j in range(3) if (i,j)!=(3,2)]
rects=[(1,0,1),(1,0,2),(1,1,2),(2,0,1),(2,0,2),(2,1,2),(3,0,1)]
# coordinates R1,R2,R3,C1,C2; R0=C0=0
vw=[]
for i,j in vars_:
 v=np.zeros(5,dtype=int)
 if i:v[i-1]=1
 if j:v[2+j]=1
 vw.append(v)
qw=[];desired=[]
for i,j,k in rects:
 q=np.zeros(5,dtype=int);q[i-1]=1
 if j:q[2+j]+=1
 if k:q[2+k]+=1
 qw.append(q)
 desired.append({(vars_.index(x),vars_.index(y)) for x,y in [((0,j),(i,k)),((i,k),(0,j)),((0,k),(i,j)),((i,j),(0,k))]})
start=time.time();cnt=0;feas=0;found=None;opp=0
for c2 in range(2,p):
 for r1,r2 in combinations(range(1,p),2):
  for r3 in range(1,p):
   residues=np.array([r1,r2,r3,1,c2])
   vs=[int(v@residues)%p for v in vw]
   if len(set(vs))<len(vs):continue
   qs=[int(q@residues)%p for q in qw]
   if len(set(qs))<len(qs):continue
   cnt+=1;constraints=set()
   for a,q in enumerate(qw):
    for i in range(len(vars_)):
     for j in range(len(vars_)):
      if (vs[i]+vs[j])%p==qs[a] and (i,j) not in desired[a]:
       d=tuple((vw[i]+vw[j]-q).tolist())
       assert any(d)
       constraints.add(d)
   opp+=any(tuple(-x for x in d) in constraints for d in constraints)
   M=np.array(sorted(constraints))
   sol=linprog(np.zeros(5),A_ub=-M,b_ub=-np.ones(len(M)),bounds=[(None,None)]*5,method='highs')
   if sol.success:
    found={'modulus':p,'residues':residues.tolist(),'variables':vars_,'rectangles':rects,'constraints':M.tolist(),'weight_solution_float':sol.x.tolist(),'candidate_index':cnt}
    print('FOUND',found,flush=True);break
  if found:break
 if found:break
print('eligible residue assignments',cnt,'seconds',time.time()-start,'found',bool(found),'opposite_pair_cases',opp,flush=True)
Path(__file__).with_name('j7_cyclic_search.json').write_text(json.dumps({'candidate':found,'eligible_assignments_examined':cnt,'seconds':time.time()-start},indent=2)+'\n')
