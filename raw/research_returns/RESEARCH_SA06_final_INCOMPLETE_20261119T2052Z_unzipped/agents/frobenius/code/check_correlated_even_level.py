#!/usr/bin/env python3
"""Test a necessary mod-4 graph congruence at level 2 modulo 4.

The vertex group is C/(2 L(U)+4C), so the full profile-divisibility
condition is retained. No geometric conclusion is inferred from this test.
"""
from itertools import product
from datetime import datetime,timezone
from time import perf_counter
from pathlib import Path
import json

start=perf_counter()
L=[(1,0,1,0),(1,0,0,0),(0,1,0,1),(0,0,0,1),(2,1,1,1),(0,0,1,1)]
R=[(-1,-1),(-1,1),(-1,0),(0,-1),(1,0),(0,1)]
# Coordinates c -> (u1,u2,u3,u4,Rc), with u=(c2,c3-c4,c1-c2,c4).
H=[(0,0,1,0),(1,0,-1,0),(0,1,0,0),(0,-1,0,1),(0,0,0,0),(0,0,0,0)]
verts=list(product(range(2),range(2),range(2),range(2),range(4),range(4)))
vid={v:i for i,v in enumerate(verts)}
edges=[]
for s in range(3):
  for u in verts:
    for a,b in product(range(4),repeat=2):
      if a==b==0: continue
      step=tuple(a*H[2*s][i]+b*H[2*s+1][i] for i in range(4)) + tuple(a*R[2*s][i]+b*R[2*s+1][i] for i in range(2))
      v=tuple((u[i]+step[i])%(2 if i<4 else 4) for i in range(6))
      rev=((-a)%4,(-b)%4)
      if (u,(a,b))>(v,rev):continue
      edges.append((s,u,v,a,b))
nrows=4*len(verts)+9; ncols=len(edges)
low=[0]*nrows;high=[0]*nrows
def entry(i,j,a):
  a%=4
  if a&1:low[i]|=1<<j
  if a&2:high[i]|=1<<j
for j,(s,u,v,a,b) in enumerate(edges):
  q=[(a*L[2*s][i]+b*L[2*s+1][i])%4 for i in range(4)]
  if u!=v:
    for i in range(4):
      entry(4*vid[u]+i,j,-q[i]);entry(4*vid[v]+i,j,q[i])
  base=4*len(verts)+3*s
  for i,x in enumerate((a*a,a*b,b*b)):entry(base+i,j,x)
for s in range(3):
  entry(4*len(verts)+3*s,ncols,2)
  entry(4*len(verts)+3*s+2,ncols,2)
mask=(1<<ncols)-1
rows=list(zip(low,high));rank=0
# Unit-pivot row reduction in Z/4, using exact two-bit-plane arithmetic.
while rank<len(rows):
  pick=next((j for j in range(rank,len(rows)) if rows[j][0]&mask),None)
  if pick is None:break
  rows[rank],rows[pick]=rows[pick],rows[rank]
  pl,ph=rows[rank];bit=(pl&mask)&-(pl&mask)
  if ph&bit:ph^=pl
  rows[rank]=(pl,ph)
  for j in range(rank+1,len(rows)):
    lo,hi=rows[j];a=(1 if lo&bit else 0)+(2 if hi&bit else 0)
    if a==1:rows[j]=(lo^pl,hi^ph^pl^(lo&pl))
    elif a==2:rows[j]=(lo,hi^pl)
    elif a==3:rows[j]=(lo^pl,hi^ph^(lo&pl))
  rank+=1
feasible=True;cause=None
for lo,hi in rows[rank:]:
  assert not lo&mask
  if lo>>ncols:
    feasible=False;cause='odd right-hand side after unit elimination';break
rank2=0
if feasible:
  gfrows=[hi for lo,hi in rows[rank:]]
  piv={}
  for z in gfrows:
    while z&mask:
      bit=(z&mask)&-(z&mask)
      if bit not in piv:piv[bit]=z;rank2+=1;break
      z^=piv[bit]
    else:
      if z>>ncols:feasible=False;cause='inconsistent divided residual mod2';break
out={'started_utc':datetime.now(timezone.utc).isoformat(),
     'scope':'Necessary congruences only, no sufficiency or geometric claim',
     'modulus':4,'level_modulus':2,'vertices':len(verts),'edges':ncols,
     'equations':nrows,'unit_rank':rank,'residual_mod2_rank':rank2,
     'congruences_feasible':feasible,'infeasibility_reason':cause,
     'runtime_seconds':perf_counter()-start}
p=Path(__file__).resolve().parents[1]/'output'/'check_correlated_even_level.json'
p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
