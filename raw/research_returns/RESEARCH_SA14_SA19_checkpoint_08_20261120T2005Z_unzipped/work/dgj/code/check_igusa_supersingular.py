"""Exact finite algebra checks for D4s; does not mechanize deformation theory."""
from pathlib import Path
import json
import time
import sympy as sp

started = time.perf_counter()
t, s, w = sp.symbols('t s w')
curve = w**2 + (1+t*s)*w - s**3
den = 1+t*s+w
fixed = s*(2+t*s+w)
quartic = s**4-t*s**2-2*s
assert sp.expand((w-1)*fixed-quartic-s*curve) == 0
assert sp.rem((w-1)*fixed, sp.Poly(curve,w),w).as_expr() == quartic

# The inversion preserves the curve equation, after clearing denominator.
si, wi = -s/den, -w/den
inverted = sp.cancel((wi**2+(1+t*si)*wi-si**3)*den**3)
assert sp.expand(inverted+curve) == 0
assert sp.cancel(si-s+s*(2+t*s+w)/den) == 0
assert sp.cancel(wi-w+w*(2+t*s+w)/den) == 0

# General Weierstrass discriminant, a1=t, a2=a4=a6=0, a3=1.
b2, b4, b6, b8 = t*t, t, sp.Integer(1), sp.Integer(0)
disc = sp.expand(-b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6)
assert disc == t**3-27

# The normalizing coordinate changes, at the supersingular equation.
# Rows a2',a3'-1,a4',a6'; columns r,lambda-1,b,d.
jac = sp.Matrix([[3,0,0,0],[0,-3,0,2],[0,0,-1,0],[0,0,0,-1]])
assert int(jac.det()) % 2 == 1

# Explicit formal solution w(s), enough to verify the local ideal truncation.
order = 13
wseries = sp.Integer(0)
for _ in range(order):
    wseries = sp.series(s**3-t*s*wseries-wseries**2,s,0,order).removeO().expand()
assert sp.expand(sp.series(curve.subs(w,wseries),s,0,order).removeO()) == 0
special = sp.Poly(quartic.subs(t,0),s,modulus=2).as_expr()
assert special == s**4

out = {
    'input_elliptic_curve': 'y^2+t*x*y+y=x^3 over W(k)[[t]], char(k)=2',
    'coordinate_chart': 's=x/y, w=1/y',
    'discriminant': str(disc),
    'curve_equation': str(curve),
    'inversion': ['-s/(1+t*s+w)','-w/(1+t*s+w)'],
    'inversion_cleared_curve_identity': 'curve(inverse)*denominator^3 = -curve',
    'exact_ideal_identity': '(w-1)*s*(2+t*s+w) - (s^4-t*s^2-2*s) = s*curve',
    'formal_w_mod_s13': str(wseries),
    'normalizing_jacobian': [[int(x) for x in row] for row in jac.tolist()],
    'normalizing_jacobian_determinant': int(jac.det()),
    'hull_relation': str(quartic),
    'basis_over_W_t_u_v': ['1','s','s^2','s^3'],
    'special_at_2_t_zero': str(special),
    'special_length': 4,
    'runtime_seconds': round(time.perf_counter()-started,6),
    'scope': 'Finite symbolic identities only; geometric and formal-moduli arguments are in the proof.'
}
dest = Path(__file__).with_name('check_igusa_supersingular_output.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
