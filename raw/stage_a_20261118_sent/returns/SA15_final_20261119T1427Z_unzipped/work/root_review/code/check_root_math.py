"""Exact, reproducible checks for the root review. Finite tests are labelled as such.
Universal arguments and hypotheses are supplied separately in proof_audit_root.md.
No floating-point comparison or scan-reading inference is used.
"""
import json, math, itertools
from fractions import Fraction as Q
from pathlib import Path
import sympy as S
out={}

# Augmented Amitsur cochains of Q -> Q[eps]/eps^2.
def basis(n):return list(itertools.product((0,1),repeat=n))
def diff(n):
 a,b=basis(n+1),basis(n+2);idx={x:i for i,x in enumerate(b)};M=S.zeros(len(b),len(a))
 for j,x in enumerate(a):
  for k in range(n+2):M[idx[x[:k]+(0,)+x[k:]],j]+=(-1)**k
 return M
def homotopy(n):
 a,b=basis(n+1),basis(n);idx={x:i for i,x in enumerate(b)};M=S.zeros(len(b),len(a))
 for j,x in enumerate(a):
  if x[0]==0:M[idx[x[1:]],j]=1
 return M
am=[]
for n in range(5):
 dn=diff(n);dprev=S.Matrix([[1],[0]]) if n==0 else diff(n-1)
 h=homotopy(n);hp=homotopy(n+1)
 certificate=dprev*h+hp*dn
 assert certificate==S.eye(2**(n+1))
 am.append(dict(degree=n,dimension=2**(n+1),d_rank=dn.rank(),augmented_H_dimension=2**(n+1)-dn.rank()-dprev.rank(),contraction_identity=True))
out['amitsur_dual_numbers']=am

# Closed-disc integration: coefficient valuations go to infinity, primitive ones do not.
out['closed_tate_disc']=[dict(p=p,terms=[dict(r=r,exponent=p**r-1,coefficient_valuation=r,primitive_exponent=p**r,primitive_coefficient_valuation=0) for r in range(1,7)]) for p in (2,3,5)]

t,L,Ph,w,p=S.symbols('t L Phi omega p');Ls=S.symbols('sigmaL')
U=S.Matrix([[1,0],[L,1]]);F=S.Matrix([[p,0],[Ph,1]]);Us=S.Matrix([[1,0],[Ls,1]])
Fp=S.simplify(U*F*Us.inv())
assert Fp==S.Matrix([[p,0],[Ph+p*L-Ls,1]])
out['ordinary_matrix_gauge']={'basis_order':'column (x,y)','U':str(U),'F':str(F),'U_F_sigmaU_inverse':str(Fp)}
gauge=[]
for prime in (2,3,5):
 ell=t**3+2*t+1
 sigma=lambda f:S.expand(f.subs(t,t**prime))
 sigmaform=lambda f:S.expand(prime*t**(prime-1)*sigma(f))
 dPhi=S.expand(prime*ell-sigma(ell));domega=-S.diff(ell,t)
 zero=S.expand(sigmaform(domega)-prime*domega-S.diff(dPhi,t))
 assert zero==0
 u=1+t;phi=1+t+t**2;omega=t**2
 def curvature(ph,om):return S.cancel(S.diff(ph,t)/ph-sigmaform(om)+om)
 corrected=S.cancel(curvature(u*phi/sigma(u),omega-S.diff(u,t)/u)-curvature(phi,omega))
 wrong=S.cancel(curvature(u*phi/sigma(u),omega+S.diff(u,t)/u)-curvature(phi,omega))
 assert corrected==0 and wrong!=0
 gauge.append(dict(p=prime,D1D0=str(zero),rank_one_corrected_change=str(corrected),rank_one_wrong_sign_residual=str(wrong)))
out['gauge_differentials']=gauge
i=S.symbols('i');out['isolated_arithmetic']=str(S.expand((i+p)*(p+1)-(i+p-1)*p));assert out['isolated_arithmetic']=='i + 2*p'

# alpha_p is not BT1; the zero map over k[eps] is its Frobenius pullback.
out['BT1_and_frobenius']={'alpha_p':{'M_dimension':1,'F_rank':0,'V_rank':0,'ker_F_dimension':1,'im_V_dimension':0,'is_BT1':False},'nonreduced_example':'multiplication by eps on k[eps]/eps^2 is nonzero; Frobenius pullback is multiplication by eps^p=0 for p>=2.'}

# A-linear rank-one integral Hom bounds, all exponent patterns in a finite range.
homchecks=0;dimone=[]
for f in range(1,5):
 for e in range(1,4):
  patterns=list(itertools.product(range(e+1),repeat=f))
  for r in patterns:
   for rp in patterns:
    if sum(r)!=sum(rp):continue
    sr=[0];sp=[0]
    for x,y in zip(r,rp):sr.append(sr[-1]+x);sp.append(sp[-1]+y)
    c=max(y-x for x,y in zip(sr,sp))
    assert all(c+x-y>=0 for x,y in zip(sr,sp))
    assert not all(c-1+x-y>=0 for x,y in zip(sr,sp))
    homchecks+=1
  if e==1:
   for a in range(f):
    for b in range(f):
     r=[int(j==a) for j in range(f)];rp=[int(j==b) for j in range(f)]
     sr=[0];sp=[0]
     for x,y in zip(r,rp):sr.append(sr[-1]+x);sp.append(sp[-1]+y)
     dimone.append(dict(f=f,nu_source=a,nu_target=b,pi_exponent=max(y-x for x,y in zip(sr,sp))))
out['integral_Hom_lattices']={'finite_pattern_checks':homchecks,'all_passed':True,'dimension_one_cases':dimone,'scope':'Enumeration checks valuation algebra, not existence/classification of groups.'}
def vp_fact(n,p):
 s=0
 while n:n//=p;s+=n
 return s
pd=[]
for prime in (2,3,5,7):
 for e in range(1,prime+2):
  vals=[n-e*vp_fact(n,prime) for n in range(1,prime**4+1)]
  pd.append(dict(p=prime,e=e,min_valuation=min(vals),first_failure=next((n+1 for n,x in enumerate(vals) if x<1),None),p_power_valuations=[prime**r-e*vp_fact(prime**r,prime) for r in range(1,5)]))
out['PD_valuation_tests']=pd
out['cotangent_lengths']=[dict(e=e,length_Omega_mod_p=e,length_Omega_mod_pi=1) for e in range(1,6)]
alpha=S.symbols('alpha');out['dual_lattice_exponents']={'tangent_exponent':str(-alpha),'cotangent_exponent':str(alpha),'Omega_in_terms_of_omega_exponent':str(-alpha)}

comparisons=[
('8:58',6,9,'>',11,17),('8:58',2,3,'>',11,17),('8:58',5,12,'>',7,17),('8:58',1,4,'<',3,11),('8:58',3,11,'<',2,7),('8:58',2,7,'<',5,17),('8:58',4,17,'<',1,4),('8:58',4,17,'>',1,4),('8:58',1,9,'<',2,17),('8:58',1,6,'<',3,17),('8:58',253,1,'>',285,1),('8:58',253,1,'>=',295,1),('8:58',4,13,'>',7,23),('8:58',3,10,'>',7,24),('8:58',2,3,'<',7,24),('8:58',2,7,'<',7,24),('8:58',1,3,'>',7,23),('8:58',2,7,'<',1,3),('8:58',7,9,'<',7,8),('8:58',7,9,'<',7,0),('8:58',4,5,'<',14,17),('8:58',11,17,'>',15,23),('8:58',11,17,'<',15,23),('8:58',2,3,'>',15,23),('8:58',10,14,'<',13,18),('8:58',13,17,'<',10,13),('8:58',3,5,'<',14,23),('8:58',3,4,'<',13,17),('8:58',5,7,'<',13,18),('8:58',5,7,'>',13,18),('8:58',7,10,'<',12,17),('8:59',4,5,'<',13,15),('8:59',12,14,'=',6,7),('8:59',14,16,'=',7,8),('8:60',13,15,'<',7,8),('8:60',3,4,'>',11,15),('8:60',2,3,'<',11,16),('8:60',6,11,'>=',1,2),('8:60',6,11,'!=',1,2),('8:60',12,14,'=',6,7)]
ops={'<':lambda a,b:a<b,'>':lambda a,b:a>b,'>=':lambda a,b:a>=b,'=':lambda a,b:a==b,'!=':lambda a,b:a!=b}
out['polygon_arithmetic']=[]
for loc,a,b,op,c,d in comparisons:
 record={'scan':loc,'comparison':f'{a}/{b} {op} {c}/{d}'}
 if not b or not d:record.update(result='undefined',reason='zero denominator')
 else:record.update(result=ops[op](Q(a,b),Q(c,d)),left_minus_right=str(Q(a,b)-Q(c,d)))
 out['polygon_arithmetic'].append(record)

# Lie algebra invariants in Sym^n of the standard representation, char zero.
# A torus weight zero vector exists only for even n; for n>0 its raising operator is nonzero.
inv=[]
for n in range(13):
 H=S.diag(*[n-2*j for j in range(n+1)]);E=S.zeros(n+1)
 for j in range(1,n+1):E[j-1,j]=j
 B=H.col_join(E);dim=n+1-B.rank()
 assert dim==(1 if n==0 else 0)
 inv.append(dict(n=n,B_invariants=dim,SL2_invariants=1 if n==0 else 0))
out['Borel_restriction_invariants']=inv
out['weak_admissibility']={'bad_line':{'phi':1,'Fil1_dimension':1,'t_H':1,'t_N':0,'weakly_admissible':False},'good_plane':{'phi':'diag(1,p)','Fil1':'span(e0+e1)','t_H':1,'t_N':1,'phi_stable_lines':[{'line':'e0','t_H':0,'t_N':0},{'line':'e1','t_H':0,'t_N':1}],'weakly_admissible':True,'Fil1_phi_stable':False}}

a,ga,gha,chi_g,chi_h=S.symbols('a ga gha chi_g chi_h',nonzero=True)
lhs=gha/(a*chi_g*chi_h);rhs=(ga/(a*chi_g))*(gha/(ga*chi_h));assert S.cancel(lhs-rhs)==0
out['period_cocycle']={'u_g':'g(a)/(a chi(g))','u_gh_minus_u_g_g_u_h':str(S.cancel(lhs-rhs)),'period_rescaling':'Every c in K* fixes the same eigen-equation; c=uniformizer need not be in A*.','subgroup_test':'For J={1}, every nonzero scalar is an invariant: the unrestricted subgroup claim is false.'}

# Finite jet coordinate counts include no constant term for origin-preserving jets.
jets=[]
for p0 in range(1,5):
 for q0 in range(1,4):
  for k in range(5):
   mon=[x for x in itertools.product(range(k+1),repeat=p0) if 1<=sum(x)<=k]
   actual=q0*len(mon);formula=q0*(math.comb(p0+k,k)-1)
   assert actual==formula
   jets.append(dict(p=p0,q=q0,k=k,origin_preserving_dimension=actual,printed_formula=q0*math.comb(p0+k,k)))
out['jet_dimensions']=jets
out['jet_action_type']={'source_change':'a:K^p->K^p','jet':'c:K^p->K^q','target_change':'b:K^q->K^q','well_typed':'b o c o a^-1','printed':'a o c o b^-1','printed_defined_for_p_neq_q':False}

x,y,z,v,w=S.symbols('x y z v w')
strict=S.expand(((z*z-x*y).subs({z:x*w,y:x*v}))/x**2)
assert strict==w*w-v
out['double_point_chart']={'strict_transform':str(strict),'partial_derivative_wrt_v':str(S.diff(strict,v)),'smooth_chart':True,'scope':'One explicit A1 double-point chart, not a proof of Lipman classification.'}
out['mu_n_coLie']=[dict(base='Q',n=2,H_minus_1_dimension=0,H_0_dimension=0),dict(base='F2',n=2,H_minus_1_dimension=1,H_0_dimension=1),dict(base='F3',n=3,H_minus_1_dimension=1,H_0_dimension=1),dict(base='F3',n=2,H_minus_1_dimension=0,H_0_dimension=0)]
out['analytic_estimates']={'Schwarz':'g(z)=f(z)/z^k extends at0; maximum principle gives ||f(z)||<=M|z|^k. Apply scalar continuous linear functionals to reduce Banach values.','polydisc':'For ||z-a||_infinity<rho/2, Cauchy gives ||partial_j f(z)||<=2M/rho, so ||f(y)-f(a)||<=2pM/rho ||y-a||_infinity on coordinate segments.','L_infinity_translation':'For f=1_[0,infinity) and every h>0, essential sup|f(t-h)-f(t)|=1. This does not refute continuity on the closure of C_c explicitly used on the page.'}
out['relative_mu2']={'injectivity_argument':'A rational number square in every Q_p has even valuation everywhere, hence q=+/-r^2 with r in Q*. Negative sign is not a square in Q_3. Thus Q*/Q*2 -> product_p Q_p*/Q_p*2 is injective.','H0_mapping_fibre':'diagonal mu2(Q)->product_p mu2(Q_p) is injective','caution':'Cokernel of local signs describes degree1 only after the chosen Kummer mapping-fibre convention; it does not identify the undefined handwritten A.'}

O=Path(__file__).resolve().parents[1]/'outputs';O.mkdir(exist_ok=True)
(O/'root_math.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'sections':len(out),'exact_assertions':'passed','amitsur_degrees':5,'Hom_pattern_tests':homchecks,'jet_tests':len(jets),'arithmetic_tests':len(comparisons),'finite_tests_do_not_replace_universal_proofs':True},indent=2))
