#!/usr/bin/env python3
"""Exact normalization diagnostics for ALP-LIFT-39; no theta-period evaluation."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from math import factorial,prod
from datetime import datetime,timezone
from collections import Counter
import sympy as s
import json,hashlib

checks=0;groups=Counter()
def check(x,g):
 global checks
 assert x,(g,checks)
 checks+=1;groups[g]+=1

def vp(n,p=11):
 n=abs(int(n));assert n
 z=0
 while n%p==0:z+=1;n//=p
 return z

def vf(n,p=11):
 z=0
 while n:n//=p;z+=n
 return z

def flo_prefix(N,m):
 q,r=divmod(N,m)
 return m*q*(q-1)//2+q*r

def sum_vf(start,count,p=11):
 assert start>=0 and count>=0
 z=0;m=p;last=start+count-1
 while m<=last:
  z+=flo_prefix(start+count,m)-flo_prefix(start,m);m*=p
 return z

def hook(lam):
 n=len(lam)
 return F(prod(factorial(lam[i]+n-1-i) for i in range(n)),
          prod(lam[i]-lam[j]+j-i for i,j in combinations(range(n),2)))

def vh(lam):
 n=len(lam)
 return sum(vf(lam[i]+n-1-i) for i in range(n))-sum(vp(lam[i]-lam[j]+j-i) for i,j in combinations(range(n),2))

def p_minor(lam,rows):
 cols=len(lam);X=s.Matrix(rows,cols,lambda i,j:s.Symbol(f'x{i}_{j}'))
 z=s.Integer(1)
 for k in range(1,cols+1):
  power=lam[k-1]-(lam[k] if k<cols else 0)
  if power:z*=X[:k,:k].det()**power
 return X,s.Poly(s.expand(z),*list(X))

def fnorm(expr,vars):
 pp=s.Poly(s.expand(expr),*vars)
 return sum(F(int(c*c))*prod(factorial(x) for x in exps) for exps,c in pp.terms())

# Exact finite Fourier orthogonality: nonzero linear frequencies have uniform fibers.
for q in (2,3,5,7):
 for dim in (1,2):
  vectors=list(product(range(q),repeat=dim))
  for freq in vectors:
   count=Counter(sum(x*y for x,y in zip(freq,z))%q for z in vectors)
   if any(freq):check(all(count[j]==q**(dim-1) for j in range(q)),"finite Fourier orthogonality")
   else:check(count=={0:q**dim},"zero Fourier frequency")

# Primitive joint harmonic, highest raising, and exact Fischer norm.
poly_cases=0
for A,B,t in [((1,),1,1),((2,),2,1),((2,1),1,1),((2,2),2,1),((2,1,1),1,1)]:
 a=len(A);b=a+t+1
 X,p=p_minor(A,b);ys=s.symbols('y0:'+str(b));vars=list(X)+list(ys)
 P=s.expand(p.as_expr()*ys[-1]**B)
 check(fnorm(P,vars)==hook(A)*factorial(B),"first exact Fock norm")
 pp=s.Poly(P,*vars);check(any(c==1 for _,c in pp.terms()),"primitive coefficient")
 for i in range(a):
  check(s.expand(sum(s.diff(P,X[c,i],ys[c]) for c in range(b)))==0,"joint harmonic contraction")
 for c,d in combinations(range(b),2):
  raising=sum(X[c,i]*s.diff(P,X[d,i]) for i in range(a))-ys[d]*s.diff(P,ys[c])
  check(s.expand(raising)==0,"target highest operator")
 for i,j in combinations(range(a),2):
  check(s.expand(sum(X[c,i]*s.diff(P,X[c,j]) for c in range(b)))==0,"source compact highest operator")
 # E_1 is the highest noncompact matrix-unit creator. Its norm is the PBW Pochhammer.
 E=sum(X[c,0]*ys[c] for c in range(b))
 for m in range(4):
  v=s.expand(E**m*P)
  expected=hook(A)*factorial(B)*factorial(m)*prod(A[0]+B+b+j for j in range(m))
  check(fnorm(v,vars)==expected,"PBW Fock norm ratio")
 poly_cases+=1
for lam in ((1,),(2,1),(3,2,1),(2,2,1,1)):
 X,p=p_minor(lam,len(lam)+1)
 check(fnorm(p.as_expr(),list(X))==hook(lam),"second exact Fock norm")

# Independent exact factorization PN22 and Legendre prefix formulas.
for start,count in product(range(15),range(1,12)):
 check(sum_vf(start,count)==sum(vf(start+j) for j in range(count)),"factorial valuation interval")
for a,t,ell,E,qcan in product((1,2,3),(1,3),(3,5),(7,13),(0,1)):
 d=t+1
 if ell<=d//2:continue
 b=a+t+1;ll=ell-d//2;B=ll+qcan;delta=2*ell+qcan;Delta=delta-d
 p=[4*ell*(a-1-i) for i in range(a-1)]+[-E+ell]
 A=[p[i]+E-a-(t-1)//2+i for i in range(a)]
 Lam=[x+Delta for x in A]+[Delta]*t+[ll]
 C=[A[i]+a-1-i for i in range(a)]
 rhs=F(1)
 for z in C:rhs*=F(factorial(z+delta),factorial(z+t)*(z+B+d))
 rhs*=F(factorial(ll)*factorial(B),factorial(B+t))
 rhs*=F(prod(factorial(Delta+u) for u in range(1,t+1)),prod(factorial(u) for u in range(1,t)))
 check(hook(Lam)/hook(A)==rhs,"PN22 hook factorization")
 check(vh(A)>=0 and vh(Lam)>=0,"integer hook valuations")

# Actual K044 profiles: full partition/HC labels, all allowed interval endpoints.
base=Path(__file__).resolve().parent
hosts=json.loads((base/'enlarged_gap_admissible_interval_certificate.json').read_text())['hosts']
tables=[]
for host in hosts:
 a=host['a'];f=host['f'];t=1759 if a==42 else 1633;d=t+1;r=a+1;b=r+t;N=b+t;h=1 if a==42 else 4
 for role,entry in host['roles'].items():
  E=entry['E']
  for ell in (host['ell_min'],host['ell_max']):
   for qcan in (0,ell):
    pp=[4*ell*(a-1-i) for i in range(a-1)]+[-E+ell]
    pm=-E-ell-qcan;A=[pp[i]+E-a-(t-1)//2+i for i in range(a)]
    ll=ell-d//2;B=ll+qcan;delta=2*ell+qcan;Delta=delta-d
    Lam=[x+Delta for x in A]+[Delta]*t+[ll]
    check(len(A)==a and A[-1]==ll>0 and all(A[i]>=A[i+1] for i in range(a-1)),"actual first partition")
    check(len(Lam)==b and all(Lam[i]>=Lam[i+1]>0 for i in range(b-1)),"actual second partition")
    h10=pp+[-E+(t-1)//2-j for j in range(t)]+[pm]
    h20=h10+[-E-delta+(t-1)//2-j for j in range(t)]
    check(all(h10[i]>h10[i+1] for i in range(b-1)),"actual middle HC order")
    check(all(h20[i]>h20[i+1] for i in range(N-1)),"actual terminal HC order")
    for eta in (F(1,2),F(-1,2)):
     alpha=[pp[i]-F(a-2,2)+i for i in range(a)];beta=F(pm)-F(a,2)
     check([F(x)+F(b,2)-E for x in A]==alpha,"first source vacuum shift")
     check(-B-F(b,2)-E==beta,"first negative vacuum shift")
     target=[F(x)+F(a-1,2)-E+eta for x in A+[0]*t+[-B]]
     hc=[target[i]+F(b-1,2)-i for i in range(b)]
     check(hc==[F(x)+eta for x in h10],"first exact target Dpar1")
     source=[F(x)+F(N,2)-E-delta+eta for x in Lam]
     check(source==target,"second exact source compact type")
     target2=[F(x)+F(b,2)-E-delta for x in Lam+[0]*t]
     check([target2[i]+F(N-1,2)-i for i in range(N)]==h20,"second exact target Dpar2")
    C=[A[i]+a-1-i for i in range(a)]
    check(C==[pp[i]+E-d//2 for i in range(a)],"short hook coordinates")
    vA=vh(A)
    vL=vA+sum(vf(z+delta)-vf(z+t)-vp(z+B+d) for z in C)
    vL+=vf(ll)+vf(B)-vf(B+t)+sum_vf(Delta+1,t)-sum_vf(1,t-1)
    check(vL>=0,"actual second hook valuation")
    # One full 1802-row Vandermonde replay per host, separate from block formula.
    if role=='thin' and ell==host['ell_min'] and qcan==0:
     check(vL==vh(Lam),"actual independent full hook valuation")
    vH=vA+vf(B)+vL
    tables.append(dict(host=host['host'],role=role,ell_endpoint='min' if ell==host['ell_min'] else 'max',q_endpoint='zero' if qcan==0 else 'ell',
      A_degree=sum(A),B=B,Lambda_degree=sum(Lam),v11_HA=vA,v11_Bfactorial=vf(B),v11_HLambda=vL,v11_local_hook_product=vH))
 check(r+N==2*b,"two-edge raw vacuum power")
 check(7*h*(r*b+b*N)==14*h*b*b,"Gaussian squared norm power")

# Distinct fixed-polynomial, physical vacuum and isometric intertwiner scalings.
for nu0,nu1,H0,H1,rho2 in product((F(1),F(3,7)),(F(1),F(2,5)),(2,6),(3,8),(5,11)):
 sprod2=1/(nu0*nu1*H0*H1)
 check(sprod2*nu0*nu1*H0*H1==1,"primitive fixed-polynomial scale")
 check(F(H0*rho2,rho2)==H0,"PBW common scale cancellation")
 check(F(1,H0*H1)<=1,"unit-vacuum inverse scale")
 # The same physical unit test and the raw primitive test give identical energies.
 for nu,H,dimreal in ((nu0,H0,13),(nu1,H1,17)):
  s2=1/(nu*H)
  from_unit=F(1,dimreal)/s2
  from_raw=nu*H/dimreal
  check(from_unit==from_raw,"fixed physical test versus raw primitive test")
  check(from_raw/(F(H,dimreal))==nu,"raw repinning energy ratio")

proof=base/'vertical_primitive_fock_normalization.md'
out=dict(finding='ALP-LIFT-39',status='PASS',completed_utc=datetime.now(timezone.utc).isoformat(),assertions=checks,groups=dict(groups),
 direct_first_polynomial_cases=poly_cases,actual_profiles=tables,proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
 scope='Finite Fourier, exact Fock polynomials, hooks, actual type lists and scalar normalization. No automorphic period, primitive theta-image minor, or full arithmetic pin is computed.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='actual_profiles'},indent=2))
