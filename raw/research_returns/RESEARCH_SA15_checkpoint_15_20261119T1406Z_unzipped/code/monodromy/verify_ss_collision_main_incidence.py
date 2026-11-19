#!/usr/bin/env python3
"""Exact main-incidence check for the three already audited global witnesses."""
from pathlib import Path
from time import perf_counter
import json
started=perf_counter()
MOD=0x43
def mul(a,b):
 z=0
 while b:
  if b&1:z^=a
  b>>=1;a<<=1
  if a&64:a^=MOD
 return z
def power(a,n):
 r=1
 while n:
  if n&1:r=mul(r,a)
  a=mul(a,a);n>>=1
 return r
def rows_at(P):
 A=[1,*P[0]];B=[1,*P[1]]
 DA=[0,1,mul(P[0][0],P[0][0])]
 DB=[0,1,mul(P[1][0],P[1][0])]
 return [[mul(a,b) for a in AA for b in BB] for AA,BB in ((A,B),(DA,B),(A,DB))]
def row_reduce(M):
 A=[list(row) for row in M];pivots=[];r=0
 for c in range(len(A[0])):
  p=next((i for i in range(r,len(A)) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];inv=power(A[r][c],62)
  A[r]=[mul(inv,x) for x in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][c]:
    v=A[i][c];A[i]=[x^mul(v,y) for x,y in zip(A[i],A[r])]
  pivots.append(c);r+=1
  if r==len(A):break
 return r,pivots,A
examples=[
 ('contact03',((17,52),(8,53)),((18,35),(19,10))),
 ('tangent_triple_collinear',((24,23),(56,26)),((51,23),(23,34))),
 ('tangent_triple_noncollinear',((3,44),(14,44)),((18,34),(50,30)))
]
results=[]
for name,P,Q in examples:
 rows=rows_at(P)+rows_at(Q)
 rank,pivots,reduced=row_reduce(rows)
 assert rank==6
 results.append({'name':name,'P':P,'Q':Q,'six_jet_rows':rows,'rank':rank,'pivot_columns':pivots,'reduced_rows':reduced})
out={'status':'PASS','scope':'All three retained global witnesses lie in the main full-six-jet pair incidence; no additional global geometry inferred.','field_modulus':MOD,'checks':results,'elapsed_seconds':perf_counter()-started}
p=Path(__file__).resolve().parent.parent/'outputs'/'verify_ss_collision_main_incidence.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
