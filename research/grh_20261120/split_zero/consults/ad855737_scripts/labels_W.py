"""Labels of zeros under the Hurwitz deformation zeta(s,1+t), against the corrected Gram rule.
For each zero rho_n = 1/2 + i g_n (mpmath.zetazero), compute
  v = rho zeta(rho+1)/zeta'(rho)               (velocity at t=0)
  label: right iff Re v > 0
  rule (BOOLEAN_LABEL note): right iff frac((theta(g)+phi)/pi) < 1/2, phi = arg zeta(3/2+ig)
  W_n = S_mid(g_n) - phi/pi with S_mid(g_n) = n - 3/2 - theta(g_n)/pi  (midpoint convention, simple zeros)
Claims tested: (A) right iff (W_n mod 2) in (0,1); (B) rule == label iff (W_n mod 2) in (-1/2,1/2].
Also: running sum of v against i T^2/(4 pi); consecutive-label agreement.
usage: labels_W.py n_start n_end outfile"""
import sys, mpmath as mp
mp.mp.dps = 20
a, b, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
f = open(out, "w")
sv = mp.mpc(0); right = 0; rule_ok = 0; A_ok = 0; B_ok = 0; same = 0; prev = None; first_fail = None
for n in range(a, b + 1):
    rho = mp.zetazero(n); g = rho.imag
    v = rho * mp.zeta(rho + 1) / mp.zeta(rho, 1, 1)
    sv += v
    lab = 1 if v.real > 0 else 0
    th = mp.siegeltheta(g); phi = mp.arg(mp.zeta(rho + 1))
    f1 = ((th + phi) / mp.pi) % 1
    rule = 1 if f1 < 0.5 else 0
    W = (n - mp.mpf(1.5) - th / mp.pi) - phi / mp.pi
    Wm = W % 2
    A = 1 if (0 < Wm < 1) else 0
    B = 1 if (Wm <= 0.5 or Wm > 1.5) else 0
    right += lab; rule_ok += (rule == lab); A_ok += (A == lab); B_ok += (B == (rule == lab))
    if rule != lab and first_fail is None: first_fail = (n, float(g), float(W))
    if prev is not None: same += (prev == lab)
    prev = lab
    f.write("%d\t%.6f\t%d\t%d\t%.6f\t%.6e\t%.6e\n" % (n, float(g), lab, rule, float(W), float(v.real), float(v.imag)))
N = b - a + 1
T = float(g)
print(f"zeros {a}..{b} (T={T:.2f}): right {right}/{N}; rule matches {rule_ok}/{N}; claim A {A_ok}/{N}; claim B {B_ok}/{N}; "
      f"consecutive same {same}/{N-1}; first rule failure {first_fail}")
print(f"sum v = {complex(sv)};  i T^2/(4 pi) = {T*T/(4*float(mp.pi)):.2f}i")
