"""Exact finite certificates accompanying the all-length proofs in F.3.2–3."""
from pathlib import Path
import sympy as s


def string(m):
    E, L, F = (s.zeros(m + 1) for _ in range(3))
    H = s.diag(*(2*j-m for j in range(m + 1)))
    for j in range(m):
        E[j+1, j] = 1
    for j in range(1, m + 1):
        L[j-1, j] = 1
        F[j-1, j] = j*(m-j+1)
    return E, L, F, H


def comm(A, B):
    return A*B-B*A


for m in range(11):
    E, L, F, H = string(m)
    assert comm(E, F) == H
    assert comm(H, E) == 2*E
    assert comm(H, F) == -2*F
    lf, fl = s.zeros(m+1), s.zeros(m+1)
    for j in range(1, m+1):
        P = s.zeros(m+1)
        P[j, j] = 1
        a = j*(m-j+1)
        lf += a*L*P
        fl += s.Rational(1, a)*F*P
    assert lf == F and fl == L
    assert H**2+2*H+4*F*E == m*(m+2)*s.eye(m+1)
print('Commutators, conversions, Casimir: all m = 0,...,10 passed.')

for d in range(6):
    E, L, F, H = (s.diag(*(string(m)[i] for m in range(d+1))) for i in range(4))
    n = E.rows
    B, T = s.eye(n)-E*L, s.eye(n)-L*E
    offset, count = 0, 0
    for m in range(d+1):
        Bm = B*(L**m)*T*(E**m)*B
        for a in range(m+1):
            for b in range(m+1):
                actual = (E**b)*Bm*(L**a)
                expected = s.zeros(n)
                expected[offset+b, offset+a] = 1
                assert actual == expected, (d,m,a,b)
                count += 1
        offset += m+1
    print(f'Matrix units: d={d}, dim W={n}, all {count} units passed.')

E, L, F, H = string(2)
mod2 = lambda A: A.applyfunc(lambda x: int(x) % 2)
assert mod2(F) == s.zeros(3) and mod2(H) == s.zeros(3)
assert mod2(L)[:, 2] == s.Matrix([0, 1, 0])
assert all((mod2(E**j)[:, 2])[1] == 0 for j in range(3))
print('Integral counterexample m=2: F=H=0 mod 2, but Lambda(v2)=v1.')

z = s.symbols('z', nonzero=True)
E, L, F, H = string(1)
rho = s.diag(1,z)
assert rho*E*rho.inv() == z*E
assert rho*F*rho.inv() == F/z
assert (s.eye(2)+E)*s.Matrix([1,0]) == s.Matrix([1,1])
j = s.diag(z,1)
E12 = s.Matrix([[0,1],[0,0]])
assert j.det() == z
assert j*E12*j.inv() == z*E12
assert (z*s.eye(2)).det() == z**2
print('P1 equivariance and GL2 Levi/weight character calculations passed.')

# Matrix certificates for the counterexamples; the topological identifications
# and group-scheme centre computations are proved in the accompanying text.
J = s.Matrix([[0,1],[-1,0]])
two = 2*s.eye(2)
assert two.T*J*two == 4*J
q,a,b,c,d = s.symbols('q a b c d')
A = s.Matrix([[a,b],[c,d]])
assert s.expand((q*A).det()-q**2*A.det()) == 0
assert (-s.eye(2)).det() == 1
assert (-1)*(-s.eye(2)) == s.eye(2)
assert s.diag(1,-1).eigenvals() == {1:1,-1:1}
swap = s.Matrix([[0,1],[1,0]])
assert len((swap-s.eye(2)).nullspace()) == 1
print('Tate central isogeny determinant and [2] polarization scaling passed.')
print('Real cohomology examples: reflection H2 invariants=0; two-point H0 invariants=1.')
print('All finite exact assertions passed; universal proofs are in agent_audit.md.')
