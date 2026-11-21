"""Exact modular Jacobian certificate for per3 cubic suffix-order2 projection."""
from itertools import product
from random import Random
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

def monomials(r,n):return sorted((a for a in product(range(n+1),repeat=r) if sum(a)==n))
def quadratic(a,b):
 r=len(a);q={}
 for i in range(r):
  for j in range(r):
   e=[0]*r;e[i]+=1;e[j]+=1;e=tuple(e)
   q[e]=q.get(e,0)+a[i]*b[j]
 return q

def jacobian(A,r):
 target=[e for e in monomials(r,3) if sum(e[2:])<=2];pos={e:i for i,e in enumerate(target)}
 J=[[0]*(9*r) for _ in target]
 for i in range(3):
  for j in range(3):
   rows=[a for a in range(3) if a!=i];cols=[a for a in range(3) if a!=j]
   q1=quadratic(A[rows[0]][cols[0]],A[rows[1]][cols[1]])
   q2=quadratic(A[rows[0]][cols[1]],A[rows[1]][cols[0]])
   cofactor={e:q1.get(e,0)+q2.get(e,0) for e in set(q1)|set(q2)}
   for k in range(r):
    col=(3*i+j)*r+k
    for e,c in cofactor.items():
     f=list(e);f[k]+=1;f=tuple(f)
     if f in pos:J[pos[f]][col]+=c
 return target,J

def echelon(J,p):
 M=[[v%p for v in row] for row in J];rank=0;pivots=[];det=1;row_swaps=0
 for col in range(len(M[0])):
  row=next((i for i in range(rank,len(M)) if M[i][col]),None)
  if row is None:continue
  if row!=rank:M[rank],M[row]=M[row],M[rank];row_swaps+=1
  pivot=M[rank][col];det=det*pivot%p;inv=pow(pivot,-1,p)
  M[rank]=[(v*inv)%p for v in M[rank]]
  for i in range(rank+1,len(M)):
   if M[i][col]:
    c=M[i][col];M[i]=[(a-c*b)%p for a,b in zip(M[i],M[rank])]
  pivots.append(col);rank+=1
  if rank==len(M):break
 return rank,pivots,det*((-1)**row_swaps)%p

r=7;p=1000003;rng=Random(240526);trials=[];best=None
for trial in range(5):
 A=[[[rng.randint(-4,4) for k in range(r)] for j in range(3)] for i in range(3)]
 target,J=jacobian(A,r);rank,pivots,det=echelon(J,p)
 print(json.dumps({'trial':trial,'rank':rank,'target_dimension':len(target)}),flush=True)
 trials.append({'trial':trial,'rank':rank})
 if best is None or rank>best['rank']:best={'trial':trial,'rank':rank,'pencil_coefficients':A,'target_monomials':target,'pivot_columns':pivots,'selected_minor_mod_prime':det,'Jacobian':J}
 if rank==len(target):break
result={'date_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed','run':'GCT_KRON_20261120','method':'Coefficient Jacobian of the actual3x3 permanent map at an integer pencil in7variables; output all cubic monomials with suffixdegree<=2 in variables3..7; sourceall63linearentrycoefficients. Modular Gaussian elimination produces a squareminor witness.','prime':p,'trials':trials,'best':best,'status':'FULL RANK' if best['rank']==len(target) else 'RANK DEFICIENT'}
pth=Path(__file__).with_name('per3_binary_transverse_jacobian_certificate.json');pth.write_text(json.dumps(result,indent=2)+'\n');print(str(pth),flush=True)
