"""Exact finite arithmetic accompanying CC-AG15.

The arbitrary-degree root-of-unity and local-index argument is a written
proof; this checker verifies only the displayed finite numerical data.
"""
from math import isqrt

p = 163
assert all(p % d for d in range(2, isqrt(p) + 1))
x, y = 419, 798
assert x*x + x*y + 6*y*y == p**3
assert 818**2 + 23*399**2 == p**3 == 4330747
assert 2*818 == 1636
assert 1636 % p == 6
roots = [r for r in range(p) if (r*r + 23) % p == 0]
assert roots == [38, 125]
assert (818 + 399*125) % p == 0
assert (818 + 399*38) % p == 6
assert all((2*r) % p != 0 for r in roots)

norm_tests = [4*p - 23*j*j for j in range(6)]
assert norm_tests == [652, 629, 560, 445, 284, 77]
assert all(isqrt(n)**2 != n for n in norm_tests)
assert 4*p - 23*6**2 < 0

assert pow(35, 3, p) == 6
assert (3*35**2) % p != 0
assert pow(6, 27, p) == 1
assert pow(6, 9, p) == 58 != 1
assert (27*pow(6, 26, p)) % p != 0
# Since all proper divisors of 27 divide 9, these two power tests prove
# that the reduction has exact order 27, not merely order dividing 27.

print('PASS: p prime; quadratic norm and trace; both split roots and residues;')
print('      exhaustive norm-p nonsquare list; simple cube root; exact order27;')
print('      nonzero Hensel derivatives. Infinite-lift exclusion remains the written proof.')
