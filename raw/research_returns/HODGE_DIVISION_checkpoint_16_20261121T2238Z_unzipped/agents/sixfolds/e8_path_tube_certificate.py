#!/usr/bin/env python3
"""Independent exact tube certificate for the E8 ODE integration paths.

NumPy chooses the same dyadic polygon vertices as verify_M.py.  Every
subsequent geometric statement is verified with fractions.Fraction.
This checks the actual rounded adaptive polyline, not only its endpoints
or its winding vector.  No monodromy or period-rank assertion is computed.
"""
from pathlib import Path
from fractions import Fraction as Q
import json
import numpy as np

OUT = Path(__file__).resolve().with_name("e8_path_tube_certificate_output.json")
zbase = .5 - 1j
poles = [0., 1., 2. + 1j]
eps = Q(1, 10**12)

def pair(z):
    return (Q(float(z.real)), Q(float(z.imag)))

def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))

def add(a, b):
    return tuple(x+y for x, y in zip(a, b))

def norm2(a):
    return sum(x*x for x in a)

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def segment_distance2(p, a, b):
    v = sub(b, a)
    if norm2(v) == 0:
        return norm2(sub(p, a))
    u = dot(sub(p, a), v) / norm2(v)
    u = max(Q(0), min(Q(1), u))
    return norm2(sub(p, add(a, tuple(u*x for x in v))))

def loop_path(p):
    phi = np.angle(zbase-p)
    return [zbase] + [p + .45*np.exp(1j*(phi+2*np.pi*k/12))
                     for k in range(13)] + [zbase]

max_vertex_distance2 = Q(0)
min_pole_distance2 = None
max_bits = 0
counts = []
for p in poles:
    path = loop_path(p)
    path_steps = 0
    for z1, z2 in zip(path[:-1], path[1:]):
        a, b = pair(z1), pair(z2)
        for pole in poles:
            ds = segment_distance2(pair(pole), a, b)
            assert ds > Q(1, 100), "intended segment too near a pole"
            min_pole_distance2 = ds if min_pole_distance2 is None else min(min_pole_distance2, ds)
        za = a
        while True:
            zc = complex(float(za[0]), float(za[1]))
            rem = complex(z2)-zc
            if abs(rem) < 1e-300:
                assert za == b, "rounded endpoint discrepancy"
                break
            dmin = min(abs(zc-q) for q in poles)
            final = abs(rem) <= .35*dmin
            if final:
                h = sub(b, za)
            else:
                hc = rem/abs(rem)*.35*dmin
                h = pair(complex(round(hc.real*2**50)/2**50,
                                 round(hc.imag*2**50)/2**50))
            assert norm2(h) < min(norm2(sub(za,pair(q))) for q in poles)/4
            za = add(za,h)
            path_steps += 1
            ds = segment_distance2(za,a,b)
            assert ds < eps**2
            max_vertex_distance2 = max(max_vertex_distance2,ds)
            for v in za+h:
                assert v.denominator & (v.denominator-1) == 0
                max_bits = max(max_bits,abs(v.numerator).bit_length())
            if final:
                assert za == b
                break
    counts.append(path_steps)
assert counts == [31,31,53]
assert max_bits < 256
out = {
    "status": "PASS",
    "scope": "exact rational adaptive-polyline homotopy to the intended three polygonal loops",
    "step_counts": counts,
    "tube_radius": str(eps),
    "intended_segment_to_every_pole_distance_lower_bound": "1/10",
    "maximum_vertex_distance_squared": str(max_vertex_distance2),
    "minimum_segment_pole_distance_squared": str(min_pole_distance2),
    "maximum_dyadic_numerator_bits": max_bits,
    "homotopy_argument": "The closed eps-tube of a line segment is convex. All adaptive vertices and segments lie in it, and it contains no pole. Thus the actual and intended paths are homotopic relative endpoints in this tube."
}
OUT.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:out[k] for k in ["status","step_counts","tube_radius","intended_segment_to_every_pole_distance_lower_bound","maximum_dyadic_numerator_bits"]}))

