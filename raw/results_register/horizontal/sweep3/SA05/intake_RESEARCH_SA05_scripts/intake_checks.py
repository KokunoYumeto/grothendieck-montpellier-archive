# Intake of RESEARCH_SA05 (final, INCOMPLETE, 19 Nov 2026): independent computational checks.
# Claude Opus 5.5 at effort max (agent a7b7747fd6dd29f87). Run: python -I -B intake_checks.py
# Each check prints PASS/FAIL with the computed data. No input files are read.
import itertools, json
from sympy import (symbols, sqrt, I, Rational, minimal_polynomial, Poly, factor_list, QQ, legendre_symbol,
                   simplify, nsimplify, expand, conjugate, Abs, re as sre)
from sympy.combinatorics import SymmetricGroup
import mpmath

out = {}

# 1. D.2(b): S4 is not metabelian (derived length 3), so the Taniyama group (which maps onto Gal(Qbar/Q),
#    hence onto S4 for any S4-extension of Q) has non-metabelian quotients.
S4 = SymmetricGroup(4)
series = S4.derived_series()
out['S4_derived_orders'] = [g.order() for g in series]
out['S4_metabelian'] = (series[2].order() == 1) if len(series) > 2 else True
print('1 S4 derived series orders', out['S4_derived_orders'], 'metabelian:', out['S4_metabelian'],
      'PASS' if out['S4_derived_orders'] == [24, 12, 4, 1] else 'FAIL')

# 2. A.3(c) framed counterexample: the global square classes supported at {-1, 2, 3} that are the class 3 at Q_3
#    are +-3, +-6; each must fail to be a square at one of 5, 7, 13.
res = {}
for d in (3, -3, 6, -6):
    res[d] = {p: legendre_symbol(d % p, p) for p in (5, 7, 13)}
out['residues'] = {str(k): v for k, v in res.items()}
ok2 = all(any(v == -1 for v in res[d].values()) for d in res)
print('2 Legendre symbols of +-3, +-6 at 5, 7, 13:', res, 'each excluded:', ok2, 'PASS' if ok2 else 'FAIL')

# 3. A.5 Lefschetz example over F5: alpha = 1+2i, beta = (3+sqrt(-11))/2, lambda^2 = alpha*beta.
alpha = 1 + 2*I
beta = (3 + sqrt(-11))/2
x = symbols('x')
na = simplify(alpha*conjugate(alpha)); nb = simplify(expand(beta*conjugate(beta)))
ta = simplify(alpha + conjugate(alpha)); tb = simplify(beta + conjugate(beta))
lam2 = expand(alpha*beta)
mp = minimal_polynomial(sqrt(lam2), x)
deg = Poly(mp, x).degree()
irr = len(factor_list(mp, domain=QQ)[1]) == 1
pts_a = 5 + 1 - ta; pts_b = 5 + 1 - tb
out['lefschetz'] = dict(norm_alpha=str(na), norm_beta=str(nb), trace_alpha=str(ta), trace_beta=str(tb),
                        minpoly_lambda=str(mp), degree=deg, irreducible=irr, points_alpha=str(pts_a), points_beta=str(pts_b))
ok3 = (na == 5 and nb == 5 and deg == 8 and irr)
print('3 |alpha|^2, |beta|^2 =', na, nb, '; traces', ta, tb, '; #E(F5) =', pts_a, pts_b,
      '; minpoly of lambda: degree', deg, 'irreducible', irr, 'PASS' if ok3 else 'FAIL')
# all roots of the minimal polynomial have absolute value sqrt(5) (lambda is a Weil 5-number of weight 1, lambda^2 of weight 2)
roots = Poly(mp, x).nroots(n=30)
absvals = sorted(set(round(float(abs(r))**2, 9) for r in roots))
print('  |root|^2 of the minimal polynomial:', absvals, 'PASS' if absvals == [5.0] else 'FAIL')

# 4. C.4 counterexample: an elliptic curve over F5 with Frobenius polynomial T^2 + 2T + 5 (trace -2, 8 points).
def count(a, b, p=5):
    n = 1
    for X in range(p):
        r = (X**3 + a*X + b) % p
        n += sum(1 for Y in range(p) if (Y*Y - r) % p == 0)
    return n
found = [(a, b) for a in range(5) for b in range(5) if (4*a**3 + 27*b**2) % 5 != 0 and count(a, b) == 8]
out['F5_curves_with_8_points'] = found
print('4 curves y^2 = x^3+ax+b over F5 with 8 points:', found[:6], '; disc of T^2+2T+5 =', 4 - 20,
      'PASS' if found else 'FAIL')

# 5. B.4 / Lead B2: zeta at integers: simple zeros at -2k, nonzero at 1-2k and at 0, pole at 1.
mpmath.mp.dps = 30
z = {}
for k in range(1, 6):
    z[-2*k] = (mpmath.zeta(-2*k), mpmath.zeta(-2*k, derivative=1))
    z[1-2*k] = (mpmath.zeta(1-2*k), None)
ok5 = all(abs(z[-2*k][0]) < 1e-25 and abs(z[-2*k][1]) > 1e-6 and abs(z[1-2*k][0]) > 1e-6 for k in range(1, 6))
print('5 zeta(-2k)=0 with zeta\'(-2k)!=0, zeta(1-2k)!=0 for k=1..5:', ok5, '; zeta(0) =', mpmath.zeta(0),
      'PASS' if ok5 and abs(mpmath.zeta(0) + 0.5) < 1e-25 else 'FAIL')
# Borel ranks of K_{2n-1}(Z) (n>=2): 1 for n odd, 0 for n even -> H^1(Spec Z, Q(n)); the zero of zeta at s = 1-n
ok5b = all(((n % 2 == 1) == (abs(mpmath.zeta(1-n)) < 1e-25)) for n in range(2, 12))
print('  rank pattern H^1(Z,Q(n)) = [n odd] matches the zeros of zeta at s = 1-n for n = 2..11:', ok5b,
      'PASS' if ok5b else 'FAIL')

# 6. X0(11): y^2 + y = x^3 - x^2 - 10x - 20; #E(F_p) divisible by 5 for good p (rational 5-torsion), discriminant -11^5.
def count11(p):
    n = 1
    for X in range(p):
        for Y in range(p):
            if (Y*Y + Y - (X**3 - X*X - 10*X - 20)) % p == 0:
                n += 1
    return n
b2, b4, b6, b8 = -4, -20, -79, -21  # for [a1,a2,a3,a4,a6] = [0,-1,1,-10,-20]
a1, a2, a3, a4, a6 = 0, -1, 1, -10, -20
b2 = a1*a1 + 4*a2; b4 = 2*a4 + a1*a3; b6 = a3*a3 + 4*a6; b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
disc = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
cnts = {p: count11(p) for p in (2, 3, 5, 7, 13, 17, 19, 23)}
ok6 = disc == -11**5 and all(c % 5 == 0 for c in cnts.values())
print('6 X0(11): discriminant', disc, '= -11^5:', disc == -11**5, '; #E(F_p):', cnts, 'all divisible by 5:',
      all(c % 5 == 0 for c in cnts.values()), 'PASS' if ok6 else 'FAIL')

# 7. C.1(c): the Fermat quartic X^4+Y^4=Z^4 is smooth of genus 3 and contains (0:1:1).
X, Y, Z = symbols('X Y Z')
on = (0**4 + 1**4 - 1**4) == 0
genus = (4-1)*(4-2)//2
print('7 Fermat quartic: point (0:1:1) on the curve', on, '; genus', genus, 'PASS' if on and genus == 3 else 'FAIL')

with open(__file__.replace('intake_checks.py', 'intake_checks_output.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=1, default=str)
