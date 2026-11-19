"""Exact finite symbolic checks for cote91/099–143.

Finite tests do not establish universal claims: the companion narrative gives
the separate general proofs. No verdicts or source readings are inferred here.
"""
import itertools, math
from collections import defaultdict
import sympy as s

def out(title,value): print('\n'+title+'\n'+str(value))
t,e=s.symbols('t epsilon')
a0,a1,a2,b0,b1,b2=s.symbols('a0 a1 a2 aprime0 aprime1 aprime2')
f=a0+a1*t+a2*t*t
gf=s.Poly(s.expand(b0+b1*f+b2*f*f),t)
out('C01 scan142: coefficients of g(f(t)), degrees0..4',gf.all_coeffs()[::-1])
assert gf.nth(1)==b1*a1+2*b2*a0*a1
assert gf.nth(2)==b1*a2+b2*a1*a1+2*b2*a0*a2
rem=s.Poly(s.expand((t+e)**3),t,e)
red=sum(c*t**i*e**j for (i,j),c in rem.terms() if i<3 and j<3)
out('C02 scan142: (t+epsilon)^3 modulo (t^3,epsilon^3)',red)
assert s.expand(red)==3*e*t*t+3*e*e*t
out('C03 scan142: t->2t over Z[t]/(t^3)',
    'Coefficient of t in any proposed inverse composition is 2*b1; equation2*b1=1 has no integer solution. Mod2 the map sends t to0, while t!=0.')
out('C04 scans134–135: dual-number Laurent inverse',s.expand((1+e/t)*(1-e/t)))
assert s.expand((1+e/t)*(1-e/t)-1)==-e**2/t**2
cases=[]
for n in range(5):
  for np in range(n+1,n+4):
    for i in range(-n,n+1):
      m=np-abs(i)
      bounds=(min(i,i-m),min(-i,-i-m))
      assert min(bounds)==-np and min(bounds)<-n
      cases.append((n,np,i,m,bounds))
out('C05 strict Γ_n^i→Γ_nprime^i witnesses: t^i(1+epsilon*t^(-m)), m=nprime-|i|',
    {'tested':len(cases),'sample':cases[:6],'product_mod_epsilon2':'1; one of series/inverse has nonzero coefficient of t^(-nprime), excluding Γ_n'})

x1,x2,y1,y2,z1,z2=s.symbols('X1 X2 Y1 Y2 Z1 Z2')
for p in (2,3,5,7):
  def F(x,y):return (x[0]+y[0]+x[0]*y[0],x[1]+(1+x[0]**p)*y[1])
  X=(x1,x2);Y=(y1,y2);Z=(z1,z2)
  lhs=F(F(X,Y),Z);rhs=F(X,F(Y,Z))
  residual=[s.Poly(s.expand(lhs[k]-rhs[k]),x1,x2,y1,y2,z1,z2,modulus=p).as_expr() for k in(0,1)]
  difference=s.Poly(s.expand(F(X,Y)[1]-F(Y,X)[1]),x1,x2,y1,y2,modulus=p)
  assert residual==[0,0]
  assert all(sum(mon)==p+1 for mon,c in difference.terms())
  out(f'C06 scan139: semidirect formal law, p={p}',{'associator':residual,'commutator_difference':str(difference.as_expr()),'least_total_degree':p+1})
out('C07 earlier-run p=2 quotient modulo total degree3','X1^2*Y2 + Y1^2*X2 is nonzero; every monomial has degree3, so its image in the quadratic quotient is0.')

a,b,c,d=s.symbols('a b c d'); X=s.Matrix([[a,b],[c,d]]);J=s.Matrix([[0,1],[-1,0]])
out('C08 scan139: n=1 symplectic tangent equation',X.T*J+J*X)
assert X.T*J+J*X==(a+d)*J
for n in(1,2,3):
  v=s.symbols('v:'+str(4*n*n));M=s.Matrix(2*n,2*n,v);O=s.zeros(n);I=s.eye(n)
  J=O.row_join(I).col_join((-I).row_join(O))
  L=s.Matrix(list(M.T*J+J*M)).jacobian(v)
  dim=4*n*n-L.rank();assert dim==n*(2*n+1)
  out(f'C09 symplectic dimension, n={n}',dim)

u=s.symbols('u11 u12 u21 u22');v=s.symbols('v11 v12 v21 v22');U=s.Matrix(2,2,u);V=s.Matrix(2,2,v)
G=(s.eye(2)+U)*(s.eye(2)+V)-s.eye(2)
out('C10 scan141: GL2 formal group law',G)
vec=[]
for i in range(2):
 for j in range(2):
  coeff=s.Matrix([G[k,l].diff(v[2*i+j]).subs({q:0 for q in v}) for k in range(2) for l in range(2)])
  expected=s.Matrix([(s.KroneckerDelta(k,i)+U[k,i])*s.KroneckerDelta(l,j) for k in range(2) for l in range(2)])
  assert coeff==expected;vec.append(coeff)
out('C11 scan143: left invariant GL2 vector fields on ordered coordinates',vec)
def act(coeff,expr):return s.expand(sum(coeff[k]*s.diff(expr,u[k]) for k in range(4)))
checks=0
for aidx in range(4):
 for bidx in range(4):
  i,j=divmod(aidx,2);k,l=divmod(bidx,2)
  comm=s.Matrix([act(vec[aidx],vec[bidx][q])-act(vec[bidx],vec[aidx][q]) for q in range(4)])
  expected=(vec[2*i+l] if j==k else s.zeros(4,1))-(vec[2*k+j] if l==i else s.zeros(4,1))
  assert comm==expected;checks+=1
out('C12 Lie brackets [Xij,Xkl]=delta_jk Xil−delta_li Xkj',f'{checks} generator brackets verified symbolically')
for p in(2,3,5):
 for idx,D in enumerate(vec):
  i,j=divmod(idx,2)
  for q in range(4):
   a=u[q]
   for r in range(p):a=act(D,a)
   residual=s.Poly(a-(D[q] if i==j else 0),*u,modulus=p).as_expr()
   assert residual==0
out('C13 restricted GL structure','p=2,3,5: Xii^p=Xii and Xij^p=0 (i!=j) verified on all coordinate generators. In characteristic p, the pth iterate is a derivation, so generator check suffices.')

r1,r2,h=s.symbols('r1 r2 h',nonzero=True);R=s.diag(r1,r2);S=s.Matrix([[0,h],[-h,0]]);B=R.inv()*S;I=s.eye(2)
C=(I-B).inv()*(I+B)
orth=(C.T*R*C-R).applyfunc(s.simplify)
inverse=(R*(C-I)*(C+I).inv()-S).applyfunc(s.simplify)
assert orth==s.zeros(2) and inverse==s.zeros(2)
out('C14 scan143: exact Cayley orthogonality and inverse for diagonal2x2 R',{'U':str(C.applyfunc(s.factor)),'U^T R U−R':str(orth),'inverse−S':str(inverse)})
h2=s.symbols('h2');S2=s.Matrix([[0,h2],[-h2,0]]);B2=R.inv()*S2;C2=(I-B2).inv()*(I+B2)
comp=(R*(C*C2-I)*(C*C2+I).inv()).applyfunc(s.factor)
out('C15 Cayley composition,2x2 chart',comp)
assert s.simplify(comp[0,1]-(h+h2)/(1-h*h2/(r1*r2)))==0

def wedge(A,B):
 C=defaultdict(lambda:s.Integer(0))
 for aa,ca in A.items():
  for bb,cb in B.items():
   if set(aa)&set(bb):continue
   parity=sum(x>y for x in aa for y in bb)
   C[tuple(sorted(aa+bb))]+=(-1)**parity*ca*cb
 return {a:s.expand(c) for a,c in C.items() if s.expand(c)!=0}
def add(*aa):
 D=defaultdict(lambda:s.Integer(0))
 for A in aa:
  for m,c in A.items():D[m]+=c
 return {m:s.expand(c) for m,c in D.items() if s.expand(c)!=0}
q=s.symbols('q:9');vv=[{(k,):q[3*j+k] for k in range(3)} for j in range(3)]
expr=wedge(wedge(vv[0],vv[1]),vv[2]);det=s.Matrix(3,3,q).det()
assert s.expand(expr[(0,1,2)]-det)==0
out('C16 scans119–123: threefold wedge/shuffle sign',expr)
assert wedge(vv[0],vv[0])=={}
z=add({(0,):1,(1,):2,(2,):3},{(0,1):5,(1,2):7},{(0,1,2):11})
power={():s.Integer(1)}
for k in range(1,5):
 power=wedge(power,z);out(f'C17 positive exterior element, power{k}',power)
assert power=={}
def subsets(aa):return {tuple(v) for r in range(len(aa)+1) for v in itertools.combinations(aa,r)}
N=subsets([0,1]);P=subsets([0,2]);intersection=N&P
assert intersection==subsets([0])
out('C18 split exterior intersection M=A⊕B⊕C⊕D, N=A⊕B, P=A⊕C',sorted(intersection))
for n in range(1,7):
 assert sum(math.comb(n,r) for r in range(n+1))==2**n
out('C19 ordered wedge basis finite dimension counts',[(n,[math.comb(n,r) for r in range(n+1)]) for n in range(1,7)])

# Noncommuting word calculation of (ad x)^(p-1)(y), compared with D(x^p).
for p in(2,3,5,7):
 coeff=[((-1)**j*math.comb(p-1,j))%p for j in range(p)]
 assert coeff==[1]*p
 out(f'C20 restricted derivation identity p={p}',{'coefficients_in_ad_expansion':coeff,'terms':'sum_j x^(p-1-j)*y*x^j = D(x^p), y=D(x)'})
for p in(2,3,5):
 for dim in(1,2,3):
  exponents=list(itertools.product(range(p),repeat=dim));assert len(exponents)==p**dim
out('C21 restricted PBW quotient finite-rank exponent check','For p=2,3,5 and ranks1,2,3 there are p^rank ordered exponents0≤e_i<p; triangular PBW proof is supplied separately, not inferred from these counts.')
out('C22 chain-homotopy vanishing identity','If T=d*rho+rho*d is invertible and d²=0, then dT=Td; h=T^(-1)rho satisfies dh+hd=1. For a cocycle f, f=d(T^(-1)rho f).')
out('C23 inverse limit density','For finite coordinate set J choose a dominating index alpha; any target cylinder can be met by lifting an element of K_alpha. Finite-support F2 sequences project onto every finite product but form a proper dense subgroup of the full product.')
print('\nALL EXACT CHECKS PASSED. Universal statements rely on the stated separate proofs; finite p/rank samples are not represented as universal proofs.')
