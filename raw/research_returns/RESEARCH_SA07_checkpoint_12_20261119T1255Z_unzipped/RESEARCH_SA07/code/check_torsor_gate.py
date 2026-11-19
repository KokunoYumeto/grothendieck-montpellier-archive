"""Exact symbolic checks for the h=a tensor and generated-torsor audit.

These are algebraic matrix identities, not a construction of a non-CM
elliptic curve with algebraic Hodge splitting.
"""
import sympy as s

x, y, p, q, a, tau, taub, delta = s.symbols(
    'x y p q a tau taub delta', nonzero=True
)
P = s.Matrix([[x, p], [y, q]])
F = s.diag(1, -1)
S = s.simplify(P.inv() * F * P)
R = x*q + y*p + 2*a*x*y
assert s.simplify(S[0, 0] - a*S[1, 0] - R/P.det()) == 0
assert s.simplify(S*S - s.eye(2)) == s.zeros(2)
assert s.simplify(s.trace(S)) == 0
print('single-valued equation: s11-a*s21 = (x*q+y*p+2*a*x*y)/det(P)')

B = s.Matrix([[1, a], [0, 1]])
Pshift = P*B
assert s.expand(Pshift[0, 0]*Pshift[1, 1] +
                Pshift[1, 0]*Pshift[0, 1]) == R
print('algebraic basis shift: R_0(P*B_a)=R_a(P)')

H = s.Matrix([[1, 1], [1, -1]])
V = s.Matrix([[x, p], [y, -y*p/x]])
assert s.diag(x, y)*H*s.diag(1, p/x) == V
assert s.simplify(V.det() + 2*y*p) == 0
print('h=0 hypersurface: P=diag(x,y)*H*diag(1,p/x), det(P)=-2*y*p')

I = s.eye(2)
Z = s.diag(1, -1)
X = H.inv()*Z*H
Y = Z*X-X*Z
rank = s.Matrix.hstack(*(s.Matrix(list(A)) for A in [I, Z, X, Y])).rank()
assert rank == 4
print('Lie span rank for two contained diagonal tori:', rank)
print('H^-1*Z*H =', X)
print('[Z,H^-1*Z*H] =', Y)

M = s.Matrix([[1, 1], [tau, taub]])
Q = s.simplify(M*s.diag(0, 1)*M.inv())
Qexpected = s.Matrix([[-tau, 1], [-tau*taub, taub]])/(taub-tau)
assert s.simplify(Q-Qexpected) == s.zeros(2)
assert s.simplify(-Q[0, 0]/Q[0, 1]-tau) == 0
assert s.simplify(Q[1, 1]/Q[0, 1]-taub) == 0
assert s.simplify(Q*Q-Q) == s.zeros(2)
print('Betti Hodge projector:', Qexpected)
print('recovery: tau=-Q11/Q12; taub=Q22/Q12')

Pdelta = s.Matrix([[x, -delta/(2*y)-a*x],
                   [y, delta/(2*x)-a*y]])
assert s.simplify(Pdelta.det()-delta) == 0
assert s.simplify(Pdelta[0, 0]*Pdelta[1, 1] +
                  Pdelta[1, 0]*Pdelta[0, 1] +
                  2*a*Pdelta[0, 0]*Pdelta[1, 0]) == 0
print('fixed-determinant h=a locus has free coordinates x,y in Gm^2')
print('All exact identities passed.')
