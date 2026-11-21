#!/usr/bin/env python3
"""Marked C3*C3 genus-zero quotient of the affine216 dessin; DELTA23."""
import importlib.util,pathlib,contextlib,io,json
from sympy.combinatorics import Permutation,PermutationGroup
p=pathlib.Path('work/agents/pentagon/affine_cubic_detector.py');sp=importlib.util.spec_from_file_location('cub',p);c=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()):sp.loader.exec_module(c)
def shifted_real(a):
 assert all(j<3 for j in a[2:])
 m=a[2:];t=(0,2)
 return ((a[0]%3-((t[0]-m[0]*t[0]-m[1]*t[1])%3))%3,(a[1]%3-((t[1]-m[2]*t[0]-m[3]*t[1])%3))%3)+m
def perm(a):return tuple(3*((a[0]+a[2]*(v//3)+a[3]*(v%3))%3)+(a[1]+a[4]*(v//3)+a[5]*(v%3))%3 for v in range(9))
u=shifted_real(c.r);v=shifted_real(c.am(c.am(c.s,c.r),c.s));x=shifted_real(c.x);y=shifted_real(c.y)
up,vp,xp,yp=map(perm,[u,v,x,y]);inv=lambda p:tuple(p.index(j) for j in range(len(p)))
assert all(xp[vp[up[j]]]==j for j in range(9))
def ct(p):return sorted([len(a) for a in Permutation(p).cyclic_form]+[1]*(len(p)-sum(len(a) for a in Permutation(p).cyclic_form)),reverse=True)
assert ct(up)==[3,3,3] and ct(vp)==[3,3,1,1,1] and ct(xp)==[6,2,1]
assert PermutationGroup([Permutation(up),Permutation(vp)]).order()==216
# Database distinguished triple (zero,one,infinity), converted from Magma 1-based arrays.
db=[tuple(j-1 for j in p) for p in [[7,6,4,3,5,9,2,1,8],[1,8,6,4,2,9,7,5,3],[2,7,4,9,8,5,1,6,3]]]
def simultaneous(A,B):
 for start in range(9):
  mp={0:start};todo=[0];ok=True
  for a in todo:
   for p,q in zip(A,B):
    b=p[a];bb=q[mp[a]]
    if b in mp:
     if mp[b]!=bb:ok=False;break
    else:mp[b]=bb;todo.append(b)
   if not ok:break
  if ok and len(mp)==9 and len(set(mp.values()))==9:return [mp[j] for j in range(9)]
 return None
matches=[]
for invboth in [False,True]:
 # Database right permutation convention may invert every oriented branch loop.
 aa=[xp,vp] if not invboth else [inv(xp),inv(vp)]
 cc=simultaneous(aa,db[:2])
 if cc is not None:matches.append({'inverse_both':invboth,'conjugator':cc})
assert matches
out={'statement':'D23.C14','Gamma_plus':'<r,srs> = C3*C3','u_r':u,'v_srs':v,'x':x,'y':y,'u_permutation':up,'v_permutation':vp,'x_permutation':xp,'cycle_types':[ct(xp),ct(vp),ct(up)],'database_matches':matches,'genus_quotient':0,'order3_orbifold_points':3,'cusps':3,'cyclic_degree_E_over_quotient':3,'genus_E':1,'result':'PASS'}
pathlib.Path('work/agents/characters/records/cubic_orbifold_topology.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
