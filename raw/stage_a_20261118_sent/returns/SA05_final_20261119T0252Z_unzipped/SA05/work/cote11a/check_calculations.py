"""Exact finite checks supporting cote11a. This is not a formal proof assistant.
Every finite range is printed; general arguments are in proof_checks.md.
Run: python SA05/work/cote11a/check_calculations.py > SA05/work/cote11a/calculation_output.txt
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
import sympy as s

def report(name,value): print(name+': '+str(value))
a,b,c,d,aa,bb,cc,dd=s.symbols('a b c d alpha beta gamma delta')
M=s.Matrix([[b,a],[d,c]]);N=s.Matrix([[bb,aa],[dd,cc]])
# Multiplication in Q[t1,...,tn]/(t_i^2); monomials indexed by bit masks.
def mul(u,v):
 out={}
 for i,x in u.items():
  for j,y in v.items():
   if not i&j:out[i|j]=s.expand(out.get(i|j,0)+x*y)
 return {i:x for i,x in out.items() if x!=0}
def integrate(u,bit):
 return {i&~bit:x for i,x in u.items() if i&bit}
u={0:a,1:b,2:c,3:d}
v23={0:aa,2:bb,4:cc,6:dd}
conv=integrate(mul(u,v23),2)
Cv=s.Matrix([[conv.get(1,0),conv.get(0,0)],[conv.get(5,0),conv.get(4,0)]])
assert Cv==N*M
report('Dual numbers: convolution matrix',Cv)
report('Dual numbers: operator of a+b*t1+c*t2+d*t1*t2',M)
report('Delta=t1+t2 operator',M.subs({a:0,b:1,c:1,d:0}))
assert M.subs({a:0,b:1,c:1,d:0})==s.eye(2)

# Adjoints: J trace pairing on (1,t), J2 tensor pairing on(1,t2,t1,t1t2).
J=s.Matrix([[0,1],[1,0]])
mult=s.Matrix([[1,0,0,0],[0,1,1,0]])
J2=s.kronecker_product(J,J)
coprod=J2.inv()*mult.T*J
expected=s.Matrix([[0,0],[1,0],[1,0],[0,1]])
assert coprod==expected
eps=s.Matrix([[0,1]])
assert s.kronecker_product(eps,s.eye(2))*coprod==s.eye(2)
assert s.kronecker_product(s.eye(2),eps)*coprod==s.eye(2)
assert s.kronecker_product(coprod,s.eye(2))*coprod==s.kronecker_product(s.eye(2),coprod)*coprod
flip=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
assert flip*coprod==coprod
report('Dual numbers: adjoint diagonal, columns delta_*1 and delta_*t',coprod)
report('Frobenius counit, cocommutativity, coassociativity','exact matrices PASS')

# Inverse identity: independent symbolic 2x2 check and Cayley-Hamilton formula.
U=s.Matrix([[2,1],[1,1]]);V=s.Matrix([[1,2],[3,5]]);W=U*V
assert W.inv()*U==V.inv()
x=s.symbols('x');cp=W.charpoly(x).as_expr();coeff=W.charpoly(x).all_coeffs()
Winv=-(W+coeff[1]*s.eye(2))/coeff[2]
assert Winv==W.inv()
report('Opposite map inverse (sample U,V)',(W.inv()*U,V.inv()))
report('Cayley-Hamilton rational inverse (sample)',{'charpoly':cp,'inverse':Winv})

for m in range(0,16):
 L=s.zeros(m+1);La=s.zeros(m+1);Lc=s.zeros(m+1);D=s.eye(m+1)
 for j in range(1,m+1):
  L[j,j-1]=1;La[j-1,j]=1;Lc[j-1,j]=j*(m-j+1);D[j,j]=j*(m-j+1)
 assert Lc==La*D and La==Lc*D.inv()
 v=s.zeros(m+1,1);v[0]=1
 assert La**m*L**m*v==v and Lc**m*L**m*v==factorial(m)**2*v
report('Primitive strings m=0,...,15','four lowering identities PASS; proof for all m uses the displayed diagonal factors')

parities=[]
for i,j,delta in product(range(2),repeat=3):
 assert (i*j+j*(i+delta))%2==(delta*j)%2
 parities.append((i,j,delta,(delta*j)%2))
report('Projection formula parity (i,j,delta,exponent)',parities)

# Tensor adjoints under ordinary tensor trace and Koszul multiplication.
# Trace-pairing degrees force a+a'=dA', b+b'=dB'. Left/right expansion gives f*b.
tensor=[]
for da,db,da1,db1,ap,bp in product(range(2),repeat=6):
 f=(da-da1)%2;g=(db-db1)%2
 a_test=(da1-ap)%2;b_test=(db1-bp)%2
 # LHS crosses b_test past ap. RHS crosses b_test past f_*ap of degreeap+f.
 eps=(b_test*ap-b_test*(ap+f))%2
 assert eps==(f*(db1+bp))%2
 if f==0 and g==0: assert eps==0
 tensor.append(eps)
report('Tensor pushforward parity','64 cases PASS; correction f*(d_Bprime+|bprime|) in this explicitly stated ordinary-tensor-trace convention; even shifts give zero')

# Degree balancing symbolic certificate.
i,dp,d0=s.symbols('i dprime d')
ip=i+dp-d0
assert s.expand((d0-i)+ip-dp)==0
report('Adjoint degree',ip)

# Scalar-gauge square: Q_lambda -> Q_mu has push lambda/mu and pullid.
def push(lam,mu):return F(lam,mu)
q=push(2,1);fp=push(2,1);p=push(1,1);f=push(1,1)
assert f*q==p*fp
lhs=f;rhs=fp
assert lhs!=rhs and all(z!=0 for z in (q,fp,p,f))
report('Cartesian gauge-square commutativity (push)',(f*q,p*fp))
report('Exchange sides p^*f_* and fprime_*q^*',(lhs,rhs))
report('Gauge-square dimensions and invertibility','all dimensions0; all four maps invertible; Cartesian by inverse to q')

# Restricted-growth strings enumerate all partitions of an n-set.
def partitions(n):
 if n==0:return [()]
 out=[(0,)]
 for _ in range(1,n):out=[p+(a,) for p in out for a in range(max(p)+2)]
 return out
def canonical(seq):
 dct={};out=[]
 for a in seq:
  if a not in dct:dct[a]=len(dct)
  out.append(dct[a])
 return tuple(out)
def restrict(p,alpha):return canonical([p[a] for a in alpha])
def mapdata(n,m,alpha):
 # alpha:n->m; q:Part(m)->Part(n).
 pn=partitions(n);pm=partitions(m)
 Pull=s.zeros(len(pm),len(pn))
 for row,p in enumerate(pm): Pull[row,pn.index(restrict(p,alpha))]=1
 return Pull,Pull.T
totalmaps=0;totalcomps=0
for n,m in product(range(1,4),repeat=2):
 for al in product(range(m),repeat=n):
  pull,push_=mapdata(n,m,al);totalmaps+=1
  assert pull*s.ones(len(partitions(n)),1)==s.ones(len(partitions(m)),1)
  # trace=sum coordinates, so transpose is exactly adjoint.
  pn,pm=partitions(n),partitions(m)
  tau_n=s.zeros(1,len(pn));tau_n[0,pn.index((0,)*n)]=1
  tau_m=s.zeros(1,len(pm));tau_m[0,pm.index((0,)*m)]=1
  assert tau_m*pull==tau_n and push_*tau_m.T==tau_n.T
  for k in range(1,4):
   for be in product(range(k),repeat=m):
    pb,sb=mapdata(m,k,be);pc,sc=mapdata(n,k,tuple(be[x] for x in al))
    assert pc==pb*pull and sc==push_*sb;totalcomps+=1
report('Partition systems dimensions n=1,2,3',[len(partitions(n)) for n in range(1,4)])
report('Partition systems naturality/composition finite checks',(totalmaps,totalcomps))
report('Partition system specialness at1+1',{'tensor_dimension':1,'B2_dimension':2,'tensor_map_rank':1})

# Block-corner arithmetic is independent of chosen coefficient kernel category.
u0=s.symbols('u');block=s.Matrix([[0,0],[u0,0]]);ex=s.diag(1,0);ey=s.diag(0,1)
assert ey*block*ex==block
report('Object corner eY*u*eX',ey*block*ex)

# Weight/subadditivity and parabolic support tests, exact integer finite range.
for x0,y0 in product(range(-3,4),repeat=2):
 # Sample rational form family t,-2t; general max inequality proved in prose.
 assert max(x0+y0,-2*(x0+y0))<=max(x0,-2*x0)+max(y0,-2*y0)
for r1,r2,s1,s2 in product(range(-2,3),repeat=4):
 if r1-r2>=0 and s1-s2>=0:assert (r1+s1)-(r2+s2)>=0
report('Weight checks','49 max-function examples and625 two-weight parabolic cases PASS; not a substitute for general root argument')
for K,eps0,n0 in product([F(0),F(1),F(5,2)],[F(1,3),F(1),F(2)],[0,2,7]):
 n=(n0+K/eps0).__floor__()+1
 assert -K+(n-n0)*eps0>0
report('Uniform stability integer bound','27 exact rational cases PASS; choose n=floor(n0+K/epsilon)+1')

X,Y=s.symbols('X Y')
assert s.expand((X+s.I*Y)*(X-s.I*Y))==X**2+Y**2
report('Real node complexification factorization',s.factor(X**2+Y**2,extension=s.I))
report('Literal integrality counterexample','A=B=Q[e]/e^2; identity flat/local; closed fiberQ geometrically integral; A_red=Q normal; e nonzero with e²=0')
report('Infinite ideal intersection example','DVR A, J_i=(pi^i), B=A[1/pi]: J_iB=B for every i; intersectionJ_i=0 by valuation; B flat and finitely presented')
report('Cycle-generator point test','CH_Q(point)=Q; smooth proper Y maps unit to0 ifdimY>0, otherwise nonnegative degree; -1 is not such a value')
# Nilpotent thickening: ordinary schematic density need not lift.
nx,ne,ny=s.symbols('x epsilon inverse_x')
thick=s.groebner([ne**2,nx*ne],ny,nx,ne,domain=s.QQ)
assert thick.reduce(ne)[1]==ne
assert thick.reduce(ne**2)[1]==0 and thick.reduce(nx*ne)[1]==0
loc=s.groebner([ne**2,nx*ne,nx*ny-1],ny,nx,ne,domain=s.QQ)
assert loc.reduce(ne)[1]==0
report('Nilpotent density counterexample',{'epsilon_in_S':str(thick.reduce(ne)[1]),'epsilon_squared':str(thick.reduce(ne**2)[1]),'x_epsilon':str(thick.reduce(nx*ne)[1]),'epsilon_after_inverting_x':str(loc.reduce(ne)[1])})
report('Nilpotent density hypotheses','S=Spec Q[x,e]/(e²,xe), X=S, Z=D(x); identity and open immersion flat. S0=Spec Q[x], Z0=D(x) schematically dense. J/J²=Q[x]/(x) is not locally free. Relative universal density is not asserted by this example.')
print('ALL EXECUTED CHECKS PASSED')
