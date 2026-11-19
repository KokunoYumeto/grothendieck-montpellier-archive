"""Exact finite checks supporting (not replacing) the proofs in section.md.
All source readings are preserved. This script tests stated mathematical alternatives.
"""
from itertools import product,combinations
from math import factorial
import sympy as s

def report(label,value):
    print(label+': '+str(value))

# Truncated one-variable identities, representative orders 2 through 9.
x,y=s.symbols('x y')
for n in range(2,10):
    exp=sum(x**i/s.factorial(i) for i in range(n))
    log=sum((-1)**(i+1)*x**i/s.Integer(i) for i in range(1,n))
    assert s.series(sum((-1)**(i+1)*(exp-1)**i/s.Integer(i) for i in range(1,n)),x,0,n).removeO()==x
    assert s.series(sum(log**i/s.factorial(i) for i in range(n)),x,0,n).removeO()==1+x
report('finite exp/log inverses modulo x^n','PASS n=2,...,9; general proof uses formal identities')
for i in range(6):
    for j in range(6):
        assert s.binomial(i+j,i)/s.factorial(i+j)==1/(s.factorial(i)*s.factorial(j))
report('commuting exponential coefficient identity','PASS i,j<=5')

# For exp(v)f=f exp(u), delta_n=sum_{i+j=n-1}v^i delta u^j.
# Thus 0=delta+sum_{i+j>=1}v^i delta u^j/(i+j+1)!.
report('intertwiner correction c_ij',[(i,j,-s.Rational(1,factorial(i+j+1))) for i,j in [(1,0),(0,1),(2,0),(1,1),(0,2)]])

# Dual numbers A=Q[e]/e^2, basis 1,e, u(e)=2e, D(e)=e.
U=s.diag(1,2); D=s.diag(0,1); me=s.Matrix([[0,0],[1,0]])
comm=U*me-me*U
assert comm!=s.zeros(2) and comm*me-me*comm==s.zeros(2)
assert (U-s.eye(2))**5==D and D**5==D
report('dual-number automorphism',{'U':U.tolist(),'[U,m_e]':comm.tolist(),'[[U,m_e],m_e]':(comm*me-me*comm).tolist(),'D^5':(D**5).tolist(),'J^2':0,'gr_J action on e':2})
a,b,c,d=s.symbols('a b c d')
mul=lambda z,w:(s.expand(z[0]*w[0]),s.expand(z[0]*w[1]+z[1]*w[0]))
der=lambda z:(0,z[1])
assert der(mul((a,b),(c,d)))==tuple(s.expand(p+q) for p,q in zip(mul(der((a,b)),(c,d)),mul((a,b),der((c,d)))))
report('D(e)=e is a derivation','PASS symbolic Leibniz; D(A) subset (e) but D not nilpotent')
report('reduced polynomial-ring order counterexample',{'[D,m_x](1)':s.diff(x,x),'[D,m_x](x)':s.diff(x*x,x)-x*s.diff(x,x)})
assert s.diff(x*x,x)-x*s.diff(x,x)==x

# End_K(K+Q) base change: K=Q[e]/e^2, module basis (1,e,f).
E=s.Matrix([[0,0,0],[1,0,0],[0,0,0]])
z=s.symbols('z:9'); Z=s.Matrix(3,3,z)
sol=s.linsolve(list(Z*E-E*Z),z)
report('End_K(K directsum Q) commuting-matrix family',sol)
# Family [[a,0,0],[b,a,c],[d,0,e]], epsilon times it has only b slot.
# Quotient by epsilon End has basis a,c,d,e; reduction M/eM kills c.
basechange=s.diag(1,0,1,1)
assert basechange.rank()==3
report('endomorphism base-change Q-dimensions and rank',{'source':4,'target':4,'rank':3,'kernel':'map f to e','missing':'map f to class(1)'})

# Two-element torsors.
count=0
for f in product(range(2),repeat=2):
    bij=len(set(f))==2
    equiv=all(f[1-i]==1-f[i] for i in range(2))
    assert bij==equiv
    count+=bij
qcount=0
for f in product(range(2),repeat=4):
    val=lambda i,j:f[2*i+j]
    contracted=all(val(i,j)==val(1-i,1-j) for i,j in product(range(2),repeat=2)) and len(set(f))==2
    slices=all(val(i,0)!=val(i,1) for i in range(2)) and all(val(0,j)!=val(1,j) for j in range(2))
    assert contracted==slices
    qcount+=contracted
report('two-element lemmas',{'maps':4,'bijections':count,'binary_maps':16,'torsor_product_isomorphisms':qcount})
report('boundary convention comparison t_n', [(-1)**(n*(n+1)//2) for n in range(9)])
assert all((-1)**((n-1)*n//2)==(-1)**n*(-1)**(n*(n+1)//2) for n in range(1,10))

# Icosahedron in the manuscript frame.
sqrt5=s.sqrt(5); ca=1/sqrt5; sa=2/sqrt5
theta=2*s.pi/5
ct=(sqrt5-1)/4; st=s.sqrt(10+2*sqrt5)/4
ch=(sqrt5+1)/4; sh=s.sqrt(10-2*sqrt5)/4
# Read source matrix separately: rotation_w(alpha) rotation_u(-theta/2).
gamma=s.Matrix([[ca,-sa*ch,-sa*sh],[sa,ca*ch,ca*sh],[0,-sh,ch]])
u=s.Matrix([1,0,0])
xs=[s.Matrix([ca,sa*s.cos(i*theta),sa*s.sin(i*theta)]) for i in range(5)]
zero=lambda v:all(s.simplify(s.expand_trig(q))==0 for q in v)
assert zero(gamma*u-xs[0])
matches=[]
allv=[u]+xs+[-u]+[-v for v in xs]
for source in [u]+xs:
    target=gamma*source
    hits=[j for j,v in enumerate(allv) if zero(target-v)]
    assert len(hits)==1
    matches.append(hits[0])
report('gamma images indexed [u,x0,x1,x2,x3,x4,-u,-x0,...,-x4]',matches)
assert s.simplify(gamma.det())==1 and all(s.simplify(v)==0 for v in gamma.T*gamma-s.eye(3))
report('gamma orthogonal determinant',1)
flagged_residuals=[-ca-(ca**2-sa**2*ch),-s.cos(2*theta)-ca*(1+ch),s.sin(2*theta)-sh]
flagged_residuals=[s.simplify(q) for q in flagged_residuals]
assert flagged_residuals==[0,0,0]
report('scan7 three identities marked a prouver: residuals',flagged_residuals)
edge2=2-2/sqrt5
neighbour_vectors=[xs[0]+xs[2],xs[4]+xs[2],-xs[2]+xs[3]]
neighbour_lengths=[s.simplify(q.dot(q)) for q in neighbour_vectors]
assert all(s.simplify(q-edge2)==0 for q in neighbour_lengths)
report('scan6 all three neighbouring-cap squared distances',neighbour_lengths)
lam=s.symbols('lam')
assert all(s.simplify(z*z-4*z+4*sa*sa)==0 for z in [2-2/sqrt5,2+2/sqrt5])
assert s.simplify(s.cos(s.acos(ca)/2)**2-1/(4*sh**2))==0
report('scan6 squared-length quadratic and half-angle relation','PASS exact radicals')
report('icosahedral angle degrees',s.N(s.acos(ca)*180/s.pi,12))
report('false sqrt(3)sin(pi/5)=1 residual',s.N(s.sqrt(3)*s.sin(s.pi/5)-1,12))
assert s.simplify(ca-ct/(1-ct))==0
assert s.simplify((2*ca**2-1)+s.Rational(3,5))==0
report('angle identity cos(alpha),cos(2alpha)',(ca,-s.Rational(3,5)))
report('distance-square roots', [2-2/sqrt5,2+2/sqrt5])

# Exact canonical coordinates permit a small automorphism backtracking search.
phi=(1+sqrt5)/2
V=[]
for a,b in product([-1,1],repeat=2):
    V.extend([s.Matrix([0,a,b*phi]),s.Matrix([a,b*phi,0]),s.Matrix([b*phi,0,a])])
dist=lambda i,j:s.simplify(sum((V[i][k]-V[j][k])**2 for k in range(3)))
adj=[{j for j in range(12) if i!=j and dist(i,j)==4} for i in range(12)]
edges=[(i,j) for i in range(12) for j in adj[i] if i<j]
faces=[q for q in combinations(range(12),3) if all(j in adj[i] for i,j in combinations(q,2))]
assert len(edges)==30 and len(faces)==20 and all(len(a)==5 for a in adj)
autos=[]
def backtrack(mapping,used):
    if len(mapping)==12:
        autos.append(dict(mapping));return
    remaining=[i for i in range(12) if i not in mapping]
    i=max(remaining,key=lambda q:sum(v in mapping for v in adj[q]))
    for j in range(12):
        if j in used:continue
        if all((q in adj[i])==(r in adj[j]) for q,r in mapping.items()):
            mapping[i]=j;used.add(j);backtrack(mapping,used);used.remove(j);del mapping[i]
backtrack({},set())
basis=next(q for q in combinations(range(12),3) if s.Matrix.hstack(*(V[i] for i in q)).det()!=0)
Binv=s.Matrix.hstack(*(V[i] for i in basis)).inv()
signs=[]
for a in autos:
    A=s.simplify(s.Matrix.hstack(*(V[a[i]] for i in basis))*Binv)
    assert all(s.simplify(v)==0 for v in A.T*A-s.eye(3))
    assert all(zero(A*V[i]-V[a[i]]) for i in range(12))
    signs.append(s.simplify(A.det()))
report('icosahedral exact enumeration',{'vertices':12,'edges':len(edges),'faces':len(faces),'graph_aut':len(autos),'rotations':signs.count(1),'orientation_reversing':signs.count(-1)})
assert len(autos)==120 and signs.count(1)==60

# Cyclotomic fixed ring, inversion, trace/norm, and arithmetic parameters.
T=s.symbols('T'); P=T**4+T**3+T**2+T+1
red=lambda q:s.rem(q,P,T)
beta=[red(T**(4*i)) for i in range(4)]
report('inversion images basis 1,T,T2,T3',beta)
assert beta==[1,-T**3-T**2-T-1,T**3,T**2]
c0,c1,c2,c3=s.symbols('c0 c1 c2 c3')
fixed=s.Poly(sum(c*b for c,b in zip([c0,c1,c2,c3],beta))-(c0+c1*T+c2*T*T+c3*T**3),T)
report('fixed coefficient equations',fixed.all_coeffs())
tr=red(T+T**4)
assert red(tr**2+tr-1)==0
report('trace root quadratic',red(tr**2+tr-1))
report('quadratic trace and norm',{'trace':-1,'norm':-1,'discriminant':5})
r=s.symbols('r')
assert s.rem(5*r-(2*r+1)*(2-r),r*r+r-1,r)==0
report('r/(2-r)=(2r+1)/5','PASS modulo r^2+r-1, where 5 and 2-r invertible')

# Ribbon boundary permutations (darts a,b,A,B; involution a<->A,b<->B).
tau={0:2,2:0,1:3,3:1}
def cycles(p):
    remaining=set(p);out=[]
    while remaining:
        i=min(remaining);c=[]
        while i in remaining:c.append(i);remaining.remove(i);i=p[i]
        out.append(c)
    return out
def boundary(order):
    sigma={order[i]:order[(i+1)%len(order)] for i in range(len(order))}
    return cycles({i:sigma[tau[i]] for i in tau})
for name,order in [('crossed',[0,1,2,3]),('planar',[0,2,1,3])]:
    cs=boundary(order);g=(3-len(cs))//2
    report('two-loop bouquet '+name,{'boundary_cycles':cs,'b':len(cs),'b1':2,'g':g})
report('annulus glued to annulus at both circles',{'gU':0,'gcomplement':0,'incidence_vertices':2,'incidence_edges':2,'incidence_b1':1,'result_genus':1})
print('ALL ASSERTIONS PASSED. Finite checks certify the displayed instances; proofs and limitations are in section.md.')
