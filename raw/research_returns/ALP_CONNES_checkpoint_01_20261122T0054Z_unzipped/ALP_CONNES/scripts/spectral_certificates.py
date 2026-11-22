#!/usr/bin/env python3
"""Exact symbolic checks for AC-S04, AC-S05, AC-S11, and AC-S12.

These checks certify the displayed finite algebra, not analytic convergence.
They use no approximate zero data and no presumed proof of RH.
"""
import json
from datetime import datetime, timezone
from pathlib import Path
import sympy as s

u, z, y, lam, t, n, c = s.symbols("u z y lam t n c", positive=True)
pi = s.pi

# Mellin integral: integral_0^infinity u^(z+k-1) exp(-pi*u^2) du.
def gaussian_mellin(k):
    return s.Rational(1, 2)*pi**(-(z+k)/2)*s.gamma((z+k)/2)

source_mellin = pi**2*gaussian_mellin(4)-s.Rational(3,2)*pi*gaussian_mellin(2)
xi_mellin = s.Rational(1,2)*z*(z-1)*pi**(-z/2)*s.gamma(z/2)
ratio = s.simplify(s.expand_func(source_mellin/xi_mellin))
assert ratio == s.Rational(1, 4)
assert s.simplify(4*source_mellin-xi_mellin) == 0

h = 2*pi*u**2*(2*pi*u**2-3)*s.exp(-pi*u**2)
log_derivative_polynomial = s.expand(s.diff(u**s.Rational(1,2)*h,u)*u
                                    /(u**s.Rational(1,2)*s.exp(-pi*u**2)))
assert s.expand(log_derivative_polynomial
                +pi*u**2*(8*pi**2*u**4-30*pi*u**2+15)) == 0

def comm(a,b):
    return a*b-b*a

# Buffer two rows: all degree-two commutator identities are checked away
# from the artificial final truncation boundary.
size = 10
N = s.diag(*range(size))
Q = N+c*s.eye(size)
B = s.zeros(size)
for j in range(size-1):
    B[j,j+1] = B[j+1,j] = s.sqrt((j+1)*(j+2*c))
C = comm(B,N)
H = -s.I*B
Ep_old, Em_old = s.I*Q/2+C/4, -s.I*Q/2+C/4
Ep, Em = s.I*Q+C/2, -s.I*Q+C/2
def interior_zero(M):
    return all(s.simplify(v)==0 for v in M[:size-2,:size-2])
assert interior_zero(comm(Ep_old,Em_old)-H/4)
assert interior_zero(comm(Ep,Em)-H)
assert interior_zero(comm(H,Ep)-2*Ep)
assert interior_zero(comm(H,Em)+2*Em)
assert s.expand((n+1)*(n+2*c)-n*(n-1+2*c)-2*(n+c)) == 0

p = lam**2+y**2
liouville_extra = s.diff(p,y,2)/4-s.diff(p,y)**2/(16*p)
assert s.simplify(liouville_extra-s.Rational(1,4)-lam**2/(4*p)) == 0
transformed = s.simplify(liouville_extra.subs(y,lam*s.sinh(t)))
assert s.simplify(transformed-s.Rational(1,4)-1/(4*s.cosh(t)**2)) == 0

result = {
    "date_utc": datetime.now(timezone.utc).isoformat(),
    "method": "exact symbolic algebra with SymPy",
    "model": "GPT-6 Astra Pro",
    "effort": "inherited/not separately observable",
    "checks": {
        "AC-S04_source_Mellin_ratio": str(ratio),
        "AC-S04_corrected_Mellin_ratio": "1",
        "AC-S05_tail_derivative": str(log_derivative_polynomial),
        "AC-S11_source_commutator": "[e_plus,e_minus] = h/4",
        "AC-S11_corrected_relations": "all three standard sl2 relations pass for symbolic c > 0",
        "AC-S11_recurrence": "b_n^2=(n+1)(n+2*c)",
        "AC-S12_Liouville_extra_potential": "1/4 + 1/(4*cosh(t)^2)",
    },
    "scope": "Finite algebra only; no analytic, formal Lean, or independent-human verification claimed."
}
out = Path(__file__).resolve().parents[1]/"evidence"/"spectral_certificates.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
