#!/usr/bin/env python3
from pathlib import Path
import json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;start=time.monotonic()
d=np.load(HERE/'hurwitz_colored_raw48_gentle.npz');n=len(d['x']);k=d['raw_subset'];targetC=d['new_C'];c=d['raw_C']
invt=np.load(HERE.parent/'characters/records/affine216_marked_pair_kernels.npz');els=invt['elements'];x0,y0=map(int,invt['cubic_pair'])
def aff(g):
 u,v,A,B,C,D=map(int,g);return np.array([3*((u+A*(j//3)+B*(j%3))%3)+(v+C*(j//3)+D*(j%3))%3 for j in range(9)])
xi=np.array([aff(els[x0]),aff(els[y0])]);s4=np.array([[1,2,0,3],[1,2,3,0]])
gens=np.array([np.r_[g,n+h,n+9+t]for g,h,t in zip([d['x'],d['y']],xi,s4)])
G=PermutationGroup([Permutation(g.tolist())for g in gens]);order=int(G.order());D=G.derived_subgroup();do=int(D.order());print('order',order,'derived',do,flush=True)
rows=[]
for j,f in enumerate(d['all_gentle']):
 for rho in range(3):
  mat=np.array([[1,rho],[rho,1+rho*rho]])%3
  for a3 in[0,1]:
   ee=(a3,(rho+(rho+1)*a3)%3,*mat.ravel());ff=aff(ee)
   for a2 in[0,1]:
    pp=s4[0];tt=s4[1];perm=np.arange(4)
    for _ in range(2*a2):perm=perm[tt]
    for _ in range(rho):perm=perm[pp]
    target=np.r_[f,n+ff,n+9+perm]
    if D.contains(Permutation(target.tolist())):
     rawR=f[:48];cov=np.array_equal(rawR[c[np.argsort(rawR)]],targetC)
     rows.append({'gentle_index':j,'rho':rho,'a3':a3,'a2':a2,'raw_C_covariance':bool(cov)})
print('normalized',[r for r in rows if r['rho']==0 and r['a3']==1 and r['a2']==0],flush=True)
(HERE/'hurwitz_colored_raw48_frame_labels.json').write_text(json.dumps({'order':order,'derived_order':do,'labels':rows,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
