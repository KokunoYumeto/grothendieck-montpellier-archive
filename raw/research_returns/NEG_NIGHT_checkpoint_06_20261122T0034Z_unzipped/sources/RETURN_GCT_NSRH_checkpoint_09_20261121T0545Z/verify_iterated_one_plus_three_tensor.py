"""Exact F67 one-plus-three certificate; left actions on column vectors."""
import sympy as s

m, a, n, b, v = s.symbols("m a n b v")
I = s.eye(2)
N = [s.Matrix([[m, a], [0, 0]]), s.Matrix([[0, 0], [a, m]])]
L = [s.Matrix([[n, b], [0, 0]]), s.Matrix([[0, 0], [b, n]])]
R = [s.kronecker_product(N[i], L[i])
     + s.kronecker_product(m*I-N[i], n*I-L[i]) for i in range(2)]
expected = [
    s.Matrix([[m*n, m*b, a*n, 2*a*b], [0, 0, 0, -a*n],
              [0, 0, 0, -m*b], [0, 0, 0, m*n]]),
    s.Matrix([[m*n, 0, 0, 0], [-m*b, 0, 0, 0],
              [-a*n, 0, 0, 0], [2*a*b, a*n, m*b, m*n]])]
assert R == expected
for r in R:
    assert (r*r-m*n*r).applyfunc(s.expand) == s.zeros(4)
product = R[0]*R[1]
diagonal = [s.expand(product[i, i]) for i in range(4)]
assert diagonal == [m*m*n*n-a*a*n*n-m*m*b*b+4*a*a*b*b,
                    -a*a*n*n, -m*m*b*b, m*m*n*n]
trace = s.expand(s.trace(product))
assert trace == 2*m*m*n*n-2*a*a*n*n-2*m*m*b*b+4*a*a*b*b
delta = v+v**-1
D = delta**2
A4 = D**2-8*D+8
sub = {m: delta, a: 1, n: delta**3, b: 3*D-4}
actual = s.expand(trace.subs(sub))
expected_trace = (2*(v**8+v**-8)-4*(v**6+v**-6)
                  +20*(v**4+v**-4)+20*(v**2+v**-2)+52)
assert s.expand(actual-expected_trace) == 0
assert s.expand(actual-(D**2*(D-2)**2+A4**2)) == 0
assert s.expand(actual-(2*D**4-20*D**3+84*D**2-128*D+64)) == 0
coeff = {int(t.as_powers_dict().get(v, 0)):
         t/v**int(t.as_powers_dict().get(v, 0))
         for t in s.Add.make_args(actual)}
assert {e:c for e,c in coeff.items() if c<0} == {-6: -4, 6: -4}
assert sum(c for c in coeff.values() if c>0) == 136
assert -sum(c for c in coeff.values() if c<0) == 8
assert actual.subs(v, 1) == 128
for f in sub.values():
    assert all(t/v**int(t.as_powers_dict().get(v, 0)) > 0
               for t in s.Add.make_args(s.expand(f)))
print("PASS: actual Delta^(1,3) matrices, quadratics and four product diagonals")
print("diagonal =", diagonal)
print("whole trace =", actual)
print("PASS: D^2(D-2)^2+A4^2; negative -4 at v^±6")
print("PASS: individually effective inputs; mixed Tate totals136/8; value128 at1")
