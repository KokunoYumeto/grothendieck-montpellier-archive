# Search for a dimension ring for (H-check_3, E^opp(3)): CONSULT_a157422a_COUNTING_CONSTRUCTION.md, section 3.
# Same-shape symmetric ansatz; unknowns are polynomials in D with integer coefficients (lists, lowest degree first).
# Run: python -I -B consult_a157422a_dimension_ring_search.py
from fractions import Fraction
from math import comb


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def add(p, r):
    n = max(len(p), len(r))
    return trim([(p[i] if i < len(p) else 0) + (r[i] if i < len(r) else 0) for i in range(n)])


def sub(p, r):
    n = max(len(p), len(r))
    return trim([(p[i] if i < len(p) else 0) - (r[i] if i < len(r) else 0) for i in range(n)])


def mul(p, r):
    if not p or not r:
        return []
    out = [0] * (len(p) + len(r) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(r):
                out[i + j] += a * b
    return trim(out)


def ev(p, x):
    s = 0
    for c in reversed(p):
        s = s * x + c
    return s


def divexact(p, r):
    """p / r in Z[D], or None."""
    p = [Fraction(c) for c in trim(p)]
    r = trim(r)
    if not r:
        return None
    if not p:
        return []
    if len(p) < len(r):
        return None
    out = [Fraction(0)] * (len(p) - len(r) + 1)
    for k in range(len(p) - len(r), -1, -1):
        c = p[k + len(r) - 1] / r[-1]
        out[k] = c
        for j, b in enumerate(r):
            p[k + j] -= c * b
    if any(p):
        return None
    if any(c.denominator != 1 for c in out):
        return None
    return trim([int(c) for c in out])


def to_q(p):
    """coefficients in q of a polynomial in D = q + 2 + 1/q, centred."""
    p = trim(p)
    if not p:
        return [0]
    n = len(p) - 1
    out = [0] * (2 * n + 1)
    for k, c in enumerate(p):
        for j in range(-k, k + 1):
            out[j + n] += c * comb(2 * k, k + j)
    return out


def pad(a, n):
    k = (n - len(a)) // 2
    return [0] * k + a + [0] * k


def ge_abs(p, r):
    """p >= |r| coefficientwise in q, and p = r mod 2."""
    a, b = to_q(p), to_q(r)
    n = max(len(a), len(b))
    a, b = pad(a, n), pad(b, n)
    return all(x >= abs(y) and (x - y) % 2 == 0 for x, y in zip(a, b))


D = [0, 1]
Dm1 = [-1, 1]
DD = [0, 0, 1]
g1 = mul([0, 4], Dm1)                 # 4D(D-1)
g2 = mul([0, 0, 1], Dm1)              # D^2(D-1)
s0 = mul([0, 0, 4], mul(Dm1, Dm1))    # 4D^2(D-1)^2
dtrue = mul(Dm1, [-4, 1])             # (D-1)(D-4)
K1 = [-4, 5]
K2 = [4, -5, 2]
l1true = D
l2true = mul([-2, 1], [-2, 1])


def search(lin, deltas, L1, L2, limit=5):
    found = []
    for W in lin:
        WW = mul(W, W)
        for U1 in lin:
            for U2 in lin:
                Den = sub(WW, mul(U1, U2))
                if not Den:
                    continue
                e7, e11 = ev(Den, 7), ev(Den, 11)
                if e7 <= 0 or e11 <= 0:
                    continue
                for d1 in deltas:
                    for d2 in deltas:
                        N1 = mul(mul(D, W), add(mul(W, d1), mul(U1, d2)))
                        N2 = mul(mul(D, W), add(mul(W, d2), mul(U2, d1)))
                        if ev(N1, 7) % e7 or ev(N2, 7) % e7 or ev(N1, 11) % e11 or ev(N2, 11) % e11:
                            continue
                        G1 = divexact(N1, Den)
                        if G1 is None:
                            continue
                        G2 = divexact(N2, Den)
                        if G2 is None:
                            continue
                        if not (ge_abs(G1, g1) and ge_abs(G2, g2)):
                            continue
                        S = divexact(mul(G1, G2), W)
                        if S is None or not ge_abs(S, s0):
                            continue
                        found.append((W, U1, U2, d1, d2, G1, G2, S))
    print("solutions of C0, C2-C5:", len(found))
    full = []
    for (W, U1, U2, d1, d2, G1, G2, S) in found:
        ok1 = None
        for La in L1:
            t = divexact(mul(mul(W, d1), sub(DD, La)), G2)
            if t is None:
                continue
            V1 = add(mul(D, U1), t)
            if ge_abs(V1, K1):
                ok1 = (La, V1)
                break
        if ok1 is None:
            continue
        for La in L2:
            t = divexact(mul(mul(W, d2), sub(DD, La)), G1)
            if t is None:
                continue
            V2 = add(mul(D, U2), t)
            if ge_abs(V2, K2):
                full.append((W, U1, U2, d1, d2, G1, G2, S, ok1, (La, V2)))
                break
    print("solutions of all conditions C0-C6:", len(full))
    names = ("W", "U1", "U2", "delta1", "delta2", "G1", "G2", "S")
    for sol in full[:limit]:
        print({n: x for n, x in zip(names, sol[:8])}, "Lambda1,V1:", sol[8], "Lambda2,V2:", sol[9])
    return found, full


if __name__ == "__main__":
    lin = [[w0, w1] for w1 in (1, 3, 5, 7, 9) for w0 in (0, 2, 4, 6)]
    deltas = [d for d in ([b, a, 1] for a in (-3, -1, 1, 3, 5) for b in range(-16, 7, 2)) if ge_abs(d, dtrue)]
    L1 = [l for l in ([l0, l1, l2] for l2 in (0, 2, 4, 6) for l1 in range(-9, 10, 2) for l0 in range(-8, 9, 2))
          if ge_abs(l, l1true)]
    L2 = [l for l in ([l0, l1, l2] for l2 in (1, 3, 5) for l1 in range(-12, 9, 2) for l0 in range(-8, 13, 2))
          if ge_abs(l, l2true)]
    print("candidates: linear", len(lin), "; deltas", len(deltas), "; Lambda1", len(L1), "; Lambda2", len(L2))
    search(lin, deltas, L1, L2)
