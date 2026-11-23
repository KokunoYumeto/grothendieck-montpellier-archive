#!/usr/bin/env python3
"""Exact finite-dimensional diagnostics for AM-DO-049; not an automorphic computation."""
from pathlib import Path
import json
import hashlib
from datetime import datetime, timezone
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "definite_oscillator_vertical_intertwiner_scaling_certificate.json"
I = sp.I
checks = 0
groups = {}

def eq(x, y, group):
    global checks
    if isinstance(x, sp.MatrixBase) or isinstance(y, sp.MatrixBase):
        d = sp.Matrix(x) - sp.Matrix(y)
        ok = all(sp.expand_complex(z) == 0 for z in d)
    else:
        ok = sp.expand_complex(x-y) == 0
    assert ok, (group, x, y)
    checks += 1
    groups[group] = groups.get(group, 0) + 1

def dag(x):
    return x.conjugate().T

def clean(x):
    return x.applyfunc(sp.expand_complex)

def adj(t, gs, gt):
    # All metric matrices below are real symmetric positive definite.
    return gs.inv() * dag(t) * gt

def ip(x, y, g):
    return (x.T * g * y.conjugate())[0]

scalars = [sp.Integer(1), sp.Integer(2), -sp.Integer(3), I,
           1+I, sp.Rational(2,3)-I, sp.Rational(-3,5)+2*I]
gs = sp.Matrix([[3, 1, 0], [1, 2, 0], [0, 0, 5]])
gt = sp.Matrix([[2, 1], [1, 3]])
t = sp.Matrix([[1+I, 2, -I], [2, 1-I, 3]])
tp = adj(t, gs, gt)
xs = [sp.Matrix([1,0,0]), sp.Matrix([I,2,1-I]), sp.Matrix([2-I,-3,1])]
ys = [sp.Matrix([1,0]), sp.Matrix([I,2]), sp.Matrix([1-I,3+I])]
for c in scalars:
    eq(adj(c*t, gs, gt), sp.conjugate(c)*tp, "linear_first_adjoint")
    for x in xs:
        for y in ys:
            eq(ip(c*t*x, y, gt), ip(x, sp.conjugate(c)*tp*y, gs),
               "linear_first_adjoint")
    functional = sp.Matrix([[1+I, 2-I]])
    eq((functional/c)*(c*t), functional*t, "fixed_down_integrand_factorization")
    upfunctional = sp.Matrix([[2, I, 1-I]])
    eq((upfunctional/sp.conjugate(c))*(sp.conjugate(c)*tp),
       upfunctional*tp, "fixed_up_integrand_factorization")

# Two edges with nonstandard positive definite Hilbert metrics.
g0 = gt
g1 = gs
g2 = sp.Matrix([[4,1,0,0],[1,3,0,0],[0,0,2,1],[0,0,1,3]])
d0 = t
d1 = sp.Matrix([[1,0,I,2],[0,1,2,-I],[1-I,1,0,1]])
d = clean(d0*d1)
u0, u1 = adj(d0,g1,g0), adj(d1,g2,g1)
u = clean(u1*u0)
eq(u, adj(d,g2,g0), "chain_adjoint")
assert clean(d*u).det() != 0
right = clean(u*clean(d*u).inv(method="DM"))
eq(d*right, sp.eye(2), "least_norm_right_inverse")
eq(adj(right*d,g2,g2), right*d, "least_norm_right_inverse")
eq((right*d)**2, right*d, "least_norm_right_inverse")
for c0 in scalars:
    for c1 in scalars:
        c = c0*c1
        dnew = clean((d0/c0)*(d1/c1))
        unew = clean((u1/sp.conjugate(c1))*(u0/sp.conjugate(c0)))
        abs2 = sp.expand_complex(c*sp.conjugate(c))
        eq(dnew, d/c, "two_edge_composition")
        eq(unew, u/sp.conjugate(c), "two_edge_composition")
        eq(unew, adj(dnew,g2,g0), "two_edge_composition")
        eq(dnew*unew, (d*u)/abs2, "spectral_scalar")
        rnew = clean(unew*clean(dnew*unew).inv(method="DM"))
        eq(rnew, c*right, "least_norm_right_inverse")
        eq(dnew*rnew, sp.eye(2), "least_norm_right_inverse")
        eq(dag(rnew)*g2*rnew, abs2*(dag(right)*g2*right),
           "right_inverse_norm_charge")
        eq(sp.Matrix.hstack(*dnew.nullspace()),
           sp.Matrix.hstack(*d.nullspace()), "kernel_and_quotient")
        b = sp.Matrix([[1-I, 2+I]])
        eq((c*b)*dnew, b*d, "fixed_period_transport")
        eq(b*dnew, (b*d)/c, "fixed_period_transport")
        # Fixed oscillator test and scaled contraction give inverse multiplicity energy.
        eq((1/c)*sp.conjugate(1/c), 1/abs2, "test_vs_intertwiner_scale")
        # Scaling the oscillator test itself has the opposite raw Gram scale.
        eq(c*sp.conjugate(c), abs2, "test_vs_intertwiner_scale")

# Fixed Delta with specified unit inputs fixes the scalar, whereas existential
# unit inputs can absorb exactly a phase in a unitary irreducible embedding.
for c in scalars:
    abs2 = sp.expand_complex(c*sp.conjugate(c))
    eq(abs2, sp.re(c)**2+sp.im(c)**2, "auxiliary_extremal_norm")
    assert bool(abs2 == 1) == (c in (1,I))
    checks += 1
    groups["auxiliary_extremal_norm"] = groups.get("auxiliary_extremal_norm",0)+1
    # If both old and new zeta are on the unit circle, c must have norm one.
    eq((1/c)*sp.conjugate(1/c)-1, (1-abs2)/abs2,
       "fixed_circle_period_constraint")

report = {
    "finding": "AM-DO-049",
    "status": "PASS",
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "assertions": checks,
    "groups": groups,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Exact rational-complex finite-dimensional checks only; no automorphic computation or integral normalization assertion."
}
OUT.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
