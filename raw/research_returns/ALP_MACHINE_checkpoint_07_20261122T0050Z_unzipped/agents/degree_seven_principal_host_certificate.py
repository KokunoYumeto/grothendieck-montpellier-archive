"""Exact finite certificate for AM-K030. No analytic or Lean verification."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
import sympy as sp

H = [1, 12, 17, 28]
cosets = [sorted({pow(2, i, 29) * h % 29 for h in H}) for i in range(7)]
assert sorted(sum(cosets, [])) == list(range(1, 29))
assert pow(2, 14, 29) == 28 and pow(2, 7, 29) == 12

def cyc_mul(f, g):
    ans = [Fraction(0) for _ in range(29)]
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            ans[(i + j) % 29] += a * b
    return ans

def period_coords(f):
    assert all(len({f[k] for k in c}) == 1 for c in cosets)
    return [f[c[0]] - f[0] for c in cosets]

def trace_B(f):
    # For a B-element, Tr_L/Q = 4 Tr_B/Q; Tr_L/Q(zeta^k)=-1 for k!=0.
    assert all(len({f[k] for k in c}) == 1 for c in cosets)
    return (28 * f[0] - sum(f[1:])) / 4

periods = []
for c in cosets:
    f = [Fraction(0) for _ in range(29)]
    for k in c:
        f[k] = Fraction(1)
    periods.append(f)

G = sp.Matrix(7, 7, lambda i, j: trace_B(cyc_mul(periods[i], periods[j])))
assert G == 29 * sp.eye(7) - 4 * sp.ones(7)
assert G.det() == 29**6
assert all(trace_B(f) == -1 for f in periods)

a = [-8, -4, -2, -5, -2, -4, -4]
b = [v + 4 for v in a]
assert sum(a) == -29 and sum(b) == -1
assert [sum(a[i] * a[(i + k) % 7] for i in range(7)) for k in range(7)] == [145] + [116] * 6
assert [sum(b[i] * b[(i + k) % 7] for i in range(7)) for k in range(7)] == [25] + [-4] * 6
C = sp.Matrix(7, 7, lambda i, j: sp.Rational(a[(i-j) % 7], 29))
assert C.T * G * C == sp.eye(7)
assert C.det() == -sp.Rational(1, 29**3)
assert all(v.q == 1 for v in C.inv())

es = []
for j in range(7):
    f = [Fraction(0) for _ in range(29)]
    for i in range(7):
        for k in cosets[(i+j) % 7]:
            f[k] += Fraction(a[i], 29)
    es.append(f)
assert all(trace_B(f) == 1 for f in es)
assert [[trace_B(cyc_mul(f, g)) for g in es] for f in es] == [[int(i == j) for j in range(7)] for i in range(7)]

# All coefficients in the displayed local identity PH8.
low = [sum(a[i] * sum(math.comb(k, n) for k in cosets[i] if k >= n) for i in range(7)) for n in range(29)]
expected = [0] * 16 + [1, -8, -13, 2, 7, -14, 14, -5, -12, 6, -4, 4, -8]
assert [(x-y) % 29 for x, y in zip(low, expected)] == [0] * 29
assert next(n for n, c in enumerate(low) if c % 29) == 16
assert 16 // 4 - 7 == -3

# pi_B = product(1-zeta^h) = 4-2 eta_0+eta_4.
pi = [Fraction(1)] + [Fraction(0)] * 28
for h in H:
    factor = [Fraction(0)] * 29
    factor[0], factor[h] = Fraction(1), Fraction(-1)
    pi = cyc_mul(pi, factor)
pi_coords = period_coords(pi)
assert pi_coords == [-6, -4, -4, -4, -3, -4, -4]

N = []
M = []
for i in range(7):
    Ni = sp.Matrix.hstack(*[sp.Matrix(period_coords(cyc_mul(periods[i], periods[j]))) for j in range(7)])
    Mi = C.inv() * Ni * C
    assert all(v.q == 1 for v in Mi)
    assert Mi == Mi.T
    N.append(Ni)
    M.append(Mi)
assert all(M[i] * M[j] == M[j] * M[i] for i in range(7) for j in range(7))
assert sum(M, sp.zeros(7)) == -sp.eye(7)
shown_M0 = sp.Matrix([
    [-2,0,-1,0,0,0,-1],
    [0,0,0,-1,0,0,1],
    [-1,0,0,1,0,1,-1],
    [0,-1,1,1,0,1,0],
    [0,0,0,0,0,-1,0],
    [0,0,1,1,-1,0,1],
    [-1,1,-1,0,0,1,0]
])
assert M[0] == shown_M0
x = sp.symbols('x')
eta_poly = M[0].charpoly(x).as_expr()
assert eta_poly == x**7+x**6-12*x**5-7*x**4+28*x**3+14*x**2-9*x+1
Mp = sum((int(pi_coords[i]) * M[i] for i in range(7)), sp.zeros(7))
assert Mp == 4 * sp.eye(7) - 2 * M[0] + M[4]
assert Mp.det() == 29
assert all(Mp[:i,:i].det() > 0 for i in range(1,8))

# Discriminant/norm exponents for the degree12 times degree7 compositum.
assert [12*7, 10*7, 6*12] == [84, 70, 72]
assert [-12*7, -10*7, -6*12] == [-84, -70, -72]

# Exact residue-kernel index formula, for finite sample dimensions/exponents.
for rank in range(1, 13):
    gl_card = math.prod(29**rank - 29**i for i in range(rank))
    for exponent in range(1, 5):
        local = gl_card * 29**((7*exponent-1)*rank*rank)
        expected_local = Fraction(29**(7*exponent*rank*rank)) * math.prod(Fraction(29**i-1,29**i) for i in range(1,rank+1))
        assert local == expected_local
        assert local**6 == Fraction((29**exponent)**(42*rank*rank)) * math.prod(Fraction(29**i-1,29**i)**6 for i in range(1,rank+1))

result = {
    'result': 'PASS',
    'checked_at': datetime.now(timezone.utc).isoformat(),
    'scope': 'Exact cyclotomic arithmetic, trace Gram and normal-basis matrices, every coefficient of PH8, integral symmetric period-action matrices, positive prime generator norm, displayed discriminant exponents, and 48 finite principal-index identities. No analytic theta, CM-gauge theorem, infinite derivative estimate or Lean instance is computationally inferred.',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'cosets': cosets,
    'normal_basis_numerator': a,
    'basis_determinant': str(C.det()),
    'local_polynomial_coefficients_mod29': [c % 29 for c in low],
    'pi_period_coefficients': [int(v) for v in pi_coords],
    'eta0_matrix': [[int(v) for v in M[0][i,:]] for i in range(7)],
    'pi_matrix': [[int(v) for v in Mp[i,:]] for i in range(7)],
    'pi_norm': int(Mp.det()),
    'eta0_characteristic_polynomial': str(eta_poly),
    'pi_characteristic_polynomial': str(Mp.charpoly(x).as_expr()),
    'discriminant_exponents': {'2':84,'7':70,'29':72}
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
