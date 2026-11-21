#!/usr/bin/env python3
"""Search exact marked cubic216 quotients in a motivated B3 Hurwitz family.

The class consists of fixed-point-free affine elements of order three.
All triples, modulo simultaneous conjugation, are enumerated.  This is only
the B3 prerequisite to a potentially useful five-point test.
"""
import itertools,json,pathlib,time,sys
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=pathlib.Path(__file__).parent
def run(class_kind='free3'):
 st=time.monotonic();sl=[a for a in itertools.product(range(3),repeat=4) if (a[0]*a[3]-a[1]*a[2])%3==1]
 els=[v+a for v in itertools.product(range(3),repeat=2) for a in sl];idx={v:j for j,v in enumerate(els)};n=len(els);one=idx[(0,0,1,0,0,1)]
 def mm(a,b):
  u,v,A,B,C,D=a;x,y,E,F,G,H=b
  return ((u+A*x+B*y)%3,(v+C*x+D*y)%3,(A*E+B*G)%3,(A*F+B*H)%3,(C*E+D*G)%3,(C*F+D*H)%3)
 mt=np.array([[idx[mm(a,b)] for b in els] for a in els],dtype=np.int16)
 iv=np.array([next(j for j in range(n) if mt[i,j]==one) for i in range(n)],dtype=np.int16)
 seed=idx[(0,0,2,1,0,2) if class_kind=='order6' else (0,1,0,1,2,2)]
 cl=sorted({int(mt[mt[g,seed],iv[g]]) for g in range(n)});ci={g:j for j,g in enumerate(cl)};m=len(cl)
 assert m==(36 if class_kind=='order6' else 24)
 stem='hurwitz_cubic216_order6' if class_kind=='order6' else 'hurwitz_cubic216'
 con=np.array([[ci[int(mt[mt[g,a],iv[g]])] for a in cl] for g in range(n)],dtype=np.int16)
 ids=np.full(m**3,-1,dtype=np.int32);reps=[]
 for code in range(m**3):
  if ids[code]>=0:continue
  ijk=[code//m**2,code//m%m,code%m]
  orbit=con[:,ijk];codes=orbit[:,0].astype(int)*m*m+orbit[:,1]*m+orbit[:,2]
  ids[codes]=len(reps);reps.append([cl[j] for j in ijk])
 reps=np.array(reps,dtype=np.int16);N=len(reps);ps=[]
 for s in range(2):
  a=reps.copy();u=a[:,s].copy();v=a[:,s+1].copy();a[:,s]=mt[mt[u,v],iv[u]];a[:,s+1]=u
  local=np.array([[ci[int(x)]for x in row]for row in a]);codes=local[:,0]*m*m+local[:,1]*m+local[:,2]
  q=ids[codes];assert len(set(q))==N;ps.append(q)
 co=lambda a,b:a[b];A,B=ps;I=np.arange(N)
 assert np.array_equal(co(co(A,B),A),co(co(B,A),B))
 Q=co(A,B);assert np.array_equal(co(co(Q,Q),Q),I)
 # Every B3 orbit is invariant under the first pure pair.
 seen=set();orbits=[]
 for j in range(N):
  if j in seen:continue
  todo=[j];seen.add(j)
  for v in todo:
   for p in ps:
    w=int(p[v])
    if w not in seen:seen.add(w);todo.append(w)
  orbits.append(todo)
 detector=json.loads((ROOT/'cubic_detector_216.json').read_text())
 def aff(a):
  return [3*((a[0]*(v//3)+a[1]*(v%3)+a[2])%3)+(a[3]*(v//3)+a[4]*(v%3)+a[5])%3 for v in range(9)]
 xp,yp=[aff(detector[k])for k in ['x','y']];rows=[]
 for j,orb in enumerate(sorted(orbits,key=len)):
  ix={v:k for k,v in enumerate(orb)};pa,pb=[np.array([ix[int(p[v])]for v in orb])for p in ps]
  x,y=pa[pa],pb[pb];X,Y=Permutation(x.tolist()),Permutation(y.tolist());G=PermutationGroup([X,Y]);order=int(G.order())
  d=len(orb);joint=PermutationGroup([Permutation(x.tolist()+[d+v for v in xp]),Permutation(y.tolist()+[d+v for v in yp])]);jo=int(joint.order())
  row={'orbit':j,'degree':d,'representative':[els[t]for t in reps[orb[0]]],
       'pure_generator_orders':[int(X.order()),int(Y.order())],'pure_group_order':order,
       'joint_with_marked216_order':jo,'has_marked216_quotient':jo==order}
  if jo==order:
   np.savez_compressed(ROOT/f'{stem}_triple_{j}.npz',generators=np.array([pa,pb]))
  rows.append(row);print(json.dumps(row),flush=True)
 # Retain raw triples as well: a fourth point can retain this framing, so
 # failure in the conjugacy quotient alone would not be a sufficient gate.
 raw=[];raw_x=[];raw_y=[]
 for row in rows:
  seed0=tuple(idx[tuple(v)]for v in row['representative']);todo=[seed0];seen={seed0:0};pp=[[],[]]
  for v in todo:
   for j in range(2):
    a=list(v);u,w=a[j:j+2];a[j]=int(mt[mt[u,w],iv[u]]);a[j+1]=u;a=tuple(a)
    if a not in seen:seen[a]=len(todo);todo.append(a)
    pp[j].append(seen[a])
  pa,pb=map(np.array,pp);x,y=pa[pa],pb[pb];d=len(todo)
  G=PermutationGroup([Permutation(x.tolist()),Permutation(y.tolist())]);order=int(G.order())
  J=PermutationGroup([Permutation(x.tolist()+[d+v for v in xp]),Permutation(y.tolist()+[d+v for v in yp])]);jo=int(J.order())
  rr={'orbit':row['orbit'],'degree':d,'pure_order':order,'joint_with_marked216_order':jo,
      'has_marked216_quotient':jo==order};raw.append(rr);print(json.dumps(rr),flush=True)
  raw_x.append(x);raw_y.append(y)
  np.savez_compressed(ROOT/f'{stem}_raw_triple_{row["orbit"]}.npz',generators=np.array([pa,pb]))
 def cat(xs):
  off=0;v=[]
  for a in xs:v.extend((a+off).tolist());off+=len(a)
  return v
 xx,yy=cat(raw_x),cat(raw_y);d=len(xx)
 G=PermutationGroup([Permutation(xx),Permutation(yy)])
 J=PermutationGroup([Permutation(xx+[d+v for v in xp]),Permutation(yy+[d+v for v in yp])])
 full_order,full_joint=int(G.order()),int(J.order())
 out={'group':'ASL2(F3)','group_order':216,'class_representative':els[seed],'class_size':m,
      'triple_quotient_degree':N,'braid_and_full_twist':'PASS','orbits':rows,
      'raw_triple_orbits':raw,'joint_raw_pure_order':full_order,
      'joint_raw_with_marked216_order':full_joint,
      'kernel_in_marked216_order':full_joint//full_order,
      'elapsed_seconds':time.monotonic()-st,
      'scope':'Exact B3 prerequisite search; no five-point or GT conclusion.'}
 (ROOT/f'{stem}_triples.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k!='orbits'}),flush=True)
if __name__=='__main__':run(sys.argv[1] if len(sys.argv)>1 else 'free3')
