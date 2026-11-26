#!/usr/bin/env python3
"""Exact small arithmetic checks for the exponent-31 feasibility report.
No L-value computation and no conjectural rank/Sha claim.
Run: python check_thirtyone.py
"""
from fractions import Fraction
from math import comb
import json
import sympy as sp

p=31; g=3; H={1,5,25}
S={b for b in range(1,p) if b+(5*b%p)<p}
assert len(S)==15
stabilizer=[a for a in range(1,p) if {a*b%p for b in S}==S]
assert set(stabilizer)==H
assert sp.n_order(g,p)==30
CM_cosets=[{pow(g,j,p)*h%p for h in H} for j in range(10)]
T=[j for j,cc in enumerate(CM_cosets) if cc<=S]
assert T==[0,1,2,4,8]
assert [j for j in range(10) if {(t+j)%10 for t in T}==set(T)]==[0]

B=[Fraction(1)]
for n in range(1,29):
    B.append(-sum(Fraction(comb(n+1,k))*B[k] for k in range(n))/Fraction(n+1))
regularity=[(k,B[k].numerator%p) for k in range(2,29,2)]
assert all(v for k,v in regularity)
B28=(B[28].numerator*pow(B[28].denominator,-1,p))%p
assert B28==14
mod=p*p
aa=pow(5,5,mod)*pow(pow(-6,6,mod),-1,mod)%mod
q=((pow(aa,p-1,mod)-1)//p)%p
assert q==0
assert (q**3+5*(-6)*B28)%p==14

R=H|{(-h)%p for h in H}
RC=[sorted({pow(g,j,p)*h%p for h in R}) for j in range(5)]
def multiply_periods(A,B):
    c=[0]*p
    for a in A:
        for b in B:c[(a+b)%p]+=1
    assert all(len({c[t] for t in cc})==1 for cc in RC)
    return [c[cc[0]]-c[0] for cc in RC]
mat=sp.Matrix.hstack(*[sp.Matrix(multiply_periods(RC[0],cc)) for cc in RC])
poly=mat.charpoly().all_coeffs()
assert poly==[1,1,-12,-21,1,5]
assert mat.det()==-5
mink=Fraction(120*31**2,5**5)
assert mink<37
small=[]
for prime in list(sp.primerange(2,37)):
    if prime==31:small.append((prime,1));continue
    f=next(i for i in range(1,6) if pow(prime,i,p) in R)
    if prime**f<=mink:small.append((int(prime),f))
assert small==[(2,5),(5,1),(31,1)]

z=sp.symbols('z')
num=sum(pow(g,j,p)*z**j for j in range(30))
reduced=sp.rem(num,sp.cyclotomic_poly(10,z),z)
assert reduced==-62*z
quad=sum(pow(g,j,p)*(-1)**j for j in range(30))
assert quad==-93
norm_order10=Fraction(62**4,p**4)
assert norm_order10==16
relative=Fraction(2,2**5)*(-Fraction(quad,p))*norm_order10
assert relative==3

out={
 "arithmetic":"exact integer/rational; no L-values",
 "software":{"python":"standard Fraction/int arithmetic","sympy":sp.__version__},
 "p":p,"a":5,"primitive_root":g,"H":sorted(H),"CM_type_K":sorted(S),
 "CM_type_M":T,"CM_type_stabilizer_K":stabilizer,
 "CM_type_parity_balance":sum((-1)**t for t in T),
 "bernoulli_numerator_residues":regularity,"B28_mod31":B28,
 "fermat_quotient_argument_mod31sq":aa,"fermat_quotient_mod31":q,
 "McCallum_Tzermias_condition_mod31":14,
 "real_period_cosets":RC,"period_multiplication_matrix":mat.tolist(),
 "period_minpoly_coefficients":list(map(int,poly)),
 "period_norm":int(mat.det()),"Minkowski_bound":str(mink),
 "small_prime_ideals_q_f":small,
 "order10_B1_numerator_reduced":str(reduced),
 "quadratic_B1":str(Fraction(quad,p)),
 "order10_B1_norm":str(norm_order10),
 "relative_class_number_given_proved_unit_index_1":str(relative),
 "theorem_dependent_conclusions":{"h_real":1,"h_CM":3,"rank_J_upper_bound":4,"rank_P_possibilities":[0,2]},
 "not_proved":["rank P=0","L(P,1) nonzero","full Sha(P) finite"]
}
print(json.dumps(out,indent=2,default=int))

