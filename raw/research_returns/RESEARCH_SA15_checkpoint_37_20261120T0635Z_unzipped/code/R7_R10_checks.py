"""Exact certificates for the elliptic families in the R9 audit.

The general all-prime argument is in R7_R10_audit.tex.  This program
checks its explicit Weierstrass equations and sample coefficient identities;
it does not substitute finite sampling for the binomial proof.
"""
from pathlib import Path
import json
from math import comb
from time import perf_counter
import sympy as s

started = perf_counter()
x, lam, t = s.symbols('x lambda t')

def invariants(a1, a2, a3, a4, a6):
    b2 = a1*a1 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    delta = s.expand(-b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6)
    c4 = s.expand(b2*b2 - 24*b4)
    return delta, c4

legendre_delta, _ = invariants(0, -(1+lam), 0, lam, 0)
assert s.expand(legendre_delta - 16*lam**2*(1-lam)**2) == 0
char2_delta, char2_c4 = invariants(t, 0, 1, 0, 0)
assert char2_delta == t**3-27
assert s.Poly(char2_delta-(t**3+1),t,modulus=2).is_zero
assert s.Poly(char2_c4-t**4,t,modulus=2).is_zero
checks=[]
for p in (3,5,7,11,13,17,19):
    m=(p-1)//2
    hp=sum(comb(m,i)**2*lam**i for i in range(m+1))
    actual=s.Poly(s.expand((x*(x-1)*(x-lam))**m),x).coeff_monomial(x**(p-1))
    assert s.expand(actual-(-1)**m*hp)==0
    assert hp.subs(lam,0)==1
    assert hp.subs(lam,1)==comb(p-1,m)
    assert int(hp.subs(lam,1))%p!=0
    checks.append({'p':p,'degree':m,'Hasse_polynomial_mod_p':str(s.Poly(hp,lam,modulus=p).as_expr()),
                   'Hasse_at_0':1,'Hasse_at_1_mod_p':int(hp.subs(lam,1))%p,
                   'coefficient_identity_over_Z':'PASS'})
assert s.Poly((1+lam).subs(lam,2+t)-t,t,modulus=3).is_zero
out={
    'arithmetic':'exact integers and exact polynomial reduction; no floating point',
    'legendre_discriminant':str(s.factor(legendre_delta)),
    'characteristic_2_family':{'equation':'y^2+t*x*y+y=x^3',
        'discriminant_over_Z':str(char2_delta),'discriminant_mod_2':'t^3+1',
        'c4_over_Z':str(char2_c4),'c4_mod_2':'t^4','Hasse_mod_2':'a1=t'},
    'characteristic_3_family':{'parameter':'lambda=2+t','Hasse_mod_3':'t'},
    'legendre_checks':checks,'result':'PASS',
    'elapsed_seconds':round(perf_counter()-started,6)}
path=Path(__file__).with_name('R7_R10_checks_output.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
