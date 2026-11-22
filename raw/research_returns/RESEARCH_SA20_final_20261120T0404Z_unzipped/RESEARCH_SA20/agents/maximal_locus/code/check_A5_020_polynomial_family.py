#!/usr/bin/env python3
"""Exact symbolic checks for A5.020, not a substitute for its topology proof.

AI-produced by GPT-6 Astra, OpenAI, 20 November 2026.
The proof of image-boundary recognition and rotation conjugacy is in the TeX.
This program checks polynomial identities, the degree, and two extremum
identities used in that proof. No floating-point arithmetic is used.
"""
import json
import time
import sympy as sp

started = time.perf_counter()
x, y, z, m = sp.symbols("x y z m", real=True)
Y = x*x + y*y - 1
A = x*Y - 2*y*z
B = (x+m*y)*Y - 2*(y-m*x)*z
X = A*A*B*B
reflection = {y: -y, z: -z}
checks = []

def identity(name, expression):
    residual = sp.expand(expression)
    checks.append({"name": name, "pass": residual == 0,
                   "exact_residual": str(residual)})

identity("source_reflection_preserves_Y", Y.subs(reflection, simultaneous=True)-Y)
identity("source_reflection_preserves_A", A.subs(reflection, simultaneous=True)-A)
identity("source_reflection_changes_m_to_minus_m_in_B",
         B.subs(reflection, simultaneous=True)-B.subs(m, -m))
identity("source_and_target_reflections_match_first_output",
         X.subs(reflection, simultaneous=True)-X.subs(m, -m))
identity("target_reflection_restores_third_output",
         -z.subs(reflection, simultaneous=True)-z)
identity("properness_radius_identity", x*x+y*y-(1+Y))
poly = sp.Poly(X, x, y, z)
checks.append({"name":"degree_is_twelve", "pass":poly.total_degree()==12,
               "exact_degree":poly.total_degree()})
checks.append({"name":"x_to_twelfth_coefficient_is_one",
               "pass":sp.expand(poly.coeff_monomial(x**12)-1)==0,
               "exact_coefficient":str(poly.coeff_monomial(x**12))})
leading = sum(coeff * x**powers[0] * y**powers[1] * z**powers[2]
              for powers, coeff in poly.terms() if sum(powers)==12)
identity("degree_twelve_homogeneous_part",
         leading-x*x*(x+m*y)**2*(x*x+y*y)**4)
c, s, d, v = sp.symbols("c s d v", real=True)
identity("trigonometric_product_reduced_mod_unit_circle",
         2*c*(c+m*s)-(1+c*c-s*s+2*m*c*s)-(c*c+s*s-1))
identity("maximum_square_gap_factorization",
         (1+d)**2-(1+d*v)**2-d*(1-v)*(2+d*(1+v)))
identity("positive_maximum_exceeds_negative_endpoint_square",
         (1+d)**2-(1-d)**2-4*d)
identity("zero_lines_have_nonzero_determinant_for_m_positive",
         sp.Matrix([[1,0],[1,m]]).det()-m)
report = {
    "result": "A5.020",
    "status": "PASS" if all(item["pass"] for item in checks) else "FAIL",
    "exact_checks": len(checks),
    "runtime_seconds": time.perf_counter()-started,
    "scope": "Exact algebra only; topological inequivalence is proved in the authored TeX.",
    "checks": checks,
}
print(json.dumps(report, indent=2))
if report["status"] != "PASS":
    raise SystemExit(1)
