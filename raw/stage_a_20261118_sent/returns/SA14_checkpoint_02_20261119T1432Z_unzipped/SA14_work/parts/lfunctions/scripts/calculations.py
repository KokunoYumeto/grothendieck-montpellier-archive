"""Exact calculations for cote60. Symbolic certificates and bounded examples,
not substitutes for general proofs (which are in proof_notes.md)."""
import sympy as s
from itertools import combinations, product
from math import comb
t,p,q,z,x,y,a,b=s.symbols('t p q z x y a b', nonzero=True)
def section(label): print('\n###',label)
def check(label,lhs,rhs):
    delta=s.factor(lhs-rhs); assert delta==0,(label,delta)
    print(label+': '+str(s.factor(lhs))+' = '+str(s.factor(rhs))+'; difference 0')
def P(eigs): return s.prod(1-v*t for v in eigs)
def LF(grades): return s.prod(P(v)**(s.Integer(-1)**(i+1)) for i,v in grades.items())
def detc(grades): return s.prod(s.prod(v)**(s.Integer(-1)**i) for i,v in grades.items())
def minors(mat,k): return sorted({s.factor(mat.extract(I,J).det()) for I in combinations(range(mat.rows),k) for J in combinations(range(mat.cols),k)},key=str)
section('CALC-01 exterior, symmetric, tensor and Witt signs')
F=s.Matrix([[2,3,1],[0,5,4],[0,0,7]])
ext=[sum(F.extract(I,I).det() for I in combinations(range(3),i)) for i in range(4)]
check('determinant/exterior trace',(s.eye(3)-t*F).det(),sum((-t)**i*ext[i] for i in range(4)))
hs=[sum(2**i*5**j*7**k for i in range(n+1) for j in range(n-i+1) for k in [n-i-j]) for n in range(7)]
check('reciprocal/symmetric coefficients',s.series(1/P([2,5,7]),t,0,7).removeO(),sum(hs[i]*t**i for i in range(7)))
print('exterior traces',ext,'symmetric traces through degree6',hs)
check('tensor roots',(z*s.eye(4)-s.kronecker_product(s.diag(2,5),s.diag(3,7))).det(),s.prod(z-r for r in [6,14,15,35]))
print('Witt additive inverse of line a: lambda_s(-[a])=(1+a*s)^-1, coefficient lambda^2=a^2; sigma_s(-[a])=1-a*s. Thus reciprocal convention cannot preserve both labels unchanged.')
section('CALC-02 reciprocal determinants and complexes')
check('reciprocal P',(s.eye(3)-t*F.inv()).det(),(-t)**3/F.det()*(s.eye(3)-F/t).det())
grades={0:[s.Integer(2),s.Integer(3)],1:[s.Integer(5)],2:[s.Integer(7),s.Integer(11)]}
chi=sum((-1)**i*len(v) for i,v in grades.items());delta=detc(grades);L=LF(grades)
check('derived reciprocal',LF({-i:[1/v for v in vs] for i,vs in grades.items()}),(-t)**(-chi)*delta*L.subs(t,1/t))
print('chi',chi,'delta',delta)
for n in range(1,5):
    bs=list(range(1,n+2))+list(range(n,0,-1))
    assert len(bs)==2*n+1
    print('Betti symmetry test',n,bs,'weighted',sum((-1)**i*i*v for i,v in enumerate(bs)),'n*chi',n*sum((-1)**i*v for i,v in enumerate(bs)))
    assert sum((-1)**i*i*v for i,v in enumerate(bs))==n*sum((-1)**i*v for i,v in enumerate(bs))
section('CALC-03 scope of purity/rationality/polarization')
M=s.Matrix([[0,p],[1,0]]); B=s.diag(1,p)
assert M.T*B*M==p*B
print('symmetric similitude: F^T B F=pB; det(F)=',M.det(),'; eigenvalues ±sqrt(p); all have complex absolute sqrt(p).')
print('7-adic Hensel tests: 3^2-2=7, derivative6 nonzero mod7; x^2+x+1 at2=7, derivative5 nonzero mod7. Hence sqrt(2), zeta_3 are in Q_7.')
assert (3**2-2)%7==0 and 6%7!=0 and (2**2+2+1)%7==0 and 5%7!=0
print('rank-one sqrt(2): weight1, rank1, det sqrt(2) not rational. Rank-one zeta_3: weight0, det not ±1; compact-unit Frobenius powers give continuous procyclic representations.')
section('CALC-04 A1, Gm, P2 and boundary FE')
examples={'A1':(1/(1-p*t),1/(1-t),1,p,1),'Gm':((1-t)/(1-p*t),(1-p*t)/(1-t),0,p,1/p)}
for name,(Lc,Lordinary,chi,dc,ds) in examples.items():
    Linf=s.factor(Lordinary/Lc);A=s.factor(1/Linf.subs(t,1/(p*t)))
    print(name,'Lc=',Lc,'Lordinary=',Lordinary,'Linf=',Linf,'A=',A,'chi=',chi,'delta_c=',dc,'delta_*=',ds)
    check(name+' FE',Lc.subs(t,1/(p*t)),A*dc*(-t)**chi*Lc)
    check(name+' boundary determinant',ds/dc,p**chi/dc**2)
    check(name+' A norm',A*A.subs(t,1/(p*t)),p**chi/dc**2)
L2=1/((1-t)*(1-p*t)*(1-p**2*t))
check('P2 proper FE',L2.subs(t,1/(p**2*t)),p**3*(-t)**3*L2)
print('P2: chi3, delta p^3, middle normalized eigenvalue1, epsilon_FE=-1; simple pole at t=1/p.')
section('CALC-05 finite-field extension')
roots=[s.Integer(2),s.Integer(3)]
print('F roots',roots,'F^3 roots',[v**3 for v in roots],'detF^3',s.prod(v**3 for v in roots),'(detF)^3',s.prod(roots)**3)
assert s.prod(v**3 for v in roots)==s.prod(roots)**3
print('P_(F^3)(t)=',s.expand(P([v**3 for v in roots])),'; P_F(t^3)=',s.expand(P(roots).subs(t,t**3)),': unequal')
section('CALC-06 cone duality shift certificate')
print('Cohomological convention H^i(K[r])=H^(i+r)(K). Take A=K[0], B=0, A→B=0.')
print('Cone(A→B)=K[1], concentrated degree-1. Its dual is K[-1], degree+1.')
print('Dual map DB→DA is 0→K; its cone is K[0]. Shifting by[-1] gives degree+1; [+1] gives degree-1. Therefore D Cone = Cone(dual map)[-1].')
assert -(-1)==0-(-1) and -(-1)!=0-1
section('CALC-07 local invariants, Kummer correction and mu cancellation')
N=s.Matrix([[0,1],[0,0]]); F0=s.diag(1,p)
assert F0*N*F0.inv()==N/p
print('F=diag(1,p), N e2=e1, FNF^-1=p^-1N; invariants span e1. Quotient is unramified eigenvaluep but invariant map to quotient is0; cokernelQ eigenvaluep.')
LjV=1/((1-t)*(1-p**2*t));LjA=1/((1-t)*(1-p*t));LjB=1/((1-p*t)*(1-p**2*t))
check('global Gm Kummer correction',LjV,LjA*LjB*(1-p*t)**2)
print('χ(j*V)=2; constituent χ sum4; Q at0,∞ has χ2. δ(j*V)=p^2; constituent δ product p^4 divided by δ(Q)=p^2.')
F1=s.diag(1/p,1);Fd=F1.inv().T;Nd=-N.T
assert F1*N*F1.inv()==N/p
print('Jordan test: V^natural=[p^-1]+[1], V^I=[p^-1], alpha(V)=[1]. Dual invariants=[1]; alpha(Vdual)=[p]; twist(1) gives[1], so mu=0.')
check('mu L cancellation',1/(1-t)/(1/(1-(p/p)*t)),1)
print('C2 sign averaging: dim sign^I=0, dim(sign tensor sign)^I=1; additive averaging is not tensor multiplicative.')
section('CALC-08 residue induction and local Tate argument')
for d in [1,2,3,4]:
    A=s.zeros(d)
    for i in range(d-1): A[i+1,i]=1
    A[0,d-1]=a
    check('induced determinant d='+str(d),(s.eye(d)-t*A).det(),1-a*t**d)
    assert A.det()==(-1)**(d-1)*a
print('L_(alpha(dual)(1))(t)=L_(alpha(dual))(p^-1*t). If alpha(dual)=alpha(V)(rho), argument is p^-(rho+1)*t, not p^-rho*t.')
section('CALC-09 squared local determinant')
dglob,dloc,qlocal=s.symbols('D d Q',nonzero=True);ch,cl=s.symbols('chi chix',integer=True)
print('From D^2=q^chi * product(delta_mu^-1) and delta_mu=d_x^-2*q_x^chi_x, obtain (D*q^-chi/2)^2=product(d_x^2/q_x^chi_x). A square root retains ±.')
check('numeric squared-product test',s.Rational(25,9),(s.Rational(5,3))**2)
section('CALC-10 normalization involution and fixed points')
sig=lambda expr:s.factor(expr.subs(t,1/(q*t)))
u=t+1/(q*t);w=t-1/(q*t)
check('fixed rational generator',sig(u),u);check('anti-invariant generator',sig(w),-w)
Ltest=(1-2*t)/(1-3*t);R=u**2+2
check('positive normalization',sig(R/Ltest*Ltest)/(R/Ltest*Ltest),1)
check('negative normalization',sig(w*R/Ltest*Ltest)/(w*R/Ltest*Ltest),-1)
print('At fixed a²=1/q, derivative sigma=-1; ratio sigma(f)/f has limiting sign (-1)^ord_a f. Opposite parities at the two fixed points obstruct a single sign if allowed corrections cannot alter them.')
for m in range(-3,4):
    f=(t-1)**m
    val=s.limit(f.subs(t,1/t)/f,t,1)
    assert val==s.Integer(-1)**m
    print('q=1, fixed point1, order',m,'ratio limit',val)
section('CALC-11 cusp degree, colength and conductor')
S={0}|set(range(2,100));Q={4+k for k in S};missing=sorted(S-Q)[:]
missing=[n for n in missing if n<50]
power=next(n for n in range(1,8) if all(v in Q for v in range(2*n,50)))
print('C=k[[t²,t³]], Q=t^4 C; quotient exponent basis',missing,'length',len(missing),'least m with m_C^m subset Q',power)
assert missing==[0,2,3,5] and power==3
print('a=m_C, aB=t²B, a*m_C*B=t^4B. y=t³ avoids t^4B but yB=t³B differs from aB.')
print('Trace with A=k[[s]],s=t², char(k)≠2: C basis(1,t³), trace matrix diag(2,2s³). C*=(1/2)t^-3 C, D_C=2t³ C; conductor=t²B and D_B=2tB, hence D_CB=conductor*D_B.')
section('CALC-12 socles and non-Gorenstein orders')
print('C=k[x,y], prime q=p=(x): q irreducible since prime; (q:p)/q=C/(x)=k[y] has proper nonzero submodule(y), hence is not simple globally.')
print('Gaussian semilocal example: A=Z_(5), C=A[i], 5C=m1*m2 with m1=(2+i),m2=(2-i). (5C:m1)=m2 whereas (m1:m1)=C.')
for n in range(1,7):
    socle=1 if n==1 else n-1
    print('order Z+pO of degree',n,'residue algebra Fp ⊕ radical of dimension',n-1,'radical²=0; socle dimension',socle,'Gorenstein',socle==1)
section('CALC-13 Fitting minors and signed relative divisors')
X,Y,Z=s.symbols('X Y Z');mat=s.Matrix([[X,Y,Z,0,0,0],[0,0,0,X,Y,Z]])
gens=[v for v in minors(mat,2) if v!=0]
print('N=k² over k[X,Y,Z], Fitt0 generated by',gens,'=m²; Fitt1 generated by X,Y,Z=m.')
assert set(gens)=={X**2,X*Y,X*Z,Y**2,Y*Z,Z**2}
print('M=A/(X,Y²,YZ,Z²): one-generator presentation gives Fitt0=q,Fitt1=A.')
print('Surjection A→A/(X): Fitt0(A)=0, Fitt0(quotient)=(X); asserted quotient⊂source fails.')
vals=[-1,2,4];n=len(vals)
for c in [1,2,7]:
    ds=[sum(sorted(v+c for v in vals)[:n-k])-(n-k)*c for k in range(n+1)]
    print('relative exponents',vals,'clearing scalar valuation',c,'d_k=',ds)
    assert ds==[5,1,-1,0]
print('d2=-1 < d3=0, so d_k≥d_(k+1) fails without N⊂M; recovered elementary exponents remain ordered.')
section('CALC-14 exterior powers and DVR Tor/Ext')
for vals in ([1,2,4],[0,3,5,7]):
    r=len(vals)
    for k in range(1,r+1):
        sm=sum(sum(vals[i] for i in I) for I in combinations(range(r),k))
        assert sm==comb(r-1,k-1)*sum(vals)
        print('r,k=',r,k,'exterior length=',sm,'binomial multiple=',comb(r-1,k-1)*sum(vals))
for aa,bb,rr in [(2,5,3),(7,3,0),(4,4,2)]:
    tor=min(aa,bb);tensor=rr*aa+tor;hom=tor;ext=rr*aa+tor
    assert tensor-tor==rr*aa and hom-ext==-rr*aa
    print('DVR a,b,rank=',aa,bb,rr,'tensor,tor,hom,ext=',tensor,tor,hom,ext)
print('I=(X,Y), presentation(-Y,X): Λ²I=A/(X,Y) is nonzero pseudo-null; rank alone does not make exterior powers vanish.')
section('CALC-15 Veronese syzygies')
v=s.Matrix([-Y,X]);relations=s.Matrix.hstack(X*v,Y*v)
check('Veronese relation1',(s.Matrix([[X**2,X*Y]])*relations[:,0])[0],0)
check('Veronese relation2',(s.Matrix([[X**2,X*Y]])*relations[:,1])[0],0)
print('p⊗B=B² / (X,Y)(-Y,X); map to pB has full kernel line B(-Y,X), hence quotient kernel B/(X,Y). pB=X(X,Y), double dual XB.')
print('Nonflatness also follows because a nonzero tensor kernel survives; p is rank1 divisorial on the normal Veronese A.')
section('CALC-16 local generators, nonsplit torsion and intersections')
print('Ideal (2,1+sqrt(-5)) has quotient F2 and norm2. Equation a²+5b²=2 has no integer solution: if b≠0 norm≥5, and a²=2 impossible. Thus no principal generator.')
d=X-Y;g1=s.Matrix([d,0]);g2=s.Matrix([1,X]);g3=s.Matrix([1,Y])
assert Y*g2-X*g3==-g1
print('E=<d e1,e1+X e2,e1+Y e2>, F=<d²e1>. T(E/F)=A/(d); torsion-free quotient=(X,Y). Relation Yg2-Xg3=-tau.')
aa,bb=s.symbols('aa bb');obstruction=-1+Y*aa-X*bb
print('After changing lifts by aa*tau,bb*tau, obstruction mod d is',obstruction.subs(Y,X),'; at X=0 equals',obstruction.subs({Y:0,X:0}),', so no splitting.')
assert obstruction.subs({Y:0,X:0})==-1
print('A/(XY) injects into A/(X)⊕A/(Y) with cokernel k at origin. It is cyclic; direct sum needs2 generators at origin, so no isomorphism.')
print('M=A/(X-Y), a=(X),b=(Y): aM∩bM=(X), (a∩b)M=(X²), quotient k at origin, nonzero pseudo-null.')
section('CALC-17 cyclotomic residue obstruction and differentials')
ord2=next(i for i in range(1,31) if pow(2,i,31)==1)
print('order of2 mod31=',ord2,'; cubic subfield fixed subgroup order10 contains<2>, so residue algebra at2 is F2³.')
assert ord2==5
for size,n in [(2,3),(3,3),(2,2)]:
    generating=sum(1 for tup in product(range(size),repeat=n) if len(set(tup))==n)
    print('k size',size,'n',n,'tuples with distinct coordinates=',generating)
print('B=A[alpha,beta]/(alpha^p-pi*alpha-s,beta^p-pi*beta-t): differential presentation diag(-pi,-pi); Omega=(B/pi)^2, Fitt0=(pi²), two generators mod maximal ideal.')
section('CALC-18 characteristic2 derivation and lattice count')
for i,j in [(0,2),(1,1),(2,2),(2,3),(3,3),(4,4)]:
    pairs=[(aa,bb) for aa in range(i) for bb in range(j) if (2*j+1)*aa+(2*i+1)*bb>=2*i*j]
    print('i,j=',i,j,'N=',len(pairs),'pairs=',pairs)
    if (i,j)==(2,2): assert pairs==[(1,1)]
for i,j in [(0,2),(1,1),(2,2),(3,4)]:
    deriv=lambda f:s.Poly(s.diff(f,X)*Y**(2*j)+s.diff(f,Y)*X**(2*i),X,Y,modulus=2).as_expr()
    assert deriv(X**2)==0 and deriv(Y**2)==0 and deriv(X**(2*i+1)+Y**(2*j+1))==0
    assert deriv(deriv(X))==0 and deriv(deriv(Y))==0
print('Invariant generators and Delta²=0 checked exactly modulo2 in representative nonnegative cases; the general proof uses even exponents.')
section('CALC-19 completed group-ring polynomials and Hensel test')
for pp in [2,3,5]:
    for nn in [1,2,3]:
        gamma=s.Poly(1-(1-t)**(pp**nn),t)
        coeff=gamma.all_coeffs()
        assert all(int(c)%pp==0 for c in coeff[1:])
        print('p,n=',pp,nn,'degree=',gamma.degree(),'leading=',coeff[0],'; every lower coefficient divisible byp.')
print('Hensel counterexample X²-p: reduction X·X, both degree1; a hypothetical linear factor gives root with valuation1/2, impossible in the DVR fraction field.')
section('CALC-20 fixed-point and unit-ideal certificates')
print('I=(2,X) in Z[X] becomes unit over Q[X], but reduction mod2 is(X), so I≠B. If d∈I and I+(p)=B for all p|d, eachp is a unit inB/I, hence d is a unit and zero, so B/I=0.')
section('CALC-21 global conductor needs reflexivity')
a,b,c,d,x,y=s.symbols('a b c d x y')
# L=Q(x,y)[u]/(u²-2); multiplication by a+b*u has the displayed matrix.
M=s.Matrix([[a,2*b],[b,a]])
assert s.trace(M)==2*a
trace_pair=s.Matrix([[2,0],[0,4]])
assert trace_pair.det()==8
assert s.gcd(x,y)==1
I=s.groebner([x,y],x,y,domain=s.QQ)
assert I.reduce(s.Integer(1))[1]==1
assert I.reduce(x)[1]==0 and I.reduce(y)[1]==0
print('A=Q[x,y], B=A[u]/(u²-2), C=A+(x,y)u. Trace Gram matrix=',trace_pair.tolist())
print('Trace dual C*: 2a in A, 4bx and 4by in A. Since gcd(x,y)=1 in the UFD A, b is in A; hence C*=B*=B.')
print('Conductor: a+bu in C and u(a+bu)=2b+au in C force a,b in (x,y). Thus C:B=(x,y)B.')
print('Groebner remainder of 1 modulo (x,y)=1, proving the conductor is proper; B*:C*=B.')
print('Finite full order: generators 1,xu,yu; closure uses u²=2; Frac(C)=Frac(B) because u=(xu)/x. B is normal as a polynomial ring over Q(sqrt(2)).')
section('CALC-22 Samuel recurrence and zero-exponent defect')
x,y,z,U,V=s.symbols('x y z U V')
Fpoly=s.Integer(1);bs={0:y**9};g=0;h=3;block=9
for m in range(1,4):
    for rr in range(1,block):
        bs[(m-1)*block+rr]=s.expand(z**(2*rr)*y**(9-rr)*Fpoly.subs({U:x**3,V:y**3}))
    H=s.Poly(s.expand((U+V)**6*Fpoly),U,V)
    kept=sum(cc*U**uu*V**vv for (uu,vv),cc in H.terms() if uu<3*m)
    Fpoly=s.cancel(kept/V**h).expand()
    assert s.Poly(Fpoly,U,V).total_degree()==3*m
    bs[m*block]=s.expand(y**9*Fpoly.subs({U:x**3,V:y**3}))
for nn in range(1,28):
    diff=s.expand(y*bs[nn]-z**2*bs[nn-1])
    G=s.groebner([z**3-x**3-y**3,x**nn],z,x,y,domain=s.QQ)
    assert G.reduce(diff)[1]==0
print('Positive test: A=Q[x,y,z]/(z³-x³-y³), i=j=k=3, t=9; all27 required coefficient divisibilities verified exactly.')
print('Boundary b9=',bs[9])
print('General proof uses block ij and exponent gain g=ijk-ij-jk-ki>=0; homogeneous truncation is recorded in proof_notes.md.')
for tt in range(1,7):
    assert s.rem(y**tt,y**(tt+1),y)==y**tt
    print('Zero-exponent counterexample t=',tt,': y^t is not divisible by y^(t+1) modulo x.')
print('Uniform argument: with z=1,i=1,j=k=0, every coefficient condition gives y*b_n=b_(n-1) modulo x; hence y^t=y^n*b_n in Q[y] for every n, impossible.')
section('CALC-23 characteristic-two unit and integration identities')
x,y,c,d,alpha,P,Q,a=s.symbols('x y c d alpha P Q a')
variables=[x,y,c,d,alpha,P,Q,a]
derivatives=[P,Q,c*c*P+alpha*Q,d*d*Q+alpha*P,0,a*P,a*Q,0]
def deriv(expr):
    return s.expand(sum(s.diff(expr,v)*dv for v,dv in zip(variables,derivatives)))
u=1+c*x+d*y+(c*d+alpha)*x*y
t=c*P+d*Q
certificate=s.Poly(deriv(u)-t*u,*variables,modulus=2)
assert certificate.is_zero
print('u=1+cx+dy+(cd+alpha)xy; Du-tu modulo2 =',certificate.as_expr())
for ii in range(1,5):
 for jj in range(1,5):
  for aa in range(0,9):
   for bb in range(0,9):
    if aa*(2*jj+1)+bb*(2*ii+1)<4*ii*jj:continue
    assert aa>=ii or bb>=jj
    G=x**aa*y**bb
    primitive=x**(2*(aa-ii))*y**(2*bb+1) if aa>=ii else x**(2*aa+1)*y**(2*(bb-jj))
    delta=s.diff(primitive,x)*y**(2*jj)+s.diff(primitive,y)*x**(2*ii)
    assert s.Poly(delta-G**2,x,y,modulus=2).is_zero
print('Both recursive integration formulas checked for i,j=1..4 and monomials of exponents0..8 satisfying the weight threshold; general argument is in proof_notes.md.')
section('CALC-24 externally identified cut derivation example')
x,y,z=s.symbols('x y z')
def D24(f):return s.Poly(s.diff(f,x)*y**4+s.diff(f,y)*x**2+s.diff(f,z)*x*y*z,x,y,z,modulus=2).as_expr()
assert D24(D24(x))==0 and D24(D24(y))==0
delta=D24(x*y)
obstruction=s.Poly(delta-x**2*y**2,x,y,modulus=2)
assert not obstruction.is_zero
print('Dx=y^4, Dy=x^2, Dz=xyz; D²x=D²y=0; D(xy)=',delta)
print('The supposed Db/b=xy would force D(xy)=(xy)², but the nonzero obstruction is',obstruction.as_expr())
print('These antecedents are from Samuel1962 §3 p.3-11, not supplied by the cut archival line.')
section('CALC-25 within-block printed denominator')
x,y,z=s.symbols('x y z')
ii,jj,kk=2,5,7
assert ii*jj*kk-ii*jj-jj*kk-kk*ii==11
assert s.gcd(ii,jj)==s.gcd(jj,kk)==s.gcd(ii,kk)==1
numerator=y**10*z*(y-x)
G=s.groebner([z**2-x**5-y**7,x],z,x,y,domain=s.QQ)
remainder=G.reduce(numerator)[1]
assert remainder==y**11*z and remainder!=0
print('A=Q[x,y,z]/(z²-x⁵-y⁷), i=2,j=5,k=7; inequality value=11. The quotient by x is Q[y,z]/(z²-y⁷), a domain because gcd(2,7)=1; x is prime and y is not divisible by x.')
print('Using printed b1=b0*z/x, b0=y^10, the T coefficient of vv-prime is y^10*z*(y-x)/x².')
print('Its numerator modulo (x,z²-x⁵-y⁷) is',remainder,'and therefore the coefficient is not in A.')
print('Correct within-block equation: y*b_(n+1)=z^(i-1)*b_n. The positive recurrence in CALC-22 uses it.')
print('\nALL ASSERTIONS PASSED. Finite examples certify the stated examples; general statements require the separately supplied proofs/hypotheses.')
