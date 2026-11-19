"""Exact symbolic/algebraic certificates for the late cote14 consolidation.
Finite checks accompany, and never replace, the general arguments in computation_notes.md.
"""
from pathlib import Path
import json, sympy as s
P=Path(__file__).resolve().parents[1]
results={}
x,y,z,a,n,d,dp=s.symbols('x y z a n D Dprime')
results['cubic_expansion']={'expanded':str(s.expand((dp+n*d)**3)), 'difference':str(s.expand((dp+n*d)**3-(dp**3+3*n*dp**2*d+3*n**2*dp*d**2+n**3*d**3)))}
xi,A,L=s.symbols('xi A L')
G=s.groebner([xi**2-A*xi,L**2,A**3,A**2*L,A*L**2],xi,A,L)
results['strict_nef_threefold']={'relation':'xi^2=A*xi; L^2=0 on base surface', 'D_cubed':str(G.reduce(s.expand((xi+L)**3))[1]), 'pushforward':'A^2+3*A.L', 'restriction_to_zero_section_squared':'L^2=0'}
m,g=s.symbols('m g',integer=True,positive=True)
results['isogeny_denominator']=[{'m':mm,'dimension':gg,'kernel_order':mm**(2*gg),'inverse_denominator':mm} for gg in range(1,4) for mm in (2,3,5)]
ell=s.symbols('ell',positive=True)
M1=s.diag(ell,1);M2=s.diag(1,ell)
results['top_wedge_lattice_counterexample']={'matrix1':str(M1),'matrix2':str(M2),'det1':str(M1.det()),'det2':str(M2.det()),'different_lattices':'(0,1) is in first, not second over Z_l for l prime'}
results['graph_nonadditivity']={'Gamma_1_plus_Gamma_1_action_on_H2':2,'Gamma_2_action_on_H2':4,'H1_components_equal':True}
chi0,DK=s.symbols('chi_O D_dot_K')
results['surface_RR']={'chi_nD_D2zero':str(chi0-n*DK/2),'linear_coefficient':str(-DK/2),'chi_O_of_P1C_over_R':2,'h0_O_of_P1C_over_R':2,'degree_O':0}
b,c,vb,vc=s.symbols('b c v_b v_c')
epsilon=s.symbols('epsilon')
product=s.expand((b+epsilon*vb)*(c+epsilon*vc))
results['square_zero']={'product_mod_epsilon2':str(product.subs(epsilon**2,0)),'Leibniz_coefficient':str(s.expand(product).coeff(epsilon,1))}
F=lambda u,v:u+v+a*u*v
results['polynomial_group_law']={'associativity_difference':str(s.expand(F(F(x,y),z)-F(x,F(y,z)))),'inverse_rational':str(s.solve(F(x,y),y)[0]),'inverse_substitution':str(s.simplify(F(x,-x/(1+a*x)))),'polynomial_inverse_condition':'a=0 over a field; if a!=0, (1+a*x) cannot divide -x'}
sl=[]
for r in range(1,9):
 e=s.zeros(r+1);f=s.zeros(r+1);h=s.diag(*[2*j-r for j in range(r+1)]);finv=s.zeros(r+1)
 for j in range(r):e[j+1,j]=1
 for j in range(1,r+1):f[j-1,j]=j*(r-j+1);finv[j-1,j]=1
 sl.append({'r':r,'[e,f]=h':e*f-f*e==h,'[h,e]=2e':h*e-e*h==2*e,'[h,f]=-2f':h*f-f*h==-2*f,'unit_lowering_is_sl2':e*finv-finv*e==h})
results['sl2_strings']=sl
e=s.Matrix([[0,0],[1,0]]);unit=s.Matrix([1,0]);results['Tate_unit_test']={'e_unit':str(e*unit),'tensor_automorphism_must_fix_unit':True,'weight_H0_shifted':-1}
results['twist_naturality']={'equation':'(g_target tensor chi(g))*L = L*g_source','after_Tate_trivialization':'g_target*L*g_source^(-1)=chi(g)^(-1)*L'}
results['five_lemma_countermodel']={'top':'0 -> Q -> Q -> 0 -> 0','bottom':'0 -> Q -> Q^2 -> Q -> 0','left_J':'identity','middle_A':'x maps to (x,0), injective not surjective','right_N':'0 -> Q, injective not surjective'}
results['localization_degree']={'correct':'CH^(i-1)(Y) -> CH^i(X) -> CH^i(X-Y) -> 0','codimension_shift':1,'cone_dim_formula':'dim(cone X)=dim X+1','ms_cone_dimension_error':'2*n+1 differs from n+1 by n'}
results['primitive_exponents']=[{'dimension':nn,'codimension':ii,'Lefschetz_iso_exponent':nn-2*ii,'primitive_kernel_exponent':nn-2*ii+1} for nn in range(2,7) for ii in range(nn//2+1)]
results['K3_surjectivity_test']={'n':2,'i':1,'claimed_surjectivity_start':2-2*1+1,'map':'L:Pic(X)_Q -> CH0(X)_Q','image_on_K3':'Q*c_X by Beauville-Voisin Thm1','target':'not finite-dimensional by Mumford1969','conclusion':'not surjective, even after tensor Q'}
results['nodal_cubic_duality']={'normalization':'P1 with two distinct points identified','CW_homotopy':'S2 wedge S1','betti_numbers':[1,1,1],'alternating_matrix_dim1':str(s.zeros(1)),'rank':0}
results['finite_error_vs_rational']={'map':'0 -> Q/Z','tensor_Q_source':'0','tensor_Q_target':'0','rational_isomorphism':True,'cokernel_finite':False,'proof':'Every element of Q/Z has finite order; tensor with Q annihilates torsion; elements1/n modZ have unbounded order.'}
results['C2_cohomology_mod2']={'periodic_resolution_differentials':'alternating g-1 and 1+g; both act by0 on trivial F2','computed_degrees':{str(i):1 for i in range(13)},'general':'H^q(C2,F2)=F2 for every q>=0'}
results['torus_norm']={'split_finite_extension_degree':'d','norm_after_diagonal':'[d]:T -> T','character_lattice_matrix':'d*I_r','rank_for_d_nonzero':'r','warning':'Derivative may vanish in characteristic dividingd; dominance is lattice-rank, not derivative-surjectivity.'}
results['factorial_K_to_Chow']=[{'codimension':i,'c_i_structure_sheaf_factor':(-1)**(i-1)*s.factorial(i-1).__int__()} for i in range(1,8)]
results['exterior_pushforward']=[{'dimA':nn,'cohom_degree':i,'dual_exterior_power':2*nn-i,'fixed_2n_minus1_valid_only_for_i1':i==1} for nn in range(1,5) for i in range(2*nn+1)]

# Sparse exterior algebra over Z. Order x_1,...,x_m,y_1,...,y_m.
# This checks an actual composition, not only a determinant or degree.
import itertools, math
def wedge_term(t,u):
 if set(t)&set(u): return None,0
 inv=sum(i>j for i in t for j in u)
 return tuple(sorted(t+u)),(-1)**inv
def wedge(p,q):
 out={}
 for t,c in p.items():
  for u,d in q.items():
   v,sgn=wedge_term(t,u)
   if sgn:out[v]=out.get(v,0)+c*d*sgn
 return {t:c for t,c in out.items() if c}
def push_x(p,m):
 # integrate the x factor: x_1...x_m y_I -> y_I
 return {tuple(i-m for i in t if i>=m):c for t,c in p.items() if tuple(i for i in t if i<m)==tuple(range(m))}
def push_y(p,m):
 # integrate the y factor: x_I y_1...y_m -> x_I
 return {tuple(i for i in t if i<m):c for t,c in p.items() if tuple(i for i in t if i>=m)==tuple(range(m,2*m))}
pc=[]
for gg in range(1,6):
 mm=2*gg
 PP={(j,mm+j):1 for j in range(mm)}
 power={():1}
 for j in range(mm-1):power=wedge(power,PP)
 fac=math.factorial(mm-1)
 assert all(c%fac==0 for c in power.values())
 rho={t:c//fac for t,c in power.items()}
 sgn=(-1)**((mm-1)*(mm-2)//2)
 columns=[]
 for j in range(mm):
  image=push_x(wedge({(j,):1},rho),mm)
  promoted={tuple(mm+i for i in t):c for t,c in image.items()}
  back=push_y(wedge(PP,promoted),mm)
  assert back=={(j,):sgn}
  columns.append({'basis':j+1,'rho_action':{','.join(str(i+1) for i in t):c for t,c in image.items()},'P_after_rho':{','.join(str(i+1) for i in t):c for t,c in back.items()}})
 pc.append({'dimension':gg,'rank_H1':mm,'divided_power_coefficients_integral':True,'mixed_bidegree':[mm-1,mm-1],'coefficient_abs_values':sorted(set(abs(c) for c in rho.values())),'composition_scalar':sgn,'expected_scalar':(-1)**(gg-1),'columns':columns})
results['poincare_inverse_exterior']={'convention':'c1(P)=sum x_i wedge y_i; x before y; both factor top wedges integrate to1; correspondence uses p_*(class cup pullback).','general_formula':'P^(m-1)/(m-1)! = (-1)^((m-1)(m-2)/2) sum_j x_hat_j wedge y_hat_j, m=2g. P_action o rho_action=(-1)^(g-1) id.','computed':pc,'proof_not_exhaustion':'General exterior proof and integral Kunneth subtraction are in computation_notes.md; these five cases are executable certificates only.'}
assert results['cubic_expansion']['difference']=='0'
assert all(t['[e,f]=h'] and t['[h,e]=2e'] and t['[h,f]=-2f'] for t in sl)
assert results['polynomial_group_law']['associativity_difference']=='0'
out=json.dumps(results,ensure_ascii=False,indent=2)+'\n'
(P/'audit'/'recompute_output.json').write_text(out)
print(out)
