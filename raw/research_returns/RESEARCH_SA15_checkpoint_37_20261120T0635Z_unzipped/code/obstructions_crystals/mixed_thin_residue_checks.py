#!/usr/bin/env python3
"""Universal characteristic-two identities for the mixed thin-strip proof.

This checks the local linear algebra and residue rational identities.
Global pencil cohomology, evaluation isomorphisms and existence are proved
in the companion TeX; no finite sample substitutes for those arguments.
"""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp

started = perf_counter()
a0,a1,b1,b2,mu,lam,x2,y0,g0,g1,g2,omega = sp.symbols(
    "a0 a1 b1 b2 mu lam x2 y0 g0 g1 g2 omega")
variables = (a0,a1,b1,b2,mu,lam,x2,y0,g0,g1,g2,omega)
checks = []

def zero(expr, label):
    numerator, denominator = sp.fraction(sp.cancel(expr))
    assert not sp.Poly(denominator,*variables,modulus=2).is_zero
    assert sp.Poly(numerator,*variables,modulus=2).is_zero, (label,expr)
    checks.append(label)

T=sp.Matrix([
    [a1,mu*b1,a0,0,0,0],
    [0,mu*b2,0,0,a0,0],
    [0,0,0,mu*b2,a1,mu*b1],
])
ka=sp.Matrix([a0,0,a1,0,0,0])
kb=sp.Matrix([0,0,0,b1,0,b2])
for name,vector in [("first pencil",ka),("second pencil",kb)]:
    for i,entry in enumerate(T*vector):
        zero(entry,f"{name} kernel row {i}")
zero(a0*(mu*b2)+mu*b2*a0,"middle exact-sequence kernel")

# Use the exact middle equation, not an assumed independent local value.
middle=a0*x2+mu*b2*y0
zero((g0+mu*b1*y0)/(a0*a1)
     +(g0+b1*middle/b2)/(a0*a1)
     +b1*x2/(b2*a1),
     "A-residue substitution differs by a regular term")
zero((g2+a1*x2)/(mu*b1*b2)
     +(g2+a1*middle/a0)/(mu*b1*b2)
     +a1*y0/(a0*b1),
     "D-residue substitution differs by a regular term")

t=a1*b1/(a0*b2)
u=mu*b1**3/(a0*a1*b2)
v=a1**3/(mu*a0*b1*b2)
shift={b1:b1+lam*b2}
zero(t.subs(shift)+t+lam*a1/a0,
     "t-change is a global differential with poles only at A")
zero(v.subs(shift)+v+
     lam*a1**3/(mu*a0*b1*(b1+lam*b2)),
     "v-change has no b2 denominator and is regular at D")
zero(u.subs(shift)+u+
     lam*mu*b1**2/(a0*a1)+
     lam**2*mu*b1*b2/(a0*a1)+
     lam**3*mu*b2**2/(a0*a1),
     "full cubic variation of u")

# At each reduced A-point this is the nonzero square-evaluation coefficient.
alpha,aa,bb,mm,ww = sp.symbols("alpha aa bb mm ww")
coefficient = mm*ww/(alpha*aa)
assert coefficient != 0

# The two obstruction determinants are computed in characteristic two.
t0,u0,v0,c1,c2,c3 = sp.symbols("t0 u0 v0 c1 c2 c3")
det=sp.Matrix([[t0,u0+lam*c1+lam**2*c2+lam**3*c3],[v0,t0]]).det()
expected=t0**2+v0*(u0+lam*c1+lam**2*c2+lam**3*c3)
assert sp.Poly(det-expected,t0,u0,v0,c1,c2,c3,lam,modulus=2).is_zero
assert sp.Poly(expected,lam).coeff_monomial(lam)==v0*c1
checks.append("determinant has nonzero linear coefficient when v and c1 are nonzero")

out={
    "status":"PASS",
    "scope":"Universal symbolic identities only; global residue duality, all-degree evaluation isomorphisms and the nonempty-open existence proof are in the TeX.",
    "identities":checks,
    "identity_count":len(checks),
    "cartier_matrix":[[str(v) for v in row] for row in T.tolist()],
    "kernel_vectors":[[str(v) for v in ka],[str(v) for v in kb]],
    "obstruction_matrix":[["t","u"],["v","t"]],
    "linear_coefficient_of_shifted_determinant":"v*c1",
    "finite_elliptic_curves_tested":0,
    "elapsed_seconds":perf_counter()-started,
}
destination=Path(__file__).with_suffix(".output.json")
assert not destination.exists(), "Preserve previous output before rerunning"
destination.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
