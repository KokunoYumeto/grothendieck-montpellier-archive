"""Rigorous four-value Dirichlet certificate for NN-A034.

The mathematical tail proof and Artin factorization are in the accompanying
TeX argument. No host-clock timestamp is used; events are recorded separately.
"""
from pathlib import Path
from math import isqrt
import json
from flint import arb, acb, ctx
from sympy import kronecker_symbol

ctx.dps = 60
p = 751
assert all(p % ell for ell in (2,3,5,7,11,13,17,19,23))
assert all(pow(3, (p-1)//ell, p) != 1 for ell in (2,3,5))
exponents = {}
n = 1
for k in range(p-1):
    assert n not in exponents
    exponents[n] = k % 3
    n = (3*n) % p
assert n == 1 and len(exponents) == p-1

omega = acb(-arb(1)/2, arb(3).sqrt()/2)
roots = (acb(1), omega, omega.conjugate())
def cubic(n):
    r = n % p
    return acb(0) if r == 0 else roots[exponents[r]]

tau = sum((cubic(n) * acb(arb(2*n)/p).exp_pi_i()
           for n in range(1,p)), acb(0))
epsilon = tau / arb(p).sqrt()
assert abs(epsilon).contains(1)
quarter = arb(1)/4
records = {}
boxes = {
    1: ('-0.0265980','-0.0265979','0.2188449','0.2188450'),
    5: ('1.2071682','1.2071683','-0.5141633','-0.5141632'),
    41: ('0.3418888','0.3418889','0.0415524','0.0415525'),
    205: ('0.8806422','0.8806423','2.0675988','2.0675989')
}
for d in (1,5,41,205):
    q = d*p
    eps = int(kronecker_symbol(d,p))*cubic(d)*epsilon
    assert abs(eps).contains(1)
    cutoff = 5*(isqrt(q)+1)
    value = acb(0)
    for n in range(1,cutoff+1):
        ch = int(kronecker_symbol(d,n))*cubic(n)
        if ch == 0:
            continue
        x = arb.pi()*n*n/q
        weight = x.gamma_upper(quarter,regularized=1)/arb(n).sqrt()
        value += (ch+eps*ch.conjugate())*weight
    # Gamma(1/4)>1, |chi+epsilon*conj(chi)|<=2, and monotonicity
    # give the explicit omitted-series bound proved in the TeX file.
    tail = ((arb(q)/arb.pi())**(arb(7)/4)
            *(-arb.pi()*cutoff*cutoff/q).exp()/cutoff**3)
    value = acb(value.real+arb(0,tail), value.imag+arb(0,tail))
    assert abs(value) > arb(1)/1000
    rlo,rhi,ilo,ihi = boxes[d]
    assert value.real>arb(rlo) and value.real<arb(rhi)
    assert value.imag>arb(ilo) and value.imag<arb(ihi)
    records[str(d)] = dict(conductor=q, cutoff=cutoff,
                          epsilon_ball=str(eps),
                          L_half_ball=str(value),
                          absolute_value_ball=str(abs(value)),
                          certified_rectangle=[rlo,rhi,ilo,ihi],
                          tail_bound_ball=str(tail),
                          certified_abs_gt_one_thousandth=True)
    print(d, str(value), 'tail',str(tail),flush=True)

disc_power_difference = 205**9 * 751**8 - 4371**12
assert disc_power_difference > 0
data = dict(
    finding_id='NN-A034',
    arithmetic='FLINT/Arb complex balls at60 decimal digits; exact Kronecker symbols and modular exponentiation',
    event_time_source='Authoritative tool-clock events are recorded separately; no host timestamp.',
    cubic_character=dict(prime=p,primitive_root=3,definition='chi(3^k)=exp(2*pi*i*k/3)',
                         gauss_sum_ball=str(tau),epsilon_ball=str(epsilon)),
    central_values=records,
    exact_root_discriminant_test=dict(expression='205^9 *751^8 -4371^12',
                                    integer=disc_power_difference,positive=True),
    scope='Four central Dirichlet nonvanishing values and exact root-discriminant comparison only. Artin holomorphy/factorization and the branch theorem are separately proved or cited.'
)
dest=Path(__file__).with_name('cubic_compositum_certificate.json')
dest.write_text(json.dumps(data,indent=2)+'\n')
print(dest)
