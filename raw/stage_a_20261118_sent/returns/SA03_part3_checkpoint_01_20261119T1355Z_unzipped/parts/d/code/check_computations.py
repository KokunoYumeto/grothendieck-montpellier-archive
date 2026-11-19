"""Exact computations for cote 93 Pro scans 3–46; no scans are emended.
Run: python deliverable/parts/d/code/check_computations.py
"""
from pathlib import Path
import sympy as S
from math import comb
from fractions import Fraction
OUT=Path(__file__).resolve().parents[1]/'outputs/computations.txt'
out=[]
def say(*a): out.append(' '.join(map(str,a)))
def zero(label,expr):
    v=S.factor(expr); say(label,':',v); assert v==0,(label,v)
a1,a2,a3,a4,a6,u,r,s,t,x,y,X,Y,z,lam=S.symbols('a1 a2 a3 a4 a6 u r s t x y X Y z lambda')
def inv(A):
    a,b,c,d,e=A
    b2=a*a+4*b; b4=a*c+2*d; b6=c*c+4*e
    b8=a*a*e+4*b*e-a*c*d+b*c*c-d*d
    c4=b2*b2-24*b4; c6=-b2**3+36*b2*b4-216*b6
    D=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    d6=b2*b4-18*b6; d8=b2*b2*b4-48*b4*b4+18*b2*b6
    return dict(b2=b2,b4=b4,b6=b6,b8=b8,c4=c4,c6=c6,Delta=D,d6=d6,d8=d8)
I=inv([a1,a2,a3,a4,a6]); globals().update(I)
say('EXACT POLYNOMIAL CERTIFICATES (zero means identity, over Z)')
zero('scan7 -4b8 relation',-4*b8-(b4*b4-b2*b6))
zero('scan7 12d6 relation',12*d6-c6-b2*c4)
zero('scan7 -12d8 relation',-12*d8-c4*c4-b2*c6)
zero('scan8 two Delta expressions',Delta-(b4**3-27*b6*b6+b8*(36*b4-b2*b2)))
zero('scan4/10 invariant identity',c4**3-c6**2-1728*Delta)
F=y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6
Ap=[(a1+2*s)/u,(a2-s*a1+3*r-s*s)/u**2,(a3+r*a1+2*t)/u**3,(a4-s*a3+2*a2*r-(t+r*s)*a1+3*r*r-2*s*t)/u**4,(a6+r*a4+r*r*a2+r**3-t*a3-t*t-r*t*a1)/u**6]
Fp=Y*Y+Ap[0]*X*Y+Ap[2]*Y-X**3-Ap[1]*X*X-Ap[3]*X-Ap[4]
zero('scan8 all five coefficient transformations',F.subs({x:u*u*X+r,y:u**3*Y+s*u*u*X+t})-u**6*Fp)
zero('scan8 fourth coefficient derivative repair',Ap[3]*u**4-(-S.diff(F,x).subs({x:r,y:t})-s*S.diff(F,y).subs({x:r,y:t})))
say('scan8 literal F instead of F_r residual:',S.factor(Ap[3]*u**4-(-F.subs({x:r,y:t})-s*S.diff(F,y).subs({x:r,y:t}))))
J=inv(Ap)
expected={'b2':b2+12*r,'b4':b4+r*b2+6*r*r,'b6':b6+2*r*b4+r*r*b2+4*r**3,'b8':b8+3*r*b6+3*r*r*b4+r**3*b2+3*r**4,'d6':d6+c4*r,'d8':d8-c6*r,'c4':c4,'c6':c6,'Delta':Delta}
weights={'b2':2,'b4':4,'b6':6,'b8':8,'d6':6,'d8':8,'c4':4,'c6':6,'Delta':12}
for k,v in expected.items():zero('scan8-9 '+k+' transformation',u**weights[k]*J[k]-v)
Ishort=inv([0,0,0,a4,a6])
zero('scan9 short c4',Ishort['c4']+48*a4)
zero('scan9 short c6',Ishort['c6']+864*a6)
zero('scan9 short Delta',Ishort['Delta']+16*(4*a4**3+27*a6*a6))
Iodd=inv([0,a2,0,a4,a6]); c4o=Iodd['c4'];c6o=Iodd['c6'];Do=Iodd['Delta']
zero('scan10 discriminant',Do-16*S.discriminant(x**3+a2*x*x+a4*x+a6,x))
G=S.groebner([a2*a4-9*a6],a2,a4,a6)
for label,e in [('3.3 c6',-c6o-64*(a2**3-27*a6)),('3.3 Delta',Do-64*(-a2**3*a6-a4**3+54*a6*a6)),('3.4 first',4*a2*c4o+c6o),('3.4 second',a4*c4o*c4o+36*Do),('3.4 third',a6*c4o**3-c6o*Do)]:
    rem=G.reduce(S.expand(e))[1];zero('scan11 mod d6=0 '+label,rem)
def red(e,p):return S.Poly(S.expand(e),*sorted(e.free_symbols,key=str),modulus=p).as_expr() if e.free_symbols else int(e)%p
for p,A in [(2,[1,a2,0,0,a6]),(3,[0,0,0,a4,a6]),(2,[0,0,a3,a4,a6])]:
    vals=inv(A); say('scans12-13 chart',p,A,{k:str(red(vals[k],p)) for k in ['c4','c6','Delta']})
zero('scan12 involution equation in char2 (divisible by 2)',red(F.subs({a1:1,a3:0,a4:0,y:y+x})-F.subs({a1:1,a3:0,a4:0}),2))
L=inv([0,-(1+lam),0,lam,0]);jleg=256*(1-lam+lam**2)**3/(lam*(1-lam))**2
zero('scan4 Legendre j',L['c4']**3/L['Delta']-jleg)
orbit=[lam,1-lam,1/lam,1-1/lam,1/(1-lam),1/(1-1/lam)]
for k,q in enumerate(orbit,1):zero('scan4 j under orbit map '+str(k),jleg.subs(lam,q)-jleg)
say('scan4 doubtful negative sixth map residual:',S.factor(jleg.subs(lam,-1/(1-1/lam))-jleg))
for p in [3,5,7,11,13,17,19,23,29,31]:
    n=(p-1)//2
    h=sum((-1)**n*comb(n,i)**2*lam**i for i in range(n+1))
    coeff=S.Poly((x*(x-1)*(x-lam))**n,x).coeff_monomial(x**(p-1))
    zero('scan4 Legendre Hasse coefficient p='+str(p),coeff-h)
say('General coefficient proof: to obtain x^(2n) from x^n(x-1)^n(x-lambda)^n, choose exponents i and n-i; signs multiply to (-1)^n and binomial coefficients to binom(n,i)^2.')
for label,A,p in [('equal char 3',[0,t,0,-1,0],3),('equal char 2',[t,0,1,0,0],2),('mixed char 3',[0,0,0,1,1],3),('mixed char 2',[2,0,1,0,0],2)]:
    v=inv(A)
    if 'equal' in label:
        cv=red(v['c4'],p);dv=red(v['Delta'],p)
        say('scan18',label,'c4=',cv,'Delta=',dv,'j=',S.factor(cv**3/dv))
    else:
        jj=Fraction(int(v['c4']**3),int(v['Delta'])); n=jj.numerator;d=jj.denominator;val=0
        while n%p==0 and n:val+=1;n//=p
        while d%p==0 and d:val-=1;d//=p
        assert int(v['Delta'])%p!=0
        say('scan18',label,'Delta=',v['Delta'],'j=',jj,'valuation=',val,'good reduction=true')
# Finite field F4 = F2[w]/(w²+w+1), exact arithmetic as two-bit integers.
def fadd(a,b):return a^b
def fmul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return c
def fpow(a,n):
    q=1
    for _ in range(n):q=fmul(q,a)
    return q
els=[(v,h,k) for v in [1,2,3] for h in range(4) for k in range(4) if fadd(fmul(k,k),k)==fpow(h,3)]
def mul(a,b):
    U,H,K=a;u_,h,k=b
    return(fmul(U,u_),fadd(H,fmul(U,h)),fadd(fadd(K,fmul(fpow(U,3),k)),fmul(H,fmul(fpow(U,2),fpow(h,2)))))
one=(1,0,0)
def order(a):
    r_=one
    for n in range(1,25):
        r_=mul(r_,a)
        if r_==one:return n
assert len(els)==24 and all(mul(a,b) in els for a in els for b in els)
assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a in els for b in els for c in els)
kernel=[a for a in els if a[0]==1]
from collections import Counter
say('scans18-22 F4 automorphism enumeration: order',len(els),'orders',dict(sorted(Counter(map(order,els)).items())))
say('kernel(u) order',len(kernel),'orders',dict(sorted(Counter(map(order,kernel)).items())),'noncommutative',any(mul(a,b)!=mul(b,a) for a in kernel for b in kernel))
say('central involution',(1,0,1),'central',all(mul((1,0,1),a)==mul(a,(1,0,1)) for a in els),'splitting element',(2,0,0),'order',order((2,0,0)))
say('Conclusion: kernel is Q8 (nonabelian order 8, unique involution); u quotient C3 splits, so full group Q8 semidirect C3. No claim about faithfulness of a deformation action is inferred.')
U,R,H,K=S.symbols('U R H K')
xcomp=S.expand(U**2*(u**2*X+r)+R)
ycomp=S.expand(U**3*(u**3*Y+s*u**2*X+t)+H*U**2*(u**2*X+r)+K)
zero('scan22 corrected composition x',xcomp-((U*u)**2*X+R+U**2*r))
zero('scan22 corrected composition y',ycomp-((U*u)**3*Y+(H+U*s)*(U*u)**2*X+K+U**3*t+H*U**2*r))
say('Composition outer (U,R,H,K) after inner (u,r,s,t): (Uu, R+U²r, H+Us, K+U³t+HU²r). The source middle t′ must be checked against s′.')
f=S.Function('f')(z)
def schwarz(h):return S.diff(h,z,3)/S.diff(h,z)-S.Rational(3,2)*(S.diff(h,z,2)/S.diff(h,z))**2
zero('scan36 exponential Schwarzian correction',-2*schwarz(S.exp(f))+2*schwarz(f)-S.diff(f,z)**2)
zero('scan36 exponential test',-2*schwarz(S.exp(z))-1)
y1=S.Function('y1')(z);y2=S.Function('y2')(z);q=S.Function('q')(z)
expr=schwarz(y1/y2)-2*q
sub={}
for h in [y1,y2]:sub[S.diff(h,z,3)]=-S.diff(q,z)*h-q*S.diff(h,z);sub[S.diff(h,z,2)]=-q*h
zero('ratio-of-solutions S(y1/y2)=2q',expr.subs(sub))
for p in [3,5,7,11,13,17,19,23,29,31]:
    A=S.Matrix([[0,1],[pow(4,-1,p),0]])
    Ap=A**p
    assert all(int(v)%p==0 for v in Ap-A)
    det=int((-A).det())%p;assert det
    say('scan36 arithmetic counterexample p=',p,'p-curvature=-A; determinant=',det,'non-nilpotent=true')
say('D^[p]=0 on Fp(z): D^p is a derivation, annihilates z and constants, hence the rational function field. Constant A commutes with D; (D-A)^p=-A^p=-A.')
say('scan19 disconnected-base counterexample: sign choices on 2 components = 2² =',2**2)
say('scan24 graded obstruction: nonnegative combinations of 4,6,12 contain neither 1 nor 2; mod-p rings contain a1(weight1), b2(weight2).')
say('scan43 cancellation proof: Fq=pz => p q=VFq=pVz => q=Vz if Q is p-torsion-free. Symmetrically ker Vbar=im Fbar. This proves exactness, not local freeness.')
say('scan43 node: in k[x,y]/(xy), ann(y)=(x), ann(x)=(y); hence alternating x,y complex exact; (y) is nonzero with nonzero annihilator at (x,y), so not free or split in that local ring.')
say('scan44 Frobenius example: epsilon²=0 => epsilon^p=0 for every p>=2; lines span(1,0), span(1,epsilon) are distinct direct summands but have equal Frobenius pullbacks.')
say('scan45 Hodge tangent rank: rank Hom(F,H/F)=g*(2g-g)=g²; for g=1 rank=1. This is conditional on a fixed ambient lift.')
OUT.write_text('\n'.join(out)+'\n'); print('\n'.join(out))
