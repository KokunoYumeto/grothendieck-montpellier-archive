#!/usr/bin/env python3
"""Audited adaptation of Severn cert_L.py, run against freshly verified M.
Inputs are safe JSON and the new proof's contraction enclosure. No archived
rank or certificate truth value is read. Floating QR selects pivots only.
"""
# Rank certificate, part L [C]: ball-arithmetic rank of mu at the cover C0 = chi (x) (s^5)^* M.
# Input: the certified M (x~ and radius rho from cert_M.py). Every unknown of M is a ball of radius rho.
#   L on the s-plane (scalar gauge s^(theta - K) included): s = 0: 5 B0 + (theta - K) I; s^5 = 1: B1;
#   s^5 = c0: Bc; s = oo: 5 Binf - (theta - K) I. Coordinates sigma = 1/(s - s*), s* = 0.37 + 0.21 i, so that
#   sigma = oo is a regular point (G32 v0.8 App. B setting). theta = 1/4, K = 3.
# Steps: exact exponents; eigenbases P_p by pivot solves (multiplicities known exactly);
# Frobenius recursion with exact resonance detection (resonant entries set to 0: no-log, semisimple local
# monodromy; the enclosed right-hand sides there are printed and must contain 0); Phi for A and B as in
# the rank program; kernel bases by a certified-invertible square pivot block (G32 Lemma B.1(3)); the 9 x 12
# residue matrix of mu; a 9 x 9 minor certified nonzero.
import sys, json, time
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '..'); sys.path.insert(0, '.')
from cert_lib import *

CLS='g'; TAG='rerun_g'
setprec(256)
mvals = [1, 3, 7, 9, 11, 13, 17, 19]
TH = Fr(1, 4); KSH = 3
saved=json.load(open('center_g.json'));xt=saved['center'];meta=saved['gauge']
cert=json.load(open('certM_rerun_g.json'))
assert cert['contraction'] and cert['side']
rho=cert['rho']
U1=[C(complex(*z))for z in meta['u1f']];j0=meta['j0'];others=meta['others'];U2J0=C(complex(*meta['u2j0']))
w=[acb(arb(arb(a).mid(),rho),arb(arb(b).mid(),rho))for a,b in xt]
v1 = w[0:8]; u2 = [None] * 8; u2[j0] = U2J0
for t, j in enumerate(others): u2[j] = w[8 + t]
v2 = w[15:23]
n = 8
B0 = acb_mat([[acb(mvals[i]) / 20 if i == j else 0 for j in range(n)] for i in range(n)])
B1 = acb_mat([[U1[i] * v1[j] for j in range(n)] for i in range(n)])
Bc = acb_mat([[u2[i] * v2[j] for j in range(n)] for i in range(n)])
Binf = -(B0 + B1 + Bc)
th_inf = {'g': [0, 0, Fr(1, 12), Fr(5, 12), Fr(7, 12), Fr(11, 12), Fr(1, 3), Fr(2, 3)],
          'h': [Fr(1, 2), Fr(1, 2), Fr(1, 12), Fr(5, 12), Fr(7, 12), Fr(11, 12), Fr(1, 6), Fr(5, 6)]}[CLS]
E_inf = [Fr(cert['Einf_num'][k]) for k in range(8)]    # exact exponents of M at oo (rationals, from cert_M)
I8 = eye(n)
# Independently bound infinity eigenvalue discs relative to exact candidate rationals.
Bn = np.array([[complex(float(Binf[i,j].real.mid()),float(Binf[i,j].imag.mid())) for j in range(n)] for i in range(n)])
_,Vn = np.linalg.eig(Bn)
Vb = acb_mat([[C(Vn[i,j]) for j in range(n)] for i in range(n)])
Tb = Vb.inv()*Binf*Vb
for i in range(n):
    rad = sum((abs(Tb[i,j]) for j in range(n) if j!=i),arb(0))
    e = acb(E_inf[i].numerator)/E_inf[i].denominator
    assert abs(Tb[i,i]-e)+rad < arb(1)/10**10
print("Infinity exponent Gershgorin discs within 1e-10 of exact labels",flush=True)
c0 = C(2 + 1j)
zeta = [acb.exp_pi_i(acb(2 * j) / 5) for j in range(5)]
r5 = c0 ** (acb(1) / 5)
spts = [acb(0)] + zeta + [r5 * z for z in zeta]
sA = [B0 * 5 + I8 * acb(TH.numerator - KSH * TH.denominator) / TH.denominator] + [B1] * 5 + [Bc] * 5
Ainf = zeros(n)
for A in sA: Ainf -= A
SSTAR = C(0.37 + 0.21j)
ps = [1 / (p - SSTAR) for p in spts] + [acb(0)]
As = sA + [Ainf]
# exact exponents
ex0 = [5 * Fr(m, 20) + TH - KSH for m in mvals]
exR = [Fr(0)] * 7 + [Fr(1, 2)]
exI = [5 * e - (TH - KSH) for e in E_inf]
EXP = [ex0] + [exR] * 10 + [exI]


def eigbasis(A, exps):
    """columns: kernel bases of A - lambda for the distinct exact lambdas, by pivot solves in balls."""
    An = np.array([[complex(float(A[i, j].real.mid()), float(A[i, j].imag.mid())) for j in range(n)] for i in range(n)])
    cols = []; lam_list = []
    for lam in sorted(set(exps)):
        mult = exps.count(lam)
        Mn = An - float(lam) * np.eye(n)
        # pivot: choose n - mult columns (dependent) and the free columns F (mult of them) by QR with pivoting
        import scipy.linalg as sl
        Qr, Rr, piv = sl.qr(Mn, pivoting=True)
        dep = list(piv[:n - mult]); free = list(piv[n - mult:])
        _, _, prow = sl.qr(Mn[:, dep].T, pivoting=True)
        rows = list(prow[:n - mult])
        Mb = A - I8 * acb(lam.numerator) / lam.denominator
        S = acb_mat([[Mb[i, j] for j in dep] for i in rows])
        assert not S.det().contains(0), "eigenbasis pivot"
        Si = S.inv()
        for f in free:
            rhs = acb_mat([[-Mb[i, f]] for i in rows])
            sol = Si * rhs
            v = [acb(0)] * n; v[f] = acb(1)
            for t, j in enumerate(dep): v[j] = sol[t, 0]
            cols.append(v); lam_list.append(lam)
    P = acb_mat([[cols[j][i] for j in range(n)] for i in range(n)])
    return P, lam_list


def frob(k, order):
    Ap = As[k]; p = ps[k]
    P, lam = eigbasis(Ap, EXP[k])
    Pi = P.inv()
    # b_m = sum_{q != k} A_q (-1)^(m-1) / (p - p_q)^m
    H = [eye(n)]; resmax = 0.0
    bt = [None]
    for m in range(1, order + 1):
        bm = zeros(n)
        for q in range(len(ps)):
            if q == k: continue
            dd = p - ps[q]
            bm += As[q] * (((-1) ** (m - 1)) / dd ** m)
        bt.append(Pi * bm * P)
    for m in range(1, order + 1):
        R = zeros(n)
        for l in range(1, m + 1): R += bt[l] * H[m - l]
        Hm = zeros(n)
        for i in range(n):
            for j in range(n):
                den = m + lam[j] - lam[i]
                if den == 0:
                    resmax = max(resmax, float(abs(R[i, j]).upper()))
                    if not (abs(R[i, j]).lower() == 0 or R[i, j].contains(0)):
                        raise ValueError('log obstruction ball excludes 0')
                else:
                    Hm[i, j] = R[i, j] * acb(den.denominator) / den.numerator
        H.append(Hm)
    return P, lam, H, resmax


def series_inv(H, order):
    G = [eye(n)]
    for m in range(1, order + 1):
        s = zeros(n)
        for l in range(1, m + 1): s -= H[l] * G[m - l]
        G.append(s)
    return G


def binom(a, t):
    r = Fr(1)
    for i in range(t): r *= Fr(a - i, i + 1)
    return r


def build_phi(kind, data):
    fl = []
    for k in range(len(ps)):
        lam = data[k][1]
        f = [(l.numerator // l.denominator) if kind == 'A' else ((-l).numerator // (-l).denominator) for l in lam]
        fl.append(f)
    M = [max(0, -min(f)) for f in fl]
    base = {}; t = 0
    for k in range(len(ps)): base[k] = t; t += M[k] * n
    NU = t
    def Rmat(k, o):
        R = [[acb(0)] * NU for _ in range(n)]
        for q in range(len(ps)):
            for m in range(1, M[q] + 1):
                col = base[q] + (m - 1) * n
                if q == k:
                    if o == -m:
                        for i in range(n): R[i][col + i] += 1
                elif o >= 0:
                    d = ps[k] - ps[q]
                    cf = acb(binom(-m, o).numerator) / binom(-m, o).denominator * d ** (-m - o)
                    for i in range(n): R[i][col + i] += cf
        return acb_mat(R)
    rows = []
    for k in range(len(ps)):
        P, lam, H, _ = data[k]
        lo = -M[k]; hi = max(fl[k]) - 1
        if hi < lo: continue
        if kind == 'A':
            G = series_inv(H, hi - lo + 1); Pi = P.inv()
            L = [G[t] * Pi for t in range(len(G))]
        else:
            L = [H[t].transpose() * P.transpose() for t in range(hi - lo + 2)]
        Rs = {o: Rmat(k, o) for o in range(lo, hi + 1)}
        for o in range(lo, hi + 1):
            Cm = acb_mat(n, NU)
            for u in range(lo, o + 1):
                if o - u < len(L): Cm += L[o - u] * Rs[u]
            for j in range(n):
                if o < fl[k][j]: rows.append([Cm[j, c] for c in range(NU)])
    for i in range(n):
        row = [acb(0)] * NU
        for k in range(len(ps)):
            if M[k] >= 1: row[base[k] + i] = acb(1)
        rows.append(row)
    return rows, NU, M, base


def kernel_basis(rows, NU):
    Phi = acb_mat(rows)
    Pn = np.array([[complex(float(Phi[i, j].real.mid()), float(Phi[i, j].imag.mid())) for j in range(NU)] for i in range(len(rows))])
    import scipy.linalg as sl
    _, _, piv = sl.qr(Pn, pivoting=True)
    dep = sorted(piv[:NU - 3]); free = sorted(piv[NU - 3:])
    _, _, prow = sl.qr(Pn[:, dep].T, pivoting=True)
    R = sorted(prow[:NU - 3])
    S = acb_mat([[Phi[i, j] for j in dep] for i in R])
    Si = S.inv()
    Rpoint = acb_mat([[Si[i,j].mid() for j in range(S.ncols())] for i in range(S.nrows())])
    err = eye(S.nrows()) - Rpoint*S
    bound = max(sum((abs(err[i,j]) for j in range(err.ncols())), arb(0)).upper() for i in range(err.nrows()))
    assert bound < 1
    print("kernel pivot", S.nrows(), "Neumann bound", bound, flush=True)
    basis = []
    for f in free:
        rhs = acb_mat([[-Phi[i, f]] for i in R]); sol = Si * rhs
        v = [acb(0)] * NU; v[f] = acb(1)
        for t, j in enumerate(dep): v[j] = sol[t, 0]
        basis.append(v)
    # all rows (not only R) must vanish on the basis: consistency (balls contain 0)
    worst = 0.0
    for v in basis:
        for i in range(len(rows)):
            s = sum((Phi[i, j] * v[j] for j in range(NU)), acb(0))
            if not s.contains(0): raise ValueError('kernel consistency failed')
            worst = max(worst, float(abs(s).upper()))
    return basis, len(rows), worst


def laurent(vec, Mq, base, k, order_lo, order_hi):
    """Laurent coefficients at ps[k] of r = sum_{q,m} c_{q,m} (sigma - p_q)^-m."""
    out = {o: [acb(0)] * n for o in range(order_lo, order_hi + 1)}
    for q in range(len(ps)):
        for m in range(1, Mq[q] + 1):
            c = vec[base[q] + (m - 1) * n: base[q] + m * n]
            if q == k:
                if order_lo <= -m <= order_hi:
                    out[-m] = [a + b for a, b in zip(out[-m], c)]
            else:
                d = ps[k] - ps[q]
                for o in range(max(order_lo, 0), order_hi + 1):
                    cf = acb(binom(-m, o).numerator) / binom(-m, o).denominator * d ** (-m - o)
                    out[o] = [a + cf * b for a, b in zip(out[o], c)]
    return out


if __name__ == '__main__':
    t0 = time.time()
    ORDER = 12
    data = [frob(k, ORDER) for k in range(len(ps))]
    print('Frobenius done; max |log-obstruction ball| =', max(d[3] for d in data), f'({time.time()-t0:.0f}s)', flush=True)
    rowsA, NA, MA, baseA = build_phi('A', data)
    rowsB, NB, MB, baseB = build_phi('B', data)
    print('Phi_A', len(rowsA), 'x', NA, '; Phi_B', len(rowsB), 'x', NB, flush=True)
    bA, _, wA = kernel_basis(rowsA, NA); bB, _, wB = kernel_basis(rowsB, NB)
    print('kernel bases certified (pivot blocks invertible); consistency residual <=', wA, wB, f'({time.time()-t0:.0f}s)', flush=True)
    mx = max(MA + MB) + 1
    mu = []
    for r in bA:
        for q in bB:
            row = []
            for k in range(len(ps)):
                Lr = laurent(r, MA, baseA, k, -mx - 1, mx + 1); Lq = laurent(q, MB, baseB, k, -mx - 1, mx + 1)
                s = acb(0)
                for o in Lq:
                    if -1 - o in Lr:
                        s += sum((x * y for x, y in zip(Lq[o], Lr[-1 - o])), acb(0))
                row.append(s)
            mu.append(row)
    mun = np.array([[complex(float(x.real.mid()), float(x.imag.mid())) for x in row] for row in mu])
    print('mu (midpoints) singular values:', np.linalg.svd(mun, compute_uv=False), flush=True)
    # residue relations sum rho_p p^k = 0 (k = 0, 1, 2): consistency
    for kk in range(3):
        for row in mu:
            s = sum((x * p ** kk for x, p in zip(row, ps)), acb(0))
            assert s.contains(0), 'residue relation'
    # best 9 columns
    import itertools
    best = None
    for cols in itertools.combinations(range(12), 9):
        dt = abs(np.linalg.det(mun[:, cols]))
        if best is None or dt > best[0]: best = (dt, cols)
    cols = best[1]
    Mm = acb_mat([[mu[i][j] for j in cols] for i in range(9)])
    det = Mm.det()
    print('9x9 minor on columns', cols, ':', det, flush=True)
    ok = not det.contains(0)
    print('CERTIFIED rank mu = 9' if ok else 'minor ball contains 0: NOT certified', f'({time.time()-t0:.0f}s)', flush=True)
    json.dump({'cols': list(cols), 'det_mid': [float(det.real.mid()), float(det.imag.mid())],
               'det_rad': float(abs(det).rad() if hasattr(abs(det), 'rad') else 0), 'certified': ok,
               'abs_det_lower': lower_float(abs(det)), 'det_real_ball':str(det.real), 'det_imag_ball':str(det.imag), 'det_real_radius_upper':upper_float(det.real.rad()), 'det_imag_radius_upper':upper_float(det.imag.rad())}, open(f'certL_{TAG}.json', 'w'))
