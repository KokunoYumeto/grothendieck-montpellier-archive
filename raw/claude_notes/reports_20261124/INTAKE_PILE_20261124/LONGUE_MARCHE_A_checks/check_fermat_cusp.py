import sympy as sp
t, lam = sp.symbols('t lam')
# Legendre j-invariant and q-expansion inverse: q = 1/j + 744/j^2 + ...
j = 256*(lam**2 - lam + 1)**3/(lam**2*(1 - lam)**2)
for n in (3, 5, 7):
    jt = sp.simplify(j.subs(lam, -t**n))
    inv = sp.series(1/jt, t, 0, 2*n + n + 1).removeO()
    lead = sp.Poly(sp.expand(inv), t).terms()[-1]
    print('n', n, 'lowest term of 1/j:', sp.factor(sp.expand(inv)).as_leading_term(t) if False else min(sp.Poly(sp.expand(inv), t).terms(), key=lambda m: m[0][0]))
    # 1/j = 256^-1 t^{2n} (1 + O(t^n)) ? check ratio
    ratio = sp.series(sp.expand(inv)/(t**(2*n)/256), t, 0, n + 1).removeO()
    print('   ratio 256 t^{-2n}/j up to t^n:', sp.expand(ratio))
print('v_2(1/256) =', sp.multiplicity(2, 256) * -1)
# Y1(7) example: y^2 - x y - 4 y = x^3 - 4 x^2 : a1=-1, a2=-4, a3=-4, a4=0, a6=0
a1, a2, a3, a4, a6 = -1, -4, -4, 0, 0
b2 = a1**2 + 4*a2; b4 = 2*a4 + a1*a3; b6 = a3**2 + 4*a6
b8 = a1**2*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3**2 - a4**2
disc = -b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
print('discriminant', disc, sp.factorint(disc))
# group law on the curve with rational arithmetic, check (0,0) has exact order 7
from fractions import Fraction as Fr
def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and y1 + y2 + a1*x2 + a3 == 0: return None
    if x1 == x2:
        l = (3*x1**2 + 2*a2*x1 + a4 - a1*y1)/(2*y1 + a1*x1 + a3)
    else:
        l = (y2 - y1)/(x2 - x1)
    nu = y1 - l*x1
    x3 = l**2 + a1*l - a2 - x1 - x2
    y3 = -(l + a1)*x3 - nu - a3
    return (x3, y3)
P = (Fr(0), Fr(0)); Q = None
for k in range(1, 8):
    Q = add(Q, P); print(k, Q)
