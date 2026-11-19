#!/usr/bin/env python3
"""Exact, deliberately small certificates for the ega claim map.

Each output states its scope. Symbolic/finite checks do not prove unrestricted
geometric assertions. The accompanying proof notes give the general arguments.
"""
import json
from fractions import Fraction as F
from math import factorial
import sympy as s

out=[]
def record(name, inputs, result, scope):
    out.append(dict(name=name,inputs=inputs,result=result,scope=scope))

t,x,y,z,a,b,c=s.symbols('t x y z a b c')
truncate=lambda f,n: s.Poly(s.expand(f),t).trunc(10**9) if False else s.series(f,t,0,n).removeO().expand()

# Cote23/009: printed product of logarithms fails already in dual numbers.
g=1+t
logg=truncate(s.log(g),2)
lhs=truncate(s.log(g*g),2); rhs=truncate(logg*logg,2)
assert lhs==2*t and rhs==0
record('log-product-counterexample',{'ring':'Q[t]/(t^2)','g':'1+t','gprime':'1+t'},
       {'log_ggprime':str(lhs),'product_of_logs':str(rhs),'sum_of_logs':str(2*logg)},
       'A literal counterexample to multiplicative RHS; additive identity checked here.')

# Cote22/012: the source uses B rather than C in conditions 1–3.
quotient=s.Matrix([[1,0]])
assert quotient.rank()==1 and len(quotient.nullspace())==1
record('theorem-4.6-source-target',{'A':'Q[e]/(e^2)','B':'A','C':'Q','I':'(e)','u':'quotient'},
       {'B_over_A':'identity: free and formally smooth','u_mod_I':'Q -> Q identity',
        'u_kernel_basis':[str(v) for v in quotient.nullspace()],'is_isomorphism':False},
       'Every ring is noetherian, discrete and complete for the nilpotent topology; C meets adic/closed-ideal hypotheses. P holds for identity B/A.')

# Cote23/013: exponential of a primitive is group-like, not 1+primitive.
exp_tx=1+t*x+t*t*x*x/2
red=truncate(exp_tx.subs(x,x+y)-exp_tx-exp_tx.subs(x,y)+1,3)
groupdiff=truncate(exp_tx.subs(x,x+y)-exp_tx*exp_tx.subs(x,y),3)
assert red==t*t*x*y and groupdiff==0
record('exp-target-counterexample',{'Hopf_algebra':'Q[x], x primitive','Lambda':'Q[t]/(t^3)'},
       {'exp_tx':str(exp_tx),'reduced_coproduct_exp_minus_1':str(red),'group_like_defect':str(groupdiff)},
       'Refutes destination 1+pi_0; validates gamma_0 in this universal truncated one-primitive example.')

# Cote23/009–015: universal one-variable inverse identities to order8.
N=9
E=sum(t**i/s.factorial(i) for i in range(N))
L=sum((-1)**(i+1)*t**i/s.Integer(i) for i in range(1,N))
EL=truncate(sum(L**i/s.factorial(i) for i in range(N)),N)
LE=truncate(sum((-1)**(i+1)*(E-1)**i/s.Integer(i) for i in range(1,N)),N)
assert EL==1+t and LE==t
record('exp-log-truncations',{'modulus':'t^9','coefficients':'Q'},
       {'exp_log_1plus_t':str(EL),'log_exp_t':str(LE)},
       'Finite check through degree8. General identity follows coefficientwise in Q[[t]], then by nilpotence or completeness.')

# Elliptic adjunction and discriminant homogeneity.
rankE=3; filtration=[0,2,3]; omega=-1
M=sum(filtration)-omega
assert M==6
record('elliptic-adjunction-exponent',{'L_exponents_of_E_factors':filtration,'Omega_exponent':omega},
       {'detE':sum(filtration),'M':M,'check':sum(filtration)-M==omega},
       'Tensor-exponent calculation for the stated elliptic filtration; existence of the filtration is geometric input.')
degrees=[]
for r in range(1,5):
 for d in range(2,6):degrees.append({'r':r,'d':d,'literal':(d-1)*(r+1),'standard':(r+1)*(d-1)**r})
record('discriminant-degrees',{'projective_dimension':'r','hypersurface_degree':'d'},degrees,
       'Evaluates two candidate formulas; standard formula is sourced independently in Buse–Jouanolou Prop4.7.')
f=a*x**3+b*x**2+c*x+z
disc=s.discriminant(f,x)
assert s.Poly(disc,a,b,c,z).total_degree()==4
record('binary-cubic-discriminant',{'polynomial':str(f)},
       {'discriminant':str(disc),'coefficient_total_degree':4},
       'Binary cubic r=1 is a case where both formulas agree and cannot detect the missing exponent; plane cubic r=2 gives6 versus12.')

# Cartier's shortened checklist: H=functions C3 -> R.
# A primitive f satisfies f(i+j)=f(i)+f(j); a group-like maps into R^*.
P=s.zeros(9,3)
for i in range(3):
 for j in range(3):
  row=3*i+j;P[row,(i+j)%3]+=1;P[row,i]-=1;P[row,j]-=1
assert P.rank()==3
record('cartier-short-checklist-counterexample',{'H':'R^{C3}','Delta':'Delta f(i,j)=f(i+j mod3)','epsilon':'f(0)'},
       {'primitive_constraint_rank':P.rank(),'primitive_dimension':3-P.rank(),
        'real_group_likes':'f(1)^3=1 in R gives f(1)=1, so only1',
        'dimension_H':3,'dimension_U_Prim':1,'augmentation_ideal':'I^2=I !=0'},
       'Satisfies finite-dimensional cocommutative Hopf and no nontrivial real group-likes, but not Cartier connected filtration; also excluded by earlier I-adic nilpotence.')

# Cote23/019: a finite projective associated graded need not force nilpotence.
e=s.Matrix([0,1])
product=lambda u,v:s.Matrix([u[0]*v[0],u[1]*v[1]])
assert product(e,e)==e
record('augmentation-graded-not-nilpotent',{'Lambda':'k x k','augmentation':'first projection','I':'0 x k'},
       {'idempotent_generator':list(e),'e_squared':list(product(e,e)),
        'gr0':'k','gr_positive':'0','I_nilpotent':False},
       'Lambda finite free rank2; every graded piece finite free. Refutes bracketed therefore I^n=0.')

# Cote23/035: non-geometrically regular curve in characteristic3.
curve=y*y-x**3+a
dx=s.Poly(s.diff(curve,x),x,y,a,modulus=3).as_expr()
dy=s.Poly(s.diff(curve,y),x,y,a,modulus=3).as_expr()
assert dx==0 and dy==-y
record('regular-not-geometrically-regular-curve',{'p':3,'k':'F3(a), a transcendental','A':'k[x,y]/(y^2-x^3+a)'},
       {'partial_x':str(dx),'partial_y':str(dy),'bad_point':'(y,x^3-a)',
        'local_maximal_generator':'y because x^3-a=y^2',
        'after_adjoining_a_root':'y^2-z^3; origin has dimension1 embedding dimension2'},
       'Jacobian calculation checked; the local maximal-ideal argument proves regularity before base change, while cusp gives failure after inseparable base change.')

# Cote23/083: avoid one top-dimensional component is insufficient.
record('dimension-drop-quantifier',{'A':'k[x,y,z]_(x,y,z)/(xy)','Y':'closed point','f':'x'},
       {'dim_A':2,'minimal_primes':['(x)','(y)'],'f_nonzero_on_component_y0':True,
        'A_mod_f':'k[y,z]_(y,z)','dim_A_mod_f':2,'claimed_equal_value':1},
       'Explicit component decomposition verifies all noetherian/local hypotheses and refutes exists in the equality criterion.')

# Cote23/096–099 graded-algebra statements.
record('graded-missing-composition',{'A':'k[t]','B':'k[t]','C':'k[t]','psi':'identity','phi':'identity','u':'identity'},
       {'a':'split surjective in every degree','v':'multiplication, surjective',
        'kernel_phi':'0','psi_Aplus_B':'(t)'},
       'Refutes bprime=>b unless phi psi kills positive degrees.')
record('graded-sections-independence',{'A':'k[x]','B':'k[x,y]','C':'k[t]','psi':'x maps x','phi':'x,y both map t'},
       {'section1':'t maps y: A tensor C -> B is isomorphism','section2':'t maps x: image k[x] only'},
       'Both sections are graded algebra sections; a+bdoubleprime alone does not imply section independence without augmentation composition.')
record('graded-Poincare-missing-b',{'A':'k','B':'k[t]','C':'k','phi':'augmentation'},
       {'a':True,'P_B':'1/(1-t)','P_A_times_P_C':'1','coefficient_degree1':[1,0]},
       'Refutes stated coefficient inequality under a alone.')
record('graded-rank-equality-not-enough',{'A':'k[x]','B':'k[u,v]','C':'k[v]','psi':'x maps0','phi':'u maps0,v maps v'},
       {'a':True,'P_B_equals_P_A_P_C':True,'v_image':'k[v]','v_surjective':False},
       'All graded pieces finite free; refutes c=>bdoubleprime if b is omitted.')
record('graded-flatness-question-i',{'A':'k[t]','B':'k[t]','C':'k','psi':'identity','phi':'augmentation'},
       {'a':True,'b':True,'bdoubleprime':True,'A_flat_k':True,'Tor1_B_C_C':'k !=0','C_flat_B':False},
       'Satisfies even corrected good hypotheses. Two-term resolution B --t--> B certifies nonflatness.')

# Cote22/027–029: characteristic2 differential coefficients.
# y=b^2*x+c^2 in F2(x,b,c); d y = b^2 d x.
jac=s.Matrix([[1,0,0],[b*b,0,0]])
ker=s.Matrix([[-b*b],[1]])
assert jac.T*ker==s.zeros(3,1)
record('field-differential-kernel',{'k':'F2(x,y)','K':'F2(x,b,c)','embedding':'y=b^2*x+c^2'},
       {'Jacobian_rows_dx_dy':str(jac),'kernel_in_dx_dy_basis':str(ker),'kernel_dimension':1},
       'Derivative rows are characteristic2. Non-descent b^2 notin k and k intersect K^2=k^2 are proved in proof_notes.md, not by this finite matrix.')

# Cote23/061–064: signs in the spectral sequence.
record('Auslander-Buchsbaum-corner',{'p_range':'-d <= p <=0','q_range':'q >=a','d':4,'a':7},
       {'lowest_total_degree':min(p+q for p in range(-4,1) for q in range(7,12)),
        'unique_lowest_corner':[-4,7]},
       'Index arithmetic only; nonvanishing Tor_d(k,M) uses a minimal finite free resolution.')

# Cote23/092: exact quotient sequence for fibre products.
record('fibre-product-quotient',{'C':'A prime x_B A doubleprime','f':'(fprime,fdoubleprime)','f0':'common image in B, nonzerodivisor'},
       {'kernel_check':'fprime*hprime and fdoubleprime*hdoubleprime agree over B implies f0*(hprime-hdoubleprime)=0, hence hprime=hdoubleprime over B',
        'conclusion':'C/fC = (Aprime/fprime) x_(B/f0) (Adoubleprime/fdoubleprime)'},
       'Algebraic proof certificate; nonzerodivisibility of f0 is essential.')

print(json.dumps(out,indent=2,ensure_ascii=False,default=lambda v:int(v) if isinstance(v,s.Integer) else str(v)))
