import sys; sys.path.insert(0, '.')
from qs import mul, powr, eprod
from sympy import primerange
N = 600
# eta(6t)^4 = q * prod (1-q^{6n})^4 : a[n] coefficient of q^n
f = [0] + powr(eprod(6, N), 4, N)[:N-1]
bad = []
for p in primerange(5, 300):
    cnt = 1 + sum(1 for x in range(p) for y in range(p) if (y*y - x**3 - 1) % p == 0)
    ap = p + 1 - cnt
    if f[p] != ap: bad.append((p, f[p], ap))
print("eta(6t)^4 a_p == a_p(y^2=x^3+1) for 5<=p<300:", not bad, bad[:4])
# eta(3t)^8 = q * prod(1-q^{3n})^8 ; compare with sum over primary pi of norm p of pi^3 + conj
g = [0] + powr(eprod(3, N), 8, N)[:N-1]
import cmath
w = complex(-0.5, 3**0.5/2)
bad = []
for p in primerange(5, 300):
    if p % 3 == 2:
        if g[p] != 0: bad.append((p, g[p], 0))
        continue
    # find pi = a + b w with norm a^2 - ab + b^2 = p and pi = 1 mod 3 (primary: a = 1 mod 3? use pi = 2 mod 3 convention): try both
    sols = []
    for a in range(-40, 41):
        for b in range(-40, 41):
            if a*a - a*b + b*b == p: sols.append((a, b))
    vals = set()
    for a, b in sols:
        if (a - 1) % 3 == 0 and b % 3 == 0:  # pi = 1 mod 3
            z = complex(a, 0) + b*w
            vals.add(round((z**3 + z.conjugate()**3).real))
    if g[p] not in vals: bad.append((p, g[p], vals))
print("eta(3t)^8 a_p == pi^3 + pibar^3 (pi = 1 mod 3) for p<300:", not bad, bad[:4])
