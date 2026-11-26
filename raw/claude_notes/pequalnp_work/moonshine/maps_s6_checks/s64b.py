import sys; sys.path.insert(0, '.')
from qs import mul, powr
M = 24*80
def eprod_x(d):
    a = [0]*M; a[0] = 1; k = 1
    while 24*d*k < M:
        b = a[:]; s = 24*d*k
        for i in range(M - s): b[i+s] -= a[i]
        a = b; k += 1
    return a
def etaq_x(rs):
    lead = sum(d*r for d, r in rs.items()); out = [1] + [0]*(M-1)
    for d, r in rs.items(): out = mul(out, powr(eprod_x(d), r, M), M)
    return ([0]*lead + out)[:M]
def S6(r):
    a = [0]*M
    for k in range(-200, 201):
        if (k - r) % 12 == 0 and k*k < M: a[k*k] += k
    return a
e = etaq_x({2: 2, 4: -1, 8: 2})
print("S_{6,4} == 4 eta(2t)^2 eta(8t)^2/eta(4t) through q^80:", all(int(a) == 4*int(b) for a, b in zip(S6(4), e)))
e5 = etaq_x({1: 5, 2: -2}); S1, S5 = S6(1), S6(5)
print("S_{6,1}-S_{6,5} == eta^5/eta(2t)^2 through q^80:", all(int(a - b) == int(c) for a, b, c in zip(S1, S5, e5)))
