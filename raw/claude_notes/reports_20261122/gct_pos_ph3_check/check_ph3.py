"""Independent checks of GCT_POS K-023, R-NEW-004, K-024 and PNEW-013's inputs, and of P-F30 in small rank.

Main session e0d20ada (Claude Opus 5.5 at effort max), 22 Nov 2026. Written from the statements; imports nothing from the run
or from the intake agent's scripts. Reads nothing, writes nothing. Memory: a few hundred MB (a non-critical calculation).

A  k_n(s) by S_d characters; the cyclic trace by S_d characters at cubes; b_n(s) by the Weyl alternant on a weight DP.
B  the gl_n stabilizer of z_n: rank of the action matrix on associative words (mod a prime; full rank there implies over Q).
C  the support theorem by exhaustion over every independent set of hook weights, n <= 6.
D  the residue formula: n = 2, 3 exactly; n = 4, 5 against the run's n = 4, 5 tensor residues modulo 3.
"""
import cmath
import collections
import functools
import itertools
import math
import sys
import time
from fractions import Fraction

import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
T0 = time.time()


def say(*a):
    print("[%6.1fs]" % (time.time() - T0), *a, flush=True)


# ---------- A ----------
def partitions(d, top=None):
    if d == 0:
        yield ()
        return
    for k in range(min(d, top or d), 0, -1):
        for rest in partitions(d - k, k):
            yield (k,) + rest


@functools.lru_cache(maxsize=None)
def chi(beta, mu):
    if not mu:
        return 1
    r = mu[0]
    have, total = set(beta), 0
    for b in beta:
        c = b - r
        if c >= 0 and c not in have:
            sign = (-1) ** sum(1 for x in beta if c < x < b)
            total += sign * chi(tuple(sorted((have - {b}) | {c}, reverse=True)), mu[1:])
    return total


def z(mu):
    out = 1
    for j, m in collections.Counter(mu).items():
        out *= j ** m * math.factorial(m)
    return out


def cube(mu):
    out = []
    for j in mu:
        out += [j // 3] * 3 if j % 3 == 0 else [j]
    return tuple(sorted(out, reverse=True))


def kron_and_trace(n, s):
    d = n * s
    beta = tuple(s + n - 1 - i for i in range(n))
    fd = math.factorial(d)
    k = tr = 0
    for mu in partitions(d):
        size = fd // z(mu)
        k += size * chi(beta, mu) ** 3
        tr += size * chi(beta, cube(mu))
    assert k % fd == 0 and tr % fd == 0
    return k // fd, tr // fd


def hook_weights(n, with_mult):
    """the weights of W + S_(2,1)W"""
    out = [tuple(int(a == i) for a in range(n)) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                out.append(tuple(2 * int(a == i) + int(a == j) for a in range(n)))
    for t in itertools.combinations(range(n), 3):
        w = tuple(int(a in t) for a in range(n))
        out += [w, w] if with_mult else [w]
    return out


def b_value(n, s):
    top = s + n - 1
    c = np.zeros((top + 1,) * n, dtype=np.int64)
    c[(0,) * n] = 1
    for w in hook_weights(n, True):
        p = next(i for i in range(n) if w[i])
        for v in range(w[p], top + 1):
            to = [slice(w[i], None) for i in range(n)]
            fro = [slice(0, top + 1 - w[i]) for i in range(n)]
            to[p], fro[p] = v, v - w[p]
            c[tuple(to)] += c[tuple(fro)]
    delta = [n - 1 - i for i in range(n)]
    total = 0
    for perm in itertools.permutations(range(n)):
        a = tuple(s + delta[perm[i]] - delta[i] for i in range(n))
        if min(a) < 0:
            continue
        inv = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        total += (-1) ** inv * int(c[a])
    return total


def part_a():
    cases = {2: 12, 3: 8, 4: 6, 5: 4, 6: 4, 7: 3}
    bad = total = 0
    for n, smax in cases.items():
        row_k, row_b = [], []
        for s in range(1, smax + 1):
            k, tr = kron_and_trace(n, s)
            b = b_value(n, s)
            total += 1
            bad += not (tr == b and (k - b) % 3 == 0 and k >= b)
            row_k.append(k)
            row_b.append(b)
        say("A n=%d s=1..%d k=%s b=%s" % (n, smax, row_k, row_b))
    say("A RESULT cases=%d failures=%d" % (total, bad))


# ---------- B ----------
P = 1000003


def rank_mod(m):
    m = m % P
    r = 0
    for col in range(m.shape[1]):
        hit = np.nonzero(m[r:, col])[0]
        if not len(hit):
            continue
        q = r + int(hit[0])
        m[[r, q]] = m[[q, r]]
        m[r] = m[r] * pow(int(m[r, col]), -1, P) % P
        rest = r + 1 + np.nonzero(m[r + 1:, col])[0]
        if len(rest):
            m[rest] = (m[rest] - m[rest, col][:, None] * m[r]) % P
        r += 1
        if r == m.shape[0]:
            break
    return r


def part_b():
    bad = 0
    for n in range(2, 15):
        words = collections.Counter()
        for i in range(n - 1):
            j = i + 1
            words[(i, i, j)] += 1
            words[(i, j, i)] -= 2
            words[(j, i, i)] += 1
        rows = collections.defaultdict(lambda: collections.Counter())
        for a in range(n):
            rows[("W", a)][a * n + n - 1] += 1  # E_ab sends e_b to e_a
        for word, coef in words.items():
            for pos in range(3):
                b = word[pos]
                for a in range(n):
                    rows[word[:pos] + (a,) + word[pos + 1:]][a * n + b] += coef
        m = np.zeros((len(rows), n * n), dtype=np.int64)
        for i, row in enumerate(rows.values()):
            for col, v in row.items():
                m[i, col] = v
        bad += rank_mod(m) != n * n
    say("B RESULT n=2..14 rank deficiencies=%d" % bad)


# ---------- C ----------
def two_part(x):
    x = np.abs(x)
    return x & -x


def is_chain(cols, n):
    linear = [c.index(1) for c in cols if sum(c) == 1]
    edges = {c.index(1): c.index(2) for c in cols if sum(c) == 3 and max(c) == 2}
    if len(cols) != n or len(linear) != 1 or len(edges) != n - 1:
        return False
    at, seen = linear[0], {linear[0]}
    while at in edges:
        at = edges[at]
        if at in seen:
            return False
        seen.add(at)
    return len(seen) == n


def part_c():
    for n in range(2, 7):
        ws = hook_weights(n, False)
        col = np.array(ws, dtype=np.float64).T
        M = 2 ** (n - 1)
        best, top, tested = 0, [], 0
        for r in range(1, n + 1):
            it = itertools.combinations(range(len(ws)), r)
            while True:
                chunk = np.fromiter(itertools.chain.from_iterable(itertools.islice(it, 200000)), dtype=np.int16)
                if not len(chunk):
                    break
                chunk = chunk.reshape(-1, r)
                tested += len(chunk)
                K = col[:, chunk].transpose(1, 0, 2)
                gram = np.matmul(K.transpose(0, 2, 1), K)
                det = np.rint(np.linalg.det(gram))
                ok = det > 0.5  # independent columns
                if not ok.any():
                    continue
                K, gram, det, chunk = K[ok], gram[ok], det[ok], chunk[ok]
                rhs = K.sum(axis=1)[..., None]
                c = np.linalg.solve(gram, rhs)
                inside = (np.abs(np.matmul(K, c)[..., 0] - 1) < 1e-7).all(axis=1)
                if not inside.any():
                    continue
                det, c, chunk = det[inside], c[inside, :, 0], chunk[inside]
                y = det[:, None] * c
                assert np.abs(y - np.rint(y)).max() < 1e-3
                g = det.astype(np.int64)
                for i in range(r):
                    g = np.gcd(g, np.rint(y[:, i]).astype(np.int64))
                order = two_part(det.astype(np.int64) // g)  # two-part of the order of (1,...,1) modulo the support lattice
                here = int(order.max())
                if here > best:
                    best, top = here, []
                if here == best:
                    top += [[ws[i] for i in row] for row in chunk[order == best]]
        wt = [(-2) ** i % M for i in range(n - 1)] + [0]
        fixed = sum(1 for w in hook_weights(n, True) if sum(a * b for a, b in zip(w, wt)) % M == 0)
        say("C n=%d subsets=%d max two-part=%d (claim %d) maximizers=%d (n!=%d) all chains=%s fixed weights of g=%d"
            % (n, tested, best, M, len(top), math.factorial(n), all(is_chain(t, n) for t in top), fixed))


# ---------- D ----------
def residue(n, one, root, mul, inv, sub):
    M = 2 ** (n - 1)
    w = [(-2) ** i % M for i in range(n - 1)] + [0]
    num, den = one, one
    for i in range(n):
        for j in range(n):
            if i != j:
                num = mul(num, sub(one, root((w[i] - w[j]) % M)))
    for wt in hook_weights(n, True):
        e = sum(a * b for a, b in zip(wt, w)) % M
        if e:
            den = mul(den, sub(one, root(e)))
    return mul(num, inv(den)), sum(w) % M


def part_d():
    for n, exact in ((2, lambda x: 1 + 0j), (3, lambda x: 1 / ((1 - x ** 2) * (1 - x ** 3)))):
        M = 2 ** (n - 1)
        got, S = residue(n, 1 + 0j, lambda e: cmath.exp(2j * cmath.pi * e / M), lambda a, b: a * b, lambda a: 1 / a,
                         lambda a, b: a - b)
        xi = cmath.exp(2j * cmath.pi * S / M)
        say("D n=%d exact-series residue agrees: %s" % (n, abs(got - exact(xi)) < 1e-9))

    claims = {4: ([14, -10, 0, 10], 256), 5: ([78, 446, -211, -301, -301, -211, 446, 78], 32768)}
    for n, (num, den) in claims.items():
        M, h = 2 ** (n - 1), 2 ** (n - 2)

        def root(e):
            v = [0] * h
            e %= M
            v[e % h] = 1 if e < h else 2
            return tuple(v)

        def sub(a, b):
            return tuple((x - y) % 3 for x, y in zip(a, b))

        def mul(a, b):
            v = [0] * h
            for i, x in enumerate(a):
                for j, y in enumerate(b):
                    if i + j < h:
                        v[i + j] += x * y
                    else:
                        v[i + j - h] -= x * y  # x^h = -1
            return tuple(x % 3 for x in v)

        one = root(0)

        def inv(a):
            e = (8 if n == 4 else 80) - 1
            out = one
            while e:
                if e & 1:
                    out = mul(out, a)
                a = mul(a, a)
                e >>= 1
            return out

        got, S = residue(n, one, root, mul, inv, sub)
        scale = pow(den, -1, 3)
        hits = []
        for a in range(1, M, 2):
            v = [0] * h
            for i, x in enumerate(num):
                for j, y in enumerate(root(i * a)):
                    v[j] = (v[j] + scale * x * y) % 3
            if tuple(v) == got:
                hits.append(a)
        say("D n=%d C mod 3=%s at xi=zeta^%d; the run's tensor residue congruent under zeta->zeta^a for a=%s"
            % (n, got, S, hits))


if __name__ == "__main__":
    part_a()
    chi.cache_clear()
    part_b()
    part_d()
    part_c()
    say("DONE")
