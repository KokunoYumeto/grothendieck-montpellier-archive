"""Full GL2 model extension to e=26,28,30; earlier certificates unchanged.

Reuses the already audited integer series and matrix arithmetic routines.
The complete uniform modular basis proof is gl2_general_section.tex.
No stored Hecke matrix is input.
"""
from pathlib import Path
from hashlib import sha256
import importlib.util
import json

HERE = Path(__file__).parent
BASE = HERE.parent / 'gl2_general_certificate.py'
spec = importlib.util.spec_from_file_location('audited_gl2_arithmetic', BASE)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
c.PRECISION = 260
ES = (26, 28, 30)
PRIMES = (7, 13)

a = [1] + [6*sum(c.chi(d) for d in range(1, n+1) if n % d == 0)
           for n in range(1, c.PRECISION+1)]
b = c.eta_product([(3, 9), (1, -3)], 1)
D = c.eta_product([(1, 6), (3, 6)], 1)
ap = c.powers(a, max(2*e-5 for e in ES))
bp = c.powers(b, max((2*e-5)//3 for e in ES))
degrees = []
for e in ES:
    d = 2*e-5
    dimension = d//3+1
    basis = [c.mul(D, c.mul(ap[d-3*j], bp[j])) for j in range(dimension)]
    leading = [[f[n] for f in basis] for n in range(1, dimension+1)]
    assert all(leading[i][i] == 1 for i in range(dimension))
    assert all(leading[i][j] == 0 for i in range(dimension)
               for j in range(i+1, dimension))
    results = []
    for p in PRIMES:
        columns, raws = [], []
        for f in basis:
            raw = [f[p*n] + (c.chi(p)*p**(2*e)*f[n//p]
                             if n % p == 0 else 0)
                   for n in range(1, dimension+1)]
            coordinates = []
            for i in range(dimension):
                coordinates.append(raw[i]-sum(
                    leading[i][j]*coordinates[j] for j in range(i)))
            for n in range(1, c.PRECISION//p+1):
                target = f[p*n] + (c.chi(p)*p**(2*e)*f[n//p]
                                   if n % p == 0 else 0)
                assert target == sum(coordinates[j]*basis[j][n]
                                     for j in range(dimension))
            columns.append(coordinates)
            raws.append(raw)
        matrix = [[columns[j][i] for j in range(dimension)]
                  for i in range(dimension)]
        raw_rows = [[raws[j][i] for j in range(dimension)]
                    for i in range(dimension)]
        assert c.matrix_multiply(leading, matrix) == raw_rows
        poly = c.characteristic_polynomial(matrix)
        point = 1+p**(2*e)
        for x in (0, 1, point):
            assert c.determinant_bareiss([
                [x*int(i == j)-matrix[i][j] for j in range(dimension)]
                for i in range(dimension)]) == c.evaluate(poly, x)
        value = c.evaluate(poly, point)
        assert value != 0
        results.append({
            'p': p, 'matrix': matrix,
            'initial_hecke_coefficient_rows': raw_rows,
            'charpoly_coefficients': poly,
            'evaluation_point': point, 'evaluation': value,
            'coefficients_checked_through': c.PRECISION//p,
            'independent_bareiss_checks': [0, 1, point],
        })
    degrees.append({
        'e': e, 'weight': 2*e+1, 'dimension': dimension,
        'basis_exponents_a_b': [[d-3*j, j] for j in range(dimension)],
        'leading_coefficient_matrix': leading,
        'results': results,
    })
report = {
    'status': 'PASS: exact complete GL2 modular-form models',
    'precision': c.PRECISION,
    'arithmetic_routines_sha256': sha256(BASE.read_bytes()).hexdigest(),
    'degrees': degrees,
    'scope': 'No Galois-source coverage or K-group deduction in this computation.',
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({
    'status': report['status'], 'output': str(out),
    'summary': [{'e': r['e'], 'weight': r['weight'],
                 'dimension': r['dimension'],
                 'evaluations': {z['p']: z['evaluation'] for z in r['results']}}
                for r in degrees],
}))
