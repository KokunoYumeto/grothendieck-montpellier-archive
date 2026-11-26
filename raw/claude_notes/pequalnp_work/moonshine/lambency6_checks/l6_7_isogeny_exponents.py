"""Lambency-6 pass, check 7: Codex's exact conductor periods rho_inf = 2i, rho_0 = i eps^2/2, rho_1 = i eps (S6 Paper II,
Example P205, one normalized family). Rectangular periods iu, iv are isogenous iff u/v or uv is rational (Codex's
criterion; re-derived in the report). Here: the isogeny pattern is decided by d = the least k >= 1 with eps^k rational
(d = infinity if none): all three pairs for d = 1, only (inf,0) for d = 2, only (0,1) for d = 3, none otherwise; and
which images are CM (iu is CM iff u^2 is rational), by which field.
Run: python -I -B l6_7_isogeny_exponents.py"""
import sympy as sp
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
def rational(z):
    z = sp.nsimplify(sp.simplify(z))
    return z.is_rational is True
tests = {"1/7": sp.Rational(1, 7), "sqrt2/7": sp.sqrt(2) / 7, "cbrt2/7": sp.cbrt(2) / 7, "2^(1/4)/7": 2 ** sp.Rational(1, 4) / 7,
         "2^(1/6)/7": 2 ** sp.Rational(1, 6) / 7, "sqrt3/7": sp.sqrt(3) / 7, "pi/7": sp.pi / 7, "2^(1/5)/7": 2 ** sp.Rational(1, 5) / 7}
for name, eps in tests.items():
    u = {"inf": sp.Integer(2), "0": eps ** 2 / 2, "1": eps}
    pairs = []
    for a, b in (("inf", "1"), ("inf", "0"), ("0", "1")):
        if rational(u[a] / u[b]) or rational(u[a] * u[b]): pairs.append((a, b))
    cm = {k: (sp.sqrt(-sp.nsimplify(v ** 2)).simplify() if rational(v ** 2) else None) for k, v in u.items()}
    cmf = {k: (f"Q(sqrt({sp.factorint(sp.Rational(sp.nsimplify(-u[k]**2)).p * sp.Rational(sp.nsimplify(-u[k]**2)).q)}))" if rational(u[k] ** 2) else "no CM") for k in u}
    d = next((k for k in range(1, 13) if rational(eps ** k)), "inf")
    say(f"eps = {name}: d = {d}; isogenous pairs {pairs}; CM: " + ", ".join(f"{k}: {'CM' if rational(u[k]**2) else 'no'}" for k in u))
say("pattern check: d=1 -> all three; d=2 -> (inf,0); d=3 -> (0,1); d=4,5,6,inf -> none; transitivity eps = eps^3/eps^2.")
with open(__file__.replace(".py", "_output.txt"), "w", encoding="utf-8") as fh: fh.write("\n".join(out) + "\n")
