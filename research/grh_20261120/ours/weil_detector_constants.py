"""Constants for Theorem W (detector-degree reduction for Weil classes) and checks of GHOSTS D0, D6.
Claude Opus 5.5 at effort high, 21 Nov 2026. Exact integer/sympy arithmetic.
For K imaginary quadratic, a in O_K with a/abar not a root of unity, n>=1:
  f(t)=(t-a^{2n})(t-abar^{2n}),  g(t)=prod_{j=1}^{2n-1}(t-a^j abar^{2n-j}),  R=Res(f,g),
  u f + v g = R with u,v in Z[t] (adjugate of Sylvester matrix), P(t)=v(t)g(t)=sum c_j t^j,
  kappa = sum_j |c_j| Nm(a)^{j n},
  C(delta,T) = delta*Nm^{2n}*max(R^4/(n!)^4, 4*sqrt(T)*kappa*R^3/(n!)^3).
"""
import sympy as sp
from math import factorial
t=sp.symbols('t')
def constants(name, a, n):
    ab=sp.conjugate(a); Nm=sp.expand(a*ab)
    f=sp.expand((t-a**(2*n))*(t-ab**(2*n)))
    g=sp.expand(sp.prod([t-a**j*ab**(2*n-j) for j in range(1,2*n)]))
    f=sp.Poly(sp.nsimplify(sp.expand(f)),t); g=sp.Poly(sp.nsimplify(sp.expand(g)),t)
    assert all(c.is_integer for c in f.all_coeffs()+g.all_coeffs())
    R=sp.resultant(f.as_expr(),g.as_expr(),t)
    # integral Bezout: solve u f + v g = R with deg u < deg g, deg v < deg f via Sylvester adjugate
    s,r_=sp.gcdex(f.as_expr(),g.as_expr(),t)[:2]  # rational s f + r g = 1
    u=sp.Poly(sp.expand(s*R),t); v=sp.Poly(sp.expand(r_*R),t)
    assert all(sp.Rational(c).q==1 for c in u.all_coeffs()+v.all_coeffs()), "Bezout not integral"
    P=sp.Poly(sp.expand(v.as_expr()*g.as_expr()),t)
    coeffs=P.all_coeffs()[::-1]
    kappa=sum(abs(c)*Nm**(j*n) for j,c in enumerate(coeffs))
    # projector check on eigenvalues
    lam=[sp.expand(a**j*ab**(2*n-j)) for j in range(2*n+1)]
    vals=[sp.simplify(P.as_expr().subs(t,l)/R) for l in lam]
    assert vals[0]==1 and vals[-1]==1 and all(x==0 for x in vals[1:-1])
    print(f"{name}: n={n}, a={a}, Nm={Nm}, |R|={abs(R)} = {sp.factorint(abs(R))}, kappa={kappa}")
    nf=factorial(n)
    A1=sp.Rational(abs(R)**4, nf**4); A2=sp.Rational(4*kappa*abs(R)**3, nf**3)
    print(f"   C(delta,T) = delta * {Nm**(2*n)} * max({A1}, {A2} * sqrt(T))")
    return R,kappa
w=sp.Rational(-1,2)+sp.sqrt(3)*sp.I/2
I=sp.I
for n in (2,3,4):
    constants("Q(omega)", 3+w, n)
    constants("Q(i)", 2+I, n)
# GHOSTS R12 and R20-R24 Bezout constants
D0=sp.Rational(3**4*sp.factorial(7)//sp.factorial(3) * 3**4*216, 9)
print("D0 =", D0, "(68040*17496/9)", 3**4*sp.factorial(7)//sp.factorial(3), 3**4*216)
deg_W6=3**6*sp.factorial(10)/sp.factorial(4); deg_T0=3**6*(sp.factorial(6)*27)
print("D6 check:", deg_W6, deg_T0, deg_W6*deg_T0/27)
print("C4 for delta=1,T=6 (t0 of GHOSTS):", 531441*D0**4*(1+4*sp.ceiling(sp.sqrt(6))))
