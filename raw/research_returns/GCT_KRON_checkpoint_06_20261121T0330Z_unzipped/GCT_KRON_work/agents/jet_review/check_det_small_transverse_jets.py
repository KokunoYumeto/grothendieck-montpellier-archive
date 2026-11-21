"""Small determinant coefficient-projection tests for the lifted LMR family."""
from pathlib import Path
from itertools import permutations,product
from random import Random
from datetime import datetime,timezone
import json
source=Path(__file__).with_name('check_per3_binary_transverse_jacobian.py');ns={'__file__':str(source)}
exec(source.read_text().split('r=7;p=1000003;')[0],ns)
echelon=ns['echelon']

def multiply_linear(poly,linear):
 r=len(linear);out={}
 for a,c in poly.items():
  for i,v in enumerate(linear):
   if not v:continue
   e=list(a);e[i]+=1;e=tuple(e)
   if sum(e[2:])<=2:out[e]=out.get(e,0)+c*v
 return {e:c for e,c in out.items() if c}
def cofactor(A,i,j):
 n=len(A);r=len(A[0][0]);rows=[a for a in range(n) if a!=i];cols=[a for a in range(n) if a!=j];out={}
 for perm in permutations(range(n-1)):
  sign=(-1)**(i+j+sum(perm[a]>perm[b] for a in range(n-1) for b in range(a+1,n-1)))
  term={(0,)*r:sign}
  for a,p in enumerate(perm):term=multiply_linear(term,A[rows[a]][cols[p]])
  for e,c in term.items():out[e]=out.get(e,0)+c
 return {e:c for e,c in out.items() if c}
def jac(A):
 n=len(A);r=len(A[0][0]);target=sorted(a for a in product(range(n+1),repeat=r) if sum(a)==n and sum(a[2:])<=2);pos={a:i for i,a in enumerate(target)}
 J=[[0]*(n*n*r) for a in target]
 for i in range(n):
  for j in range(n):
   cof=cofactor(A,i,j)
   for k in range(r):
    col=(n*i+j)*r+k
    for a,c in cof.items():
     e=list(a);e[k]+=1;e=tuple(e)
     if e in pos:J[pos[e]][col]=c
 return target,J

p=1000003;r=7;rng=Random(260526);records=[]
for n in [4,5]:
 best=None
 for trial in range(3):
  A=[[[rng.randint(-3,3) for k in range(r)] for j in range(n)] for i in range(n)]
  target,J=jac(A);rank,cols,det=echelon(J,p)
  rec={'n':n,'r':r,'trial':trial,'rank':rank,'target_dimension':len(target),'source_dimension':n*n*r,'pencil_coefficients':A,'target_monomials':target,'pivot_columns':cols,'selected_minor_mod_prime':det,'Jacobian':J}
  print(json.dumps({k:rec[k] for k in ['n','trial','rank','target_dimension']}),flush=True)
  if best is None or rank>best['rank']:best=rec
  if rank==len(target):break
 records.append(best)
result={'date_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed','run':'GCT_KRON_20261120','status':'FULL RANK' if all(r['rank']==r['target_dimension'] for r in records) else 'SOME DEFICIENCY','prime':p,'scope':'Tests of determinant degree-n coefficients with suffixdegree<=2 in7variables; no larger-n claim inferred from tests alone.','records':records}
out=Path(__file__).with_name('det_small_transverse_jet_certificate.json');out.write_text(json.dumps(result,indent=2)+'\n');print(str(out),flush=True)
