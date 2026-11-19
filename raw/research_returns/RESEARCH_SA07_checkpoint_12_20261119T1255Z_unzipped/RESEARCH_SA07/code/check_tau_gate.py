"""Exact symbolic checks for the explicitly non-arithmetic TG-6 construction.

No numerical value is tested for algebraicity and no actual elliptic curve
is attributed to these formal tuples. Inputs are independent indeterminates.
"""
import sympy as S

t, r, s, p, h, pi_symbol = S.symbols("t r s p h pi_symbol", real=True)
z = t + S.I*t**2
u = r + S.I*s
v = p + S.I*h
c = 2*S.I*pi_symbol
w1, w2, eta1, eta2 = u, u*z, v, z*v-c/u

tests = {
    "Legendre residual": S.cancel(eta1*w2-eta2*w1-c),
    "conjugate Legendre residual": S.cancel(S.conjugate(eta1)*S.conjugate(w2)
        -S.conjugate(eta2)*S.conjugate(w1)+c),
    "symmetric ratio relation": S.expand(4*(z-S.conjugate(z))**2
        +(z+S.conjugate(z))**4),
    "recover t": S.expand((z+S.conjugate(z))/2-t),
    "recover r": S.expand((u+S.conjugate(u))/2-r),
    "recover s": S.expand((u-S.conjugate(u))/(2*S.I)-s),
    "recover p": S.expand((v+S.conjugate(v))/2-p),
    "recover h": S.expand((v-S.conjugate(v))/(2*S.I)-h),
}
for title, residual in tests.items():
    print(f"{title}: {residual}")
    assert residual == 0

# A nonconstant rational involution has trace-zero Möbius representative.
a, b, c_mobius, x = S.symbols("a b c_mobius x")
R = (a*x+b)/(c_mobius*x-a)
residual = S.cancel(R.subs(x, R)-x)
print(f"trace-zero Möbius involution residual: {residual}")
assert residual == 0
print("All exact checks passed. The proof of algebraic independence is in TG-6.")
