#!/usr/bin/env python3
"""Independent finite witnesses for HOS20--22, not their universal proof.

The author checker is not imported. Rank/type counts are recovered by exact
quadratic Gauss sums; primary polynomials are derived by cyclotomic factoring.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import datetime
import hashlib
import json
import time
import warnings
import numpy as np
import sympy as sp
from flint import nmod_poly

START = time.perf_counter()
HERE = Path(__file__).resolve().parent
PROOF = HERE.parents[1] / "g34_eightfolds/bireflection/higher_odd_symplectic_three_semisimple_section.tex"
FROZEN = "700d6e80b8e7d7183dfd698627b36b116bf0b8a7235b9e8fccc2c17ff294bf6b"
assert hashlib.sha256(PROOF.read_bytes()).hexdigest() == FROZEN


def identity(n):
    return np.eye(n, dtype=np.int64)


def power(a, n):
    r = identity(a.shape[0])
    while n:
        if n & 1:
            r = r @ a % 3
        a = a @ a % 3
        n //= 2
    return r


def row_reduce(a):
    a = np.array(a, dtype=np.int64).copy() % 3
    row = 0
    pivots = []
    for col in range(a.shape[1]):
        choices = np.flatnonzero(a[row:, col])
        if not len(choices):
            continue
        j = row + int(choices[0])
        a[[row, j]] = a[[j, row]]
        a[row] = a[row] * a[row, col] % 3
        for j in range(a.shape[0]):
            if j != row:
                a[j] = (a[j] - a[j, col] * a[row]) % 3
        pivots.append(col)
        row += 1
        if row == a.shape[0]:
            break
    return a, pivots


def kernel(a):
    r, pivots = row_reduce(a)
    out = []
    for j in range(r.shape[1]):
        if j in pivots:
            continue
        v = np.zeros(r.shape[1], dtype=np.int64)
        v[j] = 1
        for i, p in enumerate(pivots):
            v[p] = -r[i, j] % 3
        out.append(v)
    return out


def rank(a):
    return len(row_reduce(a)[1])


def inverse(a):
    n = a.shape[0]
    r, pivots = row_reduce(np.column_stack((a, identity(n))))
    assert pivots == list(range(n))
    return r[:, n:]


def primary_companion(prime, degree):
    # For prime ell, Phi_ell has all coefficients one. FLINT returns the
    # exact factors without SymPy's unsupported ordering of nmod scalars.
    factors = nmod_poly([1]*prime, 3).factor()[1]
    coeffs = []
    for f, multiplicity in factors:
        assert multiplicity == 1 and f.degree() == degree
        coeffs.append(tuple(int(f[j]) % 3 for j in range(degree + 1)))
    chosen = min(coeffs)
    assert chosen[-1] == 1
    a = np.zeros((degree, degree), dtype=np.int64)
    a[1:, :-1] = identity(degree - 1)
    a[:, -1] = -np.array(chosen[:-1]) % 3
    assert np.array_equal(power(a, prime), identity(degree))
    assert rank(a - identity(degree)) == degree
    return a, chosen, len(factors)


def fixed_forms(a, alternating=False):
    n = a.shape[0]
    coords = [(i, j) for i in range(n)
              for j in range(i + int(alternating), n)]
    basis = []
    for i, j in coords:
        b = np.zeros((n, n), dtype=np.int64)
        b[i, j] = 1
        b[j, i] = 2 if alternating else 1
        basis.append(b)
    columns = np.array([(a.T @ b @ a - b).reshape(-1) % 3 for b in basis]).T
    out = [np.einsum("i,ijk->jk", v, np.array(basis)) % 3 for v in kernel(columns)]
    assert all(np.array_equal(a.T @ b @ a % 3, b) for b in out)
    return out


def symplectic_pair(a):
    n = a.shape[0]
    h = np.zeros((2*n, 2*n), dtype=np.int64)
    h[:n, :n], h[n:, n:] = a, inverse(a).T
    j = np.zeros_like(h)
    j[:n, n:], j[n:, :n] = identity(n), -identity(n) % 3
    assert np.array_equal(h.T @ j @ h % 3, j)
    assert np.count_nonzero(j[:n, :n]) == np.count_nonzero(j[n:, n:]) == 0
    return h, j


# Exact Gauss sums classify every symmetric 4-form, independently of any
# congruence diagonalization or published orthogonal orbit-size formula.
a5, p5, f5 = primary_companion(5, 4)
n = 4
coords = [(i, j) for i in range(n) for j in range(i, n)]
coeff = np.array(list(product(range(3), repeat=len(coords))), dtype=np.int16)
vectors = np.array(list(product(range(3), repeat=n)), dtype=np.int16)
monomials = np.array([(1 if i == j else 2) * vectors[:, i] * vectors[:, j]
                      for i, j in coords], dtype=np.int16)
values = coeff @ monomials % 3
counts = np.array([(values == j).sum(axis=1) for j in range(3)]).T
alpha, beta = counts[:, 0] - counts[:, 2], counts[:, 1] - counts[:, 2]
norm = alpha*alpha - alpha*beta + beta*beta
lookup = {3**j: j for j in range(2*n + 1)}
ranks = np.array([2*n - lookup[int(z)] for z in norm])
discs = np.zeros(len(coeff), dtype=np.int8)
for rr in range(n + 1):
    use = ranks == rr
    scale = (-1)**(rr//2) * 3**(n - (rr+1)//2)
    assert np.all(beta[use] == (2*alpha[use] if rr % 2 else 0))
    assert np.all(np.abs(alpha[use]) == abs(scale))
    discs[use] = np.where(alpha[use] == scale, 1, 2)
acted_vectors = vectors @ a5.T % 3
powers3 = np.array([3**j for j in range(n-1, -1, -1)])
perm = acted_vectors @ powers3
is_fixed = np.all(values[:, perm] == values, axis=1)
totals = Counter(zip(map(int, ranks), map(int, discs)))
fixed = Counter(zip(map(int, ranks[is_fixed]), map(int, discs[is_fixed])))
assert sum(totals.values()) == 59049
assert fixed == {(0, 1): 1, (4, 2): 8}
assert Fraction(fixed[(4, 2)], totals[(4, 2)]) == Fraction(1, 2106)
for (rr, dd), count in totals.items():
    if rr:
        assert Fraction(fixed[(rr, dd)], count) <= Fraction(1, 9)

# Independently construct both primary behaviors, including an order11
# example not used by the author supplement.
h5, j5 = symplectic_pair(a5)
assert np.array_equal(power(h5, 5), identity(8))
assert rank(h5 - identity(8)) == 8
a11, p11, f11 = primary_companion(11, 5)
assert len(fixed_forms(a11)) == 0
h11, j11 = symplectic_pair(a11)
assert np.array_equal(power(h11, 11), identity(10))
assert len(fixed_forms(h11)) == 5
assert rank(h11 - identity(10)) == 10

# Directly count the full toral centralizer: the irreducible companion
# forces every commuting map to be a polynomial in it.
a41, p41, f41 = primary_companion(41, 8)
alternating = fixed_forms(a41, alternating=True)
assert len(alternating) == 4
j41 = next(b for b in alternating if rank(b) == 8)
polynomial_basis = np.array([power(a41, j) for j in range(8)])
all_coeff = np.array(list(product(range(3), repeat=8)), dtype=np.int64)
all_commuting = np.einsum("bi,ijk->bjk", all_coeff, polynomial_basis) % 3
assert np.all((all_commuting @ a41 - a41 @ all_commuting) % 3 == 0)
isometries = np.all((all_commuting.transpose(0, 2, 1) @ j41 @ all_commuting - j41) % 3 == 0,
                    axis=(1, 2))
assert int(isometries.sum()) == 82 == 3**4 + 1
assert 82 <= 10**2

# Unitriangular count, using exact integer matrix multiplication.
unitriangular_counts = []
upper = [(i, j) for i in range(4) for j in range(i+1, 4)]
for last in (1, 2):
    d = identity(4)
    d[3, 3] = last
    seen = set()
    for c in product(range(3), repeat=6):
        l = identity(4)
        for (i, j), v in zip(upper, c):
            l[i, j] = v
        seen.add(tuple((l.T @ d @ l % 3).reshape(-1)))
    assert len(seen) == 729
    unitriangular_counts.append(len(seen))

q = Fraction
assert q(4, 5) * q(8, 9) * q(3, 8) == q(4, 15)
assert (1-q(10, 27))/2 == q(17, 54) > q(4, 15) > q(2, 9)
assert 3**4 > 4**3 and 3**2 < 10 < 3**4
assert q(19, 78) > q(2, 9) > q(19, 104)
assert 6 / (12*q(2, 9)-2) == 9 < 27
assert 6 / (12*q(19, 104)-2) == q(156, 5) < 81
r = sp.Symbol("r", integer=True, positive=True)
assert sp.expand(((r+2)*r - r*(r-2))/4) == r

out = {
    "status": "PASS",
    "actual_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "proof_sha256": FROZEN,
    "runtime_seconds": time.perf_counter()-START,
    "methods": ["exact integer quadratic Gauss sums", "derived cyclotomic primary polynomials",
                "independent modular linear equations", "full polynomial centralizer enumeration"],
    "symmetric_four_forms": len(coeff),
    "rank_type_counts": [{"rank": rr, "discriminant": dd, "total": c,
                           "fixed": fixed[(rr, dd)],
                           "fraction": str(q(fixed[(rr, dd)], c))}
                          for (rr, dd), c in sorted(totals.items())],
    "unitriangular_counts": unitriangular_counts,
    "primary_witnesses": [
        {"prime": 5, "polynomial_ascending": p5, "factor_count": f5,
         "symplectic_dimension": 8, "opposite_isotropic_dimension": 4},
        {"prime": 11, "polynomial_ascending": p11, "factor_count": f11,
         "symplectic_dimension": 10, "opposite_isotropic_dimension": 5,
         "fixed_symmetric_single_primary": 0, "fixed_symmetric_pair": 5},
        {"prime": 41, "polynomial_ascending": p41, "factor_count": f41,
         "symplectic_dimension": 8, "invariant_alternating_dimension": 4,
         "commuting_polynomials": len(all_coeff), "symplectic_centralizer": int(isometries.sum())}
    ],
    "exact_supports": ["4/15", "17/54", "2/9", "19/104"],
    "source_degree_ceilings": ["9", "156/5"],
    "scope": "Finite independent witnesses plus exact constants; the universal proof was separately read in full. No author code imported.",
    "failures_before_pass": ["Initial run stopped at SymPy factor_list sorting: TypeError nmods cannot be ordered. Replaced only cyclotomic factor extraction by exact flint.nmod_poly.factor; retained deterministic coefficient-tuple selection. No mathematical assertion failed."]
}
(HERE/"independent_check.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
