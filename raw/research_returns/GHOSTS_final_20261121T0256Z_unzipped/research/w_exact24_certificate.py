#!/usr/bin/env python3
"""Exact, self-contained certificate for W04: c_C(e_W[Gamma_1]) = 24.

Run with Python 3.10 or later; no third-party modules or input files are used:
    python w_exact24_certificate.py

Mathematical completeness is proved in W01--W04 of the accompanying paper.
This file performs only finite integer arithmetic.  It checks the upper
certificate and exhausts the abelian-cycle classes allowed by that reduction.
It regenerates its catalog in memory, without loading any binary cache.

Conventions: E = C/(Z+Z*omega), omega^2+omega+1=0; coordinates (u_i,v_i)
give the integral H^1 basis, in that order.  A pair (a,b) denotes a+b*omega.
H^4 has its 70 increasing exterior basis vectors.  Surface degree is theta^2
intersection, without a factorial.  Translates have identical classes.

Every encoded equality is an exact equality of all 70 integer coefficients:
the program proves a coefficient bound strictly below the base before using
the encoding.  There are no floating-point calculations or probabilistic
hashes.  Python sets compare the full exact integers even if hashes collide.
Expected memory is several hundred MB; the full run may take a few minutes.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, product


# Eisenstein arithmetic.
def ka(x, y):
    return x[0] + y[0], x[1] + y[1]


def kn(x):
    return -x[0], -x[1]


def km(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def bar(x):
    return x[0] - x[1], -x[1]


def norm(x):
    return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]


def det(h):
    return ka(km(h[0], h[3]), kn(km(h[1], h[2])))


# Integral exterior algebra, represented by dictionaries indexed by tuples.
def add(*xs):
    d = {}
    for x in xs:
        for a, v in x.items():
            d[a] = d.get(a, 0) + v
    return {a: v for a, v in d.items() if v}


def scale(c, x):
    return {a: c * v for a, v in x.items() if c * v}


def wedge(x, y):
    d = {}
    for a, c in x.items():
        for b, e in y.items():
            if set(a) & set(b):
                continue
            k = tuple(sorted(a + b))
            sign = (-1) ** sum(i > j for i in a for j in b)
            d[k] = d.get(k, 0) + sign * c * e
    return {a: v for a, v in d.items() if v}


def form(i):
    return {(i,): 1}


def cmforms(q, k):
    a, b = q
    u, v = form(2 * k), form(2 * k + 1)
    return (add(scale(a, u), scale(-b, v)),
            add(scale(b, u), scale(a - b, v)))


BASIS = list(combinations(range(8), 4))
TOP = tuple(range(8))
BASE = 1001
WEIGHTS = [BASE ** i for i in range(70)]
ZERO = (0, 0)
ONE = (1, 0)
OMEGA = (0, 1)
UNITS = [q for q in product(range(-1, 2), repeat=2) if norm(q) == 1]


def vector(x):
    return tuple(x.get(b, 0) for b in BASIS)


def as_form(v):
    return {b: c for b, c in zip(BASIS, v) if c}


def encode(v):
    return sum(a * w for a, w in zip(v, WEIGHTS))


def va(x, y):
    return tuple(a + b for a, b in zip(x, y))


def vs(x, y):
    return tuple(a - b for a, b in zip(x, y))


def graph(h, inputs=(0, 1)):
    """Class of x_outputs = h*x_inputs, with outputs in increasing order."""
    outputs = [j for j in range(4) if j not in inputs]
    z = {(): 1}
    for row, k in enumerate(outputs):
        pu, pv = {}, {}
        for col, i in enumerate(inputs):
            u, v = cmforms(h[2 * row + col], i)
            pu, pv = add(pu, u), add(pv, v)
        z = wedge(z, add(form(2 * k), scale(-1, pu)))
        z = wedge(z, add(form(2 * k + 1), scale(-1, pv)))
    return vector(z)


THETA = add(*(wedge(form(2 * k), form(2 * k + 1)) for k in range(4)))
THETA2 = wedge(THETA, THETA)


def degree(v):
    return wedge(THETA2, as_form(v)).get(TOP, 0)


def pullback_diagonal(v, entries):
    images = []
    for k, a in enumerate(entries):
        images.extend(cmforms(a, k))
    out = {}
    for b, c in zip(BASIS, v):
        term = {(): c}
        for i in b:
            term = wedge(term, images[i])
        out = add(out, term)
    return vector(out)


def cross_divisor(a, i, j):
    # D_ij(a) = [x_j=a*x_i] - theta_i - theta_j, for norm(a)=1.
    u, v = cmforms(a, i)
    return add(wedge(add(form(2 * j), scale(-1, u)),
                     add(form(2 * j + 1), scale(-1, v))),
               scale(-1, wedge(form(2 * i), form(2 * i + 1))),
               scale(-1, wedge(form(2 * j), form(2 * j + 1))))


P, Q = cross_divisor(ONE, 0, 2), cross_divisor(OMEGA, 0, 2)
U, V = cross_divisor(ONE, 1, 3), cross_divisor(OMEGA, 1, 3)
Q_FORM = add(wedge(P, U), scale(-1, wedge(P, V)),
             scale(-1, wedge(Q, U)), scale(-2, wedge(Q, V)))
Q_VECTOR = vector(Q_FORM)  # q = 3w.
Q_CODE = encode(Q_VECTOR)


def check_target_and_upper_bound():
    identity = graph((ONE, ZERO, ZERO, ONE))
    r_entries = (OMEGA, OMEGA, bar(OMEGA), bar(OMEGA))
    r = pullback_diagonal(identity, r_entries)
    r2 = pullback_diagonal(r, r_entries)
    basic = tuple(2 * a - b - c for a, b, c in zip(identity, r, r2))
    s = (1, 2)  # sqrt(-3) = 1+2*omega.
    sbasic = pullback_diagonal(basic, (s, s, bar(s), bar(s)))
    # P06: 54 e_W = (9+S)(2-R-R^2), hence 18q = that operator on Gamma_1.
    assert tuple(9 * a + b for a, b in zip(basic, sbasic)) == tuple(18 * x for x in Q_VECTOR)
    assert wedge(Q_FORM, Q_FORM).get(TOP, 0) == 18
    assert degree(Q_VECTOR) == 0
    assert max(map(abs, Q_VECTOR)) == 2
    assert pullback_diagonal(Q_VECTOR, ((-1, 0), ONE, ONE, ONE)) == tuple(-x for x in Q_VECTOR)

    def z(a, b):
        return graph((a, ZERO, ZERO, b))

    # Written with -omega=(0,-1), -omega^2=(1,1).
    positives = [z(ONE, (0, -1)), z(ONE, (1, 1)), z(OMEGA, (-1, 0))]
    negatives = [z((0, -1), (0, -1)), z((1, 1), (-1, 0)), z((1, 1), (1, 1))]
    assert all(degree(v) == 8 for v in positives + negatives)
    difference = tuple(sum(v[i] for v in positives) - sum(v[i] for v in negatives)
                       for i in range(70))
    assert difference == Q_VECTOR
    print('Target q=3w: projector identity, square 18, degree zero verified.', flush=True)
    print('Upper certificate: multiplier 3, positive/negative degrees 24/24; all 70 coordinates verified.', flush=True)


def surface_z(h, inputs):
    rows = [None] * 4
    rows[inputs[0]], rows[inputs[1]] = (ONE, ZERO), (ZERO, ONE)
    for row, k in enumerate([j for j in range(4) if j not in inputs]):
        rows[k] = h[2 * row], h[2 * row + 1]
    return km(det(rows[0] + rows[1]), bar(det(rows[2] + rows[3])))


def zero_catalog():
    """All zero-Weil irreducible abelian surface classes of degree <=14."""
    entries = [q for q in product(range(-2, 3), repeat=2) if norm(q) <= 5]
    small_h = []
    for h in product(entries, repeat=4):
        t = sum(map(norm, h))
        if t > 6:
            continue
        d = 2 * (1 + t + norm(det(h)))
        if d <= 14:
            small_h.append((d, h))
    zeros = {}
    for inputs in combinations(range(4), 2):
        for d, h in small_h:
            if surface_z(h, inputs) == ZERO:
                v = graph(h, inputs)
                assert degree(v) == d
                zeros[v] = d, ('coordinate_graph', inputs, h)

    # W03 exceptions with no unit coordinate-pair minor.  The curve has
    # parametrization x_j=a*t, x_k=b*t, with norms {3,4}.  Coprimality gives
    # the exact defining equation b*x_j-a*x_k=0, with connected kernel.
    norm3 = [q for q in product(range(-2, 3), repeat=2) if norm(q) == 3]
    norm4 = [q for q in product(range(-2, 3), repeat=2) if norm(q) == 4]
    for free in range(4):
        for j, k in combinations([i for i in range(4) if i != free], 2):
            fixed = next(i for i in range(4) if i not in (free, j, k))
            for aa, bb in product(norm3, norm4):
                for a, b in ((aa, bb), (bb, aa)):
                    bu, bv = cmforms(b, j)
                    au, av = cmforms(a, k)
                    curve = wedge(add(bu, scale(-1, au)), add(bv, scale(-1, av)))
                    cl = wedge(curve, wedge(form(2 * fixed), form(2 * fixed + 1)))
                    v = vector(cl)
                    assert degree(v) == 14
                    zeros[v] = 14, ('two_minor', free, j, k, a, b)
    counts = Counter(x[0] for x in zeros.values())
    assert dict(counts) == {2: 6, 4: 72, 6: 288, 8: 180, 10: 1440, 12: 864, 14: 1440}
    print('Zero-Weil abelian surface counts:', sorted(counts.items()), flush=True)
    return zeros


def zero_cycle_classes(zeros):
    """Exact unbounded-knapsack enumeration of all such cycles to degree14."""
    groups = {d: sorted({encode(v) for v, (degree_, _) in zeros.items() if degree_ == 2 * d})
              for d in range(1, 8)}
    dp = {0: {0}, **{d: set() for d in range(1, 8)}}
    for d in range(1, 8):
        sums = {0: {0}}
        for k in range(1, 7 // d + 1):
            sums[k] = {sum(xs) for xs in combinations_with_replacement(groups[d], k)}
        old = dp
        dp = {n: set(old[n]) for n in range(8)}
        for n in range(1, 8):
            for k in range(1, n // d + 1):
                dp[n].update(a + b for a in old[n - k * d] for b in sums[k])
        print('After zero-generator degree', 2 * d, ':', [len(dp[n]) for n in range(8)], flush=True)
    assert [len(dp[n]) for n in range(8)] == [1, 6, 93, 776, 6066, 48564, 322050, 2162952]
    return dp


PERM = [4, 5, 6, 7, 0, 1, 2, 3]
TRANS = []
for b in BASIS:
    bb = tuple(PERM[i] for i in b)
    TRANS.append((BASIS.index(tuple(sorted(bb))),
                  (-1) ** sum(bb[i] > bb[j] for i in range(4) for j in range(i + 1, 4))))


def transpose(v):
    out = [0] * 70
    for c, (j, sign) in zip(v, TRANS):
        out[j] = sign * c
    return tuple(out)


PLUS_Z = {(2, 0), (1, -1), (2, 1)}
MINUS_Z = {(a - 3, b) for a, b in PLUS_Z}


def weil_catalog():
    # Period values of at most two unit graphs or one norm3/norm4 graph.
    possible = {q for q in product(range(-3, 4), repeat=2) if norm(q) in (0, 1, 3, 4)}
    feasible_plus = {q for q in possible if (q[0] - 3, q[1]) in possible}
    assert feasible_plus == {(1, 0), (2, 0), (1, -1), (2, 1)}
    # The involution [-1] on the first E sends q to -q; swapping the
    # numerators changes feasible plus value1 to value2.  Other values stay.
    assert {((3 - a), -b) for a, b in feasible_plus} == feasible_plus
    entries = [z for z in product(range(-3, 4), repeat=2) if norm(z) <= 9]
    graphs, seen = [], set()

    def insert(d, z, v, name, isogeny_degree):
        if v in seen:
            return
        seen.add(v)
        assert degree(v) == d
        graphs.append((d, z, encode(v), v, name, isogeny_degree))

    for h in product(entries, repeat=4):
        t = sum(map(norm, h))
        if t > 9:
            continue
        determinant = det(h)
        isogeny_degree = norm(determinant)
        if isogeny_degree not in (1, 3, 4) or t + isogeny_degree > 10:
            continue
        d = 2 * (1 + isogeny_degree + t)
        z = bar(determinant)
        if isogeny_degree == 1:
            # Two-component mains use only degree<=14.  A single unit
            # graph can contribute only the retained negative period -1.
            if d > 14 and z != (-1, 0):
                continue
        elif z not in PLUS_Z | MINUS_Z and bar(z) not in PLUS_Z | MINUS_Z:
            continue
        v = graph(h)
        insert(d, z, v, ('graph', h), isogeny_degree)
        if isogeny_degree > 1:
            insert(d, bar(z), transpose(v), ('transpose_graph', h), isogeny_degree)
    print('Weil graph counts (degree, isogeny degree):', sorted(Counter((g[0], g[5]) for g in graphs).items()), flush=True)
    return graphs


def compare(zeros, dp, graphs):
    # A cycle of degree<=22 has at most11 irreducible components, counting
    # multiplicity, since every surface degree is at least2.  The difference
    # of two such cycles minus q therefore has every coefficient bounded by
    # 2*11*M + max|q_i|.  If its encoding is zero, its lowest coefficient is
    # a multiple of BASE of smaller absolute value, hence zero; repeat for
    # each coefficient.  This proves injectivity on every comparison made.
    m = max(max(abs(x) for v in zeros for x in v),
            max(abs(x) for g in graphs for x in g[3]))
    bound = 2 * 11 * m + max(map(abs, Q_VECTOR))
    assert bound == 156 and bound < BASE
    print('Exact encoding: M =', m, ', coefficient bound =', bound, '< base', BASE, flush=True)
    autos = [i for i, g in enumerate(graphs) if g[5] == 1 and g[0] <= 14]
    pairs = defaultdict(list)
    for ai, i in enumerate(autos):
        for j in autos[ai:]:
            d = graphs[i][0] + graphs[j][0]
            if d > 22:
                continue
            z = ka(graphs[i][1], graphs[j][1])
            kind = 'plus' if z in PLUS_Z else 'minus' if z in MINUS_Z else None
            if kind:
                pairs[d, kind].append((graphs[i][2] + graphs[j][2], i, j))
    single_plus = [i for i, g in enumerate(graphs) if g[5] > 1 and g[1] in PLUS_Z]
    single_minus = [i for i, g in enumerate(graphs) if g[1] in MINUS_Z]
    print('Pair groups:', sorted((k, len(v)) for k, v in pairs.items()), flush=True)
    print('Single plus/minus:', len(single_plus), len(single_minus), flush=True)
    generators = [(d // 2, encode(v), name, v) for v, (d, name) in zeros.items()]

    def reconstruct_extra(code, n):
        out = []
        while n:
            for d, c, name, v in generators:
                if d <= n and code - c in dp[n - d]:
                    out.append((2 * d, name, v))
                    code, n = code - c, n - d
                    break
            else:
                raise AssertionError('zero-cycle reconstruction failed')
        assert code == 0
        return out

    def find_positive(code, d):
        for (main_d, kind), pp in pairs.items():
            if kind != 'plus' or main_d > d:
                continue
            n = (d - main_d) // 2
            for pc, i, j in pp:
                if code - pc in dp[n]:
                    return [i, j], reconstruct_extra(code - pc, n)
        for i in single_plus:
            g = graphs[i]
            if g[0] <= d and code - g[2] in dp[(d - g[0]) // 2]:
                return [i], reconstruct_extra(code - g[2], (d - g[0]) // 2)
        raise AssertionError('positive reconstruction failed')

    def full_vector(main, extras):
        v = (0,) * 70
        for i in main:
            v = va(v, graphs[i][3])
        for _, _, x in extras:
            v = va(v, x)
        return v

    def report_unexpected_equality(code, d, minus_main, minus_extra):
        plus_main, plus_extra = find_positive(code, d)
        assert vs(full_vector(plus_main, plus_extra), full_vector(minus_main, minus_extra)) == Q_VECTOR
        print('UNEXPECTED EXACT EQUALITY AT DEGREE', d, flush=True)
        print('PLUS', [graphs[i][4] for i in plus_main], plus_extra, flush=True)
        print('MINUS', [graphs[i][4] for i in minus_main], minus_extra, flush=True)
        raise AssertionError('The proposed lower bound has been disproved in all 70 coordinates.')

    expected = {16: (750, 193344), 18: (14364, 1544688),
                20: (184902, 11659752), 22: (1898952, 79234032)}
    for d in (16, 18, 20, 22):
        positive = set()
        for (main_d, kind), pp in pairs.items():
            if kind != 'plus' or main_d > d:
                continue
            n = (d - main_d) // 2
            for pc, _, _ in pp:
                positive.update(pc + e for e in dp[n])
        for i in single_plus:
            g = graphs[i]
            if g[0] <= d:
                positive.update(g[2] + e for e in dp[(d - g[0]) // 2])
        print('Degree', d, 'positive classes', len(positive), flush=True)
        checked = 0
        for (main_d, kind), pp in pairs.items():
            if kind != 'minus' or main_d > d:
                continue
            n = (d - main_d) // 2
            for pc, i, j in pp:
                for e in dp[n]:
                    checked += 1
                    if pc + e + Q_CODE in positive:
                        report_unexpected_equality(pc + e + Q_CODE, d, [i, j], reconstruct_extra(e, n))
        for i in single_minus:
            g = graphs[i]
            if g[0] > d:
                continue
            n = (d - g[0]) // 2
            for e in dp[n]:
                checked += 1
                if g[2] + e + Q_CODE in positive:
                    report_unexpected_equality(g[2] + e + Q_CODE, d, [i], reconstruct_extra(e, n))
        assert (len(positive), checked) == expected[d]
        print('No equality at degree', d, '; negative candidates checked', checked, flush=True)
    print('PASS W04: no certificate of cost below24; the degree24 upper certificate is exact.', flush=True)


if __name__ == '__main__':
    check_target_and_upper_bound()
    zero_surfaces = zero_catalog()
    zero_cycles = zero_cycle_classes(zero_surfaces)
    weil_surfaces = weil_catalog()
    compare(zero_surfaces, zero_cycles, weil_surfaces)
