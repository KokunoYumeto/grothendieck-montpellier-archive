#!/usr/bin/env python3
"""Exact symbolic Lie-stabilizer test for polar Coble tensor of
RS17 gamma with c9=1,c12=a,c24=b and remaining coefficients0.
All arithmetic in F2[a,b,c]; unit-pivot certificate, not sampling.
"""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
import itertools,json,time
start=time.perf_counter();P=Path(__file__).resolve().parents[1]
def add(*ps):
 z=set()
 for p in ps:z.symmetric_difference_update(p)
 return frozenset(z)
def mul(p,q):
 z=set()
 for a in p:
  for b in q:
   c=tuple(x+y for x,y in zip(a,b))
   if c in z:z.remove(c)
   else:z.add(c)
 return frozenset(z)
def var(i,n):
 z=[0]*n;z[i]=1;return frozenset({tuple(z)})
zero=frozenset();one12=frozenset({(0,)*12});one=frozenset({(0,)*3})
T={tuple(int(i)-1 for i in t):one12 for t in ['267','258','348','169','357','249','178','456','148']}
for j,t in enumerate(['147','134']):T[tuple(int(i)-1 for i in t)]=var(9+j,12)
M=[[zero]*9 for _ in range(9)]
for (a,b,c),v in T.items():
 for i,j,k in [(a,b,c),(a,c,b),(b,c,a)]:M[i][j]=M[j][i]=add(M[i][j],mul(v,var(k,12)))
@lru_cache(None)
def pf(I):
 if not I:return one12
 i=I[0];return add(*(mul(M[i][j],pf(tuple(k for k in I[1:] if k!=j))) for j in I[1:]))
qs=[]
for i in range(9):
 q=set()
 for e in pf(tuple(j for j in range(9) if j!=i)):
  assert e[i];ee=list(e);ee[i]-=1;q.add(tuple(ee))
 qs.append(frozenset(q))
assert all(q==qs[0] for q in qs)
B={}
for m in qs[0]:
 if max(m[:9])!=1:continue
 t=tuple(i for i,e in enumerate(m[:9]) if e)
 assert len(t)==3
 B[t]=add(B.get(t,zero),frozenset({m[9:]}))
trips=list(itertools.combinations(range(9),3));ix={t:i for i,t in enumerate(trips)}
A=[[zero]*81 for _ in range(85)]
for a in range(9):
 for b in range(9):
  col=9*a+b
  for t,v in B.items():
   if b not in t:continue
   tt=[a if c==b else c for c in t]
   if len(set(tt))<3:continue
   row=ix[tuple(sorted(tt))];A[row][col]=add(A[row][col],v)
  if a==b:A[84][col]=one
rows=list(range(85));cols=list(range(81));piv=[]
while cols:
 found=next(((r,c) for r in rows for c in cols if A[r][c]==one),None)
 if found is None:break
 r,c=found;piv.append([r,c]);rows.remove(r);cols.remove(c)
 for rr in rows:
  a=A[rr][c]
  if a:
   for cc in cols:A[rr][cc]=add(A[rr][cc],mul(a,A[r][cc]))
   A[rr][c]=zero
# Exact determinant of one remaining4-by4 minor; no field sampling.
def det4(rr):
 return add(*(mul(mul(A[rr[0]][cols[p[0]]],A[rr[1]][cols[p[1]]]),mul(A[rr[2]][cols[p[2]]],A[rr[3]][cols[p[3]]])) for p in itertools.permutations(range(4))))
assert len(piv)==77 and len(cols)==4
b4=frozenset({(0,4,0)})
selected=next(rr for rr in itertools.combinations(rows,4) if det4(rr)==b4)
assert det4(selected)==b4
used=[r for r,c in piv]+list(selected)
assert len(set(used))==81 and 84 not in used
unused=[r for r in range(84) if r not in used]
out={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'parameters':'c9=1,c12=a,c24=b; c3=c6=c15=c18=c30=0','pfaffian_all_nine_identity':True,'cubic_monomials':len(qs[0]),'polar_terms':[[list(t),[list(e) for e in sorted(v)]] for t,v in sorted(B.items())],'unit_pivot_count':len(piv),'unit_pivots':piv,'remaining_rows':rows,'remaining_columns':cols,'remaining_matrix':[[[list(e) for e in sorted(A[r][c])] for c in cols] for r in rows],'selected_residual_rows':selected,'residual_minor':'b^4','deleted_original_rows':unused,'deleted_original_triples':[[i+1 for i in trips[r]] for r in unused],'full_81_minor':'b^4','scope':'Exact identity overF2[a,b], hence zero GL9 Lie stabilizer for every b!=0. The third polynomial variable is unused. Geometric normal-form/Coble transfer is a separate proof.'}
(P/'outputs/ppav_two_rank_one_polar_uniform_minor.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['unit_pivots','polar_terms','remaining_matrix']},indent=2))
