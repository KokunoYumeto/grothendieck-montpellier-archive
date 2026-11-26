# Unary theta components S_{6,r}(tau) = sum_{k = r mod 12} k q^{k^2/24} as eta products; Omega^X action.
# Work in the variable x = q^{1/24}; series indexed by exponent of x.
from qs import mul, inv, powr, eprod
M = 24*40  # exponent bound in x

def eprod_x(d):
    # prod (1 - q^{dk}) in x = q^{1/24}: (1 - x^{24 d k})
    a = [0]*M; a[0] = 1
    k = 1
    while 24*d*k < M:
        b = a[:]
        s = 24*d*k
        for i in range(M - s):
            b[i+s] -= a[i]
        a = b
        k += 1
    return a

def etaq_x(rs):
    lead = sum(d*r for d, r in rs.items())  # exponent of x from q^{d r/24}
    out = [1] + [0]*(M-1)
    for d, r in rs.items():
        out = mul(out, powr(eprod_x(d), r, M), M)
    # shift by lead (must be >= 0 here)
    assert lead >= 0
    return ([0]*lead + out)[:M]

def S6(r):
    a = [0]*M
    for k in range(-60, 61):
        if (k - r) % 12 == 0 and k*k < M:
            a[k*k] += k
    return a

def show(a, n=8):
    return [(i, a[i]) for i in range(M) if a[i] != 0][:n]

S = {r: S6(r) for r in range(12)}
print("S_{6,1}-S_{6,5}:", show([x - y for x, y in zip(S[1], S[5])]))
e5 = etaq_x({1: 5, 2: -2})
print("eta^5/eta(2t)^2  :", show(e5))
print("equal:", all(int(x - y) == int(z) for x, y, z in zip(S[1], S[5], e5)))
print("S_{6,1}+S_{6,5}:", show([x + y for x, y in zip(S[1], S[5])]))
print("S_{6,3}:", show(S[3]))
e3 = etaq_x({3: 3})
print("3 eta(3t)^3:", show([3*x for x in e3]))
print("S_{6,3} == 3 eta(3t)^3:", all(int(a) == 3*int(b) for a, b in zip(S[3], e3)))
print("S_{6,2}:", show(S[2]))
e2 = etaq_x({4: 5, 8: -2})
print("2 eta(4t)^5/eta(8t)^2:", show([2*x for x in e2]))
print("S_{6,2} == 2 eta(4t)^5/eta(8t)^2:", all(int(a) == 2*int(b) for a, b in zip(S[2], e2)))
print("S_{6,4}:", show(S[4]))
# try to identify S_{6,4} = 4 * sum_{j = 1 mod 3} j q^{2 j^2/3}: test eta quotients of level dividing 48 with small exponents
import itertools
target = S[4]
found = []
divs = [1, 2, 4, 8, 16, 3, 6, 12, 24, 48]
for combo in itertools.product(range(-3, 6), repeat=4):
    ds = [8, 16, 4, 32]
    rs = {d: r for d, r in zip(ds, combo) if r != 0}
    lead = sum(d*r for d, r in rs.items())
    if lead != 16: continue
    if sum(rs.values()) != 3: continue  # weight 3/2
    try:
        ser = etaq_x(rs)
    except AssertionError:
        continue
    if all(4*int(b) == int(a) for a, b in zip(target[:300], ser[:300])):
        found.append(rs)
print("S_{6,4} = 4*eta-quotient candidates:", found)
# S_{6,1}+S_{6,5}: also search small eta quotients (lead exponent 1)
target = [x + y for x, y in zip(S[1], S[5])]
found = []
for combo in itertools.product(range(-6, 7), repeat=4):
    ds = [1, 2, 4, 8]
    rs = {d: r for d, r in zip(ds, combo) if r != 0}
    lead = sum(d*r for d, r in rs.items())
    if lead != 1 or sum(rs.values()) != 3: continue
    ser = etaq_x(rs)
    if all(int(b) == int(a) for a, b in zip(target[:300], ser[:300])):
        found.append(rs)
print("S_{6,1}+S_{6,5} eta-quotient candidates (levels 1,2,4,8):", found)
