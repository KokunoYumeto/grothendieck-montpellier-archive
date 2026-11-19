"""Exact cube orbit certificates and characteristic-five projective counterexample."""
from itertools import permutations,product,combinations
from collections import Counter
import json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'outputs'
def psign(a):return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
rot=[(p,s) for p in permutations(range(3)) for s in product([-1,1],repeat=3) if psign(p)*s[0]*s[1]*s[2]==1]
def act(g,v):p,s=g;return tuple(s[i]*v[p[i]] for i in range(3))
verts=set(product([-1,1],repeat=3))
anti=lambda v:tuple(-x for x in v)
edges={frozenset([a,b]) for a,b in combinations(verts,2) if sum(x!=y for x,y in zip(a,b))==1}
faces={frozenset(v for v in verts if v[i]==s) for i in range(3) for s in [-1,1]}
body={frozenset([v,anti(v)]) for v in verts}
oppedges={frozenset([a,frozenset(anti(v) for v in a)]) for a in edges}
oppfaces={frozenset([a,frozenset(anti(v) for v in a)]) for a in faces}
directed={(a,b) for a,b in product(verts,repeat=2) if frozenset([a,b]) in edges}
tetra={frozenset(v for v in verts if v[0]*v[1]*v[2]==s) for s in [-1,1]}
diagonals={frozenset([a,b]) for a,b in combinations(verts,2) if sum(x!=y for x,y in zip(a,b))==2}
dirs={tuple((i,j)) for i in range(3) for j in range(3) if i!=j}
def aset(g,o):return frozenset(act(g,v) for v in o)
rows=[('vertices',verts,act,8,3),('edges',edges,aset,12,2),('faces',faces,aset,6,4),('body_diagonals',body,aset,4,6),('opposite_edges',oppedges,lambda g,o:frozenset(aset(g,a) for a in o),6,4),('opposite_faces',oppfaces,lambda g,o:frozenset(aset(g,a) for a in o),3,8),('directed_edges',directed,lambda g,o:tuple(act(g,v) for v in o),24,1),('tetrahedra',tetra,aset,2,12),('face_diagonals',diagonals,aset,12,2),('ordered_face_directions',dirs,lambda g,o:tuple(g[0].index(i) for i in o),6,4)]
cube=[]
bd=sorted(body,key=lambda x:sorted(x))
for name,objs,action,n,h in rows:
 o=next(iter(objs));orb={action(g,o) for g in rot};stab=[g for g in rot if action(g,o)==o]
 assert orb==objs and len(objs)==n and len(stab)==h
 stypes=[]
 for g in stab:
  p=tuple(bd.index(aset(g,x)) for x in bd)
  stypes.append({'permutation':p,'sign':psign(p),'fixed_body_diagonals':sum(i==j for i,j in enumerate(p))})
 if name=='face_diagonals':assert sorted(x['sign'] for x in stypes)==[1,1]
 if name=='edges':assert sorted(x['sign'] for x in stypes)==[-1,1]
 cube.append({'object':name,'size':n,'stabilizer_order':h,'stabilizer_on_body_diagonals':stypes})

def field(p,quadratic=False):
 n=p*p if quadratic else p
 def ad(x,y):return ((x%p+y%p)%p)+p*((x//p+y//p)%p) if quadratic else (x+y)%p
 def neg(x):return ((-x%p)%p)+p*((-(x//p))%p) if quadratic else -x%p
 def mu(x,y):
  if not quadratic:return x*y%p
  a,b=x%p,x//p;c,d=y%p,y//p
  return (a*c-b*d)%p+p*((a*d+b*c)%p)
 def iv(x):return next(y for y in range(n) if mu(x,y)==1)
 return n,ad,neg,mu,iv
results=[]
for p,quadratic in [(3,True),(5,False),(13,False),(17,False)]:
 q,ad,neg,mu,iv=field(p,quadratic)
 sqri=next(x for x in range(q) if mu(x,x)==neg(1))
 inf=q
 D={0,inf,1,neg(1),sqri,neg(sqri)}
 opp={frozenset([0,inf]),frozenset([1,neg(1)]),frozenset([sqri,neg(sqri)])}
 def mapm(m,x):
  a,b,c,d=m
  u,v=(a,c) if x==inf else (ad(mu(a,x),b),ad(mu(c,x),d))
  return inf if v==0 else mu(u,iv(v))
 mats=[]
 for m in product(range(q),repeat=4):
  a,b,c,d=m
  if ad(mu(a,d),neg(mu(b,c)))==0:continue
  first=next(x for x in m if x)
  if first!=1:continue
  if {mapm(m,x) for x in D}==D:mats.append(m)
 structured=[m for m in mats if {frozenset(mapm(m,x) for x in a) for a in opp}==opp]
 assert len(structured)==24
 assert len(mats)==(120 if p==5 else 24)
 row={'characteristic':p,'field_order':q,'bare_stabilizer':len(mats),'structured_stabilizer':len(structured)}
 if p==5:
  witness=(2,1,0,1)
  assert {mapm(witness,x) for x in D}==D
  assert mapm(witness,inf)==inf and mapm(witness,4)==4
  assert {frozenset(mapm(witness,x) for x in a) for a in opp}!=opp
  def pairings(xs):
   if not xs:yield frozenset();return
   a=min(xs)
   for b in xs-{a}:
    for rest in pairings(xs-{a,b}):yield rest|{frozenset([a,b])}
  partitions=set(pairings(D));assert len(partitions)==15
  counts=Counter(len([m for m in mats if frozenset(frozenset(mapm(m,x) for x in a) for a in pp)==pp]) for pp in partitions)
  assert counts=={24:5,12:10}
  row.update({'witness':'z -> 2 z + 1','witness_action':{str(x):mapm(witness,x) for x in sorted(D)},'oppositions_by_stabilizer_order':dict(counts)})
 results.append(row)
out={'cube_orbits':cube,'projective_stabilizers':results}
(OUT/'cube_and_pgl.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cube_orbits':[{k:v for k,v in x.items() if k!='stabilizer_on_body_diagonals'} for x in cube],'projective_stabilizers':results},indent=2))
