"""Exact algebra supporting the independent cote9:13–14 counterexample.

The p-adic existence statements use Hensel's lemma and elementary discriminant
and CM arguments written in proofs.md. This script checks the division
polynomial, all valuations, and the complete finite residue calculation.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json
W=Path(__file__).resolve().parents[1]
def add(A,B):
    C=A.copy()
    for k,v in B.items():C[k]=C.get(k,0)+v
    return {k:v for k,v in C.items() if v}
def smul(A,c):return {k:c*v for k,v in A.items() if c*v}
def mul(A,B):
    C={}
    for (i,j),v in A.items():
        for (k,l),w in B.items():C[i+k,j+l]=C.get((i+k,j+l),0)+v*w
    return {k:v for k,v in C.items() if v}
def pw(A,n):
    C={(0,0):1}
    for _ in range(n):C=mul(C,A)
    return C
# psi5 = psi4 psi2^3 - psi3^3, with y²=x³+B.
f={(3,0):1,(0,1):1}
q={(6,0):1,(3,1):20,(0,2):-8}
psi3={(4,0):3,(1,1):12}
psi5=add(smul(mul(pw(f,2),q),32),smul(pw(psi3,3),-1))
expected={(12,0):5,(9,1):380,(6,2):-240,(3,3):-1600,(0,4):-256}
assert psi5==expected
def val(n,p=5):
    v=0
    while n%p==0:n//=p;v+=1
    return v
rows=[];normalized=[]
for (x,b),c in sorted(psi5.items(),reverse=True):
    # t^8=5, B=5^4=t^32, x=t^10 X; divide by t^128.
    cv=val(abs(c));exponent=8*cv+32*b+10*x-128
    assert exponent>=0
    unit=c//5**cv
    rows.append({'x_power':x,'B_power':b,'coefficient':c,'v5_coefficient_after_B_5^4':cv+4*b,'v5_term_after_x_5^(5/4)':str(Fraction(cv+4*b)+Fraction(5*x,4))})
    normalized.append({'X_power':x,'t_power':exponent,'integer_unit':unit})
assert normalized==[{'X_power':12,'t_power':0,'integer_unit':1},{'X_power':9,'t_power':2,'integer_unit':76},{'X_power':6,'t_power':4,'integer_unit':-48},{'X_power':3,'t_power':14,'integer_unit':-64},{'X_power':0,'t_power':0,'integer_unit':-256}]

# F25=F5[a]/(a²−2), since 2 is nonsquare modulo5.
E=list(product(range(5),repeat=2));zero=(0,0);one=(1,0)
def fm(x,y):return ((x[0]*y[0]+2*x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0])%5)
def fp(x,n):
    y=one
    for _ in range(n):y=fm(y,x)
    return y
roots=[x for x in E if fp(x,12)==one]
pairs=[(x,y) for x in roots for y in E if fp(y,2)==fp(x,3)]
assert len(roots)==12 and len(pairs)==24
assert all(fm((2,0),fp(x,11))!=zero for x in roots) # derivative12X11 mod5
assert all(fm((2,0),y)!=zero for x,y in pairs)
assert len({x for x,y in pairs})==12

# E'=y²=x³−x, good ordinary CM by Z[i]. Its etale p-character has order4.
trace=-2;tr=[2,trace]
for n in range(2,5):tr.append(trace*tr[-1]-5*tr[-2])
counts={n:5**n+1-tr[n] for n in range(1,5)}
assert counts=={1:8,2:32,3:104,4:640}
assert pow(3,4,5)==1 and pow(3,2,5)!=1

result={
 'type':'exact polynomial, valuation, and finite-field certificate; p-adic proof in proofs.md',
 'E_bad':'y²=x³+5⁴ over Q5',
 'K':'F(5^(1/8)), F/Q5 the unramified extension of degree4',
 'ramification_index':8,'residue_field':'F625','contains_unramified_quadratic':True,
 'division_polynomial':[{ 'x_power':i,'B_power':j,'coefficient':c} for (i,j),c in sorted(psi5.items(),reverse=True)],
 'valuation_table':rows,'normalized_polynomial_terms':normalized,
 'normalized_polynomial':'X^12+76t²X^9−48t⁴X^6−64t^14X³−256, t⁸=5',
 'residue_polynomial':'X^12−1 over F25','simple_residue_x_roots':roots,
 'simple_residue_xy_pairs':pairs,'nonzero_5_torsion_points_lifted_by_Hensel':24,
 'y_equation_after_scaling':'Y²=X³+t², y=t^15Y',
 'E_bad_discriminant':'−432*5⁸','v5_discriminant':8,
 'vK_discriminant':64,'vK_discriminant_mod12':4,
 'good_reduction_impossible_over_K':'A unit-discriminant equation would change valuation64 by a multiple of12.',
 'good_reduction_over_cubic_extension':'u=5^(2/3), x=u²X, y=u³Y gives Y²=X³+1',
 'special_fiber_supersingular':'coefficient of x⁴ in (x³+1)² is0 modulo5',
 'inertial_image_order':3,'trace_on_nonidentity_inertia':-1,
 'mu5_in_K':'Weil pairing because all E_bad[5] points are K-rational',
 'E_good':'y²=x³−x; CM automorphism (x,y)↦(−x,iy), i∈Q5',
 'E_good_point_counts':counts,'etale_5_Frobenius_eigenvalue_mod5':3,'etale_character_order':4,
 'E_good_5_torsion_in_K':'CM splits E_good[5] into two Q5-stable lines; the etale line is trivial over F, and the other character is cyclotomic times its inverse, hence trivial over K.',
 'two_curve_hypotheses':{'complete_DVR_fraction_field':True,'residue_perfect':True,'contains_mu5':True,'both_potentially_good':True,'both_E5_trivial_rank2':True},
 'inertia_traces_differ':{'E_bad':-1,'E_good':2,'inertia_element_order':3,'prime_to_p':True},
 'historical_attribution':'Independent construction in this run; not claimed to be the example Tate gave Grothendieck.'
}
(W/'outputs/elliptic_inertia_counterexample.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['E_bad','K','normalized_polynomial','nonzero_5_torsion_points_lifted_by_Hensel','vK_discriminant_mod12','inertial_image_order','E_good','two_curve_hypotheses','inertia_traces_differ','historical_attribution']},ensure_ascii=False,indent=2))
