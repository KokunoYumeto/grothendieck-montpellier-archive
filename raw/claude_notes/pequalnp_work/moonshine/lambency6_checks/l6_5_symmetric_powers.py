"""Lambency-6 pass, check 5: the twined shadow of A5^4 D4 is the symmetric-power tower of the faithful two-dimensional
representation of the umbral group GL2(F3), and the GL(2) x GL(3) -> GL(6) decomposition 2 x 3 = 4 + 2 holds inside it,
with the '+2' twisted by the sign.

V = 2' (faithful, character values 2, -2, 0, -1, 1, 0, +-i sqrt2), det V = sgn = s.
Claims (all 48 elements g of GL2(F3); a, b, c, s are Codex's twined-shadow class functions, see l6_1):
  s = det V;  a - 1 = Sym^2 V;  b = Sym^3 V;  c = 2-dim rep of the S3 quotient;
  V (x) Sym^2 V = Sym^3 V (+) V (x) det   (Clebsch-Gordan 2 x 3 = 4 + 2, the '+2' is V twisted by the sign);
  Sym^k V(-g) = (-1)^k Sym^k V(g): the centre (= quadratic twist) acts on the Sym^k layer by (-1)^k, matching the
  theta-index parity (-1)^(r+1) of the shadow components that carry it.
Arithmetic form on E: y^2 = x^3 - 3x + 1 (mod-3 image GL2(F3)), t(p) = chi_V(Frob_p):
  U(p) - 2 = t^2 - s = a_p(Sym^2),  V(p) = b(p) = t^3 - 2 s t = a_p(Sym^3),  s = chi_-3(p).
Run: python -I -B l6_5_symmetric_powers.py
"""
import cmath
from itertools import product
from collections import Counter

out = []
def say(*a):
    s_ = " ".join(str(x) for x in a); print(s_); out.append(s_)

GL = [(a, b, c, d) for a, b, c, d in product(range(3), repeat=4) if (a * d - b * c) % 3]
I = (1, 0, 0, 1)
def mul(g, h):
    a, b, c, d = g; e, f, gg, hh = h
    return ((a * e + b * gg) % 3, (a * f + b * hh) % 3, (c * e + d * gg) % 3, (c * f + d * hh) % 3)
def neg(g): return tuple((-x) % 3 for x in g)
def order(g):
    k, x = 1, g
    while x != I: x = mul(x, g); k += 1
    return k
lines = [(1, 0), (0, 1), (1, 1), (1, 2)]
def act(g, v): return ((g[0] * v[0] + g[1] * v[1]) % 3, (g[2] * v[0] + g[3] * v[1]) % 3)
def nl(v):
    x, y = v
    inv = (1 if x == 1 else 2) if x else (1 if y == 1 else 2)
    return ((x * inv) % 3, (y * inv) % 3)
P = [frozenset({frozenset({(1, 0), (0, 1)}), frozenset({(1, 1), (1, 2)})}),
     frozenset({frozenset({(1, 0), (1, 1)}), frozenset({(0, 1), (1, 2)})}),
     frozenset({frozenset({(1, 0), (1, 2)}), frozenset({(0, 1), (1, 1)})})]
def stats(g):
    a = b = 0; perm = {}
    for l in lines:
        im = act(g, l); perm[l] = nl(im)
        if nl(im) == l: a += 1; b += 1 if im == l else -1
    c = sum(1 for Q in P if frozenset(frozenset(perm[x] for x in blk) for blk in Q) == Q) - 1
    s = 1 if (g[0] * g[3] - g[1] * g[2]) % 3 == 1 else -1
    return a, b, c, s
r2 = cmath.sqrt(-2)
def chiV(g):
    o = order(g)
    if g == I: return 2
    if g == neg(I): return -2
    if o == 3: return -1
    if o == 6: return 1
    if o == 8: return r2 if (g[0] + g[3]) % 3 == 1 else -r2
    return 0
def sym(k, g):
    # character of Sym^k V via eigenvalues: chiV(g) = al + be, det = al be; Sym^k = sum al^i be^(k-i)
    t = chiV(g); dt = stats(g)[3]
    # roots of X^2 - t X + dt
    disc = cmath.sqrt(t * t - 4 * dt)
    al, be = (t + disc) / 2, (t - disc) / 2
    return sum(al ** i * be ** (k - i) for i in range(k + 1))
bad = Counter()
for g in GL:
    a, b, c, s = stats(g)
    t = chiV(g)
    # det V = s  (det from eigenvalues = al*be; check via chi(g)^2 - chi(g^2) = 2 det)
    if abs((t * t - chiV(mul(g, g))) / 2 - s) > 1e-9: bad["det V != s"] += 1
    if abs(sym(2, g) - (a - 1)) > 1e-9: bad["Sym^2 V != a - 1"] += 1
    if abs(sym(3, g) - b) > 1e-9: bad["Sym^3 V != b"] += 1
    if abs(t * sym(2, g) - (sym(3, g) + t * s)) > 1e-9: bad["V x Sym^2 V != Sym^3 V + V x det"] += 1
    for k in range(0, 7):
        if abs(sym(k, neg(g)) - (-1) ** k * sym(k, g)) > 1e-9: bad[f"centre on Sym^{k}"] += 1
    # the remaining components: r = 3 coefficient a + c = 1 + Sym^2 V + c; U = a + 1 = 2 + Sym^2 V
    if abs((a + c) - (1 + sym(2, g) + c)) > 1e-9: bad["r=3"] += 1
    # c is the S3 two-dimensional character: c = V x (S3 2-dim) relation b = t c
    if abs(b - t * c) > 1e-9: bad["b != V c"] += 1
say("GL2(F3), all 48 elements: failures", dict(bad) if bad else "none")
say("  s = det V; a - 1 = Sym^2 V; b = Sym^3 V = V (x) c; V (x) Sym^2 V = Sym^3 V (+) V (x) det;")
say("  centre -I acts on Sym^k V by (-1)^k (k = 0..6).")
say("  Twined shadow at g (Codex's matrix): r=1,5 diagonal a + 1 = 2 + Sym^2 V; r=1,5 cross term s = det V;")
say("  r=2,4: b = Sym^3 V; r=3: a + c = 1 + Sym^2 V + c.  Odd r carry even symmetric powers, even r the odd one.")
# multiplicities of irreducibles (inner products) of Sym^k V for k = 0..6 against the 8 irreducible characters
def irr(g):
    a, b, c, s = stats(g); t = chiV(g)
    return [1, s, c, a - 1, (a - 1) * s, t, t.conjugate() if isinstance(t, complex) else t, b]
names = ["1", "sgn", "2(S3)", "3", "3'", "2'", "2''", "4"]
for k in range(0, 7):
    mults = [sum(sym(k, g) * complex(irr(g)[j]).conjugate() for g in GL) / 48 for j in range(8)]
    say(f"  Sym^{k} V =", " + ".join(f"{round(m.real)}*{n}" for m, n in zip(mults, names) if abs(m) > 1e-9))

# arithmetic form on E: y^2 = x^3 - 3x + 1
def primes_upto(n):
    sv = bytearray([1]) * (n + 1); sv[0] = sv[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sv[i]: sv[i * i::i] = bytearray(len(sv[i * i::i]))
    return [i for i in range(n + 1) if sv[i]]
def leg(x, p):
    x %= p
    return 0 if x == 0 else (1 if pow(x, (p - 1) // 2, p) == 1 else -1)
A, B = -3, 1
def ap(p): return -sum(leg(x ** 3 + A * x + B, p) for x in range(p))
def stats_of_class(g): return stats(g)
bad = Counter(); n = 0
for p in primes_upto(3000):
    if p < 5: continue
    n += 1
    a_p = ap(p)
    hr = [x for x in range(p) if (x ** 4 - 6 * x * x + 4 * x - 3) % p == 0]
    nplus = sum(1 for x in hr if leg(x ** 3 + A * x + B, p) == 1)
    nminus = len(hr) - nplus
    a_, b_ = len(hr), nplus - nminus
    s_ = 1 if p % 3 == 1 else -1
    cands = [g for g in GL if (g[0] + g[3]) % 3 == a_p % 3 and (g[0] * g[3] - g[1] * g[2]) % 3 == p % 3 and stats(g)[:2] == (a_, b_)]
    t = chiV(cands[0])
    U = a_ + 1; Vc = b_
    if abs(U - 2 - (t * t - s_)) > 1e-9: bad["U - 2 != t^2 - s"] += 1
    if abs(Vc - (t ** 3 - 2 * s_ * t)) > 1e-9: bad["V != t^3 - 2 s t"] += 1
    if stats(cands[0])[3] != s_: bad["s != chi_-3(p)"] += 1
say("E: y^2 = x^3 - 3x + 1, primes 5..3000 (", n, "): U - 2 = t^2 - chi_-3(p) and V = t^3 - 2 chi_-3(p) t with t =",
    "chi_V(Frob_p) (the trace of the weight-one octahedral form of the Langlands-Tunnell step); failures:", dict(bad) if bad else "none")
with open(__file__.replace(".py", "_output.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
