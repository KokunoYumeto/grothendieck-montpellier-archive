from pathlib import Path
from itertools import product
from fractions import Fraction
import json,math,cmath
import mpmath as mp
p=Path(__file__).resolve().parent
r=json.loads((p/'dyadic_n4_classification.json').read_text())['records'][3]
weights=[list(a) for a in r['spectra']]
S=[tuple(weights[j].index(e[j]) for j in range(3)) for e in r['aggregate_support']]
masses=[Fraction(x) for x in r['aggregate_positive_masses']]

def solve2(rows,rhs,k):
 mat=[sum((v%2)<<i for i,v in enumerate(row)) | ((b%2)<<k) for row,b in zip(rows,rhs)]
 piv=[];rr=0
 for c in range(k):
  z=next((i for i in range(rr,len(mat)) if (mat[i]>>c)&1),None)
  if z is None:continue
  mat[rr],mat[z]=mat[z],mat[rr]
  for i in range(len(mat)):
   if i!=rr and (mat[i]>>c)&1:mat[i]^=mat[rr]
  piv.append(c);rr+=1
 assert all(v & ((1<<k)-1) or not(v>>k) for v in mat)
 ans=[0]*k
 for j,c in enumerate(piv):ans[c]=(mat[j]>>k)&1
 return ans

def summary(n,M,weights,S,masses):
 d=sum(map(sum,weights))%M; inv=pow(d,-1,M)
 W=[[a*inv%M for a in X] for X in weights]
 ES=[e for e in product(range(n),repeat=3) if sum(W[j][e[j]] for j in range(3))%M==0]
 assert all(sum(masses[k] for k,e in enumerate(S) if e[j]==i)==1 for j in range(3) for i in range(n))
 denom=[sum(e)%M for e in product(*W) if sum(e)%M]
 numerator=[(a-b)%M for X in W for a in X for b in X if a!=b]
 # phase of numerator is positive real, denominator known exactly by principal exponents
 N=len(denom); assert N%2==0
 sign_exp=(sum(denom)-n*n)//M-N//2
 assert (sum(denom)-n*n)%M==0
 sign=(-1)**sign_exp
 mp.mp.dps=60
 logamp=sum(mp.log(2*mp.sin(mp.pi*a/M)) for a in numerator)-sum(mp.log(2*mp.sin(mp.pi*a/M)) for a in denom)
 return {'n':n,'M':M,'weights':W,'support':S,'masses':[str(t) for t in masses],'extra_eigenvalue_one_edges':[e for e in ES if e not in S],'distinct_spectra':all(len(set(X))==n for X in W),'phase_sign':int(sign),'log2_abs_local':str(logamp/mp.log(2))}

records=[]
for n in range(4,21):
 M=2**(n-1)
 rec=summary(n,M,weights,S,masses);records.append(rec)
 print(n,'extra',len(rec['extra_eigenvalue_one_edges']),'distinct',rec['distinct_spectra'],'sign',rec['phase_sign'],'log2',rec['log2_abs_local'],flush=True)
 # Initially select edge index whose mass is 3/8; thereafter select new root.
 ei=next(i for i,m in enumerate(masses) if m==Fraction(3,8)) if n==4 else len(S)-1
 edge=S[ei];mass=masses[ei]
 assert (mass*M).denominator==1 and (mass*M).numerator%2
 rows=[[int(e[j]==v) for j in range(3) for v in range(n)] for e in S]
 rhs=[((1 if i==ei else 0)-sum(weights[j][e[j]] for j in range(3))//M)%2 for i,e in enumerate(S)]
 delta=solve2(rows,rhs,3*n)
 lift=[[weights[j][i]+M*delta[j*n+i] for i in range(n)] for j in range(3)]
 root=[(-sum(lift[k][edge[k]] for k in range(3) if k!=j))%(2*M) for j in range(3)]
 weights=[lift[j]+[root[j]] for j in range(3)]
 S=[e for i,e in enumerate(S) if i!=ei]+[(edge[0],edge[1],n),(edge[0],n,edge[2]),(n,edge[1],edge[2]),(n,n,n)]
 masses=[t for i,t in enumerate(masses) if i!=ei]+[mass/2]*3+[1-mass/2]
(p/'negative_seed_extensions.json').write_text(json.dumps({'scope':'exact supports and diagonal stabilizer/moment data; local determinants only, full non-diagonal stabilizers not yet proved for n>4','records':records},indent=2))
