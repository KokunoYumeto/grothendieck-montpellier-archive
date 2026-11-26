#!/usr/bin/env python3
"""Unconditional exact-ball proof that h(Q(zeta7,E49[3]))=1.

Uses the normalized autocorrelation kernel specified in the companion paper.
The original independent certificate is preserved in the accompanying record.
Odlyzko (1990), printed p.122, equation (2.3), gives for a totally complex
degree-n field log(rd) >= log(B)-8*b/(3*n). All prime terms are discarded.
The nonnegative autocorrelation kernel below makes the bound unconditional.
An unramified extension of the degree-48 field, if nontrivial, has degree
at least96; the same root discriminant is then impossible.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import flint
from flint import arb, acb, ctx

ctx.prec = 192
pi = arb.pi()
b = arb(51)/5
eps = arb(1)/(2**14)

def H(t):
    return ((2-t)*(1+(pi*t).cos()/2)/3
            + (pi*t).sin()/(2*pi))

def integrand(z, analytic):
    return (1-H(z/b)/(z/2).cosh())/(2*(z/2).sinh())

middle_c = acb.integral(integrand, eps, 2*b,
                        rel_tol=arb(2)**(-120), abs_tol=arb(2)**(-120))
assert middle_c.is_finite() and middle_c.imag.contains(0)
middle = middle_c.real
tail = -(b/2).tanh().log()
# On [0,eps] the integrand lies between0 and x, as proved in the companion paper.
endpoint_upper = eps*eps/2
logB_lower = (8*pi).log()+arb.const_euler()-middle-tail-endpoint_upper
lower96 = (logB_lower-(8*b/3)/96).exp()
lower144 = (logB_lower-(8*b/3)/144).exp()
rdK0 = (arb(3).log()*42/48+arb(7).log()*44/48).exp()
assert lower96 > arb(1585)/100
assert lower144 > arb(1742)/100
assert rdK0 < arb(1557)/100
assert lower96 > rdK0
assert 3**21*7**22 < 16**24

out = {
    'model': 'GPT-6 Astra Pro',
    'effort': 'not exposed', 'type': 'reproducible certified computation',
    'completed_utc': datetime.now(timezone.utc).isoformat(),
    'python_flint_version': flint.__version__, 'precision_bits': ctx.prec,
    'kernel_parameter_b': '51/5', 'epsilon': '1/16384',
    'base_degree': 48, 'base_discriminant': '3^42*7^44',
    'minimum_nontrivial_unramified_extension_degree': 96,
    'middle_integral_ball': str(middle), 'tail_ball': str(tail),
    'endpoint_integral_upper_ball': str(endpoint_upper),
    'B_lower_ball': str(logB_lower.exp()),
    'degree96_root_discriminant_lower_ball': str(lower96),
    'degree144_root_discriminant_lower_ball': str(lower144),
    'base_root_discriminant_ball': str(rdK0),
    'gap_at_degree96_ball': str(lower96-rdK0),
    'certified_inequalities': ['rd(K0)<15.57', 'bound(degree>=96)>15.85'],
    'conclusion': 'h(K0)=1; no assertion about h(K) or h(M)',
    'all_assertions': 'PASS',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
dest = Path(__file__).with_suffix('.json')
if dest.exists():
    raise SystemExit('Refusing to overwrite existing certificate output')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
