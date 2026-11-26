"""Exact checks for note G7 that are not in the run's certificate, written by the note's writer
(agent a3c8d7ded052a745e, Claude Opus 5.5 at effort max, 25 Nov 2026).

All computations are in characteristic two, over GF(2) with sympy. Run from any folder:
    python -I -B check_g7_writer.py
It prints one line per assertion and a final count; it writes no file.

What it checks:
  1. the weighted blow-up charts of S0: b^2 + t^5 b + a^5 = 0 (weights a:2, b:5, t:1), the comparison surface of
     Corollary C: the t-chart is t^10 (y^2 + y + x^5) and the a,b-chart is rho^10 xi^2 (xi^2 (1 + xi) + tau^5);
  2. the partial derivatives of S0 and of S, which locate their singular points at the origin;
  3. the same two charts for S: b^2 + (t^5 + t^2 a^2) b + a^5 = 0;
  4. the change of monomial coordinates (rho, xi, tau) -> (a, b, t) is unimodular and inverts as stated;
  5. the identity a = c^2 + t^2 c from z^2 + t z = x, c = t z, a = t^2 x;
  6. the identity (I): F(c^2 + t^2 c, t^2 d + c^5, t) = t^4 H(c, d, t), and the deck involution;
  7. the infinity chart of the curve C: y^2 + y = x^5 becomes v^2 + u^3 v = u with u = 1/x, v = y/x^3.
"""
import sys
import sympy as sp

sys.stdout.reconfigure(encoding="utf-8")
a, b, t, x, y, c, d, z, rho, tau, xi, u, v = sp.symbols("a b t x y c d z rho tau xi u v")
n = 0


def zero2(expr, label):
    """Assert that a polynomial (after clearing nothing) vanishes over GF(2)."""
    global n
    p = sp.Poly(sp.expand(expr), *sorted(sp.expand(expr).free_symbols, key=str) or [t], modulus=2)
    assert p.is_zero, (label, p)
    n += 1
    print("ok", n, label)


F0 = b**2 + t**5 * b + a**5
F = b**2 + (t**5 + t**2 * a**2) * b + a**5
H = d**2 + (c**4 + t**3 + t**4 * c**2) * d + t * c**5 + t**2 * c**7 + t**4 * c**6 + t**6 * c**5

# 1. charts of S0
zero2(F0.subs({a: t**2 * x, b: t**5 * y}) - t**10 * (y**2 + y + x**5), "S0 t-chart = t^10 (y^2+y+x^5)")
zero2(F0.subs({a: rho**2 * xi, b: rho**5 * xi**2, t: rho * tau}) - rho**10 * xi**2 * (xi**2 * (1 + xi) + tau**5),
      "S0 a,b-chart = rho^10 xi^2 (xi^2(1+xi)+tau^5)")
zero2(sp.diff(xi**2 * (1 + xi) + tau**5, xi) - xi**2, "S0 a,b-chart: d/dxi = xi^2 (a unit there)")

# 2. partial derivatives
zero2(sp.diff(F0, a) - a**4, "S0: F_a = a^4")
zero2(sp.diff(F0, b) - t**5, "S0: F_b = t^5")
zero2(sp.diff(F0, t) - t**4 * b, "S0: F_t = t^4 b")
zero2(sp.diff(F, a) - a**4, "S: F_a = a^4")
zero2(sp.diff(F, b) - t**2 * (a**2 + t**3), "S: F_b = t^2 (a^2 + t^3)")
zero2(sp.diff(F, t) - t**4 * b, "S: F_t = t^4 b")

# 3. charts of S
zero2(F.subs({a: t**2 * x, b: t**5 * y}) - t**10 * (y**2 + (1 + t * x**2) * y + x**5), "S t-chart (Y0)")
zero2(F.subs({a: rho**2 * xi, b: rho**5 * xi**2, t: rho * tau})
      - rho**10 * xi**2 * (xi**2 * (1 + xi + rho * tau**2) + tau**5), "S a,b-chart (Yinf)")
zero2(sp.diff(y**2 + (1 + t * x**2) * y + x**5, y) - (1 + t * x**2), "S t-chart: d/dy = 1 + t x^2")
zero2(sp.diff(y**2 + (1 + t * x**2) * y + x**5, x) - x**4, "S t-chart: d/dx = x^4")

# 4. monomial coordinates rho = b/a^2, xi = a^5/b^2, tau = t a^2/b
M = sp.Matrix([[-2, 5, 2], [1, -2, -1], [0, 0, 1]])  # exponents of a, b (rows 1-2) and t (row 3) in rho, xi, tau
assert M.det() == -1
n += 1
print("ok", n, "exponent matrix of (rho, xi, tau) is unimodular, det = -1")
r_, x_, t_ = b / a**2, a**5 / b**2, t * a**2 / b
assert sp.simplify(r_**2 * x_ - a) == 0 and sp.simplify(r_**5 * x_**2 - b) == 0 and sp.simplify(r_ * t_ - t) == 0
n += 1
print("ok", n, "a = rho^2 xi, b = rho^5 xi^2, t = rho tau")

# 5. a = c^2 + t^2 c
zero2((t * z)**2 + t**2 * (t * z) - t**2 * (z**2 + t * z), "c = tz: c^2 + t^2 c = t^2 (z^2 + t z)")

# 6. identity (I) and the deck involution
zero2(F.subs({a: c**2 + t**2 * c, b: t**2 * d + c**5}, simultaneous=True) - t**4 * H, "identity (I)")
cs, ds = c + t**2, d + c**4 + t**6 * c + t**8
zero2((cs**2 + t**2 * cs) - (c**2 + t**2 * c), "deck map fixes a")
zero2((t**2 * ds + cs**5) - (t**2 * d + c**5), "deck map fixes b")
zero2(H.subs({c: cs, d: ds}, simultaneous=True) - H, "deck map preserves H")
zero2(cs.subs(c, cs) - c, "deck map: c -> c on applying twice")
zero2(ds.subs({c: cs, d: ds}, simultaneous=True) - d, "deck map: d -> d on applying twice")

# 7. the curve at infinity
zero2(sp.expand((y**2 + y + x**5) / x**6).subs({y: v * x**3}).subs({x: 1 / u}) - (v**2 + u**3 * v + u),
      "y^2+y=x^5 at infinity: v^2 + u^3 v + u")
zero2(sp.diff(v**2 + u**3 * v + u, u) - (1 + u**2 * v), "at infinity: d/du = 1 + u^2 v, a unit at (0,0)")

print("assertions passed:", n)
