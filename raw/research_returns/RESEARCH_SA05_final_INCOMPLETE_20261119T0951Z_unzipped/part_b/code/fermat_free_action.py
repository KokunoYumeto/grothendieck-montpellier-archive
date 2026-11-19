"""Exact finite certificates for the cyclic Fermat-surface strictness witnesses."""
from math import gcd

for r in (5, 7):
    print('prime_degree', r)
    for a in range(1, r):
        exponents = [(a*j) % r for j in range(4)]
        assert len(set(exponents)) == 4
        print('nonidentity_exponent', a, 'eigenvalue_exponents', exponents,
              'pairwise_distinct', True)
    for i in range(4):
        point = [int(j == i) for j in range(4)]
        fermat_value = sum(x**r for x in point)
        assert fermat_value == 1
        print('coordinate_point', point, 'integer_Fermat_value', fermat_value)
    print('derivatives:', [f'{r}*x{i}^{r-1}' for i in range(4)])
    print('If p does not divide r, all four derivatives vanish only at the affine origin;'
          ' hence the projective hypersurface is smooth.')
print('choice: r=5 for every characteristic p!=5; r=7 when p=5')
print('base field: F_(p^ord_r(p)); all rth roots of unity are present')
print('FERMAT_FREE_ACTION_CERTIFICATE_COMPLETE')
