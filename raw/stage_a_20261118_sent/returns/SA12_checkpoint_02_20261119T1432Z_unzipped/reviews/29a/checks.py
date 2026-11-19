"""Reproducible finite calculations used in the 29a review.

The accompanying independent_checks.md supplies the general proofs and limits.
No finite sample here purports to prove a universal cohomological statement.
"""
from fractions import Fraction
from itertools import product
from math import comb, prod
import sympy as s

print('SA12 / review_29a mathematical calculations; 2026-11-19')
print('Symbolic engine:', s.__version__)

# Finite-Hom bound: stalk maps determine maps, whether or not they are equivariant.
print('\nC01 finite stalk-map bound:', prod(b**a for a,b in [(2,3),(3,2)]))

# Degrees of AS polynomials: displayed finite instances of the degree proof.
x,y,z,t,e,a,b,c=s.symbols('x y z t e a b c')
print('\nC02 Artin-Schreier leading degrees')
for p in [2,3,5]:
    print('p=',p,' degrees h=1..5:',[p*d for d in range(1,6)],
          'independent exponents <=12:',[m for m in range(1,13) if m%p])
    assert s.Poly((x*y)**p-x*y,x,y, modulus=p).total_degree()==2*p
print('Mixed AS example h=xy has highest mixed term x^p y^p, not xy alone.')

# Blow-up chart; the inverse image ideal (x,y) becomes (x,xt)=(x).
print('\nC03 blow-up: substitute y=x*t ->',s.expand(y.subs(y,x*t)))
print('The ideal (x,x*t) equals (x); exceptional chart Spec k[t] has dimension 1.')

# Quotient surface invariants, and rational expression of the fixed field.
assert s.expand((x*x)*(y*y)-(x*y)**2)==0
print('\nC04 quotient invariant relation ac-b^2=0 verified after a=x^2,b=xy,c=y^2.')
print('With t=y/x: b=a*t, c=a*t^2; extension x^2=a has ord_a(a)=1 and e=2.')
print('Jacobian of ac-b^2:',[s.diff(a*c-b*b,v) for v in (a,b,c)])

# Cyclic inverse systems and growing kernel ranks, illustrative finite stages.
print('\nC05 nonstationary cyclic stages:',[2**m for m in range(1,8)])
for p in [2,3]:
    for m in [2,4,8]:
        mat=s.Matrix([[comb(j,i) if i<=j else 0 for j in range(m)] for i in range(m)])
        assert int(mat.det())%p==1
    print('p=',p,': conjugates (1+T)^j, 0<=j<m, form a basis mod T^m for m=2,4,8.')
print('This explains two generators for the semidirect product; kernel ranks m are unbounded.')

# Infinitesimal groups: alpha_{p^r} means ker F^r in G_a, not a product.
print('\nC06 alpha_{p^r} lengths and tangent dimensions')
for p in [2,3,5]:
    print('p=',p,[(r,p**r,1) for r in range(1,5)])
print('Columns: r, coordinate-ring length p^r, dimension of (t)/(t^2).')

# Nilpotent Frobenius coefficient matrix. Semilinearity is immaterial for kernels.
F=s.Matrix([[0,1],[0,0]])
print('\nC07 F=',F.tolist(),'dim ker F=',2-F.rank(),'dim ker F^2=',2-(F**2).rank())
assert (F-s.eye(2)).det()==1
print('F-id is invertible on this nilpotent block; fixed space is zero.')

# Elliptic point count and smoothness in characteristic 3.
p=3
pts=[(i,j) for i,j in product(range(p),repeat=2) if (j*j-i**3+i)%p==0]
print('\nC08 E/F_3: y^2=x^3-x, affine points=',pts,'plus infinity; total=',len(pts)+1)
assert len(pts)+1==4
print('Affine defining polynomial x^3-x-y^2 has d/dx=-1 mod 3, so no affine singularity.')
X,Y,Z=s.symbols('X Y Z')
hom=Y**2*Z-X**3+X*Z**2
print('Projective gradient at infinity [0:1:0]=', [s.diff(hom,v).subs({X:0,Y:1,Z:0}) for v in (X,Y,Z)])

# Non-geometrically-integral extension and finite diagonalizable lengths.
print('\nC09 C tensor_R C: over C, t^2+1=',s.factor(t*t+1,extension=s.I))
for p in [2,3,5]:
    assert s.Poly((t-1)**p-(t**p-1),t,modulus=p).is_zero
    print('C10 mu_%s: t^p-1=(t-1)^p mod p; length %s, one geometric point.'%(p,p))
M=range(6); subgroup=[0,3]; reps=[0,1,2]
cosets=[sorted((r+h)%6 for h in subgroup) for r in reps]
assert sorted(v for C in cosets for v in C)==list(M)
print('C11 group-algebra cosets for Z/2 -> Z/6:',cosets,'free rank=',len(reps))

# Jets: dual comultiplication and pushforward projection formula.
r=4
f=2+3*x+5*x*x+x**4
g=1-x+2*x**3
def coeff(poly,j): return s.expand(poly).coeff(x,j)
for j in range(r+1):
    assert coeff(f*g,j)==sum(coeff(f,i)*coeff(g,j-i) for i in range(j+1))
print('\nC12 jets: Delta(delta_j)=sum(delta_i tensor delta_(j-i)); j=0..4 verified.')
phi=x+x*x
for j in range(r+1):
    left=coeff(f.subs(x,phi)*g.subs(x,phi),j)
    right=coeff((f*g).subs(x,phi),j)
    assert left==right
print('Pushforward projection formula verified for phi=x+x^2, two degree<=4 polynomials, orders0..4.')
for rr in [1,2,3,4]:
    pairs=[(i,j) for i in range(rr+1) for j in range(rr+1) if i+j<=rr]
    print('Two-coordinate jets order',rr,': total-degree dimension',len(pairs),
          'versus tensor of separate jets',(rr+1)**2)

# S3 semidirect product, tau=(012), phi=(12).
def compose(u,v): return tuple(u[v[i]] for i in range(len(u)))
tau=(1,2,0); phi=(0,2,1)
assert compose(compose(phi,tau),phi)==compose(tau,tau)
print('\nC13 S3 cyclotomic conjugation: phi*tau*phi^-1=',compose(compose(phi,tau),phi),'=tau^2.')

# Heisenberg quotient over F_3: (a,b,c)*(u,v,w)=(a+u,b+v,c+w+a*v).
def mul(g,h,p=3):
    a,b,c=g; u,v,w=h
    return ((a+u)%p,(b+v)%p,(c+w+a*v)%p)
def inv(g,p=3):
    a,b,c=g
    return ((-a)%p,(-b)%p,(-c+a*b)%p)
A=(1,0,0); B=(0,1,0)
comm=mul(mul(mul(A,B),inv(A)),inv(B))
assert comm==(0,0,1)
print('C14 Heisenberg quotient: [A,B]=',comm,'nonzero central element; extension nonsplit.')

print('\nC15 prime-to-p part of nonzero degree d; d=0 gives infinite procyclic inertia')
for p in [2,3,5]:
    out=[]
    for d in [-12,-1,1,6,12]:
        q=abs(d)
        while q%p==0: q//=p
        out.append((d,q))
    print('p=',p,out)

# Square-zero gluing, boundary, and roots. General argument is in the proof file.
aa,bb=s.symbols('aa bb')
def mod_eps2(poly): return s.series(poly,e,0,2).removeO().expand()
assert s.expand(mod_eps2((1+e*aa)*(1+e*bb))-(1+e*(aa+bb)))==0
print('\nC16 square-zero gluing: (1+eps*a)(1+eps*b)=1+eps*(a+b) mod eps^2.')
for n in [2,3,5,7]:
    assert mod_eps2((1+e*aa/s.Integer(n))**n)==1+e*aa
    q=Fraction(1,n)
    assert q.denominator!=1 and (n*q).denominator==1
    print('n=',n,': root coefficient 1/n=',q,'is nonzero mod Z, n*(1/n)=1=0 mod Z.')
for n in [2,3,5]:
    expr=s.series(s.exp(t*aa/s.Integer(n))**n-s.exp(t*aa),t,0,6).removeO().expand()
    assert expr==0
print('Formal exponential root identity checked through t^5; exact exponential law proves all orders.')

# Extra explicit finite-jet formulas used in the manuscript comparison.
u,v=s.symbols('u v')
phi=s.Matrix([x+x*y,y+x**2])
psi=s.Matrix([u**2+v,u*v+v**2])
composed=psi.subs({u:phi[0],v:phi[1]},simultaneous=True)
chain=psi.jacobian([u,v]).subs({u:phi[0],v:phi[1]},simultaneous=True)*phi.jacobian([x,y])
assert (composed.jacobian([x,y])-chain).applyfunc(s.expand)==s.zeros(2,2)
print('\nC17 two-variable Jacobian chain rule verified symbolically.')
jet_basis=[(i,j) for i in range(5) for j in range(5-i)]
ideal_y=[ij for ij in jet_basis if ij[1]>=1]
annihilator=[ij for ij in jet_basis if ij[1]==0]
assert len(jet_basis)-len(ideal_y)==len(annihilator)==5
print('C18 order4 two-variable jets: annihilator of ideal(y) has derivative indices',annihilator)
print('This is exactly the one-variable order4 distribution space on y=0.')
# Finite root cocycle: transition exponents a_ij+a_jk=a_ik produce a mu_n defect.
q=s.symbols('q')
for n in [2,3,5]:
    root=s.exp(2*s.pi*s.I/s.Integer(n))
    assert s.simplify(root**n)==1
print('C19 finite Cech-root defect lies in mu_n for n=2,3,5; general cocycle argument is in the proof file.')
print('\nAll asserted finite calculations completed. Universal statements require independent_checks.md.')
