"""Check: for the completed Hurwitz family Lambda_t(s) = pi^(-s/2) Gamma(s/2) zeta(s, 1+t) (the user's 'completed shifted
family', defect preprint section 5), the first-order motion of a zero rho = 1/2 + i gamma of Lambda_0 splits as
    Re rho'(0) =  Im Phi_minus(rho) / Z'(gamma),     Im rho'(0) = -Phi_plus(rho) / Z'(gamma),
where Phi = d/dt Lambda_t |_{t=0} = pi^(-s/2) Gamma(s/2) (-s zeta(s+1)), Phi_plus/minus(s) = (Phi(s) +/- Phi(1-s))/2 are its
parts invariant / anti-invariant under s -> 1-s, and Z(gamma) = Lambda_0(1/2 + i gamma) (real on the critical line).
So the anti-invariant part of the variation moves a zero off the line, the invariant part moves it along the line.
Also checks that Phi_plus is real and Phi_minus purely imaginary on the line (the preprint's 'critical-line separation').
mpmath; N zeros from the command line (default 200)."""
import sys
import mpmath as mp
sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200


def G(s):
    return mp.pi ** (-s / 2) * mp.gamma(s / 2)


def Lam0(s):
    return G(s) * mp.zeta(s)


def Phi(s):
    return G(s) * (-s * mp.zeta(s + 1))


worst_re = worst_im = worst_sep = mp.mpf(0)
right = 0
for n in range(1, N + 1):
    rho = mp.zetazero(n)
    g = rho.imag
    v = rho * mp.zeta(rho + 1) / mp.zeta(rho, 1, 1)          # velocity from the jet formula (zeros of zeta = zeros of Lambda_0)
    Zp = mp.diff(lambda x: mp.re(Lam0(mp.mpf(1) / 2 + 1j * x)), g)  # Z'(gamma), Z real on the line
    P, Q = Phi(rho), Phi(1 - rho)
    Pp, Pm = (P + Q) / 2, (P - Q) / 2
    worst_sep = max(worst_sep, abs(mp.im(Pp)) / abs(Pp), abs(mp.re(Pm)) / abs(Pm))
    re_pred, im_pred = mp.im(Pm) / Zp, -mp.re(Pp) / Zp
    worst_re = max(worst_re, abs(re_pred - v.real) / abs(v.real))
    worst_im = max(worst_im, abs(im_pred - v.imag) / abs(v.imag))
    right += v.real > 0
    if n <= 5:
        print(f"n={n} gamma={mp.nstr(g, 10)} Re v={mp.nstr(v.real, 10)} pred={mp.nstr(re_pred, 10)} "
              f"Im v={mp.nstr(v.imag, 10)} pred={mp.nstr(im_pred, 10)}")
print(f"N={N}: right-movers {right}; max rel. error Re: {mp.nstr(worst_re, 3)}, Im: {mp.nstr(worst_im, 3)}; "
      f"max |Im Phi+|/|Phi+|, |Re Phi-|/|Phi-| on the line: {mp.nstr(worst_sep, 3)}")
