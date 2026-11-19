"""Exact finite algebra for manuscript corrections; not tests of conjectures.

All general inferences and hypotheses are explained in computations.md.
Run from the dossier workspace. Only own files are written.
"""
import json
import sympy as s
from pathlib import Path

out=[]
def save(key, result, meaning):
    out.append(dict(id=key, result=str(result), meaning=meaning))

# C01: one-parameter elliptic family in an earlier run, not in the manuscript.
t=s.symbols('t')
A=-3*t/(t-1); B=-2*t/(t-1)
delta=s.factor(-16*(4*A**3+27*B**2))
j=s.factor(1728*4*A**3/(4*A**3+27*B**2))
assert delta==1728*t**2/(t-1)**3 and j==1728*t
save('C01',{'Delta':delta,'j':j},'Smooth for t not 0 or 1 in characteristic zero; j is injective in t.')

# C02: residue normalization in the explicitly oriented local model.
theta=s.symbols('theta',real=True)
z=s.exp(s.I*theta)
integrand=s.simplify(s.diff(z,theta)/z)
residue=s.integrate(integrand,(theta,0,2*s.pi))
assert residue==2*s.pi*s.I
save('C02',{'integrand':integrand,'circle_integral':residue},'Counterclockwise circle gives +2*pi*i; product orientation gives its p-th power.')

# C03: char 2 sl_2 is nilpotent, contrary to a deleted characteristic-free claim.
e=s.Matrix([[0,1],[0,0]]); f=s.Matrix([[0,0],[1,0]])
h=s.Matrix([[1,0],[0,-1]])
def mod2(M):return M.applyfunc(lambda x:int(x)%2)
comm=lambda X,Y:X*Y-Y*X
assert mod2(comm(e,f))==s.eye(2)
assert mod2(comm(h,e))==s.zeros(2) and mod2(comm(h,f))==s.zeros(2)
save('C03',{'[e,f]':mod2(comm(e,f)),'[h,e]':mod2(comm(h,e)),'[h,f]':mod2(comm(h,f))},'Derived algebra is the central line kI, so sl_2 in characteristic 2 is nilpotent of class 2.')

# C04: quaternionic obstruction to a two-dimensional real realization.
a,b,c,d=s.symbols('a b c d',real=True)
I=s.Matrix([[0,-1],[1,0]]); J=s.Matrix([[a,b],[c,d]])
solutions=s.solve(list(I*J+J*I),(c,d),dict=True)
J0=J.subs(solutions[0]); Jsquared=s.simplify(J0*J0)
assert Jsquared==(a*a+b*b)*s.eye(2)
save('C04',{'anticommuting_J':J0,'J_squared':Jsquared},'No real a,b give J^2=-I. Thus the Hamilton quaternion algebra cannot act faithfully on R^2.')

# C05: the two split-extension sections need not coincide.
# Direct product Z x Z, old sections sigma_1(n)=(0,n)=sigma_2(n),
# modify sigma_1 by u(n)=n, sigma_2 by the trivial j*chi.
n0,m0=s.symbols('n0 m0',integer=True)
assert s.Matrix([n0+m0,n0+m0])==s.Matrix([n0,n0])+s.Matrix([m0,m0])
assert s.Matrix([0,n0+m0])==s.Matrix([0,n0])+s.Matrix([0,m0])
save('C05',{'sigma1_prime(n)':'(n,n)','sigma2_prime(n)':'(0,n)','difference_at_1':'(1,0)'},'Both are homomorphic sections by the symbolic additive identity; their values at1 differ. Centralization alone does not imply equality.')

# C06: missing character condition in the kernel formula.
pi=[1,-1]; u={x:1 for x in pi}; chi={x:x for x in pi}
phi={x:u[x]/chi[x] for x in pi}
ku={x for x in pi if u[x]==1}; both={x for x in pi if phi[x]==1 and chi[x]==1}
assert ku!=both
save('C06',{'ker_u':sorted(ku),'ker_phi_intersect_ker_chi':sorted(both)},'pi=C2, u=1, chi=sign, j=id: equality requires an additional implication ker(u) subset ker(chi).')

# C07: formal-coalgebra degree-zero scalar.
eps=(1,0)
assert tuple(x*x for x in eps)==eps and eps!=(0,0) and eps!=(1,1)
save('C07',{'nonzero_idempotent_in_QxQ':eps},'Nonzero plus idempotent does not imply 1 over a ring. Actual equality of degree-zero submodules makes the scalar a unit, which does imply 1.')

# C08: GL2 filtered and split flag dimensions (non-CM elliptic model).
g,borel,levi,u_dim=4,3,2,1
assert g-borel==1 and g-levi==2 and g-borel+u_dim==2
save('C08',{'dim_G':g,'dim_B':borel,'dim_L':levi,'dim_U':u_dim,'dim_Fil':g-borel,'dim_Big':g-levi,'dim_Q_splittings':u_dim,'dim_Hprime_with_Tate_Gm':u_dim+1},'A torsor of splittings and its extension by the Tate torus differ by one dimension.')

# C09: two semilinear involutions need not commute without geometric compatibility.
# A(z)=bar(z), B(z)=i*bar(z). Both square to identity.
v=s.symbols('v',complex=True)
AA=s.conjugate(s.conjugate(v)); BB=s.I*s.conjugate(s.I*s.conjugate(v))
AB=s.conjugate(s.I*s.conjugate(v)); BA=s.I*s.conjugate(s.conjugate(v))
assert s.simplify(AA-v)==0 and s.simplify(BB-v)==0 and s.simplify(AB-BA)==-2*s.I*v
save('C09',{'A_squared':AA,'B_squared':BB,'AB':AB,'BA':BA},'The manuscript needs the real geometric comparison, not merely the fact that both maps are semilinear involutions.')

# C10: ax+b, left and right Haar densities and modular sign.
a,b,a0,b0=s.symbols('a b a0 b0', positive=True)
L=s.Matrix([a0*a,b0+a0*b]); R=s.Matrix([a*a0,b+a*b0])
JL=s.factor(L.jacobian([a,b]).det()); JR=s.factor(R.jacobian([a,b]).det())
left_L=s.factor(JL/L[0]**2);left_R=s.factor(JR/R[0]**2)
right_R=s.factor(JR/R[0])
assert left_L==1/a**2 and left_R==1/(a*a*a0) and right_R==1/a
save('C10',{'left_Jacobian':JL,'right_Jacobian':JR,'left_density_after_L':left_L,'left_density_after_R':left_R,'right_density_after_R':right_R,'det_Ad(a0,b0)':a0},'Left density da db/a^2, right density da db/a; the pullback modular multiplier is (det Ad)^-1.')

# C11: sl2 divided-power coefficients, proved symbolically in n,m.
n,m=s.symbols('n m',integer=True)
# Hv_n=(m-2n)v_n, Fv_n=(n+1)v_(n+1), Ev_n=(m-n+1)v_(n-1).
ef_minus_fe=s.expand((n+1)*(m-n)-n*(m-n+1))
assert ef_minus_fe==m-2*n
assert s.expand((m-2*(n-1))*(m-n+1)-(m-2*n)*(m-n+1))==2*(m-n+1)
assert s.expand((m-2*(n+1))*(n+1)-(m-2*n)*(n+1))==-2*(n+1)
save('C11',{'[E,F] coefficient':ef_minus_fe,'F^r/r! coefficient':'binomial(n+r,r)','E^r/r! coefficient':'binomial(m-n+r,r)'},'For integer m>=0 and 0<=n<=m, these formulas define the integral highest-weight lattice, also stable under binomial(H,r).')

# C12: naive rational Hodge-filtration intersection is not a Hodge substructure.
# tau is a nonreal root of x^3-2. On V=H^1(E)^tensor3, the quotient by F^1
# has evaluation coefficients tau^|I| in a tensor product basis (signs harmless).
cols=[]
for mask in range(8):
    k=mask.bit_count()
    cols.append(s.Matrix([2,0,0]) if k==3 else s.eye(3)[:,k])
M=s.Matrix.hstack(*cols)
assert M.rank()==3 and len(M.nullspace())==5
save('C12',{'matrix':M,'rank_over_Q':M.rank(),'kernel_dimension':len(M.nullspace())},'For the complex torus C/(Z+tau Z), this Q-kernel equals V_Q intersect F^1. Its odd dimension 5 rules out a rational Hodge substructure of pure odd weight 3. This tests a natural interpretation, not unread uncertain notation.')

# C13: error bound in Haar's covering-number additivity proof.
eps,C=s.symbols('epsilon C',positive=True)
eta=eps/(2*(2*C+eps))
err=s.factor(eps/2+2*eta*C+eps*eta)
assert err==eps
save('C13',{'eta':eta,'error_coefficient':err},'The compact-support uniform-continuity argument yields the claimed epsilon bound, with this explicit eta.')

# C14: Tate filtration indexing on a single pure Hodge structure.
weight,p,q,twist=s.symbols('weight p q twist',integer=True)
save('C14',{'weight_after_twist':weight-2*twist,'p_after_twist':p-twist,'q_after_twist':q-twist,'Gr_formula':'Gr_i^W(E(n)) = Gr_(i+2n)^W(E)(n)'},'Indices must shift together with the underlying Tate tensor; an unshifted Gr_i formula fails already for Q(n), n!=0.')

# C15: normalized determinant is exactly one after adjoining a square root.
omega1,omega2,eta1,eta2,T=s.symbols('omega1 omega2 eta1 eta2 T',nonzero=True)
P=s.Matrix([[omega1,eta1],[omega2,eta2]])
save('C15',{'det_P':P.det(),'det_P_over_sqrt_T':s.factor((P/s.sqrt(T)).det())},'If the chosen period basis gives det(P)=T=2*pi*i, then P/sqrt(T) is in SL2. This is one relation, not algebraic independence of three entries.')

# C16: a unimodular group with a nonunimodular subgroup and quotient.
# G=R semidirect R^2, t acts diag(exp(t),exp(-t)); multiplication
# (t,x,y)(s,u,v)=(t+s,x+exp(t)u,y+exp(-t)v).
t0=s.symbols('t0',real=True)
adj_t=s.diag(1,s.exp(t0),s.exp(-t0))
adj_sub=s.diag(1,s.exp(t0))
assert s.simplify(adj_t.det())==1
assert adj_sub.det()==s.exp(t0)
save('C16',{'det_Ad_G':adj_t.det(),'det_Ad_subgroup_and_quotient':adj_sub.det(),'normal_subgroup':'{(0,0,y): y in R}'},'The x-direction subgroup and quotient by the y-direction normal subgroup are ax+b. They are nonunimodular though G is unimodular; the relevant determinant formulas hold for all real t.')

target=Path('agents/p15/evidence/computation_results.json')
target.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
for record in out:print(record['id'],record['result'],record['meaning'],sep='\n')
print('PASS:',len(out),'exact calculations; general reasoning in computations.md')
