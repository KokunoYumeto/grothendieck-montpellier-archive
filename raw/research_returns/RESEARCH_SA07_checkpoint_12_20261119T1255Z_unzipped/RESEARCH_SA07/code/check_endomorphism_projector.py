"""Exact checks for A.4.18--19 and A.4.21; no assertion about an unknown non-CM h."""
import sympy as s

a, d, h = s.symbols('a d h')
e = s.Matrix([[0, h], [0, 1]])
T = a*s.eye(2) + (d-a)*e
assert e*e == e
assert T*s.Matrix([1, 0]) == a*s.Matrix([1, 0])
assert s.simplify(T*s.Matrix([h, 1])-d*s.Matrix([h, 1])) == s.zeros(2, 1)
print('D_E matrices: [[a,(d-a)*h],[0,d]] preserve both Hodge lines.')

A, B, C, D, hs = s.symbols('A B C D hs')
F = s.Matrix([[A, B], [C, D]])
es = s.Matrix([[0, hs], [0, 1]])
defect = F*es-e*F
assert defect == s.Matrix([[-C*h, A*hs+B-D*h], [-C, C*hs]])
print('F*sigma(e)-e*F = [[-C*h,A*sigma(h)+B-D*h],[-C,C*sigma(h)]].')

u = s.sqrt(-2)
alpha = u*s.Matrix([[1, -1], [0, -1]])
assert s.simplify((alpha-u*s.eye(2))/(-2*u)-e.subs(h,s.Rational(1,2))) == s.zeros(2)
print('CM projector identity: e_(1/2)=(alpha-u*I)/(-2*u), u^2=-2.')

p = 5
counts = [sum((y*y-(4*x*x*x+2))%p == 0 for y in range(p)) for x in range(p)]
assert counts == [0, 2, 2, 1, 0]
N = 1+sum(counts)
assert N == 6
assert p+1-N == 0
assert (30**3-27*28**2)%5 != 0
print('CM reduction at5: y-counts=', counts, ', #E(F5)=',N,', a5=0; characteristic polynomial T^2+5.')
print('Irreducibility over Q5 follows from v5(-5)=1, whereas v5(z^2) is even.')

counts_star = [sum((y*y-(4*x*x*x-4*x-1))%p == 0 for y in range(p)) for x in range(p)]
assert counts_star == [2, 2, 0, 1, 2]
N_star = 1+sum(counts_star)
assert N_star == 8 and p+1-N_star == -2
assert 37%p != 0 and (-2)%p != 0
print('Non-CM E_* at5: y-counts=', counts_star, ', #E_*(F5)=',N_star,', a5=-2; good ordinary reduction.')
