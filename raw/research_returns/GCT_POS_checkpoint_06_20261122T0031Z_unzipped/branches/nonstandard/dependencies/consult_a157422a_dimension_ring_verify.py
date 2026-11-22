# Verify a dimension ring for (H-check_3, E^opp(3)): CONSULT_a157422a_COUNTING_CONSTRUCTION.md, section 3.
# Builds the ten-dimensional algebra at epsilon = +1 from a solution of C0-C6, then checks, for all 1000 triples:
#   nonnegativity in q, domination d >= |c|, congruence d = c mod 2, and associativity.
# Run: python -I -B consult_a157422a_dimension_ring_verify.py
import itertools
import os
import sys
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script folder from the path
import consult_a157422a_dimension_ring_search as S

Dsym = sp.symbols("D")
q = sp.symbols("q")
WORDS = ["1", "12", "2", "21"]


def P(lst):
    return sp.Poly(sum(c * Dsym ** k for k, c in enumerate(lst)), Dsym)


def reduce_word(w):
    alpha = beta = 0
    w = list(w)
    changed = True
    while changed:
        changed = False
        for i in range(len(w) - 1):
            if w[i] == w[i + 1]:
                del w[i]
                alpha += 1
                changed = True
                break
        if not changed and len(w) >= 3:
            del w[0:2]
            beta += 1
            changed = True
    return "".join(w), alpha, beta


def table(par):
    """structure constants as sympy expressions in D; par has D-polynomials G[i], Ssc, delta[i], Lam[i], W."""
    names = ["mu", "Sigma"] + ["g%d_%s" % (i, x) for i in (1, 2) for x in WORDS]
    c = {}
    for b in names:
        c[("mu", b, b)] = sp.Integer(1)
        c[(b, "mu", b)] = sp.Integer(1)
    c[("Sigma", "Sigma", "Sigma")] = par["S"]
    for i in (1, 2):
        for x in WORDS:
            g = Dsym ** (len(x) - 1) * par["G"][i]
            c[("Sigma", "g%d_%s" % (i, x), "Sigma")] = g
            c[("g%d_%s" % (i, x), "Sigma", "Sigma")] = g
    for i in (1, 2):
        for j in (1, 2):
            for x in WORDS:
                for y in WORDS:
                    bx, by = "g%d_%s" % (i, x), "g%d_%s" % (j, y)
                    if i != j:
                        c[(bx, by, "Sigma")] = Dsym ** (len(x) + len(y) - 2) * par["W"]
                    else:
                        z, al, be = reduce_word(x + y)
                        m = par["delta"][i] * Dsym ** al * par["Lam"][i] ** be
                        c[(bx, by, "g%d_%s" % (i, z))] = m
                        num = Dsym ** (len(x) + len(y) - 2) * par["G"][i] ** 2 - m * Dsym ** (len(z) - 1) * par["G"][i]
                        kap, rem = sp.div(sp.Poly(sp.expand(num), Dsym), sp.Poly(sp.expand(par["S"]), Dsym))
                        assert rem.is_zero, (bx, by)
                        c[(bx, by, "Sigma")] = kap.as_expr()
    return names, {k: sp.expand(val) for k, val in c.items() if sp.expand(val) != 0}


def qcoeffs(expr):
    e = sp.expand(sp.expand(expr).subs(Dsym, q + 2 + 1 / q))
    e = sp.Poly(sp.expand(e * q ** 40), q)
    return {m[0] - 40: int(cf) for m, cf in e.terms()}


TRUE = {"S": 4 * Dsym ** 2 * (Dsym - 1) ** 2, "G": {1: 4 * Dsym * (Dsym - 1), 2: Dsym ** 2 * (Dsym - 1)}, "W": Dsym,
        "delta": {1: -(Dsym - 1) * (Dsym - 4), 2: (Dsym - 1) * (Dsym - 4)}, "Lam": {1: Dsym, 2: (Dsym - 2) ** 2}}


def check(par, label):
    names, d = table(par)
    _, c = table(TRUE)
    bad_pos = bad_dom = bad_par = 0
    for key in set(d) | set(c):
        dq = qcoeffs(d.get(key, 0))
        cq = qcoeffs(c.get(key, 0))
        for e in set(dq) | set(cq):
            x, y = dq.get(e, 0), cq.get(e, 0)
            bad_pos += x < 0
            bad_dom += x < abs(y)
            bad_par += (x - y) % 2 != 0
    # associativity
    def mult(u, w):
        out = {}
        for (a, ca) in u.items():
            for (b, cb) in w.items():
                for z in names:
                    k = d.get((a, b, z))
                    if k is not None:
                        out[z] = out.get(z, 0) + ca * cb * k
        return out
    bad_assoc = 0
    for a, b, e in itertools.product(names, repeat=3):
        l = mult(mult({a: 1}, {b: 1}), {e: 1})
        r = mult({a: 1}, mult({b: 1}, {e: 1}))
        for z in names:
            if sp.expand(l.get(z, 0) - r.get(z, 0)) != 0:
                bad_assoc += 1
    print(label, ": nonzero constants", len(d), "(true:", len(c), "); negative coefficients", bad_pos,
          "; domination failures", bad_dom, "; parity failures", bad_par, "; associativity failures", bad_assoc)
    return d


if __name__ == "__main__":
    check(TRUE, "H-check_3 itself (control: negative coefficients expected, the rest 0)")
    lin = [[w0, w1] for w1 in (1, 3, 5, 7, 9) for w0 in (0, 2, 4, 6)]
    deltas = [dd for dd in ([b, a, 1] for a in (-3, -1, 1, 3, 5) for b in range(-16, 7, 2)) if S.ge_abs(dd, S.dtrue)]
    L1 = [l for l in ([l0, l1, l2] for l2 in (0, 2, 4, 6) for l1 in range(-9, 10, 2) for l0 in range(-8, 9, 2))
          if S.ge_abs(l, S.l1true)]
    L2 = [l for l in ([l0, l1, l2] for l2 in (1, 3, 5) for l1 in range(-12, 9, 2) for l0 in range(-8, 13, 2))
          if S.ge_abs(l, S.l2true)]
    found, full = S.search(lin, deltas, L1, L2, limit=0)
    full.sort(key=lambda s: S.ev(s[7], 4))
    best = full[0]
    W, U1, U2, d1, d2, G1, G2, Ssc, (La1, V1), (La2, V2) = best
    print("smallest solution by S at q = 1:")
    for n, x in (("W", W), ("U1", U1), ("U2", U2), ("delta1", d1), ("delta2", d2), ("G1", G1), ("G2", G2), ("S", Ssc),
                 ("Lambda1", La1), ("V1", V1), ("Lambda2", La2), ("V2", V2)):
        print("  ", n, "=", sp.factor(P(x).as_expr()), "  q-coefficients", S.to_q(x))
    par = {"S": P(Ssc).as_expr(), "G": {1: P(G1).as_expr(), 2: P(G2).as_expr()}, "W": P(W).as_expr(),
           "delta": {1: P(d1).as_expr(), 2: P(d2).as_expr()}, "Lam": {1: P(La1).as_expr(), 2: P(La2).as_expr()}}
    check(par, "dimension ring")
