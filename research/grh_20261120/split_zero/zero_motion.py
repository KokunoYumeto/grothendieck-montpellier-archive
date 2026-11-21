"""First-order motion of the zeros of zeta under the split-zero deformation L_t(s) = sum (n+t)^(-s) = zeta(s, 1+t).
From the user's jet formula d/dt L_t(s) = -s L_t(s+1): a simple zero rho of zeta moves with velocity
v(rho) = rho * zeta(rho+1) / zeta'(rho) at t = 0. We record Re v (motion off the critical line) for the first N zeros,
and check v against a finite difference of the actual zero of the Hurwitz zeta at small t."""
import sys
import mpmath as mp
sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100
pos = neg = 0
rows = []
for k in range(1, N + 1):
    rho = mp.zetazero(k)
    dz = mp.zeta(rho, 1, 1)              # zeta'(rho)
    v = rho * mp.zeta(rho + 1) / dz
    rows.append((k, rho.imag, v.real, v.imag))
    if v.real > 0:
        pos += 1
    else:
        neg += 1
for k, g, vr, vi in rows[:12]:
    print(f"zero {k:4d}  gamma={mp.nstr(g, 12):>16}  Re v={mp.nstr(vr, 8):>14}  Im v={mp.nstr(vi, 8):>14}")
print(f"first {N} zeros: Re v > 0 for {pos}, Re v < 0 for {neg}")
# check with the actual Hurwitz zero at t = 1e-6 for the first zero
t = mp.mpf("1e-6")
rho1 = mp.zetazero(1)
rt = mp.findroot(lambda s: mp.zeta(s, 1 + t), rho1)
print("finite-difference velocity at zero 1:", mp.nstr((rt - rho1) / t, 10), " predicted:", mp.nstr(rows[0][2] + 1j * rows[0][3], 10))
