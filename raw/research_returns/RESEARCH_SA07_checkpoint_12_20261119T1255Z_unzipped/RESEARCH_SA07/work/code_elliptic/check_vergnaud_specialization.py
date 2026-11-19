#!/usr/bin/env python3
"""Exact input and normalization checks for the Vergnaud-thesis route.

This is an applicability certificate, not a transcendence calculation.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as sp

started = time.perf_counter()
utc_start = datetime.now(timezone.utc).isoformat()
lam, X, U = sp.symbols('lam X U')
checks = []

def check(name, expression):
    assert sp.cancel(expression) == 0, (name, expression)
    checks.append(name)

e1 = (2-lam)/3
e2 = (2*lam-1)/3
e3 = -(1+lam)/3
g2 = -4*(e1*e2+e1*e3+e2*e3)
g3 = 4*e1*e2*e3
check('roots sum to zero', e1+e2+e3)
check('short Legendre polynomial', 4*(X-e1)*(X-e2)*(X-e3)-(4*X**3-g2*X-g3))
check('Legendre change of x', (4*X**3-g2*X-g3).subs(X,U-(1+lam)/3)-4*U*(U-1)*(U-lam))
j = sp.cancel(1728*g2**3/(g2**3-27*g3**2))
check('j lambda formula', j-256*(1-lam+lam**2)**3/(lam**2*(1-lam)**2))
j_star = sp.Rational(1728*4**3, 4**3-27)
check('E star j', j_star-sp.Rational(110592,37))
P = sp.Poly(37*(lam**2-lam+1)**3-432*lam**2*(1-lam)**2,lam)
check('E star Legendre equation', P.as_expr()-sp.Rational(37,256)*lam**2*(1-lam)**2*(j-j_star))
assert P.all_coeffs()==[37,-111,-210,605,-210,-111,37]
checks.append('primitive Legendre polynomial coefficients')
candidates = sorted(set(sp.Rational(a,b) for a in (-37,-1,1,37) for b in (1,37)))
root_values = {str(r):str(P.eval(r)) for r in candidates}
assert all(P.eval(r)!=0 for r in candidates)
checks.append('all rational-root-theorem candidates excluded')

# Let s=sn(u|lam). Then s'^2=(1-s^2)(1-lam*s^2) and
# s''=-(1+lam)s+2lam*s^3. The derivative of s'/s is exact below.
s = sp.symbols('s', nonzero=True)
sp2=(1-s**2)*(1-lam*s**2)
spp=-(1+lam)*s+2*lam*s**3
log_derivative=(spp*s-sp2)/s**2
check('Jacobi logarithmic derivative', log_derivative-(-1/s**2+lam*s**2))
# E'(u)=dn(u)^2=1-lam*sn(u)^2; x=e3+sn(u)^-2.
zeta_derivative=log_derivative+1-lam*s**2+(lam-2)/3
check('zeta derivative normalization', zeta_derivative+e3+1/s**2)
K, EE, eta, omega, h, hV = sp.symbols('K EE eta omega h hV')
check('quasiperiod shear', (2*EE+2*(lam-2)*K/3)+(2-lam)*(2*K)/3-2*EE)
shear = sp.Matrix([[1,0],[(2-lam)/3,1]])
assert shear.det()==1 and sp.simplify(shear.inv()*shear)==sp.eye(2)
checks.append('invertible algebraic shear of the two normalized periods')

result={'utc_start':utc_start,'elapsed_seconds':time.perf_counter()-started,
        'sympy_version':sp.__version__,'checks':checks,'number_of_checks':len(checks),
        'inputs':{'E_star_g2':4,'E_star_g3':1,'j':str(j_star),
                  'Legendre_polynomial':str(P.as_expr()),
                  'rational_root_candidates':root_values},
        'result':'PASS: exact specialization and normalization only; H1 unchanged'}
base=Path(__file__).with_suffix('')
base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
lines=[f'PASS {i+1}: {name}' for i,name in enumerate(checks)]
lines+=['RATIONAL_ROOT_CANDIDATES '+json.dumps(root_values,sort_keys=True),
        'FINAL '+result['result'],f'WALL_SECONDS {result["elapsed_seconds"]:.9f}']
text='\n'.join(lines)+'\n'
base.with_suffix('.out').write_text(text)
print(text,end='')
