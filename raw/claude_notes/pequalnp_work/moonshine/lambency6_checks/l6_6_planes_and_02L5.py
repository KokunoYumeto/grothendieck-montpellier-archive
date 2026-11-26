"""Lambency-6 pass, check 6: the planes PG(2,q) with their polarity, the (2,3,6) triangle group, and the orders 11 / 13.

(a) Singer models D_q = {0,1,3} mod 7, {0,1,3,9} mod 13, {0,1,4,14,16} mod 21: difference sets, multipliers, the
    polarity x -> -x and its absolute points (a conic for q = 3, a line for q = 2, 4).
(b) Delta(2,3,6) = Z[omega] x| mu6 -> Z/(q^2+q+1) x| <-1, q> via omega -> q (q^3 = 1 mod q^2+q+1): every element maps
    to a collineation (u = q^k) or a correlation (u = -q^k) of the Singer plane; for q = 3 the image is the whole group
    of order 78 of affine maps x -> u x + t preserving the Singer structure.
(c) PG(2,3) = P(sl2(F3)) with the determinant (Killing) form: the adjoint action of GL2(F3) gives PGO3(3) = PGL2(3) = S4;
    the absolute conic = the nilpotent cone = P^1(F3) (kernel map), equivariantly.
(d) The PG(2,3) line code over F3 against the ternary quadratic-residue code of length 13; the ternary Golay code is the
    QR code of length 11.  Both 11 and 13 are p = -+1 mod 12 (chi_12(p) = 1, i.e. 3 a square mod p).
(e) 02L5: peripheral integers 12 l0 - 4 l1 - 3 l2 with (l1, l2) = (1, -1): 12 l0 - 1 (right gluing) and -12 l0 - 1 (wrong
    gluing); residues mod 12, primality, and whether the two sequences stay aligned with plane sizes q^2+q+1 and
    ternary/binary QR-code lengths.
Run: python -I -B l6_6_planes_and_02L5.py
"""
from itertools import product, combinations
from collections import Counter
import math

out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

# (a) ------------------------------------------------------------------------------------------------------------------
planes = {2: (7, [0, 1, 3]), 3: (13, [0, 1, 3, 9]), 4: (21, [0, 1, 4, 14, 16])}
for q, (n, D) in planes.items():
    diffs = Counter((a - b) % n for a in D for b in D if a != b)
    ok = all(diffs[d] == 1 for d in range(1, n))
    mults = [m for m in range(1, n) if math.gcd(m, n) == 1 and sorted((m * d) % n for d in D) in
             [sorted((d + t) % n for d in D) for t in range(n)]]
    lines = [frozenset((d + y) % n for d in D) for y in range(n)]
    absolute = [x for x in range(n) if (2 * x) % n in D]    # P_x on its polar line L_{-x}: x - (-x) in D
    collinear_triples = sum(1 for T in combinations(absolute, 3) if any(set(T) <= L for L in lines))
    is_line = frozenset(absolute) in lines
    say(f"(a) q={q}: PG(2,{q}) Singer set {D} mod {n}: difference set {ok}; multipliers {mults}; absolute points of the",
        f"polarity x->-x: {absolute} ({len(absolute)} = q+1); collinear triples among them {collinear_triples}; they form a line: {is_line}")

# (b) ------------------------------------------------------------------------------------------------------------------
for q, (n, D) in planes.items():
    # ring map Z[omega] -> Z/n, a + b omega -> a + b q
    assert (q * q + q + 1) % n == 0
    mu6 = sorted({(s * pow(q, k, n)) % n for s in (1, -1) for k in range(3)})
    Dset = set(D)
    def preserves(u, t):
        img = {(u * d + t) % n for d in D}
        lines = [frozenset((d + y) % n for d in D) for y in range(n)]
        negl = [frozenset((-d + y) % n for d in D) for y in range(n)]
        return frozenset(img) in lines, frozenset(img) in negl
    coll = sum(1 for u in mu6 for t in range(n) if preserves(u, t)[0])
    corr = sum(1 for u in mu6 for t in range(n) if preserves(u, t)[1])
    # all affine maps with u a unit that map D to a translate of +-D
    allaff = [(u, t) for u in range(1, n) if math.gcd(u, n) == 1 for t in range(n) if any(preserves(u, t))]
    us = sorted({u for u, t in allaff})
    say(f"(b) q={q}: image of mu6 = {mu6} (omega -> {q}); affine maps x->ux+t with u in mu6 preserving the plane: "
        f"{coll} collineations (u = q^k), {corr} correlations (u = -q^k); all units u that occur: {us}; group order {len(allaff)}"
        f" = 6 x {n}: {len(allaff) == 6 * n}")
say("    => for q = 2, 3 the Singer normalizer with polarity IS (Z[omega]/(q - omega)) x| mu6, the image of the (2,3,6)")
say("       triangle group: omega -> Frobenius multiplier q, -1 -> the polarity; for q = 4 the image has index 2 (multiplier 2).")

# (c) ------------------------------------------------------------------------------------------------------------------
F3 = range(3)
GL = [(a, b, c, d) for a, b, c, d in product(F3, repeat=4) if (a * d - b * c) % 3]
def mmul(g, h):
    a, b, c, d = g; e, f, gg, hh = h
    return ((a * e + b * gg) % 3, (a * f + b * hh) % 3, (c * e + d * gg) % 3, (c * f + d * hh) % 3)
def minv(g):
    a, b, c, d = g; det = (a * d - b * c) % 3; di = 1 if det == 1 else 2
    return ((d * di) % 3, (-b * di) % 3, (-c * di) % 3, (a * di) % 3)
# sl2(F3): trace-zero matrices X = [[x, y], [z, -x]] <-> vector (x, y, z); det form = -x^2 - yz
def to_vec(X): return (X[0] % 3, X[1] % 3, X[2] % 3)
def normp(v):
    for c in v:
        if c % 3:
            inv = 1 if c % 3 == 1 else 2
            return tuple((x * inv) % 3 for x in v)
    return None
points = sorted({normp(v) for v in product(F3, repeat=3) if any(v)})
detform = lambda v: (-v[0] * v[0] - v[1] * v[2]) % 3
conic = [v for v in points if detform(v) == 0]
def adj(g, v):
    X = (v[0], v[1], v[2], (-v[0]) % 3)
    Y = mmul(mmul(g, X), minv(g))
    return normp(to_vec(Y))
perm_images = Counter()
kernel = [g for g in GL if all(adj(g, v) == v for v in points)]
img = {tuple(adj(g, v) for v in points) for g in GL}
say(f"(c) PG(2,3) = P(sl2(F3)): {len(points)} points; absolute conic of det: {len(conic)} points {conic}")
say(f"    adjoint action of GL2(F3): kernel order {len(kernel)} (centre), image order {len(img)}; preserves the conic:",
    all(adj(g, v) in conic for g in GL for v in conic))
# kernel map: nilpotent X (rank 1) -> its kernel line in F3^2
def kerline(v):
    x, y, z = v
    # X = [[x, y], [z, -x]]; kernel vector w with X w = 0
    for w in [(1, 0), (0, 1), (1, 1), (1, 2)]:
        if (x * w[0] + y * w[1]) % 3 == 0 and (z * w[0] - x * w[1]) % 3 == 0: return w
def act2(g, w):
    r = ((g[0] * w[0] + g[1] * w[1]) % 3, (g[2] * w[0] + g[3] * w[1]) % 3)
    return normp(r + (0,))[:2] if r != (0, 0) else None
ok_eq = all(kerline(adj(g, v)) == act2(g, kerline(v)) for g in GL for v in conic)
say("    the kernel map conic -> P^1(F3) is a bijection:", len({kerline(v) for v in conic}) == 4,
    "and GL2(F3)-equivariant:", ok_eq)
# full orthogonal group check: matrices in PGL3(3) preserving the form up to scalar
def m3mul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) % 3 for j in range(3)) for i in range(3))
Q = ((2, 0, 0), (0, 0, 1), (0, 1, 0))  # Gram matrix of -x^2 - yz up to the factor 2: bilinear 2*(-x x' ) - (y z' + z y')
def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])) % 3
count = 0
for ent in product(F3, repeat=9):
    M = (ent[0:3], ent[3:6], ent[6:9])
    if det3(M) == 0: continue
    MT = tuple(tuple(M[j][i] for j in range(3)) for i in range(3))
    G = m3mul(m3mul(MT, Q), M)
    for lam in (1, 2):
        if G == tuple(tuple((lam * Q[i][j]) % 3 for j in range(3)) for i in range(3)):
            count += 1; break
say(f"    GO(3,3) (similitudes of the form) has {count} matrices; modulo scalars {count // 2} = |PGO3(3)| (S4 has 24)")

# (d) ------------------------------------------------------------------------------------------------------------------
def rank_mod(rows, p):
    M = [list(r) for r in rows]; rk = 0; ncol = len(M[0])
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] % p), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = pow(M[rk][c], p - 2, p)
        M[rk] = [(x * inv) % p for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] % p:
                f = M[i][c]; M[i] = [(x - f * y) % p for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk
n, D = 13, [0, 1, 3, 9]
lines13 = [[1 if (x - y) % 13 in D else 0 for x in range(13)] for y in range(13)]
say("(d) F3-rank of the PG(2,3) incidence matrix:", rank_mod(lines13, 3), "(QR code of length 13 has dimension 7)")
# polynomial arithmetic over F3: is every line polynomial divisible by g_N(x) = prod_{r nonresidue}(x - a^r) ?
# Build F27 = F3[t]/(t^3 - t - 1) (irreducible: no roots in F3), find a primitive 13th root of unity.
def f27_mul(a, b):
    # a, b as tuples (c0, c1, c2) of c0 + c1 t + c2 t^2 with t^3 = t + 1
    prod_ = [0] * 5
    for i in range(3):
        for j in range(3): prod_[i + j] += a[i] * b[j]
    for k in (4, 3):
        c = prod_[k]; prod_[k] = 0
        prod_[k - 2] += c; prod_[k - 3] += c       # t^k = t^{k-2} + t^{k-3}
    return tuple(x % 3 for x in prod_[:3])
def f27_pow(a, e):
    r = (1, 0, 0)
    while e:
        if e & 1: r = f27_mul(r, a)
        a = f27_mul(a, a); e >>= 1
    return r
elems = [e for e in product(F3, repeat=3) if any(e)]
gen = next(e for e in elems if all(f27_pow(e, 26 // q) != (1, 0, 0) for q in (2, 13)))
alpha = f27_pow(gen, 2)   # order 13
def f27_add(a, b): return tuple((x + y) % 3 for x, y in zip(a, b))
def evalp(coeffs, x):
    r = (0, 0, 0); pw = (1, 0, 0)
    for c in coeffs:
        r = f27_add(r, tuple((c * y) % 3 for y in pw)); pw = f27_mul(pw, x)
    return r
theta = [1 if k in D else 0 for k in range(13)]   # 1 + x + x^3 + x^9
zeros = [j for j in range(13) if evalp(theta, f27_pow(alpha, j)) == (0, 0, 0)]
qr13 = sorted({(k * k) % 13 for k in range(1, 13)})
say("    zeros alpha^j of theta(x) = 1 + x + x^3 + x^9:", zeros, "; quadratic residues mod 13:", qr13,
    "; nonresidues:", [j for j in range(1, 13) if j not in qr13])
say("    => the line code is the cyclic code with zero set =", "the NONRESIDUES" if sorted(zeros) == [j for j in range(1, 13) if j not in qr13]
    else ("the RESIDUES" if sorted(zeros) == qr13 else "neither: the zero set is the residue coset {1,3,9} plus the nonresidue coset {7,8,11}"))
# compare with the two ternary QR codes of length 13 (zeros = nonresidues, or residues): minimum weights
def cyclic_code_min_weight(zero_set):
    # generator g(x) = prod_{j in zero_set} (x - alpha^j) over F27, coefficients land in F3
    g = [(1, 0, 0)]
    for j in zero_set:
        a = f27_pow(alpha, j)
        neg_a = tuple((-c) % 3 for c in a)
        new = [(0, 0, 0)] * (len(g) + 1)
        for k, c in enumerate(g):
            new[k + 1] = f27_add(new[k + 1], c)
            new[k] = f27_add(new[k], f27_mul(c, neg_a))
        g = new
    assert all(c[1] == 0 and c[2] == 0 for c in g)
    gc = [c[0] for c in g]
    k = 13 - len(zero_set)
    rows = [[0] * i + gc + [0] * (13 - len(gc) - i) for i in range(k)]
    wts = Counter()
    for coeffs in product(F3, repeat=k):
        w = [sum(c * r[i] for c, r in zip(coeffs, rows)) % 3 for i in range(13)]
        wts[sum(1 for x in w if x)] += 1
    return min(wt for wt in wts if wt), sorted(wts.items())[:4]
nr13 = [j for j in range(1, 13) if j not in qr13]
say("    ternary QR codes of length 13: zeros = nonresidues ->", cyclic_code_min_weight(nr13), "; zeros = residues ->",
    cyclic_code_min_weight(qr13), "; the PG(2,3) line code ->", cyclic_code_min_weight(zeros))
say("    => the PG(2,3) line code [13,7,4] is not a quadratic-residue code (no multiplier maps its zero set to R or N)")
# minimum weight of the line code
basis = []
for r in lines13:
    if rank_mod(basis + [r], 3) > len(basis): basis.append(r)
words = Counter()
for coeffs in product(F3, repeat=len(basis)):
    w = [sum(c * b[i] for c, b in zip(coeffs, basis)) % 3 for i in range(13)]
    words[sum(1 for x in w if x)] += 1
say("    weight distribution of the [13,7] line code:", sorted(words.items()))
# ternary Golay as QR code of length 11
qr11 = sorted({(k * k) % 11 for k in range(1, 11)})
say("    ternary Golay = QR code of length 11 (3 is a square mod 11:", 3 in qr11, "); 3 is a square mod 13:", 3 in qr13)

# (e) ------------------------------------------------------------------------------------------------------------------
def isprime(m):
    return m > 1 and all(m % d for d in range(2, int(m ** 0.5) + 1))
def plane_size(m):
    # m = q^2 + q + 1 for a prime power q?
    for q in range(2, 100):
        if q * q + q + 1 == m:
            f = [p for p in range(2, q + 1) if q % p == 0 and isprime(p)]
            if len(f) == 1: return q
    return None
rows = []
for l0 in range(0, 13):
    right, wrong = 12 * l0 - 4 * 1 - 3 * (-1), -12 * l0 - 4 * 1 - 3 * (-1)
    R, W_ = abs(right), abs(wrong)
    rows.append((l0, right, wrong, right % 12, wrong % 12, R if isprime(R) else "-", W_ if isprime(W_) else "-",
                 plane_size(R), plane_size(W_)))
say("(e) 02L5: l0, right = 12 l0 - 1, wrong = -12 l0 - 1, residues mod 12, primes, plane orders q with |.| = q^2+q+1:")
for r in rows: say("   ", r)
say("    both residues are -1 mod 12 for every l0 (the class of W6 = r -> -r in (Z/12)^x);")
say("    |right| = 12 l0 - 1 and |wrong| = 12 l0 + 1 are -+1 mod 12, so chi_12 = +1 (3 is a square mod every prime among them);")
say("    plane sizes among |wrong|: only", [r[0] for r in rows if r[8]], "(l0 with 12 l0 + 1 = q^2+q+1);",
    "13 = PG(2,3) at l0 = 1, then 73 = PG(2,8) at l0 = 6, 133 = PG(2,11) at l0 = 11: the alignment does not persist")
qr_tern = [r[5] for r in rows if r[5] != "-"]
say("    primes 12 l0 - 1 (lengths of ternary QR codes on the right-gluing side):", qr_tern,
    "; perfect among them: only 11 (ternary Golay); binary-QR lengths (p = -+1 mod 8):", [p for p in qr_tern if p % 8 in (1, 7)])
with open(__file__.replace(".py", "_output.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
