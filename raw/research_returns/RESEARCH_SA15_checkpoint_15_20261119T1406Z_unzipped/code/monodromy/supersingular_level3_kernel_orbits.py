#!/usr/bin/env python3
"""Exact finite kernel/orbit certificate; no contact-existence inference."""
from pathlib import Path
from itertools import combinations
from time import perf_counter
import json

started=perf_counter()
def mul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return c
def inv(a):
    assert a
    return mul(a,a)
def div(a,b):return mul(a,inv(b))
def sq(a):return mul(a,a)
O=None
E=[O]+[(x,y) for x in range(4) for y in range(4) if sq(y)^y==mul(sq(x),x)]
assert len(E)==9
index={P:i for i,P in enumerate(E)}
def neg(P):return O if P is O else (P[0],P[1]^1)
def add(P,Q):
    if P is O:return Q
    if Q is O:return P
    x,y=P;u,v=Q
    if x==u:
        if y!=v:return O
        slope=sq(x)
    else:slope=div(y^v,x^u)
    intercept=y^mul(slope,x)
    z=sq(slope)^x^u
    return (z,mul(slope,z)^intercept^1)
for P in E:
    assert add(P,neg(P)) is O
    assert add(add(P,P),P) is O
for P in E:
 for Q in E:
  for R in E:
   assert add(add(P,Q),R)==add(P,add(Q,R))
w=2
def aut_i(P):return O if P is O else (P[0]^1,P[1]^P[0]^w)
def aut_j(P):return O if P is O else (P[0]^w,P[1]^mul(sq(w),P[0])^w)
def aut_z(P):return O if P is O else (mul(w,P[0]),P[1])
gens=[tuple(index[f(P)] for P in E) for f in (aut_i,aut_j,aut_z)]
identity=tuple(range(9))
def compose(a,b):return tuple(a[b[i]] for i in range(9))
group={identity};queue=[identity]
while queue:
 a=queue.pop()
 for b in gens:
  c=compose(a,b)
  if c not in group:group.add(c);queue.append(c)
assert len(group)==24
for a in group:
 for P in E:
  for Q in E:
   assert a[index[add(P,Q)]]==index[add(E[a[index[P]]],E[a[index[Q]]])]
b=lambda P:add(P,aut_i(P))
graph_map=tuple(index[neg(b(P))] for P in E)
assert len(set(graph_map))==9
inverse_graph=tuple(graph_map.index(i) for i in range(9))
for a in group:
 assert compose(compose(graph_map,a),inverse_graph) in group
K=[(E[graph_map[i]],P) for i,P in enumerate(E)]
assert all(P is not O and Q is not O for P,Q in K[1:])
p0=(0,0);p1=(1,w)
G=K[index[p0]];H=K[index[p1]]
assert G==((w,sq(w)),(0,0))
assert H==((sq(w),sq(w)),(1,w))
nonzero_orbit={a[index[p0]] for a in group}
assert nonzero_orbit==set(range(1,9))
# Affine special linear action on K, parametrized by the second coordinate.
affine=[]
for a in group:
 for T in E:
  affine.append(tuple(index[add(E[a[i]],T)] for i in range(9)))
assert len(set(affine))==216
remaining=set(combinations(range(9),3));orbits=[]
while remaining:
 base=min(remaining)
 orbit={tuple(sorted(a[i] for i in base)) for a in affine}
 assert orbit<=remaining
 remaining-=orbit
 is_collinear=all(add(add(E[t[0]],E[t[1]]),E[t[2]]) is O for t in orbit)
 orbits.append({'size':len(orbit),'collinear':is_collinear,'representative':base})
assert sorted((o['size'],o['collinear']) for o in orbits)==[(12,True),(72,False)]
result={'status':'PASS','scope':'Finite E[3], graph kernel and affine orbit identities only; contact existence and Hasse irreducibility remain unproved.',
 'field':'F2[w]/(w^2+w+1), encoding 0,1,w,w+1 as0,1,2,3',
 'elliptic_points':E,'automorphism_group_order':len(group),'affine_group_order':len(set(affine)),
 'kernel_points':K,'G':G,'H':H,'triple_orbits':orbits,
 'elapsed_seconds':perf_counter()-started}
out=Path(__file__).resolve().parent.parent/'outputs'/'supersingular_level3_kernel_orbits.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
