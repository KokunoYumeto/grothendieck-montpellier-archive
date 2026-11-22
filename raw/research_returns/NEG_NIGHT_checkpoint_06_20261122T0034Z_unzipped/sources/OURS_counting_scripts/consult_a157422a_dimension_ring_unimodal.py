# Among the same-shape dimension rings, are there any whose structure constants are all unimodal?
# Run: python -I -B consult_a157422a_dimension_ring_unimodal.py
import contextlib, io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import consult_a157422a_dimension_ring_search as S
mul, add, to_q, ev, D, DD = S.mul, S.add, S.to_q, S.ev, S.D, S.DD

def unimodal(p):
    a = to_q(p)
    h = a[: len(a) // 2 + 1]
    return a == a[::-1] and min(a) >= 0 and all(h[i] <= h[i + 1] for i in range(len(h) - 1))

lin = [[w0, w1] for w1 in (1, 3, 5, 7, 9) for w0 in (0, 2, 4, 6)]
deltas = [d for d in ([b, a, 1] for a in (-3, -1, 1, 3, 5) for b in range(-16, 7, 2)) if S.ge_abs(d, S.dtrue)]
L1 = [l for l in ([l0, l1, l2] for l2 in (0, 2, 4, 6) for l1 in range(-9, 10, 2) for l0 in range(-8, 9, 2)) if S.ge_abs(l, S.l1true)]
L2 = [l for l in ([l0, l1, l2] for l2 in (1, 3, 5) for l1 in range(-12, 9, 2) for l0 in range(-8, 13, 2)) if S.ge_abs(l, S.l2true)]
with contextlib.redirect_stdout(io.StringIO()):
    found, _ = S.search(lin, deltas, [], [], limit=0)
base_ok = 0; good = []
for (W, U1, U2, d1, d2, G1, G2, Ssc) in found:
    base = [Ssc, G1, mul(D, G1), G2, mul(D, G2), W, mul(D, W), mul(DD, W), U1, mul(D, U1), U2, mul(D, U2), d1, mul(D, d1), d2, mul(D, d2)]
    if not all(unimodal(x) for x in base):
        continue
    base_ok += 1
    ok1 = None
    for La in L1:
        t = S.divexact(mul(mul(W, d1), S.sub(DD, La)), G2)
        if t is None: continue
        V1 = add(mul(D, U1), t)
        if S.ge_abs(V1, S.K1) and all(unimodal(x) for x in (V1, mul(D, V1), mul(d1, La), mul(D, mul(d1, La)))):
            ok1 = (La, V1); break
    if ok1 is None: continue
    for La in L2:
        t = S.divexact(mul(mul(W, d2), S.sub(DD, La)), G1)
        if t is None: continue
        V2 = add(mul(D, U2), t)
        if S.ge_abs(V2, S.K2) and all(unimodal(x) for x in (V2, mul(D, V2), mul(d2, La), mul(D, mul(d2, La)))):
            good.append((ev(Ssc, 4), W, U1, U2, d1, d2, G1, G2, Ssc, ok1[0], ok1[1], La, V2)); break
print("same-shape solutions of C0, C2-C5:", len(found), "; with unimodal W, U, delta, G, S:", base_ok,
      "; with every structure constant unimodal:", len(good))
good.sort()
names = ("W", "U1", "U2", "delta1", "delta2", "G1", "G2", "S", "Lambda1", "V1", "Lambda2", "V2")
for g in good[:2]:
    print({n: x for n, x in zip(names, g[1:])})
    print("  q-coefficients:", {n: to_q(x) for n, x in zip(names, g[1:]) if n in ("delta1", "delta2", "Lambda1", "Lambda2", "S")})
