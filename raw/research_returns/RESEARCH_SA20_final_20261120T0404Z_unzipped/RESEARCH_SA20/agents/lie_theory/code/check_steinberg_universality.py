"""Exact A3 first-order deformation certificate for Steinberg366 p158(a).

The published standalone hypotheses allow C2=Sp4.  Its subregular slice
has type A3, whose Tjurina space has dimension three; the quotient base
has dimension two.  This checks the finite Jacobian-quotient calculation.
"""
from time import perf_counter
from sympy import Matrix, QQ, S, eye, groebner, symbols, zeros

started = perf_counter()
J = zeros(4)
J[:2, 2:] = eye(2)
J[2:, :2] = -eye(2)
N = zeros(4)
N[:2, 2:] = eye(2)
u = eye(4) + N
assert N.T * J + J * N == zeros(4)
assert N.T * J * N == zeros(4)
assert N * N == zeros(4)
assert u.T * J * u == J
v = symbols("a00 a01 a10 a11 b00 b01 b11 c00 c01 c11")
A = Matrix(2, 2, v[:4])
B = Matrix([[v[4], v[5]], [v[5], v[6]]])
C = Matrix([[v[7], v[8]], [v[8], v[9]]])
X = A.row_join(B).col_join(C.row_join(-A.T))
commutator = X * N - N * X
expected = (-C).row_join(A + A.T).col_join(zeros(2).row_join(C))
assert commutator == expected
centralizer_dimension = 10 - Matrix(list(commutator)).jacobian(v).rank()
assert centralizer_dimension == 4
x, y, z = symbols("x y z")
f = x**4 + y**2 + z**2
basis = groebner([f, f.diff(x), f.diff(y), f.diff(z)], x, y, z, domain=QQ)
assert [p.as_expr() for p in basis.polys] == [x**3, y, z]
normal = [basis.reduce(m)[1] for m in [S.One, x, x**2, x**3, y, z]]
assert normal == [1, x, x**2, 0, 0, 0]
# A monomial avoids divisibility by x^3,y,z exactly when it is 1,x,x^2.
standard = [(a, b, c) for a in range(4) for b in range(2) for c in range(2)
            if not (a >= 3 or b >= 1 or c >= 1)]
assert standard == [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
base_tangent_dimension = 2
assert len(standard) > base_tangent_dimension
print("SOURCE: Steinberg LNM366 (1974), Appendix p158(a)")
print("SLICE: C2=Sp4 subregular surface A3")
print("UNIPOTENT: I4+[[0,I2],[0,0]] preserves J")
print("CENTRALIZER DIMENSION:", centralizer_dimension)
print("POLYNOMIAL: x^4+y^2+z^2 over Q")
print("TJURINA GROEBNER BASIS:", [str(p.as_expr()) for p in basis.polys])
print("STANDARD MONOMIAL EXPONENTS:", standard)
print("TJURINA DIMENSION:", len(standard))
print("ADJOINT-QUOTIENT BASE TANGENT DIMENSION:", base_tangent_dimension)
print("PASS: the unrestricted C2 family cannot be versal or universal")
print(f"RUNTIME_SECONDS: {perf_counter() - started:.9f}")
