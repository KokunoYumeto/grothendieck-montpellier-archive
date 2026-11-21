"""Independent auxiliary-prime extension of the general modular model.

Reuses only the exact series and matrix routines, not any stored matrix.
The existing frozen 7/13 certificates are not changed.
"""
from pathlib import Path
import json
import gl2_general_certificate as c

c.PRECISION = 380
e, p, dimension = 10, 19, 6
a = [1] + [6*sum(c.chi(d) for d in range(1, n+1) if n % d == 0)
           for n in range(1, c.PRECISION+1)]
b = c.eta_product([(3, 9), (1, -3)], 1)
D = c.eta_product([(1, 6), (3, 6)], 1)
ap, bp = c.powers(a, 15), c.powers(b, 5)
basis = [c.mul(D, c.mul(ap[15-3*j], bp[j])) for j in range(dimension)]
leading = [[f[n] for f in basis] for n in range(1, dimension+1)]
assert all(leading[i][i] == 1 for i in range(dimension))
assert all(leading[i][j] == 0 for i in range(dimension)
           for j in range(i+1, dimension))
columns = []
for f in basis:
    target = [f[p*n] + (p**(2*e)*f[n//p] if n % p == 0 else 0)
              for n in range(1, dimension+1)]
    coordinates = []
    for i in range(dimension):
        coordinates.append(target[i]-sum(leading[i][j]*coordinates[j]
                                         for j in range(i)))
    for n in range(1, c.PRECISION//p+1):
        assert f[p*n] + (p**(2*e)*f[n//p] if n % p == 0 else 0) == sum(
            coordinates[j]*basis[j][n] for j in range(dimension))
    columns.append(coordinates)
matrix = [[columns[j][i] for j in range(dimension)] for i in range(dimension)]
poly = c.characteristic_polynomial(matrix)
point = 1+p**(2*e)
for x in (0, 1, point):
    assert c.determinant_bareiss([
        [x*int(i == j)-matrix[i][j] for j in range(dimension)]
        for i in range(dimension)]) == c.evaluate(poly, x)
report = {
    'status': 'PASS: exact weight-21 T19 extension',
    'e': e, 'weight': 21, 'p': p, 'dimension': dimension,
    'precision': c.PRECISION, 'extra_coefficients_through': c.PRECISION//p,
    'matrix': matrix, 'charpoly_coefficients': poly,
    'evaluation_point': point, 'evaluation': c.evaluate(poly, point),
    'residue_at_9496386083': c.evaluate(poly, point) % 9496386083,
    'scope': 'Modular-form model only; no K-group assertion.',
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report))
