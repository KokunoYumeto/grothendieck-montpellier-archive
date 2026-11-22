"""Independent exact finite supplement for D-OL16--18.

No author checker or author output is imported.  Finite checks supplement,
and do not replace, the separately read universal proofs.  Natural dimension
8 below tests the matrix identities, not the theorem's dimension cutoff.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time

START = time.perf_counter()
STAMP = datetime.now(timezone.utc).isoformat()


def zero(n, m):
    return [[0] * m for _ in range(n)]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(x) for x in zip(*a)]


def add(a, b, q):
    return [[(x + y) % q for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, t, q):
    return [[t * x % q for x in row] for row in a]


def mul(a, b, q):
    return [[sum(x * y for x, y in zip(row, col)) % q for col in zip(*b)] for row in a]


def inverse(a, q):
    n = len(a)
    b = [row[:] + e for row, e in zip(a, eye(n))]
    for j in range(n):
        k = next(i for i in range(j, n) if b[i][j] % q)
        b[j], b[k] = b[k], b[j]
        b[j] = [x * pow(b[j][j], -1, q) % q for x in b[j]]
        for i in range(n):
            if i != j:
                t = b[i][j]
                b[i] = [(x - t * y) % q for x, y in zip(b[i], b[j])]
    return [row[n:] for row in b]


def rank(a, q):
    b = [row[:] for row in a]
    r = 0
    for j in range(len(b[0])):
        k = next((i for i in range(r, len(b)) if b[i][j] % q), None)
        if k is None:
            continue
        b[r], b[k] = b[k], b[r]
        b[r] = [x * pow(b[r][j], -1, q) % q for x in b[r]]
        for i in range(len(b)):
            if i != r:
                t = b[i][j]
                b[i] = [(x - t * y) % q for x, y in zip(b[i], b[r])]
        r += 1
    return r


def nullspace(a, q):
    b = [row[:] for row in a]
    pivots = []
    r = 0
    for j in range(len(b[0])):
        k = next((i for i in range(r, len(b)) if b[i][j] % q), None)
        if k is None:
            continue
        b[r], b[k] = b[k], b[r]
        b[r] = [x * pow(b[r][j], -1, q) % q for x in b[r]]
        for i in range(len(b)):
            if i != r:
                t = b[i][j]
                b[i] = [(x - t * y) % q for x, y in zip(b[i], b[r])]
        pivots.append(j)
        r += 1
    free = [j for j in range(len(b[0])) if j not in pivots]
    out = []
    for j in free:
        v = [0] * len(b[0])
        v[j] = 1
        for i, p in enumerate(pivots):
            v[p] = -b[i][j] % q
        out.append(v)
    return out


def blockdiag(*blocks):
    n = sum(len(a) for a in blocks)
    out = zero(n, n)
    at = 0
    for a in blocks:
        for i, row in enumerate(a):
            out[at+i][at:at+len(row)] = row
        at += len(a)
    return out


def reshape(v, n, m):
    return [v[m*i:m*(i+1)] for i in range(n)]


def flatten(a):
    return sum(a, [])


def linear_matrix(fn, n):
    return tr([fn([int(i == j) for i in range(n)]) for j in range(n)])


CASES = []
for q, c in [(5, 2), (7, 3)]:
    assert pow(c, (q-1)//2, q) == q-1
    for eps in [1, -1]:
        mu = eps*c % q
        a0 = [[0, c], [1, 0]]
        h0 = blockdiag(a0, a0)
        k = [[1, 0], [0, eps*c % q]]
        b0 = blockdiag(k, k)
        r = [[1, 1], [0, 1]]
        s = [[1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
        a = mul(mul(inverse(r, q), a0, q), r, q)
        h = mul(mul(inverse(s, q), h0, q), s, q)
        b = mul(mul(tr(s), b0, q), s, q)
        bi, hi, ai = inverse(b, q), inverse(h, q), inverse(a, q)
        assert mul(a, a, q) == scale(eye(2), c, q)
        assert mul(h, h, q) == scale(eye(4), c, q)
        assert mul(mul(tr(h), b, q), h, q) == scale(b, mu, q)
        gram = blockdiag(zero(2, 2), b, zero(2, 2))
        for i in range(2):
            gram[i][6+i] = gram[6+i][i] = 1
        big_h = blockdiag(a, h, scale(tr(ai), mu, q))
        assert mul(big_h, big_h, q) == scale(eye(8), c, q)
        assert mul(mul(tr(big_h), gram, q), big_h, q) == scale(gram, mu, q)

        def skew(z):
            return [[0, z % q], [-z % q, 0]]

        def unipotent(x, z):
            out = eye(8)
            right = add(skew(z), scale(mul(mul(x, bi, q), tr(x), q), -pow(2, -1, q), q), q)
            middle = scale(mul(bi, tr(x), q), -1, q)
            for i in range(2):
                out[i][2:6], out[i][6:8] = x[i][:], right[i][:]
            for i in range(4):
                out[2+i][6:8] = middle[i][:]
            return out

        def xaction(x):
            return mul(mul(a, x, q), hi, q)

        def yaction(y):
            return mul(mul(h, y, q), ai, q)

        xm = linear_matrix(lambda v: flatten(add(xaction(reshape(v, 2, 4)), scale(reshape(v, 2, 4), -1, q), q)), 8)
        ym = linear_matrix(lambda v: flatten(add(yaction(reshape(v, 4, 2)), scale(reshape(v, 4, 2), -1, q), q)), 8)
        xker, yker = nullspace(xm, q), nullspace(ym, q)
        assert len(xker) == len(yker) == 4
        rank2 = 0
        for coefficients in product(range(q), repeat=4):
            v = [sum(coefficients[j]*yker[j][i] for j in range(4)) % q for i in range(8)]
            y = reshape(v, 4, 2)
            assert yaction(y) == y
            if any(v):
                assert rank(y, q) == 2
                rank2 += 1
        assert rank2 == q**4-1
        center = scale(mul(mul(a, skew(1), q), tr(a), q), pow(mu, -1, q), q)
        assert center == skew(-eps)

        samples = [zero(2, 4)] + [reshape([int(i == j) for i in range(8)], 2, 4) for j in range(8)]
        samples += [reshape([(i*i+3*i+2) % q for i in range(8)], 2, 4)]
        laws = 0
        for ix, x in enumerate(samples):
            u = unipotent(x, ix)
            assert mul(mul(tr(u), gram, q), u, q) == gram
            assert mul(mul(big_h, u, q), inverse(big_h, q), q) == unipotent(xaction(x), -eps*ix)
            power = eye(8)
            for _ in range(q):
                power = mul(power, u, q)
            assert power == eye(8)
            for iy, y in enumerate(samples):
                central = scale(add(mul(mul(y, bi, q), tr(x), q), scale(mul(mul(x, bi, q), tr(y), q), -1, q), q), pow(2, -1, q), q)
                assert central[0][0] == central[1][1] == 0 and (central[0][1]+central[1][0]) % q == 0
                assert mul(u, unipotent(y, iy), q) == unipotent(add(x, y, q), ix+iy+central[0][1])
                laws += 1
        CASES.append({"q": q, "nonsquare_c": c, "epsilon": eps, "natural_dimension": 8,
                      "nondiagonal_gram": b, "fixed_X_dimension": len(xker), "fixed_Y_dimension": len(yker),
                      "all_nonzero_fixed_Y_rank_two": rank2, "sampled_exact_group_laws": laws,
                      "sampled_isometry_transport_exponent": len(samples), "center_scalar": -eps % q})

CARRIERS = []
for q in [5, 7]:
    signs = (1, 1, -1, -1)
    labels = [(tuple(int(i == j) for i in range(4)), (0,)*4) for j in range(4)]
    labels += [((0,)*4, tuple(int(i == j) for i in range(4))) for j in range(4)]
    labels += [((1, 2, 1, 3), (2, 1, 4, 1))]
    def parity(v):
        return tuple(s*x % q for s, x in zip(signs, v))
    checks, trace = 0, 0
    for x in product(range(q), repeat=4):
        trace += int(parity(x) == x)
        for a, b in labels:
            # Xi L_(a,b) Xi^-1 versus L_(Xi a,Xi b), recording exact roots-of-unity exponents.
            left_target = parity(tuple((t+y) % q for t, y in zip(parity(x), a)))
            right_target = tuple((t+y) % q for t, y in zip(x, parity(a)))
            left_exp = sum(v*(t+pow(2, -1, q)*y) for v, t, y in zip(b, parity(x), a)) % q
            right_exp = sum(v*(t+pow(2, -1, q)*y) for v, t, y in zip(parity(b), x, parity(a))) % q
            assert (left_target, left_exp) == (right_target, right_exp)
            checks += 1
    assert trace == q**2 and trace**2 == q**4
    CARRIERS.append({"q": q, "carrier_dimension": q**4, "trace": trace,
                     "trace_squared": trace**2, "exact_basis_generator_and_dense_label_checks": checks})

beta = F(1, 6)-F(1, 10000)
delta = (1-F(19, 20)**9)/2
assert F(1, 6) < delta < F(3, 16) < F(7, 32)
assert 13*beta-2 > F(1, 7)
assert 11*beta+delta-2 > F(1, 60)
assert 2*beta*(1-beta) > F(1, 4) > delta
endpoints = {}
for q in [3, 5, 7, 9, 11, 13]:
    for n in range(20, 62, 2):
        denominator = 1-F(1, q**(n//2-1))-F(1, q**(n-1))
        rank2_bound = (F(1, q*q)+F(1, q**(n//2-1)))/denominator
        rank1_bound = (F(1, q)+F(1, q**(n//2-1)))/denominator
        assert rank2_bound < F(1, 8)
        assert rank1_bound < (1-4*beta if q == 3 else F(1, 4))
        assert 4*F(1, q**(n-3)) < F(1, 8)
        assert q**(n-1)-q**(n//2)-1 > F(q**(n-1), 2)
        assert q**(n-2)-q**(n//2)-q > F(q**(n-2), 2)
        assert (1-F(1, q**(n//2)))/2 > F(7, 16)
        if n == 20:
            endpoints[str(q)] = {"rank_one": str(rank1_bound), "rank_two": str(rank2_bound)}

ROOT = Path(__file__).resolve().parent
PROOF = ROOT.parent.parent / "imprimitive/orthogonal_lowlevels/orthogonal_even_odd_section.tex"
assert hashlib.sha256(PROOF.read_bytes()).hexdigest() == "897ea4b9995e0668b4487cefeacd366645e67fe4509afe0a23b692c33418892a"
result = {"result": "PASS", "started_utc": STAMP, "elapsed_seconds": time.perf_counter()-START,
          "proof_sha256": hashlib.sha256(PROOF.read_bytes()).hexdigest(),
          "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "cases": CASES, "carrier_cases": CARRIERS,
          "beta": str(beta), "delta": str(delta), "fraction_bounds_at_N20": endpoints,
          "inequality_grid_size": 6*21,
          "scope": "Finite matrix identities in natural dimension8 and exact constant checks only; universal group generation, orbit bounds, all normalizers and source exclusion checked separately as proofs."}
(ROOT / "independent_check.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
