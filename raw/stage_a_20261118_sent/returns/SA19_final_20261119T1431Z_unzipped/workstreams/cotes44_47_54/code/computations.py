"""Exact checks of source formulas, with hypotheses documented in computations.md.
No numerical experiment is used to prove an unrestricted geometric statement.
"""
from fractions import Fraction
from math import comb,factorial
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
out={}
r,D,t,x=s.symbols('r D t x',nonzero=True)
chern=[]
for k in range(1,7):
    numerator=s.prod(r-j for j in range(1,k))
    correct=s.factor((-1)**k*numerator*D**k/(s.factorial(k)*r**(k-1)))
    literal=s.factor((-1)**k*numerator*D**k/(s.factorial(k)*r**(k-2)))
    integrality=s.factor(numerator*D**k/(s.factorial(k)*r**(k-2)))
    assert s.simplify(literal-r*correct)==0
    assert s.simplify(integrality-(-1)**k*r*correct)==0
    # This symbolic identity is the falling-factorial coefficient of (1-Dt/r)^r.
    assert s.simplify(correct-s.prod(r-j for j in range(k))*(-D/r)**k/s.factorial(k))==0
    chern.append({'k':k,'correct':str(correct),'literal_expanded':str(literal),'literal_over_correct':'r','integrality_equals':'(-1)^k*r*c_k'})
out['chern_coefficients']=chern

# Ring Q[theta1,theta2]/(theta1^2,theta2^2); integral theta1 theta2 = 1.
a,b=s.symbols('theta1 theta2')
def trunc(f):
    poly=s.Poly(s.expand(f),a,b)
    return s.expand(sum(c*a**i*b**j for (i,j),c in poly.terms() if i<2 and j<2))
chE=trunc((1-a)*(2-b)); c1=-2*a-b
ch2=-0+ a*b
c2=trunc(c1*c1/2-ch2)
wrong=trunc(Fraction(2-1,2)*(-c1)**2)
assert c2==a*b and wrong==2*a*b
out['elliptic_product']={'hypotheses':'A=E1×E2 over C; L has degrees (1,2), ample, r=2; theta_i degree one','chE':str(chE),'Dprime':str(-c1),'Dprime_squared':str(trunc(c1*c1)),'actual_c2_degree':1,'literal_c2_degree':2,'conclusion':'literal expanded coefficient false, corrected generating series true'}

# Exterior algebra on a1,b1,a2,b2,a3,b3, indexed 0,...,5.
def wedge(U,V):
    W={}
    for u,c in U.items():
        for v,d in V.items():
            if set(u)&set(v): continue
            inv=sum(i>j for i in u for j in v)
            q=tuple(sorted(u+v)); W[q]=W.get(q,0)+(-1)**inv*c*d
    return {q:c for q,c in W.items() if c}
def P(i,j):
    # c1(m*Theta-pr_i*Theta-pr_j*Theta)=a_i b_j-b_i a_j.
    return {(2*i,2*j+1):1,(2*i+1,2*j):-1}
def push3(U):
    return {q[:-2]:c for q,c in U.items() if q[-2:]==(4,5)}
P12=P(0,1); D0=push3(wedge(P(0,2),P(1,2)))
assert D0=={q:-c for q,c in P12.items()}
def pretty(U):
    names=['a1','b1','a2','b2','a3','b3']
    return ' + '.join(str(c)+'*'+''.join(names[j] for j in q) for q,c in sorted(U.items()))
out['full_kernel_descent']={'P12':pretty(P12),'push_P13_P23':pretty(D0),'z_multiple':2,'D_endomorphism':-4,'kernel':'E[4]','quotient_map':'[4]:E→E','pullback_multiplier_on_EndE':16,'required_quotient_endomorphism':str(Fraction(-4,16)),'integral_descent_possible':False,'hypotheses':'E/C with End(E)=Z, X=T=E, m=1, a=0, z=2c1(P), z(0)=0; D is symmetric; quotient is by full scheme-theoretic kernel; line bundle/divisor correspondences integral','scope':'refutes full-kernel integral descent, not connected-kernel descent, rational descent, or an unspecified positivity sign convention'}

out['koszul_zero_section']=[]
for g in range(0,9):
    dims=[comb(g,g-i) for i in range(g+1)]
    assert dims==[comb(g,i) for i in range(g+1)]
    out['koszul_zero_section'].append({'g':g,'degrees':list(range(g+1)),'dimensions':dims})
out['koszul_scope']='Le*e_*det(T)[-g] has H^i=Λ^(g-i)(T*)⊗det(T)≅Λ^i(T). The canonical contraction proves the isomorphism; dimensions alone do not check the manuscript comparison map.'

td=lambda y:y/(1-s.exp(-y))
assert s.simplify(td(x)*s.exp(-x)-td(-x))==0
out['todd_identity']={'exact':str(s.simplify(td(x)*s.exp(-x)-td(-x))),'Td(x)':str(s.series(td(x),x,0,7)),'Td(x)*exp(-x)':str(s.series(td(x)*s.exp(-x),x,0,7)),'relative_factor':'Td(Lie A) Td(Lie B) ch(det(Lie A)^*) = Td((Lie A)^*) Td(Lie B) = Td(H1_dR(A/S))','scope':'formal characteristic-class identity; rational Chow vanishing of final class uses Moonen Cor2.7, not this power series'}

# Translation convolution: m(x,u)=x+u, so the input is evaluated at y-u.
y,u,tv=s.symbols('y u t')
out['translation_signs']={'convolution_delta_u_argument':str(y-u),'T_t_pullback_argument':str(y+tv),'compatible_u':str(s.solve(s.Eq(y-u,y+tv),u)[0]),'Phi_P_t':'tau⊗delta_-t[-g]','rank_transform':'rank(Phi(F))=chi(F)','Euler_transform':'chi(Phi(F))=(-1)^g rank(F)'}

# Source degree filtration vs adic completion: verify inverse through finite orders.
out['completion_ungraded']={}
for n in [1,2,5,10]:
    inverse=-sum(x**j for j in range(n))
    product=s.expand((x-1)*inverse)
    assert product==1-x**n
    out['completion_ungraded'][str(n)]={'inverse_mod_xn':str(inverse),'product':str(product)}
out['completion_scope']='k[x]/(x-1)⊗k[x]k[[x]]=0 since x-1 invertible; this module is not a graded module for the standard grading, so the qualified graded faithfulness statement survives.'

out['dimension_checks']={'incidence_divisor_codimension':'m+m-(2m-1)=1','complementary_cycle_index':'i+j=n+1 for incidence; i+j=n for intersection degree on X','height_middle_condition':'2i=2j=n ⇒ i=j=n/2, n even; Y has dimension n-1=2i-1','Tate_splitting':'Given S↠T_lJ free of rank2d, choose basis e_j and lifts s_j. Map ∑a_j e_j↦∑a_j s_j is Z_l-linear section, hence injects T_lJ into S⊂H. Noncanonical; no equivariant or natural splitting asserted.'}

out['negative_polarization']={'hypotheses':'A a positive-dimensional abelian variety; L ample symmetric','lambda_L_inverse':'lambda_(L^-1)=-lambda_L is a symmetric isogeny','not_ample':'degree of L^-1 on any curve is negative','scope':'counterexample to symmetry+isogeny⇒positive; does not by itself refute the particular incidence D'}

out['nonnilpotent_flatness_counterexample']={'A':'k[t]','I':'(t)','test_algebra':'k[t,t^-1]','M':'A/(t)','joint_injection':True,'M_mod_I':'k, free rank1 overA/I','M_tensor_test':'0, free rank0','M_mod_I_squared':'k overR=k[t]/(t²)','flat':False,'certificate':'The injective ideal inclusion (t)→R becomes the zero map (t)⊗Rk≅k→R⊗Rk≅k. A flat module must preserve injections.','nilpotent_hypothesis_satisfied':False,'noetherian_and_separated':True,'scope':'literal amended Proposition4.1 after deleting I nilpotent; original nilpotent refinement is not refuted'}

# The displayed canceled root axioms omit crystallographic integrality.
# An orbit-wise rescaling preserves all reflections but need not preserve coroots.
roots=[(1,0),(-1,0),(0,1),(0,-1),(2,2),(-2,-2),(2,-2),(-2,2)]
rootset=set(roots)
certificates=[]
for av in roots:
    alpha=s.Matrix(av)
    coroot=2*alpha.T/(alpha.dot(alpha))
    reflection=s.eye(2)-alpha*coroot
    assert reflection*alpha == -alpha
    assert reflection**2 == s.eye(2)
    assert reflection.det() == -1
    assert all(q.q==1 for q in reflection)
    image={tuple(reflection*s.Matrix(v)) for v in roots}
    assert image==rootset
    collinear=[v for v in roots if s.det(s.Matrix.hstack(alpha,s.Matrix(v)))==0]
    assert set(collinear)=={av,tuple(-q for q in av)}
    certificates.append({'alpha':list(av),'reflection':[[str(q) for q in row] for row in reflection.tolist()],'coroot':[str(q) for q in coroot],'preserves_roots':True,'reduced_root_line':True})
assert (1,0) in rootset and (0,1) in rootset  # roots generate P=Z²
out['root_integrality_counterexample']={'P':'Z²','roots':[list(a) for a in roots],'generates_P':True,'certificates':certificates,'failed_claim':'For alpha=(2,2), gamma_alpha=(1/2,1/2), hence gamma_alpha(e1)=1/2 is not integral and alpha is not primitive.','scope':'all displayed finite/reduced/spanning/reflection-stability hypotheses hold; a crystallographic integrality or primitive-root hypothesis is missing','refinement':'If every root alpha is primitive in P, then (1-s_alpha)P⊂P∩Qalpha=Zalpha, so gamma_alpha(P)⊂Z.'}

out['symmetric_hom_factor_two']={'setup':'f:A→A∨, f∨=f under biduality; P normalized Poincare bundle','construction':'L=(id_A,f)^*P','calculation':'lambda_L = [id,f]∨ [[0,id],[id,0]] [id,f] = f+f∨ = 2f','scope':'integral factor-two construction; no ampleness follows from symmetry alone'}

(ROOT/'outputs/computations.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
print('All exact algebraic assertions passed. Geometric scope limitations recorded explicitly.')
