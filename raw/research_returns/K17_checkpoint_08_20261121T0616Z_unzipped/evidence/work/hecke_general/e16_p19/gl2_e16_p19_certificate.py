"""Complete weight-33, conductor-3 T19 calculation using the proved basis."""
from pathlib import Path
from hashlib import sha256
import importlib.util
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'gl2_general_certificate.py'
spec = importlib.util.spec_from_file_location('exact_gl2_base', BASE)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
c.PRECISION = 380
e, p, residual = 16, 19, 25078104767246023
d = 2*e-5
dimension = d//3+1

a = [1] + [6*sum(c.chi(t) for t in range(1,n+1) if n%t == 0)
           for n in range(1,c.PRECISION+1)]
b = c.eta_product([(3,9),(1,-3)],1)
D = c.eta_product([(1,6),(3,6)],1)
ap, bp = c.powers(a,d), c.powers(b,dimension-1)
basis = [c.mul(D,c.mul(ap[d-3*j],bp[j])) for j in range(dimension)]
leading = [[f[n] for f in basis] for n in range(1,dimension+1)]
assert dimension == 10
assert all(leading[i][i] == 1 for i in range(dimension))
assert all(leading[i][j] == 0 for i in range(dimension)
           for j in range(i+1,dimension))
columns, raw_columns = [], []
for f in basis:
    raw = [f[p*n] + (c.chi(p)*p**(2*e)*f[n//p] if n%p == 0 else 0)
           for n in range(1,dimension+1)]
    coordinates = []
    for i in range(dimension):
        coordinates.append(raw[i]-sum(leading[i][j]*coordinates[j]
                                      for j in range(i)))
    for n in range(1,c.PRECISION//p+1):
        actual = f[p*n] + (c.chi(p)*p**(2*e)*f[n//p] if n%p == 0 else 0)
        assert actual == sum(coordinates[j]*basis[j][n]
                             for j in range(dimension))
    columns.append(coordinates)
    raw_columns.append(raw)
matrix = [[columns[j][i] for j in range(dimension)] for i in range(dimension)]
raw_rows = [[raw_columns[j][i] for j in range(dimension)] for i in range(dimension)]
assert c.matrix_multiply(leading,matrix) == raw_rows
polynomial = c.characteristic_polynomial(matrix)
point = 1+p**(2*e)
for x in (0,1,point):
    assert c.determinant_bareiss([
        [x*int(i==j)-matrix[i][j] for j in range(dimension)]
        for i in range(dimension)]) == c.evaluate(polynomial,x)
value = c.evaluate(polynomial,point)
assert value != 0
report = {
    'status':'PASS complete exact weight-33 T19 model',
    'arithmetic_source_sha256':sha256(BASE.read_bytes()).hexdigest(),
    'e':e,'weight':2*e+1,'p':p,'dimension':dimension,
    'precision':c.PRECISION,'coefficient_checks_through':c.PRECISION//p,
    'basis_exponents_a_b':[[d-3*j,j] for j in range(dimension)],
    'leading_coefficient_matrix':leading,'matrix':matrix,
    'initial_hecke_coefficient_rows':raw_rows,
    'charpoly_coefficients':polynomial,'evaluation_point':point,
    'evaluation':value,'residual_prime':residual,
    'evaluation_mod_residual':value%residual,
    'independent_Bareiss_points':[0,1,point],
    'scope':'Complete GL2 model only; U3 branch and source implications are separate.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({key:report[key] for key in (
    'status','e','p','dimension','charpoly_coefficients',
    'residual_prime','evaluation_mod_residual')}))
