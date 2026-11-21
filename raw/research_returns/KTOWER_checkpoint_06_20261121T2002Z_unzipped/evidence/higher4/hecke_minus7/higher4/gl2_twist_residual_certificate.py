"""Full Gamma_1(7) all-twists tests over arbitrary residual integer rings.

No primality or irreducibility assumption is made about a modulus.
The complete integral cusp basis has a unit triangular Fourier matrix.
Determinant divisions are made only by explicitly verified units.
"""
from pathlib import Path
from math import gcd
from hashlib import sha256
import json
import time
import argparse
import sys
sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent



def calculate(e, modulus):
    start = time.monotonic()
    weight = 2*e+1
    degree = weight-3
    dimension = 2*degree+1
    precision = 2*(dimension+8)
    assert e >= 2 and e % 2 == 0 and modulus > 1
    assert gcd(modulus, 42) == 1

    def multiply(f, g):
        out = [0]*(precision+1)
        ff = [(i, x) for i, x in enumerate(f) if x]
        gg = [(i, x) for i, x in enumerate(g) if x]
        for i, x in ff:
            for j, y in gg:
                if i+j > precision:
                    break
                out[i+j] += x*y
        return [x % modulus for x in out]

    def add(f, g):
        return [(x+y) % modulus for x, y in zip(f, g)]

    def powers(f):
        values = [[1]+[0]*precision]
        for _ in range(degree):
            values.append(multiply(values[-1], f))
        return values

    tables = ((0, 1, -1, -2, 2, 1, -1),
              (0, -1, 2, -1, 1, -2, 1),
              (0, 2, 1, 1, -1, -1, -2))
    z = []
    for i, table in enumerate(tables):
        f = [int(i == 2)]+[0]*precision
        for d in range(1, precision+1):
            c = table[d % 7]
            for n in range(d, precision+1, d):
                f[n] += c
        z.append([x % modulus for x in f])
    a, b, c = add(z[2], z[0]), z[0], add(z[0], z[1])
    assert a[0] == 1 and b[:2] == [0, 1] and c[:3] == [0, 0, 1]
    assert multiply(a, c) == multiply(b, b)

    # D=Q product(1-Q^n)^3(1-Q^(7n))^3, computed integrally.
    cusp = [0, 1]+[0]*(precision-1)
    for dilation in (1, 7):
        for n in range(dilation, precision+1, dilation):
            for _ in range(3):
                for j in range(precision, n-1, -1):
                    cusp[j] = (cusp[j]-cusp[j-n]) % modulus

    # <2> cycles z1->z2->z3->z1, and fixes D.
    # Thus a->c, b->z2, c->z2+z3.
    ap, bp, cp, dbp, dcp = [
        powers(f) for f in (a, b, c, z[1], add(z[1], z[2]))]
    forms, diamonds, exponents = [], [], []
    for j in range(degree+1):
        forms.append(multiply(cusp, multiply(ap[degree-j], bp[j])))
        diamonds.append(multiply(cusp, multiply(cp[degree-j], dbp[j])))
        exponents.append([degree-j, j, 0])
    for j in range(1, degree+1):
        forms.append(multiply(cusp, multiply(bp[degree-j], cp[j])))
        diamonds.append(multiply(cusp, multiply(dbp[degree-j], dcp[j])))
        exponents.append([0, degree-j, j])
    assert len(forms) == dimension
    leading = [[f[n] for f in forms] for n in range(1, dimension+1)]
    assert all(leading[i][i] == 1 for i in range(dimension))
    assert all(leading[i][j] == 0 for i in range(dimension)
               for j in range(i+1, dimension))

    scalar = pow(2, weight-1, modulus)

    def hecke_coeff(f, diamond, n):
        return (f[2*n]+(scalar*diamond[n//2] if n % 2 == 0 else 0)) % modulus

    columns, raw_columns = [], []
    for f, diamond in zip(forms, diamonds):
        raw = [hecke_coeff(f, diamond, n) for n in range(1, dimension+1)]
        coords = []
        for i in range(dimension):
            coords.append((raw[i]-sum(leading[i][j]*coords[j]
                                      for j in range(i))) % modulus)
        for n in range(1, precision//2+1):
            assert sum(coords[j]*forms[j][n] for j in range(dimension)) % modulus == hecke_coeff(f, diamond, n)
        columns.append(coords)
        raw_columns.append(raw)
    matrix = [[columns[j][i] for j in range(dimension)]
              for i in range(dimension)]

    def matmul(x, y):
        transposed = list(zip(*y))
        return [[sum(a*b for a, b in zip(row, column)) % modulus
                 for column in transposed] for row in x]

    cube = matmul(matmul(matrix, matrix), matrix)
    point = 1+2**(2*e)
    cubic = [[(pow(point, 3, modulus)*int(i == j)-cube[i][j]) % modulus
              for j in range(dimension)] for i in range(dimension)]

    def unit_determinant(rows):
        rows = [row[:] for row in rows]
        value = 1
        pivots = []
        for col in range(len(rows)):
            pivot = next((r for r in range(col, len(rows))
                          if gcd(rows[r][col], modulus) == 1), None)
            if pivot is None:
                obstruction = gcd(modulus, *(rows[r][col] for r in range(col, len(rows))))
                return None, pivots, {'column': col, 'column_ideal_gcd': obstruction}
            if pivot != col:
                rows[col], rows[pivot] = rows[pivot], rows[col]
                value = -value
            leading_value = rows[col][col]
            assert gcd(leading_value, modulus) == 1
            inverse = pow(leading_value, -1, modulus)
            assert leading_value*inverse % modulus == 1
            pivots.append(leading_value)
            value = value*leading_value % modulus
            for r in range(col+1, len(rows)):
                multiplier = rows[r][col]*inverse % modulus
                for j in range(col+1, len(rows)):
                    rows[r][j] = (rows[r][j]-multiplier*rows[col][j]) % modulus
                rows[r][col] = 0
        return value % modulus, pivots, None

    determinant, pivots, obstruction = unit_determinant(cubic)
    is_unit = determinant is not None and gcd(determinant, modulus) == 1
    return {
        'e': e, 'weight': weight, 'modulus': modulus,
        'primality_assumed': False, 'dimension': dimension,
        'basis_degree': degree, 'basis_exponents': exponents,
        'precision': precision, 'coefficients_checked_through': precision//2,
        'leading_unit_triangular': True,
        'leading_coefficient_matrix': leading,
        'initial_hecke_coefficient_columns': raw_columns,
        'hecke_matrix': matrix, 'comparison_point': point,
        'cubic_determinant': determinant, 'all_determinant_pivots': pivots,
        'determinant_gcd': gcd(determinant, modulus) if determinant is not None else None,
        'unit': is_unit, 'unresolved_pivot_obstruction': obstruction,
        'elapsed_seconds': time.monotonic()-start,
    }



parser = argparse.ArgumentParser()
parser.add_argument('e', type=int, choices=(26,28,30))
args = parser.parse_args()
support_path = (HERE.parent.parent/'hecke_general/higher4'/
                f'residual_support_e{args.e}.json')
support = json.loads(support_path.read_text())
source_row = next(r for r in support['degrees'] if r['e'] == args.e)
rows = []
for modulus in source_row['residual_support_moduli']:
    row = calculate(args.e, modulus)
    rows.append(row)
    print(json.dumps({k:row[k] for k in ('e','modulus','dimension',
                      'cubic_determinant','determinant_gcd','unit',
                      'unresolved_pivot_obstruction','elapsed_seconds')}), flush=True)
report = {
    'status':'Exact full integral GL2 residual-ring calculations',
    'e':args.e, 'all_units':all(r['unit'] for r in rows), 'cases':rows,
    'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'support_data_sha256':sha256(support_path.read_bytes()).hexdigest(),
    'complete_support_moduli':source_row['residual_support_moduli'],
    'scope':'Complete finite GL2 model only; source and U3 comparisons are separate.',
}
out = HERE/f'gl2_e{args.e}_residual_certificate.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'output':str(out), 'all_units':report['all_units'],
                  'case_count':len(rows)}), flush=True)
