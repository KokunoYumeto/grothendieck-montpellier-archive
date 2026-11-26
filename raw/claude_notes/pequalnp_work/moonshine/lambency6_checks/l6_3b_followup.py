"""Follow-up to l6_3: structure of P205's mod-4 monodromy group, and the L-polynomial of the Bolza curve.
Run: python -I -B l6_3b_followup.py"""
import itertools, sympy as sp
from collections import Counter
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
A = [sp.Matrix([[1, 0, 0, 0], [0, -1, 2, 0], [0, 0, -1, 0], [0, 1, 0, 1]]),
     sp.Matrix([[-1, 0, 0, 0], [0, 1, 0, 0], [2, 0, -1, 0], [0, 0, 1, 1]]),
     sp.Matrix([[-1, 0, 0, 0], [0, -1, -2, 0], [-2, 0, 1, 0], [2, 1, 1, 1]])]
def red4(M): return tuple(int(M[i, j]) % 4 for i in range(4) for j in range(4))
def mul4(X, Y): return tuple(sum(X[4*i+k]*Y[4*k+j] for k in range(4)) % 4 for i in range(4) for j in range(4))
id4 = red4(sp.eye(4)); gens = [red4(a) for a in A]
G = {id4}; fr = [id4]
while fr:
    nx = []
    for g in fr:
        for h in gens:
            y = mul4(g, h)
            if y not in G: G.add(y); nx.append(y)
    fr = nx
G = list(G)
sq = Counter(mul4(g, g) for g in G)
Z = [z for z in G if all(mul4(z, g) == mul4(g, z) for g in G)]
def inv(g):
    for h in G:
        if mul4(g, h) == id4: return h
comm = {mul4(mul4(inv(a), inv(b)), mul4(a, b)) for a in G for b in G}
say("P205 mod-4 monodromy group: order", len(G), "; distinct squares", len(sq), "; |centre|", len(Z), "; commutators", len(comm))
say("  squares of the generators distinct:", len({mul4(g, g) for g in gens}), "of 3")
# Q8 x C2 has a single nontrivial square; C4 x| C4 has three.  Count elements of order 4 per square value
say("  square value multiplicities:", sorted(sq.values()))
# Bolza: L-polynomial over F_p from counts over F_p and F_p^2
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]
def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)
# F_{p^2} arithmetic for p = 3 mod 4 as F_p[i]; general: use a nonresidue
def count_Fp2(p):
    # elements u + v t with t^2 = n (n nonresidue)
    n = next(k for k in range(2, p) if leg(k, p) == -1)
    def mul(a, b): return ((a[0]*b[0] + n*a[1]*b[1]) % p, (a[0]*b[1] + a[1]*b[0]) % p)
    def pw(a, e):
        r = (1, 0)
        while e:
            if e & 1: r = mul(r, a)
            a = mul(a, a); e >>= 1
        return r
    q = p * p
    cnt = 1  # point at infinity
    for u in range(p):
        for v in range(p):
            z = (u, v)
            z5 = pw(z, 5)
            f = ((z5[0] - u) % p, (z5[1] - v) % p)
            if f == (0, 0): cnt += 1
            else:
                cnt += 2 if pw(f, (q - 1)//2) == (1, 0) else 0
    return cnt
def count_Fp(p):
    return 1 + sum(1 + leg(z**5 - z, p) for z in range(p))
def ap(a2, a4, a6, p):
    return p + 1 - (1 + sum(1 + leg(x**3 + a2*x*x + a4*x + a6, p) for x in range(p)))
rows = []
for p in [q for q in primes_upto(110) if q > 2]:
    N1, N2 = count_Fp(p), count_Fp2(p)
    a1 = p + 1 - N1
    s2 = p*p + 1 - N2          # = a1^2 - 2 a2
    a2 = (a1*a1 - s2) // 2
    T = sp.symbols("T")
    L = 1 - a1*T + a2*T**2 - p*a1*T**3 + p*p*T**4
    rows.append((p, p % 8, a1, a2, sp.factor(L)))
for r in rows[:14]: say("  p=%d (p mod 8 = %d): a1=%d a2=%d  L(T) = %s" % r)
with open(__file__.replace(".py", "_output.txt"), "w", encoding="utf-8") as fh: fh.write("\n".join(out) + "\n")

# Verify the Bolza L-polynomial pattern at every odd prime < 200:
#  p = 1 mod 8: L = (1 + c T + p T^2)^2 with c = +-2a, p = a^2 + 2b^2;   p = 3 mod 8: L = 1 + 2(a^2 - 2b^2) T^2 + p^2 T^4;
#  p = 5 mod 8: L = (1 - p T^2)^2;   p = 7 mod 8: L = (1 + p T^2)^2.
def rep_a2b2(p):
    for a in range(0, int(p ** 0.5) + 1):
        r = p - a * a
        if r >= 0 and r % 2 == 0:
            b2 = r // 2; b = int(round(b2 ** 0.5))
            if b * b == b2: return a, b
    return None
nok = 0; nall = 0; fails = []
for p in [q for q in primes_upto(200) if q > 2]:
    nall += 1
    N1, N2 = count_Fp(p), count_Fp2(p)
    a1 = p + 1 - N1; s2 = p * p + 1 - N2; a2 = (a1 * a1 - s2) // 2
    r = p % 8
    if r == 1:
        a, b = rep_a2b2(p); ok = (a1 in (4 * a, -4 * a)) and a2 == a1 * a1 // 4 + 2 * p   # L = (1 - (a1/2) T + p T^2)^2, a1/2 = +-2a
    elif r == 3:
        a, b = rep_a2b2(p); ok = a1 == 0 and a2 == 2 * (a * a - 2 * b * b)
    elif r == 5:
        ok = a1 == 0 and a2 == -2 * p
    else:
        ok = a1 == 0 and a2 == 2 * p
    nok += ok
    if not ok: fails.append((p, a1, a2))
say("Bolza L-polynomial pattern (eigenvalues -pi twice at p=1 mod 8, +-i pi at p=3 mod 8, inert pattern at 5, 7 mod 8):",
    nok, "of", nall, "odd primes < 200; failures:", fails)
with open(__file__.replace(".py", "_output.txt"), "w", encoding="utf-8") as fh: fh.write("\n".join(out) + "\n")
