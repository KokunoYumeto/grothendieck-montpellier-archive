#!/usr/bin/env python3
"""B97 finite supplement. No formal groups or field realizations are inferred."""
from pathlib import Path
from itertools import product, combinations
from datetime import datetime,timezone
import json,time,traceback

OUT=Path(__file__).with_suffix('.output.json')
assert not OUT.exists(), 'Preserve any prior executed output before rerunning'
start=time.perf_counter();counts={}

def mul(A,B,m):
 a,b,c,d=A;e,f,g,h=B
 return ((a*e+b*g)%m,(a*f+b*h)%m,(c*e+d*g)%m,(c*f+d*h)%m)

def power(A,n,m):
 R=(1,0,0,1)
 while n:
  if n&1:R=mul(R,A,m)
  A=mul(A,A,m);n//=2
 return R

def evalv(A,v,p):
 return ((A[0]*v[0]+A[1]*v[1])%p,(A[2]*v[0]+A[3]*v[1])%p)

def det(A,p):return (A[0]*A[3]-A[1]*A[2])%p

def projective(n,p):
 for pivot in range(n):
  for tail in product(range(p),repeat=n-pivot-1):yield (0,)*pivot+(1,)+tail

def planes(p):
 for i,j in combinations(range(4),2):
  positions=[(0,k) for k in range(i+1,4) if k!=j]+[(1,k) for k in range(j+1,4)]
  for values in product(range(p),repeat=len(positions)):
   rows=[[0]*4 for _ in range(2)];rows[0][i]=rows[1][j]=1
   for (r,k),v in zip(positions,values):rows[r][k]=v
   yield tuple(rows[0]),tuple(rows[1])

def run():
 plane_rows=[];totalplanes=totaldivisions=normaltests=0
 powertests=0;coefftests=0;boundarytests=0;uniformtests=0;forbidden=0
 for p in (5,7,11):
  lines=list(projective(2,p));nplanes=ndiv=0
  for X,Y in planes(p):
   nplanes+=1
   onto=all(det((*evalv(X,v,p),*evalv(Y,v,p)),p)!=0 for v in lines)
   # The preceding determinant uses two evaluation rows; nonvanishing
   # is the same as using them as columns. Check independently by
   # enumerating every projective nonzero matrix in the plane.
   division=all(det(tuple((a*x+b*y)%p for x,y in zip(X,Y)),p)!=0 for a,b in lines)
   assert onto==division
   if division:
    ndiv+=1
    for v in lines:
     assert all(evalv(tuple((a*x+b*y)%p for x,y in zip(X,Y)),v,p)!=(0,0) for a,b in lines)
     normaltests+=len(lines)
  assert nplanes==p**4+p**3+2*p*p+p+1
  plane_rows.append({'p':p,'all_planes':nplanes,'every_evaluation_surjective_planes':ndiv})
  totalplanes+=nplanes;totaldivisions+=ndiv
  # Exact power identity for every first matrix and five explicit second
  # matrices. The all-coefficient proof is in the candidate.
  Bs=[(0,0,0,0)]+[tuple(int(i==j) for i in range(4)) for j in range(4)]
  for A in product(range(p),repeat=4):
   for B in Bs:
    M=tuple(((1 if i in (0,3) else 0)+p*A[i]+p*p*B[i])%(p**3) for i in range(4))
    expected=tuple(((1 if i in (0,3) else 0)+p*p*A[i])%(p**3) for i in range(4))
    assert power(M,p,p**3)==expected;powertests+=1
  q=p*p;N=q-1;A=p*(p-1);D1=q*A;D2=q*q*A
  a0=(D1-A)//p;j0=A+(p-1)*a0
  assert a0==N*(p-1) and j0==D1-a0 and j0%p==p-1
  for a in range(1,D1-A+1):
   if a==a0:continue
   j=A+(p-1)*a if a<a0 else D1-a
   if j<=A or j%p==0:forbidden+=1;continue
   b=a+1
   expected=(p-1)*(b-a)+(0 if a<a0 else p*(a-a0))
   assert A+p*b-(j+b)==expected>0;coefftests+=1
  bstar=D2-j0
  assert p*bstar-(D2-A)==(p-1)*(D2-D1)>0
  assert A+p*bstar>D2 and j0+bstar==D2
  for b in (a0+1,bstar,D2-A):
   assert A+p*b-(j0+b)==(p-1)*(b-a0)>0;boundarytests+=1
  # Uniform displacement conductor: all possible integer first breaks.
  for level,D in ((1,D1),(2,D2)):
   b0=(D-A)//p
   assert b0==(q**level-1)*(p-1)
   for t in range(1,b0):
    j=A+(p-1)*t;u=D-j
    assert u>t and j+u==D
    assert u+(p-1)*t==p*b0
    assert A+p*u>j+u
    uniformtests+=1
 counts.update({'matrix_planes':totalplanes,'division_planes':totaldivisions,
  'central_stabilizer_evaluation_checks':normaltests,'literal_pth_powers':powertests,
  'two_level_first_break_checks':coefftests,'impermissible_first_degrees':forbidden,
  'boundary_comparisons':boundarytests,'uniform_point_conductor_rows':uniformtests})

 # Every three-dimensional matrix hyperplane at the three primes.
 lie_rows=[];hyper=lietests=0
 for p in (5,7,11):
  nlie=ntrace=0
  for normal in projective(4,p):
   pivot=next(i for i,x in enumerate(normal) if x)
   basis=[]
   for j in range(4):
    if j==pivot:continue
    x=[0]*4;x[j]=1;x[pivot]=-normal[j]%p;basis.append(tuple(x))
   closed=True
   for X,Y in combinations(basis,2):
    XY=mul(X,Y,p);YX=mul(Y,X,p)
    if sum(normal[j]*(XY[j]-YX[j]) for j in range(4))%p:closed=False;break
   hyper+=1
   if not closed:continue
   nlie+=1
   tracefree=all((X[0]+X[3])%p==0 for X in basis)
   if tracefree:ntrace+=1
   else:
    common=[]
    for v in projective(2,p):
     if all((evalv(X,v,p)[0]*v[1]-evalv(X,v,p)[1]*v[0])%p==0 for X in basis):common.append(v)
    assert common, (p,normal,basis)
   lietests+=1
  assert ntrace==1 and nlie==p+2
  lie_rows.append({'p':p,'three_dimensional_Lie_algebras':nlie,'tracefree':ntrace,'others_preserve_a_line':nlie-ntrace})
 counts['three_dimensional_hyperplanes']=hyper
 counts['three_dimensional_Lie_algebras']=lietests

 # Exact Frobenius check in quadratic fields, retaining every element.
 ftests=0;cycro=[]
 for p in (5,7,11,13,17,19,23,29,31):
  nu=next(x for x in range(2,p) if pow(x,(p-1)//2,p)==p-1)
  def fm(x,y):return ((x[0]*y[0]+nu*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
  def fp(x,n):
   y=(1,0)
   while n:
    if n&1:y=fm(y,x)
    x=fm(x,x);n//=2
   return y
  for x in product(range(p),repeat=2):
   assert fp(x,p)==(x[0],-x[1]%p);ftests+=1
  assert fp((1,0),p)==(1,0) and fp((0,1),p)!=(0,1)
  q=p*p;N=q-1;c1=N*(p-1);c2=(q*q-1)*(p-1)
  lhs=p**3*(N*N-c1)-p*c2
  rhs=p*N*(p-1)*(p**3-p*p-1)
  assert lhs==rhs>0
  cycro.append({'p':p,'point25_last_conductor':c1,'point125_relative_last_conductor':c2,
                'cyclotomic_strict_gap':lhs})
 counts['quadratic_field_elements']=ftests
 counts['cyclotomic_inequalities']=len(cycro)
 return {'plane_rows':plane_rows,'Lie_rows':lie_rows,'point_conductor_rows':cycro}

try:
 data=run();status='PASS';error=None
except Exception:
 status='FAIL';error=traceback.format_exc();data={}
record={'status':status,'actual_utc':datetime.now(timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-start,'counts':counts,'data':data,'error':error,
 'scope':'Exact finite supplement to B97. Matrix-plane and Lie-algebra censuses, literal matrix powers, permitted and impossible first degrees, boundary arithmetic, uniform point-field conductor identities, and exact quadratic-field Frobenius checks. Every actual field, normality, ramification conversion and all-prime assertion requires the complete written proof. No formal-group realization or unrestricted least-index equality is asserted.'}
OUT.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='data'},indent=2))
if status!='PASS':raise SystemExit(1)
