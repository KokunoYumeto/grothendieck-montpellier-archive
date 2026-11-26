#!/usr/bin/env python3
"""Rigorous central-derivative certificate for the Jacobian of y^11=x(1-x)^2.

Analytic inputs: the Jacobi-sum Hecke character, conductor 11¹¹, root
number -1 and Gamma(s)^5 factor; the companion paper proves and identifies these inputs.
The code counts exact finite-field Jacobi sums, forms all required
Euler coefficients, and uses Arb to enclose a finite contour integral.
The omitted Dirichlet and vertical contour tails have proved explicit
bounds. No numerical rank routine or unproved BSD implication is used.

Requirements: Python 3, python-flint, sympy, and a C compiler named cc.
The temporary compiled helper is removed when the process exits.
"""
from __future__ import annotations
from pathlib import Path
import ctypes, json, math, time, tempfile, subprocess, argparse
from flint import fq_default_ctx, arb, acb, ctx
BASE=Path(__file__).resolve().parent
_temporary = tempfile.TemporaryDirectory(prefix='fermat_eleven_')
_library = Path(_temporary.name)/'jacobi_counts.so'
subprocess.run(['cc','-x','c','-O3','-shared','-fPIC',str(BASE/'eleven_rankone_counts_source.txt'),'-o',str(_library)],check=True)
lib=ctypes.CDLL(str(_library))
lib.jacobi_counts.argtypes=[ctypes.c_int,ctypes.POINTER(ctypes.c_int)]

def sieve(N):
 spf=list(range(N+1))
 for p in range(2,math.isqrt(N)+1):
  if spf[p]==p:
   for n in range(p*p,N+1,p):
    if spf[n]==n:spf[n]=p
 return [n for n in range(2,N+1) if spf[n]==n],spf

def mul(a,b):
 c=[0]*11
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[(i+j)%11]+=x*y
 return c

def polynomial_from_counts(counts, degree, trace_divisor=1):
 j=[-x for x in counts]
 powers=[1]+[0]*10
 poly=[1]
 tr=[0]
 for e in range(1,degree+1):
  powers=mul(powers,j)
  full_trace=11*powers[0]-sum(powers)
  assert full_trace%trace_divisor==0
  tr.append(full_trace//trace_divisor)
  z=-sum(poly[e-i]*tr[i] for i in range(1,e+1))
  assert z%e==0
  poly.append(z//e)
 return poly

def extension_counts(p):
 from sympy import factorint
 F=fq_default_ctx(p,5,'a');q=p**5
 factors=list(factorint(q-1))
 # Exhaustive enumeration makes the choice independent of FLINT's modulus.
 for index in range(1,q):
  g=F([(index//(p**i))%p for i in range(5)])
  if all(g**((q-1)//f)!=1 for f in factors):
   break
 else:
  raise AssertionError('No primitive element in the finite field')
 logs={};values=[];x=F(1)
 for i in range(q-1):
  assert str(x) not in logs
  logs[str(x)]=i%11;values.append(x);x*=g
 assert x==1
 counts=[0]*11
 for x in values:
  if x==1:continue
  counts[(logs[str(x)]+2*logs[str(F(1)-x)])%11]+=1
 assert sum(counts)==q-2
 poly=polynomial_from_counts(counts,2,5)
 assert poly[2]==q
 return -poly[1],str(F.modulus()),counts

def compute(N):
 primes,spf=sieve(N);local={};pp={}
 for p in primes:
  e=0;q=p
  while q<=N:e+=1;q*=p
  if p==11:
   poly=[1];data={'order_mod_11':None,'Euler_known':poly}
  else:
   f=1;r=p%11
   while r!=1:f+=1;r=r*p%11
   if f>e:
    pp[p]=[1]+[0]*e
    continue
   if f%2==0:
    poly=[0]*(min(e,10)+1)
    for k in range(10//f+1):
     if k*f<len(poly):poly[k*f]=math.comb(10//f,k)*p**(f*k//2)
    data={'order_mod_11':f,'Euler_known':poly,'method':'even residue degree Jacobi sum identity'}
   elif f==5:
    s,mod,counts=extension_counts(p)
    poly=[0]*11;poly[0]=1;poly[5]=-s;poly[10]=p**5
    data={'order_mod_11':f,'Euler_known':poly,'trace_degree5_factor':s,'finite_field_modulus':mod,'jacobi_counts':counts}
   else:
    arr=(ctypes.c_int*11)();lib.jacobi_counts(p,arr);counts=list(arr)
    assert sum(counts)==p-2
    poly=polynomial_from_counts(counts,min(e,10))
    data={'order_mod_11':f,'Euler_known':poly,'jacobi_counts':counts}
   local[p]=data
  b=[1]
  for k in range(1,e+1):b.append(-sum(poly[j]*b[k-j] for j in range(1,min(k,len(poly)-1)+1)))
  pp[p]=b
  if p==11:local[p]=data
 a=[0]*(N+1);a[1]=1
 for n in range(2,N+1):
  p=spf[n];m=n;e=0
  while m%p==0:m//=p;e+=1
  a[n]=a[m]*pp[p][e]
 assert all(a[n]==0 for n in range(1,N+1) if n%11!=1)
 return {'curve':'y^11=x(1-x)^2','limit':N,'local_factors':local,'coefficients':[[n,x] for n,x in enumerate(a) if x]}

def certificate(N, precision):
 ctx.prec=precision
 data=compute(N)
 A=arb(11**11).sqrt()/(2*arb.pi())**5
 sigma=arb(11)/10
 root=acb(0,2*arb.pi()/10).exp()
 # zeta_K(s)=product of all ten Dirichlet L-functions modulo 11.
 # The principal imprimitive L requires the factor at the ramified prime:
 # zeta_K = zeta(s) * product(nonprincipal L), not product(all imprimitive L).
 zetaK=acb(sigma.zeta())
 for k in range(1,10):
  L=acb(0)
  for j in range(10):
   a=pow(2,j,11)
   L += root**(k*j)*acb(sigma).zeta(arb(a)/11)
  L /= acb(11)**sigma
  zetaK *= L
 
 assert zetaK.real<4
 # The finite sum is a meromorphic function of the complex t variable.
 # Gamma evaluation and division detect poles, so analytic=True is safe.
 terms=[(arb(a)/arb(n)**3,arb(n).log()) for n,a in data['coefficients']]
 logA=A.log()
 seen=0
 def integrand(t,analytic):
  nonlocal seen
  seen+=1
  z=acb(2)+acb(0,1)*t
  S=acb(0)
  for w,logn in terms:S += w*(-acb(0,1)*t*logn).exp()
  return (z+1).gamma()**5/z**2 * A**2 * (acb(0,1)*t*logA).exp()*S
 start=time.time()
 # Split into moderate intervals to avoid enclosing remote gamma poles.
 I=acb(0)
 for lo in range(20):
  piece=acb.integral(integrand,lo,lo+1,abs_tol=arb('1e-12'),rel_tol=arb('1e-12'),eval_limit=20000)
  I+=piece
 
 central=2/arb.pi()*I.real
 # Polynomial recurrence bounds for vertical tails |t|>=20.
 S=sum(abs(arb(a))/arb(n)**3 for n,a in data['coefficients'])
 m=17;T=arb(20)
 vertical=2/arb.pi()*A**2*S*arb(3+m).gamma()**5/((5*m+1)*T**(5*m+1))
 k=4
 directory=2*arb(k+1).gamma()**5*A**k*arb(N)**(sigma-k-arb(1)/2)*zetaK.real/k
 value=central+arb(0,(vertical+directory).upper())
 
 result={'curve':'y^11=x(1-x)^2','conductor':11**11,'sign':-1,'cutoff':N,'precision_bits':ctx.prec,'A':str(A),'zeta_K_11_over_10':str(zetaK),'truncated_central_value':str(central),'vertical_contour_tail':str(vertical),'Dirichlet_coefficient_tail':str(directory),'Lprime_at_one':value.str(25, radius=True),'proved_lower_bound':'3.114','proved_upper_bound':'3.137','bounds_verified':bool(value>arb('3.114') and value<arb('3.137')),'positive':bool(value>0),'evaluation_count':seen,'seconds':time.time()-start,'local_factors':data['local_factors'],'nonzero_coefficients':data['coefficients']}
 assert value>arb('3.114') and value<arb('3.137')
 return result

if __name__=='__main__':
 parser=argparse.ArgumentParser()
 parser.add_argument('--limit',type=int,default=50000)
 parser.add_argument('--precision',type=int,default=112)
 parser.add_argument('--output',type=Path,default=BASE/'eleven_rankone_certificate.json')
 args=parser.parse_args()
 result=certificate(args.limit,args.precision)
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 for key in ['cutoff','precision_bits','zeta_K_11_over_10','truncated_central_value','vertical_contour_tail','Dirichlet_coefficient_tail','Lprime_at_one','positive']:
  print(f'{key}: {result[key]}')
