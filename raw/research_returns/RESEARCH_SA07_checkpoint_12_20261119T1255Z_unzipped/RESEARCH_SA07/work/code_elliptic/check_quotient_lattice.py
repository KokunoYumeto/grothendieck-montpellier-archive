"""Exact finite identities supporting A.4.34.

These polynomial checks do not establish arithmetic algebraicity assertions.
The period-theorem and CM arguments are proved in the accompanying text.
"""

import sympy as s

p, q, c, x1, y1, x2, y2 = s.symbols(
    "p q c x1 y1 x2 y2", real=True
)
b = p + s.I * q
w1, w2 = x1 + s.I * y1, x2 + s.I * y2
mu1 = b * w1 + c * s.conjugate(w1)
mu2 = b * w2 + c * s.conjugate(w2)
matrix = s.Matrix([[p + c, -q], [q, p - c]])
determinant = p**2 + q**2 - c**2
assert s.expand(matrix.det() - determinant) == 0
print("real determinant =", determinant)

oriented_area = x1 * y2 - y1 * x2
numerator = s.expand(s.im(s.conjugate(mu1) * mu2))
assert s.expand(numerator - determinant * oriented_area) == 0
print("Im(conjugate(mu1)*mu2) = determinant * Im(conjugate(w1)*w2): PASS")

denominator = s.expand(mu1 * s.conjugate(mu1))
assert s.expand(
    denominator - ((p + c) * x1 - q * y1)**2
    - (q * x1 + (p - c) * y1)**2
) == 0
print("|mu1|^2 is the sum of squares of the two real coordinates: PASS")
print("Im(mu2/mu1) numerator and denominator: PASS")

# Algebraic coLie chart t=zeta(u)-s, du=omega, ds=-dt-x*du.
a, x, du, dt, ds = s.symbols("a x du dt ds")
pullback = (ds - a * du + dt).subs(ds, -dt - x * du)
assert s.expand(pullback + (x + a) * du) == 0
print("d(zeta(u)-a*u) = -(x+a)*du in the algebraic chart: PASS")

# The second-kind convention is integral(x*du)=-eta.
omega, eta = s.symbols("omega eta")
period = -(-eta + a * omega)
assert s.expand(period - (eta - a * omega)) == 0
print("period of -(xi+a*omega) is eta-a*omega: PASS")

print("All exact symbolic identities passed.")
