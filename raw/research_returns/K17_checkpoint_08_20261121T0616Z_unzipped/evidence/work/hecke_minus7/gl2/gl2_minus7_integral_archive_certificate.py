"""Independent exact T_2 calculation in the integral conic basis.

No imports from the Eisenstein/character-block calculation.  The coefficient
tables and diamond action are Meier--Ozornova, Section 2, Proposition 2.4 and
Lemma 2.5.  All arithmetic after these tables is over the certified prime field.
The whole 61-dimensional space is used, without choosing a sixth root of unity.
"""
from pathlib import Path
import hashlib
import json

P = 25078104767246023
N = 160
WEIGHT = 33
DEGREE = 30


def convolution(f, g):
    return [sum(f[j] * g[n-j] for j in range(n+1)) % P
            for n in range(N+1)]


def scalar_series(which):
    # Coefficient at q^n is the divisor sum of the indicated integral function.
    tables = ((0, 1, -1, -2, 2, 1, -1),
              (0, -1, 2, -1, 1, -2, 1),
              (0, 2, 1, 1, -1, -1, -2))
    return [int(which == 2)] + [
        sum(tables[which][d % 7] for d in range(1, n+1) if n % d == 0) % P
        for n in range(1, N+1)]


z = [scalar_series(i) for i in range(3)]
one = [1] + [0]*N
zp = [[one] for _ in range(3)]
for i in range(3):
    for _ in range(DEGREE):
        zp[i].append(convolution(zp[i][-1], z[i]))
relation = [sum(v) % P for v in zip(convolution(z[0], z[1]),
                                    convolution(z[1], z[2]),
                                    convolution(z[2], z[0]))]
assert relation == [0]*(N+1)

# q times the product (1-q^n)^3(1-q^(7n))^3.  Descending updates multiply
# by each linear factor separately; this is independent of binomial expansion.
cusp = [0, 1] + [0]*(N-1)
for dilation in (1, 7):
    for n in range(dilation, N+1, dilation):
        for repetition in range(3):
            for j in range(N, n-1, -1):
                cusp[j] = (cusp[j] - cusp[j-n]) % P

# Standard monomials for leading term z1*z2 of the conic relation.
exponents = [(a, 0, DEGREE-a) for a in range(DEGREE+1)]
exponents += [(0, b, DEGREE-b) for b in range(1, DEGREE+1)]
assert len(exponents) == 61


def modular_form(exps):
    answer = cusp[:]
    for i, e in enumerate(exps):
        if e:
            answer = convolution(answer, zp[i][e])
    return answer


forms = [modular_form(exps) for exps in exponents]
# <2>z1=z2, <2>z2=z3, <2>z3=z1, and <2>D=D.
diamonds = [modular_form((c, a, b)) for a, b, c in exponents]
rows = [[f[n] for f in forms] for n in range(1, 62)]
target = [[(f[2*n] + (2**32)*g[n//2]*(n % 2 == 0)) % P
           for f, g in zip(forms, diamonds)] for n in range(1, 62)]


def solve(left, right):
    d = len(left)
    a = [left[i][:] + right[i][:] for i in range(d)]
    det = 1
    for col in range(d):
        row = next(i for i in range(col, d) if a[i][col])
        if row != col:
            a[row], a[col] = a[col], a[row]
            det = -det
        pivot = a[col][col]
        det = det*pivot % P
        inv = pow(pivot, -1, P)
        a[col] = [x*inv % P for x in a[col]]
        for i in range(d):
            if i == col:
                continue
            c = a[i][col]
            a[i] = [(x-c*y) % P for x, y in zip(a[i], a[col])]
    assert [r[:d] for r in a] == [[int(i == j) for j in range(d)]
                                for i in range(d)]
    return [r[d:] for r in a], det % P


matrix, identifying_det = solve(rows, target)
assert identifying_det in (1, P-1)
for n in range(1, 81):
    actual = [(f[2*n] + (2**32)*g[n//2]*(n % 2 == 0)) % P
              for f, g in zip(forms, diamonds)]
    derived = [sum(forms[i][n]*matrix[i][j] for i in range(61)) % P
               for j in range(61)]
    assert actual == derived


def matrix_product(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) % P
             for j in range(len(b[0]))] for i in range(len(a))]


def det(a):
    # Fraction-free Bareiss elimination, performed in the prime field.
    a = [r[:] for r in a]
    sign = 1
    previous = 1
    for i in range(len(a)-1):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            sign = -sign
        leading = a[i][i]
        inverse_previous = pow(previous, -1, P)
        for j in range(i+1, len(a)):
            for k in range(i+1, len(a)):
                a[j][k] = (leading*a[j][k]-a[j][i]*a[i][k])*inverse_previous % P
            a[j][i] = 0
        previous = leading
    return sign*a[-1][-1] % P


t = 1 + 2**32
cube = matrix_product(matrix_product(matrix, matrix), matrix)
cubic = [[(pow(t, 3, P)*int(i == j)-cube[i][j]) % P
          for j in range(61)] for i in range(61)]
answer = det(cubic)
assert answer != 0
report = {
    'status': 'PASS independent integral-basis finite certificate',
    'prime': P, 'weight': WEIGHT, 'auxiliary_prime': 2,
    'dimension': 61, 'precision': N, 'coefficient_checks_through': 80,
    'basis_exponents': exponents, 'identifying_indices': list(range(1, 62)),
    'identifying_determinant': identifying_det,
    'comparison_point': t, 'cubic_determinant': answer,
    'hecke_matrix': matrix,
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope': 'Complete finite GL2 model; source/conductor and U3 gates are separate.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('status', 'dimension',
                'identifying_determinant', 'cubic_determinant')}))
