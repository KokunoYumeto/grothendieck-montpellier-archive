"""Exact integral Hecke matrices for S_(2e+1)(Gamma_0(3), chi_-3).

The basis D*a^(2e-5-3j)*b^j is proved using the polynomial ring
M(Gamma_1(3)) = C[a,b] and division by the cusp form D.  The full proof
is in gl2_general_section.tex.  This standard-library program computes
the Fourier expansions, solves in the unitriangular integral basis,
checks extra Hecke coefficients, and computes characteristic polynomials.
It makes no Galois-conductor or algebraic K-group claim.
"""

from pathlib import Path
from math import comb
import json

PRECISION = 182
ES = (6, 8, 10, 12)
PRIMES = (7, 13)


def mul(a, b):
    out = [0] * (PRECISION + 1)
    for i, x in enumerate(a):
        if x:
            for j in range(min(len(b), PRECISION + 1 - i)):
                if b[j]:
                    out[i+j] += x * b[j]
    return out


def powers(a, largest):
    out = [[1] + [0] * PRECISION]
    for _ in range(largest):
        out.append(mul(out[-1], a))
    return out


def eta_product(factors, shift):
    out = [0] * shift + [1] + [0] * (PRECISION - shift)
    for scale, exponent in factors:
        for t in range(scale, PRECISION + 1, scale):
            factor = [0] * (PRECISION + 1)
            for k in range(PRECISION // t + 1):
                if exponent >= 0:
                    if k > exponent:
                        break
                    c = (-1)**k * comb(exponent, k)
                else:
                    c = comb(-exponent+k-1, k)
                factor[t*k] = c
            out = mul(out, factor)
    return out


def chi(n):
    return 0 if n % 3 == 0 else 1 if n % 3 == 1 else -1


def matrix_multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def characteristic_polynomial(a):
    """Faddeev--LeVerrier, with exact divisibility checked each step."""
    n = len(a)
    b = [[int(i == j) for j in range(n)] for i in range(n)]
    coefficients = [1]
    for k in range(1, n+1):
        b = matrix_multiply(a, b)
        negative_trace = -sum(b[i][i] for i in range(n))
        c, rem = divmod(negative_trace, k)
        assert rem == 0
        coefficients.append(c)
        for i in range(n):
            b[i][i] += c
    assert all(x == 0 for row in b for x in row)
    return coefficients


def determinant_bareiss(a):
    """Independent determinant check, retaining exact integral divisions."""
    a = [row[:] for row in a]
    n = len(a)
    previous = 1
    sign = 1
    for k in range(n-1):
        if a[k][k] == 0:
            swap = next((i for i in range(k+1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = pivot*a[i][j] - a[i][k]*a[k][j]
                value, rem = divmod(numerator, previous)
                assert rem == 0
                a[i][j] = value
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def evaluate(poly, x):
    out = 0
    for c in poly:
        out = out*x+c
    return out


def main():
    a = [1] + [6*sum(chi(d) for d in range(1, n+1) if n % d == 0)
               for n in range(1, PRECISION+1)]
    b = eta_product([(3, 9), (1, -3)], 1)
    D = eta_product([(1, 6), (3, 6)], 1)
    ap = powers(a, max(2*e-5 for e in ES))
    bp = powers(b, max((2*e-5)//3 for e in ES))
    reports = []
    for e in ES:
        d = 2*e-5
        dimension = d//3+1
        basis = [mul(D, mul(ap[d-3*j], bp[j]))
                 for j in range(dimension)]
        leading = [[f[n] for f in basis]
                   for n in range(1, dimension+1)]
        assert all(leading[i][i] == 1 for i in range(dimension))
        assert all(leading[i][j] == 0
                   for i in range(dimension) for j in range(i+1, dimension))
        results = []
        for p in PRIMES:
            columns = []
            raw = []
            for f in basis:
                v = [f[p*n] + (chi(p)*p**(2*e)*f[n//p]
                                if n % p == 0 else 0)
                     for n in range(1, dimension+1)]
                raw.append(v)
                c = []
                for i in range(dimension):
                    c.append(v[i]-sum(leading[i][j]*c[j] for j in range(i)))
                for n in range(1, PRECISION//p+1):
                    actual = f[p*n] + (chi(p)*p**(2*e)*f[n//p]
                                       if n % p == 0 else 0)
                    assert actual == sum(c[j]*basis[j][n]
                                         for j in range(dimension))
                columns.append(c)
            matrix = [[columns[j][i] for j in range(dimension)]
                      for i in range(dimension)]
            raw_rows = [[raw[j][i] for j in range(dimension)]
                        for i in range(dimension)]
            assert matrix_multiply(leading, matrix) == raw_rows
            poly = characteristic_polynomial(matrix)
            point = 1+p**(2*e)
            value = evaluate(poly, point)
            assert value != 0
            # Two complete, independent determinant evaluations.
            for x in (point, 0, 1):
                assert determinant_bareiss([
                    [x*int(i == j)-matrix[i][j] for j in range(dimension)]
                    for i in range(dimension)]) == evaluate(poly, x)
            results.append({
                'p': p,
                'initial_hecke_coefficient_rows': raw_rows,
                'matrix': matrix,
                'charpoly_coefficients': poly,
                'evaluation_point': point,
                'evaluation': value,
                'all_coefficients_checked_through': PRECISION//p,
                'independent_bareiss_checks': [point, 0, 1],
            })
        reports.append({
            'e': e, 'weight': 2*e+1, 'dimension': dimension,
            'basis_exponents_a_b': [[d-3*j, j] for j in range(dimension)],
            'leading_coefficient_matrix': leading,
            'basis_coefficients_through_13': [f[:14] for f in basis],
            'results': results,
        })
    # Reproduce the independently certified weight-thirteen control.
    control = reports[0]
    assert control['results'][0]['charpoly_coefficients'] == [
        1, 73002, -10736848500, 248682833875000]
    assert control['results'][1]['charpoly_coefficients'] == [
        1, 6829482, -22485145931700, 15494586622814755000]
    report = {
        'status': 'PASS: exact complete modular-form model',
        'precision': PRECISION,
        'degrees': reports,
        'scope': 'No Galois-conductor, unitary-transfer, or K-group assertion.',
    }
    out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({
        'status': report['status'], 'output': str(out),
        'summary': [
            {'e': r['e'], 'dimension': r['dimension'], 'results': [
                {k: z[k] for k in ('p', 'charpoly_coefficients',
                                   'evaluation_point', 'evaluation')}
                for z in r['results']]}
            for r in reports],
    }))


if __name__ == '__main__':
    main()
