"""Exact finite supplement for B80; no full-BT CM claim is made."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
from math import isqrt
from datetime import datetime,timezone
import json,time
st=time.perf_counter();counts=Counter();plane_rows=[]
I=(1,0,0,1)
def add(A,B,m):return tuple((x+y)%m for x,y in zip(A,B))
def scale(a,A,m):return tuple(a*x%m for x in A)
def mul(A,B,m):return ((A[0]*B[0]+A[1]*B[2])%m,(A[0]*B[1]+A[1]*B[3])%m,(A[2]*B[0]+A[3]*B[2])%m,(A[2]*B[1]+A[3]*B[3])%m)
def power(A,n,m):
 R=I
 while n:
  if n&1:R=mul(R,A,m)
  A=mul(A,A,m);n//=2
 return R
def det(A,m):return (A[0]*A[3]-A[1]*A[2])%m
def action(A,v,m):return ((A[0]*v[0]+A[1]*v[1])%m,(A[2]*v[0]+A[3]*v[1])%m)
def bracket(A,B,m):return add(mul(A,B,m),scale(-1,mul(B,A,m),m),m)
def scalar(A):return A[1]==A[2]==0 and A[0]==A[3]

for p in (5,7,11):
 d=next(x for x in range(2,p) if pow(x,(p-1)//2,p)==p-1)
 T=(0,d,1,0);Ti=scale(pow(d,-1,p),T,p)
 local=Counter();total=0
 for i,j in combinations(range(4),2):
  places=[(r,k) for r,pivot in enumerate((i,j)) for k in range(pivot+1,4) if k not in (i,j)]
  for vals in product(range(p),repeat=len(places)):
   rs=[[0]*4 for _ in range(2)];rs[0][i]=1;rs[1][j]=1
   for (r,k),x in zip(places,vals):rs[r][k]=x
   A,B=map(tuple,rs);total+=1;counts['all_RREF_matrix_planes']+=1
   def contains(v):return all(v[k]%p==(v[i]*A[k]+v[j]*B[k])%p for k in range(4))
   C=bracket(A,B,p)
   if not contains(C):continue
   counts['Lie_closed_planes']+=1
   stable=contains(mul(mul(T,A,p),Ti,p)) and contains(mul(mul(T,B,p),Ti,p))
   if not stable:continue
   counts['irreducible_tame_stable_Lie_planes']+=1
   assert C==(0,0,0,0)
   assert contains(I)
   X=A if not scalar(A) else B
   assert not scalar(X)
   disc=((X[0]+X[3])**2-4*det(X,p))%p
   assert disc!=0
   typ='split' if pow(disc,(p-1)//2,p)==1 else 'nonsplit'
   original=bracket(T,A,p)==(0,0,0,0) and bracket(T,B,p)==(0,0,0,0)
   assert not original or typ=='nonsplit'
   local[typ+('_original' if original else '_other')]+=1
   m=p**3
   g=add(I,scale(p,A,m),m);h=add(I,scale(p,B,m),m)
   gi=add(add(I,scale(-p,A,m),m),scale(p*p,mul(A,A,m),m),m)
   hi=add(add(I,scale(-p,B,m),m),scale(p*p,mul(B,B,m),m),m)
   assert mul(mul(mul(g,h,m),gi,m),hi,m)==add(I,scale(p*p,C,m),m)
   counts['actual_commutator_identities']+=1
 assert total==(p*p+1)*(p*p+p+1)
 plane_rows.append({'p':p,'all_planes':total,'stable_Lie_types':dict(local)})
 # Every B coefficient in the actual split-Cartan lift is checked.
 m=p**3;E22=(0,0,0,1)
 for B in product(range(p),repeat=4):
  g=add(add(I,scale(p,E22,m),m),scale(p*p,B,m),m)
  terminal=add(I,scale(-p*p*B[0],(1,0,0,0),m),m)
  g=mul(terminal,g,m)
  v=(1,(-p*B[2])%m)
  assert action(g,v,m)==v
  assert power(g,p,m)==add(I,scale(p*p,E22,m),m)!=I
  assert power(g,p*p,m)==I
  counts['split_Cartan_fixed_lifts']+=1

primes=[p for p in range(5,102) if all(p%d for d in range(2,isqrt(p)+1))]
for p in primes:
 q=p*p;N=q-1;A=p*(p-1)
 assert sum(1 for s in range(1,5) for t in range(5) if s+t==4 and s<=t)==2
 counts['layer_shapes']+=1
 for D in (q*A,q*q*A):
  b0=(D-A)//p;assert p*b0==D-A and b0%N==0
  # Exact boundary/first-coefficient checks on a transparent set of breaks.
  test_breaks={N//2,N//2+N,b0-N//2,b0+N//2,2*b0-N//2}
  for b in sorted(test_breaks):
   assert b>0 and b%N==N//2 and b!=b0
   if b<b0:
    j=A+(p-1)*b
    assert A<j<D and (j%p!=0)==(b%p!=0)
    c=D-j
    assert c>b0 and c%N==0
    for b2 in (b+N,b+2*N,b0+N//2,2*b0+N//2):
     if b2>b:assert j+b2<A+p*b2
     counts['low_to_later_break_comparisons']+=1
   else:
    j=D-b
    for b2 in (b+N,b+2*N):
     assert j+b2>D and A+p*b2>D
     counts['high_to_later_break_comparisons']+=1
   counts['first_prime_degree_cases']+=1
 # The exact anti lift/pth-power clash includes all low tame-compatible
 # anti breaks at the first (qA) displacement level.
 a0=N*(p-1);D2=q*q*A
 for a in range(N//2,a0,N):
  if a%p==0:continue
  j=A+(p-1)*a;forced_b=D2-j
  assert forced_b>a and forced_b%N==0
  assert forced_b%N!=N//2
  assert j+forced_b<A+p*forced_b
  counts['anti_lift_power_clashes']+=1
 # Explicit cardinality of p-1 power fibres in the quadratic field.
 d=next(x for x in range(2,p) if pow(x,(p-1)//2,p)==p-1)
 def fm(x,y):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
 def fpow(x,n):
  z=(1,0)
  while n:
   if n&1:z=fm(z,x)
   x=fm(x,x);n//=2
  return z
 fibres=Counter(fpow(x,p-1) for x in product(range(p),repeat=2) if x!=(0,0))
 assert len(fibres)==p+1 and set(fibres.values())=={p-1}
 counts['finite_field_power_fibres']+=len(fibres)
 if p<=13:
  for a in product(range(p),repeat=2):
   if a==(0,0):continue
   scalar_factor=fpow(a,q-p)
   for beta in product(range(p),repeat=2):
    beta2=fm(scalar_factor,fpow(beta,p))
    for z in ((1,0),(0,1)):
     left=fm(a,fpow(fm(beta,fpow(z,p)),p))
     right=fm(beta2,fpow(fm(a,fpow(z,p)),p))
     assert left==right
     counts['exact_anti_Cartan_conjugacies']+=1


out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-st,'counts':dict(counts),'plane_rows':plane_rows,
     'scope':'All RREF matrix planes at p5,7,11 and their Lie/tame conditions; all displayed split-Cartan lift coefficients at those primes; retained first-coefficient break tests and exact quadratic-field power fibres for primes5..101. Uniform proofs are separate. No finite-level Cartan is promoted to a full CM endomorphism action.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
