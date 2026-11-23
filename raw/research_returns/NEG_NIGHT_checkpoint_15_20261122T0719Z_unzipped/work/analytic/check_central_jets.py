"""Arb certificates for NN-A018; no GRH or central-order computation.

The classical Martinet/Fröhlich inputs are cited in central_puiseux.tex.
This script certifies the three quadratic central signs and explicit
gamma/zeta constants. Character values are exact Kronecker symbols.
"""
from pathlib import Path
import json
from flint import arb, acb, acb_series, ctx
from sympy import kronecker_symbol

ctx.dps = 70
half = acb(arb(1)/2)
values = {}
intervals = {5: ('0.23','0.24'), 41: ('1.10','1.11'), 205: ('1.17','1.18')}
for d in (5,41,205):
    value = acb(0)
    for a in range(1,d+1):
        ch = int(kronecker_symbol(d,a))
        if ch:
            value += ch * half.zeta(acb(a)/d)
    value *= acb(d)**(-half)
    lo,hi = intervals[d]
    assert value.real > arb(lo) and value.real < arb(hi)
    assert value.imag.contains(0)
    values[str(d)] = {'L_half_ball': str(value),
                      'certified_interval': [lo,hi], 'positive': True}

a_R = (arb(1)/4).digamma()/2-arb.pi().log()/2
ss = acb_series([arb(3)/2,1],2)
zs = ss.zeta()
zeta_log_derivative = (zs[1]/zs[0]).real
C_star = -a_R-zeta_log_derivative
threshold = (2*C_star).exp()
assert threshold < 4371
upper = 2+3*arb(205).log()+8*a_R
assert upper < arb('-3.5197')

data = {
    'finding_id': 'NN-A018',
    'event_time_source': 'Authoritative tool-clock events are recorded separately in CHECK_EVENTS.tsv; this certificate intentionally does not use the host clock.',
    'arithmetic': 'FLINT/Arb complex balls,70 decimal digits; exact SymPy Kronecker symbols',
    'quadratic_values': values,
    'a_R': str(a_R),
    'zeta_log_derivative_at_three_halves': str(zeta_log_derivative),
    'C_star': str(C_star),
    'exp_2_C_star': str(threshold),
    'certified_exp_2_C_star_lt_4371': True,
    'Q8_C_upper_bound': str(upper),
    'certified_Q8_C_lt_minus_3_5197': True,
    'scope': 'Central quadratic values and analytic constants only. Field data and odd Artin central order use cited classical theorems; no numerical assumption that the central order is exactly two.'
}
dest=Path(__file__).with_name('central_jets_certificate.json')
dest.write_text(json.dumps(data,indent=2)+'\n')
print(dest)
