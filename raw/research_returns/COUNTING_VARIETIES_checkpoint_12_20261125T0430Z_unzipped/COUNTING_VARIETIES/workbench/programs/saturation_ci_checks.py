"""Original finite checks of the new bounded-gap/colon algorithm.

The proof in sections/saturation_ci.tex was written before this program.
All six examples use a nonreduced regular sublist (w^2,E), with
K=(wx,wy,wz,w^2,E), K^sat=(w,E), e=B=1.
The ordinary and supersingular cubics below are smooth over the
algebraic closure: for odd p their affine cubic h is squarefree, and
the characteristic-two cases have no simultaneous projective zero
of the equation and its three partial derivatives.
"""
import itertools
import json


def mons(d, n=4):
    if d < 0:
        return []
    if n == 1:
        return [(d,)]
    return [(i,) + tail for i in range(d + 1) for tail in mons(d - i, n - 1)]


def add(a, b, p):
    out = dict(a)
    for u, v in b.items():
        out[u] = (out.get(u, 0) + v) % p
    return {u: v for u, v in out.items() if v}


def mul(a, b, p):
    out = {}
    for u, v in a.items():
        for w, z in b.items():
            t = tuple(x + y for x, y in zip(u, w))
            out[t] = (out.get(t, 0) + v * z) % p
    return {u: v for u, v in out.items() if v}


def power(a, n, p):
    out = {(0, 0, 0, 0): 1}
    for _ in range(n):
        out = mul(out, a, p)
    return out


def degree(a):
    return sum(next(iter(a)))


def rref(rows, width, p):
    a = [[v % p for v in row] for row in rows]
    pivots = []
    at = 0
    for col in range(width):
        hit = next((j for j in range(at, len(a)) if a[j][col]), None)
        if hit is None:
            continue
        a[at], a[hit] = a[hit], a[at]
        inv = pow(a[at][col], -1, p)
        a[at] = [v * inv % p for v in a[at]]
        for j in range(len(a)):
            if j != at and a[j][col]:
                t = a[j][col]
                a[j] = [(x - t * y) % p for x, y in zip(a[j], a[at])]
        pivots.append(col)
        at += 1
        if at == len(a):
            break
    return a[:at], pivots


def nullspace(rows, width, p):
    reduced, pivots = rref(rows, width, p)
    out = []
    for free in range(width):
        if free in pivots:
            continue
        v = [0] * width
        v[free] = 1
        for row, pivot in zip(reduced, pivots):
            v[pivot] = -row[free] % p
        out.append(v)
    return out


def recover_q(inputs, selected, e, p):
    qm = mons(e)
    columns = []
    for u in qm:
        col = {}
        for i, f in enumerate(inputs):
            for w, z in mul({u: 1}, f, p).items():
                col[i, w] = z
        columns.append(col)
    for i, f in enumerate(inputs):
        for g in selected:
            d = e + degree(f) - degree(g)
            for u in mons(d):
                columns.append({(i, w): -z % p for w, z in mul({u: 1}, g, p).items()})
    keys = sorted(set().union(*(set(col) for col in columns)))
    rows = [[col.get(key, 0) for col in columns] for key in keys]
    kernel = nullspace(rows, len(columns), p)
    projected = [v[:len(qm)] for v in kernel]
    _, piv = rref(projected, len(qm), p)
    assert len(piv) == 1, ("annihilator dimension", p, len(piv))
    v = next(v for v in projected if any(v))
    q = {u: z for u, z in zip(qm, v) if z}
    return q, {"equations": len(rows), "unknowns": len(columns), "annihilator_dimension": 1}


def trace(a, p):
    out = {}
    for u, v in a.items():
        if all(t % p == p - 1 for t in u):
            w = tuple((t - p + 1) // p for t in u)
            out[w] = (out.get(w, 0) + v) % p
    return {u: v for u, v in out.items() if v}


def evaluate(a, point, p):
    return sum(v * product(pow(x, k, p) for x, k in zip(point, u)) for u, v in a.items()) % p


def product(xs):
    out = 1
    for x in xs:
        out *= x
    return out


def cubic(p, ordinary):
    if p == 2:
        terms = (
            {(0, 2, 1, 0): 1, (1, 1, 1, 0): 1, (3, 0, 0, 0): 1, (0, 0, 3, 0): 1}
            if ordinary else
            {(0, 2, 1, 0): 1, (0, 1, 2, 0): 1, (3, 0, 0, 0): 1,
             (1, 0, 2, 0): 1, (0, 0, 3, 0): 1}
        )
    elif ordinary:
        terms = {(0, 2, 1, 0): 1, (3, 0, 0, 0): -1,
                 (2, 0, 1, 0): -1, (0, 0, 3, 0): -1}
    elif p == 3:
        terms = {(0, 2, 1, 0): 1, (3, 0, 0, 0): -1,
                 (1, 0, 2, 0): -1, (0, 0, 3, 0): -1}
    else:
        terms = {(0, 2, 1, 0): 1, (3, 0, 0, 0): -1, (0, 0, 3, 0): -1}
    return {u: v % p for u, v in terms.items() if v % p}


records = []
for p, ordinary in itertools.product((2, 3, 5), (False, True)):
    w = {(0, 0, 0, 1): 1}
    variables = [{tuple(int(i == j) for i in range(4)): 1} for j in range(4)]
    E = cubic(p, ordinary)
    ww = power(w, 2, p)
    inputs = [mul(w, x, p) for x in variables] + [E]
    selected = [ww, E]
    q, stats = recover_q(inputs, selected, 1, p)
    assert set(q) == {(0, 0, 0, 1)}
    r = trace(mul(q, power(mul(ww, E, p), p - 1, p), p), p)
    alpha = power(mul(w, E, p), p - 1, p).get((p - 1,) * 4, 0)
    assert r == {u: alpha * v % p for u, v in q.items() if alpha * v % p}
    points = 1 + sum(evaluate(E, (x, y, 1, 0), p) == 0 for x in range(p) for y in range(p))
    assert alpha == (1 - points) % p
    assert (alpha != 0) == ordinary
    records.append({"p": p, "ordinary": ordinary, "Y_nonreduced": True,
                    "q": str(q), "alpha": alpha, "rational_points_on_X": points, **stats})
print(json.dumps({"status": "passed", "cases": records}, indent=2))
