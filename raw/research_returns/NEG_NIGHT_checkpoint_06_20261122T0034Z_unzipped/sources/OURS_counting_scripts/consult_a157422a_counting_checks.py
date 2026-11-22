# Checks for CONSULT_a157422a_COUNTING_CONSTRUCTION.md (Claude Fable 5.2 at effort max, 21 Nov 2026).
# Part 1: closed formulas for all structure constants of E^opp(3) against a8d75352's e3_constants.json.
# Run: python -I -B consult_a157422a_counting_checks.py
import json, os, itertools
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
v = sp.symbols("v")
D = (v + 1 / v) ** 2
lam = {1: D, 2: (D - 2) ** 2}
delta = {1: lam[1] - lam[2], 2: lam[2] - lam[1]}
WORDS = ["1", "12", "2", "21"]

def reduce_word(w):
    """P_w = D^alpha * lambda^beta * P_z in a two-dimensional block."""
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

def predicted():
    out = {}
    names = ["Sigma", "mu"] + ["g%d_%s" % (i, x) for i in (1, 2) for x in WORDS]
    for b in names:
        out[("mu", b, b)] = sp.Integer(1); out[(b, "mu", b)] = sp.Integer(1)
    out[("Sigma", "Sigma", "Sigma")] = D * (D ** 2 - lam[1]) * (D ** 2 - lam[2])
    for i in (1, 2):
        for x in WORDS:
            g = D ** len(x) * (D ** 2 - lam[3 - i])
            out[("Sigma", "g%d_%s" % (i, x), "Sigma")] = g
            out[("g%d_%s" % (i, x), "Sigma", "Sigma")] = g
    for i in (1, 2):
        for j in (1, 2):
            for x in WORDS:
                for y in WORDS:
                    if i != j:
                        out[("g%d_%s" % (i, x), "g%d_%s" % (j, y), "Sigma")] = D ** (len(x) + len(y) - 1)
                    else:
                        z, al, be = reduce_word(x + y)
                        out[("g%d_%s" % (i, x), "g%d_%s" % (i, y), "g%d_%s" % (i, z))] = delta[i] * D ** al * lam[i] ** be
                        K = 1 if be == 0 else D ** 2 + delta[i]
                        assert be in (0, 1)
                        out[("g%d_%s" % (i, x), "g%d_%s" % (i, y), "Sigma")] = D ** (len(z) + al - 1) * K
    return out

if __name__ == "__main__":
    data = json.load(open(os.path.join(HERE, "E4_scripts", "e3_constants.json")))
    pred = predicted()
    seen = set(); bad = 0
    for row in data:
        key = (row["b"], row["bp"], row["bpp"])
        seen.add(key)
        c = sp.sympify(row["c"], locals={"v": v})
        if key not in pred or sp.simplify(c - pred[key]) != 0:
            bad += 1
            if bad <= 5:
                print("MISMATCH", key, row["c"], pred.get(key))
    missing = [k for k in pred if k not in seen and sp.simplify(pred[k]) != 0]
    print("constants in the json:", len(data), "; predicted nonzero:", len(pred), "; mismatches:", bad, "; predicted but absent:", len(missing))
    for name, expr in (("D-1", D - 1), ("D-2", D - 2), ("5D-4", 5 * D - 4), ("2D^2-5D+4", 2 * D ** 2 - 5 * D + 4), ("(D-1)(D-4)", (D - 1) * (D - 4))):
        num = sp.Poly(sp.expand(expr * v ** 8), v)
        print(" ", name, "coefficients in q:", [c for c in num.all_coeffs() if True][::2] if False else sp.expand(expr))
