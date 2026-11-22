#!/usr/bin/env python3
"""Exact GF(2)[z] search for an isotropic pencil at alpha=(1,1,1,1).
All polynomial operations are retained here; no field sampling is used.
"""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
from itertools import combinations
import json,time
start=time.perf_counter()
def mul(a,b):
 r=0
 while b:
  if b&1:r^=a
  a<<=1;b>>=1
 return r
def show(a):return '+'.join('1' if i==0 else 'z' if i==1 else f'z^{i}' for i in range(a.bit_length()) if (a>>i)&1) or '0'
pts=[(x,y) for x in range(3) for y in range(3)]
count=0;found=None
supports=[u for wt in (4,6,8,2) for u in combinations(range(9),wt)]
for ui in supports:
 for vi in supports:
  if len(set(ui)&set(vi))%2:continue
  pivot=next((i for i in ui if i not in vi),None)
  if pivot is None:continue
  u=[int(i in ui) for i in range(9)];v=[int(i in vi) for i in range(9)];s=[u[i]+2*v[i] for i in range(9)]
  M=[[0]*9 for _ in range(9)]
  for i,p in enumerate(pts):
   for j,q in enumerate(pts):
    if i==j:continue
    k=pts.index(((-p[0]-q[0])%3,(-p[1]-q[1])%3));M[i][j]=s[k]
  @lru_cache(None)
  def pf(ids):
   if not ids:return 1
   out=0;i=ids[0]
   for j in ids[1:]:out^=mul(M[i][j],pf(tuple(k for k in ids[1:] if k!=j)))
   return out
  ids=tuple(i for i in range(9) if i!=pivot);p8=pf(ids);count+=1
  if not p8:continue
  numerator=0
  for i in ids:
   for j in ids:
    if i!=j and u[i] and v[j]:numerator^=pf(tuple(k for k in ids if k not in (i,j)))
  if numerator:
   found={'u_support':ui,'v_support':vi,'pivot':pivot,'s':[show(x) for x in s],'pf8':show(p8),'inverse_pairing_numerator':show(numerator),'stable_loss_pairing':'(z^4+z)*(numerator/pf8)^2','raw_pf8':p8,'raw_numerator':numerator}
   break
 if found:break
assert found
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,'status':'PASS','examined_pencils':count,'witness':found,'scope':'Exact one-parameter witness at equal theta coefficients; global reduction and monodromy require a separate proof.'}
(Path(__file__).resolve().parents[1]/'outputs/ppav_theta_equal_cubes_pencil.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
