"""Computation for RESEARCH_SA20 B.022: the node sequence a_n of its proof on R = F_q + t^m F_q[[t]].
Checks, for prime q, small m and n <= N, exhaustively over x in R mod t^M:
  (1) v(d_n) = sum_{i<n} v(a_n - a_i) equals m*floor(n/q) + sum_{j>=2} floor(n/q^j);
  (2) sum_{i<n} v(x - a_i) >= v(d_n) for every x in R (so b_n maps R into V), with equality at x = a_n.
Claude Opus 5.5 at effort max, acf08879a01b97ed4, full intake round 3, 22 Nov 2026."""
import itertools, sys

def digits(n, q):
    d = []
    while n:
        d.append(n % q); n //= q
    return d or [0]

def node(n, q, m, M):
    # a_n = c_{n_0} + sum_{j>=1} c_{n_j} t^{m+j-1}, with c_i = i in F_q (q prime); coefficient vector mod t^M
    v = [0] * M
    ds = digits(n, q)
    v[0] = ds[0] % q
    for j in range(1, len(ds)):
        e = m + j - 1
        if e < M: v[e] = (v[e] + ds[j]) % q
    return tuple(v)

def val(a, b, q, M):
    for e in range(M):
        if (a[e] - b[e]) % q: return e
    return M  # lower bound

def run(q, m, M, N):
    nodes = [node(n, q, m, M) for n in range(N + 1)]
    assert len(set(nodes)) == N + 1
    # all x in R mod t^M: constant c in F_q, coefficients t^1..t^{m-1} zero, t^m..t^{M-1} free
    free = list(range(m, M))
    ok1 = ok2 = True; worst = None
    for n in range(1, N + 1):
        vd = sum(val(nodes[n], nodes[i], q, M) for i in range(n))
        formula = m * (n // q) + sum(n // q ** j for j in range(2, 40))
        if vd != formula: ok1 = False; worst = ("formula", n, vd, formula)
    for c in range(q):
        for tail in itertools.product(range(q), repeat=len(free)):
            x = [0] * M; x[0] = c
            for e, t in zip(free, tail): x[e] = t
            x = tuple(x)
            s = 0
            for n in range(1, N + 1):
                s += val(x, nodes[n - 1], q, M)
                vd = m * (n // q) + sum(n // q ** j for j in range(2, 40))
                if s < vd: ok2 = False; worst = ("bound", n, x, s, vd)
    print("q=%d m=%d M=%d N=%d: valuation formula for v(d_n): %s; sum v(x-a_i) >= v(d_n) for all %d x in R mod t^M: %s %s"
          % (q, m, M, N, ok1, q * q ** len(free), ok2, worst or ""))

for args in [(2, 2, 11, 40), (2, 3, 11, 40), (3, 1, 7, 30), (3, 2, 7, 30), (2, 1, 11, 40)]:
    run(*args)
