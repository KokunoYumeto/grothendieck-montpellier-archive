"""Exact polynomial and differential-order checks for the NG07 example."""
import sympy as s

x = s.symbols('x')
f = x**5 - x - 1
assert s.discriminant(f, x) == 2869
q2 = x**2 + x + 1
q3 = x**3 + x**2 + 1
assert s.Poly(f - q2*q3, x, modulus=2).is_zero
assert s.Poly(q2, x, modulus=2).is_irreducible
assert s.Poly(q3, x, modulus=2).is_irreducible
assert s.Poly(f, x, modulus=3).is_irreducible
assert all(int(f.subs(x, a)) % 3 for a in range(3))
quadratics = [x*x+1, x*x+x-1, x*x-x-1]
remainders = [s.rem(f, q, domain=s.GF(3)) for q in quadratics]
assert remainders == [-1, x-1, x-1]
forms = [(0,1), (0,2), (1,2), (2,2)]
orders = [-3*a-4+5*b for a,b in forms]
assert orders == [1,6,3,0]
eigen_exponents = [(-b) % 3 for _,b in forms]
assert eigen_exponents.count(1) == 3
assert eigen_exponents.count(2) == 1
print('PASS: discriminant 2869; mod2 factor degrees (2,3); mod3 irreducible.')
print('Direct mod3 quadratic remainders:', remainders)
print('Orders at infinity:', orders)
print('Eigenvalue exponents of zeta3:', eigen_exponents)
print('Signature (3,1); determinant types (3,1),(1,3).')
