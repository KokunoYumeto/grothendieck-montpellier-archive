"""Finite polynomial checks for E4.S, characteristic-two cuspidal Igusa family.

These identities check the equations, discriminants, inversion, singular locus,
and cusp normalization. The Picard descent argument is a proof, not a claimed
computer computation of an entire relative Picard scheme.
"""
import json
import time
from pathlib import Path
import sympy as s

started = time.perf_counter()
x, y, z, t, u = s.symbols('x y z t u')
def mod2(f, *v):
    return s.Poly(s.expand(f), *v, modulus=2).as_expr()

F = y*y*z+t*x*y*z+t*y*z*z-x*x*x
g = y+t*x+t*z
assert mod2(F.subs(y,g)-F,x,y,z,t)==0
assert mod2(g.subs(y,g)-y,x,y,z,t)==0
assert mod2(s.diff(F,z).subs({x:0,y:1,z:0}),t)==1
aff=F.subs(z,1)
generic_jac=s.groebner([aff,s.diff(aff,x),s.diff(aff,y)],x,y,
                      domain=s.GF(2).frac_field(t))
assert [q.as_expr() for q in generic_jac.polys]==[1]
special_jac=s.groebner([aff.subs(t,0),s.diff(aff,x).subs(t,0),
                       s.diff(aff,y).subs(t,0)],x,y,modulus=2)
assert set(q.as_expr() for q in special_jac.polys)=={x*x,y*y}
assert mod2(F.subs({t:0,x:u*u,y:u*u*u,z:1}),u)==0

# Integral Weierstrass discriminant formula, reduced modulo two.
b2=t*t; b4=t*t; b6=t*t; b8=0
disc=mod2(-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6,t)
assert disc==t**6+t**4
c4=mod2(b2*b2-24*b4,t)
assert c4==t**4

B=y*y+x*y-x*x*x-1
B_jac=s.groebner([B,s.diff(B,x),s.diff(B,y)],x,y,modulus=2)
assert [q.as_expr() for q in B_jac.polys]==[1]
assert mod2(B.subs({x:0,y:1}),t)==0
assert mod2((y+x).subs({x:0,y:1})-1,t)==0

out={
 'family':'y^2*z+t*x*y*z+t*y*z^2=x^3 over F_2bar[[t]]',
 'discriminant':str(disc), 'c4':str(c4),
 'j':'t^8/(1+t^2)',
 'inversion_preserves_equation':True, 'inversion_squared_is_identity':True,
 'infinity_smooth_derivative':1,
 'generic_affine_jacobian_basis':[str(q.as_expr()) for q in generic_jac.polys],
 'special_affine_jacobian_basis':[str(q.as_expr()) for q in special_jac.polys],
 'special_normalization':{'x':'u^2','y':'u^3','conductor':'(u^2)',
                          'smooth_locus_coordinate':'v=1/u; infinity has v=0'},
 'B_equation':'y^2+x*y=x^3+1',
 'B_affine_jacobian_basis':[str(q.as_expr()) for q in B_jac.polys],
 'B_nonzero_2_torsion_point':[0,1],
 'elapsed_seconds':time.perf_counter()-started,
}
dest=Path(__file__).with_suffix('.output.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
