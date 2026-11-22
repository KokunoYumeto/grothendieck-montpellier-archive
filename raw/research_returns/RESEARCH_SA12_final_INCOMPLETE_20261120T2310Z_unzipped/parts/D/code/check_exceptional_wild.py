"""Exact finite and rational-identity checks for D:fixed-vs-valuation."""
from pathlib import Path
import itertools, json, time
import sympy as sp

started = time.monotonic()
x, y, t, a, b = sp.symbols("x y t a b")

def zero_mod2(expression, variables):
    numerator = sp.together(expression).as_numer_denom()[0]
    return sp.Poly(numerator, *variables, modulus=2).is_zero

def change(expression, variables, images):
    return expression.subs(dict(zip(variables, images)), simultaneous=True)

sigma_x = x / (1+x)
sigma_t = t*(1+x)/(1+x*t)
assert zero_mod2(change(sigma_x, (x,t), (sigma_x,sigma_t))-x, (x,t))
assert zero_mod2(change(sigma_t, (x,t), (sigma_x,sigma_t))-t, (x,t))
assert sigma_t.subs(x,0)==t

v=x*t/(1+t)
u=x*x/(1+x)
assert zero_mod2(change(v, (x,t), (sigma_x,sigma_t))-v, (x,t))
assert zero_mod2(change(u, (x,t), (sigma_x,sigma_t))-u, (x,t))
z=sp.cancel(u/v**2)
residue=sp.cancel(z.subs(x,0))
assert zero_mod2(residue-(1+t**2)/t**2, (t,))
assert zero_mod2(sp.diff(residue,t), (t,))
assert zero_mod2((a+1)+(b+1)-(a+b), (a,b))
assert zero_mod2((a+1)**2+(a+1)-(a*a+a), (a,))

# P1(F2): None denotes infinity.  Nontrivial translation fixes only infinity.
P1=[0,1,None]
translate=lambda q: None if q is None else (q+1)%2
fixed=[(q,r) for q,r in itertools.product(P1,P1)
       if (translate(q),translate(r))==(q,r)]
assert fixed==[(None,None)]
assert all(translate(translate(q))==q for q in P1)

out={
 "characteristic":2,
 "P1_F2_points":P1,
 "diagonal_action_fixed_points":fixed,
 "action_order":2,
 "exceptional_action":{"x":str(sigma_x),"t":str(sigma_t),"residue_action":"identity"},
 "invariants":{"v":str(v),"u":str(u),"z_residue":str(residue)},
 "rational_identity_checks":9,
 "residue_field_extension":"k(t)/k(t^2), purely inseparable degree 2",
 "valuation_ramification_index":1,
 "runtime_seconds":round(time.monotonic()-started,6)
}
(Path(__file__).with_name("check_exceptional_wild_output.json")).write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
