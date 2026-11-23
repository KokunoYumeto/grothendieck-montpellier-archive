"""Exact rational certificates for the chosen genus-three period/theta model.

The logical certificate uses Fraction arithmetic, Machin's identity and
alternating Taylor bounds. mpmath is used only for separately labelled
diagnostic approximations. This is a mathematical computation, not a Lean
formal certificate. Run with Python 3; output is theta_certificate.json.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product
from pathlib import Path
import json
import datetime


def atan_bounds(x, terms=40):
    s = sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    t = (-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(s, s+t), max(s, s+t)


def sin_bounds(x, terms=24):
    s = sum(((-1)**k*x**(2*k+1)/factorial(2*k+1) for k in range(terms)), F(0))
    t = (-1)**terms*x**(2*terms+1)/factorial(2*terms+1)
    return min(s, s+t), max(s, s+t)


def ceil_fraction(x):
    return -((-x.numerator)//x.denominator)


def outer_grid(a, b, scale=10**6):
    return F((a*scale).__floor__(), scale), F(ceil_fraction(b*scale), scale)


def exp_minus_upper(t, terms=40, scale=10**12):
    assert t >= 0
    # e^t is bounded BELOW by its finite positive Taylor sum.
    s = sum((t**k/factorial(k) for k in range(terms+1)), F(0))
    return F(ceil_fraction(scale/s), scale)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


a5 = atan_bounds(F(1, 5))
a239 = atan_bounds(F(1, 239))
pi = (16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0])
assert pi[0] > F(314159, 100000)
abc = []
for k in (1, 2, 3):
    lo = sin_bounds(k*pi[0]/7)[0]
    hi = sin_bounds(k*pi[1]/7)[1]
    abc.append(outer_grid(lo, hi))
a, b, c = abc
d = add(add(a,b),neg(c))
e = add(add(add(a,a),a),add(b,neg(c)))
Y = [[c,a,d],[a,e,a],[d,a,c]]
gershgorin = [Y[i][i][0]-sum(max(abs(Y[i][j][0]),abs(Y[i][j][1])) for j in range(3) if i!=j) for i in range(3)]
assert min(gershgorin) > F(6,25)

cutoff = 3
finite = F(0)
for n in product(range(-cutoff,cutoff+1),repeat=3):
    if n == (0,0,0):
        continue
    q = F(0)
    for i in range(3):
        for j in range(3):
            mult=n[i]*n[j]
            q += mult*(Y[i][j][0] if mult>=0 else Y[i][j][1])
    assert q > 0
    finite += exp_minus_upper(F(314159,100000)*q)

# pi * lambda_min(Y) > 3/4. For |k|>N,
# (N+1+j)^2 >= (N+1)^2+(2N+3)j.
aa = F(3,4)
u = exp_minus_upper(aa)
one_dim = 1+2*u/(1-u)
tail_first = exp_minus_upper(aa*(cutoff+1)**2)
tail_ratio = exp_minus_upper(aa*(2*cutoff+3))
tail = 3*(2*tail_first/(1-tail_ratio))*one_dim**2
total=finite+tail
assert total < F(3,8)

output={
  'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'method':'exact rational outward bounds; no floating-point premises',
  'pi_bounds':[str(x) for x in pi],
  'sin_pi_k_over_7_bounds':[[str(x) for x in v] for v in abc],
  'Y_bounds':[[[str(x) for x in v] for v in row] for row in Y],
  'gershgorin_lower_bounds':[str(x) for x in gershgorin],
  'theta_abs_tail_cube':cutoff,
  'finite_abs_sum_upper':str(finite),
  'outside_cube_tail_upper':str(tail),
  'total_abs_sum_upper':str(total),
  'total_abs_sum_upper_decimal_diagnostic':float(total),
  'conclusions':['lambda_min(Im tau)>6/25','abs(theta(0,tau)-1)<3/8','abs(theta(0,tau))>5/8'],
  'scope':'chosen actual principal theta line/germ; not an automorphic MainX certificate'
}
dest=Path(__file__).resolve().parents[1]/'evidence'/'theta_certificate.json'
dest.parent.mkdir(parents=True,exist_ok=True)
dest.write_text(json.dumps(output,indent=2))
print(json.dumps({k:output[k] for k in ['method','total_abs_sum_upper_decimal_diagnostic','conclusions']},indent=2))
