"""Which zeros move right under the split-zero (Boolean) deformation, against their position in the Gram interval.
Re v = -|zeta(rho+1)| (gamma cos(theta+phi) + 1/2 sin(theta+phi)) / Z'(gamma), phi = arg zeta(3/2 + i gamma).
Records: n, frac of theta(gamma_n)/pi, frac of (theta+phi)/pi, sign of Z'(gamma_n), sign of Re v, Gram's law for zero n."""
import sys
import mpmath as mp
sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 25
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
agree_half = agree_half_corr = gram_ok = 0
right = 0
out = []
for n in range(1, N + 1):
    rho = mp.zetazero(n)
    g = rho.imag
    th = mp.siegeltheta(g)
    zp = mp.siegelz(g, derivative=1)
    z32 = mp.zeta(rho + 1)
    phi = mp.arg(z32)
    v = rho * z32 / mp.zeta(rho, 1, 1)
    s_v = 1 if v.real > 0 else -1
    right += s_v > 0
    f0 = (th / mp.pi) % 1
    f1 = ((th + phi) / mp.pi) % 1
    # Gram's law for the n-th zero: theta(gamma_n) lies in ((n-2)pi, (n-1)pi]
    k = int(mp.floor(th / mp.pi))
    gram = (k == n - 2)
    gram_ok += gram
    sz = 1 if zp > 0 else -1
    pred = -sz * (1 if (g * mp.cos(th + phi) + mp.sin(th + phi) / 2) > 0 else -1)
    assert pred == s_v, (n, pred, s_v)
    # class relative to the alternating sign: c = s_v * (-1)^n
    agree_half += (s_v > 0) == (f0 < 0.5)
    agree_half_corr += (s_v > 0) == (f1 < 0.5)
    if (s_v > 0) != (f1 < 0.5):
        print('exception n=%d gamma=%.4f f1=%.4f gram=%s' % (n, float(g), float(f1), gram))
    out.append((n, float(g), float(f0), float(f1), sz, s_v, gram))
print(f"N = {N}: right-movers {right}, left-movers {N - right}; Gram's law holds for {gram_ok}")
print(f"right-mover matches 'theta/pi mod 1 < 1/2' for {agree_half}/{N}; "
      f"with the phi-correction for {agree_half_corr}/{N}")
for r in out[:15]:
    print("n=%3d gamma=%9.4f frac(theta/pi)=%.3f frac((theta+phi)/pi)=%.3f sgnZ'=%+d sgnRe v=%+d gram=%s" % r)
