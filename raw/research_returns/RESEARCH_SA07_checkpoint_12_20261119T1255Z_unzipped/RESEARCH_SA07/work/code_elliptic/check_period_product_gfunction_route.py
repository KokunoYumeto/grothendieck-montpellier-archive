#!/usr/bin/env python3
"""Exact identities for the actual two-period product and a G-function counterexample."""
import datetime,hashlib,json,pathlib,time
import sympy as s
start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.perf_counter()
m,delta,K,L,E,F=s.symbols('m delta K L E F',nonzero=True)
p=(1-2*m)/(m*(1-m));q=-1/(4*m*(1-m))
kprime=(E-(1-m)*K)/(2*m*(1-m))
lprime=-(F-m*L)/(2*m*(1-m))
r=s.cancel(kprime/K+lprime/L)
h=delta*s.Rational(1,2)*(E/K-F/L+(2*m-1)/3)
assert s.cancel(h-delta*(m*(1-m)*r-(2*m-1)/3))==0
# Generic symmetric-square equation, derived directly from y''=-p*y'-q*y.
y,z,yp,zp,P,Q,Pp,Qp=s.symbols('y z yp zp P Q Pp Qp')
def D(f):
 return s.expand(s.diff(f,y)*yp+s.diff(f,z)*zp+s.diff(f,yp)*(-P*yp-Q*y)+s.diff(f,zp)*(-P*zp-Q*z)+s.diff(f,P)*Pp+s.diff(f,Q)*Qp)
u=y*z;u1=D(u);u2=D(u1);u3=D(u2)
assert s.expand(u3+3*P*u2+(Pp+4*Q+2*P**2)*u1+(2*Qp+4*P*Q)*u)==0
assert s.expand(u1**2-2*u*u2-2*P*u*u1-4*Q*u**2-(y*zp-yp*z)**2)==0
coeff=[s.cancel(a*m**2*(1-m)**2) for a in [1,3*p,s.diff(p,m)+4*q+2*p**2,2*s.diff(q,m)+4*p*q]]
# Exact Wronskian from Legendre's E*Kc+Ec*K-K*Kc=pi/2.
pi=s.symbols('pi')
W=s.cancel(K*lprime-kprime*L)
assert s.cancel(W.subs(F,(pi/2+K*L-E*L)/K)+pi/(4*m*(1-m)))==0
# Actual normalized first two jets from h and c.
a,c=s.symbols('a c')
rh=(a/delta+(2*m-1)/3)/(m*(1-m))
second=s.cancel((rh**2-2*p*rh-4*q-c**2/(delta**2*m**2*(1-m)**2))/2)
assert s.cancel(s.diff(second,c,2)+1/(delta**2*m**2*(1-m)**2))==0
# Exact counterexample: G=1+2log(1-2Mz)-log(1-3Mz).
x,M=s.symbols('x M',positive=True)
R=s.cancel(-4*M/(1-2*M*x)+3*M/(1-3*M*x))
assert s.cancel(R.subs(x,1/(4*M))-4*M)==0
assert s.cancel(((1-2*M*x)**2/(1-3*M*x)).subs(x,1/(4*M))-1)==0
assert s.residue(R,x,1/(2*M))==2
assert s.residue(R,x,1/(3*M))==-1
G=1+2*s.log(1-2*M*x)-s.log(1-3*M*x)
for n in range(1,13):
 assert s.expand(s.diff(G,x,n).subs(x,0)/s.factorial(n)-(3**n-2**(n+1))*M**n/n)==0
record={'start_utc':start,'elapsed_seconds':time.perf_counter()-tick,
 'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 'input':'symbolic m,delta,K,Kc,E,Ec; independent ODE jets; G_M(z)=1+2log(1-2Mz)-log(1-3Mz)',
 'symmetric_square_coefficients':[str(s.factor(v)) for v in coeff],
 'h':'delta*(m*(1-m)*Fprime/F-(2*m-1)/3)',
 'normalized_second_jet':str(s.factor(second)),
 'counterexample_point':'z=1/(4M): G_M=1, G_Mprime=4M; ordinary point inside radius1/(3M)',
 'counterexample_residues':[2,-1],'taylor_coefficients_checked':12,
 'status':'PASS'}
print(json.dumps(record,indent=2));pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
