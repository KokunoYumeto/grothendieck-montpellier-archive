#!/usr/bin/env python3
"""Bounded searches for the two degree-three tangent-triple collision types.

Rational-point screens only reject candidates; global algebraic-closure
certificates are required separately. All coefficients are in the monomial basis.
"""
from pathlib import Path
import sys,json,random,itertools,time
base=Path(__file__).resolve().parents[1];root=base.parents[1]
sys.path.insert(0,str(root/'code'))
import ss_contact_witness as ff
started=time.perf_counter()
kind=sys.argv[1] if len(sys.argv)>1 else 'collinear'
assert kind in ('collinear','noncollinear')
seed=202611191140+(kind=='noncollinear');rng=random.Random(seed)
reference=json.loads((root/'outputs/ss_contact_witness_03.json').read_text())
def point(p):return None if p is None else tuple(p)
G=tuple(point(p) for p in reference['G']);H=tuple(point(p) for p in reference['H'])
K=[tuple(point(p) for p in g) for g in reference['kernel']]
third=tuple(ff.neg(p) for p in G) if kind=='collinear' else H
mul=[[ff.mul(a,b) for b in range(64)] for a in range(64)]
def dot(a,b):
 out=0
 for x,y in zip(a,b):out^=mul[x][y]
 return out
points=[(x,y) for x in range(64) for y in range(64) if mul[y][y]^y==mul[mul[x][x]][x]]+[None]
assert len(points)==81
idx={P:i for i,P in enumerate(points)}
values=[[0,0,1] if p is None else [1,*p] for p in points]
derivatives=[[0,1,0] if p is None else [0,1,mul[p[0]][p[0]]] for p in points]
def tensor(a,b):return [mul[x][y] for x in a for y in b]
rows=[tensor(a,b) for a in values for b in values]
drows0=[tensor(a,b) for a in derivatives for b in values]
drows1=[tensor(a,b) for a in values for b in derivatives]
point_pairs=[(P,Q) for P in points for Q in points]
translations={g:[idx[ff.add(P,g[0])]*81+idx[ff.add(Q,g[1])] for P,Q in point_pairs] for g in K}
remaining=set(range(81**2));orbits=[];orbit_of={}
while remaining:
 representative=min(remaining)
 orbit=tuple(sorted(translations[g][representative] for g in K))
 assert len(set(orbit))==9
 remaining.difference_update(orbit)
 no=len(orbits);orbits.append(orbit)
 for i in orbit:orbit_of[i]=no
assert len(orbits)==729
choices=[P for P in points if P is not None and ff.scalar(3,P) is not None]
rejections={};records=[];found=None
for base_attempt in range(1,101):
 P=(rng.choice(choices),rng.choice(choices));pindex=idx[P[0]]*81+idx[P[1]]
 qindex=translations[G][pindex];rindex=translations[third][pindex]
 Q=point_pairs[qindex];R=point_pairs[rindex]
 c=rng.randrange(1,64)
 equations=[rows[pindex],rows[qindex],rows[rindex]]
 for jets in (drows0,drows1):equations.append([a^mul[c][b] for a,b in zip(jets[qindex],jets[pindex])])
 N=ff.nullspace(equations,9)
 for trial in range(1,1001):
  co=[rng.randrange(64) for _ in N]
  s=[dot(co,[v[j] for v in N]) for j in range(9)]
  D=ff.determinant3(s);Qhasse=ff.hasse_cubic(s)
  if not D or not Qhasse:continue
  grad=[dot(s,drows0[pindex]),dot(s,drows1[pindex])]
  gradQ=[dot(s,drows0[qindex]),dot(s,drows1[qindex])]
  gradR=[dot(s,drows0[rindex]),dot(s,drows1[rindex])]
  assert gradQ==[mul[c][v] for v in grad]
  cross=mul[grad[0]][gradR[1]]^mul[grad[1]][gradR[0]]
  if not cross:continue
  velocity=[grad[1],grad[0]]
  second=ff.second_coefficient(s,Q,velocity)^mul[c][ff.second_coefficient(s,P,velocity)]
  second^=dot(gradQ,[mul[ff.translation_second(P[i],G[i])][mul[velocity[i]][velocity[i]]] for i in range(2)])
  if not second:continue
  expected={pindex,qindex,rindex};expected_orbit=orbit_of[pindex]
  zero={i for i,row in enumerate(rows) if dot(s,row)==0}
  reason=None
  for number,orbit in enumerate(orbits):
   hits=zero.intersection(orbit)
   if number==expected_orbit:
    if hits!=expected:reason='extra point in expected triple orbit';break
   elif len(hits)>=3:reason='additional rational triple orbit';break
  if reason is None:
   gradients={i:(dot(s,drows0[i]),dot(s,drows1[i])) for i in zero}
   for i in zero:
    a,b=gradients[i]
    if not (a or b):reason='rational source singularity';break
    for g in K:
     j=translations[g][i]
     if j==i or j not in zero:continue
     u,v=gradients[j]
     if not (mul[a][v]^mul[b][u]) and {i,j}!={pindex,qindex}:
      reason='additional rational tangent pair';break
    if reason:break
  rec={'base_attempt':base_attempt,'attempt':trial,'P':P,'Q':Q,'R':R,
       'coefficients':s,'determinant':D,'Hasse_cubic_value':Qhasse,
       'gradient':grad,'gradient_Q':gradQ,'gradient_R':gradR,
       'gradient_ratio':c,'transverse_third_determinant':cross,
       'tacnode_second_difference':second,'rational_rejection':reason}
  if len(records)<100:records.append(rec)
  if reason:
   rejections[reason]=rejections.get(reason,0)+1;continue
  found=rec;break
 if found:break
result={'status':'CANDIDATE_FOUND' if found else 'BUDGET_EXHAUSTED',
 'type':kind,'field_modulus_binary':67,'omega':reference['omega'],'G':G,'H':H,'kernel':K,
 'third_translation':third,'seed':seed,'budget':'100 base pairs,1000 sections each',
 'basis':'(1,x,y) tensor (1,x,y), index3*i+j',
 'rational_orbits':len(orbits),'rejection_counts':rejections,'first_local_candidates':records,
 'candidate':found,'global_smoothness_checked':False,'global_collisions_checked':False,
 'elapsed_seconds':time.perf_counter()-started}
out=base/'outputs'/f'ss_tangent_triple_{kind}.json';out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('first_local_candidates','kernel')},indent=2))
