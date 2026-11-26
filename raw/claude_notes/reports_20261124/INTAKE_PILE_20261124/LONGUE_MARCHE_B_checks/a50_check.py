# Independent check of ANABELIAN_A1_SUCCESSOR A.50 (Claude Opus 5.5 at effort high, 24 Nov 2026). Standard library only.
# Curve C: y^2 + (x^2+x) y = x^5 + 1 over F_2; L = F_8; cover = pullback of the 19-part of the Lang isogeny along R -> [R - base].
MOD = 0b1000011  # x^6+x+1, GF(64)
def gmul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
        if a & 64: a ^= MOD
    return r
EXP = [0]*126; LOG = [0]*64
x = 1
for i in range(63):
    EXP[i] = x; LOG[x] = i; x = gmul(x, 2)
assert x == 1 and len(set(EXP[:63])) == 63
for i in range(63, 126): EXP[i] = EXP[i-63]
def ginv(a): return EXP[(63 - LOG[a]) % 63]
def gpow(a, n):
    if a == 0: return 0 if n else 1
    return EXP[(LOG[a]*n) % 63]
F8 = [a for a in range(64) if gpow(a, 8) == a]
assert len(F8) == 8
def trim(p):
    p = list(p)
    while p and p[-1] == 0: p.pop()
    return p
def padd(p, q):
    n = max(len(p), len(q))
    return trim([(p[i] if i < len(p) else 0) ^ (q[i] if i < len(q) else 0) for i in range(n)])
def pmul(p, q):
    if not p or not q: return []
    r = [0]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                if b: r[i+j] ^= gmul(a, b)
    return trim(r)
def pdivmod(p, q):
    p = trim(p); q = trim(q); assert q
    out = [0]*max(1, len(p)-len(q)+1); iq = ginv(q[-1])
    while len(p) >= len(q) and p:
        c = gmul(p[-1], iq); d = len(p)-len(q); out[d] = c
        for i, b in enumerate(q): p[i+d] ^= gmul(c, b)
        p = trim(p)
    return trim(out), p
def pmod(p, q): return pdivmod(p, q)[1]
def pdiv(p, q):
    a, b = pdivmod(p, q); assert not b, "inexact"; return a
def monic(p):
    p = trim(p); c = ginv(p[-1]); return [gmul(c, a) for a in p]
def xgcd(a, b):
    r0, r1, s0, s1, t0, t1 = trim(a), trim(b), [1], [], [], [1]
    while r1:
        qq, rr = pdivmod(r0, r1)
        r0, r1 = r1, rr
        s0, s1 = s1, padd(s0, pmul(qq, s1))
        t0, t1 = t1, padd(t0, pmul(qq, t1))
    c = ginv(r0[-1])
    return [gmul(c, z) for z in r0], [gmul(c, z) for z in s0], [gmul(c, z) for z in t0]
H = [0, 1, 1]            # h = x^2 + x
F = [1, 0, 0, 0, 0, 1]   # f = x^5 + 1
G = 2
def peval(p, a):
    r = 0
    for c in reversed(p): r = gmul(r, a) ^ c
    return r
def norm(u, v):
    u = monic(u) if u else [1]
    return (tuple(u), tuple(pmod(v, u)))
def reduce_(u, v):
    while len(u)-1 > G:
        u = monic(pdiv(padd(padd(F, pmul(v, H)), pmul(v, v)), u))   # (f - v h - v^2)/u, char 2
        v = pmod(padd(H, v), u)
    return norm(u, v)
def add(D1, D2):
    u1, v1 = list(D1[0]), list(D1[1]); u2, v2 = list(D2[0]), list(D2[1])
    d1, e1, e2 = xgcd(u1, u2)
    d, c1, c2 = xgcd(d1, padd(padd(v1, v2), H))
    s1, s2, s3 = pmul(c1, e1), pmul(c1, e2), c2
    u = pdiv(pmul(u1, u2), pmul(d, d))
    num = padd(padd(pmul(pmul(s1, u1), v2), pmul(pmul(s2, u2), v1)), pmul(s3, padd(pmul(v1, v2), F)))
    v = pmod(pdiv(num, d), u)
    return reduce_(u, v)
ZERO = ((1,), ())
def neg(D): return norm(list(D[0]), padd(H, list(D[1])))
def mul(n, D):
    R = ZERO; B = D
    while n:
        if n & 1: R = add(R, B)
        B = add(B, B); n >>= 1
    return R
def is_valid(D):
    u, v = list(D[0]), list(D[1])
    return not pmod(padd(padd(pmul(v, v), pmul(H, v)), F), u)
def points(field):
    return [(a, b) for a in field for b in field if gmul(b, b) ^ gmul(peval(H, a), b) ^ peval(F, a) == 0]
def pt(R):  # [R - O], O the point at infinity
    a, b = R
    return norm([a, 1], [b] if b else [])
P = (0, 1); Q = (1, 0)
CF8 = points(F8); CF64 = points(range(64))
q = 8; N1 = len(CF8)+1; N2 = len(CF64)+1
print("#C(F8) =", N1, " #C(F64) =", N2)
J = set([ZERO])
for a in F8:
    for b in F8:
        D = norm([a, 1], [b])
        if is_valid(D): J.add(D)
for a0 in F8:
    for a1_ in F8:
        for b0 in F8:
            for b1 in F8:
                D = norm([a0, a1_, 1], [b0, b1])
                if is_valid(D): J.add(D)
print("#J(F8) by enumeration =", len(J))
a1 = N1 - q - 1; a2 = (N2 - q*q - 1 + a1*a1)//2
print("#J(F8) from zeta =", 1 + a1 + a2 + q*a1 + q*q, " (L(T)=1+a1 T+a2 T^2+q a1 T^3+q^2 T^4 with a1,a2 =", a1, a2, ")")
# group law sanity: closure and associativity on a sample
Jl = sorted(J)
assert all(add(y, z) in J for y in Jl[:20] for z in Jl[:20])
assert all(add(add(Jl[i], Jl[j]), Jl[k]) == add(Jl[i], add(Jl[j], Jl[k])) for i in range(0, 76, 7) for j in range(0, 76, 5) for k in range(0, 76, 11))
assert all(add(y, neg(y)) == ZERO for y in Jl)
DPQ = add(pt(P), neg(pt(Q)))
print("[P-Q] nonzero:", DPQ != ZERO, " 2[P-Q] = 0:", mul(2, DPQ) == ZERO)
two_part = [y for y in Jl if mul(4, y) == ZERO]
print("#J(F8)[2^inf] =", len(two_part))
g = next(mul(4, y) for y in Jl if mul(4, y) != ZERO)
assert mul(19, g) == ZERO
dl = {}; T = ZERO
for k in range(19): dl[T] = k; T = add(T, g)
def chi_exp(y): return dl[mul(4, y)]
def frob(a): return gpow(a, 8)
def RsigmaR(R):  # class of R + sigma(R) - 2O in J(F8)
    a, b = R
    if frob(a) == a and frob(b) == b: return add(pt(R), pt(R))
    return add(pt(R), pt((frob(a), frob(b))))
def cmul(A, B):
    r = [0]*19
    for i, s in enumerate(A):
        if s:
            for j, t in enumerate(B):
                if t: r[(i+j) % 19] += s*t
    return r
def rel_classnumber(base):
    jb = pt(base)
    c1 = [0]*19; c2 = [0]*19
    for R in CF8 + ['O']:
        y = neg(jb) if R == 'O' else add(pt(R), neg(jb))
        c1[chi_exp(y)] += 1
    for R in CF64 + ['O']:
        y = add(neg(jb), neg(jb)) if R == 'O' else add(RsigmaR(R), add(neg(jb), neg(jb)))
        c2[chi_exp(y)] += 1
    split = c1[0]  # number of rational points R with chi([R-base]) trivial: base point fibre splits iff [base-base]=0, trivially
    sq = cmul(c1, c1)
    num = [sq[i] + c2[i] for i in range(19)]
    if num[0] % 2: num = [c + 1 for c in num]   # add 1+x+...+x^18 (= 0 at zeta) to make all coefficients even
    assert all(c % 2 == 0 for c in num), num
    Lv = [(1 if i == 0 else 0) + c1[i] + num[i]//2 for i in range(19)]   # L(chi,1) = 1 + S1 + (S1^2+S2)/2
    prod = [1] + [0]*18
    for k in range(1, 19):
        conj = [0]*19
        for i, c in enumerate(Lv): conj[(i*k) % 19] += c
        prod = cmul(prod, conj)
    assert len(set(prod[1:])) == 1
    return prod[0] - prod[1]
print("Q splits in the P-based cover (chi([Q-P]) trivial):", chi_exp(add(pt(Q), neg(pt(P)))) == 0)
for name, base in [("P", P), ("Q", Q)]:
    print("relative class number, cover based at", name, "=", rel_classnumber(base))
res = {}
for R in CF8:
    res[R] = rel_classnumber(R)
print("all affine rational points:", sorted(res.values()))
