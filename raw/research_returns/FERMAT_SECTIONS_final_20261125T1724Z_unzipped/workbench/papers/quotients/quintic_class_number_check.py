#!/usr/bin/env python3
"""Quintic class-number certificate.

Model-generated mathematical certificate; GPT-6 Astra Pro.
The original independent reconstruction is preserved in the check records.

Primary formula: Odlyzko (1990), JTNB 2(1), printed p.122, Eq.(2.3).
The nonnegative kernel below is the normalized autocorrelation of
g(t)=1+cos(pi*t) on [-1,1], zero elsewhere. Consequently its Fourier
transform is nonnegative and F(x)=H(x/b)/cosh(x/2) is admissible
UNCONDITIONALLY. The 1976 table description confirms this kernel, but
no decimal number from any table is used in the proof.

For a totally complex degree-240 field with three primes of norm 81,
  log(rd) >= log(8*pi)+Euler-I +(f81-8*b/3)/240,
  I = integral_0^infty (1-F(x))/(2*sinh(x/2)) dx.

The integral from eps to 2b is computed by rigorous acb quadrature.
The tail beyond 2b is exactly -log(tanh(b/2)).
For 0<=x<=eps, 0<=H(x/b)<=1, H(0)=1, H'(0)=0, |H''|<=6.
Thus 1-H(x/b)<=3*x*x/(b*b), and 1-sech(x/2)<=x*x/8.
Since b>=2, 0<=(1-F(x))/(2*sinh(x/2))<=x, so the omitted
endpoint integral is at most eps**2/2. We use this UPPER bound in
the negative archimedean term, producing a certified LOWER bound.

All inputs and acceptance thresholds are integers or exact rationals.
Arb balls, not ordinary floating point, are used throughout.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

import flint
from flint import acb, arb, ctx


def main():
    ctx.prec = 192
    pi = arb.pi()
    b = arb(51) / 5
    eps = arb(1) / (2**14)

    def H(t):
        return ((2-t)*(1+(pi*t).cos()/2)/3
                + (pi*t).sin()/(2*pi))

    def integrand(z, analytic):
        # This expression is meromorphic on C. Ball evaluation returns
        # nonfinite balls on pole-containing domains, so the analytic
        # flag needs no extra branch handling.
        return (1-H(z/b)/(z/2).cosh())/(2*(z/2).sinh())

    middle_complex = acb.integral(
        integrand, eps, 2*b,
        rel_tol=arb(2)**(-120), abs_tol=arb(2)**(-120)
    )
    assert middle_complex.is_finite()
    assert middle_complex.imag.contains(0)
    middle = middle_complex.real
    tail = -(b/2).tanh().log()
    endpoint_upper = eps*eps/2
    log_B_lower = (8*pi).log() + arb.const_euler() - (
        middle + tail + endpoint_upper
    )
    B_lower = log_B_lower.exp()
    log81 = arb(81).log()
    f81 = 6*log81*H(log81/b)/((log81/2).cosh()*9)
    E = 8*b/3
    lower = (log_B_lower + (f81-E)/240).exp()
    rd_K = (arb(3).log()*76/80 + arb(5).log()*94/80).exp()

    # Comparisons of balls certify the stated strict inequalities.
    assert B_lower > arb(21046)/1000
    assert f81 > arb(472)/1000
    assert lower > arb(18828)/1000
    assert rd_K < arb(18818)/1000
    assert lower > rd_K

    here = Path(__file__)
    out = {
        "model": "GPT-6 Astra Pro",
        "effort": "not exposed",
        "type": "independent original certified computation",
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "python_flint_version": flint.__version__,
        "precision_bits": ctx.prec,
        "b_exact": "51/5",
        "epsilon_exact": "1/16384",
        "degree": 240,
        "prime_norm": 81,
        "number_of_known_primes": 3,
        "middle_integral_ball": str(middle),
        "tail_exact_formula_ball": str(tail),
        "endpoint_integral_upper_ball": str(endpoint_upper),
        "log_B_lower_ball": str(log_B_lower),
        "B_lower_ball": str(B_lower),
        "prime_correction_f81_ball": str(f81),
        "E_exact": "136/5",
        "root_discriminant_lower_ball": str(lower),
        "root_discriminant_K_ball": str(rd_K),
        "gap_ball": str(lower-rd_K),
        "certified_rational_bounds": [
            "B_lower > 21046/1000",
            "f81 > 472/1000",
            "rd(hypothetical cubic extension) > 18828/1000",
            "rd(K) < 18818/1000",
        ],
        "assertions_passed": True,
        "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
    }
    destination = here.with_suffix(".json")
    destination.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
