"""Independent targeted audit of the parent's Hodge proof; exact checks only.

This program checks explicitly authored identities and inequalities. It does not
infer a claim's status from text or from a search result.
"""
from pathlib import Path
import json
import sympy as s

P=Path(__file__).resolve().parents[1]
out={}
a,ab=s.symbols('a abar')
rho=s.symbols('rho',positive=True,real=True)
beta=-2*s.I*rho
c=(a*ab-1)/beta
old=s.Matrix([[a,c],[beta,-ab]])
oldbar=s.Matrix([[ab,-c],[-beta,-a]])
out['rejected_matrix_residual']=str(s.simplify(old*oldbar-s.eye(2)))
M=s.Matrix([[a,c],[beta,ab]])
Mbar=s.Matrix([[ab,-c],[-beta,a]])
res=s.simplify(M*Mbar-s.eye(2))
assert res==s.zeros(2)
assert s.simplify(M.det())==1
assert s.simplify(4*rho*c/(2*s.I)-(a*ab-1))==0
out['corrected_matrix_residual']=str(res)
out['corrected_matrix_determinant']=str(s.factor(M.det()))
out['corrected_four_rho_sigma']=str(s.factor(4*rho*c/(2*s.I)))

r=s.Rational(1,200)
Pfactor=(1+4*r+r*r)/(1-r)**4
exp_lower=sum(s.Rational(27,5)**k/s.factorial(k) for k in range(21))
assert exp_lower>200
assert Pfactor<s.Rational(21,20)
assert Pfactor-1<1
derivative_upper=48*10*s.Rational(3,800)*s.Rational(21,20)
assert derivative_upper<3
out['zero_locus_bounds']={
    'exp_5_4_Taylor20':str(exp_lower),
    'exp_5_4_Taylor20_gt200':True,
    'sum_n3_rn_divided_by_r_at_1_over200':str(Pfactor),
    'factor_lt21_over20':True,
    'tail_divided_by_first':str(Pfactor-1),
    'derivative_upper':str(derivative_upper),
    'derivative_upper_lt3':True,
    'scope':'The monotonicity and Fourier sign arguments are read and explained in review.md; these exact inequalities support them.'}

w,wb,y,F,Delta,K=s.symbols('omega1 omega1bar y E2star Delta K',nonzero=True)
real_a=-(wb/w)*s.pi*y*F/3
Delta_coeff=K*Delta/w**12
positive_prefactor=(w*wb)**6*(s.pi*y/3)**6/K
phase_res=s.factor(real_a**6/Delta_coeff-positive_prefactor*F**6/Delta)
assert phase_res==0
out['phase_identity_residual']=str(phase_res)
out['positive_prefactor']='|omega1|^12*(pi*y/3)^6/K, with y>0 and K>0'

x=s.symbols('x')
poly=s.Poly(x**6+4,x,domain=s.QQ)
assert poly.is_irreducible
out['abstract_Hodge_counterexample']={
    'tau':'I*real_cuberoot(2)',
    'minimal_polynomial':'x^6+4',
    'irreducible_over_Q':bool(poly.is_irreducible),
    'argument':'The two lines spanned by(1,tau) and(1,conjugate(tau)) are Qbar-defined. An endomorphism of Z+Z*tau beyond Z would force a quadratic equation overQ for tau, impossible. This refutes the overbroad abstract Betti-Hodge assertion in the model-generated UQ answer, not Katz’s algebraic-elliptic-curve conjecture.'}

(P/'outputs/check_review.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
