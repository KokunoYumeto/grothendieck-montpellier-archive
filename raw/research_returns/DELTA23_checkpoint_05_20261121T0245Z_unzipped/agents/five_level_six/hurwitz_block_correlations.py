#!/usr/bin/env python3
"""Exact block-kernel correlations and its binary outer-coordinate image."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_block_stabilizer import group,compact,inverse

HERE=Path(__file__).parent;PENT=HERE.parent/'pentagon'
def rank2(a):
 a=np.array(a,dtype=np.uint8).copy();r=0
 for j in range(a.shape[1]):
  piv=next((i for i in range(r,len(a)) if a[i,j]),None)
  if piv is None:continue
  a[[r,piv]]=a[[piv,r]]
  for i in range(len(a)):
   if i!=r and a[i,j]:a[i]^=a[r]
  r+=1
 return r,a[:r]
def run():
 start=time.monotonic()
 d=np.load(HERE/'hurwitz_block_stabilizer.npz')
 raw=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators']
 b=np.load(PENT/'hurwitz_cubic216_four_13_block0.npz')
 qs,blocks=b['generators'],b['block_map'];base=d['base'];loc={int(v):i for i,v in enumerate(base)}
 ts={0:np.arange(1344)};todo=[0]
 for v in todo:
  for g,q in zip(raw,qs):
   w=int(q[v])
   if w not in ts:ts[w]=g[ts[v]];todo.append(w)
 assert len(ts)==12
 def restrict(p):return np.array([loc[int(v)] for v in p[base]],dtype=np.int16)
 norm=np.array([[restrict(inverse(ts[j])[p[ts[j]]]) for j in range(12)] for p in d['kernel_full']])
 H=group(d['stabilizer_compact']);S=H.derived_subgroup();assert H.order()==6531840 and S.order()==3265920
 S.schreier_sims()
 signs=np.array([[int(not S.contains(Permutation(p.tolist()))) for p in row] for row in norm],dtype=np.uint8)
 sr,basis=rank2(signs)
 print('binary code rank',sr,'basis',basis.tolist(),flush=True)
 Q=group(qs);qorbs=sorted([sorted(o) for o in Q.stabilizer(0).orbits()],key=len)
 qseries=[int(g.order()) for g in Q.derived_series()]
 assert qseries==[216,72,18,9,1]
 print('block quotient stabilizer orbits',qorbs,flush=True)
 parallel0=[0]+next(o for o in qorbs if len(o)==2)
 parallel=sorted({tuple(sorted(int(g(v)) for v in parallel0)) for g in Q.generate_schreier_sims()})
 assert len(parallel)==4 and sorted(sum((list(t) for t in parallel),[]))==list(range(12))
 assert all(len({sum(int(row[v]) for v in t)%2 for t in parallel})==1 for row in basis)
 assert sr==9
 # The binary character of each local transition gives a genuine24-point
 # signed-block quotient, without using a classical-group identification.
 signed=[];transition_signs=[]
 for g,q in zip(raw,qs):
  p=np.empty(24,dtype=np.int16);sg=[]
  for j in range(12):
   k=int(q[j]);local=restrict(inverse(ts[k])[g[ts[j]]])
   assert H.contains(Permutation(local.tolist()))
   bit=int(not S.contains(Permutation(local.tolist())));sg.append(bit)
   p[2*j]=2*k+bit;p[2*j+1]=2*k+(bit^1)
  signed.append(p);transition_signs.append(sg)
 a,b,c=signed;one=np.arange(24)
 assert np.array_equal(a[b[a]],b[a[b]]) and np.array_equal(b[c[b]],c[b[c]])
 assert np.array_equal(a[c],c[a]);z=a[b[c]];assert np.array_equal(z[z[z[z]]],one)
 G24=group(signed);assert G24.order()==110592
 px,py=a[a],b[b];mx=c[c];ss=a[b[a]];my=ss[ss]
 target=json.loads((PENT/'cubic_detector_216.json').read_text())
 def aff(t):return np.array([3*((t[0]*(v//3)+t[1]*(v%3)+t[2])%3)+(t[3]*(v//3)+t[4]*(v%3)+t[5])%3 for v in range(9)])
 def joint(gs,us):return group([np.r_[g,len(g)+u] for g,u in zip(gs,us)])
 first=group([px,py]);fj=joint([px,py],[aff(target['x']),aff(target['y'])])
 mixed=group([mx,my]);mj=joint([mx,my],[np.array([1,2,0,3]),np.array([1,2,3,0])])
 signed_info={'degree':24,'order':int(G24.order()),'first_pair_order':int(first.order()),
              'first_joint_marked216_order':int(fj.order()),
              'mixed_pair_order':int(mixed.order()),'mixed_joint_markedS4_order':int(mj.order()),
              'generators':[p.tolist() for p in signed],'transition_signs':transition_signs}
 print('signed quotient',signed_info,flush=True)
 pairs=[]
 for orb in qorbs:
  j=orb[0]
  if j==0:continue
  gs=[np.r_[p[0],112+p[j]] for p in norm]
  J,short=compact(gs);jo=J.order()
  D=J.derived_subgroup();do=D.order()
  print('pair',j,'orders',jo,do,flush=True)
  pairs.append({'block':j,'equivalent_blocks':orb,'joint_order':int(jo),
                'joint_derived_order':int(do),'compact_generators':len(short),
                'generators':[g.tolist() for g in short]})
 # The rank-three orbital graph is checked directly without identification.
 orbs=H.stabilizer(0).orbits();neighbors=next(o for o in orbs if len(o)==30)
 hgs=d['stabilizer_compact'];ht={0:np.arange(112)};todo=[0]
 for v in todo:
  for g in hgs:
   w=int(g[v])
   if w not in ht:ht[w]=g[ht[v]];todo.append(w)
 A=np.zeros((112,112),dtype=np.int16)
 for v,t in ht.items():A[v,t[list(neighbors)]]=1
 assert np.array_equal(A,A.T) and np.all(np.diag(A)==0)
 A2=A@A
 assert np.all(np.diag(A2)==30)
 assert np.all(A2[A==1]==2)
 assert np.all(A2[(A==0)&(np.eye(112)==0)]==10)
 np.savez_compressed(HERE/'hurwitz_block_correlations.npz',normalized_kernel_generators=norm,
                     outer_signs=signs,outer_basis=basis,adjacency=A,
                     transversals=np.array([ts[j] for j in range(12)]),signed_generators=np.array(signed))
 out={'stabilizer_order':int(H.order()),'stabilizer_derived_order':int(S.order()),
      'outer_code_rank':sr,'outer_code_basis':basis.tolist(),
      'parallel_triples':[list(t) for t in parallel],'signed_quotient':signed_info,
      'quotient_point_stabilizer_orbits':qorbs,'pairs':pairs,
      'block_quotient_derived_orders':qseries,
      'orbital_graph_parameters':[112,30,2,10],
      'elapsed_seconds':time.monotonic()-start,
      'scope':'Exact finite kernel projections and binary quotient data. Abstract orthogonal identification and simplicity are separate.'}
 (HERE/'hurwitz_block_correlations.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='pairs'},indent=2))
if __name__=='__main__':run()
