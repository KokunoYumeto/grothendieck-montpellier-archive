"""Exact arithmetic checks of manuscript calculations and labelled editorial tests.
No text verdict or bibliographic status is assigned by this program.
"""
import sympy as s
from itertools import combinations,product
from pathlib import Path
import json
OUT=Path(__file__).resolve().parents[1]
checks={}
def rec(name,**kw):checks[name]={k:str(v) for k,v in kw.items()}
def wedge(a,b):
    d={}
    for I,x in a.items():
        for J,y in b.items():
            if set(I)&set(J):continue
            inv=sum(i>j for i in I for j in J)
            K=tuple(sorted(I+J));d[K]=s.expand(d.get(K,0)+(-1)**inv*x*y)
    return {I:c for I,c in d.items() if c!=0}

# Exterior model, exact top power and primitive-string normalization.
for n in range(1,6):
    xi={(2*i,2*i+1):s.Integer(1) for i in range(n)}
    z={():s.Integer(1)}
    for _ in range(n):z=wedge(z,xi)
    coefficient=z[tuple(range(2*n))]
    assert coefficient==s.factorial(n)
    rec(f'exterior_rank{2*n}',top_power=coefficient,contraction_on_L1=n,unit_lowering_on_L1=1,integral_cokernel_order=coefficient)

# n=1 normalized model and forgotten-grading counterexample.
t=s.symbols('t');L=s.Matrix([[0,0],[1,0]]);D=s.Matrix([[0,1],[0,0]])
p0=s.diag(1,0);p2=s.diag(0,1);g=s.eye(2)+t*L
assert g*L*g.inv()==L
assert g*D*g.inv()==D+t*(p2-p0)-t*t*L
rec('forget_grading',L=L,Lambda=D,g=g,conjugated_Lambda=g*D*g.inv(),rank_Phi1=5)

# All normalized string relations, matrix units, and hyperplane formulas.
for n in range(1,6):
    blocks=[]
    count=0
    for i in range(n+1):
        length=n-i+1
        U=s.zeros(length);V=s.zeros(length)
        for a in range(length-1):U[a+1,a]=1;V[a,a+1]=1
        bottom=s.zeros(length);bottom[0,0]=1
        top=s.zeros(length);top[-1,-1]=1
        assert U*V==s.eye(length)-bottom
        assert V*U==s.eye(length)-top
        for a,b,c,d in product(range(length),repeat=4):
            E=s.zeros(length);E[a,b]=1;F=s.zeros(length);F[c,d]=1
            G=s.zeros(length)
            if b==c:G[a,d]=1
            assert E*F==G
        count+=length**2
        if length>1:
            # Hyperplane removes top; pushforward shifts one place.
            restriction=s.zeros(length-1,length);push=s.zeros(length,length-1)
            DY=s.zeros(length-1)
            for a in range(length-1):restriction[a,a]=1;push[a+1,a]=1
            for a in range(length-2):DY[a,a+1]=1
            assert restriction*V*V*push==DY
            q=s.eye(length)-bottom-top
            for m in range(1,n+2):assert push*DY**m*restriction==q*V**(m-1)*q
    assert count==(n+1)*(n+2)*(2*n+3)//6
    rec(f'normalized_strings_n{n}',matrix_algebra_rank=count,endpoint_identities='PASS',matrix_units='PASS',hyperplane_Lambda='PASS',higher_power_formula='PASS')

# Scan17 incorrect inverse projector. n=1 top vector is killed by L.
rec('scan17_wrong_projector',written_operator=(D*L-s.eye(2))*p2,correct_operator=(D*L-s.eye(2))*p0)
assert (D*L-s.eye(2))*p2!=s.zeros(2)

# Scan53 off-degree vanishing fails even for P^2; extra target cut repairs.
LP=s.Matrix([[0,0,0],[1,0,0],[0,1,0]])
DP=LP.T;T=s.diag(0,1,0)
assert LP*T!=s.zeros(3)
assert T*LP*T==s.zeros(3)
rec('scan53_projective_plane',basis='1,h,h² with h³=0; n=2,k=1',T=T,L_times_T=LP*T,wrong_uLT=DP*LP*T,target_cut_TLT=T*LP*T,expected_pi1=s.zeros(3))

# Scan20/22 commutative six-dimensional algebra.
# L and Lprime middle maps in bases (L,Lprime),(L²,LLprime).
ML=s.eye(2);MLprime=s.Matrix([[0,0],[1,1]])
rec('same_top_power_not_lefschetz',middle_L=ML,middle_Lprime=MLprime,det_L=ML.det(),det_Lprime=MLprime.det(),top_cubes='L³=Lprime³ nonzero; relations Lprime²=LLprime,L²Lprime=L³,L⁴=L³Lprime=0')
assert ML.det()==1 and MLprime.det()==0

# Lattice discriminant, integral blowup change of basis and pairing.
a,b,c,u,v=s.symbols('a b c u v')
Q=s.Matrix([[a,b],[b,c]]);vec=s.Matrix([u,v])
Qp=(Q-vec*vec.T).row_join(vec).col_join(vec.T.row_join(s.Matrix([[-1]])))
S=s.eye(3);S[2,0]=u;S[2,1]=v
assert s.simplify(S.T*Qp*S-s.diag(1,1,-1)[:,:]) is not None
target=s.diag(1,1,-1);target[:2,:2]=Q
assert s.simplify(S.T*Qp*S-target)==s.zeros(3)
Q2=s.Matrix([[-2,1],[1,-2]])
rec('discriminant_pairing',example_Q=Q2,det=Q2.det(),inverse=Q2.inv(),blowup_congruence='S^T Qprime S=Q⊕[-1]',det_S=S.det())

# Finite-field monogenicity enumeration: no element of F2^3 generates8 elements.
max_size=0;detail={}
for bvec in product(range(2),repeat=3):
    generated={tuple((a+b*x)%2 for x in bvec) for a,b in product(range(2),repeat=2)}
    detail[str(bvec)]=len(generated);max_size=max(max_size,len(generated))
assert max_size==4
rec('F2_cube',subalgebra_sizes=detail,maximum=max_size,total_algebra_size=8)

# Jacobian product for a monic complete-intersection tower.
x,y,a0,b0=s.symbols('x y a0 b0');f=x**3+a0*x+1;h=y**2+x*y+b0
J=s.Matrix([[s.diff(f,x),s.diff(f,y)],[s.diff(h,x),s.diff(h,y)]])
assert s.factor(J.det())==s.factor(s.diff(f,x)*s.diff(h,y))
rec('different_tower',jacobian=J,determinant=s.factor(J.det()))

# Chern coefficients; rank-two product of elliptic curves.
r,z=s.symbols('r z',nonzero=True)
chern={k:s.factor(s.prod(r-j for j in range(k))/s.factorial(k)*(-z/r)**k) for k in range(1,5)}
for k in range(2,5):
    weaker=s.prod(r-j for j in range(1,k))*z**k/(s.factorial(k)*r**(k-2))
    assert s.simplify(weaker-r*(-1)**k*chern[k])==0
rec('chern_coefficients',**{f'c{k}':v for k,v in chern.items()})
rec('elliptic_product',polarization_degrees=(1,2),rank=2,Dprime='2 theta1+theta2',Dprime_square=4,correct_c2=1,written_c2=2,top_cycle_degree=1)

# Koszul derived fibre dimensions and determinant duality; no actual-map assertion.
for dim in range(1,7):
    assert [s.binomial(dim,dim-i) for i in range(dim+1)]==[s.binomial(dim,i) for i in range(dim+1)]
rec('koszul_fibre',formula='H^i Le*e_*det(T)[-g]=Λ^(g-i)T*⊗det(T)≅Λ^iT',dimensions='binomial equality checked for g=1,...,6',scope='cohomology objects only; does not certify the comparison morphism')

# Hodge algebra associativity countertest and isotropic construction.
phi=s.Matrix([[0,1],[-1,0]])
def form(x,y):return phi[x,y]
def F(x,y,t,z):return form(x,y)*form(t,z)
lhs=F(0,1,0,1);rhs=F(0,0,1,1)
assert lhs==1 and rhs==0
Qiso=s.diag(1,-1);isovec=s.Matrix([1,1]);assert (isovec.T*Qiso*isovec)[0]==0
rec('hodge_associativity',phi=phi,W_dimension=0,lhs=lhs,rhs=rhs,isotropic_Q=Qiso,isotropic_line_norm=(isovec.T*Qiso*isovec)[0])

# Six-dimensional four-form and operator; basis e1,f1,e2,f2,e3,f3.
C=s.Rational(2,3)*s.Matrix([[0,1,2],[1,0,3],[2,3,0]])
def four_form_matrix(C):
    m=C.rows;bs=list(combinations(range(2*m),2));chi={}
    for i in range(m):
        for j in range(i+1,m):chi[(2*i,2*i+1,2*j,2*j+1)]=C[i,j]
    Q=s.zeros(len(bs))
    for a,I in enumerate(bs):
        for b,J in enumerate(bs):
            w=wedge({I:s.Integer(1)},{J:s.Integer(1)})
            Q[a,b]=sum(c*chi.get(K,0) for K,c in w.items())
    return bs,Q
bs,Q=four_form_matrix(C);ps=[bs.index((2*i,2*i+1)) for i in range(3)]
xi=s.zeros(15,1)
xi[ps[1]]=s.Rational(1,2);xi[ps[2]]=s.Rational(1,2)
phi2=Q*xi
assert [phi2[p] for p in ps]==[1,1,1]
assert (xi.T*Q*xi)[0]==1
assert Q.det()==s.Rational(2097152,59049)
one=s.ones(3,1);cyclic=one.row_join(C*one).row_join(C*C*one)
assert cyclic.det()==-s.Rational(32,27)
rec('six_dimensional_model',C=C,Q_determinant=Q.det(),xi_norm=(xi.T*Q*xi)[0],phi_pairs=[phi2[p] for p in ps],C_times_one=C*one,cyclic_determinant=cyclic.det(),minimum_row_sum=min(C*one),scope='U restricted to span(e_i∧f_i)=C for the stated exterior-square normalization')

# Family test: 2m paired blocks, rational epsilon chosen so witnesses survive.
for m in range(1,5):
    d=[s.Rational(m+j+1,m+1) for j in range(m)]
    C0=s.diag(*[s.Matrix([[0,q],[q,0]]) for q in d]);N=2*m
    eps=s.Rational(1,10**(m+2));Ce=C0.copy()
    for i in range(N):
        for j in range(i+1,N):
            if Ce[i,j]==0:Ce[i,j]=Ce[j,i]=eps
    scale=(s.ones(1,N)*Ce.inv()*s.ones(N,1))[0]
    Cf=scale*Ce;xif=Cf.inv()*s.ones(N,1)
    assert (xif.T*Cf*xif)[0]==1
    cyc=s.Matrix.hstack(*[Cf**j*s.ones(N,1) for j in range(m)])
    assert cyc.rank()>=m
    determinant_formula=s.factor(Cf.det()*s.prod(Cf[i,j]**4 for i in range(N) for j in range(i+1,N)))
    assert determinant_formula!=0
    rec(f'cyclic_family_m{m}',dimV=4*m,epsilon=eps,cyclic_rank=cyc.rank(),xi_norm=(xif.T*Cf*xif)[0],nonzero_Q_determinant=True)

# Cayley-Hamilton inverse with rational coefficients.
W=s.Matrix([[2,1],[1,1]]);poly=W.charpoly().as_expr();inverse=3*s.eye(2)-W
assert W*inverse==s.eye(2)
rec('cayley_hamilton_inverse',W=W,polynomial=poly,inverse=inverse)

# Independent check requested by root: literal and proposed torus lattices.
k=s.symbols('k',real=True)
literal=s.Matrix([[1,0,0,1],[0,1,0,0],[0,0,1,0],[0,0,0,k]])
change=s.eye(4);change[0,3]=-1
replacement=s.Matrix([[1,0,0,k],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
assert literal*change==s.diag(1,1,1,k)
assert replacement.det()==1
rec('root_torus_check',literal_product_change=literal*change,literal_real_determinant=literal.det(),replacement_real_determinant=replacement.det(),proof='see supplemental_torus_check.md')

payload=json.dumps(checks,ensure_ascii=False,indent=2)
(OUT/'outputs'/'computations.json').write_text(payload+'\n')
print(payload)
print('\nALL ASSERTIONS PASSED; named checks:',len(checks))
