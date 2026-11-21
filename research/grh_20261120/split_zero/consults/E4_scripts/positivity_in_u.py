"""Rank three: is every f in N[u], u = q + q^-1 (the normalized count of the Gaussian line R = Res P^1 from F_{q^2})?
And are the two cells the split and the inert sheet: lambda_2(v) = lambda_1(v^2)?  (main session, Claude Opus 5.5 at
effort max, 21 Nov 2026 ~19:3x UTC.) Reads e3_constants.json (a8d75352's 132 constants, field f = the bar-invariant
factor in c = +-(v - v^-1)^a f)."""
import os, sys, json
import sympy as sp
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
v, u = sp.symbols("v u")
C = json.load(open(os.path.join(here, "e3_constants.json"), encoding="utf-8"))

def in_u(f):
    """Write a bar-invariant Laurent polynomial in v with even exponents as a polynomial in u = v^2 + v^-2."""
    f = sp.expand(f)
    out = sp.Integer(0)
    while f != 0:
        p = sp.Poly(sp.expand(f * v ** 200), v)
        top = p.degree() - 200
        assert top % 2 == 0 and top >= 0, ("odd or negative top exponent", top)
        k = top // 2
        c = p.LC()
        out += c * u ** k
        f = sp.expand(f - c * (v ** 2 + v ** -2) ** k)
    return sp.Poly(out, u) if out != 0 else sp.Poly(0, u)

bad, forms = 0, {}
for r in C:
    f = sp.sympify(r["f"], locals={"v": v})
    P = in_u(f)
    coeffs = P.all_coeffs()
    if any(c < 0 for c in coeffs):
        bad += 1
        print("NOT in N[u]:", r["b"], r["bp"], r["bpp"], P.as_expr())
    forms[str(P.as_expr())] = forms.get(str(P.as_expr()), 0) + 1
print("constants:", len(C), " f not in N[u]:", bad)
print("distinct f as polynomials in u (count):")
for k, n in sorted(forms.items(), key=lambda x: -x[1])[:12]:
    print("   ", n, "x", k)
D = (v + 1 / v) ** 2
lam1, lam2 = D, (D - 2) ** 2
print("lambda_2(v) == lambda_1(v^2):", sp.simplify(lam2 - lam1.subs(v, v ** 2)) == 0)
six = sp.expand((v**2 + 1 + v**-2) * (v**2 + v**-2) ** 2)
print("six failures' f = [3]_q * u^2, q-coefficients:", sp.Poly(sp.expand(six * v**6), v).all_coeffs()[::2])
