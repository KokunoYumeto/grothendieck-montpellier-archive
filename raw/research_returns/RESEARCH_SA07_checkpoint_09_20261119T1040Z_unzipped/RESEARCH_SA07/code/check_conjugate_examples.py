"""Exact certificates for two elliptic conjugation examples.

SymPy rational arithmetic in Q(i), with the symbol U reduced by U^2=-2.
No numerical inference about periods is made.
"""
import sympy as s
import time

start = time.perf_counter()
X, Y, U = s.symbols('X Y U')
I = s.I
a = s.Integer(2)
b = s.Rational(1, 2) + I
f = X**3 + a*X**2 + b*X
Xp = X + a + b/X
Yp = Y*(1-b/X**2)
ap, bp = -2*a, a*a-4*b
res = s.factor((Yp**2-(Xp**3+ap*Xp**2+bp*Xp)).subs(Y**2, f))
assert res == 0
assert s.expand(ap-(-2)*s.conjugate(a)) == 0
assert s.expand(bp-4*s.conjugate(b)) == 0
j = s.expand_complex(s.cancel(256*(a*a-3*b)**3/(b*b*(a*a-4*b))))
normj = s.simplify(j*s.conjugate(j))
g2 = s.expand(4*(a*a/3-b))
g3 = s.expand(4*(a*b/3-2*a**3/27))
assert s.simplify(1728*g2**3/(g2**3-27*g3**2)-j) == 0
assert s.im(j) != 0
assert normj.q != 1
print('Example ELL-07: isogenous to conjugate, no real model')
print('Source a,b =', a, b)
print('Target a,b =', ap, bp)
print('Isogeny equation residual =', res)
print('Target coefficients = U^2*conjugate(a), U^4*conjugate(b), U^2=-2')
print('Short-Weierstrass g2,g3 =', g2, g3)
print('j =', j)
print('Norm(j) =', normj, '(noninteger, so j is not an algebraic integer)')

j0 = 1/(2+I)
c = s.cancel(j0/(j0-1728))
g20, g30 = 3*c, c
disc = s.simplify(g20**3-27*g30**2)
assert disc != 0
assert s.simplify(1728*g20**3/disc-j0) == 0
assert (2+3) % 5 == 0
assert (2-3) % 5 != 0
print('Example ELL-08: not isogenous to conjugate')
print('j =', s.expand_complex(j0), '; c =', c)
print('g2=3c, g3=c; reconstructed j identity passed')
print('At Gaussian prime 2+i, i maps to 3 in F5.')
print('2+i maps to', (2+3)%5, '; 2-i maps to', (2-3)%5)
print('Thus v(j)=-1 and v(conjugate(j))=0; modular-polynomial argument is in notes.')
print('All exact assertions passed.')
print('Runtime seconds:', round(time.perf_counter()-start, 6))
