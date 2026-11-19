"""Exact exterior-algebra certificate for an Orlov-transform surface-cycle lead.

This is a calculation for a restricted construction, not a calculation of the
full algebraic-cycle lattice.  A has polarization type (1,e).  We compute
  integral_z v(x+z) w(z) exp(-P(z,y))
for the nine even algebraic cohomology basis tensors 1,theta,point.
The inverse Fourier transform has this sign in dimension two; changing y to
-y only changes the sign of the displayed P coefficient.
"""
from itertools import combinations
import sympy as s

e = s.symbols("e", positive=True, integer=True)

def add(*terms):
    out = {}
    for term in terms:
        for key, value in term.items():
            out[key] = s.expand(out.get(key, 0) + value)
    return {key: val for key, val in out.items() if val != 0}

def scale(a, term):
    return {key: s.expand(a * val) for key, val in term.items() if a * val != 0}

def mul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            if set(ka) & set(kb):
                continue
            inv = sum(i > j for i in ka for j in kb)
            key = tuple(sorted(ka + kb))
            out[key] = s.expand(out.get(key, 0) + (-1) ** inv * va * vb)
    return {key: val for key, val in out.items() if val != 0}

def power(a, n):
    ans = {(): s.Integer(1)}
    for _ in range(n):
        ans = mul(ans, a)
    return ans

def wedge(*a):
    ans = {(): s.Integer(1)}
    for item in a:
        ans = mul(ans, item)
    return ans

def degree(a, n):
    return {key: val for key, val in a.items() if len(key) == n}

def integrate_z(a):
    # Variable order x0..x3,z0..z3,y0..y3.  Move z to the end before integrating.
    out = {}
    for key, val in a.items():
        if not all(i in key for i in range(4, 8)):
            continue
        others = tuple(i for i in key if i not in range(4, 8))
        inv = sum(i in range(4, 8) and j >= 8 for i in key for j in key if i < j)
        out[others] = s.expand(out.get(others, 0) + (-1) ** inv * val)
    return {key: val for key, val in out.items() if val != 0}

def coords(a, basis, deg):
    keys = list(combinations(tuple(range(4)) + tuple(range(8, 12)), deg))
    matrix = s.Matrix([[b.get(key, 0) for b in basis] for key in keys])
    vector = s.Matrix([a.get(key, 0) for key in keys])
    ans, params = matrix.gauss_jordan_solve(vector)
    assert params.rows == 0
    assert matrix * ans == vector
    return [s.factor(c) for c in ans]

one = {(): s.Integer(1)}
xs = [{(i,): s.Integer(1)} for i in range(4)]
zs = [{(i,): s.Integer(1)} for i in range(4, 8)]
ys = [{(i,): s.Integer(1)} for i in range(8, 12)]
us = [add(x, z) for x, z in zip(xs, zs)]

def theta(v):
    return add(wedge(v[0], v[1]), scale(e, wedge(v[2], v[3])))

thx, thz, thu = theta(xs), theta(zs), theta(us)
ptz, ptu = wedge(*zs), wedge(*us)
# Dual theta is chosen so FT(theta) = -theta_dual.
thy = add(scale(e, wedge(ys[0], ys[1])), wedge(ys[2], ys[3]))
pzy = add(*(wedge(z, y) for z, y in zip(zs, ys)))
pxy = add(*(wedge(x, y) for x, y in zip(xs, ys)))
kernel = add(*(scale(s.Rational((-1)**j, s.factorial(j)), power(pzy, j))
               for j in range(5)))

basis1 = [thx, pxy, thy]
basis2 = [scale(s.Rational(1,2), power(thx,2)), mul(thx,pxy),
          mul(thx,thy), scale(s.Rational(1,2), power(pxy,2)),
          mul(pxy,thy), scale(s.Rational(1,2), power(thy,2))]
input_left = [one, thu, ptu]
input_right = [one, thz, ptz]
labels = ["1", "theta", "point"]

print("basis(ch1) = [D,P,Dhat]")
print("basis(ch2) = [D^2/2,D*P,D*Dhat,P^2/2,P*Dhat,Dhat^2/2]")
print("left,right,rank,ch1,ch2,c2_P2_over_2")
rows = []
for i, v in enumerate(input_left):
    for j, w in enumerate(input_right):
        ans = integrate_z(wedge(v, w, kernel))
        rank = ans.get((), 0)
        c1 = coords(degree(ans, 2), basis1, 2)
        ch2 = coords(degree(ans, 4), basis2, 4)
        c2coef = s.factor(c1[1]**2 - ch2[3])
        rows.append((i, j, rank, c1, ch2, c2coef))
        print(labels[i], labels[j], rank, c1, ch2, c2coef, sep=" | ")

# The parity condition on this additive K-lattice is ch2[P^2/2] == c1[P] mod2.
test_d = s.Symbol("d", integer=True)
for i, j, rank, c1, ch2, c2coef in rows:
    diff_even = s.Poly(s.expand((ch2[3] - c1[1]).subs(e, 2*test_d)), test_d)
    assert all(int(c) % 2 == 0 for c in diff_even.coeffs())
    even_c2 = s.Poly(s.expand(c2coef.subs(e, 2*test_d)), test_d)
    assert all(int(c) % 2 == 0 for c in even_c2.coeffs())
print("PASS: for even e, every basis transform has even c2 coefficient at P^2/2.")
print("PASS: the additive parity identity q=b mod2 extends to every integral")
print("linear combination, because b^2=b mod2.  It is also preserved by tensor")
print("products, since b(EF)=r(E)b(F)+r(F)b(E) and q(EF) has the same expression")
print("mod2 (the P*P cross term contributes 2*b(E)*b(F) in the P^2/2 basis).")
