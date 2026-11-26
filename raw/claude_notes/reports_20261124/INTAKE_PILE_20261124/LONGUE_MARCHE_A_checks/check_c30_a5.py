# LM4_SUCCESSOR C.30 calibration example: lambda=1, f=[x,y]^2, x=(123), y=(345) in A5, right-to-left products
def perm(cycles, n=5):
    p = list(range(n + 1))
    for c in cycles:
        for i in range(len(c)):
            p[c[i]] = c[(i + 1) % len(c)]
    return tuple(p)
def mul(a, b):  # (a*b)(i) = a(b(i)), right-to-left
    return tuple(a[b[i]] for i in range(len(a)))
def inv(a):
    r = [0] * len(a)
    for i, v in enumerate(a): r[v] = i
    return tuple(r)
def gen(gs):
    e = tuple(range(6)); S = {e}; fr = [e]
    while fr:
        nf = []
        for g in fr:
            for h in gs:
                k = mul(g, h)
                if k not in S: S.add(k); nf.append(k)
        fr = nf
    return S
def cyc(p):
    seen = set(); out = []
    for i in range(1, 6):
        if i in seen or p[i] == i: continue
        c = [i]; j = p[i]
        while j != i: c.append(j); j = p[j]
        seen |= set(c); out.append(tuple(c))
    return out
x = perm([(1, 2, 3)]); y = perm([(3, 4, 5)])
c = mul(mul(x, y), mul(inv(x), inv(y)))
f = mul(c, c)
y2 = mul(mul(inv(f), y), f)
print('f =', cyc(f), ' f^-1 y f =', cyc(y2))
print('|<x,y>| =', len(gen([x, y])), ' |<x, f^-1 y f>| =', len(gen([x, y2])))
H = gen([x, y2]); print('fixes 4:', all(h[4] == 4 for h in H))
