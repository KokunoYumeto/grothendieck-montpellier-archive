"""Universal Q8 and residual-quadratic identities; no nodality assertion.

Exact arithmetic over F2(r)[w,beta,t,p,X] modulo the three displayed
Artin--Schreier relations.  The unresolved question is the fibre size
of the resulting degree-seven theta image.
"""
from pathlib import Path
import datetime
import json
import time
from sympy import symbols
from sympy.polys.domains import GF
from sympy.polys.rings import ring

start = time.perf_counter()
rr = symbols("r")
base = GF(2).frac_field(rr)
r = base.gens[0]
R, w, beta, t, p, X = ring("w,beta,t,p,X", base)
z = R.ground_new((r**2 + 1) / r**3)
D = R.ground_new(r**2)
a = z**2
b = z**2 + z + 1
rt = R.ground_new(r)
gt = t**2 + t + D

def mod_t(v):
    return v.div([gt])[1]

ft = mod_t(a*t**5 + b*t**3)
relations = [w**2 + w + ft, beta**2 + beta + z + 1, gt]

def red(v):
    return v.div(relations)[1]

checks = []

def check(name, v):
    answer = red(v)
    assert not answer, (name, str(answer))
    checks.append(name)

u = z*(t + rt)
v = z*t**2 + t + R.ground_new(1/r**2)
F = lambda x: a*x**5 + b*x**3
G = lambda x: z*x**2 + (z+1)*x + beta
H = lambda x: u*x**2 + v*x + w
check("h_quartic_coefficient", u**2 + a*t)
check("h_quadratic_coefficient", v**2 + u + b*t)
check("h_linear_coefficient", v + a*t**4 + b*t**2)
check("h_curve_automorphism", H(p)**2 + H(p) + F(p+t) + F(p))
check("g_curve_automorphism", G(p)**2 + G(p) + F(p+1) + F(p))
check("h_square_is_hyperelliptic", u*t**2 + v*t + 1)
check("g_square_is_hyperelliptic", z + (z+1) + 1)
cg = mod_t(z*t**2 + (z+1)*t)
check("quaternion_commutator", cg + u + v + 1)

d1 = a*p**4 + b*p**2
gp, hp = G(p), H(p)
Z = red(hp + t**2*gp + D*d1 + t*cg)
c = red(D*cg)
E = red(t*gp + hp + (t+1)*cg)
A3 = red((Z*E + c*cg).mul_ground(1/r**2))
A2 = red((Z+c)*gp + c*d1 + A3)
A1 = red(c*d1)
poly = A1*X + A2*X**2 + A3*X**3
check("double_zero_at_P", A1 + c*d1)
check("zero_at_gP", (Z+c)*gp + A1 + A2 + A3)
check("zero_at_hP", (Z*t+c)*hp + A1*t + A2*t**2 + A3*t**3)
check("zero_at_ghP", (Z*(t+1)+c)*(gp+hp+cg)
      + A1*(t+1) + A2*(t+1)**2 + A3*(t+1)**3)
linear = Z*X+c
norm = red(poly**2 + linear*poly + linear**2*(F(p+X)+F(p)))
prescribed = X**2*(X+1)*(X+t)*(X+t+1)
residual_B = red(A3**2 + a*p*Z**2)
residual_C = red((b+a*(D+1))*Z**2 + a*c**2)
residual = a*Z**2*X**2 + residual_B*X + residual_C
check("degree_seven_norm_factorization", norm + prescribed*residual)
U4 = p**4+(D+1)*p**2+D*p
Z0 = red(w+t**2*beta+t*cg)
check("linearized_denominator", Z+a*D*U4+p**2+Z0)
check("denominator_translation_one", Z.compose(p,p+1)+Z+1)
check("denominator_translation_t", Z.compose(p,p+t)+Z+t**2)
global_const = red(a*Z**2*p**2 + residual_B*p + residual_C)
check("global_residual_constant", global_const+p*A3**2
      +(b+a*(D+1))*Z**2+a*c**2)

E0 = red(w+t*beta+(t+1)*cg)
check("residual_linear_coefficient_depends_only_on_Z", E**2+a*D**2*p+Z+E0**2+Z0)

result = {
    "status": "PASS",
    "actual_timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "runtime_seconds": time.perf_counter()-start,
    "coefficient_domain": "F2(r), r nonzero and r!=1",
    "relations": [str(q) for q in relations],
    "parameters": {"z": str(z), "u": str(u), "v": str(v)},
    "checks": checks,
    "Z": str(Z),
    "E": str(E),
    "c": str(c),
    "residual_formula": "a Z^2 X^2+(A3^2+a p Z^2)X+(b+a(D+1))Z^2+a c^2",
    "scope": "Exact Q8 automorphism and interpolation identities only. Rosati norm seven is a separate elementary argument. Theta nodality and degree-seven monodromy are not inferred.",
}
output = Path(__file__).resolve().parent.parent / "outputs/independent_uniform_seven_interpolation.json"
output.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
