"""Numerical check that the Tate parameter of the Legendre curve y^2=x(x-1)(x-lambda) at lambda=0 is
q = (lambda^2/256)(1+lambda+O(lambda^2)): invert j(q)=1/q+744+196884q+... at j(lambda)=256(1-lambda+lambda^2)^3/(lambda^2(1-lambda)^2).
Claude Opus 5.5 at effort max, sweep 1 (scope sections), 18 Nov 2026. usage: python -I -B tools/tate_constant_check.py"""
from mpmath import mp, mpf, findroot
mp.dps = 60
c = [744, 196884, 21493760, 864299970, 20245856256]
for e in [3, 5, 7, 9]:
    l = mpf(10) ** (-e)
    J = 256 * (1 - l + l * l) ** 3 / (l * l * (1 - l) ** 2)
    q = findroot(lambda q: 1 - J * q + sum(ci * q ** (i + 1) for i, ci in enumerate(c)), 1 / J, tol=mpf(10) ** (-80))
    r = q * 256 / (l * l)
    print(e, mp.nstr(r, 20), mp.nstr((r - 1) / l, 12))
