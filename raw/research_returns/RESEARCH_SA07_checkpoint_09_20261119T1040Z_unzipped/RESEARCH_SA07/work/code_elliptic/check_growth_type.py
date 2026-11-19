"""Exact algebraic checks for A.4.30; the lattice lower bound is proved in text."""
import sympy as sp

x, y, l, m, c, r, s, T = sp.symbols("x y l m c r s T", real=True)
u = x + sp.I*y
lam = l + sp.I*m
growth = c * sp.re(sp.conjugate(lam)*u) + c*(l*l+m*m)/2
norm_defect = sp.expand(
    growth - c*((x+l)**2+(y+m)**2)/2 + c*(x*x+y*y)/2
)
assert norm_defect == 0

Q = sp.expand(c*(x*x+y*y) + sp.re((r+sp.I*s)*u*u))
matrix = sp.Matrix([[c+r, -s], [-s, c-r]])
assert sp.expand(Q - (sp.Matrix([[x,y]])*matrix*sp.Matrix([x,y]))[0]) == 0
char = sp.factor((T*sp.eye(2)-matrix).det())
assert sp.expand(char - ((T-c)**2-r*r-s*s)) == 0

print("Reduced norm automorphy exponent defect:", norm_defect)
print("Real quadratic growth matrix:", matrix)
print("Characteristic polynomial:", char)
print("Eigenvalues: c ± sqrt(r^2+s^2), with r+i*s = h-a")
print("Hence maximal quadratic exponent: (c+abs(h-a))/2")
print("A.4.30 lattice covering argument and infinite asymptotic: proved in text.")
