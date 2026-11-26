import sys; sys.path.insert(0, '.')
from qs import mul, eprod
from sympy import primerange
N = 400
# eta(t) eta(23 t) = q * prod(1-q^n)(1-q^{23n}) ; leading q^{(1+23)/24} = q^1
f = mul(eprod(1, N), eprod(23, N), N)
a = [0] + f[:N-1]   # a[n] = coefficient of q^n
bad = []
for p in primerange(2, N):
    if p == 23: continue
    roots = sum(1 for x in range(p) if (x**3 - x + 1) % p == 0)
    if a[p] != roots - 1: bad.append((p, a[p], roots))
print("a_p(eta eta23) == #roots(x^3-x+1 mod p) - 1 for all p<400, p!=23:", not bad, bad[:5])
# AG-012: E: y^2 = x^3 - x + 1, Delta = -16(4(-1)^3 + 27) ; j
a4, a6 = -1, 1
Delta = -16*(4*a4**3 + 27*a6**2)
from fractions import Fraction as Fr
j = Fr(-1728*(4*a4)**3, Delta)
print("Delta =", Delta, " j =", j)
