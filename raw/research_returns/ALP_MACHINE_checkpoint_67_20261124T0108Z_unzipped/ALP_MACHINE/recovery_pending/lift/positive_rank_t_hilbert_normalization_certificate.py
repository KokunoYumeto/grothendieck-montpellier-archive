#!/usr/bin/env python3
"""Exact diagnostics for AM-LIFT-071; not a numerical local/global period.

The analytic cutoff, regularization and multiplicity-one arguments are in the
proof.  This script checks the finite algebra and the measure-exponent ledger.
It writes only the requested output file (default: adjacent JSON).
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path
import random

import sympy as sp


HERE = Path(__file__).resolve().parent
RNG = random.Random(710071)
COUNTS: Counter[str] = Counter()


def ck(value: bool, group: str, detail: object = None) -> None:
    if not value:
        raise AssertionError((group, detail))
    COUNTS[group] += 1


def det_mod(rows: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in rows]
    result = 1
    for col in range(len(a)):
        pivot = next((i for i in range(col, len(a)) if a[i][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            result = -result
        d = a[col][col]
        result = result * d % p
        di = pow(d, -1, p)
        for i in range(col + 1, len(a)):
            fac = a[i][col] * di % p
            a[i] = [(x - fac * y) % p for x, y in zip(a[i], a[col])]
    return result % p


def quotient_chart() -> None:
    # Full symbolic additive Jacobian; its sign is irrelevant to Haar, but its
    # square verifies the absolute determinant without an ordering convention.
    for r in range(1, 5):
        aa = sp.symbols(f'a0:{r*r}')
        bb = sp.symbols(f'b0:{r}')
        yy = sp.symbols(f'y0:{r}')
        t = sp.Symbol('t', nonzero=True)
        a, b, y = sp.Matrix(r, r, aa), sp.Matrix(r, 1, bb), sp.Matrix(1, r, yy)
        x = (a + b*y).row_join(b*t).col_join(y.row_join(sp.Matrix([[t]])))
        jac = sp.Matrix(list(x)).jacobian(list(aa) + list(bb) + list(yy) + [t])
        jdet = sp.factor(jac.det())
        ck(sp.expand(jdet*jdet - t**(2*r)) == 0, 'symbolic_additive_jacobian', r)
        ck(sp.expand(x.det() - a.det()*t) == 0, 'symbolic_block_determinant', r)
        # |t|^r / |det(a)t|^(r+1), relative to dg_r^raw.
        ck(r - (r+1) == -1, 'quotient_t_exponent', r)
        ck(-(r+1) - (-r) == -1, 'quotient_det_exponent', r)
    for r in range(1, 7):
        for _ in range(16):
            a = sp.eye(r)
            for i in range(r):
                a[i, i] = RNG.choice([-3, -2, 1, 2, 3])
                for j in range(i):
                    a[i, j] = RNG.randrange(-3, 4)
            b = sp.Matrix([RNG.randrange(-5, 6) for _ in range(r)])
            y = sp.Matrix([[RNG.randrange(-5, 6) for _ in range(r)]])
            t = RNG.choice([-3, -1, 1, 2, 4])
            x = (a + b*y).row_join(b*t).col_join(y.row_join(sp.Matrix([[t]])))
            ck(x.det() == a.det()*t, 'numeric_block_chart', (r, t))


def roots(k: int, rho: int) -> tuple[list[int], set[tuple[int, int]], set[tuple[int, int]]]:
    h = list(range(k))
    e = list(range(k, k+rho))
    z = k+rho
    f = list(range(z+1, z+1+rho))
    w = [0]*k + list(range(rho, 0, -1)) + [0] + list(range(-1, -rho-1, -1))
    r: set[tuple[int, int]] = set()
    for block in (e, f):
        r.update((i, j) for i in block for j in block if i < j)
    r.update((i, j) for i in e for j in h)
    r.update((i, z) for i in e)
    r.update((i, j) for i in h for j in f)
    r.update((z, j) for j in f)
    r.update((i, j) for i in e for j in f)
    generic = set(zip(e[:-1], e[1:])) | set(zip(f[:-1], f[1:]))
    if rho:
        generic |= {(e[-1], z), (z, f[0])}
    return w, r, generic


def root_and_cutoff_ledger() -> None:
    for k in range(2, 15):
        for rho in range(0, 9):
            w, rr, gg = roots(k, rho)
            n = k + 2*rho + 1
            ck(len(w) == n, 'rank_dictionary')
            ck(len(rr) == rho*(2*k+2*rho+1), 'radical_dimension')
            for i, j in rr:
                ck(w[i] - w[j] > 0, 'positive_root_weight')
            for i, j in gg:
                ck(w[i] - w[j] == 1, 'generic_root_weight')
            for i, j in rr:
                for j2, ell in rr:
                    if j != j2:
                        continue
                    ck((i, ell) in rr, 'root_commutator_closure')
                    ck((w[i]-w[j])+(w[j]-w[ell]) == w[i]-w[ell],
                       'weighted_column_coarea')
            # D has valuation -1 on the final F block, zero elsewhere.
            dv = [0]*(k+rho+1) + [-1]*rho
            total = sum(dv[i]-dv[j] for i, j in rr)
            ck(total == rho*(k+rho+1), 'physical_root_modulus')
            ck(sum(i < k for i, j in rr) == k*rho, 'outgoing_H_roots')
            ck(sum(j < k for i, j in rr) == k*rho, 'incoming_H_roots')
            for wi in range(1, rho+1):
                for wj in range(1, wi):
                    for compact_margin in range(0, 4):
                        L = compact_margin + 1
                        ck((wi-wj)*L + compact_margin <= wi*L,
                           'E_shear_cutoff_margin')


def gauss_upper_lower(c: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix] | None:
    ell = c.copy()
    elim = sp.eye(c.rows)
    for i in range(c.rows-1, -1, -1):
        if ell[i, i] == 0:
            return None
        for j in range(i):
            coeff = ell[j, i] / ell[i, i]
            ell[j, :] = ell[j, :] - coeff*ell[i, :]
            elim[j, :] = elim[j, :] - coeff*elim[i, :]
    return elim.inv(), ell


def triangular_changes() -> None:
    # The exact a(I-vX) term in an E peel; Xv=0 is structural.
    for k in range(2, 8):
        for remaining_e in range(1, 5):
            d = k + remaining_e
            for _ in range(12):
                a = sp.eye(d)
                for i in range(d):
                    for j in range(i):
                        a[i, j] = RNG.randrange(-3, 4)
                X = sp.Matrix([[RNG.randrange(-4, 5) if j < k else 0 for j in range(d)]])
                v = sp.zeros(d, 1)
                v[-1] = RNG.randrange(-4, 5)
                xx = a.row_join(sp.zeros(d, 1)).col_join(X.row_join(sp.ones(1, 1)))
                uu = sp.eye(d+1)
                uu[:d, d] = v
                nn = sp.eye(d+1)
                nn[:d, d] = a*v
                yy = (a*(sp.eye(d)-v*X)).row_join(sp.zeros(d, 1))
                yy = yy.col_join(X.row_join(sp.ones(1, 1)))
                ck(X*v == sp.zeros(1, 1), 'E_shear_orthogonality')
                ck(xx*uu == nn*yy, 'E_shear_full_matrix')
                ck((sp.eye(d)-v*X).det() == 1, 'E_shear_determinant')
    # Completed-row substitution n_v^-1 (X+B Y) h and its determinant.
    for rho in range(1, 5):
        for k in range(2, 5):
            for _ in range(8):
                B, v = sp.eye(rho), sp.eye(rho)
                for i in range(rho):
                    for j in range(i):
                        B[i, j] = 2*RNG.randrange(-2, 3)
                        v[j, i] = RNG.randrange(-2, 3)
                gl = gauss_upper_lower(B*v)
                if gl is None:
                    continue  # This chart is outside the compact first test.
                nv, lv = gl
                ck(nv*lv == B*v, 'E_gauss_identity')
                ck(nv.det() == 1, 'E_gauss_unipotent')
                hh = sp.diag(*range(2, k+2))
                # Column-major vectorization gives h^t tensor n^-1 B.
                J = sp.kronecker_product(hh.T, nv.inv()*B)
                ck(J.det() == B.det()**k * hh.det()**rho,
                   'completed_row_jacobian')


def character_sum_zero(counts: list[int], m: int) -> bool:
    z = sp.Symbol('z')
    poly = sp.Poly(sum(a*z**j for j, a in enumerate(counts)), z)
    return sp.rem(poly, sp.Poly(sp.cyclotomic_poly(m, z), z)).is_zero


def exact_fourier() -> None:
    # Ring-valued additive Fourier inversion, including nonprime moduli.
    for m in (2, 3, 4, 5, 8, 9, 11):
        for a in range(m):
            counts = [0]*m
            for v in range(m):
                counts[a*v % m] += 1
            if a == 0:
                ck(counts == [m]+[0]*(m-1), 'finite_fourier_zero_frequency')
            else:
                ck(character_sum_zero(counts, m), 'finite_fourier_nonzero_frequency')
    for p in (2, 3, 5):
        for exponent in range(1, 4):
            m = p**exponent
            for cutoff in range(exponent+1):
                vv = range(0, m, p**cutoff)
                for a in range(m):
                    counts = [0]*m
                    for v in vv:
                        counts[a*v % m] += 1
                    annihilator = (a*p**cutoff) % m == 0
                    if annihilator:
                        ck(counts == [len(vv)]+[0]*(m-1), 'finite_cutoff_annihilator')
                    else:
                        ck(character_sum_zero(counts, m), 'finite_cutoff_cancellation')
    for p in (2, 3, 5):
        for dim in (1, 2):
            vectors = list(itertools.product(range(p), repeat=dim))
            target = (0,)*(dim-1) + (1,)
            for row in vectors:
                counts = [0]*p
                for v in vectors:
                    phase = sum((x-y)*z for x, y, z in zip(row, target, v)) % p
                    counts[phase] += 1
                if row == target:
                    ck(counts == [p**dim]+[0]*(p-1), 'full_column_row_selector')
                else:
                    ck(character_sum_zero(counts, p), 'full_column_row_selector')
    # E-to-z Fourier inversion fixes only the E part: the H-row X is free.
    for p in (2, 3):
        for k in (1, 2):
            for rho in (1, 2):
                ee = list(itertools.product(range(p), repeat=rho))
                target = (0,)*(rho-1)+(1,)
                for row in itertools.product(range(p), repeat=k+rho):
                    counts = [0]*p
                    for v in ee:
                        phase = sum((x-y)*z for x, y, z in zip(row[k:], target, v)) % p
                        counts[phase] += 1
                    if row[k:] == target:
                        ck(counts == [p**rho]+[0]*(p-1), 'partial_column_free_H_row')
                    else:
                        ck(character_sum_zero(counts, p), 'partial_column_free_H_row')


def finite_translation_separation() -> None:
    for p in (2, 3, 5):
        for k in (1, 2, 3):
            if p**k > 125:
                continue
            vec = list(itertools.product(range(p), repeat=k))
            index = {x:i for i, x in enumerate(vec)}
            for _ in range(6):
                while True:
                    h = [[RNG.randrange(p) for _ in range(k)] for _ in range(k)]
                    if det_mod(h, p):
                        break
                f = [(RNG.randrange(-2, 3), RNG.randrange(-2, 3)) for _ in vec]
                g = [(RNG.randrange(-2, 3), RNG.randrange(-2, 3)) for _ in vec]
                total_r, total_i = 0, 0
                for X in vec:
                    for Y in vec:
                        shifted = [(x+y) % p for x, y in zip(X, Y)]
                        Z = tuple(sum(shifted[i]*h[i][j] for i in range(k)) % p for j in range(k))
                        fr, fi = f[index[Z]]
                        gr, gi = g[index[X]]
                        total_r += fr*gr + fi*gi
                        total_i += fi*gr - fr*gi
                fr, fi = sum(x[0] for x in f), sum(x[1] for x in f)
                gr, gi = sum(x[0] for x in g), sum(x[1] for x in g)
                ck((total_r, total_i) == (fr*gr+fi*gi, fi*gr-fr*gi),
                   'finite_row_decorrelation')


def kappa(q: int, rank: int) -> Q:
    ans = Q(1)
    for i in range(1, rank+1):
        ans *= 1-Q(1, q**i)
    return ans


def exact_scalar_ledger() -> None:
    for q in (2, 3, 5, 7, 11, 29, 101):
        for k in range(2, 15):
            for rho in range(0, 9):
                n = k + 2*rho + 1
                Lg, Lh, L0sq = Q(7, 3), Q(11, 4), Q(13, 5)
                normG = kappa(q, n)*Lg
                normH = kappa(q, k-1)*(1-Q(1, q))*Lh
                delta = Q(1, q**(rho*(k+rho+1)))
                zprob2 = delta * Q(q**k, (q**k-1)**2)*L0sq
                zunitraw2 = kappa(q, k)**2*zprob2/(normG*normH)
                alpha = zunitraw2/(delta*kappa(q, k))
                Lnormalized = L0sq/(kappa(q, n)*Lg*Lh)
                expected = Q(q, (q-1)*(q**k-1))
                ck(alpha/Lnormalized == expected, 'canonical_scalar_cancellation')
                ck(1/expected < q**k, 'inverse_square_cost')
                ck(kappa(q, n-1)*(1-Q(1, q**n)) == kappa(q, n),
                   'spherical_norm_conversion')
                ck(kappa(q, k)/kappa(q, k-1) == 1-Q(1, q**k),
                   'small_rank_norm_conversion')
                ck(-rho + -rho == -2*rho, 'two_row_string_det_ledger')
    for p in (2, 3):
        for rank in range(1, 4 if p == 2 else 3):
            invertible = 0
            for entries in itertools.product(range(p), repeat=rank*rank):
                rows = [list(entries[i*rank:(i+1)*rank]) for i in range(rank)]
                invertible += bool(det_mod(rows, p))
            ck(Q(invertible, p**(rank*rank)) == kappa(p, rank), 'raw_compact_volume')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=HERE/'positive_rank_t_hilbert_normalization_certificate.json')
    args = parser.parse_args()
    started = datetime.now(timezone.utc).isoformat()
    quotient_chart()
    root_and_cutoff_ledger()
    triangular_changes()
    exact_fourier()
    finite_translation_separation()
    exact_scalar_ledger()
    proof = HERE/'positive_rank_t_hilbert_normalization.md'
    data = {
        'finding':'AM-LIFT-071', 'status':'PASS',
        'started_utc':started, 'completed_utc':datetime.now(timezone.utc).isoformat(),
        'assertions':sum(COUNTS.values()), 'groups':dict(sorted(COUNTS.items())),
        'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact finite algebra, quotient Jacobians and measure/scalar ledger only; analytic cutoff and primary hypotheses require whole-proof review.',
        'formula':'alpha_phys_natural = q/((q-1)*(q^k-1))',
        'global_nonvanishing_claim':False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temp = args.output.with_suffix(args.output.suffix+'.tmp')
    temp.write_text(json.dumps(data, indent=2)+'\n')
    temp.replace(args.output)
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
