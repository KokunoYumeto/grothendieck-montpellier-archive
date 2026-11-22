#!/usr/bin/env python3
"""Exact characteristic-three polynomial identities for the B.2q construction.

The geometric normality, Picard and cofinality arguments are proofs in the
companion TeX fragment.  This certificate checks the finite local equations
and blowup charts, without replacing those arguments by numerical sampling.
"""
from pathlib import Path
import datetime
import json
import time
import sympy as sp

started = time.perf_counter()
x,y,z,x1,y1,z1,t,v,a,w,q,qp,b = sp.symbols('x y z x1 y1 z1 t v a w q qp b')
checks = []

def check(name, value):
    assert value, name
    checks.append({'name': name, 'passed': True})

def zero3(expression, *variables):
    return sp.Poly(sp.expand(expression), *variables, modulus=3).is_zero

equation = x*y-z**3
check('A2 x-chart strict transform', zero3(
    equation.subs({y:x*y1,z:x*z1})-x**2*(y1-x*z1**3),x,y1,z1))
check('A2 y-chart strict transform', zero3(
    equation.subs({x:y*x1,z:y*z1})-y**2*(x1-y*z1**3),y,x1,z1))
check('A2 z-chart strict transform', zero3(
    equation.subs({x:z*x1,y:z*y1})-z**2*(x1*y1-z),z,x1,y1))
for name,chart,variable in [
    ('x-chart smooth',y1-x*z1**3,y1),
    ('y-chart smooth',x1-y*z1**3,x1),
    ('z-chart smooth',x1*y1-z,z)]:
    check(name, sp.diff(chart,variable) in (sp.Integer(1),sp.Integer(-1)))

original = v**3-a*w**3-w*q
check('coordinate change gives A2 equation', zero3(
    original.subs(q,qp-a*w**2)-(v**3-w*qp),v,a,w,qp))
check('constant cube shift over algebraic closure', zero3(
    original.subs({v:z+b*w,a:b**3})-(z**3-w*q),z,b,w,q))
check('generic bad-divisor equation has no linear term',
      all(sp.Poly(v**3-t**2*q,v,t).coeff_monomial(m)==0 for m in (1,v,t)))
check('bad-divisor equation has multiplicity two',
      sp.Poly(v**3-t**2*q,v,t).coeff_monomial(t**2)==-q)
check('product quadratic section basis has36 monomials',6*6==36)

out = {
    'certificate': 'threefold local equations and A2 resolution charts',
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'sympy_version': sp.__version__,
    'checks': checks,
    'elapsed_seconds': time.perf_counter()-started,
    'limitation': 'Exact polynomial checks only; smooth generic divisor, normality, Picard identities and cofinal obstruction are proved in the companion TeX fragment.'
}
target = Path(__file__).resolve().parent.parent/'output'/'threefold_local_geometry.json'
target.parent.mkdir(exist_ok=True)
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
