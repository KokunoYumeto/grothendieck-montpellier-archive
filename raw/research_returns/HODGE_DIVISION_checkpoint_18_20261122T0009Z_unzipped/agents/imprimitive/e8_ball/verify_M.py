#!/usr/bin/env python3
"""Standalone verification from saved candidate data; no continuation input.
Adapted from Severn cert_M.py, with saved gauge restored directly, safe JSON
inputs, and reuse of center monodromy for the 64 Q-only finite differences.
No archived truth value is used to establish the contraction.
"""
import json,time,sys,hashlib
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np
from cert_lib import *
setprec(256)
D=json.load(open('mtuple.json'));CLS='g';TI=0
saved=json.load(open('center_g.json'));xt=saved['center'];meta=saved['gauge']
a_T=np.array(D['a'],dtype=int)
b_T,c_T,d_T=[np.array(m,dtype=int) for m in D[CLS][TI]]
POLES=[0.0,1.0,2.0+1.0j];z0=0.5-1.0j
mvals=[1,3,7,9,11,13,17,19]
def loop_path(z0,p,r,m=12):
 phi=np.angle(z0-p)
 circ=[p+r*np.exp(1j*(phi+2*np.pi*k/m)) for k in range(m+1)]
 return [z0]+circ+[z0]
PATHS=[loop_path(z0,p,0.45)for p in POLES]
U1=[C(complex(*z))for z in meta['u1f']];j0=meta['j0'];others=meta['others'];U2J0=C(complex(*meta['u2j0']))
X=[acb(arb(a).mid(),arb(b).mid())for a,b in xt]
assert [[list(map(int,z.real.man_exp())),list(map(int,z.imag.man_exp()))]for z in X]==saved['center_exact_dyadics']
def eigvec_exact_ball(Amat, lam, kfix):
    """eigenvector e of the integer matrix Amat for eigenvalue lam (acb), normalized e[kfix] = 1; computed by
    solving 7 rows (chosen by a numerical pivot) of (A - lam) e = 0 in balls."""
    n = 8
    An = Amat.astype(complex); ln = complex(float(lam.real.mid()), float(lam.imag.mid()))
    Mn = An - ln * np.eye(n)
    cols = [j for j in range(n) if j != kfix]
    # choose 7 rows maximizing |det|
    best = None
    for drop in range(n):
        rows = [i for i in range(n) if i != drop]
        dt = abs(np.linalg.det(Mn[np.ix_(rows, cols)]))
        if best is None or dt > best[0]: best = (dt, rows)
    rows = best[1]
    Mb = acb_mat([[C(int(Amat[i, j])) - (lam if i == j else 0) for j in cols] for i in rows])
    rhs = acb_mat([[-(C(int(Amat[i, kfix])) - (lam if i == kfix else 0))] for i in rows])
    sol = Mb.solve(rhs)
    e = [None] * n; e[kfix] = acb(1)
    for t, j in enumerate(cols): e[j] = sol[t, 0]
    return e


def refl_data(t):
    """t = I - x' y'^T exactly: x' = column of I - t, y' = row / pivot (rationals as acb)."""
    R = np.eye(8, dtype=int) - t
    j = int(np.argmax(np.abs(R).sum(0)))
    xprime = R[:, j]; i = int(np.argmax(np.abs(xprime)))
    yprime = [acb(int(R[i, k])) / int(xprime[i]) for k in range(8)]
    # check exactness: R = x' y'^T
    for r in range(8):
        for k in range(8):
            assert R[r, k] * xprime[i] == xprime[r] * R[i, k]
    yi = [R[i, k] for k in range(8)]
    kk = int(np.argmax(np.abs(yi)))
    W = []
    for m in range(8):
        if m == kk: continue
        wv = [acb(0)] * 8; wv[m] = acb(1); wv[kk] = -acb(int(yi[m])) / int(yi[kk])
        W.append(wv)
    return [acb(int(v)) for v in xprime], yprime, W


setprec(256)
LAM = [acb.exp_pi_i(acb(2 * m) / 20) for m in mvals]
an = a_T.astype(complex); evn, evecn = np.linalg.eig(an)
EV = []
for m, lam in zip(mvals, LAM):
    ln = np.exp(2j * np.pi * m / 20)
    k = int(np.argmin(np.abs(evn - ln))); v = evecn[:, k]
    EV.append(eigvec_exact_ball(a_T, lam, int(np.argmax(np.abs(v)))))
RB = refl_data(b_T); RC = refl_data(c_T)


def to_np(M):
    return np.array([[complex(float(M[i, j].real.mid()), float(M[i, j].imag.mid())) for j in range(M.ncols())]
                     for i in range(M.nrows())])



def unpack(w):
    v1 = [w[k] for k in range(8)]
    u2 = [None] * 8; u2[j0] = U2J0
    for t, j in enumerate(others): u2[j] = w[8 + t]
    v2 = [w[15 + k] for k in range(8)]
    Q = acb_mat([[w[23 + 8 * i + j] for j in range(8)] for i in range(8)])
    return v1, u2, v2, Q


def residues(w):
    v1, u2, v2, _ = unpack(w)
    B0 = acb_mat([[acb(mvals[i]) / 20 if i == j else 0 for j in range(8)] for i in range(8)])
    B1 = acb_mat([[U1[i] * v1[j] for j in range(8)] for i in range(8)])
    Bc = acb_mat([[u2[i] * v2[j] for j in range(8)] for i in range(8)])
    return [B0, B1, Bc]


def F(w, N=100, frac=0.35, precomputed=None):
    v1, u2, v2, Q = unpack(w)
    As = residues(w); ps = [C(p) for p in POLES]
    Ms = precomputed if precomputed is not None else [transport(As, ps, P, frac=frac, N=N) for P in PATHS]
    out = [sum((U1[k] * v1[k] for k in range(8)), acb(0)) - acb(1) / 2,
           sum((u2[k] * v2[k] for k in range(8)), acb(0)) - acb(1) / 2]
    I8 = eye(8)
    for m in range(8):
        e = acb_mat([[t] for t in EV[m]])
        r = (Ms[0] - I8 * LAM[m]) * (Q * e)
        out += [r[i, 0] for i in range(8) if i != DROP0[m]]
    for M, (xp, yp, W), (dropP, rpiv) in ((Ms[1], RB, DROPR[0]), (Ms[2], RC, DROPR[1])):
        r = (M + I8) * (Q * acb_mat([[t] for t in xp]))
        out += [r[i, 0] for i in range(8) if i != dropP]
        for wv in W:
            r = (M - I8) * (Q * acb_mat([[t] for t in wv]))
            out.append(r[rpiv, 0])
    out.append(Q.det() - 1)
    return out, Ms




# The following choices are only pivots, subsequently verified on the whole ball.
t0=time.time()
center_As=residues(X)
center_Ms=[transport(center_As,[C(p)for p in POLES],P,N=100)for P in PATHS]
DROP0=[]
for lam in LAM:
 M=to_np(center_Ms[0]);ln=complex(float(lam.real.mid()),float(lam.imag.mid()))
 ev,V=np.linalg.eig((M-ln*np.eye(8)).T)
 DROP0.append(int(np.argmax(np.abs(V[:,int(np.argmin(np.abs(ev)))]))))
DROPR=[]
for Mb in center_Ms[1:]:
 M=to_np(Mb);ev,V=np.linalg.eig((M+np.eye(8)).T)
 drop=int(np.argmax(np.abs(V[:,int(np.argmin(np.abs(ev)))])))
 T=np.eye(8)-M;col=T[:,int(np.argmax(np.abs(T).sum(0)))];pivot=int(np.argmax(np.abs(col)))
 DROPR.append((drop,pivot))
print('pivots',DROP0,DROPR,flush=True)

F0, Ms0 = F(X,precomputed=center_Ms)
nU=87
print('F(x~) max upper', max(upper_float(abs(t)) for t in F0), f'({time.time()-t0:.0f}s)', flush=True)
h = 2.0 ** -80
Dm = [[None] * nU for _ in range(nU)]
for j in range(nU):
    Xp = list(X); Xp[j] = X[j] + h
    Fp, _ = F(Xp,precomputed=center_Ms if j>=23 else None)
    for i in range(nU): Dm[i][j] = (Fp[i] - F0[i]) / h
    if j % 10 == 0: print('  FD column', j, f'({time.time()-t0:.0f}s)', flush=True)
Dmat = acb_mat(Dm)
Dn = np.array([[complex(float(Dmat[i, j].real.mid()), float(Dmat[i, j].imag.mid())) for j in range(nU)] for i in range(nU)])
print('cond(D)', np.linalg.cond(Dn), flush=True)
Yn = np.linalg.inv(Dn)
Y = acb_mat([[C(Yn[i, j]) for j in range(nU)] for i in range(nU)])
# K_i = sup over the polydisc P_R of |F_i|
R = 2.0 ** -40
XR = [acb(arb(t.real.mid(), R), arb(t.imag.mid(), R)) for t in X]   # contains the polydisc (box in C)
FR, _ = F(XR)
K = [upper_float(abs(t)) for t in FR]
print('K max', max(K), f'({time.time()-t0:.0f}s)', flush=True)
Fv = acb_mat([[t] for t in F0])
YF = Y * Fv
eta = max(upper_float(abs(YF[i, 0])) for i in range(nU))
IYD = eye(nU) - Y * Dmat
n1 = mat_norm_upper(IYD); nY = mat_norm_upper(Y)
# finite-difference error |D_ij - J_ij(x~)| <= K_i h / (R (R - h))  (the box contains the polydisc
# of radius R in each coordinate, so Cauchy's estimates on |t| <= R apply)
Erow = max(upper_float(nU * arb(Ki) * arb(h) / (arb(R) * (arb(R) - arb(h)))) for Ki in K)
rho = upper_float(10 * arb(eta))
Crow = max(upper_float(nU * 2 * nU * arb(rho) * arb(Ki) / (arb(R) - arb(rho)) ** 2) for Ki in K)
kappa = upper_float(arb(n1) + arb(nY) * arb(Erow) + arb(nY) * arb(Crow))
ok = (kappa < 1) and (arb(eta) + arb(kappa) * arb(rho) < arb(rho))
print(f'eta = {eta:.3e}, ||I - YD|| = {n1:.3e}, ||Y|| = {nY:.3e}, FD term = {nY*Erow:.3e}, '
      f'Cauchy term = {nY*Crow:.3e}, kappa = {kappa:.3e}, rho = {rho:.3e}: contraction {"OK" if ok else "FAILED"}', flush=True)
# side conditions at every w in B_rho: monodromy enclosed with inputs of radius rho
Xr = [acb(arb(t.real.mid(), rho), arb(t.imag.mid(), rho)) for t in X]
Fr_, Ms = F(Xr)
side = True
I8 = eye(8)
for m in range(8):
    Mm = Ms[0] - I8 * LAM[m]
    kept = [i for i in range(8) if i != DROP0[m]]
    best = None
    for drop in range(8):
        cols = [c for c in range(8) if c != drop]
        dt = acb_mat([[Mm[i, c] for c in cols] for i in kept]).det()
        if not dt.contains(0): best = dt; break
    side = side and best is not None
for M, (dropP, rpiv) in ((Ms[1], DROPR[0]), (Ms[2], DROPR[1])):
    Mp = M + I8; kept = [i for i in range(8) if i != dropP]
    good = False
    for drop in range(8):
        cols = [c for c in range(8) if c != drop]
        if not acb_mat([[Mp[i, c] for c in cols] for i in kept]).det().contains(0): good = True; break
    row_nonzero = any(not (M - I8)[rpiv, c].contains(0) for c in range(8))
    side = side and good and row_nonzero
print('side conditions (rank of kept rows, pivot rows nonzero):', side, flush=True)
# exponents at infinity: Gershgorin in a numerical eigenbasis of Binf (inputs of radius rho)
As_ = residues(Xr); Binf = -(As_[0] + As_[1] + As_[2])
Bn = np.array([[complex(float(Binf[i, j].real.mid()), float(Binf[i, j].imag.mid())) for j in range(8)] for i in range(8)])
ev, V = np.linalg.eig(Bn)
Vb = acb_mat([[C(V[i, j]) for j in range(8)] for i in range(8)])
T = Vb.inv() * Binf * Vb
discs = []
for i in range(8):
    r_ = sum(float(abs(T[i, j]).upper()) for j in range(8) if j != i)
    discs.append((complex(float(T[i, i].real.mid()), float(T[i, i].imag.mid())), r_ + float(abs(T[i, i]).rad()) if hasattr(abs(T[i, i]), 'rad') else r_))
print('Gershgorin discs of Binf:', [(np.round(c, 10), f'{r:.1e}') for c, r in discs], flush=True)
Einf_frac = [str(Fr(round(c.real * 12), 12)) for c, r in discs]
# Rigorous eigenvalue localization, separate from the display-only float discs.
rigorous_disc_bounds=[]
for i,label in enumerate(Einf_frac):
 e=Fr(label);e0=acb(e.numerator)/e.denominator
 rad=sum((abs(T[i,j])for j in range(8)if j!=i),arb(0))
 bound=abs(T[i,i]-e0)+rad
 assert bound<arb(1)/10**10
 rigorous_disc_bounds.append(upper_float(bound))
json.dump({'eta': eta, 'kappa': kappa, 'rho': rho, 'contraction': ok, 'side': side,
           'Einf_num': Einf_frac, 'disc_radius_max': max(r for c, r in discs), 'rigorous_disc_bounds':rigorous_disc_bounds, 'norm_I_minus_YD':n1, 'norm_Y':nY, 'FD_row_bound':Erow, 'Cauchy_row_bound':Crow, 'Kmax':max(K), 'R':R, 'h':h, 'dimension':nU, 'drops':DROP0, 'reflection_pivots':DROPR, 'center_sha256':hashlib.sha256(Path('center_g.json').read_bytes()).hexdigest(), 'target_sha256':hashlib.sha256(Path('mtuple.json').read_bytes()).hexdigest()},
          open('certM_rerun_g.json', 'w'))
assert ok and side
print("VERIFIED from center data",time.time()-t0,flush=True)
