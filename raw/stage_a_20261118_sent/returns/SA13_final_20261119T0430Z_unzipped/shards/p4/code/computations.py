"""Exact arithmetic checks for p4. Finite examples illustrate, not prove,
the general geometric theorems. General arguments are in proof_audit.md.
Only Python standard-library exact integers/Fractions are used.
"""
from fractions import Fraction as F
from math import gcd, comb, factorial
from functools import reduce
from itertools import product

def add(a,b,L=None,mod=None):
 L=L or max(len(a),len(b));r=[(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(L)]
 return [x%mod for x in r] if mod else r
def scale(a,c,mod=None):return [(x*c)%mod if mod else x*c for x in a]
def mul(a,b,L,mod=None):
 r=[0]*L
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   if i+j<L:r[i+j]+=x*y
 return [x%mod for x in r] if mod else r
def power(a,n,L,mod=None):
 r=[1]+[0]*(L-1)
 for _ in range(n):r=mul(r,a,L,mod)
 return r
def deriv(a):return [i*a[i] for i in range(1,len(a))]
def hasse(a,n):return [comb(i,n)*a[i] for i in range(n,len(a))]
def compose(a,b,L,mod=None):
 r=[0]*L;bn=[1]+[0]*(L-1)
 for x in a:r=add(r,scale(bn,x,mod),L,mod);bn=mul(bn,b,L,mod)
 return r
def inv(a,L,mod=None):
 a0=pow(int(a[0]),-1,mod) if mod else F(1,a[0]);r=[a0]
 for n in range(1,L):
  v=-a0*sum((a[j] if j<len(a) else 0)*r[n-j] for j in range(1,n+1))
  r.append(v%mod if mod else v)
 return r
def show(a):return '['+', '.join(str(x) for x in a)+']'
def matmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

print('P4 exact computations, 2026-11-19; finite tests are labelled as such.')
print('\n1. Reynolds identity for the sign action, an illustrative representation')
E=lambda a:[x if i%2==0 else 0 for i,x in enumerate(a)]
r=[1,0,1];f=[2,3,4,5]
assert E(mul(r,f,6))==mul(r,E(f),6)
print('E((1+x²)(2+3x+4x²+5x³)) = (1+x²)E(f) =',show(E(mul(r,f,6))))

print('\n2. Quadratic identity and Picard exponents')
for u,v in product(range(-5,6),repeat=2):assert (u+v)**2+(u-v)**2==2*(u*u+v*v)
u,v=1,0
print('Literal minus identity at (u,v)=(1,0): LHS=',(u+v)**2-(u-v)**2,'RHS=',2*(u*u+v*v))
assert (u+v)**2-(u-v)**2!=2*(u*u+v*v)
for n in range(-10,11):assert n*(n+1)//2+n*(n-1)//2==n*n
print('n(n+1)/2+n(n−1)/2=n² checked on −10..10; algebraic proof in audit.')

print('\n3. Haar avoidance counterexample')
U={0,-2,2};V={0,-3,3};meets=lambda W:{z for z in W if z%2==0}
avoid=lambda W:meets(W)=={0}
print('H=2Z; U=',sorted(U),'V=',sorted(V),'avoidU=',avoid(U),'avoidV=',avoid(V),'avoid(U∩V)=',avoid(U&V))
assert (avoid(U) and avoid(V))!=avoid(U&V)
assert (avoid(U) and avoid(V))==avoid(U|V)

print('\n4. Multiplicities, cyclic tensors, torsion quotients and towers')
d=[2,3];mu=[1,2]
print('gcd(mu_i*d_i)=',reduce(gcd,[a*b for a,b in zip(d,mu)]),'gcd(d_i)*gcd(mu_i)=',reduce(gcd,d)*reduce(gcd,mu))
assert reduce(gcd,[a*b for a,b in zip(d,mu)])!=reduce(gcd,d)*reduce(gcd,mu)
for ds in ([2,4],[2,3],[6,10,14],[3,6,12]):print('tors(Z^r/Zd), d=',ds,': Z/',reduce(gcd,ds))
for e,l in ((4,2),(8,2),(9,3),(12,2),(18,3),(12,5)):
 v=0;m=e
 while m%l==0:v+=1;m//=l
 order=l**v
 assert gcd(e,l**20)==order
 print('e=',e,'ell=',l,'tensor order=',order)
delta=set(range(4));sub={0,2};tors={x for x in delta if 2*x%4==0};subtors=tors&sub
image={x%2 for x in tors};qtors={0,1}
assert image=={0} and len(qtors)==2
print('δ=Z/4,δ′={0,2},n=2: δ[n]/δ′[n] has order',len(tors)//len(subtors),'whereas δ″[n] has order',len(qtors))
for p in (2,3,5):
 ident=[seq for seq in product(range(p),repeat=4) if all(seq[i]==seq[i+1] for i in range(3))]
 timesp=[seq for seq in product(range(p),repeat=4) if all(seq[i]==p*seq[i+1]%p for i in range(3))]
 assert len(ident)==p and all(seq[:3]==(0,0,0) for seq in timesp)
 print('Z/',p,'length4 towers: identity permits',len(ident),'constant choices; ×p forces first3 coordinates0 (last is a finite-truncation boundary).')
print('Infinite-tower proof: x_i=p^N x_(i+N)=0 once p^N annihilates all terms.')

print('\n5. Frobenius spectral separation and finite torsion pairing')
for q in (2,3,5,7):
 # Toy source eigenvalues q² and q³; they only illustrate disjoint spectrum.
 A=[[q*q,1],[0,q*q]]
 # For each row-vector B, BA=qB forces B=0; coefficient determinant nonzero.
 det=(q*q-q)**2
 assert det!=0
 print('q=',q,'Jordan source eigenvalue q², target q: intertwiner coefficient determinant=',det)
print('General q^(3/2) versus q proof uses absolute values and coprime annihilators, not this toy matrix.')
for n in (2,3,4,5,8):
 pairing=lambda a,b:(a[0]*b[1]-a[1]*b[0])%n
 assert pairing((1,0),(0,1))==1
 print('Nonzero symplectic torsion pairing modulo',n,': e1,e2 ↦1')

print('\n6. Weighted lattices and discriminant pairing')
D=[[1,0],[0,2]];u=[[-2,2],[1,-1]];M=[[-2,2],[2,-2]]
assert matmul(D,u)==M and M==list(map(list,zip(*M)))
assert matmul(u,[[1],[1]])==[[0],[0]]
assert matmul([[1,2]],u)==[[0,0]]
print('D=',D,'u=',u,'D u=symmetric intersection M=',M)
print('E=Z²/Z(1,1), E*=ker(1,2), generator(-2,1): pairing with[e1]=−2, so weighted duality has index2.')
for m in range(2,10):
 b=lambda a,c:F(-a*c,m)%1
 chars={tuple(b(a,c) for c in range(m)) for a in range(m)}
 assert len(chars)==m
 for a,c,z in product(range(m),repeat=3):
  assert b(a,c)==b(c,a)
  assert b((a+z)%m,c)==(b(a,c)+b(z,c))%1
 print('u=[−',m,']: discriminant pairing −ab/',m,' has',len(chars),'distinct characters (perfect).',sep='')

print('\n7. Formal ODE, Hasse, inverse, implicit and BCH checks')
L=16;x=[0,1]+[0]*(L-2)
exp=[F(1,factorial(i)) for i in range(L)]
log=[0]+[F((-1)**(i+1),i) for i in range(1,L)]
sin=[F((-1)**((i-1)//2),factorial(i)) if i%2 else F(0) for i in range(L)]
cos=[F((-1)**(i//2),factorial(i)) if i%2==0 else F(0) for i in range(L)]
assert deriv(exp)==exp[:-1]
assert deriv(log)==inv([1,1],L-1)
assert deriv(sin)==cos[:-1]
assert deriv(cos)==scale(sin[:-1],-1)
assert add(mul(sin,sin,L),mul(cos,cos,L),L)==[1]+[0]*(L-1)
tan=mul(sin,inv(cos,L),L)
assert deriv(tan)==add([1],mul(tan,tan,L-1),L-1)
assert compose(log,add(exp,[-1],L),L)==x
print('exp/log inverse, sin²+cos²=1, and tan′=1+tan² through degree',L-2)
timed=compose(exp,[0,0,F(1,2)],L)
assert deriv(timed)==mul(x,timed,L-1)
print('Nonautonomous x′=t x, x(0)=1: exp(t²/2), coefficients',show(timed[:9]))
f=[2,3,1];finv=inv(f,L)
assert mul(f,finv,L)==[1]+[0]*(L-1)
print('Triangular inverse (t,s)↦(t,f(t)s) has last component f(t)^−1 s, coefficients',show(finv[:6]))
h=[0,1,1];hplus=add(h,[1],L);g=add(inv(hplus,L),[-1],L)
assert add(mul(hplus,add(g,[1],L),L),[-1],L)==[0]*L
print('H-only Jacobson repair: (1+h)(1+g)−1=0; g=(1+h)^−1−1, g(0)=0.')
# Implicit P(t,z)=z+z²−t: Catalan coefficients with alternating sign.
z=[0]+[F((-1)**(n-1)*comb(2*n-2,n-1),n) for n in range(1,L)]
assert add(add(z,mul(z,z,L),L),scale(x,-1),L)==[0]*L
print('Implicit root z+z²=t, coefficients',show(z[:9]))
# Factorization of (Z−a)(Z−b): coefficient Jacobian determinant b−a.
for a,b in product(range(-4,5),repeat=2):
 jac=[[-1,-1],[b,a]];assert jac[0][0]*jac[1][1]-jac[0][1]*jac[1][0]==b-a
print('Two linear-factor coefficient map Jacobian determinant b−a = resultant up to convention.')
f=[0,0,F(1,2)]
assert deriv(f)==[0,1] and hasse(f,2)==[F(1,2)]
print('Ordinary derivative of t²/2 is t; HasseD2 is1/2. Z[t,t²/2] test does not assert all family axioms.')
for p in (2,3,5):
 a=[0]*p+[1];assert all(v%p==0 for v in deriv(a));assert hasse(a,p)==[1]
print('In F_p[t], ordinary D(t^p)=0 but HasseD_p(t^p)=1 for p=2,3,5.')
a=[F(i-3,i+1) for i in range(12)]
for r,s in product(range(4),repeat=2):
 left=hasse(hasse(a,s),r);right=scale(hasse(a,r+s),comb(r+s,r));assert left==right
for r in range(5):
 rhs=[0]*(22-r+1)
 for j in range(r+1):rhs=add(rhs,mul(hasse(a,j),hasse(a,r-j),len(rhs)),len(rhs))
 assert hasse(mul(a,a,23),r)==rhs
print('Hasse composition and product formula verified exactly through order4; coefficient extraction gives a_r.')
def bch(A,B):
 a,b,c=A;d,e,f=B
 return (a+d,b+e,c+f+F(a*e-b*d,2))
for vals in product((-1,0,1),repeat=9):
 A=vals[:3];B=vals[3:6];C=vals[6:]
 assert bch(bch(A,B),C)==bch(A,bch(B,C))
print('Class-two Heisenberg BCH associative on all 3^9 triples; general bilinear identity proved in audit.')
q=[1]*L;assert mul([1,-1],q,L)==[1]+[0]*(L-1)
print('(1−t)Σ_(i<16)t^i=1 modulo t^16, illustrating Q[t]/(1−t) killed by Q[[t]].')

print('\n8. Finite nilpotent substitution and full-unit Weierstrass division')
# For k=Z/8, constant2 is nilpotent: coefficients at t^j of f(2+t)
# have only terms with i−j<3, when f=Σt^i; compare geometric inverse.
LL=12
geom=compose([1]*(LL+3),[2,1],LL,8)
assert geom==inv([1-2,-1],LL,8)
print('Substitute 2+t into Σz^i over Z/8: agrees with (1−2−t)^−1 through degree11.')
L=40;N=2;mod=8;U=[1,1];Uinv=inv(U,L,mod);R=[2,4];Fseries=[2,4,1,1]
def phi0inv(G):return (G[:N]+[0]*max(0,N-len(G)),mul(G[N:]+[0]*N,Uinv,L,mod))
def T(pair):return phi0inv(mul(pair[1],R,L,mod))
def div(G):
 term=phi0inv(G+[0]*max(0,L-len(G)));res=term
 for j in (1,2):
  term=T(term);sgn=(-1)**j
  res=(add(res[0],scale(term[0],sgn,mod),N,mod),add(res[1],scale(term[1],sgn,mod),L,mod))
 return res
G=[3,5,2,1,7,0,6,1,0,4]
rem,Q=div(G);back=add(rem,mul(Q,Fseries,L,mod),L,mod)
assert back[:25]==(G+[0]*L)[:25]
print('A=Z/8,F=2+4z+z²+z³; G=',G)
print('Unique remainder=',rem,'Q first12=',Q[:12],'; identity checked through degree24 with40-term buffer.')
rr,qq=div([0,0,1]);P=[(-rr[0])%8,(-rr[1])%8,1];prepU=inv(qq,L,8)
assert mul(P,prepU,25,8)==(Fseries+[0]*25)[:25]
print('Preparation P=',P,'U first12=',prepU[:12],'; P*U=F checked through degree24.')
print('Modulo(2), F=z²(1+z), not a scalar times z²: last manuscript scalarα would drop the z³ term.')
print('\nALL EXACT CHECKS PASSED. General statements and limitations are in proof_audit.md.')
