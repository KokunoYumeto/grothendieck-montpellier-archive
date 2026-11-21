#!/usr/bin/env python3
"""Genuine B4/Z Hurwitz quotients from affine reflection tuples over F3."""
import itertools,json,pathlib,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

def run(p_choice='translation',analyze=True):
 st=time.monotonic();gl=[v for v in itertools.product(range(3),repeat=4) if (v[0]*v[3]-v[1]*v[2])%3]
 els=[v+a for v in itertools.product(range(3),repeat=2) for a in gl];idx={v:j for j,v in enumerate(els)};n=len(els);one=idx[(0,0,1,0,0,1)]
 def mm(a,b):
  u,v,A,B,C,D=a;x,y,E,F,G,H=b
  return ((u+A*x+B*y)%3,(v+C*x+D*y)%3,(A*E+B*G)%3,(A*F+B*H)%3,(C*E+D*G)%3,(C*F+D*H)%3)
 mt=np.array([[idx[mm(a,b)] for b in els] for a in els],dtype=np.int16)
 iv=np.array([next(j for j in range(n) if mt[i,j]==one) for i in range(n)],dtype=np.int16)
 ref=idx[(0,0,1,0,0,2)];cl=sorted({int(mt[mt[g,ref],iv[g]]) for g in range(n)});ci={g:j for j,g in enumerate(cl)};m=len(cl);assert m==36
 choices={'translation':(1,0,1,0,0,1),'unipotent':(0,0,1,1,0,1),'affine_unipotent':(0,1,1,1,0,1),'cubic':(1,0,0,2,1,2)}
 p=idx[choices[p_choice]];cent=[g for g in range(n) if mt[g,p]==mt[p,g]]
 con=np.array([[ci[int(mt[mt[g,a],iv[g]])] for a in cl] for g in cent],dtype=np.int16)
 ids=np.full(m**3,-1,dtype=np.int32);reps=[];valid=0
 for code in range(m**3):
  if ids[code]>=0:continue
  i=code//m**2;j=code//m%m;k=code%m;a,b,c=[cl[t] for t in [i,j,k]];d=int(mt[iv[mt[mt[a,b],c]],p])
  if d not in ci:continue
  t=con[:,[i,j,k]];codes=t[:,0].astype(int)*m*m+t[:,1]*m+t[:,2]
  ids[codes]=len(reps);reps.append([a,b,c,d])
 reps=np.array(reps,dtype=np.int16);N=len(reps);ps=[]
 for s in range(3):
  t=reps.copy();u=t[:,s].copy();v=t[:,s+1].copy();t[:,s]=mt[mt[u,v],iv[u]];t[:,s+1]=u
  local=np.array([[ci[int(x)] for x in row[:3]] for row in t]);codes=local[:,0]*m*m+local[:,1]*m+local[:,2];pp=ids[codes]
  assert min(pp)>=0 and len(set(pp))==N;ps.append(pp)
 co=lambda p,q:p[q]
 assert np.array_equal(co(co(ps[0],ps[1]),ps[0]),co(co(ps[1],ps[0]),ps[1]))
 assert np.array_equal(co(co(ps[1],ps[2]),ps[1]),co(co(ps[2],ps[1]),ps[2]))
 assert np.array_equal(co(ps[0],ps[2]),co(ps[2],ps[0]))
 z=co(co(ps[0],ps[1]),ps[2]);z=co(co(co(z,z),z),z);assert np.array_equal(z,np.arange(N))
 covered=set();orbits=[]
 for a in range(N):
  if a in covered:continue
  orbit=[a];covered.add(a);cur=0
  while cur<len(orbit):
   x=orbit[cur];cur+=1
   for q in ps:
    y=int(q[x])
    if y not in covered:covered.add(y);orbit.append(y)
  orbits.append(orbit)
 rows=[]
 for oi,orbit in enumerate(sorted(orbits,key=len)):
  vi={v:j for j,v in enumerate(orbit)};s=[Permutation([vi[int(p[v])] for v in orbit]) for p in ps]
  x=[s[0]**2,s[1]**2,s[2]**2,(s[0]*s[1]*s[0])**2,(s[2]*s[1]*s[2])**2]
  np.savez_compressed(pathlib.Path(__file__).with_name(f'hurwitz_affine_{p_choice}_{oi}.npz'),generators=np.array([p.array_form for p in s]))
  pairs=[]
  for a,b in ([(0,1),(2,3),(3,4)] if analyze else []):
   g=PermutationGroup([x[a],x[b]]);ds=g.derived_series();orders=[int(h.order()) for h in ds]
   pairs.append({'pair':[a+1,b+1],'derived_orders':orders,'second_derived_nilpotent':bool(ds[min(2,len(ds)-1)].is_nilpotent)})
  row={'orbit':oi,'degree':len(orbit),'representative':[els[j] for j in reps[orbit[0]]],'pair_data':pairs};rows.append(row);print(json.dumps(row),flush=True)
  if not all(r['second_derived_nilpotent'] for r in pairs):
   np.savez_compressed(pathlib.Path(__file__).with_name(f'hurwitz_affine_{p_choice}_{oi}.npz'),generators=np.array([p.array_form for p in s]))
 out={'group':'F3^2 semidirect GL2(F3)','group_order':n,'reflection_class_size':m,'product':choices[p_choice],'product_centralizer_order':len(cent),'quotient_degree':N,'orbit_count':len(orbits),'orbits':rows,'all_braid_and_full_twist_relations':'PASS','elapsed_seconds':time.monotonic()-st}
 suffix='' if analyze else '_orbit_inventory'
 pathlib.Path(__file__).with_name(f'hurwitz_affine_{p_choice}{suffix}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='orbits'}),flush=True)
if __name__=='__main__':run()
