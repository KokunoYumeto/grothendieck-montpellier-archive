#!/usr/bin/env python3
"""Exact rational certificate for the explicit Hinich-type plumbing example.

This checks the finite parameter data and residue cancellation. The surface
construction, Kodaira--Spencer pairing, and Serre-duality implication are
proved in sections/A1_plumbing_comparison.tex, not claimed as computational.
"""
from fractions import Fraction as Q
import json
import time

start = time.perf_counter()
R, B, C, eps = Q(3, 2), Q(3, 4), Q(10), Q(1, 100)
A = C * (R - B) * (C - 2 * R) / (C * C - 2 * R * C + R * B)
phi = lambda z: (z - R) ** 2
a, b, c = map(phi, (A, B, C))
roots = [A, 2 * R - A, B, 2 * R - B, C, 2 * R - C]
checks = {}
checks["A_exact"] = A == Q(420, 569)
checks["inner_points"] = 0 < A < 1-eps and 0 < B < 1-eps and A != B
checks["outer_roots"] = all(abs(z) > 1+eps for z in roots if z not in [A, B])
checks["injectivity_bound"] = 2*(1+eps) < 2*R
checks["six_simple_poles"] = len(set(roots)) == 6
checks["three_distinct_finite_marks"] = len({a,b,c}) == 3
checks["no_critical_point_in_coordinate_disc"] = R > 1+eps
def residue(z):
    den = Q(1)
    for other in roots:
        if other != z:
            den *= z - other
    return 4*z*(z-R)**2/den
resA, resB = residue(A), residue(B)
checks["zero_residue_sum"] = resA + resB == 0
t0 = (1-eps)/(1+eps)
checks["valid_nonzero_plumbing_parameter"] = 0 < t0 < 1 and t0 == Q(99,101)
checks["quartic_cancellation_identity"] = (
    A*(A-R)*(B-C)*(B+C-2*R)
    == B*(B-R)*(A-C)*(A+C-2*R))
assert all(checks.values()), checks
output = {
    "kind": "exact rational finite certificate",
    "parameters": {k:str(v) for k,v in
                   dict(R=R,A=A,B=B,C=C,epsilon=eps,t0=t0,a=a,b=b,c=c).items()},
    "poles": list(map(str,roots)),
    "residues": [str(resA),str(resB)],
    "residue_sum": str(resA+resB),
    "checks": checks,
    "check_count": len(checks),
    "seconds": round(time.perf_counter()-start,6),
    "scope_limit": "No numerical or finite computation substitutes for the analytic proof."
}
print(json.dumps(output,indent=2))
