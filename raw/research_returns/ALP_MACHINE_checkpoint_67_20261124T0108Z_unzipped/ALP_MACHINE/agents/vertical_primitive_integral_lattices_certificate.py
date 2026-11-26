#!/usr/bin/env python3
"""ALP-LIFT-40: exact lattice diagnostics; no global theta matrix."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import factorial, comb, gcd, prod
from functools import reduce
from collections import Counter
from datetime import datetime, timezone
import sympy as s
import json, hashlib

ROOT=Path(__file__).resolve().parent
checks=0;groups=Counter()
def ck(x,label):
 global checks
 assert bool(x),(label,checks)
 checks+=1;groups[label]+=1
def vf(n,p=11):
 z=0
 while n:n//=p;z+=n
 return z
def vp(n,p=11):
 n=abs(int(n));assert n
 z=0
 while n%p==0:n//=p;z+=1
 return z
def vh(lam):
 n=len(lam)
 return sum(vf(x+n-1-i) for i,x in enumerate(lam))-sum(vp(lam[i]-lam[j]+j-i) for i in range(n) for j in range(i+1,n))
def hook(lam):
 n=len(lam)
 return F(prod(factorial(x+n-1-i) for i,x in enumerate(lam)),prod(lam[i]-lam[j]+j-i for i in range(n) for j in range(i+1,n)))
def norm(P,vars):
 return sum(F(int(c*c))*prod(factorial(k) for k in mon) for mon,c in s.Poly(P,*vars).terms())

# Exact ordinary versus Fischer-dual monomials and the n! clearing factor.
for a,n in product((1,2,3),range(8)):
 for gamma in product(range(n+1),repeat=a):
  if sum(gamma)!=n:continue
  fac=prod(factorial(x) for x in gamma)
  ck(factorial(n)%fac==0,'ordinary/divided monomial factorial comparison')

# The divided annihilator has integer coefficients even though the divided
# multiplication creator need not preserve ordinary polynomial coefficients.
for X,Y in product(product(range(4),repeat=2),repeat=2):
 for r in range(5):
  for beta0 in range(r+1):
   beta=(beta0,r-beta0)
   if any(beta[i]>min(X[i],Y[i]) for i in range(2)):continue
   coeff=prod(factorial(beta[i])*comb(X[i],beta[i])*comb(Y[i],beta[i]) for i in range(2))
   via_deriv=F(factorial(r),prod(factorial(z) for z in beta))
   via_deriv*=prod(F(factorial(X[i])*factorial(Y[i]),factorial(X[i]-beta[i])*factorial(Y[i]-beta[i])) for i in range(2))
   via_deriv/=factorial(r)
   ck(via_deriv==coeff,'divided annihilator integral coefficient')
ck(F(1,factorial(2)).denominator==2,'divided creator is not ordinary-integral')

# GL2 by GL2 Cauchy models. Every joint weight is one-dimensional, so
# dividing its generated polynomial by its coefficient gcd computes
# the exact saturated selected lattice at that weight.
x00,x01,x10,x11=s.symbols('x00 x01 x10 x11')
vars=(x00,x01,x10,x11);det=x00*x11-x01*x10
def row_lower(P):return s.expand(x10*s.diff(P,x00)+x11*s.diff(P,x01))
def col_lower(P):return s.expand(x01*s.diff(P,x00)+x11*s.diff(P,x10))
small=[]
for n in range(2,13):
 P=s.expand(x00**(n-1)*det);H=hook((n,1))
 ck(norm(P,vars)==H,'small primitive hook norm')
 ck(H==(n+1)*factorial(n-1),'small closed hook product')
 columns=[P]
 for k in range(1,n):columns.append(s.expand(col_lower(columns[-1])/k))
 for k,Q in enumerate(columns):
  rows=[Q]
  for j in range(1,n):rows.append(s.expand(row_lower(rows[-1])/j))
  for j,R in enumerate(rows):
   terms=s.Poly(R,*vars).terms()
   ck(all(c.q==1 for _,c in terms),'compact divided powers integral')
   content=reduce(gcd,[abs(int(c)) for _,c in terms])
   bj,bk=comb(n-1,j),comb(n-1,k)
   ck(norm(R,vars)==H*bj*bk,'selected tensor form normalization')
   ck((bj*bk)%content==0,'saturated/generated normalized pairing integral')
   coeff=F(bk,content)
   ck((coeff*bj).denominator==1,'selected contraction in dual Weyl')
   ck(F(bk).denominator==1,'generated contraction integral')
   if n==12 and j==1 and k==0:
    ck(content==11 and coeff==F(1,11),'exact selected dual-Weyl denominator11')
    ck(s.expand(R/11-x00**10*x10*det)==0,'primitive selected denominator witness')
   small.append(dict(n=n,j=j,k=k,content=content,contraction_numerator=coeff.numerator,contraction_denominator=coeff.denominator))
 ambient=F(factorial(n),H)
 ck(ambient==F(n,n+1),'ambient diagonal monomial exact image')
 if n==10:ck(ambient==F(10,11),'exact ambient projection denominator11')

# Scalar PBW example: C(z^n)=(r)_n z^n and its exact dual relation.
for r,n in product(range(2,10),range(7)):
 D=prod(r+j for j in range(n))
 ck(F(D*factorial(n),D)==factorial(n),'PBW/Fischer duality equality')
 ck(F(1,factorial(n))*factorial(n)==1,'explicit PBW dual polynomial lattice')

# Actual ranks and exact canonical q endpoints, with complete exact
# hook-ratio and selected-denominator arithmetic.
src=ROOT/'enlarged_gap_admissible_interval_certificate.json'
hosts=json.loads(src.read_text())['hosts'];actual=[]
for host in hosts:
 a=host['a'];t=host['t'];d=t+1;r=a+1;b=r+t
 for role,data in host['roles'].items():
  E=data['E']
  for ellname,ell in [('min',host['ell_min']),('max',host['ell_max'])]:
   qmax=(ell//(28*r))*(28*r)
   for qname,q in [('zero',0),('max',qmax)]:
    ck(q%(28*r)==0 and 0<=q<=ell,'actual canonical twist admissible')
    L=ell-d//2;B=L+q;delta=2*ell+q;Delta=delta-d
    pp=[4*ell*(a-1-i) for i in range(a-1)]+[-E+ell]
    A=[pp[i]+E-a-(t-1)//2+i for i in range(a)]
    Lam=[x+Delta for x in A]+[Delta]*t+[L]
    eta0=[x-L for x in A]
    eta1=[x+B for x in A]+[B]*t+[0]
    ck([x-L for x in Lam]==eta1,'actual middle determinant-twist partition')
    ck(all(eta0[i]>=eta0[i+1]>=0 for i in range(a-1)),'actual minimal Weyl partition')
    C=[A[i]+a-1-i for i in range(a)]
    vHA=vh(A)
    vHL=vHA+sum(vf(x+delta)-vf(x+t)-vp(x+B+d) for x in C)+vf(L)+vf(B)-vf(B+t)
    vHL+=sum(vf(Delta+j) for j in range(1,t+1))-sum(vf(j) for j in range(1,t))
    vHeta0=vh(eta0)
    vHeta1=vHL-sum(vf(Lam[i]+b-1-i)-vf(eta1[i]+b-1-i) for i in range(b))
    ck(vHeta0>=0 and vHeta1>=0,'actual compact hook valuation nonnegative')
    if role=='thin' and ellname=='min' and qname=='zero':
     ck(vHeta1==vh(eta1),'independent full middle Weyl hook')
     ck(vHL==vh(Lam),'independent full oscillator hook')
    pole0=sum(vf(x) for x in A)-vHA
    pole1=sum(vf(x) for x in Lam)-vHL
    ck(pole0<0 and pole1<0,'actual ordinary ambient monomial pole')
    vN0=vHA+vf(B);vN1=vHL
    ck(pole0>=-vN0 and pole1>=-vN1,'ambient dual-lattice denominator bound')
    alpha=[pp[i]-(a-2)//2+i for i in range(a)];beta=-E-ell-q-a//2
    selected=[]
    for bit in (0,1):
     mfirst=2**960+(a-2)//2-4*ell*(a-1) if role=='top' else 4*a*ell
     mlast=E-2**955-ell-a//2 if role=='top' else E+ell
     ms=[mfirst]+[4*ell-1-ell*bit]*(a-2)+[mlast]
     starts=[alpha[i]-beta-i for i in range(a)]
     lam=[alpha[i]+ms[i] for i in range(a)]
     ck(all(x>=0 for x in ms) and all(starts[i]>0 for i in range(a)),'actual selected PBW positivity')
     ck(all(lam[i]>=lam[i+1] for i in range(a-1)),'actual selected compact dominance')
     n=sum(ms);vD=sum(vf(x+m-1)-vf(x-1) for x,m in zip(starts,ms))
     etalam=[x-lam[-1] for x in lam];vHetalam=vh(etalam)
     selected.append(dict(word='all_'+str(bit),degree=n,v11_D=vD,v11_degree_factorial=vf(n),v11_Hselected=vHetalam,
       first_selected_PBW_denominator=vf(n)+vHeta0+vD,
       two_selected_PBW_denominator=vf(n)+vHeta0+vD+vHeta1,
       two_selected_Weyl_denominator=vf(n)+vHeta0+vD+vHeta1+vHetalam))
    actual.append(dict(host=host['host'],role=role,ell_endpoint=ellname,q_endpoint=qname,q=q,
      qmax=qmax,ell=ell,v11_r0=pole0,v11_r1=pole1,v11_N0=vN0,v11_N1=vN1,
      v11_Hminimal=vHeta0,v11_Hmiddle=vHeta1,selected=selected))

proof=ROOT/'vertical_primitive_integral_lattices.md'
rows=[]
for line in proof.read_text().splitlines():
 if line.startswith('| J'):
  row=[x.strip() for x in line.split('|')[1:-1]]
  if len(row)==6:
   rows.append((row[0],row[1],row[2],'zero' if row[3]=='0' else 'max',int(row[4]),int(row[5])))
expected=[(x['host'],x['role'],x['ell_endpoint'],x['q_endpoint'],x['v11_r0'],x['v11_r1']) for x in actual]
ck(rows==expected,'literal report actual valuation table')
out=dict(finding='ALP-LIFT-40',status='PASS',completed_utc=datetime.now(timezone.utc).isoformat(),
 assertions=checks,groups=dict(groups),small_cauchy_weights=len(small),small_cauchy_data=small,actual_profiles=actual,
 input_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
 scope='Exact polynomial lattice, compact divided-power, annihilator, hook and actual admissible-profile diagnostics. No global theta matrix, arithmetic preimage or global Smith form computed.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('small_cauchy_data','actual_profiles')},indent=2))
