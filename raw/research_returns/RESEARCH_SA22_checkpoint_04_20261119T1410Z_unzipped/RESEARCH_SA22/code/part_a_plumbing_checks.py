"""Exact specialization of Hinich's plumbing counterexample, equations (5)-(9).

This checks the finite rational arithmetic and residue cancellation. The
global plumbing coordinate and the moduli cross-ratio are proved directly in the paper.
"""
from fractions import Fraction as F
import json,time
import sympy as S
start=time.perf_counter()
R,B,C,eps=F(3,2),F(3,4),F(10),F(1,10)
A=C*(R-B)*(C-2*R)/(C*C-2*R*C+R*B)
assert A==F(420,569)
assert abs(A)<1-eps and abs(B)<1-eps and A!=B
assert R>1+eps and abs(C)>1+eps and abs(C-2*R)>1+eps
phi=lambda z:(z-R)**2
a,b,c=map(phi,(A,B,C))
assert len({a,b,c})==3
res_a=4*A*(A-R)**2/((2*A-2*R)*(A-B)*(A+B-2*R)*(A-C)*(A+C-2*R))
res_b=4*B*(B-R)**2/((B-A)*(B+A-2*R)*(2*B-2*R)*(B-C)*(B+C-2*R))
assert res_a+res_b==0
t=S.symbols('t')
rat=lambda q:S.Rational(q.numerator,q.denominator)
k=S.Rational(11,9)*t
at=(rat(R)-k*rat(A))**2
bt=(rat(R)-k*rat(B))**2
lam=(at-rat(c))/(bt-rat(c))
t0=S.Rational(9,11)
first=S.factor(S.diff(lam,t).subs(t,t0))
second=S.factor(S.diff(lam,t,2).subs(t,t0))
assert first==0
assert second!=0
print(json.dumps(dict(status='PASS',A=str(A),B=str(B),C=str(C),R=str(R),epsilon=str(eps),
 plumbing_t=str((1-eps)/(1+eps)),marks=[str(x) for x in (a,b,c)],
 residues=[str(res_a),str(res_b)],residue_sum='0',
 injectivity_certificate='If phi(z)=phi(w), z=w or z+w=2R; |z|,|w|<11/10 excludes the second alternative since 2R=3.',
 exact_assertions=7,cross_ratio=str(lam),cross_ratio_derivative=str(first),cross_ratio_second_derivative=str(second),seconds=round(time.perf_counter()-start,6)),indent=2))
