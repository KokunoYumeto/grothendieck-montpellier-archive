"""Exact symbolic checks for SA07 p18. Finite examples illustrate, never prove general claims.
General proofs and conventions are supplied in computations.md.
Run: python agents/p18/computations.py > agents/p18/evidence/computations.out
"""
import sympy as s
from fractions import Fraction
from math import prod

def section(name):
    print('\n'+name)

section('C01 Cycle, trace and degree bookkeeping')
p,r,d,q=s.symbols('p r d q', integer=True)
print('cycle exponent -r plus trace exponent d =',s.simplify(-r+d))
print('cohomological target degree =',q+2*r-2*d)
print('degree-zero r=d: exponent =',(-r+d).subs(r,d))
print('orientation parity p=0..5:',[(-1)**i for i in range(6)])
print('Lipman-trace extra parity n=0..5:',[(-1)**(n*(n-1)//2) for n in range(6)])

section('C02 Real forms and tensor defect')
for a in [0,1]:
    for b in [0,1]:
        target=s.I**((a+b)%2)
        product=s.I**a*s.I**b
        print('minus parities',a,b,'ambient product / additive target =',s.simplify(product/target))
print('sign Artin obstruction: q rational would require q^2=-1')
print('Tate-only tensor rule i^(a+b)=i^a*i^b holds for integer grading, not parity reduction')

section('C03 Algebraic projectors and Artin–Tate counterexample')
I=s.eye(2); c=s.Matrix([[0,1],[1,0]])
pp=(I+c)/2; pm=(I-c)/2
print('pplus idempotent:',pp*pp==pp,'pminus idempotent:',pm*pm==pm,'orthogonal:',pp*pm==s.zeros(2))
print('pminus rank:',pm.rank(),'conjugation on image:',c*pm==-pm)
print('f∞ on sign⊗Q(-1):',(-1)*(-1),'weight:',0+2,'even Tate weights are multiples of4')

section('C04 Hodge polarization parity')
for n in range(6):
    print('weight',n,'f∞ pairing factor',(-1)**n,'C inverse/C factor',(-1)**n,'combined isometry factor',(-1)**(2*n))

section('C05 Elliptic pair and quotient dimensions')
print('SL2 dimension=',2**2-1,'GL2 dimension=',2**2)
print('GL2×_Gm GL2 dimension=',2*4-1)
print('B_GL2×_Gm B_GL2 dimension=',2*3-1)
n,D=s.symbols('n D', integer=True, positive=True)
print('free diagonal torsor quotient dimension=',s.expand(n*D-D))

section('C06 Cyclotomic squares: finite projections of the Q(-2) counterexample')
primes=[3,5,7,11,13,17,19,23]
indices=[]
for l in primes:
    squares={pow(a,2,l) for a in range(1,l)}
    idx=(l-1)//len(squares);indices.append(idx)
    print('prime',l,'unit count',l-1,'square count',len(squares),'index',idx)
print('indices of product reductions for first r primes:',[prod(indices[:r]) for r in range(1,len(indices)+1)])
print('Proof for every odd prime uses cyclic F_l^×; unbounded indices 2^r prove infinite adelic index.')

section('C07 Strong approximation fails for Gm')
print('Q^× ∩ product_l Z_l^× = {−1,+1} by all prime valuations zero.')
print('Residue conditions x=1 mod3, x=2 mod5 exclude both:',[(x,x%3==1 and x%5==2) for x in [-1,1]])
print('A unit with prescribed residues exists in the compact product, so this is a nonempty open missed by Q^×.')

section('C08 Noncommutative cocycle certificates')
def inv(w): return tuple((a,-e) for a,e in reversed(w))
def mul(*words):
    out=[]
    for word in words:
        for a,e in word:
            if out and out[-1]==(a,-e):out.pop()
            else:out.append((a,e))
    return tuple(out)
def w(a): return ((a,1),)
def show(word):return ' '.join(a+('^-1' if e==-1 else '') for a,e in word) or '1'
g,tg,sg,tsg=map(w,['g','tau(g)','sigma(g)','tau(sigma(g))'])
rhs=mul(inv(tsg),tg,inv(tg),g)
lhs=mul(inv(tsg),g)
print('right coboundary tau(phi_sigma)*phi_tau:',show(rhs),'equals phi_tau_sigma:',rhs==lhs)
print('inverse becomes left cocycle by reversing product order.')
# Gauge law for right cocycles: phi'_sigma=sigma(g) phi_sigma g^-1.
tp,pt=map(w,['tau(phi_sigma)','phi_tau'])
rhs2=mul(tsg,tp,inv(tg),tg,pt,inv(g))
lhs2=mul(tsg,tp,pt,inv(g))
print('gauge law consistency:',show(rhs2),'=',show(lhs2),rhs2==lhs2)
sig,gl=map(w,['sigma_l','g_l'])
cancel=mul(sig,gl,inv(sig),sig,inv(gl))
print('finite component cancellation:',show(cancel),'equals sigma_l:',cancel==sig)
print('semidirect product (a,sigma)(b,tau)=(a sigma(b),sigma*tau): use psi=phi^-1')

section('C09 pi can belong to a minimum CURVE field of definition')
j=s.symbols('j')
A=-3*j/(j-1728); B=-2*j/(j-1728)
jcalc=s.factor(1728*4*A**3/(4*A**3+27*B**2))
disc=s.factor(-16*(4*A**3+27*B**2))
print('j(y^2=x^3+A*x+B)=',jcalc)
print('discriminant=',disc)
assert jcalc==j
print('j=pi is nonsingular; any embedded field of definition contains j=pi.')
print('This is a curve-level test. Minimal descent of the h1 motive up to isogeny is not proved by this calculation.')

section('C10 Root system A_l and G2 exact checks')
for l in range(1,6):
    vp=s.Matrix([s.Rational(l,l+1)]+[-s.Rational(1,l+1)]*l)
    print('A_'+str(l),'sum(vprime)=',sum(vp),'(l+1)*vprime=',list((l+1)*vp))
# alpha1 short; alpha2 long; Cartan entries from exact Euclidean coordinates.
a=s.Matrix([2,0]);b=s.Matrix([-3,s.sqrt(3)])
roots=[a,b,a+b,2*a+b,3*a+b,3*a+2*b]
print('G2 positive root squared lengths:',[s.expand(x.dot(x)) for x in roots])
print('G2 Cartan pairings 2(ai,aj)/(aj,aj):',[[s.simplify(2*x.dot(y)/y.dot(y)) for y in [a,b]] for x in [a,b]])
print('highest root coordinates=',list(roots[-1]))
print('crystallographic product 4cos^2(pi/m):',[(m,s.simplify(4*s.cos(s.pi/m)**2)) for m in [2,3,4,5,6]])

section('C11 Ideal valuation formula examples')
av={2:3,3:-1,5:2};bv={2:1,3:2,7:1};ps=sorted(set(av)|set(bv))
print('primes',ps)
print('product',[av.get(p,0)+bv.get(p,0) for p in ps])
print('quotient',[av.get(p,0)-bv.get(p,0) for p in ps])
print('sum',[min(av.get(p,0),bv.get(p,0)) for p in ps])
print('intersection',[max(av.get(p,0),bv.get(p,0)) for p in ps])
from sympy.ntheory.modular import crt
num,modulus=crt([8,27],[3,2]); xx=s.Rational(int(num),6)
print('CRT target x=1/2 at2, x=1/3 at3: numerator=',num,'modulus=',modulus,'x=',xx)
print('exact differences:',s.factor(xx-s.Rational(1,2)),s.factor(xx-s.Rational(1,3)))
print('denominator6 has no primes outside2,3; valuations of the differences are3 at2 and3 at3.')

section('C12 Lefschetz sl2 bridge, unit-step convention')
ell,jj=s.symbols('ell j', integer=True, nonnegative=True)
print('f e coefficient − e f coefficient =',s.expand((jj+1)*(ell-jj)-jj*(ell-jj+1)))
print('h weight=',ell-2*jj)
print('Casimir h^2+2h+4ef coefficient=',s.simplify((ell-2*jj)**2+2*(ell-2*jj)+4*jj*(ell-jj+1)))
# e raises index; f lowers with coefficient j(ell-j+1), [f,e]=h, h=ell-2j.
for l in range(1,5):
    E=s.zeros(l+1);F=s.zeros(l+1);H=s.diag(*[l-2*j for j in range(l+1)])
    for j in range(l):E[j+1,j]=1
    for j in range(1,l+1):F[j-1,j]=j*(l-j+1)
    assert F*E-E*F==H
    assert H*E-E*H==-2*E
    assert H*F-F*H==2*F
    print('string length',l,'sl2 identities exact; Casimir=',l*(l+2))
print('These finite matrices illustrate the preceding symbolic all-ell coefficient proof.')

section('C13 Degree-two P1 Lefschetz action versus Tate tensor group')
L=s.Matrix([[0,0],[1,0]]);H=s.diag(1,-1)
print('L sends unit basis to degree2:',list(L*s.Matrix([1,0])))
print('Any tensor automorphism must fix unit, so L is not an infinitesimal tensor automorphism.')

section('C14 Formal coordinate type check')
print('phi1*: P(M1)→A; psi1*:P(M2)→P(M1); valid composition phi1*∘psi1*:P(M2)→A.')
print('Written reversed composition psi1*∘phi1* is not typed without an extra identification.')

section('C15 Haar normalization and actual-image density')
print('Z_p is disjoint union of p^n cosets of p^n Z_p; normalized mass per coset is p^-n.')
print('The set {0,1} in Ga is finite; its generated subgroup Z is Zariski dense in characteristic0.')
g0=1+s.sqrt(2); conj=1-s.sqrt(2); ratio=s.simplify(g0/conj)
print('Exact note P26 test: g=1+sqrt2, conjugates g and1-sqrt2; image=',[1,ratio])
print('ratio minimal polynomial=',s.minpoly(ratio),'ratio absolute value >1 since -ratio=',-ratio)

section('C16 Unit-step matrix units and both Casimir conventions')
maxm=4; blocks=[];lowers=[];weighted=[];hs=[]
for m in range(maxm+1):
    eb=s.zeros(m+1);lb=s.zeros(m+1);fb=s.zeros(m+1)
    for j in range(m):eb[j+1,j]=1
    for j in range(1,m+1):lb[j-1,j]=1;fb[j-1,j]=j*(m-j+1)
    blocks.append(eb);lowers.append(lb);weighted.append(fb);hs.append(s.diag(*[2*j-m for j in range(m+1)]))
EE=s.diag(*blocks);LL=s.diag(*lowers);FF=s.diag(*weighted);HH=s.diag(*hs)
II=s.eye(EE.rows);BB=II-EE*LL;TT=II-LL*EE
cas=HH**2+2*HH+4*FF*EE
assert EE*FF-FF*EE==HH
offset=0
for m in range(maxm+1):
    bm=BB*(LL**m)*TT*(EE**m)*BB
    expected=s.zeros(EE.rows);expected[offset,offset]=1
    assert bm==expected
    for aa in range(m+1):
        for bb in range(m+1):
            expected=s.zeros(EE.rows);expected[offset+bb,offset+aa]=1
            assert (EE**bb)*bm*(LL**aa)==expected
    assert cas[offset:offset+m+1,offset:offset+m+1]==m*(m+2)*s.eye(m+1)
    print('m=',m,'bottom projector and',(m+1)**2,'matrix units exact; Casimir=',m*(m+2))
    offset+=m+1
print('Finite block checks illustrate the all-string proof in computations.md; they do not prove an integral algebra equality.')

section('C17 Tate conjugation and grading distinction')
zz=s.symbols('z',nonzero=True);rho=s.diag(1,zz);Ep=s.Matrix([[0,0],[1,0]]);Fp=Ep.T
print('rho E rho^-1=zE:',s.simplify(rho*Ep*rho.inv()-zz*Ep)==s.zeros(2))
print('rho F rho^-1=z^-1 F:',s.simplify(rho*Fp*rho.inv()-Fp/zz)==s.zeros(2))
ii,dd=s.symbols('i d',integer=True)
print('cohomological grading exponent',ii,'Lefschetz grading exponent',ii-dd,'difference',s.expand((ii-dd)-ii))
print('epsilon(weight cocharacter(t))=t^2 on Q(-1), whereas a section epsilon(j(t))=t is different.')
print('Elliptic H1: E:H1→H3=0, F:H1→H^-1=0, H weight1-1=0; the Lefschetz action is trivial there.')

section('C18 Semilinear versus ordinary homomorphism test')
tt=s.symbols('t');phi_tau_sigma=tt/(tt+3);product=(tt/(tt+2))*(tt/(tt+1))
print('translation test phi(tau sigma)-phi(tau)phi(sigma)=',s.factor(phi_tau_sigma-product))
assert s.factor(phi_tau_sigma-product)!=0
print('Gm representation category is semisimple, but conjugation kernel is all Gm; centre-free does not follow.')

section('C19 Order3 contraction coefficient')
xp=s.symbols('x_p');theta=s.pi/3
print('xi^2+xj^2-2cos(pi/3)xi*xj at xi=xj=xp =',s.simplify(2*xp*xp-2*s.cos(theta)*xp*xp))

section('C20 Finite-difference degree bookkeeping')
nn=s.symbols('n',integer=True)
for k in range(1,6):
    delta=s.expand(nn**k-(nn-1)**k)
    print('degree',k,'polynomial difference=',delta,'degree=',s.degree(delta,nn))
print('General antiderivative uses binomial basis: binom(n,k+1)-binom(n-1,k+1)=binom(n-1,k).')
print('\nAll executable assertions passed.')
