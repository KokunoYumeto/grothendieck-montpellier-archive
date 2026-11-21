"""Exact full S_33(Gamma_1(7)) Hecke test at the remaining K32 prime.

The complete integral conic-ring and cusp-divisor proofs are separate.
Every series, identifying minor, Hecke correction and determinant is
reconstructed over the explicitly certified prime field. No Hecke matrix
or desired output residue is input. Python integers have arbitrary size.
"""
from pathlib import Path
from math import comb
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent
MODULUS = 25078104767246023
PRECISION = 160
E = 16
WEIGHT = 2*E+1
ZETA = pow(3, (MODULUS-1)//6, MODULUS)
assert pow(ZETA, 6, MODULUS) == 1
assert pow(ZETA, 3, MODULUS) == MODULUS-1
assert (ZETA*ZETA-ZETA+1) % MODULUS == 0
assert ZETA not in (1, MODULUS-1)


def multiply(a, b):
    out = [0]*(PRECISION+1)
    for i, x in enumerate(a):
        if x:
            for j in range(min(len(b), PRECISION+1-i)):
                out[i+j] += x*b[j]
    return [x % MODULUS for x in out]


def powers(a, count):
    result = [[1]+[0]*PRECISION]
    for _ in range(count):
        result.append(multiply(result[-1], a))
    return result


def eta_product():
    out = [0, 1]+[0]*(PRECISION-1)
    for scale in (1, 7):
        for n in range(scale, PRECISION+1, scale):
            factor = [0]*(PRECISION+1)
            for j in range(min(3, PRECISION//n)+1):
                factor[n*j] = (-1)**j*comb(3, j)
            out = multiply(out, factor)
    return out


residue_logs = {pow(3, j, 7): j for j in range(6)}


def chi(n, exponent):
    return (0 if n % 7 == 0 else
            pow(ZETA, exponent*residue_logs[n % 7], MODULUS))


def eisenstein(exponent):
    out = [0]*(PRECISION+1)
    out[0] = (-sum(n*chi(n, exponent) for n in range(1, 7))
              * pow(14, -1, MODULUS)) % MODULUS
    for d in range(1, PRECISION+1):
        cd = chi(d, exponent)
        for n in range(d, PRECISION+1, d):
            out[n] = (out[n]+cd) % MODULUS
    return out


def determinant(a):
    a = [row[:] for row in a]
    n = len(a)
    value = 1
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            value = -value
        leading = a[j][j]
        value = value*leading % MODULUS
        inv = pow(leading, -1, MODULUS)
        for i in range(j+1, n):
            multiplier = a[i][j]*inv % MODULUS
            for k in range(j, n):
                a[i][k] = (a[i][k]-multiplier*a[j][k]) % MODULUS
    return value % MODULUS


def matmul(a, b):
    columns = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) % MODULUS
             for col in columns] for row in a]


def identifying_rows(rows):
    echelon = []
    pivots = []
    selected = []
    for index, original in enumerate(rows):
        row = original[:]
        for leading, prior in zip(pivots, echelon):
            multiplier = row[leading]
            row = [(x-multiplier*y) % MODULUS
                   for x, y in zip(row, prior)]
        leading = next((j for j, x in enumerate(row) if x), None)
        if leading is None:
            continue
        inv = pow(row[leading], -1, MODULUS)
        row = [x*inv % MODULUS for x in row]
        pivots.append(leading)
        echelon.append(row)
        selected.append(index)
        if len(selected) == len(original):
            break
    return selected


def solve_many(a, b):
    n = len(a)
    augmented = [a[i][:]+b[i][:] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if augmented[i][j])
        augmented[j], augmented[pivot] = augmented[pivot], augmented[j]
        inv = pow(augmented[j][j], -1, MODULUS)
        augmented[j] = [x*inv % MODULUS for x in augmented[j]]
        for i in range(n):
            if i != j:
                multiplier = augmented[i][j]
                augmented[i] = [(x-multiplier*y) % MODULUS
                                for x, y in zip(augmented[i], augmented[j])]
    assert all(augmented[i][j] == int(i == j)
               for i in range(n) for j in range(n))
    return [row[n:] for row in augmented]


A, B, C = [eisenstein(j) for j in (1, 3, 5)]
assert A[0] == (2*ZETA+1)*pow(7, -1, MODULUS) % MODULUS
assert B[0] == pow(2, -1, MODULUS)
assert C[0] == (3-2*ZETA)*pow(7, -1, MODULUS) % MODULUS
assert multiply(A, C) == [4*pow(7, -1, MODULUS)*x % MODULUS
                          for x in multiply(B, B)]
D = eta_product()
assert D[0] == 0 and D[1] == 1
power_a, power_b, power_c = [powers(f, 30) for f in (A, B, C)]
basis = []
for j in range(31):
    basis.append({'exponents': [30-j, j, 0],
                  'character': (3+2*j) % 6,
                  'coefficients': multiply(D, multiply(power_a[30-j], power_b[j]))})
for j in range(1, 31):
    basis.append({'exponents': [0, 30-j, j],
                  'character': (3+2*j) % 6,
                  'coefficients': multiply(D, multiply(power_b[30-j], power_c[j]))})
assert len(basis) == 61
point = 1+2**(2*E)
twists = [pow(ZETA, 2*j, MODULUS) for j in range(3)]
assert len(set(twists)) == 3 and all(pow(t, 3, MODULUS) == 1 for t in twists)
reports = []
global_twisted_det = 1
for character in (1, 3, 5):
    block = [f for f in basis if f['character'] == character]
    dimension = len(block)
    assert dimension == (21 if character == 3 else 20)
    coeffs = [f['coefficients'] for f in block]
    all_rows = [[f[n] for f in coeffs] for n in range(1, 68)]
    indices = identifying_rows(all_rows)
    assert len(indices) == dimension
    matrix_a = [all_rows[i] for i in indices]
    identifying_determinant = determinant(matrix_a)
    assert identifying_determinant != 0
    diamond = chi(2, character)

    def hecke_coefficient(f, n):
        return (f[2*n]+(diamond*2**(WEIGHT-1)*f[n//2]
                        if n % 2 == 0 else 0)) % MODULUS

    matrix_b = [[hecke_coefficient(f, i+1) for f in coeffs]
                for i in indices]
    hecke = solve_many(matrix_a, matrix_b)
    assert matmul(matrix_a, hecke) == matrix_b
    for n in range(1, PRECISION//2+1):
        actual = [hecke_coefficient(f, n) for f in coeffs]
        assert matmul([[f[n] for f in coeffs]], hecke)[0] == actual
    h3 = matmul(matmul(hecke, hecke), hecke)
    cubic_matrix = [[(pow(point, 3, MODULUS)*int(i == j)-h3[i][j]) % MODULUS
                     for j in range(dimension)] for i in range(dimension)]
    cubic_determinant = determinant(cubic_matrix)
    direct_determinants = []
    direct_product = 1
    for twist in twists:
        d = determinant([[(point*int(i == j)-twist*hecke[i][j]) % MODULUS
                          for j in range(dimension)] for i in range(dimension)])
        direct_determinants.append(d)
        direct_product = direct_product*d % MODULUS
    assert direct_product == cubic_determinant
    global_twisted_det = global_twisted_det*cubic_determinant % MODULUS
    reports.append({'character_exponent': character, 'dimension': dimension,
                    'basis_exponents': [f['exponents'] for f in block],
                    'identifying_q_indices': [i+1 for i in indices],
                    'identifying_matrix': matrix_a,
                    'identifying_determinant': identifying_determinant,
                    'raw_hecke_coefficients': matrix_b,
                    'hecke_matrix': hecke, 'diamond_at_2': diamond,
                    'twist_determinants': direct_determinants,
                    'cubic_determinant': cubic_determinant,
                    'all_q_coefficients_checked_through': PRECISION//2})
report = {'status': 'COMPLETE exact full modular-form residue calculation',
          'prime': MODULUS, 'prime_certificate': '../../hecke_general/higher2/prime_certificates.json',
          'zeta6': ZETA, 'weight': WEIGHT, 'dimension': len(basis),
          'auxiliary_prime': 2, 'precision': PRECISION,
          'comparison_point': point, 'twist_values': twists,
          'all_twists_comparison_determinant': global_twisted_det,
          'nonzero': global_twisted_det != 0,
          'blocks': reports,
          'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope': 'Finite full GL2 model; global source/conductor and U3 branch are separate.'}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({k: report[k] for k in
                  ('status', 'prime', 'zeta6', 'dimension', 'all_twists_comparison_determinant', 'nonzero')}))
print(json.dumps([{'character': r['character_exponent'], 'dimension': r['dimension'],
                   'twist_determinants': r['twist_determinants'],
                   'cubic_determinant': r['cubic_determinant']} for r in reports]))
