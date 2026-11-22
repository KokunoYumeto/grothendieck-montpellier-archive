"""Exact certificate for F63 (not a formal proof assistant).

Source: Blasiak, arXiv:1010.0421v2, equations (9), (13), (23)--(24),
Theorems 3.4/3.7.  All matrices here act on LEFT COLUMN vectors.
Transposing gives the prior F56 right-row convention.
"""

import sympy as s

v, D = s.symbols("v D", nonzero=True)
z = s.symbols("z")
delta = v + v**-1
a = D - 2
d = D**2
A = D**2 - 8 * D + 8

def zero_matrix(M):
    return all(s.cancel(x) == 0 for x in M)

def laurent_coefficients(f):
    result = {}
    for term in s.Add.make_args(s.expand(f)):
        power = int(term.as_powers_dict().get(v, 0))
        coefficient = s.simplify(term / v**power)
        assert not coefficient.has(v)
        result[power] = result.get(power, 0) + coefficient
    return dict(sorted((p, s.simplify(c)) for p, c in result.items() if c))

# The scaled Chebyshev recurrence A_j = delta^j T_j(1/delta).
scaled = [s.Integer(1), s.Integer(1)]
for j in range(1, 4):
    scaled.append(s.expand(2 * scaled[-1] - D * scaled[-2]))
assert scaled == [1, 1, 2 - D, 4 - 3*D, A]

Al = s.expand(A.subs(D, delta**2))
c4 = s.expand(Al**2)
expected = {-8: 1, -6: -8, -4: 12, -2: 8, 0: 38,
            2: 8, 4: 12, 6: -8, 8: 1}
assert laurent_coefficients(c4) == expected

# Source equation (13) gives trace(P1 P2) = c.
P1cyclic = s.Matrix([[d, A**2], [0, 0]])
P2cyclic = s.Matrix([[0, 0], [1, d]])
assert s.trace(P1cyclic * P2cyclic) == A**2

# Positive balanced matrices on the actual binary k=2 N(D-2) block.
P1 = s.Matrix([[D, a], [0, 0]])
P2 = s.Matrix([[0, 0], [a, D]])
I2 = s.eye(2)
Q1, Q2 = D*I2 - P1, D*I2 - P2
R1 = s.kronecker_product(P1, P1) + s.kronecker_product(Q1, Q1)
R2 = s.kronecker_product(P2, P2) + s.kronecker_product(Q2, Q2)
assert zero_matrix(R1**2 - d*R1)
assert zero_matrix(R2**2 - d*R2)

up = s.Matrix([d, -D*a, -D*a, d])
um = s.Matrix([0, 1, -1, 0])
b1 = s.Matrix([A, -D*a, -D*a, d])
b2 = s.Matrix([d, -D*a, -D*a, A])
B = s.Matrix.hstack(up, um, b1, b2)
target1 = s.diag(d, 0, s.Matrix([[d, A], [0, 0]]))
target2 = s.diag(d, 0, s.Matrix([[0, 0], [A, d]]))
assert zero_matrix(R1*B - B*target1)
assert zero_matrix(R2*B - B*target2)
assert s.factor(B.det()) == 128*D*(D-2)*(D-1)**2

denominator = s.factor(d**2 - A**2)
assert s.expand(denominator - 16*(D-1)*(D-2)**2) == 0
E = (d*(R1+R2) - R1*R2 - R2*R1) / denominator
E = E.applyfunc(s.cancel)
assert zero_matrix(E**2 - E)
assert zero_matrix(E*R1 - R1*E)
assert zero_matrix(E*R2 - R2*E)
assert zero_matrix(E*B - B*s.diag(0, 0, 1, 1))
assert s.cancel(s.trace(E)) == 2
assert s.factor(s.trace(E*R1*R2)) == A**2
assert s.expand(s.trace(R1*R2) - (d**2 + A**2)) == 0
assert s.expand((R1*R2).charpoly(z).as_expr()
                - z**2*(z-d**2)*(z-A**2)) == 0

# Two positive identities underpin the all-word whole-tensor boundary.
assert s.expand(d+A - 2*(D-2)**2) == 0
assert s.expand(d-A - 8*(D-1)) == 0
whole_trace = s.expand((d**2+A**2).subs(D, delta**2))
assert all(c >= 0 for c in laurent_coefficients(whole_trace).values())

# Minimality of the individual-simple positivity property for k <= 3.
positive_scaled = {1: s.Integer(1), 2: D-2, 3: 3*D-4}
for k in range(1, 4):
    for j in range(1, k+1):
        b = delta**(k-j) * positive_scaled[j].subs(D, delta**2)
        assert all(c >= 0 for c in laurent_coefficients(b).values())
        assert s.cancel(b**2 - delta**(2*(k-j))
                        * scaled[j].subs(D, delta**2)**2) == 0

# The actual defining braid relation at k=4 on the 4-dimensional tensor.
roots = [D**(4-j)*scaled[j]**2 for j in range(1, 5)]
F21 = s.eye(4)
F12 = s.eye(4)
for root in roots:
    F21 = F21*(R2*R1-root*s.eye(4))
    F12 = F12*(R1*R2-root*s.eye(4))
assert zero_matrix(R1*F21 - R2*F12)

print("PASS: exact left-column source normalization and k=4 tensor restriction.")
print("scaled Chebyshev A0..A4:", scaled)
print("A4 Laurent:", Al)
print("Tr on M^(4) of P1 P2:", c4)
print("nonzero Laurent coefficients:", laurent_coefficients(c4))
print("R1 =", R1)
print("R2 =", R2)
print("B =", B)
print("det B =", s.factor(B.det()))
print("R1 B = B diag(d,0,N1(A4)); R2 B = B diag(d,0,N2(A4)): PASS")
print("central projector E =", E)
print("projector regular denominator before cancellation =", denominator)
print("Tr(E R1 R2) =", s.factor(s.trace(E*R1*R2)))
print("whole tensor Tr(R1 R2) =", whole_trace)
print("whole tensor product characteristic polynomial =", s.factor((R1*R2).charpoly(z).as_expr()))
print("d+A4 =", s.factor(d+A), "; d-A4 =", s.factor(d-A))
print("k<=3 individual-simple positive Laurent models: PASS")
print("actual k4 defining nonstandard braid relation: PASS")
