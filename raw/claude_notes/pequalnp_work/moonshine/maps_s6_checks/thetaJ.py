import sys; sys.path.insert(0, '.')
from fractions import Fraction as Fr
import sympy as sp
from qs import mul, inv, powr, eprod, E, subs, scal, add, shift, etaq
N = 14
def cut(a): return a[:N]
E4 = E(4, N); E43 = powr(E4, 3, N)
E43_3 = subs(E43, 3, N)
Delta = shift(powr(eprod(1, N), 24, N), 1, N)
Delta3 = subs(Delta, 3, N)
eta12 = shift(mul(powr(eprod(1, N), 12, N), powr(eprod(3, N), 12, N), N), 2, N)  # q^{(12+36)/24} = q^2
Th = [Fr(7381, 66430)*x + Fr(59049, 66430)*y - Fr(531432, 6643)*z - Fr(4251528, 6643)*w + Fr(88938, 73)*v
      for x, y, z, w, v in zip(E43, E43_3, Delta, Delta3, eta12)]
print("Theta_J from S6-087 formula:", [str(x) for x in Th[:10]])
given = [1, 0, 23058, 1849032, 44291124, 514246104, 3824355978, 20831769864, 90541677312]
print("matches given coefficients through q^8:", [int(x) for x in Th[:9]] == given)
# a(q) = theta of Z[omega] with norm m^2+mn+n^2
a = [0]*N
for m in range(-20, 21):
    for n in range(-20, 21):
        v = m*m + m*n + n*n
        if v < N: a[v] += 1
print("a(q) =", a[:10])
b = shift(mul(powr(eprod(3, N), 9, N), powr(eprod(1, N), -3, N), N), 1, N)  # eta(3t)^9/eta(t)^3 = q * ...
print("b(q) = eta(3t)^9/eta(t)^3 =", [int(x) for x in b[:10]])
mons = [mul(powr(a, 12 - 3*i, N), powr(b, i, N), N) for i in range(5)]
cs = sp.symbols('c0:5')
eqs = []
for k in range(N):
    eqs.append(sum(cs[i]*sp.Rational(mons[i][k]) for i in range(5)) - sp.Rational(Th[k].numerator, Th[k].denominator))
sol = sp.solve(eqs, cs, dict=True)
print("Theta_J = sum c_i a^(12-3i) b^i :", sol)
# eta(t)^6 eta(3t)^6 = D (AG-017); check D^2 = eta^12 eta(3t)^12 trivially and D in terms of a, b: D = ?
Dser = shift(mul(powr(eprod(1, N), 6, N), powr(eprod(3, N), 6, N), N), 1, N)
mons6 = [mul(powr(a, 6 - 3*i, N), powr(b, i, N), N) for i in range(3)]
c6 = sp.symbols('d0:3')
sol6 = sp.solve([sum(c6[i]*sp.Rational(mons6[i][k]) for i in range(3)) - Dser[k] for k in range(N)], c6, dict=True)
print("D = eta^6(t) eta^6(3t) in a,b:", sol6)
# E4 and E4(3t), Delta in a, b as checks
for name, ser, wt in [("E4", E4, 4), ("Delta", Delta, 12)]:
    k = wt // 3 + 1
    mons_w = [mul(powr(a, wt - 3*i, N), powr(b, i, N), N) for i in range(wt//3 + 1)]
    cc = sp.symbols('e0:%d' % len(mons_w))
    s = sp.solve([sum(cc[i]*sp.Rational(mons_w[i][kk]) for i in range(len(mons_w))) - sp.Rational(ser[kk]) for kk in range(N)], cc, dict=True)
    print(name, "in a,b:", s)
