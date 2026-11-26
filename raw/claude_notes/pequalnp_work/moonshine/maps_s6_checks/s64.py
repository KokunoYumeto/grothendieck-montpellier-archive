import sys; sys.path.insert(0, '.')
import itertools
from qs import mul, powr
M = 24*30
def eprod_x(d):
    a = [0]*M; a[0] = 1
    k = 1
    while 24*d*k < M:
        b = a[:]; s = 24*d*k
        for i in range(M - s): b[i+s] -= a[i]
        a = b; k += 1
    return a
cache = {}
def ep(d, r):
    if (d, r) not in cache: cache[(d, r)] = powr(eprod_x(d), r, M)
    return cache[(d, r)]
def etaq_x(rs):
    lead = sum(d*r for d, r in rs.items())
    out = [1] + [0]*(M-1)
    for d, r in rs.items(): out = mul(out, ep(d, r), M)
    return ([0]*lead + out)[:M] if lead >= 0 else None
def S6(r):
    a = [0]*M
    for k in range(-60, 61):
        if (k - r) % 12 == 0 and k*k < M: a[k*k] += k
    return a
S4 = S6(4); Sp = [x + y for x, y in zip(S6(1), S6(5))]
ds = [1, 2, 3, 4, 6, 8, 12, 16, 24]
res4, resp = [], []
for combo in itertools.product(range(-4, 7), repeat=4):
    for dsub in itertools.combinations(ds, 4):
        rs = {d: r for d, r in zip(dsub, combo) if r != 0}
        if sum(rs.values()) != 3: continue
        lead = sum(d*r for d, r in rs.items())
        if lead not in (16, 1): continue
        ser = etaq_x(rs)
        if ser is None: continue
        if lead == 16 and all(4*int(b) == int(a) for a, b in zip(S4[:400], ser[:400])): res4.append(rs)
        if lead == 1 and all(int(b) == int(a) for a, b in zip(Sp[:400], ser[:400])): resp.append(rs)
print("S_{6,4} = 4 * ", sorted(set(tuple(sorted(r.items())) for r in res4)))
print("S_{6,1}+S_{6,5} = ", sorted(set(tuple(sorted(r.items())) for r in resp)))
