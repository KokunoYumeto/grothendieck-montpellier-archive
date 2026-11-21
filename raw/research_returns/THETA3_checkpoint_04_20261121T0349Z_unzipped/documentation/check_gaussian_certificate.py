"""Interval check of Q2 constants in the stated six-dimensional Gaussian model.
This verifies a numerical instance of the estimate; it does not certify an
adelic normalization or a cycle construction.
"""
from mpmath import iv
iv.dps = 60
pi = iv.pi
c = 2*pi*iv.exp(-2*pi)
b = 9*pi
first = iv.mpf(5)**6 * iv.exp(-b)
ratio = (iv.mpf(7)/5)**6 * iv.exp(-3*b)
err = 2*iv.sqrt(pi/iv.e)*first/(1-ratio)
lower = c*c-2*c*err-err*err
print('dimension=6; minimum_squared=2; lambda=1; k=6')
print('leading_gradient_amplitude:', c)
print('successive_ratio_upper:', ratio)
print('gradient_error_upper:', err)
print('wedge_lower_bound:', lower)
assert float(lower.a) > 0.000137
print('Certified coarse wedge lower bound: 137/1000000')
