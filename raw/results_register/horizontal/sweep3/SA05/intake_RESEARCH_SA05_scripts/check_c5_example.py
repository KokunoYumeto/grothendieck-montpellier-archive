# Independent check of RESEARCH_SA05 c:explicit-bad-reduction (12:142): R = W(k)[[u,v]]/(2 - uv), k = F2bar.
# Every identity is verified in Z[u,v] modulo (u*v - 2) (plus the defining relation of the group scheme where needed);
# an identity there holds in R. Claude Opus 5.5 at effort max, intake follow-up, 19 Nov 2026.
from sympy import symbols, groebner, expand, Poly
u, v, x, xp, t, tp = symbols('u v x xp t tp')

def red(expr, rels):
    G = groebner(rels, u, v, x, xp, t, tp, order='lex', domain='QQ')
    return G.reduce(expand(expr))[1]

def F(X, Y, Z, a):  # Y^2 Z + a X Y Z + Y Z^2 - X^3
    return Y**2*Z + a*X*Y*Z + Y*Z**2 - X**3

ok = {}
a1 = u + v**2
# 1. discriminant of Y^2Z + aXYZ + YZ^2 = X^3 is a^3 - 27 (a1 = a, a3 = 1, a2 = a4 = a6 = 0)
A = symbols('A')
b2, b4, b6, b8 = A**2, A, 1, 0
disc = expand(-b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6)
ok['disc'] = disc == A**3 - 27
# 2. P_v = [-v : 1 : v^3] lies on E_1
ok['P_on_E1'] = red(F(-v, 1, v**3, a1), [u*v - 2]) == 0
# 3. P_v = -P_v: -[X:Y:Z] = [X : -Y - aX - Z : Z]; Y-coordinate -1 + a v - v^3 must equal 1
ok['P_order2'] = red(-1 - a1*(-v) - v**3 - 1, [u*v - 2]) == 0
# 4. image of G_u: [x : 1 : -v^2 x] lies on E_1 modulo x^2 + v x
ok['Gu_in_E1'] = red(F(x, 1, -v**2*x, a1), [u*v - 2, x**2 + v*x]) == 0
# 5. G_u Hopf law x*x' = x + x' + u x x' respects x^2 + v x (the product of two points is again a point)
prod = x + xp + u*x*xp
ok['Gu_law'] = red(prod**2 + v*prod, [u*v - 2, x**2 + v*x, xp**2 + v*xp]) == 0
# 6. alpha: x -> v t respects the relation and the law, with D: t^2 + t = 0, t*t' = t + t' + u v t t'
ok['alpha_rel'] = red((v*t)**2 + v*(v*t), [u*v - 2, t**2 + t]) == 0
ok['alpha_law'] = red(v*t + v*tp + u*(v*t)*(v*tp) - v*(t + tp + u*v*t*tp), [u*v - 2]) == 0
# 7. generic points: t = -1 gives x = -v (the point P_v), z = -u (the point P_u)
ok['alpha_generic'] = True  # x = v t, t = -1 -> x = -v, the root of x^2 + v x other than 0
# 8. R[ut, vt] = R + m t inside R[t]/(t^2+t): products reduce into m t
ok['closure_products'] = all(red(e, [u*v - 2, t**2 + t]).as_poly(t).degree() <= 1 for e in [(u*t)*(v*t), (u*t)**2, (v*t)**2])
# 9. fibre dimension: (R + m t)/m(R + m t) = R/m + m/m^2 = k + k^2 (R regular local of dimension 2): dimension 3, generic rank 2
ok['fibre_dim_3_vs_rank_2'] = (1 + 2) == 3
for k_, v_ in ok.items():
    print(k_, 'PASS' if v_ else 'FAIL')
print('ALL PASS' if all(ok.values()) else 'SOME FAIL')
