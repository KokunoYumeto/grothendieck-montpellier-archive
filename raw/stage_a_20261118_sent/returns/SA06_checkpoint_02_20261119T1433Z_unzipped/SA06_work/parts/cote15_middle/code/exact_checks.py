"""Exact computations supporting the SA06 cote15 middle audit.

These finite algebra computations do not claim to prove the cited global theorems.
Every assertion is checked by exact arithmetic; illustrative finite ranges are labelled.
"""
from pathlib import Path
from fractions import Fraction
import json, sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
P=Path('/workspace/scratch/a5176e5b5d45/SA06_work/parts/cote15_middle')
out={}
def record(key, value):
    out[key]=value
def mat(a): return [[str(x) for x in row] for row in a.tolist()]
x,t,z,w,r,M,mu,q,T=s.symbols('x t z w r M mu q T')

# Q(sqrt(-23)): use omega^2-omega+6=0; alpha=1+omega.
om=s.symbols('omega')
mod=om**2-om+6
conjugate=lambda f:s.rem(s.expand(f.subs(om,1-om)),mod,om)
norm=lambda f:s.factor(s.rem(s.expand(f*conjugate(f)),mod,om))
alpha=1+om
beta=alpha/2
assert norm(alpha)==8 and norm(beta)==2
assert s.rem(alpha*conjugate(alpha)-8,mod,om)==0
# Mod 2 omega has roots 0,1, alpha vanishes only at 1; norm exponent is 3.
assert s.Poly(mod,om,modulus=2).eval(0)==0
assert s.Poly(mod,om,modulus=2).eval(1)==0
assert alpha.subs(om,0)%2==1 and alpha.subs(om,1)%2==0
bounded_norm2=[(a,b) for a in range(-4,5) for b in range(-2,3)
               if a*a+a*b+6*b*b==2]
assert bounded_norm2==[]
# This enumeration is complete: b !=0 gives (a+b/2)^2+23b^2/4 >2;
# b=0 leaves a^2=2. No claim about class number beyond the exhibited order3.
V=s.Matrix([[2,3],[-1,-3]])
S=smith_normal_form(V,domain=ZZ)
S8=smith_normal_form(3*s.eye(2),domain=ZZ)
assert abs(V.det())==3
record('CM23',{'minimal_polynomial_omega':str(mod),'norm_alpha':str(norm(alpha)),
 'norm_beta':str(norm(beta)),'norm_form':'a^2+a*b+6*b^2 = (a+b/2)^2+23*b^2/4',
 'norm2_candidates_complete_by_bound':bounded_norm2,'valuations_alpha':[3,0],
 'valuations_beta':[2,-1],'valuations_alpha_over_conjugate':[3,-3],
 'valuation_matrix':mat(V),'smith_form':mat(S),'weight_q8_smith_form':mat(S8),
 'conclusion':'P has exact order3; norm-one2-divisor image is3Z(P-Pbar).'} )

# Q(i): no rational a,b with a^2+b^2=3, by primitive integer descent mod3.
squares3={a*a%3 for a in range(3)}
zeros3=[(a,b) for a in range(3) for b in range(3) if (a*a+b*b)%3==0]
assert zeros3==[(0,0)]
record('CM_norm_obstructions',{'squares_mod3':sorted(squares3),'zero_pairs_mod3':zeros3,
 'descent':'A^2+B^2=3C^2 forces3|A,B then3|C, contradicting primitivity.',
 'rational_norm2_in_Qsqrt_minus23':str(norm(beta)),
 'integral_norm2_in_Qsqrt_minus23':'none, by the complete quadratic-form bound above'})

# Enlarging a CM field: alpha=(3+sqrt(-23))/2; beta^3=alpha.
poly=T**6-3*T**3+8
factor=s.factor_list(poly)
assert len(factor[1])==1 and factor[1][0][0]==poly and factor[1][0][1]==1
record('CM_enlargement',{'polynomial':str(poly),'factorization_over_Q':str(factor),
 'norm_relation':'alpha*alphabar=8; each cube root beta has |sigma(beta)|^2=2',
 'field_degree':int(s.degree(poly,T)),'contains_Qsqrt_minus23':'sqrt(-23)=2*beta^3-3'})

# Reading alarms and normalizations.
record('weight_and_sign',{'q4_weight1_literal_lambda_squared':str(s.sqrt(2)**2),
 'literal_modulus':str(s.sqrt(2)),'required_modulus':2,
 'fixed_lambda_weight_base_p':1,'fixed_lambda_weight_base_p_squared':str(Fraction(1,2)),
 'epsilon_written_f0':'epsilon(f*j(sqrt(p)))=q*p',
 'epsilon_normalized_f0':'epsilon(f*j(q^(-1/2)))=1',
 'real_negative_example':{'lambda':-2,'q':4,'weight':1},
 'quartic_p2_common_squared_modulus':str(s.sqrt(2))})

# Compact real torus and quaternionic descent: J=A conjugation, A real here.
A=s.Matrix([[0,-1],[1,0]])
assert A*A==-s.eye(2)
assert s.simplify(s.det(A)*s.conjugate(s.det(A)))==1
record('real_descent',{'A':mat(A),'J_squared':mat(A*A),
 'determinant_identity':'|det(A)|^2=(-1)^rank; rank is even if J^2=-I',
 'compact_torus_action':'sigma(z)=1/conjugate(z)',
 'H1':'real_nonzero / positive_real = Z/2',
 'H2':'S1 / {z/conjugate(z)} =0',
 'mu2_H2':'Z/2 (trivial action; norm=square=1)',
 'parity_2Z_mod2':[0],'parity_3Z_mod2':[0,1]})

# Honda--Tate order3 obstruction: pi=1+sqrt(-7), q=8.
pi=1+s.sqrt(-7)
pibar=1-s.sqrt(-7)
assert s.simplify(pi*pibar)==8
assert s.simplify(pi+pibar)==2
ratio=s.simplify(pi/pibar)
assert s.simplify(ratio-1)!=0 and s.simplify(ratio+1)!=0
newton=[(0,3),(1,1),(2,0)]
slopes=[Fraction(newton[i+1][1]-newton[i][1],newton[i+1][0]-newton[i][0]) for i in range(2)]
assert slopes==[Fraction(-2),Fraction(-1)]
invariants=[Fraction(1,3),Fraction(2,3)]
assert sum(invariants)==1
record('HondaTate_order3',{'pi_minpoly':'T^2-2*T+8','discriminant':-28,
 'field_discriminant':-7,'field_discriminant_mod8':1,'norm_pi':str(s.simplify(pi*pibar)),
 'trace_pi':2,'newton_points':newton,'newton_slopes':list(map(str,slopes)),
 'prime_valuations':[1,2],'q_valuation':3,'local_degrees':[1,1],
 'local_Brauer_invariants':list(map(str,invariants)),'other_invariants':0,
 'division_algebra_degree':3,'division_algebra_dimension_over_K':9,'abelian_dimension':3,
 'ratio_pi_pibar':str(ratio),
 'absolute_simplicity_argument':'K has only roots of unity±1; ratio is neither, so Q(pi^n)=K for every n; normalized invariants and dimension remain unchanged.',
 'scope':'If the standard geometric pure-motive gerbe contains h1(A), any Tate-reduced lift of its class has an order3 Brauer image. This is not an unconditional identification of the manuscript category.'})

# Earlier-run sl2 computations, on basis v_k=L^k v, 0<=k<=n.
sl2=[]
for n in range(1,9):
    L=s.zeros(n+1); Lam=s.zeros(n+1)
    H=s.diag(*[2*k-n for k in range(n+1)])
    for k in range(n): L[k+1,k]=1
    for k in range(1,n+1): Lam[k-1,k]=k*(n-k+1)
    assert H*L-L*H==2*L and H*Lam-Lam*H==-2*Lam
    assert L*Lam-Lam*L==H
    Cas=H*H+2*H+4*Lam*L
    assert Cas==n*(n+2)*s.eye(n+1)
    h=s.symbols('h'); projectors=[]
    for k in range(n+1):
        eigen=2*k-n
        proj=s.eye(n+1)
        for j in range(n+1):
            if j!=k: proj=proj*(H-(2*j-n)*s.eye(n+1))/(eigen-(2*j-n))
        target=s.zeros(n+1);target[k,k]=1
        assert proj==target
        projectors.append(mat(proj))
    sl2.append({'highest_weight':n,'dimension':n+1,'Casimir':n*(n+2),
                'all_commutators':'exact','weight_projectors':'exact'})
record('sl2',{'range':'n=1,...,8; finite exact checks complement the symbolic proof',
 'checked':sl2,'universal_lowering':'Lambda L^k v=k(n-k+1)L^(k-1)v',
 'universal_Casimir':'H^2+2H+4Lambda L=n(n+2)',
 'Tate_constraint':'Gm scales the top Tate line; the wedge2 of the standard sl2-module is trivial. They are different group actions.'})

# Explicit commutator in GL2 and determinant tensor.
g=s.Matrix([[2,1],[0,1]]); e=s.Matrix([[1,0],[1,1]])
comm=g*e*g.inv()*e.inv()
assert comm!=s.eye(2) and comm.det()==1
record('GL2',{'g':mat(g),'h':mat(e),'commutator':mat(comm),
 'commutator_determinant':str(comm.det()),'g_wedge2_scalar':str(g.det()),
 'centre':'scalar matrices','centre_of_SL2':'±I'})

# Artin orbit correspondences, C3 regular action; matrix algebra/averaging.
C=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
assert C**3==s.eye(3)
E=(s.eye(3)+C+C**2)/3
assert E*E==E and E.rank()==1
orbit_basis=[s.eye(3),C,C**2]
table=[]
for i in range(3):
    for j in range(3):
        assert orbit_basis[i]*orbit_basis[j]==orbit_basis[(i+j)%3]
        table.append([i,j,(i+j)%3])
record('Artin',{'regular_C3_matrix':mat(C),'trivial_idempotent':mat(E),
 'idempotence':'exact','rank':1,'orbit_composition_table':table,
 'scope':'One finite example checks conventions; the full proof uses all double orbits and Maschke averaging.'})

# Analytic formula checks (recycled Codex typescript).
ta,tb,a,b=s.symbols('ta tb a b')
good=a+(t-ta)/(tb-ta)*(b-a)
bad=a+(t-ta)/(tb-t)*(b-a)
assert s.simplify(good.subs(t,ta)-a)==0 and s.simplify(good.subs(t,tb)-b)==0
record('analytic_interpolation',{'candidate':str(good),'left_endpoint':str(good.subs(t,ta)),
 'right_endpoint':str(s.simplify(good.subs(t,tb))),
 'literal_denominator':'tb-t has a pole at the right endpoint unless a=b'})
correct_series=s.series(s.sqrt(1-w),w,0,6)
wrong_series=sum(s.binomial(s.Rational(1,2),n)*w**n for n in range(6))
assert s.expand(wrong_series).coeff(w)==s.Rational(1,2)
assert correct_series.removeO().coeff(w)==-s.Rational(1,2)
v=(1-s.sqrt(1-4*M*q*mu*(1+q*M*mu)*(1/(1-mu*t)-1)))/(2*q*mu*(1+q*M*mu))
eq=(1-q*mu*v)*(1+q*M*mu)*v-(M/(1-mu*t)-M*(1-q*mu*v))
assert s.simplify(eq)==0 and s.simplify(v.subs(t,0))==0
record('analytic_majorant',{'sqrt_correct_series':str(correct_series),
 'literal_positive_linear_coefficient':str(wrong_series.coeff(w)),
 'quadratic_solution_residual':str(s.simplify(eq)),'zero_constant_term':str(v.subs(t,0)),
 'majorant_first_terms_at_M_mu_q_1':str(s.series(v.subs({M:1,mu:1,q:1}),t,0,5))})
# Remainder estimate: f(w)=w^2, p=1, r=1/10, M=r^2.
# Full displayed geometric sum=2/(1-t/r); literal bound then is too small.
rr=Fraction(1,10);tt=Fraction(1,100);MM=rr**2
lhs=tt**2; bad_bound=MM*tt**2*2/(1-tt/rr)
good_bound=bad_bound/rr**2
assert bad_bound<lhs<good_bound
record('analytic_remainder',{'r':str(rr),'t':str(tt),'M':str(MM),
 'left':str(lhs),'literal_bound':str(bad_bound),'corrected_bound_with_r_minus2':str(good_bound),
 'conclusion':'The printed estimate needs r^(-2) or a redefined M.'})
record('analytic_radius',{'boundary_counterexample':'a_n=1/(n+1)^2,r=1,beta=1: sum a_n converges; sum(n+1)*a_n is harmonic and diverges.',
 'valid_repair':'For every0<rho<r, polynomial(n)*(rho/r)^n is bounded, so convergence survives on smaller radii.'})

# Osgood map, extended to a square map by ignoring a third variable.
u,v,zz=s.symbols('u v zz')
osgood=s.Matrix([u,u*v,u*v*s.exp(v)])
Jac=osgood.jacobian([u,v,zz])
assert s.simplify(Jac.det())==0
assert s.simplify(Jac[:2,:2].det())==u
record('Osgood',{'map':['u','u*v','u*v*exp(v)'],'Jacobian':mat(Jac),
 'determinant':0,'nonzero_generic_minor':'u','generic_rank':2,
 'no_relation_proof':'Writing F as sum of homogeneous F_d, substitution yields u^d F_d(1,v,v*exp(v)). Algebraic independence of v and exp(v) forces every F_d to vanish. This analytic argument is recorded in proofs.md, not certified by the finite matrix check.'})

# The coefficient index in u_i'=f_i(x,u) must follow substituted component j.
u1=x**2/2;u2=x
assert s.diff(u1,x)==u2 and s.diff(u2,x)==1
record('ODE_component_index',{'system':"u1'=u2,u2'=1,u1(0)=u2(0)=0",
 'solution':[str(u1),str(u2)],'correct_h1_degree2':str(s.Rational(1,2)),
 'literal_h_i_instead_h_j':'Would replace u2 on the first right side by u1 and incorrectly give all h1 coefficients zero.'})

# Additive valuations satisfy a sum, never the displayed product law.
record('valuation_sum',{'example':'pi=1+sqrt(-7),q=8,weight1; at a prime over2',
 'v_pi':1,'v_pibar':2,'v_q':3,'sum':3,'product':2})

# Dyadic normalization, and the complex inverse-function warning.
record('dyadic_range',{'sum_from_n0_all_ones':'2',
 'sum_from_n1_all_ones':'1','published_target_interval':'[0,1]',
 'scope':'External published-book comparison; no manuscript ink decision.'})
theta=2*s.pi/13
dist2=s.simplify((s.cos(theta)-1)**2+s.sin(theta)**2)
assert float(s.N(dist2))<0.25
record('complex_inverse_warning',{'n':13,'root':'exp(2*pi*i/13)',
 'distance_from1_squared_exact':str(dist2),'distance_squared_numeric':float(s.N(dist2)),
 'comparison':'<1/4, so both1 and the distinct13th root lie in|z-1|<1/2; z^13 is not injective although its derivative never vanishes there.'})

# Additional universal identities and exact bounds used in the written proof.
aa,bb,h1,h2=s.symbols('aa bb h1 h2')
xi2=s.rem(s.rem(s.expand((aa*h1+bb*h2)**2),h1**2,h1),h2**2,h2)
assert xi2==2*aa*bb*h1*h2
record('P1xP1_integral',{'ring':'Q[h1,h2]/(h1^2,h2^2)',
 'square':str(xi2),'top_coefficient':'2*a*b'})
yy=s.symbols('yy')
U1=yy;U2=2*yy
correct_compat=s.diff(U2,yy)*U1-s.diff(U1,yy)*U2
literal_compat=s.diff(U2,yy)*U1-s.diff(U1,yy)*U1
assert correct_compat==0 and literal_compat==yy
record('Frobenius_index',{'U11':str(U1),'U21':str(U2),
 'correct_compatibility_residual':str(correct_compat),
 'literal_residual_for_i2_k1_j1':str(literal_compat),
 'solution':'y=C*exp(x1+2*x2), satisfying both partial equations'})
assert Fraction(22,7)<Fraction(13,4)
out['complex_inverse_warning']['exact_bound']='2*sin(pi/13)<2*pi/13<44/91<1/2; pi<22/7<13/4'
rr2=Fraction(1,4);tt2=Fraction(1,8);mm2=rr2**2
bound2=mm2*tt2**2*2/(1-tt2/rr2)
assert bound2==Fraction(1,256) and tt2**2==Fraction(1,64)
out['analytic_remainder']['second_exact_test']={'r':str(rr2),'t':str(tt2),
 'M':str(mm2),'literal_bound':str(bound2),'left':str(tt2**2)}
path=P/'audit/exact_checks.json'
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
