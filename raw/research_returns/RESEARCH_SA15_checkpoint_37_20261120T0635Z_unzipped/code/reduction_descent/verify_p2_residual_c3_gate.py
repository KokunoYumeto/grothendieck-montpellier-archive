#!/usr/bin/env python3
"""Universal Chen mod8 identities and the residual-C3 valuation gate."""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp
started=perf_counter()
C,D,t,x,A,B,u,z=sp.symbols('C D t x A B u z')
checks=[]
ae=(C*t**8+8*D*t**7+28*C**2*t**6+56*C*D*t**5+
    (-42*C**3+112*D**2)*t**4+56*C**2*D*t**3+
    (252*C**4-224*C*D**2)*t**2+(264*C**3*D-256*D**3)*t+
    81*C**5-80*C**2*D**2)
be=(D*t**12+12*C**2*t**11+66*C*D*t**10+(44*C**3+176*D**2)*t**9+
    495*C**2*D*t**8+792*C**4*t**7+924*C**3*D*t**6+
    (-2376*C**5+3168*C**2*D**2)*t**5+
    (-5841*C**4*D+6336*C*D**3)*t**4+
    (-1188*C**6-4224*C**3*D**2+5632*D**4)*t**3+
    (-4158*C**5*D+4224*C**2*D**3)*t**2+
    (-2916*C**7+4464*C**4*D**2-1536*C*D**4)*t+
    (-1215*C**6*D+2240*C**3*D**3-1024*D**5))
phi=t**6-15*C*t**4-40*D*t**3-45*C**2*t**2-24*C*D*t+27*C**3-32*D**2
assert sp.Poly(ae**3-be**2-(C**3-D**2)*phi**4,C,D,t).is_zero
checks.append('Appendix full universal discriminant identity')
q=t*t-sp.Rational(2,3)*x*t-(2*x*x+A)/9
norm=sp.resultant(x**3+A*x+B,q,x)
assert sp.expand(norm.subs({A:-27*C,B:-54*D})-phi)==0
checks.append('Norm of the cusp-pair quadratic is the discriminant sextic')
disc=-4*A**3-27*B**2
alpha7=-(3*x*x+A)
alpha3=6*A*x*x-9*B*x+4*A*A
def reduce(expr):
    num=sp.together(expr).as_numer_denom()[0]
    return sp.rem(sp.Poly(num,x),sp.Poly(x**3+A*x+B,x)).as_expr()
assert sp.expand(reduce(alpha7*alpha3-disc))==0
checks.append('Power3 scaling equals D divided by power7 scaling')
r3=((6*A*t*t+6*B*t-sp.Rational(2,9)*A*A)*x*x+
    (sp.Rational(4,3)*A*A*t+A*B/3-9*B*t*t)*x+
    (-sp.Rational(4,9)*A**3+4*A*A*t*t+4*A*B*t-2*B*B))
r7=-(3*t*t+A/9)*x*x-(sp.Rational(4,3)*A*t+sp.Rational(2,3)*B)*x-A*t*t-2*B*t+A*A/9
assert sp.expand(reduce(alpha3*q-r3))==0
assert sp.expand(reduce(alpha7*q-r7))==0
checks += ['Theorem1.3 coefficient identity','Theorem1.4 coefficient identity']
theta=z+u*z*z
normalA=-6*u;normalB=-2-4*u**3
assert sp.rem(sp.Poly(theta**3+normalA*theta+normalB,z),sp.Poly(z**3-2,z)).is_zero
normalDelta=-16*(4*normalA**3+27*normalB**2)
assert sp.expand(normalDelta+1728*(1-2*u**3)**2)==0
checks += ['Trace-zero cubic-root normal form','Normalized discriminant']
normalc4=-48*normalA
assert sp.expand(normalc4-288*u)==0
checks.append('Normalized c4')
valuation_cases=0
for k in range(-100,101):
    for h in range(101):
        vals=[6*k,4+3*k,5,3+3*h]
        low=min(vals)
        assert vals.count(low)==1
        expected=6*k if k<=0 else (3 if h==0 else 5)
        assert low==expected
        if k<=0:assert (6+4*low)%3==0
        else:
            for scale in [0,6,4,2]:assert (low+scale)%2==1
        valuation_cases+=1
normalization_cases=0
for va in range(-30,31):
    for vb in range(-30,31):
        rootval=min(3*va+1,3*vb+2)
        deltaval=4+2*rootval
        if deltaval%3==0:
            assert 3*va+1<3*vb+2 and vb-va>=0
        normalization_cases+=1
out={'status':'PASS','scope':'Universal original Chen polynomial identities and complete valuation branches; the moduli necessity and field normalization are proved in the TeX',
     'identities':checks,'discriminant_sextic':str(phi),
     'scaling_valuations_in_F':{'r1':0,'r5':6,'r3':4,'r7':2},
     'valuation_cases':valuation_cases,'normalization_cases':normalization_cases,
     'source_sign_note':'The chosen minus sign in q agrees with Chen Theorems1.1--1.4 and the Appendix identity; Lemma3.2 prints the opposite cusp-sum sign. Valuation conclusions are unchanged by t -> -t.',
     'elapsed_seconds':perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
