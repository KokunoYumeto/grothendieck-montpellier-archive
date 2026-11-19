#!/usr/bin/env python3
"""Exact certificates for C.3x; finite samples do not prove non-torsion."""
from pathlib import Path
import json
from time import perf_counter
import sympy as sp

started = perf_counter()
base = Path(__file__).resolve().parent
x, y, z = sp.symbols("x y z")
F2 = y**2*z + y*z**2 + x**3
Fodd = y**2*z - x**3 + x*z**2
G = Fodd.subs(z, 1)
certificate = (1-sp.Rational(3,2)*x**2)*sp.diff(G,x) + sp.Rational(9,2)*x*G - sp.Rational(9,4)*x*y*sp.diff(G,y)
assert sp.expand(certificate) == 1
denominators = sorted({int(c.q) for expr in [1-sp.Rational(3,2)*x**2, sp.Rational(9,2)*x, -sp.Rational(9,4)*x*y] for c in sp.Poly(expr,x,y).coeffs()})
assert denominators == [1,2,4]
gradient2 = [sp.Poly(sp.diff(F2,a),x,y,z,modulus=2).as_expr() for a in (x,y,z)]
assert gradient2 == [x**2,z**2,y**2]
assert sp.expand(F2.subs(x,0)-y*z*(y+z)) == 0
assert sp.expand(Fodd.subs(y,0)+x*(x-z)*(x+z)) == 0
assert sp.expand(Fodd.subs(z,0)) == -x**3
assert sp.expand(sp.diff(Fodd,z).subs(z,0)) == y**2

def p2_points(p):
    # Disjoint standard projective charts; first nonzero coordinate is 1.
    return [(1,a,b) for a in range(p) for b in range(p)] + [(0,1,a) for a in range(p)] + [(0,0,1)]

samples=[]
for p in [2,3,5,7,11,13]:
    F=F2 if p==2 else Fodd
    deriv=[sp.diff(F,a) for a in (x,y,z)]
    def val(expr,point):
        return int(expr.subs(dict(zip((x,y,z),point))))%p
    points=[a for a in p2_points(p) if val(F,a)==0]
    singular=[a for a in points if all(val(df,a)==0 for df in deriv)]
    section=[a for a in points if a[0 if p==2 else 1]==0]
    assert not singular
    assert len(section)==3
    samples.append({"p":p,"elliptic_points":len(points),"singular_points":singular,"section_points":section})

result={
 "statement":"C.3x",
 "exact_odd_affine_certificate":str(certificate),
 "certificate_remainder":str(sp.expand(certificate-1)),
 "certificate_denominators":denominators,
 "characteristic_two_gradient":[str(a) for a in gradient2],
 "hyperplane_factors":{"p2":"y*z*(y+z)","odd":"-x*(x-z)*(x+z)"},
 "odd_infinity_equation":"-x^3", "odd_infinity_z_derivative":"y^2",
 "finite_samples":samples,
 "scope":"The polynomial identity is universal away from 2, and the characteristic-2 identities are exact. Finite point enumerations are only independent samples. Infinite-order classes, actual strict-local Picard injection, and the dimension theorem are proved in the text, not inferred from enumerations."
}
result["runtime_seconds"] = perf_counter()-started
out=base/"positive_characteristic_boundary_output.json"
out.write_text(json.dumps(result,indent=2)+"\n")
print("PASS: exact universal odd-characteristic affine smoothness identity; denominators only 2.")
print("PASS: characteristic-2 homogeneous gradient and both distinct-line factorizations.")
for sample in samples:
    print(f"PASS: p={sample['p']}; #E(F_p)={sample['elliptic_points']}; no singular points; three section points {sample['section_points']}.")
print("No finite computation is used to establish the infinite-order Picard class.")
print(f"Runtime seconds: {result['runtime_seconds']:.6f}")
print(f"Wrote {out.name}")
