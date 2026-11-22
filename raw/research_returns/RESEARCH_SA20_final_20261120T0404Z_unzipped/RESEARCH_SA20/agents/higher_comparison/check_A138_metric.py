"""Exact algebraic certificates for the approximation part of A.138.

The general finite-piece lower bound and the infinitesimal implication
are proved in the text.  We check its polynomial identities symbolically
and verify explicit finite sharp approximants using rational arithmetic.
No numerical assertion about all infinitesimals is made by this script.
"""
from fractions import Fraction as Q
import json
from time import perf_counter

import sympy as sp

started = perf_counter()
checks = []


def check(label, condition):
    assert bool(condition), label
    checks.append({"check": label, "passed": True})


a, b, x, y, c, d, s = sp.symbols("a b x y c d s")
error = lambda z: z**2 - (c*z+d)
check("affine midpoint second difference",
      sp.expand(error(a)+error(b)-2*error((a+b)/2)-(b-a)**2/2) == 0)
homotopy = lambda z: (1-s)*z**2+s*z
check("isotopy monotonicity factorization",
      sp.expand(homotopy(y)-homotopy(x)
                -(y-x)*((1-s)*(x+y)+s)) == 0)
sharp_line = (a+b)*x-a*b-(b-a)**2/8
check("sharp affine error normal form",
      sp.expand(x**2-sharp_line
                -((x-(a+b)/2)**2-(b-a)**2/8)) == 0)
check("left endpoint of isotopy", sp.expand(homotopy(0)) == 0)
check("right endpoint of isotopy", sp.expand(homotopy(1)-1) == 0)

certificates = []
for count in (1, 2, 3, 5, 8):
    radius = Q(1, 8*count*count)
    previous_right = None
    for index in range(count):
        left, right = Q(index, count), Q(index+1, count)
        middle = (left+right)/2
        slope = left+right
        intercept = -left*right-radius
        affine = lambda z: slope*z+intercept
        check(f"m={count}, piece={index}: left extremum",
              left*left-affine(left) == radius)
        check(f"m={count}, piece={index}: midpoint extremum",
              middle*middle-affine(middle) == -radius)
        check(f"m={count}, piece={index}: right extremum",
              right*right-affine(right) == radius)
        if previous_right is not None:
            check(f"m={count}, piece={index}: continuous join",
                  affine(left) == previous_right)
        previous_right = affine(right)
    certificates.append({"affine_pieces": count,
                         "sharp_uniform_error": str(radius)})

print(json.dumps({
    "status": "PASS",
    "checks": len(checks),
    "failed": 0,
    "elapsed_seconds": perf_counter()-started,
    "finite_certificates": certificates,
    "details": checks,
}, indent=2))
