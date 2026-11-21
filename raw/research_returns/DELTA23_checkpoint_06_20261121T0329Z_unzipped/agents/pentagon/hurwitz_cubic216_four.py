#!/usr/bin/env python3
"""Genuine B4/Z Hurwitz extension retaining the marked cubic216 detector.

All four-tuples in the order-six class of ASL2(F3), modulo simultaneous
conjugation, are constructed.  We retain only orbits whose first-three
forgetful map hits the verified degree36 cubic-detector orbit.
"""
import itertools,json,pathlib,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=pathlib.Path(__file__).parent
def run():
 st=time.monotonic();sl=[a for a in itertools.product(range(3),repeat=4) if (a[0]*a[3]-a[1]*a[2])%3==1]
 els=[v+a for v in itertools.product(range(3),repeat=2)for a in sl];ix={a:j for j,a in enumerate(els)};n=len(els);one=ix[(0,0,1,0,0,1)]
 def mm(a,b):
  u,v,A,B,C,D=a;x,y,E,F,G,H=b
  return ((u+A*x+B*y)%3,(v+C*x+D*y)%3,(A*E+B*G)%3,(A*F+B*H)%3,(C*E+D*G)%3,(C*F+D*H)%3)
 mt=np.array([[ix[mm(a,b)]for b in els]for a in els],dtype=np.int16)
 iv=np.array([next(j for j in range(n)if mt[i,j]==one)for i in range(n)],dtype=np.int16)
 seed=ix[(0,0,2,1,0,2)];cl=sorted({int(mt[mt[g,seed],iv[g]])for g in range(n)});ci={g:j for j,g in enumerate(cl)};m=len(cl);assert m==36
 con=np.array([[ci[int(mt[mt[g,a],iv[g]])]for a in cl]for g in range(n)],dtype=np.int16)
 cen=np.where(con[:,0]==0)[0];assert len(cen)==6
 transport=np.array([next(g for g in range(n)if con[g,a]==0)for a in range(m)])
 def make(k):
  size=m**(k-1);ids=np.full(size,-1,dtype=np.int32);reps=[]
  for code in range(size):
   if ids[code]>=0:continue
   js=[];tmp=code
   for _ in range(k-1):js.append(tmp%m);tmp//=m
   js=js[::-1];trans=con[cen[:,None],np.array(js)[None,:]];codes=np.zeros(len(cen),dtype=int)
   for j in range(k-1):codes=codes*m+trans[:,j]
   ids[codes]=len(reps);reps.append([0]+js)
  reps=np.array(reps,dtype=np.int16);ps=[]
  for j in range(k-1):
   a=reps.copy();u=np.array(cl)[a[:,j]];v=np.array(cl)[a[:,j+1]]
   a[:,j]=[ci[int(w)]for w in mt[mt[u,v],iv[u]]];a[:,j+1]=reps[:,j]
   gs=transport[a[:,0]];a=con[gs[:,None],a];codes=np.zeros(len(a),dtype=int)
   for t in range(1,k):codes=codes*m+a[:,t]
   p=ids[codes];assert len(set(p))==len(reps);ps.append(p)
  return ids,reps,ps
 ids3,reps3,ps3=make(3);ids4,reps4,ps4=make(4)
 def orbits(ps):
  seen=set();out=[]
  for a in range(len(ps[0])):
   if a in seen:continue
   todo=[a];seen.add(a)
   for v in todo:
    for p in ps:
     w=int(p[v])
     if w not in seen:seen.add(w);todo.append(w)
   out.append(todo)
  return out
 # Locate the positive first-three orbit by its literal previously checked seed.
 base=json.loads((ROOT/'hurwitz_cubic216_order6_triples.json').read_text())
 positive=next(row for row in base['orbits']if row['has_marked216_quotient'])
 triple=[ci[ix[tuple(v)]]for v in positive['representative']];assert triple[0]==0
 baseid=int(ids3[triple[1]*m+triple[2]])
 orb3=next(o for o in orbits(ps3)if baseid in o);assert len(orb3)==36
 idx3={v:j for j,v in enumerate(orb3)}
 small=[np.array([idx3[int(p[v])]for v in orb3])for p in ps3]
 pure=[p[p]for p in small]
 det=json.loads((ROOT/'cubic_detector_216.json').read_text())
 def aff(a):return [3*((a[0]*(v//3)+a[1]*(v%3)+a[2])%3)+(a[3]*(v//3)+a[4]*(v%3)+a[5])%3 for v in range(9)]
 target=[aff(det[k])for k in ['x','y']]
 G=PermutationGroup([Permutation(p.tolist())for p in pure]);J=PermutationGroup([Permutation(p.tolist()+[36+v for v in q])for p,q in zip(pure,target)])
 assert G.order()==J.order()==1944
 # Full B4 relations, including the central full twist.
 a,b,c=ps4;I=np.arange(len(a));mul=lambda a,b:a[b]
 assert np.array_equal(mul(mul(a,b),a),mul(mul(b,a),b))
 assert np.array_equal(mul(mul(b,c),b),mul(mul(c,b),c))
 assert np.array_equal(mul(a,c),mul(c,a))
 z=mul(mul(a,b),c);z=mul(mul(mul(z,z),z),z);assert np.array_equal(z,I)
 rows=[];all_four_orbits=sorted(orbits(ps4),key=len)
 all_degrees=[len(o)for o in all_four_orbits];assert all_degrees.count(1344)==1
 for oi,orb4 in enumerate(all_four_orbits):
  ix4={v:j for j,v in enumerate(orb4)};raw=reps4[orb4]
  forgot=ids3[raw[:,1].astype(int)*m+raw[:,2]]
  subset=[j for j,v in enumerate(forgot)if int(v) in idx3]
  if not subset:continue
  local=[np.array([ix4[int(p[v])]for v in orb4])for p in ps4]
  fm={j:idx3[int(forgot[j])]for j in subset}
  assert set(fm.values())==set(range(36))
  for gi in range(2):
   assert all(int(local[gi][v])in fm and fm[int(local[gi][v])]==int(small[gi][fm[v]])for v in subset)
  seedrow=raw[0];p=one
  for h in seedrow:p=int(mt[p,cl[h]])
  po=1;v=p
  while v!=one:po+=1;v=int(mt[v,p])
  entry={'orbit':oi,'degree':len(orb4),'first_detector_subset_degree':len(subset),
         'representative':[els[cl[v]]for v in seedrow],
         'detector_seed':[els[cl[v]]for v in raw[subset[0]]],
         'product':els[p],'product_order':po,'marked216_retained':'PASS',
         'first_forgetting_equivariance':'PASS'}
  rows.append(entry);print(json.dumps(entry),flush=True)
  np.savez_compressed(ROOT/f'hurwitz_cubic216_four_{oi}.npz',generators=np.array(local),
                      detector_subset=np.array(subset),detector_map=np.array([fm[v]for v in subset]),
                      detector_generators=np.array(small),
                      tuple_elements=np.array([[els[cl[v]]for v in row]for row in raw]))
 out={'group':'ASL2(F3)','class_size':36,'total_quotient_degree':len(reps4),
      'total_B4_orbits':len(all_four_orbits),'all_B4_orbit_degrees':all_degrees,'retaining_orbits':rows,
      'all_braid_and_full_twist_relations':'PASS','elapsed_seconds':time.monotonic()-st,
      'scope':'Genuine finite B4/Z representations retaining the marked cubic detector. No pentagon solution census yet.'}
 (ROOT/'hurwitz_cubic216_four.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k!='retaining_orbits'}),flush=True)
if __name__=='__main__':run()
