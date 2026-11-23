"""Interval certificate for correction NN-A001; python-flint/Arb, 60 decimal digits.

Computes the indexed zero with FLINT's certified zeta-zero routine and propagates
complex ball arithmetic through the jet and phase formula. The signs below are
certified inequalities, not midpoint comparisons.
"""
from flint import acb, acb_series, arb, ctx
import json
from pathlib import Path

ctx.dps = 60
out = []
for n in [1, 871, 1169]:
    rho = acb.zeta_zero(n)
    zp = acb_series([rho, 1], 3).zeta()[1]
    velocity = rho * (rho + 1).zeta() / zp
    pi = arb.pi()
    theta = acb(arb('0.25'), rho.imag / 2).lgamma().imag - rho.imag * pi.log() / 2
    phi = (rho + 1).zeta().arg()
    W = arb(n) - arb('1.5') - theta / pi - phi / pi
    delta = (1 / (2 * rho.imag)).atan()
    sine = (pi * W).sin()
    corrected_sine = (pi * W + delta).sin()
    out.append({
        'n': n, 'rho': str(rho), 'zeta_prime': str(zp),
        'velocity': str(velocity), 'W': str(W), 'delta_over_pi': str(delta / pi),
        'sine_without_correction': str(sine), 'sine_exact': str(corrected_sine),
        'certified_right': bool(velocity.real > 0),
        'certified_left': bool(velocity.real < 0),
        'exact_sign_agrees': bool((velocity.real > 0 and corrected_sine > 0)
                                  or (velocity.real < 0 and corrected_sine < 0)),
    })
assert out[2]['certified_right']
assert out[2]['exact_sign_agrees']
assert sine < 0 and corrected_sine > 0
dest = Path(__file__).with_name('label_certificate.json')
dest.write_text(json.dumps(out, indent=2) + '\n')
print(dest)
