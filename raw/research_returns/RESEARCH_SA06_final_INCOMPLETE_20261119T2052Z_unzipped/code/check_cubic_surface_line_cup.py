"""Exact polynomial and rank checks for the cubic-line cup-product research note.

The coherent duality and divisor-obstruction proof is separate; no finite
sample is asserted to certify a local Chow-kernel theorem.
"""
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
import json
import sympy as sp

root = Path(__file__).resolve().parents[1]
started = datetime.now(timezone.utc).isoformat()
tic = perf_counter()
u, v, s, t, w = sp.symbols('u v s t w')
checks = []

def check(name, value, data=None):
    passed = bool(value)
    checks.append({'name': name, 'passed': passed, 'data': data})
    if not passed:
        raise AssertionError(name)

fermat = (u-s)**3+s**3+(v-t)**3+t**3
expanded = u**3-3*u**2*s+3*u*s**2+v**3-3*v**2*t+3*v*t**2
check('Fermat_coordinate_change', sp.expand(fermat-expanded) == 0)
check('Fermat_first_line_quadric', sp.diff(fermat, u).subs({u:0,v:0}) == 3*s*s)
check('Fermat_second_line_quadric', sp.diff(fermat, v).subs({u:0,v:0}) == 3*t*t)

three = u*s*s+v*t*t+u*u*t+v*v*s
grad = [sp.diff(three, z) for z in (u,v,s,t)]
expected = [s*s-u*t,t*t-v*s,-u*s+v*v,-v*t+u*u]
check('char3_gradient_identity', all(sp.Poly(a-b,u,v,s,t,modulus=3).is_zero for a,b in zip(grad,expected)))
# With u=1, v^5=1, one has s=v^2 and t=v^4=v^-1.
substitution = {u:1,v:w,s:w*w,t:w**4}
critical_gradient = [sp.rem(sp.Poly(g.subs(substitution),w,modulus=3),sp.Poly(w**5-1,w,modulus=3)).as_expr() for g in grad]
critical_value = sp.rem(sp.Poly(three.subs(substitution),w,modulus=3),sp.Poly(w**5-1,w,modulus=3)).as_expr()
check('char3_critical_equations', all(g == 0 for g in critical_gradient), [str(g) for g in critical_gradient])
check('char3_critical_value_nonzero', critical_value == w**4 and sp.gcd(sp.Poly(w**4,w,modulus=3),sp.Poly(w**5-1,w,modulus=3)).degree() == 0, str(critical_value))
for z in (u,v,s,t):
    other = [a for a in (u,v,s,t) if a != z]
    ideal = sp.groebner([g.subs(z,0) for g in grad],*other,modulus=3)
    # Each remaining coordinate has fourth power in the gradient ideal; hence no
    # geometric projective critical point has a zero coordinate.
    check('char3_zero_'+str(z)+'_forces_origin', all(ideal.reduce(a**4)[1] == 0 for a in other), {'groebner_basis':[str(g) for g in ideal.polys], 'fourth_power_remainders':[str(ideal.reduce(a**4)[1]) for a in other]})

gram = sp.zeros(4)
gram[2,3] = gram[3,2] = 1
check('line_cup_rank_two_over_Z', gram.rank() == 2, [[int(a) for a in row] for row in gram.tolist()])
for prime in (2,3,5,7,11):
    check('line_cup_nonzero_minor_mod_'+str(prime), int(gram[2:4,2:4].det()) % prime != 0)

adams_value = (4-8)*(4-16)*(4-32)
check('fivefold_Adams_multiplier_unit_mod5', adams_value == -1344 and adams_value % 5 == 1, adams_value)
report = {
    'started_utc': started,
    'runtime_seconds': perf_counter()-tic,
    'scope': 'Exact cubic coordinate, characteristic-three critical-point, cup-rank and proposed fivefold Adams-multiplier algebra only. The cohomology and any local cycle conclusion require the separate written proofs.',
    'checks': checks,
    'passed': sum(c['passed'] for c in checks),
    'failed': sum(not c['passed'] for c in checks),
}
(root/'logs/cubic_surface_line_cup_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
