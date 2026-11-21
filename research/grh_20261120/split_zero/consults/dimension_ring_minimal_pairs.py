"""Which dimension ring?  For every solution of Fable's search window (consult_a157422a_dimension_ring_search.py),
with every admissible Lambda1/Lambda2 (not only the first), count the cancelling pairs 1 + eps the ring needs:
excess = sum over all structure constants and q-exponents of (d - |c|)/2, in total and in the bottom cell (target Sigma).
Integer-polynomial arithmetic only (the table of consult_a157422a_dimension_ring_verify.py, rebuilt on lists in D).
Main session, Claude Opus 5.5 at effort max, 21 Nov 2026 ~19:5x UTC.  Run: python -I -B dimension_ring_minimal_pairs.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
import consult_a157422a_dimension_ring_search as S

WORDS = ["1", "12", "2", "21"]


def reduce_word(w):  # as in the verify script
    alpha = beta = 0
    w = list(w)
    changed = True
    while changed:
        changed = False
        for i in range(len(w) - 1):
            if w[i] == w[i + 1]:
                del w[i]; alpha += 1; changed = True; break
        if not changed and len(w) >= 3:
            del w[0:2]; beta += 1; changed = True
    return "".join(w), alpha, beta


def Dpow(k):
    return [0] * k + [1]


def pw(p, k):
    out = [1]
    for _ in range(k):
        out = S.mul(out, p)
    return out


def table(par):
    """structure constants as integer lists in D (lowest degree first), keyed (b, b', b'')."""
    c = {}
    c[("Sigma", "Sigma", "Sigma")] = par["S"]
    for i in (1, 2):
        for x in WORDS:
            g = S.mul(Dpow(len(x) - 1), par["G"][i])
            c[("Sigma", "g%d_%s" % (i, x), "Sigma")] = g
            c[("g%d_%s" % (i, x), "Sigma", "Sigma")] = g
    for i in (1, 2):
        for j in (1, 2):
            for x in WORDS:
                for y in WORDS:
                    bx, by = "g%d_%s" % (i, x), "g%d_%s" % (j, y)
                    if i != j:
                        c[(bx, by, "Sigma")] = S.mul(Dpow(len(x) + len(y) - 2), par["W"])
                    else:
                        z, al, be = reduce_word(x + y)
                        m = S.mul(S.mul(par["delta"][i], Dpow(al)), pw(par["Lam"][i], be))
                        c[(bx, by, "g%d_%s" % (i, z))] = m
                        num = S.sub(S.mul(Dpow(len(x) + len(y) - 2), S.mul(par["G"][i], par["G"][i])),
                                    S.mul(S.mul(m, Dpow(len(z) - 1)), par["G"][i]))
                        kap = S.divexact(num, par["S"])
                        assert kap is not None
                        c[(bx, by, "Sigma")] = kap
    return {k: S.trim(v) for k, v in c.items() if S.trim(v)}


TRUE = {"S": S.s0, "G": {1: S.g1, 2: S.g2}, "W": S.D,
        "delta": {1: S.mul([-1], S.dtrue), 2: S.dtrue}, "Lam": {1: S.l1true, 2: S.l2true}}
TRUEq = {k: S.to_q(v) for k, v in table(TRUE).items()}


def unimodal(a):
    a = list(a)
    while a and a[0] == 0: a.pop(0)
    while a and a[-1] == 0: a.pop()
    i = 0
    while i + 1 < len(a) and a[i] <= a[i + 1]: i += 1
    while i + 1 < len(a) and a[i] >= a[i + 1]: i += 1
    return (i == len(a) - 1) if a else True


def score(par):
    d = table(par)
    tot = bottom = 0
    uni = True
    for key in set(d) | set(TRUEq):
        dq = S.to_q(d[key]) if key in d else [0]
        cq = TRUEq.get(key, [0])
        n = max(len(dq), len(cq))
        dq, cq = S.pad(dq, n), S.pad(cq, n)
        if any(x < abs(y) or (x - y) % 2 for x, y in zip(dq, cq)):
            return None
        ex = sum(x - abs(y) for x, y in zip(dq, cq)) // 2
        tot += ex
        if key[2] == "Sigma":
            bottom += ex
        if key in d and not unimodal(dq):
            uni = False
    return tot, bottom, uni


if __name__ == "__main__":
    lin = [[w0, w1] for w1 in (1, 3, 5, 7, 9) for w0 in (0, 2, 4, 6)]
    deltas = [dd for dd in ([b, a, 1] for a in (-3, -1, 1, 3, 5) for b in range(-16, 7, 2)) if S.ge_abs(dd, S.dtrue)]
    L1 = [l for l in ([l0, l1, l2] for l2 in (0, 2, 4, 6) for l1 in range(-9, 10, 2) for l0 in range(-8, 9, 2))
          if S.ge_abs(l, S.l1true)]
    L2 = [l for l in ([l0, l1, l2] for l2 in (1, 3, 5) for l1 in range(-12, 9, 2) for l0 in range(-8, 13, 2))
          if S.ge_abs(l, S.l2true)]
    found, full = S.search(lin, deltas, L1, L2, limit=0)
    results = []
    for (W, U1, U2, d1, d2, G1, G2, Ssc) in found:
        ok1 = [La for La in L1 if (lambda t: t is not None and S.ge_abs(S.add(S.mul(S.D, U1), t), S.K1))(
            S.divexact(S.mul(S.mul(W, d1), S.sub(S.DD, La)), G2))]
        ok2 = [La for La in L2 if (lambda t: t is not None and S.ge_abs(S.add(S.mul(S.D, U2), t), S.K2))(
            S.divexact(S.mul(S.mul(W, d2), S.sub(S.DD, La)), G1))]
        for La1 in ok1:
            for La2 in ok2:
                par = {"S": Ssc, "G": {1: G1, 2: G2}, "W": W, "delta": {1: d1, 2: d2}, "Lam": {1: La1, 2: La2}}
                try:
                    sc = score(par)
                except AssertionError:
                    continue
                if sc is not None:
                    results.append(sc + ((tuple(W), tuple(U1), tuple(U2), tuple(d1), tuple(d2), tuple(La1), tuple(La2)),))
    print("dimension rings scored (every admissible Lambda pair):", len(results))
    results.sort(key=lambda r: (r[0], r[1]))
    m = results[0][0]
    mins = [r for r in results if r[0] == m]
    print("minimal total number of cancelling pairs:", m, "; attained by", len(mins), "ring(s)")
    for r in mins[:8]:
        print("   total %d, bottom %d, unimodal %s, (W, U1, U2, delta1, delta2, Lambda1, Lambda2) = %s" % r)
    uni = [r for r in results if r[2]]
    if uni:
        mu = uni[0][0]
        umins = [r for r in uni if r[0] == mu]
        print("unimodal rings:", len(uni), "; minimal pairs among them:", mu, "; attained by", len(umins))
        for r in umins[:8]:
            print("   total %d, bottom %d, unimodal %s, %s" % r)
    mb = min(r[1] for r in results)
    print("minimal bottom-cell pairs:", mb, "; attained by", sum(1 for r in results if r[1] == mb))
