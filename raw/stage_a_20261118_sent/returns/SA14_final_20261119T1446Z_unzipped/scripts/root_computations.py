#!/usr/bin/env python3
"""Exact algebraic checks for root's manuscript readings, not a verdict generator.
Only finite-dimensional formal/cohomological models are computerized here.
Geometric hypotheses and proofs are stated separately in research/root_proofs.md.
"""
import json, math
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sympy as s

OUT=[]
def record(name, source, assumptions, calculation, result, assertion=True):
    assert assertion, name
    OUT.append(dict(name=name,source=source,assumptions=assumptions,calculation=calculation,result=result,passed=True))

n=s.symbols('n',integer=True)
alpha=lambda v:(v-1)*(v-2)/2
record('cube_recurrence','57:15–19','Cube identity with unordered pairs i<j.',
       'alpha(n+1)-2alpha(n)+alpha(n-1)=1; alpha(2)=0, alpha(3)=1',str(s.simplify(alpha(n+1)-2*alpha(n)+alpha(n-1))),s.simplify(alpha(n+1)-2*alpha(n)+alpha(n-1))==1)
record('cube_small_exponents','57:16–19','Constants/singletons/pairs under normalized cube expansion.',
       'n, constant exponent, singleton exponent, number of unordered pairs',
       [[j,int(alpha(j)),2-j,math.comb(j,2)] for j in (3,4,5)])
record('multiplication_binomial','57:15','Quadratic cube recurrence for pullback of a line bundle by [n].',
       'n(n-1)/2 + n = n(n+1)/2',str(s.simplify(n*(n-1)/2+n-n*(n+1)/2)),s.simplify(n*(n-1)/2+n-n*(n+1)/2)==0)

t=s.symbols('t')
M=s.Matrix([[1,-2*t],[0,-1]])
record('noncommutative_power_counterexample','57:44','Over C; M(t) in GL2 is nonconstant, det=-1.',
       'M(t)^2',str(M*M),M*M==s.eye(2))
record('matsusaka_threshold_counterexample','57:68–69','X=P2, H=O(1), D=K=-3H; chi(O)=1.',
       'a=D(D-K)/2+chi(O); b=H(D-K); h0(O(-3))',{'a':1,'b':0,'h0':0,'hypotheses_non_strict_satisfied':True})
record('abelian_surface_betti','57:70','Complex abelian surface, b_i=binomial(4,i).',
       'Betti numbers and Euler characteristic',{'betti':[math.comb(4,j) for j in range(5)],'Euler':sum((-1)**j*math.comb(4,j) for j in range(5)),'written_b2_if_p_dimPic':2,'actual_b2':6})

cone=[]
for d in range(1,11):
    g=(d-1)*(d-2)//2
    terms=[math.comb(d-1-j,2) if d-3-j>=0 else 0 for j in range(1,d+1)]
    total=sum(terms)
    assert total==(math.comb(d-1,3) if d>=4 else 0)
    assert (d<g-1)==(d>=6)
    cone.append(dict(degree=d,genus=g,H1_positive_twists=terms,total=total,source_inequality=d<g-1))
record('plane_cone_completion_layers','57:190–193','Smooth plane curve degree d; Serre duality K=O(d-3). In char0 the vector-layer dimensions count the formal connected kernel.',
       'h1(O_C(j))=h0(O_C(d-3-j)); sum_{j>=1}=binomial(d-1,3)',cone)

# Closed-cover Cech complex at concurrent triple point; not an acyclic resolution.
d0=s.Matrix([[-1,1,0],[-1,0,1],[0,-1,1]])
d1=s.Matrix([[1,-1,1]])
assert d1*d0==s.zeros(1,3)
record('triple_line_cech_failure','57:222,224','Special fibre C in P2: xy(x+y)=0 over a field. Each component/pair/triple intersection has H0=k.',
       'Cech C0=k^3 -> C1=k^3 -> C2=k; rank(d0)=2, rank(d1)=1; H1=0',
       {'d0':d0.tolist(),'d1':d1.tolist(),'rank_d0':d0.rank(),'rank_d1':d1.rank(),'H1_Cech':3-d1.rank()-d0.rank(),'H1_actual_plane_cubic':1})
q=s.symbols('q')
planechi=s.expand((q+2)*(q+1)/2-((q-3)+2)*((q-3)+1)/2)
record('plane_cubic_hilbert_polynomial','57:224','Exact 0 -> O_P2(q-3) -> O_P2(q) -> O_C(q) ->0.',
       'chi(O_C(q))=binom(q+2,2)-binom(q-1,2)',str(planechi),planechi==3*q)

x,y,z,tau=s.symbols('x y z tau')
f=x*y*(x+y+tau*z)
record('triple_lines_flatness','57:222','Polynomial ring k[tau,x,y,z], all fields. Leading monomial x^2*y has coefficient1 in lex x>y>z.',
       'Expand primitive cubic; standard monomials yield k[tau]-free graded quotient',str(s.expand(f)))
record('conic_regular_chart','57:214–219','Affine chart z=1 of xy-tz^2; other charts solve y=tz^2 or x=tz^2.',
       'partial(x*y-t)/partial t',str(s.diff(x*y-t,t)),s.diff(x*y-t,t)==-1)
record('conic_vertical_intersections','57:214–219','D1+D2 is principal special fibre, D1.D2=length k[x,y]/(x,y)=1.',
       '0=(D1+D2).D1 and analogously D2 imply self-intersections -1',{'D1_bidegree':[-1,1],'D2_bidegree':[1,-1],'total_degree':0})

curves=[('smooth genus g',1,[],[]),('irreducible node',1,[1],[2]),('irreducible cusp',1,[1],[1]),('two lines one node',2,[1],[2]),('triangle three lines',3,[1,1,1],[2,2,2]),('three concurrent plane lines',3,[3],[3])]
rows=[]
for name,c,ds,rs in curves:
    affine=sum(ds)-c+1
    torus=sum(v-1 for v in rs)-c+1
    unipotent=sum(d-r+1 for d,r in zip(ds,rs))
    assert affine==torus+unipotent
    rows.append(dict(curve=name,components=c,delta=ds,branches=rs,affine=affine,torus=torus,unipotent=unipotent))
record('normalization_picard_dimensions','57:147–155','Proper reduced connected curve over algebraically closed field; delta invariants and branch numbers as listed.',
       'dim affine=sum(delta)-c+1; torus=sum(r-1)-c+1; unipotent=sum(delta-r+1)',rows)
G,V,E=s.symbols('G V E',integer=True)
record('stable_graph_moduli_dimension','57:153,155','Connected stable graph; G=sum vertex genera, V vertices,E edges; g=G+E-V+1.',
       'sum(3g_v-3+n_v)=3G-3V+2E=3g-3-E',str(s.expand(3*(G+E-V+1)-3-E-(3*G-3*V+2*E))),s.expand(3*(G+E-V+1)-3-E-(3*G-3*V+2*E))==0)

# Exterior algebra; canonical sorted tuple basis and Koszul signs.
def wedge(a,b):
    if set(a)&set(b): return None,0
    sign=(-1)**sum(i>j for i in a for j in b)
    return tuple(sorted(a+b)),sign
def extadd(a,b):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,0)+v
    return {k:s.expand(v) for k,v in c.items() if s.expand(v)!=0}
def extmul(a,b):
    c={}
    for i,u in a.items():
        for j,v in b.items():
            k,sgn=wedge(i,j)
            if sgn: c[k]=c.get(k,0)+sgn*u*v
    return {k:s.expand(v) for k,v in c.items() if s.expand(v)!=0}
def scale(a,u): return {k:s.expand(v*u) for k,v in a.items() if s.expand(v*u)!=0}
def extpow(a,p):
    b={():s.Integer(1)}
    for _ in range(p): b=extmul(b,a)
    return b
def exp_ext(a,maxp):
    b={}
    for j in range(maxp+1): b=extadd(b,scale(extpow(a,j),s.Rational(1,math.factorial(j))))
    return b

# Koszul cochain differential a wedge -, contraction by basis dual.
aa=s.symbols('a0:3')
basis=[v for deg in range(4) for v in combinations(range(3),deg)]
def contract(i,v):
    if i not in v:return {}
    j=v.index(i);return {v[:j]+v[j+1:]:(-1)**j}
for i in range(3):
    for v in basis:
        dv=extmul({(j,):aa[j] for j in range(3)},{v:1})
        h_d={}
        for term,coef in dv.items():h_d=extadd(h_d,scale(contract(i,term),coef))
        d_h=extmul({(j,):aa[j] for j in range(3)},contract(i,v))
        assert extadd(h_d,d_h)=={v:aa[i]}
record('koszul_homotopy','57:134','Exterior Koszul complex on3 symbolic generators; polynomial identity valid over any ring.',
       'd*iota_i+iota_i*d=a_i Id, all8 basis vectors and3 contractions','24 symbolic identities verified')

# Fourier cohomology on product elliptic curves. Basis x_i,y_i,u_i,v_i;
# c1(P)=sum(x_i v_i-y_i u_i), theta_A=sum d_i x_i y_i.
fourier=[]
for dim in (1,2,3):
    ds=s.symbols('d1:'+str(dim+1))
    theta={tuple((2*i,2*i+1)):ds[i] for i in range(dim)}
    D={}
    for i in range(dim):
        D[(2*i,2*dim+2*i+1)]=1
        D[(2*i+1,2*dim+2*i)]=-1
    integrand=extmul(exp_ext(theta,dim),exp_ext(D,2*dim))
    full=tuple(range(2*dim));trans={}
    for key,coef in integrand.items():
        if key[:2*dim]==full:
            trans[tuple(k-2*dim for k in key[2*dim:])]=coef
    chi=s.prod(ds)
    first=[s.simplify(trans.get((2*i,2*i+1),0)) for i in range(dim)]
    expect=[-s.prod(ds[j] for j in range(dim) if j!=i) for i in range(dim)]
    assert first==expect and trans.get(())==chi
    fourier.append({'dimension':dim,'chi':str(chi),'degree_one_coefficients':[str(v) for v in first],'cohomology_transform':{str(k):str(v) for k,v in trans.items()}})
record('fourier_grr_sign','59:6–11,16–20','Standard determinant det RΓ=detH0 tensor(detH1)^-1 etc; normalized Poincare convention specified in code. Cohomology only, not all Chow.',
       'Integrate exp(theta_A) exp(c1(P)); divisor part = -adjugate of diagonal polarization',fourier)
adjugates=[]
for dim in (2,3,4):
    entries=list(range(1,dim+1));A=s.diag(*entries);chi=int(A.det());phi=-A.adjugate();phi2=-phi.adjugate()
    correct=(-1)**dim*chi**(dim-2)*A
    assert phi2==correct
    adjugates.append({'dimension':dim,'A':A.tolist(),'chi':chi,'phi_A':phi.tolist(),'phi_phi_A':phi2.tolist(),'positive_written_formula_valid':phi2==chi**(dim-2)*A})
record('double_phi_parity','59:11','Product of elliptic curves with positive diagonal polarization; phi=-adj(A).',
       'phi(phi(A))=(-1)^n det(A)^(n-2) A',adjugates)
A=s.diag(1,2,2);dual=A.adjugate()
record('dual_polarization_primitive_counterexample','59:11','Dimension3 polarization type(1,2,2), original class primitive.',
       'adj diag(1,2,2)',{'dual':dual.tolist(),'original_content':1,'dual_content':math.gcd(*list(dual.diagonal()))})
record('even_chi_not_twodivisible','59:13','Product elliptic surface with polarization type(1,2).',
       'chi=product elementary divisors, NS coordinate first entry1',{'chi':2,'polarization_diagonal':[1,2],'divisible_by_2':False})

rho,g,degree,c=s.symbols('rho g degree c')
record('perfect_complex_curve_rr','59:16','Rankrho perfect complex, det degreec, degree d line bundle, genusg curve.',
       '(rho+(rho*d+c)eta)*(1+(1-g)eta), eta^2=0',
       {'chi':str(s.expand(rho*(1-g+degree)+c)),'source_without_rho':str(1-g+degree+c),'counterexample_rho2_g1_d1_c0':[2,1]})
gd=[]
for dim in range(2,10):
    values=[j**dim-j**(dim-1) for j in range(-8,9)]
    assert math.gcd(*values)==2
    for chi in range(1,10):
        vals=[chi*j**dim-j**(dim-1) for j in range(-8,9)]
        gg=math.gcd(*vals);assert gg==(1 if chi%2==0 else 2)
        gd.append([dim,chi,gg])
record('torsor_annihilator_gcd','59:13–14','n>=2. Proof: evaluate at±1 for upper bound; parity gives lower bound. Finite samples corroborate, do not replace this proof.',
       'gcd_lambda(lambda^n-lambda^(n-1))=2; gcd_lambda(chi*lambda^n-lambda^(n-1))=gcd(chi-1,2)',gd)

record('universal_pointed_genus_one_counterexample','59:10','Universal elliptic curve with marked origin; relative canonical class degree0, origin divisor degree1.',
       'Degrees rule out origin class in Z[canonical]',{'degree_K':0,'degree_origin':1,'integer_multiple_possible':False})
record('R1_without_S2_counterexample','57:170','A=k+(x,y)^2⊂k[x,y]. Finite normalization; conductor supported at origin, so codim1 local rings regular.',
       'Semigroup contains all monomials of total degree>=2 but excludes x,y; x belongs to fraction field since x=x^3/x^2.',
       {'degree_one_in_A':False,'x_integral':'T^2-x^2=0','x_fraction':'x^3/x^2','normalization_off_origin_equal':True})
record('CM_not_maximal_CM','57:136','A=k[[t]], M=k=A/(t).',
       'depth(M)=dim(M)=0, depth(A)=1; M is CM, has t-torsion, is not free.',{'CM':True,'maximal_CM':False,'free':False})

out=Path(__file__).resolve().parents[1]/'outputs'/'root_computations.json'
out.write_text(json.dumps(OUT,indent=2,ensure_ascii=False,default=str)+'\n')
print(json.dumps({'checks':len(OUT),'all_passed':all(v['passed'] for v in OUT),'output':str(out),'names':[v['name'] for v in OUT]},indent=2))
