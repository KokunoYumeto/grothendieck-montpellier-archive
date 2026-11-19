"""Reproducible algebra and analytic spot checks for SA16 cote62.
Exact symbolic zero certificates are proofs of the displayed rational identities.
Numerical checks are evidence at the specified arguments, never universal proofs.
"""
from pathlib import Path
import sympy as s
import mpmath as m
import json
P=Path(__file__).resolve().parents[1]
out=[]
def emit(name,value,kind='exact symbolic certificate'):
    row=dict(name=name,kind=kind,value=str(value));out.append(row);print(name+': '+str(value))
def zero(name,expr):
    v=s.factor(expr); assert v==0,(name,v);emit(name,v)
x,a,b,c,t,k,z,h=s.symbols('x a b c t k z h')
F=(t+1)*(2*t-1)*(t-2); Q=t*t-t+1
i=-F**2/(27*t*t*(t-1)**2)
disc=s.discriminant(x**3+b*x+c,x)
emit('cubic discriminant',disc)
emit('resultant f,fprime',s.resultant(x**3+b*x+c,3*x*x+b,x))
emit('literal b^3-27c^2 versus true discriminant at b=1,c=0',(1,-4))
depressed=s.expand((x-a/3)**3+a*(x-a/3)**2+b*(x-a/3)+c)
emit('depression',depressed)
da=s.discriminant(x**3+a*x*x+b*x+c,x)
bb=b-a*a/3; cc=c-a*b/3+2*a**3/27
zero('general i=1-j/1728',(27*c+2*a**3-9*a*b)**2/(-27*da)-(1-4*bb**3/(4*bb**3+27*cc**2)))
emit('4x^3-h(x+1) discriminant',s.factor(s.discriminant(4*x**3-h*(x+1),x)))
zero('1-i=4Q^3/(27t^2(t-1)^2)',1-i-4*Q**3/(27*t*t*(t-1)**2))
maps={'id':t,'a':1-t,'b':1/t,'c':t/(t-1),'d':1/(1-t),'e':(t-1)/t}
for name,u in maps.items(): zero('S3 invariant '+name,i.subs(t,u)-i)
table={name:{name2:next(q for q,w in maps.items() if s.factor(v.subs(t,u)-w)==0) for name2,v in maps.items()} for name,u in maps.items()}
emit('S3 table: row first, column second',json.dumps(table,sort_keys=True))
sig=(t-2)/(2*t-1)
zero('sigma involution',sig.subs(t,sig)-t)
zero('sigma centralizes 1-t',sig.subs(t,1-t)-(1-sig))
zero('sigma centralizes 1/t',sig.subs(t,1/t)-1/sig)
zero('sigma sends i to 1/i',i.subs(t,sig)-1/i)
emit('sigma determinant and square',(s.Matrix([[1,-2],[2,-1]]).det(),s.Matrix([[1,-2],[2,-1]])**2))
emit('harmonic images',[s.limit(sig,t,v) if v==s.oo else s.factor(sig.subs(t,v)) for v in [0,1,s.oo]])
f=F/(3*s.sqrt(-3)*t*(t-1))
emit('cyclic quotient derivative',s.factor(s.diff(f,t)))
zero('cyclic quotient square',f*f-i)
zero('sigma cyclic reciprocal',f.subs(t,sig)-1/f)
rr=F/(t*(t-1))
zero('sign cover alternating a',rr.subs(t,1-t)+rr)
zero('sign cover alternating b',rr.subs(t,1/t)+rr)
zero('sign cover r^2=-27i',rr*rr+27*i)
emit('i at -1+epsilon',s.series(i.subs(t,-1+z),z,0,4))
rho=(1+s.sqrt(-3))/2
emit('1-i vanishing at cyclotomic root',s.simplify((1-i).subs(t,rho)))
emit('cyclotomic first derivatives',[s.simplify(s.diff(i,t,n).subs(t,rho)) for n in [1,2]])
emit('cyclotomic Q(-1+eps) not relevant; Q(rho+eps)',s.expand(Q.subs(t,rho+z)))
emit('degree-two filtration counterexample p=q=0,n=1','(1,1) belongs to A_0E x A_0F, not A_1(E x F), A=k[[u]]',kind='explicit counterexample')
u,lam,mu=s.symbols('u lam mu',nonzero=True)
emit('weight relation remainder',s.rem(mu**2-lam**3,mu-lam*u,mu))
for n in [2,3,4,5]: emit('pole derivative n='+str(n),s.diff(z**(-n),z))
W=s.symbols('W')
R=(12*W-(5-k*k))/(12*W-(5*k*k-1))
roots=[(1+k*k)/6,-(k*k+6*k+1)/12,-(k*k-6*k+1)/12]
weier=4*s.prod(W-e for e in roots)
zero('scan66 Mobius sn ODE',s.diff(R,W)**2*weier-(1-R*R)*(1-k*k*R*R))
zero('scan66 initial value',R.subs(W,(5-k*k)/12))
zero('scan66 initial derivative',s.diff(R,W).subs(W,(5-k*k)/12)*(1-k*k)/2-1)
e1,e2=s.symbols('e1 e2');e3=-e1-e2;D=(e1-e2)*(e1-e3)
Ppoly=4*(W-e1)*(W-e2)*(W-e3)
Wh=e1+D/(W-e1)
zero('halfperiod translation ODE',s.diff(Wh,W)**2*Ppoly-4*(Wh-e1)*(Wh-e2)*(Wh-e3))
zero('halfperiod product',(W-e1)*(Wh-e1)-D)
q2,q3,q4=s.symbols('q2 q3 q4')
# Differential recurrence for wp = z^-2 + c1 z²+c2 z⁴+c3 z⁶+c4 z⁸.
c1,c2,c3,c4=s.symbols('c1 c2 c3 c4')
wp=z**-2+c1*z*z+c2*z**4+c3*z**6+c4*z**8
ode=s.expand(s.diff(wp,z,2)-6*wp*wp+10*c1)
sol=s.solve([ode.coeff(z,4),ode.coeff(z,6)],[c3,c4]);emit('wp coefficient recurrence',sol)
zeta=1/z-c1*z**3/3-c2*z**5/5
sigma=s.series(z*s.exp(-c1*z**4/12-c2*z**6/30),z,0,9)
emit('sigma series',sigma)
cj=s.symbols('d3 d5 d7 d9'); sn=z+sum(cj[j]*z**(2*j+3) for j in range(4))
eq=s.expand(s.diff(sn,z,2)+(1+k*k)*sn-2*k*k*sn**3)
ss={}
for j,coeff in enumerate(cj):ss[coeff]=s.factor(s.solve(eq.coeff(z,2*j+1).subs(ss),coeff)[0])
emit('sn coefficients through z9',ss)
# Noetherianity/valuation claims are proved in proof_checks.md, not inferred from tests.
m.mp.dps=60
tau=m.mpc('0.27','1.13');w1=m.mpf('0.8');w2=tau*w1; nome=m.exp(m.pi*1j*tau)
th=lambda v,ta=tau:m.jtheta(1,m.pi*v,m.exp(m.pi*1j*ta))
thp=lambda ta=tau:m.diff(lambda v:th(v,ta),0)
eta=-m.diff(lambda v:th(v),0,3)/(12*w1*thp())
sigma=lambda v:2*w1/thp()*m.exp(eta*v*v/(2*w1))*th(v/(2*w1))
zet=lambda v:m.diff(lambda vv:m.log(sigma(vv)),v)
wpn=lambda v:-m.diff(zet,v)
wpprime=lambda v:m.diff(wpn,v)
def approx(name,error,tol=m.mpf('1e-45')):
    e=abs(error); assert e<tol,(name,m.nstr(e,9));emit(name,m.nstr(e,12),kind='60-digit numerical check; absolute residual')
v=m.mpc('.231','.147');v2=m.mpc('.319','-.089')
approx('sigma odd',sigma(-v)+sigma(v))
approx('zeta odd',zet(-v)+zet(v))
approx('sigma 2w1 quasiperiod',sigma(v+2*w1)+m.exp(2*eta*(v+w1))*sigma(v))
eta2=(eta*w2-m.pi*1j/2)/w1
approx('sigma 2w2 quasiperiod',sigma(v+2*w2)+m.exp(2*eta2*(v+w2))*sigma(v))
approx('wp periodic',wpn(v+2*w1)-wpn(v))
approx('sigma addition',wpn(v)-wpn(v2)+sigma(v+v2)*sigma(v-v2)/(sigma(v)**2*sigma(v2)**2))
approx('zeta addition',zet(v+v2)-zet(v)-zet(v2)-(wpprime(v)-wpprime(v2))/(2*(wpn(v)-wpn(v2))))
approx('wp addition',wpn(v+v2)+wpn(v)+wpn(v2)-(wpprime(v)-wpprime(v2))**2/(4*(wpn(v)-wpn(v2))**2))
approx('wp duplication',wpn(2*v)+2*wpn(v)-(m.diff(wpn,v,2)/(2*wpprime(v)))**2)
approx('four halfperiod translates',4*wpn(2*v)-sum(wpn(v+w) for w in [0,w1,w2,w1+w2]))
approx('theta quasi 1',th(v+1)+th(v))
approx('theta quasi tau',th(v+tau)+m.exp(-m.pi*1j*(2*v+tau))*th(v))
approx('theta modular S',th(v)-1j*m.sqrt(1j/tau)*m.exp(-m.pi*1j*v*v/tau)*th(v/tau,-1/tau))
approx('theta heat',m.diff(th,v,2)-4*m.pi*1j*m.diff(lambda ta:th(v,ta),tau))
aa=m.mpc('1.4','.2');bb=m.mpc('.3','-.1');cc=m.mpf('.4')
gauss=sum(m.exp(-aa*n*n+bb*n+cc) for n in range(-25,26))
approx('scan87 Gaussian identity literal is correct',gauss+m.exp(cc+bb/2-aa/4)*th((bb-aa-m.pi*1j)/(2*m.pi*1j),1j*aa/m.pi))
even=[m.jtheta(j,0,nome) for j in [2,4,3]]
approx('Jacobi theta derivative',thp()-m.pi*m.fprod(even))
rootvals=[wpn(w1),wpn(w2),wpn(w1+w2)]
rootform=[(m.pi/(2*w1))**2*(even[1]**4+even[2]**4)/3,-(m.pi/(2*w1))**2*(even[0]**4+even[2]**4)/3,(m.pi/(2*w1))**2*(even[0]**4-even[1]**4)/3]
for j in range(3):approx('theta halfperiod root '+str(j+1),rootvals[j]-rootform[j])
kk=m.mpf('.61');param=kk*kk;K=m.ellipk(param);Kp=m.ellipk(1-param)
snf=lambda u:m.ellipfun('sn',u,param);cnf=lambda u:m.ellipfun('cn',u,param);dnf=lambda u:m.ellipfun('dn',u,param)
for nm,ff in [('sn',snf),('cn',cnf),('dn',dnf)]:
    approx(nm+' common 4K period',ff(v+4*K)-ff(v));approx(nm+' common 4iKprime period',ff(v+4j*Kp)-ff(v))
approx('sn own 2iKprime period',snf(v+2j*Kp)-snf(v))
approx('cn 2iKprime antiperiod',cnf(v+2j*Kp)+cnf(v))
approx('dn 2K period',dnf(v+2*K)-dnf(v))
approx('dn 2iKprime antiperiod',dnf(v+2j*Kp)+dnf(v))
approx('sn derivative',m.diff(snf,v)-cnf(v)*dnf(v))
approx('cn derivative',m.diff(cnf,v)+snf(v)*dnf(v))
approx('dn derivative',m.diff(dnf,v)+param*snf(v)*cnf(v))
approx('Jacobi squares',snf(v)**2+cnf(v)**2-1)
approx('Jacobi weighted squares',param*snf(v)**2+dnf(v)**2-1)
den=1-param*snf(v)**2*snf(v2)**2
approx('sn addition',snf(v+v2)-(snf(v)*cnf(v2)*dnf(v2)+snf(v2)*cnf(v)*dnf(v))/den)
approx('cn addition',cnf(v+v2)-(cnf(v)*cnf(v2)-snf(v)*snf(v2)*dnf(v)*dnf(v2))/den)
approx('dn addition',dnf(v+v2)-(dnf(v)*dnf(v2)-param*snf(v)*snf(v2)*cnf(v)*cnf(v2))/den)
approx('sn shift K',snf(v+K)-cnf(v)/dnf(v))
approx('cn shift K',cnf(v+K)+m.sqrt(1-param)*snf(v)/dnf(v))
approx('dn shift K',dnf(v+K)-m.sqrt(1-param)/dnf(v))
approx('sn shift iKprime',snf(v+1j*Kp)-1/(kk*snf(v)))
approx('cn shift iKprime',cnf(v+1j*Kp)+1j*dnf(v)/(kk*snf(v)))
approx('dn shift iKprime',dnf(v+1j*Kp)+1j*cnf(v)/snf(v))
approx('sn imaginary transform',snf(1j*v)-1j*m.ellipfun('sn',v,1-param)/m.ellipfun('cn',v,1-param))
approx('cn imaginary transform',cnf(1j*v)-1/m.ellipfun('cn',v,1-param))
approx('dn imaginary transform',dnf(1j*v)-m.ellipfun('dn',v,1-param)/m.ellipfun('cn',v,1-param))
emit('dn at k=1,z=0 versus literal1/tanh',('dn(0,1)=1','1/tanh(0) undefined'),kind='counterexample from initial values')
T=m.mpc('.5','1');emit('nome reduction counterexample',(m.re(T),m.re(1/T)),kind='explicit numerical counterexample; exact values 1/2,2/5')
emit('universal two-transform nome bound false','equianharmonic tau=(1+i sqrt3)/2 has reduced height sqrt3/2<1',kind='exact counterexample')
# Exact fibre polynomial and all displayed Jacobi Taylor/shift/theta tables.
y=s.symbols('y')
num=s.factor(s.together(i.subs(t,y)-i))
emit('anharmonic equal-invariant difference factorization',num)
zero('fibre factors at each of six images',s.prod([s.factor(s.together(i.subs(t,u)-i)) for u in maps.values()]))
snseries=s.expand(sn.subs(ss));cnseries=s.series(s.sqrt(1-snseries**2),z,0,8).removeO().expand();dnseries=s.series(s.sqrt(1-k*k*snseries**2),z,0,8).removeO().expand()
emit('cn Taylor through z6',cnseries);emit('dn Taylor through z6',dnseries)
zero('cn displayed coefficients',cnseries-(1-z*z/2+(1+4*k*k)*z**4/24-(1+44*k*k+16*k**4)*z**6/720))
zero('dn displayed coefficients',dnseries-(1-k*k*z*z/2+k*k*(4+k*k)*z**4/24-k*k*(16+44*k*k+k**4)*z**6/720))
alpha=(k+1/k)/2
zero('sn alpha z7 coefficient',ss[cj[2]]+8*k**3*(alpha**3+33*alpha)/s.factorial(7))
Kpp=-K-1j*Kp;kp=m.sqrt(1-param)
for nm,ff,sign in [('sn',snf,-1),('cn',cnf,1),('dn',dnf,-1)]:approx(nm+' shift 2Kdoubleprime',ff(v+2*Kpp)-sign*ff(v))
approx('sn shift Kdoubleprime',snf(v+Kpp)+dnf(v)/(kk*cnf(v)))
approx('cn shift Kdoubleprime',cnf(v+Kpp)+1j*kp/(kk*cnf(v)))
emit('literal scan95 dn shift Kdoubleprime residual',m.nstr(abs(dnf(v+Kpp)-1j*kp*snf(v)/cnf(v)),20),kind='60-digit countercheck; source sign fails')
approx('corrected dn shift Kdoubleprime',dnf(v+Kpp)+1j*kp*snf(v)/cnf(v))
points=[0,K,2*K,3*K,2j*Kp,Kpp,2*Kpp,3*Kpp]
expect={'sn':[0,1,0,-1,0,-1/kk,0,1/kk],'cn':[1,0,-1,0,-1,-1j*kp/kk,1,-1j*kp/kk],'dn':[1,kp,1,kp,-1,0,-1,0]}
for nm,ff in [('sn',snf),('cn',cnf),('dn',dnf)]:
    for j,point in enumerate(points):approx(nm+' special table column '+str(j),ff(point)-expect[nm][j])
qjac=m.exp(-m.pi*Kp/K);arg=m.pi*v/(2*K)
ratios=[m.jtheta(3,0,qjac)/m.jtheta(2,0,qjac)*m.jtheta(1,arg,qjac)/m.jtheta(4,arg,qjac),m.jtheta(4,0,qjac)/m.jtheta(2,0,qjac)*m.jtheta(2,arg,qjac)/m.jtheta(4,arg,qjac),m.jtheta(4,0,qjac)/m.jtheta(3,0,qjac)*m.jtheta(3,arg,qjac)/m.jtheta(4,arg,qjac)]
for j,(nm,ff) in enumerate([('sn',snf),('cn',cnf),('dn',dnf)]):approx(nm+' theta quotient',ff(v)-ratios[j])
# Residue extraction is a numerical limit, not a symbolic certificate.
eps=m.mpf('1e-24')
for nm,ff,res in [('sn',snf,1/kk),('cn',cnf,-1j/kk),('dn',dnf,-1j)]:approx(nm+' residue at iKprime',eps*ff(1j*Kp+eps)-res,m.mpf('1e-35'))
# Full Weierstrass discriminant formula, checked by completing the square.
a1,a2,a3,a4,a6=s.symbols('a1 a2 a3 a4 a6')
b2=a1*a1+4*a2;b4=a1*a3+2*a4;b6=a3*a3+4*a6;b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
Delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
zero('general Weierstrass discriminant',s.discriminant(4*x**3+b2*x*x+2*b4*x+b6,x)-16*Delta)
emit('general Weierstrass discriminant polynomial',s.expand(Delta))
# Relative centralizer: these identities are over Z, with 2 and3 inverted in P2.
ma,mb,mc,md=s.symbols('ma mb mc md')
MM=s.Matrix([[ma,mb],[mc,md]])
PP=s.Matrix([[-1,1],[0,1]]);RR=s.Matrix([[0,1],[1,0]])
JJ=s.Matrix([[1,-2],[2,-1]])
emit('relative centralizer commutator equations',list(MM*PP-PP*MM)+list(MM*RR-RR*MM))
emit('relative centralizer anticommutator equations',list(MM*PP+PP*MM)+list(MM*RR+RR*MM))
zero('trace PR equals1',s.trace(PP*RR)-1)
zero('relative involution determinant equals3',JJ.det()-3)
for ix,val in enumerate(list(JJ*PP+PP*JJ)+list(JJ*RR+RR*JJ)):
    zero('relative anticommutator J entry '+str(ix),val)
for ix,val in enumerate(list(JJ*JJ+3*s.eye(2))):
    zero('relative involution square entry '+str(ix),val)
(P/'outputs/math_checks.json').write_text(json.dumps(out,indent=2)+'\n')
(P/'outputs/math_checks.txt').write_text('\n'.join(r['name']+': '+r['value']+' ['+r['kind']+']' for r in out)+'\n')
