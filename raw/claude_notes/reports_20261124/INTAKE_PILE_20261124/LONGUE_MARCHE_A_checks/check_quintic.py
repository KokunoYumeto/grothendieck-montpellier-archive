# FERMAT_SUCCESSOR A.53: three maps X5 -> C: v^2+v=u^5 and the six pulled-back differentials, chart Z=1, X^5+Y^5+1=0
import sympy as sp
X, Y = sp.symbols('X Y')
Z = 1
rel = X**5 + Y**5 + 1
def red(e):
    # reduce a rational function modulo the curve: substitute Y^5 -> -1-X^5 in numerator and denominator
    e = sp.together(sp.expand(e))
    n, d = sp.fraction(e)
    n = sp.rem(sp.expand(n), rel, Y); d = sp.rem(sp.expand(d), rel, Y)
    return sp.simplify(n / d)
maps = [(-X*Y/Z**2, X**5/Z**5), (-Y*Z/X**2, Y**5/X**5), (-Z*X/Y**2, Z**5/Y**5)]
dYdX = -X**4 / Y**4
omega_coeff = lambda expr_dX: sp.simplify(expr_dX * Y**4)  # coefficient c with  expr dX = c * dX/Y^4
for i, (u, v) in enumerate(maps, 1):
    curve = red(v**2 + v - u**5)
    du = sp.diff(u, X) + sp.diff(u, Y) * dYdX           # du/dX on the curve
    w1 = red(omega_coeff(du / (2*v + 1)))
    w2 = red(omega_coeff(u * du / (2*v + 1)))
    print(f'f{i}: curve identity residue = {curve};  pullbacks: {sp.factor(w1)} , {sp.factor(w2)}')
