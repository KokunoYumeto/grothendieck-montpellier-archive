"""Finite exact audit of the height-two Honda lower bound at all primes.
This certificate supplements the proof; it is not used as an induction argument.
"""
from math import gcd
import json,time
start=time.monotonic()
primes=[2,3,5,7,11,13,17,19];emax=1200

def vp(a,p):
 s=0
 while a%p==0:a//=p;s+=1
 return s

def dval(p,n,A,B):
 return (p-1)*p**(n-1)*(A+p**n*B+sum((p-1)*p**(n-j-1)*min(A,p**(2*j)*B) for j in range(1,n)))

def closed(p,n,m,e):
 if e%(p-1):return False
 s=vp(e//(p-1),p)
 return s>=n-1 and m*e>=(p*p-1)*p**max(2*n-2,4*n-4-s)
rows=[];constructed=0
for p in primes:
 for m in [p+1]:
  if (p+1)%m or m%p==0:continue
  for n in [1,2,3]:
   phi=(p-1)*p**(n-1);realized=set();pairs=0
   maxB=m*emax//(phi*(1+p**n))
   for B in range(1,maxB+1):
    if gcd(B,m)!=1:continue
    maxA=m*emax//phi-p**n*B
    for A in range(B,maxA+1,m):
     d=dval(p,n,A,B)
     if d%m==0 and 1<=d//m<=emax:realized.add(d//m);pairs+=1
   predicted={e for e in range(p-1,emax+1,p-1) if closed(p,n,m,e)}
   assert realized==predicted,(p,n,m,sorted(realized^predicted))
   for e in predicted:
    allowed=[r for r in range(n) if e%((p-1)*p**(2*n-r-2))==0 and m*e>=(p*p-1)*p**(2*n+r-2)]
    r=max(allowed);A=m*e//((p-1)*p**(2*n-r-2))-p**(2*r+1)
    assert A>=1 and A%m==1%m and dval(p,n,A,1)==m*e
    assert A>=p**(2*r) and (r==n-1 or A<=p**(2*r+2))
    constructed+=1
   rows.append({'p':p,'m':m,'n':n,'e_max':emax,'integer_pairs':pairs,'realized_indices':len(realized),'criteria_match':True})
least_checks=0
for p in primes:
 m=p+1
 for e in range(p-1,5001,p-1):
  s=vp(e//(p-1),p)
  if m*e<p*p-1:N=0
  else:
   L=0
   while (p*p-1)*p**(L+1)<=m*e:L+=1
   N=1+min(s,L//2,(L+s)//4)
  actual=max([n for n in range(1,10) if closed(p,n,m,e)] or [0])
  assert N==actual,(p,e,N,actual)
  least_checks+=1
print(json.dumps({'integer_range_checks':rows,'constructed_pairs_checked':constructed,'least_level_checks':least_checks,'all_checks_passed':True,'seconds':time.monotonic()-start},indent=2))
