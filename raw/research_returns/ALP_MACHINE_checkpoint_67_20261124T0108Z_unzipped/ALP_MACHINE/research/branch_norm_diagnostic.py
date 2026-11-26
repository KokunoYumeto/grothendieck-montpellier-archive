"""Exploratory exact diagnostics; no theorem certified by this file alone."""
from itertools import permutations,product,combinations
from math import factorial,prod
from fractions import Fraction
from functools import lru_cache
import json
from pathlib import Path

N=0

def add(p,q,c=1):
 r=p.copy()
 for m,a in q.items():
  r[m]=r.get(m,0)+c*a
  if not r[m]:del r[m]
 return r

def mul(p,q):
 r={}
 for m,a in p.items():
  for n,b in q.items():
   k=tuple(x+y for x,y in zip(m,n));r[k]=r.get(k,0)+a*b
 return {k:v for k,v in r.items() if v}

def power(p,e):
 r={(0,)*(N*N):1}
 for _ in range(e):r=mul(r,p)
 return r

def minor(rows):
 k=len(rows);r={}
 for c in permutations(range(k)):
  m=[0]*(N*N)
  for i,j in zip(rows,c):m[i*N+j]+=1
  sign=(-1)**sum(c[i]>c[j] for i in range(k) for j in range(i+1,k))
  r[tuple(m)]=sign
 return r

def xi(lam,mu):
 r={(0,)*(N*N):1}
 for i in range(N-1):
  r=mul(r,power(minor(tuple(range(i+1))),mu[i]-lam[i+1]))
  r=mul(r,power(minor(tuple(range(i))+(N-1,)),lam[i]-mu[i]))
 return r

def E(p,i,j):
 r={}
 for m,a in p.items():
  for c in range(N):
   if m[j*N+c]:
    n=list(m);b=a*m[j*N+c];n[j*N+c]-=1;n[i*N+c]+=1;n=tuple(n)
    r[n]=r.get(n,0)+b
 return {k:v for k,v in r.items() if v}

def lower(p,mu,i):
 r={};middle=list(range(i+1,N-1))
 for s in range(len(middle)+1):
  for path in combinations(middle,s):
   coeff=prod(mu[i]-mu[j]+j-i for j in middle if j not in path)
   chain=(i,)+path+(N-1,);term=p
   for j in range(len(chain)-2,-1,-1):term=E(term,chain[j+1],chain[j])
   r=add(r,term,coeff)
 return r

def norm(p):return sum(a*a*prod(factorial(e) for e in m) for m,a in p.items())

def candidate(lam,mu):
 x=Fraction(1)
 for i in range(N-1):
  for j in range(i,N-1):x*=Fraction(factorial(lam[i]-mu[j]+j-i),factorial(mu[i]-mu[j]+j-i))
 for i in range(N-1):
  for j in range(i+1,N):x*=Fraction(factorial(mu[i]-lam[j]+j-i-1),factorial(lam[i]-lam[j]+j-i-1))
 return x

def main():
 global N
 count=lc=0;fails=[]
 for N in range(2,6):
  for lam in product(range(4),repeat=N-1):
   lam=lam+(0,)
   if sorted(lam,reverse=True)!=list(lam) or sum(lam)>8:continue
   high=xi(lam,lam[:-1]);den=norm(high)
   for mu in product(*(range(lam[i+1],lam[i]+1) for i in range(N-1))):
    p=xi(lam,mu);got=Fraction(norm(p),den);want=candidate(lam,mu)
    if got!=want:fails.append({'kind':'norm','lam':lam,'mu':mu,'got':str(got),'want':str(want)})
    count+=1
    for i in range(N-1):
     if mu[i]==lam[i+1]:continue
     nxt=list(mu);nxt[i]-=1
     coeff=prod(mu[i]-lam[j]+j-i-1 for j in range(i+1,N))
     expected={k:coeff*a for k,a in xi(lam,nxt).items()}
     if lower(p,mu,i)!=expected:fails.append({'kind':'lower','lam':lam,'mu':mu,'i':i,'coeff':coeff})
     lc+=1
 out={'status':'PASS' if not fails else 'FAIL','norm_cases':count,'lower_cases':lc,'failures':fails[:20],'scope':'Exploratory finite cases; no general normalization proof.'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out))
if __name__=='__main__':main()
