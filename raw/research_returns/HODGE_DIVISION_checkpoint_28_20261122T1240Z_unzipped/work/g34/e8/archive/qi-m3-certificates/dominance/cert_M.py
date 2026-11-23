# Rank certificate, part M [C]: rigorous existence of the Fuchsian system M with monodromy (a, b, c, d).
#   M: poles z = 0, 1, c0 (finite), oo; B0 = diag(beta) (beta = m/20, m in {1,3,7,9,11,13,17,19}),
#   B1 = u1 v1^T, Bc = u2 v2^T; loops from z0 = 1/2 - i (loop_path: radius 0.45, 12-gon).
# Gauge fixing: u1 (all 8 entries) and u2[j0] are fixed dyadic constants (torus + scalings), so the unknowns
# are w = (v1 (8), u2 without j0 (7), v2 (8), Q (64)): 87 unknowns. Equations F(w) = 0, 87 of them:
#   (1) v1.u1 - 1/2, (2) v2.u2 - 1/2,
#   (3) for each eigenvector e_j of a (lambda_j = exp(2 pi i beta_j)): 7 rows (one row r_j dropped) of
#       (M_0 - lambda_j) Q e_j,
#   (4) for t = b (pole 1) and t = c (pole c0), t = I - x' y'^T: 7 rows of (M + I) Q x' (one dropped), and
#       row r of (M - I) Q w_i for the 7 basis vectors w_i of ker y'^T,
#   (5) det Q - 1.
# Lemma: F(w) = 0 implies M_k Q = Q t_k for k = 0, 1, c0, with Q invertible, provided the
# dropped-row and pivot-row conditions (nonvanishing entries of left null vectors / of X) hold; these are
# checked in balls at the end.
# Existence: contraction test for G(w) = w - Y F(w) on the max-norm ball B_rho(x~) with Cauchy bounds from a
# ball evaluation of F on the polydisc P_R(x~) (inequality (*)).
import sys, json, time, pickle
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '..'); sys.path.insert(0, '.')
from cert_lib import *

CLS = sys.argv[1]; SOL = sys.argv[2]; TI = int(sys.argv[3]) if len(sys.argv) > 3 else 0
STAGE = sys.argv[4] if len(sys.argv) > 4 else 'all'
D = json.load(open('../mtuple.json'))
a_T = np.array(D['a'], dtype=int)
b_T, c_T, d_T = [np.array(m, dtype=int) for m in D[CLS][TI]]
POLES = [0.0, 1.0, 2.0 + 1.0j]
z0 = 0.5 - 1.0j
mvals = [1, 3, 7, 9, 11, 13, 17, 19]


def loop_path(z0, p, r, m=12):
    phi = np.angle(z0 - p)
    circ = [p + r * np.exp(1j * (phi + 2 * np.pi * k / m)) for k in range(m + 1)]
    return [z0] + circ + [z0]


PATHS = [loop_path(z0, p, 0.45) for p in POLES]


def dy(x, bits=30):
    return complex(round(x.real * 2**bits) / 2**bits, round(x.imag * 2**bits) / 2**bits)


# ---------- gauge fixing of the numerical solution ----------
zc = np.load(SOL); x = zc[:32]
u1, v1, u2, v2 = x[0:8].copy(), x[8:16].copy(), x[16:24].copy(), x[24:32].copy()


def fit_Q(u1, v1, u2, v2):
    from fuchs import transport as ntr
    B0 = np.diag(np.array(mvals) / 20.0).astype(complex)
    As = np.array([B0, np.outer(u1, v1), np.outer(u2, v2)])
    Ms = [ntr(As, np.array(POLES), P) for P in PATHS]
    L = np.vstack([np.kron(M, np.eye(8)) - np.kron(np.eye(8), t.T) for M, t in zip(Ms, [a_T, b_T, c_T])])
    U_, s_, Vh = np.linalg.svd(L)
    print('fit Q: sigma_min', s_[-1], 'next', s_[-2], flush=True)
    Q = Vh[-1].conj().reshape(8, 8)
    return Q / np.linalg.det(Q) ** (1 / 8)


Qn = fit_Q(u1, v1, u2, v2)
u1f = np.array([dy(t) for t in u1])
Dg = u1f / u1
u1, v1, u2, v2, Qn = u1 * Dg, v1 / Dg, u2 * Dg, v2 / Dg, Dg[:, None] * Qn
j0 = int(np.argmax(np.abs(u2)))
u2j0 = dy(u2[j0]); sc = u2j0 / u2[j0]
u2, v2 = u2 * sc, v2 / sc
U1 = [C(t) for t in u1f]; U2J0 = C(u2j0)
others = [j for j in range(8) if j != j0]
w0 = np.concatenate([v1, u2[others], v2, Qn.ravel()])


# ---------- exact target data ----------
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


# choose dropped rows / pivot rows once, from the numerical solution
def choose_rows():
    sys.path.insert(0, '..')
    from fuchs import transport as ntr
    B0 = np.diag(np.array(mvals) / 20.0).astype(complex)
    As = np.array([B0, np.outer(u1, v1), np.outer(u2, v2)])
    Ms = [ntr(As, np.array(POLES), P) for P in PATHS]
    drop0 = []
    for m in range(8):
        ln = np.exp(2j * np.pi * mvals[m] / 20)
        wl, vl = np.linalg.eig((Ms[0] - ln * np.eye(8)).T)   # left null vector
        l = vl[:, int(np.argmin(np.abs(wl)))]
        drop0.append(int(np.argmax(np.abs(l))))
    out = []
    for M in (Ms[1], Ms[2]):
        wl, vl = np.linalg.eig((M + np.eye(8)).T); l = vl[:, int(np.argmin(np.abs(wl)))]
        dropP = int(np.argmax(np.abs(l)))
        X = (np.eye(8) - M); col = X[:, int(np.argmax(np.abs(X).sum(0)))]
        rpiv = int(np.argmax(np.abs(col)))
        out.append((dropP, rpiv))
    return drop0, out


DROP0, DROPR = choose_rows()


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


def F(w, N=100, frac=0.35):
    v1, u2, v2, Q = unpack(w)
    As = residues(w); ps = [C(p) for p in POLES]
    Ms = [transport(As, ps, P, frac=frac, N=N) for P in PATHS]
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


def vec_np(v): return np.array([complex(float(t.real.mid()), float(t.imag.mid())) for t in v])


def to_acb_vec(wn): return [C(t) for t in wn]


if __name__ == '__main__':
    t0 = time.time()
    tag = f'{CLS}_{TI}'
    if STAGE in ('all', 'newton'):
        # Newton refinement at high precision with a low-precision finite-difference Jacobian
        setprec(64)
        wn = w0.copy()
        Fv, _ = F(to_acb_vec(wn), N=45)
        f0 = vec_np(Fv)
        print('initial |F| (64-bit)', np.abs(f0).max(), flush=True)
        # the 4th-root ambiguity of det Q: rescale Q so that det Q = 1
        Qn_ = wn[23:].reshape(8, 8); Qn_ = Qn_ / np.linalg.det(Qn_) ** (1 / 8); wn[23:] = Qn_.ravel()
        Fv, _ = F(to_acb_vec(wn), N=45); f0 = vec_np(Fv)
        print('after det rescale |F|', np.abs(f0).max(), flush=True)
        Jn = np.zeros((87, 87), dtype=complex); hh = 1e-7
        for j in range(87):
            wp = wn.copy(); wp[j] += hh
            Jn[:, j] = (vec_np(F(to_acb_vec(wp), N=45)[0]) - f0) / hh
        print('approx Jacobian done; cond', np.linalg.cond(Jn), f'({time.time()-t0:.0f}s)', flush=True)
        np.save(f'Japprox_{tag}.npy', Jn)
        setprec(256)
        wa = to_acb_vec(wn)
        Jinv = np.linalg.inv(Jn)
        for it in range(6):
            Fv, _ = F(wa)
            fn = vec_np(Fv); nrm = max(upper_float(abs(t)) for t in Fv)
            print(f'newton {it}: |F| <= {nrm:.3e} ({time.time()-t0:.0f}s)', flush=True)
            if nrm < 1e-60: break
            # exact-arithmetic update with the float inverse applied to the ball midpoints
            dx = [sum((C(Jinv[i, j]) * acb(Fv[j].mid()) for j in range(87)), acb(0)) for i in range(87)]
            wa = [acb(wa[i].mid()) - dx[i] for i in range(87)]
            wa = [acb(t.mid()) for t in wa]
        pickle.dump([(str(t.real.mid()), str(t.imag.mid())) for t in wa], open(f'xtilde_{tag}.pkl', 'wb'))
        print('saved x~', flush=True)

    if STAGE in ('all', 'verify'):
        setprec(256)
        xt = pickle.load(open(f'xtilde_{tag}.pkl', 'rb'))
        X = [acb(arb(a).mid(), arb(b).mid()) for a, b in xt]
        nU = 87
        # meta for part L
        pickle.dump({'u1f': [complex(t) for t in u1f], 'j0': j0, 'u2j0': complex(u2j0), 'others': others},
                    open(f'meta_{tag}.pkl', 'wb'))
        F0, Ms0 = F(X)
        print('F(x~) max upper', max(upper_float(abs(t)) for t in F0), f'({time.time()-t0:.0f}s)', flush=True)
        h = 2.0 ** -80
        Dm = [[None] * nU for _ in range(nU)]
        for j in range(nU):
            Xp = list(X); Xp[j] = X[j] + h
            Fp, _ = F(Xp)
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
        json.dump({'eta': eta, 'kappa': kappa, 'rho': rho, 'contraction': ok, 'side': side,
                   'Einf_num': Einf_frac, 'disc_radius_max': max(r for c, r in discs)},
                  open(f'certM_{tag}.json', 'w'))
        print('DONE', f'({time.time()-t0:.0f}s)', flush=True)
