#!/usr/bin/env python3
"""Remaining-degree exact moment probe; not a sector certificate.
Copied unchanged quadrature functions from frozen DO125, for degrees164..167.
All source and endpoint geometry are separate obligations.
"""
from fractions import Fraction as F
from math import factorial,isqrt
from pathlib import Path
from datetime import datetime,timezone
import json,time,sys,hashlib
sys.set_int_max_str_digits(0)
checks=[]
def ck(v,label='exact moment inequality'):
    if not v:raise AssertionError(label)
    checks.append(label)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
PREC = 256
QS = 1 << PREC
SCALE = 700
j = 147
lam = F(29, 20)
rate = F(3514, 29)
fac = factorial(j - 1)

def ceildiv(a, b):
    return -(-a // b)

def loq(x):
    return x.numerator * QS // x.denominator

def hiq(x):
    return ceildiv(x.numerator * QS, x.denominator)

def expminus(x):
    """Alternating Taylor at x/2^m <= 1/16, then outward squaring."""
    ck(x >= 0, 'exact inequality or identity')
    m = 0
    y = x
    while y > F(1, 16):
        y /= 2
        m += 1
    term = F(1)
    total = term
    for n in range(1, 26):
        term *= -y / F(n)
        total += term
        if n == 24:
            upper = total
    lower = total
    ck(0 < lower <= upper, 'exact inequality or identity')
    l, u = (loq(lower), hiq(upper))
    for _ in range(m):
        l = l * l // QS
        u = ceildiv(u * u, QS)
    return (l, u)

def inverse_sqrt(x):
    ck(x > 0, 'exact inequality or identity')
    n = isqrt((x.denominator << 2 * PREC) // x.numerator)
    ck(n * n * x.numerator <= x.denominator << 2 * PREC, 'exact inequality or identity')
    ck((n + 1) * (n + 1) * x.numerator > x.denominator << 2 * PREC, 'exact inequality or identity')
    return (n, n + 1)

def scaled_value(t, expbounds=None, numer=None):
    """2^700 times density. Optional numerator endpoint gives interval max."""
    if expbounds is None:
        expbounds = expminus(lam * t)
    n = t if numer is None else numer
    rational = F(1 << SCALE, fac) * n ** (j - 1) * (F(4) / (t + 4)) ** 166
    root = inverse_sqrt(t * (1 + t / 2) * (1 + t / rate))
    low = rational.numerator * expbounds[0] * root[0] // (rational.denominator * QS)
    high = ceildiv(rational.numerator * expbounds[1] * root[1], rational.denominator * QS)
    return (low, high)

def derivative_bounds(a, b):
    low = F(2 * j - 3, 2) / b - F(166) / (a + 4) - F(1, 2) / (a + 2) - F(1, 2) / (a + rate) - lam
    high = F(2 * j - 3, 2) / a - F(166) / (b + 4) - F(1, 2) / (b + 2) - F(1, 2) / (b + rate) - lam
    first = max(low * low, high * high)
    second = F(2 * j - 3, 2) / (a * a) + F(166) / (a + 4) ** 2 + F(1, 2) / (a + 2) ** 2 + F(1, 2) / (a + rate) ** 2
    return first + second

def enclose(degree):
    global j, fac
    j = degree
    fac = factorial(j - 1)
    started = datetime.now(timezone.utc).isoformat()
    clock = time.monotonic()
    step = 128
    left = F(1)
    right = F(64)
    h = F(1, step)
    n = 63 * step
    last_exp = expminus(lam * left)
    last = scaled_value(left, last_exp)
    trap_lo = trap_hi = err_hi = 0
    for ix in range(n):
        a = left + ix * h
        b = a + h
        nextexp = expminus(lam * b)
        nxt = scaled_value(b, nextexp)
        trap_lo += (last[0] + nxt[0]) // (2 * step)
        trap_hi += ceildiv(last[1] + nxt[1], 2 * step)
        fmax = scaled_value(a, last_exp, numer=b)[1]
        db = derivative_bounds(a, b) * h ** 3 / 12
        err_hi += ceildiv(fmax * db.numerator, db.denominator)
        last_exp = nextexp
        last = nxt
        if (ix + 1) % 2048 == 0:
            print('completed_intervals', ix + 1, 'seconds', round(time.monotonic() - clock, 2), flush=True)
    left_tail = F(1 << SCALE, fac) / F(2 * j - 1, 2)
    left_hi = hiq(left_tail)
    ck(F(2 * j - 337, 2) < 0, 'exact inequality or identity')
    sqrt_upper = inverse_sqrt(F(1) / (2 * rate))[1]
    tail_rat = F((1 << SCALE) * 4 ** 166, fac) * right ** (j - 169) / lam
    rootT = inverse_sqrt(F(1) / right)[1]
    tail_hi = ceildiv(tail_rat.numerator * sqrt_upper * rootT * last_exp[1], tail_rat.denominator * QS * QS)
    lower = max(0, trap_lo - err_hi)
    upper = trap_hi + err_hi + left_hi + tail_hi
    ck(0 < lower < upper, 'exact inequality or identity')
    out = {'status': 'PASS_EXACT_POSITIVE_MOMENT_ENCLOSURE', 'started_utc': started, 'completed_utc': datetime.now(timezone.utc).isoformat(), 'j': j, 'lambda': '29/20', 'half_gamma_rate': '3514/29', 'scale_exponent': SCALE, 'fixed_precision': PREC, 'intervals': n, 'step': str(h), 'lower': {'numerator': str(lower), 'denominator': str(QS << SCALE)}, 'upper': {'numerator': str(upper), 'denominator': str(QS << SCALE)}, 'scaled_components': {'trapezoid_lower': str(trap_lo), 'trapezoid_upper': str(trap_hi), 'second_derivative_error_upper': str(err_hi), 'left_tail_upper': str(left_hi), 'right_tail_upper': str(tail_hi)}, 'relative_interval_width': str(F(upper - lower, lower)), 'whole_boundaries': '[0,1], [1,64], [64,infinity); no tail omitted', 'arithmetic': 'integer/Fraction/isqrt only; exp via alternating Taylor and outward squaring; trapezoid error by exact local second derivative bound'}
    return out

rows=[enclose(j) for j in (164,165,166,167)]
P=Path(__file__).resolve().parent
result={'status':'PASS_EXACT_MOMENTS_ONLY_NO_SECTOR_VERDICT','completed_utc':datetime.now(timezone.utc).isoformat(),'assertions':len(checks),'moment_enclosures':rows,'script_sha256':sha(Path(__file__)),'frozen_quadrature_source_sha256':sha(P/'closed_positive_central_mixture_support_twenty_seven_certificate.py')}
(P/'quotient_remaining_moments_probe.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'assertions':len(checks),'status':result['status'],'completed_utc':result['completed_utc']},indent=2))
