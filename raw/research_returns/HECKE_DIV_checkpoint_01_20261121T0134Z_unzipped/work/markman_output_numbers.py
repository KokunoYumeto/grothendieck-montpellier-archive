"""Exact arithmetic supporting M9; no geometric theorem is tested by this script."""
from pathlib import Path
import json
import sympy as s

u, v, x, y, p, b, c, e, t = s.symbols("u v x y p b c e t")
coeff = [s.Integer(1), s.Integer(1), s.Integer(-6), s.Integer(-2)]

def apply_input_operator(poly):
    return s.expand(sum(
        coeff[i] * coeff[j] * s.diff(poly, u, i, v, j).subs({u: 0, v: 0})
        for i in range(4) for j in range(4)
    ))

# Relative Gaussian formula, evaluated separately in degrees 0 through 3.
ch = []
for k in range(4):
    raw = s.expand((u + v) ** (3-k) * (u*v*x + v*p - y) ** k / s.factorial(k))
    ch.append(s.expand((-1) ** (k+1) * apply_input_operator(raw)))
r = ch[0]
D = ch[1]
kappa2 = s.factor(ch[2] - D**2/(2*r))
kappa3 = s.factor(ch[3] - D*ch[2]/r + D**3/(3*r**2))
assert r == 96
assert s.expand(D - (264*x + 22*y - 48*p)) == 0
assert s.expand(kappa2 + s.Rational(169,48)*(12*x+y)**2) == 0

# The product-principal intersection polynomial is det([[b,e],[e,c]])^3.
base_det = (b*c-e**2)**3
def integrate(poly):
    out = s.Integer(0)
    for powers, val in s.Poly(s.expand(poly), x, y, p).terms():
        assert sum(powers) == 6
        out += val * s.diff(base_det, b, powers[0], c, powers[1], e, powers[2]).subs(
            {b: 0, c: 0, e: 0}
        )
    return s.factor(out)

# Independent absolute GRR determinant; compare its top four homogeneous terms.
total_matrix = s.Matrix([[u+v, v, -1], [v, v+b, e], [-1, e, c]])
Ghilb = apply_input_operator(s.expand(total_matrix.det()**3))
Ehilb = s.expand(-Ghilb.subs({b: -b, c: -c, e: -e}, simultaneous=True))
for k in range(4):
    expected = integrate(ch[k]*(b*x+c*y+e*p)**(6-k))/s.factorial(6-k)
    actual = sum(val*s.prod(z**a for z, a in zip((b,c,e), powers))
                 for powers, val in s.Poly(Ehilb,b,c,e).terms() if sum(powers)==6-k)
    assert s.expand(expected-actual)==0

h = 36*x + 3*y
Hmatrix = s.diag(3,3)
hmatrix = s.diag(36,3)
Dmatrix = s.Matrix([[264,-48],[-48,22]])
c_compare, C_compare = 2, 12
comparisons = [c_compare*hmatrix-Hmatrix, C_compare*hmatrix-Dmatrix]
for mat in comparisons:
    assert mat[0,0]>0 and mat.det()>0

R = 112*r*r*c_compare+r*C_compare+6
h6 = integrate(h**6)
h4c2 = -r**4*integrate(h**4*kappa2)
h3c3 = 2*r**6*integrate(h**3*kappa3)
delta_h = h6/s.factorial(6)
assert h6==906992640 and delta_h==108**3
assert h4c2==30136419515105280
assert h3c3==28288052451512156160
Dminus = (r-2)*R*h4c2 + (r*(r-1)*(r-2)//2)*R**3*h6
Dplus = Dminus+h3c3
assert R==2065542
assert Dplus==3426088289770714707027306735206400
assert Dminus==3426088289770686418974855223050240

result = {
    "run": "HECKE_DIV_20261121",
    "date": "2026-11-21",
    "scope": "Exact polynomial and integer arithmetic only; geometric proofs are in markman_output_regularity.md.",
    "rank": int(r),
    "ch_0_to_3": [str(z) for z in ch],
    "kappa2": str(kappa2),
    "kappa3": str(kappa3),
    "determinant_matrix": [[int(a) for a in row] for row in Dmatrix.tolist()],
    "h_matrix": [[int(a) for a in row] for row in hmatrix.tolist()],
    "comparison_c": c_compare,
    "comparison_C": C_compare,
    "comparison_matrices": [[[int(a) for a in row] for row in mat.tolist()] for mat in comparisons],
    "comparison_leading_minors": [[int(mat[0,0]),int(mat.det())] for mat in comparisons],
    "normalized_regularity": int(R),
    "h_six": int(h6),
    "polarization_delta": int(delta_h),
    "h_four_c2_normalized": int(h4c2),
    "h_three_c3_normalized": int(h3c3),
    "positive_cycle_degree": int(Dplus),
    "negative_cycle_degree": int(Dminus),
    "D6_source": int(max(Dplus,Dminus)),
    "absolute_and_relative_GRR_agree_in_degrees_0_to_3": True,
    "all_arithmetic_assertions_passed": True,
}
path=Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:result[k] for k in ["rank","normalized_regularity","h_six","D6_source","all_arithmetic_assertions_passed"]},indent=2))
