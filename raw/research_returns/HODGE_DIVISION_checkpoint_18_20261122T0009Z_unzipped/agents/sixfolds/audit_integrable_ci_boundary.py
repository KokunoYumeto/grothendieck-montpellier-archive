#!/usr/bin/env python3
"""Independent Fraction and squarefree-monomial check of the root CI boundary."""
from fractions import Fraction as Q
from itertools import combinations,permutations
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
start=time.perf_counter()
u=[Q(1),Q(0),-Q(3,5),-Q(8,5)];v=[Q(0),Q(1),Q(1),Q(1)]
u2=[Q(1),Q(0),-Q(9,5),-Q(16,5)];v2=[Q(0),Q(1),Q(2),Q(3)]
cols=[u,v,u2,v2]
T=[[cols[j][i] for j in range(4)] for i in range(4)]
pairs=list(combinations(range(4),2))
p={ij:u[ij[0]]*v[ij[1]]-u[ij[1]]*v[ij[0]] for ij in pairs}
q={ij:u2[ij[0]]*v2[ij[1]]-u2[ij[1]]*v2[ij[0]] for ij in pairs}
def sign(perm):return (-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
def product(xs):
 r=Q(1)
 for x in xs:r*=x
 return r
det=sum(sign(s)*product(T[i][s[i]] for i in range(4)) for s in permutations(range(4)))
assert det==-Q(4,5)
def wedge(a,b):
 return sum(sign(i+j)*a[i]*b[j] for i in pairs for j in pairs if set(i).isdisjoint(j))
assert wedge(p,p)==wedge(q,q)==0
assert wedge(p,q)==det
# Reduction in A is bit-mask multiplication; repeated coordinates vanish.
P={ij:{(1<<ij[0])|(1<<ij[1]):4*p[ij]} for ij in pairs}
R={ij:{(1<<ij[0])|(1<<ij[1]):4*q[ij]} for ij in pairs}
def mul(a,b):
 out={}
 for i,c in a.items():
  for j,d in b.items():
   if not i&j:out[i|j]=out.get(i|j,Q(0))+c*d
 return {i:c for i,c in out.items() if c}
def sub(a,b):
 out=dict(a)
 for i,c in b.items():out[i]=out.get(i,Q(0))-c
 return {i:c for i,c in out.items() if c}
for i in pairs:
 for j in pairs:assert not sub(mul(P[i],R[j]),mul(R[i],P[j]))
soc={15:16*det}
assert soc[15]==-Q(64,5)
assert all(not mul(soc,{1<<i:Q(1)}) for i in range(4))
# Ordinary-polynomial differentiation independently checks actual f_i=ell_i^2.
def padd(a,b):
 r=dict(a)
 for mon,c in b.items():r[mon]=r.get(mon,Q(0))+c
 return {m:c for m,c in r.items() if c}
def pmul(a,b):
 r={}
 for m,c in a.items():
  for n,d in b.items():
   k=tuple(i+j for i,j in zip(m,n));r[k]=r.get(k,Q(0))+c*d
 return {m:c for m,c in r.items() if c}
def deriv(a,i):
 r={}
 for m,c in a.items():
  if m[i]:
   n=list(m);n[i]-=1;r[tuple(n)]=c*m[i]
 return r
ell=[]
for row in T:
 ell.append({tuple(int(j==i) for j in range(4)):row[i] for i in range(4) if row[i]})
for i in range(4):
 fi=pmul(ell[i],ell[i])
 for j in range(4):assert deriv(fi,j)=={m:2*T[i][j]*c for m,c in ell[i].items() if 2*T[i][j]*c}
out={'status':'PASS','finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,'method':'Independent fractions, 24-term determinant, squarefree masks and ordinary-polynomial differentiation; no author/root code imported','ordered_cross_minors':36,'actual_gradient_entries':16,'determinant':str(det),'socle_coefficient':str(soc[15]),'scope':'Boundary to scalar cross-minor inference only; no module deformation or balanced seed','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
