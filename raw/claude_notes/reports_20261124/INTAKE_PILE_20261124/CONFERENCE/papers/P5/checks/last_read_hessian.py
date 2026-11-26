"""The rank <= 2 locus of the Hessian of the chain cubic, n = 4 and 5, by Groebner bases in every affine chart.

Conference convener ae84c4aa (Claude Fable 5.2 at effort max), 25 Nov 2026; independent of p5_check_hessian.py.
Claim of Prop 6.1(2): the projective locus is [e_1], [e_n] and [a e_(n-1) + e_n] with a^2 = 3.
"""
import itertools
import sys

import sympy as sp

sys.stdout.reconfigure(encoding="utf-8")
ALL = True
for n in (4, 5):
    x = sp.symbols("x1:%d" % (n + 1))
    F = sum(x[i] ** 2 * x[i + 1] for i in range(n - 1)) + x[n - 1] ** 3
    H = sp.hessian(F, x) / 2
    # the tridiagonal shape stated in the paper
    diag = [x[i + 1] for i in range(n - 1)] + [3 * x[n - 1]]
    shape = all(sp.expand(H[i, i] - diag[i]) == 0 for i in range(n)) and \
        all(sp.expand(H[i, i + 1] - x[i]) == 0 for i in range(n - 1)) and \
        all(H[i, j] == 0 for i in range(n) for j in range(n) if abs(i - j) > 1)
    minors = []
    for rows in itertools.combinations(range(n), 3):
        for cols in itertools.combinations(range(n), 3):
            m = sp.expand(H.extract(list(rows), list(cols)).det())
            if m != 0:
                minors.append(m)
    points = set()
    for c in range(n):                      # chart x_c = 1 and x_i = 0 for i < c: every projective point once
        subs = {x[i]: 0 for i in range(c)}
        subs[x[c]] = 1
        eqs = [sp.expand(m.subs(subs)) for m in minors]
        eqs = [e for e in eqs if e != 0]
        free = [x[i] for i in range(c + 1, n)]
        if not free:
            if not eqs:
                points.add(tuple([0] * c + [1]))
            continue
        if any(e.is_number and e != 0 for e in eqs):
            continue
        G = sp.groebner(eqs, *free, order="lex")
        if G.exprs == [1]:
            continue
        sols = sp.solve(list(G.exprs), free, dict=True)
        for s in sols:
            if any(v not in s for v in free):
                points.add(("positive-dimensional component in chart", c))
                continue
            points.add(tuple([0] * c + [1] + [sp.nsimplify(s[v]) for v in free]))
    r3 = sp.sqrt(3)
    expected = {tuple([1] + [0] * (n - 1)), tuple([0] * (n - 1) + [1]),
                tuple([0] * (n - 2) + [1, 1 / r3]), tuple([0] * (n - 2) + [1, -1 / r3])}
    same = {tuple(sp.simplify(v) for v in p) for p in points} == {tuple(sp.simplify(v) for v in p) for p in expected}
    ranks = [H.subs(dict(zip(x, p))).rank() for p in expected]
    ok = shape and same and all(r <= 2 for r in ranks)
    ALL = ALL and ok
    print("n = %d: tridiagonal shape %s; %d nonzero 3x3 minors; rank<=2 points found: %s; ranks at the four points %s; %s"
          % (n, shape, len(minors), sorted(points, key=str), ranks, "as claimed" if ok else "DIFFERENT"))
print("ALL AS CLAIMED" if ALL else "SOME CHECK FAILED")
