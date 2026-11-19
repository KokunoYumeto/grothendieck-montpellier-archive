"""Exact algebraic checks for SA13 p3. Python3 + SymPy; no numerical tolerances.

Finite examples illustrate the accompanying symbolic proofs. They are not
claimed as general certificates for sheaves, abelian schemes, or monodromy.
The counterexamples are algebraic and all their hypotheses are given below.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial,comb
import sympy as s

def mod1(x): return x-(x.numerator//x.denominator)

print('C-SA13-309: two finite-group Dirac normalizations')
for m in (1,2,3,7):
    delta=[1]+[0]*(m-1); normalized=[m]+[0]*(m-1)
    print(m, 'counting=',sum(delta),sum(normalized),
          'probability=',F(sum(delta),m),F(sum(normalized),m))

print('\nC-SA13-262/263: torsion presentation, M=Z, G=Q/Z, u(1)=1/d')
for n,d in ((2,3),(3,5),(5,2)):
    pairs=[(m,mod1(F(m,d*n)+F(j,n))) for m,j in product(range(n),repeat=2)]
    assert len(set(pairs))==n*n
    assert all(mod1(n*g-F(m,d))==0 for m,g in pairs)
    def add(a,b):
        m=a[0]+b[0];carry,m=divmod(m,n)
        return m,mod1(a[1]+b[1]-F(carry,d))
    assert all(add(a,b) in pairs for a,b in product(pairs,repeat=2))
    for a in pairs:
        total=(0,F(0))
        for _ in range(n): total=add(total,a)
        assert total==(0,F(0))
    print('n=',n,'d=',d,'|Vn|=',len(pairs),'|kernel|=',sum(m==0 for m,g in pairs),
          'quotient residues=',sorted(set(m for m,g in pairs)))

print('\nC-SA13-266/290: e_N on (Z/N)^2, transition power checked additively')
def e(N,x,y): return mod1(F(x[0]*y[1]-x[1]*y[0],N))
for n,m in ((2,3),(3,2),(3,3)):
    N=m*n
    points=list(product(range(N),repeat=2))
    for x,y in product(points,repeat=2):
        # The multiplication-m map sends coordinates x at levelN to x modn.
        # These coordinates use x/N in Q/Z, so mx/N=x/n.
        assert e(n,tuple(t%n for t in x),tuple(t%n for t in y))==mod1(m*e(N,x,y))
    print('n=',n,'m=',m,'all',N**4,'simultaneous transition pairs agree')
for n in (2,3,4):
    pts=list(product(range(n),repeat=2))
    characters={tuple(e(n,x,y) for y in pts) for x in pts}
    assert len(characters)==n*n
    print('perfect symplectic finite pairing at n=',n,':',len(characters),'distinct characters')

print('\nC-SA13-268: filtered perfectness illustration')
a,b,c=s.symbols('a b c')
matrix=s.Matrix([[1,a,b],[0,1,c],[0,0,1]])
assert matrix.det()==1
print('det of an upper triangular filtered pairing with unit graded diagonals =',matrix.det())

print('\nC-SA13-274: colimit Z/n with multiplication transitions')
for n,m in ((2,3),(3,4),(5,7)):
    for h in range(n): assert mod1(F(h,n))==mod1(F(m*h,m*n))
    print('Z/',n,'→Z/',m*n,': h↦',m,'h agrees with h/n modZ')
print('Every h/n modZ is killed by n; Q is torsion-free. The two limits cannot agree for H=Z.')

print('\nC-SA13-276: norm from C to R')
x,y=s.symbols('x y',real=True)
norm=s.expand((x+s.I*y)*(x-s.I*y))
assert norm==x*x+y*y
print('N(x+iy)=',norm,'>0 for (x,y)≠(0,0); every positive real is a square.')
print('Thus R*/N(C*) has two classes; the -1 class gives Br(R)≠0.')

print('\nC-SA13-279: dual-number character of Ga')
eps,x,y=s.symbols('eps x y')
def dual(expr): return s.Poly(s.expand(expr),eps).rem(s.Poly(eps**2,eps)).as_expr()
assert dual((1+eps*x)*(1+eps*y))==1+eps*(x+y)
print('mod eps²:',dual((1+eps*x)*(1+eps*y)))

print('\nC-SA13-270/286: absolute Artin–Schreier H0 term over Fp')
for p in (2,3,5,7):
    values={ (pow(a,p,p)-a)%p for a in range(p)}
    assert values=={0}
    print('p=',p,'image(F-1)=',sorted(values),'cokernel dimension overFp=1')

print('\nC-SA13-295: finite torsion pairings lost by inverse limit')
for ell in (2,3,5):
    for r in range(1,5):
        def phi(a,b): return mod1(F(a*b,ell))
        assert phi(1,1)==F(1,ell)
        assert all(mod1(ell*phi(a,b))==0 for a,b in product(range(ell),range(ell**r)))
        assert all((ell*a)%ell==0 for a in range(ell))
    print('ell=',ell,': phi_r(1,1/ell^r)=1/ell for r=1..4; P transition is zero; limitP=0')

print('\nC-SA13-301: higher Leibniz factorial coefficients')
for n in range(9):
    assert all(F(comb(n,r),factorial(n))==F(1,factorial(r)*factorial(n-r)) for r in range(n+1))
print('binomial(n,r)/n! = 1/(r!(n-r)!) verified for n=0..8; general identity is in review.md.')
N=s.Matrix([[0,1,0],[0,0,1],[0,0,0]])
I=s.eye(3)
expN=I+N+N*N/2; expminusN=I-N+N*N/2
def ad(X): return N*X-X*N
def expad(X):
    val=s.zeros(3);term=X
    for r in range(6):
        val+=term/factorial(r);term=ad(term)
    assert term==s.zeros(3)
    return val
basis=[]
for i,j in product(range(3),repeat=2):
    X=s.zeros(3);X[i,j]=1;basis.append(X)
    assert expad(X)==expN*X*expminusN
assert all(expad(X*Y)==expad(X)*expad(Y) for X,Y in product(basis,repeat=2))
print('On M3(Q), exp(adN) equals conjugation by expN; all81 products of matrix units checked.')
for p in (2,3,5):
    x=s.symbols('x');f=x**p
    val=sum(s.diff(f,x,r)*pow(factorial(r),-1,p) for r in range(p))
    lhs=s.Poly(val,x,modulus=p).as_expr()
    rhs=s.Poly((x+1)**p,x,modulus=p).as_expr()
    assert s.Poly(rhs-lhs,x,modulus=p).as_expr()==1
    print('char',p,': D=d/dx has D^p=0, truncatedexp(D)(x^p)=',lhs,'but(expD(x))^p=',rhs)

print('\nA36: weakened subspace-trace assertion does not imply full-trace assertion')
for p in (2,3,5):
    dim=p-1
    subtraces={d%p for d in range(dim+1)}
    fulltraces={dim%p}
    assert subtraces==set(range(p)) and len(fulltraces)==1
    print('p=',p,'G={identity} onFp^',dim,': subspace traces=',sorted(subtraces),'whole-space traces=',sorted(fulltraces))
print('G is trivial, hence a p-group: the deleted stronger consequences do not follow from the revised theorem.')

print('\nA36: high-degree norm form on F2 in two variables')
pts=list(product(range(2),repeat=2))
for d in (2,3,4):
    # Norm_{F_(2^d)/F2}(x+y alpha), with alpha degree d and constant term1.
    # At the three nonzero F2-pairs this norm is1; explicit smallforms follow.
    forms={2:lambda x,y:x*x+x*y+y*y,
           3:lambda x,y:x**3+x*y*y+y**3,
           4:lambda x,y:x**4+x*y**3+y**4}
    zeros=[(x,y) for x,y in pts if forms[d](x,y)%2==0]
    assert zeros==[(0,0)]
    print('degree',d,': zeros=',zeros)
print('General norm proof: any n+1 linearly independent elements of F_(q^d), d≥n+1, give a norm form with no nonzero Fq-zero.')

print('\nA36: selection inequality and product degree arithmetic')
for r,d,n in ((2,2,1),(3,2,2),(1,3,2)):
    total=r*d**n
    assert all(N<=total for N in range(total+1))
    print('finite intersection size=',total,': selectingN points requires N≤',total,'not N≥',total)
for d1,n in ((2,2),(3,4)):
    threshold=(d1+1)*(n+1)
    assert all(d-d1*(n+1)>=n+1 for d in range(threshold,threshold+10))
    print('threshold',threshold,': d=d1(n+1)+d3 with d3≥n+1')

print('\nA36: Frobenius eigenvalues may require a nontrivial power to become0/1')
for p in (3,5,7):
    assert all(pow(a,p-1,p) in (0,1) for a in range(p))
    print('Fp eigenvalues after exponent',p-1,'are0 or1')
print('\nAll asserted finite/symbolic checks passed. General sheaf/geometric proofs are separately labelled in review.md.')
