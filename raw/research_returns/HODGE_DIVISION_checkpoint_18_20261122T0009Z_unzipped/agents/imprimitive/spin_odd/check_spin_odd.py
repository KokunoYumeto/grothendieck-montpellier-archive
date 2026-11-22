#!/usr/bin/env python3
"""Exact finite supplement to D-OL22--24; no floating-point eigenvalues.

The universal Clifford, group-generation and character estimates are proved
in the accompanying text, not inferred from these finite witnesses.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter

import numpy as np

HERE = Path(__file__).resolve().parent
COUNTS = {}
DETAILS = {}


def eq(x, y, p=3):
    return bool(np.array_equal(np.asarray(x) % p, np.asarray(y) % p))


def mm(*xs, p=3):
    z = np.asarray(xs[0], dtype=np.int64) % p
    for x in xs[1:]:
        z = (z @ np.asarray(x, dtype=np.int64)) % p
    return z


def rank(x, p=3):
    z = np.array(x, dtype=np.int64, copy=True) % p
    r = 0
    for j in range(z.shape[1]):
        hits = np.flatnonzero(z[r:, j])
        if not len(hits):
            continue
        i = r + int(hits[0])
        z[[r, i]] = z[[i, r]]
        z[r] = z[r] * pow(int(z[r, j]), -1, p) % p
        for k in range(z.shape[0]):
            if k != r:
                z[k] = (z[k] - z[k, j] * z[r]) % p
        r += 1
        if r == z.shape[0]:
            break
    return r


def inv(x, p=3):
    a = np.array(x, dtype=np.int64, copy=True) % p
    n = len(a)
    z = np.concatenate((a, np.eye(n, dtype=np.int64)), axis=1)
    for j in range(n):
        hits = np.flatnonzero(z[j:, j])
        assert len(hits)
        i = j + int(hits[0])
        z[[j, i]] = z[[i, j]]
        z[j] = z[j] * pow(int(z[j, j]), -1, p) % p
        for k in range(n):
            if k != j:
                z[k] = (z[k] - z[k, j] * z[j]) % p
    assert eq(z[:, :n], np.eye(n), p)
    return z[:, n:]


def det(x, p=3):
    a = np.array(x, dtype=np.int64, copy=True) % p
    out = 1
    for j in range(len(a)):
        hits = np.flatnonzero(a[j:, j])
        if not len(hits):
            return 0
        i = j + int(hits[0])
        if i != j:
            a[[i, j]] = a[[j, i]]
            out = -out
        pivot = int(a[j, j])
        out = out * pivot % p
        a[j] = a[j] * pow(pivot, -1, p) % p
        for k in range(j + 1, len(a)):
            a[k] = (a[k] - a[k, j] * a[j]) % p
    return out % p


def blockdiag(*xs):
    size = sum(len(x) for x in xs)
    z = np.zeros((size, size), dtype=np.int64)
    pos = 0
    for x in xs:
        n = len(x)
        z[pos:pos+n, pos:pos+n] = x
        pos += n
    return z


A = np.array([[0, 2], [1, 0]], dtype=np.int64)


def model(n):
    assert n >= 3 and n % 2
    h = blockdiag(np.ones((1, 1), dtype=np.int64), *([A] * ((n-1)//2)))
    g = blockdiag(A, h, inv(A).T)
    b = np.zeros((n+4, n+4), dtype=np.int64)
    b[:2, n+2:] = np.eye(2, dtype=np.int64)
    b[n+2:, :2] = np.eye(2, dtype=np.int64)
    b[2:n+2, 2:n+2] = np.eye(n, dtype=np.int64)
    return h, g, b


def reflection(v, b):
    v = np.asarray(v, dtype=np.int64)
    norm = int(v @ b @ v) % 3
    assert norm
    return (np.eye(len(v), dtype=np.int64)
            - 2 * pow(norm, -1, 3) * np.outer(v, v @ b)) % 3


def unipotent(x, z):
    n = x.shape[1]
    out = np.eye(n+4, dtype=np.int64)
    out[:2, 2:n+2] = x
    out[2:n+2, n+2:] = -x.T
    out[:2, n+2:] = z - 2 * (x @ x.T)
    return out % 3


def natural_checks():
    rows = []
    weight_count = 0
    for n in (3, 5, 7, 9, 21):
        h, g, b = model(n)
        assert eq(mm(g.T, b, g), b)
        assert det(g) == 1
        v = np.zeros(n+4, dtype=np.int64)
        v[2] = 1
        assert eq(mm(g, g), -reflection(v, b))
        s = np.kron(A, h) % 3
        sj = np.eye(2*n, dtype=np.int64)
        fixed = []
        for j in (1, 2, 3, 4):
            sj = mm(sj, s)
            fixed.append(2*n-rank(sj-np.eye(2*n, dtype=np.int64)))
        assert fixed == [n-1, 2*n-2, n-1, 2*n]
        if n <= 9:
            for w0 in itertools.product(range(3), repeat=n-1):
                w = np.array((0,)+w0, dtype=np.int64)
                y = np.column_stack((w, mm(h, w)))
                assert eq(mm(h, y, inv(A)), y)
                assert rank(y) == (2 if any(w0) else 0)
                weight_count += 1
        rows.append({"N": n, "dimension": n+4, "fixed_dimensions": fixed})
    COUNTS["natural_models"] = len(rows)
    COUNTS["all_fixed_dual_maps"] = weight_count
    DETAILS["fixed_space_models"] = rows

    rng = np.random.default_rng(221124)
    checks = 0
    for n in (3, 5, 7):
        h, g, b = model(n)
        for _ in range(40):
            x = rng.integers(0, 3, size=(2, n), dtype=np.int64)
            y = rng.integers(0, 3, size=(2, n), dtype=np.int64)
            zz, ww = (int(t) for t in rng.integers(0, 3, size=2))
            z = np.array([[0, zz], [-zz, 0]], dtype=np.int64)
            w = np.array([[0, ww], [-ww, 0]], dtype=np.int64)
            ux, uy = unipotent(x, z), unipotent(y, w)
            assert eq(mm(ux.T, b, ux), b)
            assert eq(mm(ux, ux, ux), np.eye(n+4))
            correction = 2 * (y @ x.T - x @ y.T)
            assert eq(mm(ux, uy), unipotent((x+y) % 3, (z+w+correction) % 3))
            assert eq(mm(g, ux, inv(g)), unipotent(mm(A, x, inv(h)), z))
            checks += 1
    COUNTS["exact_radical_group_and_conjugation_cases"] = checks


def vectors(n):
    return np.array(list(itertools.product(range(3), repeat=n)), dtype=np.int64)


def indices(v):
    n = v.shape[-1]
    return (v % 3) @ (3 ** np.arange(n-1, -1, -1, dtype=np.int64))


def carrier_checks():
    covariance = 0
    convolution_terms = 0
    carrier_rows = []
    for n in (3, 5):
        h, _, _ = model(n)
        vv = vectors(n)
        degree = len(vv)
        phase = mm(vv, h, vv.T)
        # K is the unnormalised matrix with entries zeta**phase.
        # K**2 = degree times the permutation of -h**2.  At every
        # other position the three root counts are equal exactly.
        expected_x = mm(-mm(h, h), vv.T).T
        expected_indices = indices(expected_x)
        for xi in range(degree):
            sums = (phase[xi, :, None] + phase) % 3
            counts = np.stack([(sums == j).sum(axis=0) for j in range(3)])
            good_y = expected_indices == xi
            assert np.all(counts[:, ~good_y] == degree//3)
            assert np.all(counts[0, good_y] == degree)
            assert np.all(counts[1:, good_y] == 0)
            convolution_terms += degree*degree
        assert eq(mm(-mm(h, h), -mm(h, h)), np.eye(n))

        diag_counts = [int(np.count_nonzero(np.diag(phase) == j)) for j in range(3)]
        assert diag_counts == [degree//3, 2*degree//3, 0]
        trace2 = 3**(n-1)
        trace1_imaginary = 3**((n-1)//2)
        multiplicities = [(degree+trace2)//4, (degree+trace2)//4,
                          (degree-trace2+2*trace1_imaginary)//4,
                          (degree-trace2-2*trace1_imaginary)//4]
        assert all(4*m == z for m, z in zip(multiplicities,
             [degree+trace2, degree+trace2,
              degree-trace2+2*trace1_imaginary, degree-trace2-2*trace1_imaginary]))
        assert sum(multiplicities) == degree and min(multiplicities) >= 0
        assert max(multiplicities) <= F(degree+trace2+2*trace1_imaginary, 4)
        assert max(multiplicities) < F(9*degree, 16)

        if n == 3:
            labels = [(u, v) for u in vv for v in vv]
        else:
            eye = np.eye(n, dtype=np.int64)
            zero = np.zeros(n, dtype=np.int64)
            labels = [(e, zero) for e in eye] + [(zero, e) for e in eye]
            labels += [(np.arange(n, dtype=np.int64) % 3, np.ones(n, dtype=np.int64)),
                       (np.ones(n, dtype=np.int64), np.arange(n, dtype=np.int64) % 3)]
        for u, v in labels:
            up, vp = mm(-h, v), mm(h, u)
            ypu = indices(vv+u)
            xmu = indices(vv-up)
            left = (phase[:, ypu] + (vv @ v)[None, :] + 2*int(v @ u)) % 3
            right = (phase[xmu, :] + (vv @ vp)[:, None] - 2*int(vp @ up)) % 3
            assert eq(left, right)
            covariance += degree*degree
        carrier_rows.append({"N": n, "degree": degree,
                             "trace_phase_counts": diag_counts,
                             "fourth_root_multiplicities_1_minus1_i_minusi": multiplicities,
                             "weyl_labels_checked": len(labels)})
    COUNTS["exact_carrier_convolution_terms"] = convolution_terms
    COUNTS["exact_weyl_covariance_entries"] = covariance
    DETAILS["carrier_models"] = carrier_rows


def outer_and_order_eight():
    b2 = np.eye(2, dtype=np.int64)
    e = np.array([1, 0], dtype=np.int64)
    v = np.array([1, 1], dtype=np.int64)
    assert eq(mm(reflection(v, b2), reflection(e, b2)), A)
    norms = [int(2*(w @ w)) % 3 for w in (v, e)]
    assert norms == [1, 2]
    upper = np.array([[1, 2], [0, 1]], dtype=np.int64)
    lower = np.array([[1, 0], [1, 1]], dtype=np.int64)
    assert eq(mm(upper, lower, upper), A)
    h, g, b = model(3)
    levi = blockdiag(A, np.eye(3, dtype=np.int64), inv(A).T)
    middle = blockdiag(np.eye(2, dtype=np.int64), h, np.eye(2, dtype=np.int64))
    assert eq(mm(levi, middle), g)
    DETAILS["order_four_outside_Omega_matrix_witness"] = {
        "natural_dimension": 7,
        "reflection_norms": norms,
        "spinor_norm_product": 2,
        "scope": "Exact small natural matrix witness; not a small-Spin classification premise."}

    a8 = np.array([[1, 2], [1, 1]], dtype=np.int64)
    a8_4 = mm(a8, a8, a8, a8)
    assert eq(a8_4, -np.eye(2)) and eq(mm(a8_4, a8_4), np.eye(2))
    h4 = np.zeros((4, 4), dtype=np.int64)
    h4[:2, 2:] = h4[2:, :2] = np.eye(2, dtype=np.int64)
    g4 = blockdiag(a8, inv(a8).T)
    g9 = blockdiag(np.ones((1, 1), dtype=np.int64), g4, g4)
    b9 = blockdiag(np.ones((1, 1), dtype=np.int64), h4, h4)
    assert eq(mm(g9.T, b9, g9), b9) and det(g9) == 1
    e9 = np.zeros(9, dtype=np.int64)
    e9[0] = 1
    assert eq(mm(g9, g9, g9, g9), -reflection(e9, b9))
    square = mm(g9, g9)
    fixed = [9-rank(square-s*np.eye(9, dtype=np.int64)) for s in (1, -1)]
    assert fixed == [1, 0]
    DETAILS["order_eight_model"] = {"natural_dimension": 9,
                                  "square_plus_minus_one_dimensions": fixed}
    COUNTS["nonprime_order_models"] = 2


def constants_and_text():
    beta = F(4997, 30000)
    delta = (1-F(19, 20)**9)/2
    assert F(1, 6) < delta < F(3, 16) < F(7, 32)
    assert 13*beta-2 > F(1, 7)
    assert 11*beta+delta-2 > F(1, 60)
    assert 2*beta*(1-beta) > F(1, 4)
    for q in (3, 5):
        c = (F(1, q)+F(1, q**9))/(1-F(1, q**9)-F(1, q**19))
        assert c < (1-4*beta if q == 3 else F(1, 4))
    n = 21
    assert F(4, 3**(n-2)) < F(1, 8)
    assert F(1, 4)*(1+F(1, 3)+F(2, 3**((n+1)//2))) < F(9, 16)
    # Strengthen the irrational second-vector error to an integer error.
    assert 3**(n-1)-3**((n+1)//2)-1 > F(3**(n-1), 2)
    assert 3**(n-2)-3**((n+1)//2)-3 > F(3**(n-2), 2)
    assert 3**(1135-3)-3**((1135-2+1)//2)-1 > 360
    text = (HERE/'spin_odd_extension_section.tex').read_text()
    assert not any(ord(c) < 32 and c not in '\n\t\r' for c in text)
    assert text.count('\\[') == text.count('\\]')
    assert text.count('\\begin{proof}') == text.count('\\end{proof}') == 3
    import re
    tags = re.findall(r'\\tag\{([^}]+)\}', text)
    assert len(tags) == len(set(tags)) == 21
    COUNTS['exact_endpoint_inequalities'] = 13
    DETAILS['constants'] = {"beta": str(beta), "delta": str(delta),
                            "thirteen_mark_excess": str(13*beta-2),
                            "one_good_mark_excess": str(11*beta+delta-2),
                            "two_bad_factor_support": str(2*beta*(1-beta))}
    return hashlib.sha256(text.encode()).hexdigest()


def main():
    started = perf_counter()
    natural_checks()
    carrier_checks()
    outer_and_order_eight()
    proof_hash = constants_and_text()
    result = {"status": "PASS", "arithmetic": "integers modulo 3 and rational Fractions only",
              "proof_sha256": proof_hash, "counts": COUNTS, "details": DETAILS,
              "seconds": perf_counter()-started,
              "scope": "Finite witnesses and exact constants; universal mathematical and source inputs remain the written proof."}
    target = HERE/'spin_odd_checked.json'
    target.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
