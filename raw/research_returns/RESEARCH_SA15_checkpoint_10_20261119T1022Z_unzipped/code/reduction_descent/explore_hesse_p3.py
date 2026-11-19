import sympy as S, json, time
from fractions import Fraction
pi,i=S.symbols('pi i');G=S.groebner([pi*pi+3*pi+3,i*i+1],pi,i,domain=S.QQ)
def red(a):return S.expand(G.reduce(S.expand(a))[1])
def mul(a,b):return red(a*b)
def powr(a,n):
 r=S.Integer(1)
 for _ in range(n):r=mul(r,a)
 return r
pinv=-(pi+3)/3
def vp3(q):
 q=Fraction(q)
 if not q:return 999999
 a,b=q.numerator,q.denominator;v=0
 while a%3==0:a//=3;v+=1
 while b%3==0:b//=3;v-=1
 return v
def val(a):
 pol=S.Poly(red(a),pi,i)
 return min([2*vp3(c)+powers[0] for powers,c in pol.terms()] or [999999])
def residue(a):
 assert val(a)>=0
 pol=S.Poly(red(a),pi,i); coeff=[0,0]
 for (k,j),c in pol.terms():
  if k==0:
   c=Fraction(c);assert c.denominator%3
   coeff[j]=(c.numerator*pow(c.denominator,-1,3))%3
 return tuple(coeff)
def F9mul(a,b):return((a[0]*b[0]-a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
def F9pow(a,n):
 r=(1,0)
 for _ in range(n):r=F9mul(r,a)
 return r
rows=[];start=time.monotonic()
for ca in range(3):
 for cb in [1,2]:
  c=ca+cb*i;t=1+c*pi;t3=powr(t,3);t6=powr(t,6)
  ag=mul(-3*t,t3+8);bg=2*(t6-20*t3-8)
  A=mul(ag,powr(pinv,4));B=mul(bg,powr(pinv,6))
  Bbar=residue(B);rbar=F9pow(tuple((-x)%3 for x in Bbar),3)
  rr=(rbar[0] if rbar[0]<2 else -1)+(rbar[1] if rbar[1]<2 else -1)*i
  C0=red(powr(rr,3)+mul(A,rr)+B)
  C1=red(3*powr(rr,2)+A);C2=3*rr
  rows.append(dict(c=[ca,cb],v_t3minus1=val(t3-1),v_t3plus8=val(t3+8),v_A=val(A),v_B=val(B),Bbar=Bbar,rbar=rbar,r=str(rr),v_translated_coeffs=[val(C0),val(C1),val(C2),0],C0=str(C0),A=str(A),B=str(B)))
print(json.dumps(dict(field='Q_3(i,zeta_3), i^2=-1, pi=zeta_3-1, pi^2+3pi+3=0',rows=rows,seconds=time.monotonic()-start),indent=2))
