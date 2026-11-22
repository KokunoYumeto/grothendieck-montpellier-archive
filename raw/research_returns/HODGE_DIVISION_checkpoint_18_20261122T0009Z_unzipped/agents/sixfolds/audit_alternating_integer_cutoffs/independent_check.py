"""Independent exact reconstruction of HD-ALT09, with no author imports."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from math import factorial, prod
import hashlib
import json
import time

START = time.perf_counter()
HERE = Path(__file__).resolve().parent
WORK = HERE.parents[2]
PROOF = WORK / "research/alternating_remaining_integer_cutoffs_section.tex"
EXPECTED = "6f45816c177be7398add519ed47bc679a81b65839eb6d6e1f777f2976e1505be"
assert hashlib.sha256(PROOF.read_bytes()).hexdigest() == EXPECTED


def clean(a):
    a = list(map(Q, a))
    while len(a) > 1 and not a[-1]:
        a.pop()
    return tuple(a)


def add(a, b):
    return clean([(a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))])


def scale(a, c):
    return clean([c*x for x in a])


def mul(a, b):
    c = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return clean(c)


def sub(a, b):
    return add(a, scale(b, -1))


def compose(a, b):
    c = (Q(0),)
    for x in reversed(a):
        c = add(mul(c, b), (x,))
    return c


def F(n, m):
    first = mul(scale(mul(n, sub(n, (3,))), 5),
                sub(scale(mul(m, sub(n, (4,))), 3),
                    mul(sub(n, (1,)), sub(n, (2,)))))
    return sub(first, scale(mul(m, mul(sub(n, (1,)), sub(n, (2,)))), 6))


x = (0, 1)
poly = F(x, (Q(2, 3), Q(1, 3)))
assert poly == (-8, 158, -63, 3)
shifted = compose(poly, (27, 1))
assert shifted == (17380, 3317, 180, 3)
assert all(c > 0 for c in shifted)

# The endpoint numerator identity, proved as a polynomial in m.
n_at_endpoint = (-1, 3)
num = sub(scale(mul(x, sub(n_at_endpoint, (4,))), 3),
          mul(sub(n_at_endpoint, (1,)), sub(n_at_endpoint, (2,))))
assert num == (-6,)
assert 3*169 > 5*100

# Check all intermediate h, not only the eight displayed fields.
# Integer arithmetic directly compares the positive-denominator inequalities.
rejections = 0
for h in range(2, 163):
    m = 5*h
    for n in range(27, 15*h-1):
        a = (n-1)*(n-2)
        assert 5*n*(n-3)*(3*m*(n-4)-a) > 6*m*a
        rejections += 1
    n = 15*h-1
    assert 12 < n
    assert 3*m*(n-4) < (n-1)*(n-2)
    # The endpoint satisfies even the sharper ALT08 long-row bound.
    assert 3*m*(n-3) < n*n


def hook_degree(lam):
    hooks = []
    for i, length in enumerate(lam):
        for j in range(length):
            below = sum(other > j for other in lam[i+1:])
            hooks.append(length-j+below)
    q, rem = divmod(factorial(sum(lam)), prod(hooks))
    assert rem == 0
    return q


rows = []
for radicand, h in [(1, 2), (2, 4), (7, 6), (11, 10), (19, 18),
                    (43, 42), (67, 66), (163, 162)]:
    disc = -4*radicand if radicand % 4 != 3 else -radicand
    if radicand == 1:
        assert h == 2
    elif disc % 8 == 0:
        assert h == 4
    else:
        assert h == radicand-1
    n = 15*h-1
    degree = hook_degree((n-3, 3))
    assert degree == n*(n-1)*(n-5)//6
    assert degree >= n*(n-3)//2
    beta = Q(3*(n-4), (n-1)*(n-2))
    assert beta-Q(1, 5*h) == -Q(6, 5*h*(n-1)*(n-2))
    rows.append({"radicand": radicand, "discriminant": disc, "h": h,
                 "n": n, "hook_degree": degree, "beta": str(beta),
                 "endpoint_difference": str(beta-Q(1, 5*h))})

result = {
    "status": "PASS",
    "completed_utc": datetime.now(timezone.utc).isoformat(),
    "runtime_seconds": time.perf_counter()-START,
    "proof_sha256": EXPECTED,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "rejected_integer_pairs": rejections,
    "h_grid": [2, 162],
    "universal_polynomial_ascending": list(map(str, poly)),
    "shifted_positive_polynomial_ascending": list(map(str, shifted)),
    "field_rows": rows,
    "scope": "Independent exact consequence of accepted ALT07/08 and all-count exclusions; no source-existence or additional movement claim. Universal identities are algebraic; the finite grid is a supplement."
}
(HERE / "independent_check.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
