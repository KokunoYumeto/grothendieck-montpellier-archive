#!/usr/bin/env python3
"""Exact Euler data and central-value arithmetic for the exponent-13 Prym.

Functional equation and conductor are derived in thirteen.tex.
This certificate proves the stated central-value interval, not finite Sha.
"""
from pathlib import Path
import argparse,ctypes,json,math,subprocess,tempfile,time
from flint import arb,acb,ctx,fq_default_ctx
BASE=Path(__file__).resolve().parent
temporary=tempfile.TemporaryDirectory(prefix='fermat_thirteen_')
binary=Path(temporary.name)/'counts.so'
subprocess.run(['cc','-O3','-fPIC','-shared','-x','c',str(BASE/'thirteen_counts_source.txt'),'-o',str(binary)],check=True)
lib=ctypes.CDLL(str(binary));lib.thirteen_counts.argtypes=[ctypes.c_int,ctypes.POINTER(ctypes.c_int),ctypes.POINTER(ctypes.c_int)]

def sieve(N):
 spf=list(range(N+1))
 for p in range(2,math.isqrt(N)+1):
  if spf[p]==p:
   for n in range(p*p,N+1,p):
    if spf[n]==n:spf[n]=p
 return [p for p in range(2,N+1) if spf[p]==p],spf

def count_B(p,d):
 F=fq_default_ctx(p,d,'a');total=1
 for number in range(p**d):
  digits=[]
  for _ in range(d):digits.append(number%p);number//=p
  x=F(digits)
  # w^2+w=-3t+13t^2-26t^3+26t^4-13t^5, also a good model at 2.
  g=((((-13*x+26)*x-26)*x+13)*x-3)*x
  if p==2:
   tr=sum((g**(2**j) for j in range(d)),F(0));total+=2 if tr==0 else 0
  else:
   delta=1+4*g;total+=1 if delta==0 else (2 if delta.is_square() else 0)
 return total,str(F.modulus())

def count_C(p,d):
 F=fq_default_ctx(p,d,'a');q=p**d;total=1
 assert (q-1)%13==0
 for number in range(q):
  digits=[]
  for _ in range(d):digits.append(number%p);number//=p
  x=F(digits);a=x*(1-x)**3
  total+=1 if a==0 else (13 if a**((q-1)//13)==1 else 0)
 return total,str(F.modulus())

def jacobi_poly(counts,e):
 powers=[1]+[0]*12;J=[-x for x in counts];tr=[0];poly=[1]
 for d in range(1,e+1):
  out=[0]*13
  for i,a in enumerate(powers):
   for j,b in enumerate(J):out[(i+j)%13]+=a*b
  powers=out;tr.append(13*out[0]-sum(out))
  val=-sum(poly[d-j]*tr[j] for j in range(1,d+1));assert val%d==0;poly.append(val//d)
 return poly

def coefficients(N):
 primes,spf=sieve(N);pp={};local={};counts_record=[]
 for p in primes:
  e=0;q=p
  while q<=N:e+=1;q*=p
  if p==13:
   pp[p]=[1]+[0]*e;local[p]={'P':[1]};continue
  if p==2:
   traces=[0];BP=[1]
   for d in range(1,5):
    nq,mod=count_B(p,d);counts_record.append(['B',p,d,nq,mod]);traces.append(p**d+1-nq)
    v=-sum(BP[d-j]*traces[j] for j in range(1,d+1));assert v%d==0;BP.append(v//d)
   jacobi=None
  else:
   arr=(ctypes.c_int*13)();trace=ctypes.c_int();lib.thirteen_counts(p,arr,ctypes.byref(trace));jacobi=list(arr)
   BP=[1,-trace.value]
   if e>=2:
    nq,mod=count_B(p,2);counts_record.append(['B',p,2,nq,mod]);trace2=p*p+1-nq
    v=trace.value**2-trace2;assert v%2==0;BP.extend([v//2,-p*trace.value,p*p])
  f=1;value=p%13
  while value!=1:f+=1;value=value*p%13
  if f%2==0:
   JP=[0]*13
   for j in range(12//f+1):JP[j*f]=math.comb(12//f,j)*p**(f*j//2)
  elif f==3:
   JP=[0]*13;JP[0]=1
   if e>=3:
    nq,mod=count_C(p,3);counts_record.append(['C',p,3,nq,mod]);t3=p**3+1-nq
    assert t3%3==0;JP[3]=-t3//3
    if e>=6:
     nq,mod=count_C(p,6);counts_record.append(['C',p,6,nq,mod]);t6=p**6+1-nq
     v=-JP[3]*t3-t6;assert v%6==0;JP[6]=v//6
   JP[9]=p**3*JP[3];JP[12]=p**6
  else:
   assert sum(jacobi)==p-2
   JP=jacobi_poly(jacobi,min(e,12))
  P=[1]
  for d in range(1,min(e,8)+1):
   P.append((JP[d] if d<len(JP) else 0)-sum(BP[j]*P[d-j] for j in range(1,min(d,len(BP)-1)+1)))
  inverse=[1]
  for d in range(1,e+1):inverse.append(-sum(P[j]*inverse[d-j] for j in range(1,min(d,len(P)-1)+1)))
  pp[p]=inverse;local[p]={'B_known':BP[:min(e,4)+1],'J_known':JP[:min(e,12)+1],'P_known':P,'order_mod13':f}
 a=[0]*(N+1);a[1]=1
 for n in range(2,N+1):
  p=spf[n];m=n;e=0
  while m%p==0:m//=p;e+=1
  a[n]=a[m]*pp[p][e]
 assert all(not a[n] for n in range(1,N+1) if n%13 not in (1,3,9))
 return {'local_factors':local,'nonzero_coefficients':[(n,a[n]) for n in range(1,N+1) if a[n]],'extension_counts':counts_record}

def certificate(N,precision):
 start=time.time();ctx.prec=precision;data=coefficients(N)
 B=arb(13)**4/(2*arb.pi())**4
 terms=[(arb(a)/arb(n)**3,arb(n).log()) for n,a in data['nonzero_coefficients']];logB=B.log()
 def integrand(t,analytic):
  it=acb(0,1)*t;z=2+it;S=sum((w*(-it*ln).exp() for w,ln in terms),acb(0))
  return (z+1).gamma()**4/z*B**2*(it*logB).exp()*S
 I=acb(0)
 for j in range(20):I+=acb.integral(integrand,j,j+1,abs_tol=arb('1e-13'),rel_tol=arb('1e-13'),eval_limit=30000)
 central=2/arb.pi()*I.real;S=sum(abs(w) for w,_ in terms);m=17
 vertical=2/arb.pi()*B**2*S*arb(3+m).gamma()**4/(4*m*arb(20)**(4*m))
 sigma=arb(11)/10;zeta=acb(sigma.zeta());root=acb(0,2*arb.pi()/12).exp()
 for k in (3,6,9):
  L=sum((root**(k*j)*acb(sigma).zeta(arb(pow(2,j,13))/13) for j in range(12)),acb(0))/acb(13)**sigma
  zeta*=L
 assert zeta.imag.contains(0)
 tail=2*arb(5).gamma()**4*B**4*arb(N)**(sigma-arb(9)/2)*zeta.real**2
 # This second tail needs only the universal degree-eight Weil bound.
 general=2*arb(9).gamma()**4*B**8*arb(N)**(-7)*arb(3/2).zeta()**8
 result=central+arb(0,(vertical+tail).upper())
 universal_result=central+arb(0,(vertical+general).upper())
 if N>=100000:
  assert universal_result>arb('2.632') and universal_result<arb('2.636')
 output={'N':N,'precision':precision,'conductor':13**8,'root_number':1,'gamma_power':4,'scale':str(B),'truncated':str(central),'vertical':str(vertical),'zeta_quartic':str(zeta),'CM_tail':str(tail),'universal_tail':str(general),'L_CM_interval':str(result),'L_universal_interval':str(universal_result),'universal_lower':universal_result.lower().str(40),'universal_upper':universal_result.upper().str(40),'rational_interval_verified':bool(universal_result>arb('2.632') and universal_result<arb('2.636')),'positive':bool(universal_result>0),'seconds':time.time()-start,**data}
 return output

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--limit',type=int,default=100000);parser.add_argument('--precision',type=int,default=144);parser.add_argument('--output',type=Path,default=BASE/'thirteen_certificate.json');args=parser.parse_args()
 result=certificate(args.limit,args.precision);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ('local_factors','nonzero_coefficients','extension_counts')},indent=2))
