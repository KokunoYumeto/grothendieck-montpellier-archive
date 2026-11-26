#!/usr/bin/env python3
"""Original degree-seven CM central-value certificate.

Run: python3 check_septic.py --limit 4096 --precision 112 --output septic_certificate.json
Needs Python3, sympy and python-flint. Analytic input: the Jacobi Hecke
L-function for v^2+v=u^7, conductor7^7, Gamma(s)^3, sign+1.
The coefficients are exact finite-field/Jacobi counts; Arb encloses a finite
Mellin contour. Both infinite tails have explicit inequalities.
"""
from pathlib import Path
import argparse,json,math,time
from flint import fq_default_ctx,arb,acb,ctx
from sympy import primitive_root

def sieve(N):
 spf=list(range(N+1))
 for p in range(2,math.isqrt(N)+1):
  if spf[p]==p:
   for n in range(p*p,N+1,p):
    if spf[n]==n:spf[n]=p
 return [p for p in range(2,N+1) if spf[p]==p],spf

def convolution(a,b):
 c=[0]*7
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[(i+j)%7]+=x*y
 return c

def jacobi_polynomial(p,degree):
 g=int(primitive_root(p)); logs=[0]*p;x=1
 for e in range(p-1):logs[x]=e%7;x=x*g%p
 counts=[0]*7
 for x in range(2,p):counts[(logs[x]+logs[(1-x)%p])%7]+=1
 assert sum(counts)==p-2
 powers=[1]+[0]*6;poly=[1];tr=[0];J=[-z for z in counts]
 for e in range(1,degree+1):
  powers=convolution(powers,J);tr.append(7*powers[0]-sum(powers))
  z=-sum(poly[e-i]*tr[i] for i in range(1,e+1));assert z%e==0;poly.append(z//e)
 return poly,counts

def extension_trace(p):
 F=fq_default_ctx(p,3,'a');N=1
 for i in range(p**3):
  digits=[];k=i
  for _ in range(3):digits.append(k%p);k//=p
  x=F(digits)
  if p==2:
   b=x**7;trace=b+b**2+b**4
   if trace==0:N+=2
  else:
   d=F(1)+F(4)*x**7
   N+=1 if d==0 else (2 if d.is_square() else 0)
 trace=p**3+1-N;assert trace%3==0
 return trace//3,N,str(F.modulus())

def coefficients(N):
 primes,spf=sieve(N);local={};pp={}
 for p in primes:
  e=0;q=p
  while q<=N:e+=1;q*=p
  if p==7:poly=[1];data={'order_mod7':None,'Euler_known':poly}
  else:
   f=1;q=p%7
   while q!=1:f+=1;q=q*p%7
   if f>e:pp[p]=[1]+[0]*e;continue
   if f%2==0:
    poly=[0]*(min(e,6)+1)
    for k in range(6//f+1):
     if k*f<len(poly):poly[k*f]=math.comb(6//f,k)*p**(f*k//2)
    data={'order_mod7':f,'Euler_known':poly,'method':'even residue degree identity'}
   elif f==3:
    t,Nq,mod=extension_trace(p);poly=[1,0,0,-t,0,0,p**3]
    data={'order_mod7':f,'Euler_known':poly,'points_over_p3':Nq,'field_modulus':mod}
   else:
    poly,c=jacobi_polynomial(p,min(e,6));data={'order_mod7':1,'Euler_known':poly,'jacobi_counts':c}
  b=[1]
  for k in range(1,e+1):b.append(-sum(poly[j]*b[k-j] for j in range(1,min(k,len(poly)-1)+1)))
  pp[p]=b;local[p]=data
 a=[0]*(N+1);a[1]=1
 for n in range(2,N+1):
  p=spf[n];q=n;e=0
  while q%p==0:q//=p;e+=1
  a[n]=a[q]*pp[p][e]
 assert all(x==0 for n,x in enumerate(a) if n%7!=1)
 assert pp[2][:4]==[1,0,0,2]
 return {'local_factors':local,'nonzero_coefficients':[(n,x) for n,x in enumerate(a) if x]}

def certify(N,precision):
 start=time.time();ctx.prec=precision;data=coefficients(N)
 B=arb(7**7).sqrt()/(2*arb.pi())**3;sigma=arb(11)/10
 zetaK=acb(sigma.zeta());root=acb(0,2*arb.pi()/6).exp()
 for k in range(1,6):
  L=acb(0)
  for j in range(6):L+=root**(k*j)*acb(sigma).zeta(arb(pow(3,j,7))/7)
  L/=acb(7)**sigma;zetaK*=L
 assert zetaK.imag.contains(0)
 terms=[(arb(a)/arb(n)**3,arb(n).log()) for n,a in data['nonzero_coefficients']]
 logB=B.log();evals=0
 def integrand(t,analytic):
  nonlocal evals
  evals+=1;it=acb(0,1)*t;z=acb(2)+it;S=acb(0)
  for w,logn in terms:S+=w*(-it*logn).exp()
  return (z+1).gamma()**3/z*B**2*(it*logB).exp()*S
 I=acb(0)
 for lo in range(20):I+=acb.integral(integrand,lo,lo+1,abs_tol=arb('1e-15'),rel_tol=arb('1e-15'),eval_limit=30000)
 central=2/arb.pi()*I.real
 S=sum(abs(arb(a))/arb(n)**3 for n,a in data['nonzero_coefficients']);m=17;T=arb(20)
 vertical=2/arb.pi()*B**2*S*arb(3+m).gamma()**3/(3*m*T**(3*m))
 k=4;tail=2*arb(k+1).gamma()**3*B**k*arb(N)**(sigma-k-arb(1)/2)*zetaK.real
 value=central+arb(0,(vertical+tail).upper());assert value>0
 result={'curve':'v^2+v=u^7','conductor':7**7,'sign':1,'gamma_power':3,'cutoff':N,'precision_bits':precision,'B':str(B),'zetaK_1p1':str(zetaK),'truncated_central_value':str(central),'vertical_contour_tail':str(vertical),'coefficient_tail':str(tail),'L_at_one':str(value),'positive':bool(value>0),'evals':evals,'seconds':time.time()-start,**data}
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--limit',type=int,default=4096);p.add_argument('--precision',type=int,default=112);p.add_argument('--output',type=Path,default=Path('septic_certificate.json'));a=p.parse_args();r=certify(a.limit,a.precision);a.output.write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps({k:r[k] for k in ['cutoff','precision_bits','B','zetaK_1p1','truncated_central_value','vertical_contour_tail','coefficient_tail','L_at_one','positive','seconds']},indent=2))
