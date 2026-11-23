#!/usr/bin/env python3
"""HD-S35 exact rank-four root-normalizer certificate.
GPT-6 Astra Pro, /root/sixfolds, inherited effort not exposed, 2026-11-21.
Matrices are stored as twice their Gaussian integer entries, with integer pairs.
All finite closures and geometric counts are rebuilt from the displayed roots.
"""
from itertools import product,combinations
from math import gcd
from functools import reduce
from collections import deque,Counter
from pathlib import Path
import json
z=(0,0)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def norm(a):return a[0]*a[0]+a[1]*a[1]
Id=tuple((2 if i==j else 0,0) for i in range(4) for j in range(4))
def mm(A,B):
 out=[]
 for i in range(4):
  for j in range(4):
   s=z
   for k in range(4):s=add(s,mul(A[4*i+k],B[4*k+j]))
   assert s[0]%2==s[1]%2==0
   out.append((s[0]//2,s[1]//2))
 return tuple(out)
def star(A):return tuple(conj(A[4*j+i]) for i in range(4) for j in range(4))
def scale(c,A):return tuple(mul(c,x) for x in A)
def closure(gens,cap):
 elements=[Id];seen={Id}
 for A in elements:
  for B in gens:
   C=mm(A,B)
   if C not in seen:seen.add(C);elements.append(C)
  assert len(elements)<=cap
 return elements,seen
# Integer-scaled roots: the last root is twice its actual half-coordinate root.
simple=[(0,1,-1,0),(0,0,1,-1),(0,0,0,1),(1,-1,-1,-1)]
def reflection(v):
 q=sum(a*a for a in v)
 entries=[]
 for i in range(4):
  for j in range(4):
   numerator=2*q*int(i==j)-4*v[i]*v[j]
   assert numerator%q==0
   entries.append((numerator//q,0))
 return tuple(entries)
gens=[reflection(v) for v in simple]
assert all(mm(g,g)==Id and mm(star(g),g)==Id for g in gens)
W,Wset=closure(gens,1152)
assert len(W)==1152
minus=scale((-1,0),Id)
assert minus in Wset
M=((1,1,0,0),(1,-1,0,0),(0,0,1,1),(0,0,1,-1))
U=tuple((M[i][j],M[i][j]) for i in range(4) for j in range(4))
assert mm(U,U)==scale((0,1),Id)
assert mm(star(U),U)==Id
assert all(mm(mm(U,g),star(U)) in Wset for g in gens)
H,Hset=closure(gens+[U],4608)
assert len(H)==4608
assert all(mm(star(g),g)==Id for g in H)
assert all(mm(mm(U,g),star(U)) in Wset for g in W)
cosets=[{mm(P,g) for g in W} for P in (Id,U,mm(U,U),mm(mm(U,U),U))]
assert len(set.union(*cosets))==4608 and all(len(c)==1152 for c in cosets)
Dgens=[reflection(v) for v in [(1,-1,0,0),(0,1,-1,0),(0,0,1,-1),(0,0,1,1)]]
D,Dset=closure(Dgens,192)
assert len(D)==192 and Dset<=Wset and minus in Dset
assert all(mm(mm(w,d),star(w)) in Dset for w in W for d in Dgens)
# Root sets stored at integer scale two; dot products suffice for frames.
E=[tuple(int(i==j) for i in range(4)) for j in range(4)]
short={tuple(s*2*x for x in e) for e in E for s in (-1,1)}
short.update(product((-1,1),repeat=4))
long=set()
for i,j in combinations(range(4),2):
 for a,b in product((-2,2),repeat=2):
  v=[0]*4;v[i]=a;v[j]=b;long.add(tuple(v))
assert len(short)==len(long)==24
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def image_real(A,v):
 out=[]
 for i in range(4):
  s=sum(A[4*i+j][0]*v[j] for j in range(4))
  assert s%2==0
  out.append(s//2)
 return tuple(out)
assert all({image_real(g,v) for v in short}==short and {image_real(g,v) for v in long}==long for g in gens)
def frame_counts(roots):
 levels=[{()}]
 counts=[]
 for k in range(4):
  nextlevel=set();branch=[]
  for frame in levels[-1]:
   options=[v for v in roots if all(dot(v,w)==0 for w in frame)]
   branch.append(len(options))
   nextlevel.update(frame+(v,) for v in options)
  counts.append(sorted(set(branch)));levels.append(nextlevel)
 return counts,len(levels[-1])
sc,sf=frame_counts(short);lc,lf=frame_counts(long)
assert sc==lc==[[24],[6],[4],[2]] and sf==lf==1152
# Projective lines and exact squared-angle graph for normalized F4 roots.
def canonical(v):
 d=reduce(gcd,(abs(x) for x in v));v=tuple(x//d for x in v)
 return v if next(x for x in v if x)!=-abs(next(x for x in v if x)) else tuple(-x for x in v)
shortlines={canonical(v) for v in short};longlines={canonical(v) for v in long}
assert len(shortlines)==len(longlines)==12 and not shortlines&longlines
lines=sorted(shortlines|longlines)
adj={v:{w for w in lines if w!=v and 2*dot(v,w)**2==dot(v,v)*dot(w,w)} for v in lines}
seen={lines[0]};queue=[lines[0]]
for v in queue:
 for w in adj[v]:
  if w not in seen:seen.add(w);queue.append(w)
assert len(seen)==24 and set(map(len,adj.values()))=={6}
assert all((v in shortlines)!=(w in shortlines) for v in lines for w in adj[v])
# The real M/sqrt2 swaps normalized root classes, checked without radicals:
# short norm1 roots map under M to the unnormalized long roots; long roots
# map under M/2 to short roots (at the same integer scale two).
def mv(v):return tuple(sum(M[i][j]*v[j] for j in range(4)) for i in range(4))
assert {mv(v) for v in short}==long
assert all(all(x%2==0 for x in mv(v)) for v in long)
assert {tuple(x//2 for x in mv(v)) for v in long}==short
# G(4,4,4): 24 root lines; squared inner product two gives six four-cycles.
units=[(1,0),(0,1),(-1,0),(0,-1)]
roots44=[];supports=[]
for i,j in combinations(range(4),2):
 for u in units:
  v=[z]*4;v[i]=(1,0);v[j]=(-u[0],-u[1]);roots44.append(tuple(v));supports.append((i,j))
def inner(v,w):
 s=z
 for a,b in zip(v,w):s=add(s,mul(conj(a),b))
 return s
adj44={i:{j for j in range(24) if i!=j and norm(inner(roots44[i],roots44[j]))==2} for i in range(24)}
assert set(map(len,adj44.values()))=={2}
components=[];unseen=set(range(24))
while unseen:
 a=min(unseen);comp={a};todo=[a];unseen.remove(a)
 for v in todo:
  for w in adj44[v]:
   if w in unseen:unseen.remove(w);comp.add(w);todo.append(w)
 components.append(sorted(comp))
assert sorted(map(len,components))==[4]*6
planes=[set(supports[c[0]]) for c in components]
assert all(len({supports[v] for v in c})==1 for c in components)
triple_intersections=[set.intersection(*c) for c in combinations(planes,3)]
assert sorted(tuple(x) for x in triple_intersections if x)==[(0,),(1,),(2,),(3,)]
# A4 root-line graph: its unique four-cliques are the five stars of K5.
a4edges=list(combinations(range(5),2))
cliques=[c for c in combinations(a4edges,4) if all(set(a)&set(b) for a,b in combinations(c,2))]
assert len(cliques)==5
assert all(len(set.intersection(*(set(e) for e in c)))==1 for c in cliques)
out={'statement':'HD-S35','status':'PASS','date':'2026-11-21',
'F4_order':len(W),'D4_order':len(D),'Gaussian_F4_normalizer_order':len(H),
'U_square':'i I4','normalizer_entries':'(1/2) Z[i]',
'D4_normalized_by_F4':True,'short_and_long_frame_branch_counts':sc,
'frame_count':sf,'F4_line_graph':{'vertices':24,'degree':6,'connected':True,'parts':[12,12]},
'F4_duality_exact_root_maps':True,'G444_angle_graph_component_sizes':list(map(len,components)),
'coordinate_lines_recovered_by_triple_intersections':True,'A4_four_cliques':len(cliques),
'scope':'Exact finite root and normalizer geometry. Universal reflection reduction, integral parabolic duality and primitive Jacobian map are proved in the accompanying TeX.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
