# Certificate library (python-flint / Arb ball arithmetic).
# Rigorous transport for Y' = A(z) Y, A(z) = sum_k A_k/(z - p_k) (finite poles), along polygonal paths.
# At a regular centre c with d = min_k |c - p_k| and S = sum_k ||A_k||_inf, the Taylor coefficients of A
# satisfy ||a_n|| <= S/d^(n+1), so the transport T(h) = sum_n T_n h^n is majorized by (1 - |h|/d)^(-S)
# (T' = a T, T(0) = I): ||T_n|| <= binom(S + n - 1, n)/d^n. The tail sum_{n > N} is bounded by a geometric
# series with ratio q (1 + S/(N + 2)), q = |h|/d, and added as a radius to every entry.
from flint import acb, arb, acb_mat, ctx
import math

def upper_float(x):
    return math.nextafter(float(x.upper()), math.inf)

def lower_float(x):
    return math.nextafter(float(x.lower()), -math.inf)

PREC = 256


def setprec(p):
    global PREC
    PREC = p; ctx.prec = p


def C(z):
    """exact acb from a python complex/float/int (binary floats are exact rationals)."""
    if isinstance(z, acb): return z
    z = complex(z)
    return acb(z.real, z.imag)


def eye(n):
    return acb_mat([[1 if i == j else 0 for j in range(n)] for i in range(n)])


def zeros(n, m=None):
    return acb_mat(n, m if m is not None else n)


def mat_norm_upper(M):
    """upper bound for the inf-norm (max row sum of |entries|) as a float."""
    best = 0.0
    for i in range(M.nrows()):
        s = arb(0)
        for j in range(M.ncols()):
            s += abs(M[i, j])
        u = upper_float(s)
        best = max(best, u)
    return best


def add_radius(M, r):
    """M + E with |E_ij| <= r for all entries (r a float upper bound)."""
    n, m = M.nrows(), M.ncols()
    E = acb_mat([[acb(arb(0, r), arb(0, r)) for j in range(m)] for i in range(n)])
    return M + E


def tail_bound(S, q, N):
    """bound for sum_{n > N} binom(S + n - 1, n) q^n (S >= 0, 0 < q < 1), computed in upper-rounded arb."""
    S_ = arb(S); q_ = arb(q)
    # term_{N+1} = binom(S + N, N + 1) q^(N+1)
    t = arb(1)
    for n in range(1, N + 2):
        t = t * (S_ + n - 1) / n * q_
    ratio = q_ * (1 + S_ / (N + 2))
    if not (ratio < 1): raise ValueError('tail ratio >= 1')
    return upper_float(t / (1 - ratio))


def step(As, ps, Snorm, c, h, N):
    """rigorous transport matrix from c to c + h (c, h exact acb)."""
    n = As[0].nrows()
    d = min(lower_float(abs(c - p)) for p in ps)
    q = upper_float(abs(h) / arb(d))
    assert q < 0.5, q
    # Q(t) T'(t) = P(t) T(t), with Q=prod(t+c-p),
    # P=sum A_k prod_{j!=k}(t+c-p_j). This is the same ODE,
    # but costs degree(Q) matrix products per coefficient.
    def polyprod(ds):
        out = [acb(1)]
        for d0 in ds:
            new = [acb(0)] * (len(out)+1)
            for j,v in enumerate(out):
                new[j] += d0*v
                new[j+1] += v
            out = new
        return out
    ds = [c-p for p in ps]
    Q = polyprod(ds)
    P = [zeros(n) for _ in ps]
    for k,A in enumerate(As):
        coeffs = polyprod(ds[:k]+ds[k+1:])
        for j,v in enumerate(coeffs): P[j] += A*v
    T = [eye(n)]
    for k in range(N):
        rhs = zeros(n)
        for j in range(min(k,len(P)-1)+1): rhs += P[j]*T[k-j]
        for j in range(1,min(k,len(Q)-1)+1): rhs -= T[k-j+1]*(Q[j]*(k-j+1))
        T.append(rhs/(Q[0]*(k+1)))
    # Horner
    R = T[N]
    for k in range(N - 1, -1, -1):
        R = R * h + T[k]
    return add_radius(R, tail_bound(Snorm, q, N))


def stable_step(As, ps, Snorm, c, h, N):
    """rigorous transport matrix from c to c + h (c, h exact acb)."""
    n = As[0].nrows()
    d = min(lower_float(abs(c - p)) for p in ps)
    q = upper_float(abs(h) / arb(d))
    assert q < 0.5, q
    # Taylor coefficients of A at c: a_m = sum_k A_k (-1)^m / (c - p_k)^(m+1)
    ws = [1 / (c - p) for p in ps]
    a = []
    pw = list(ws)
    for m in range(N):
        am = zeros(n)
        for A, w in zip(As, pw):
            am += A * (w if m % 2 == 0 else -w)
        a.append(am)
        pw = [x * w for x, w in zip(pw, ws)]
    T = [eye(n)]
    for k in range(N):
        s = zeros(n)
        for m in range(k + 1):
            s += a[m] * T[k - m]
        T.append(s * (acb(1) / (k + 1)))
    # Horner
    R = T[N]
    for k in range(N - 1, -1, -1):
        R = R * h + T[k]
    return add_radius(R, tail_bound(Snorm, q, N))


def transport(As, ps, path, frac=0.35, N=90):
    """As: list of acb_mat residues, ps: list of acb poles, path: list of python complex vertices."""
    n = As[0].nrows()
    Snorm = upper_float(sum((arb(mat_norm_upper(A)) for A in As), arb(0)))
    T = eye(n)
    # Polynomial recurrence has severe dependency inflation on input boxes.
    wide = any(float(A[i,j].real.rad())+float(A[i,j].imag.rad()) > 1e-50 for A in As for i in range(n) for j in range(n))
    step_impl = stable_step if wide else step
    pts = [complex(p.real.mid()) + 1j * float(p.imag.mid()) for p in ps]
    for z1, z2 in zip(path[:-1], path[1:]):
        za = C(z1); zb = C(z2)
        while True:
            zc = complex(float(za.real.mid()), float(za.imag.mid()))
            rem = complex(z2) - zc
            if abs(rem) < 1e-300:
                assert za == zb, 'rounded endpoint discrepancy'
                break
            dmin = min(abs(zc - p) for p in pts)
            if abs(rem) <= frac * dmin:
                h = zb - za                       # exact
                T = step_impl(As, ps, Snorm, za, h, N) * T
                break
            hc = rem / abs(rem) * frac * dmin
            h = C(complex(round(hc.real * 2**50) / 2**50, round(hc.imag * 2**50) / 2**50))
            T = step_impl(As, ps, Snorm, za, h, N) * T
            za = za + h                           # exact (dyadics, PREC bits)
    return T
