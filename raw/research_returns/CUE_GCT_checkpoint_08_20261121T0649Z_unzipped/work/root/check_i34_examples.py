"""Independent exact checks of I34's two explicit counterexamples."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as sp

root = Path(__file__).resolve().parent
T, Z = sp.symbols('T Z')
A, B, C, Q, R, S = sp.symbols('A B C Q R S')
vars3 = (A, B, C, Q, R, S)
primes3 = (1663, 523, 139, 127, 1093, 331)
poly3 = (1-A)*(1-S**2) - (1-R**2)*(1-C) - C*(1-B)*(1-Q**12)
assert all(sp.isprime(p) for p in primes3)
assert min(primes3) > 2*12*(6-1)
assert sp.Poly(poly3, *vars3).coeff_monomial(A*S**2) == 1
curve3 = sp.expand(poly3.subs(dict(zip(vars3, (T**p for p in primes3)))))
assert curve3 == 0
cylinder3 = sp.expand(poly3.subs({A:Z, **dict(zip(vars3[1:], (T**p for p in primes3[1:])))}))
assert sp.expand(cylinder3 - (T**1663-Z)*(1-T**662)) == 0

xs = sp.symbols('x1:9')
primes4 = (17, 19, 23, 29, 31, 37, 41, 43)
poly4 = (xs[0]*xs[7]-xs[1]*xs[6])*(xs[2]*xs[5]-xs[3]*xs[4])
assert all(sp.isprime(p) for p in primes4)
assert min(primes4)>2*(8-1)
single_cylinders = []
for i in range(8):
    substitutions = {x:(Z if j==i else T**primes4[j]) for j,x in enumerate(xs)}
    value = sp.expand(poly4.subs(substitutions))
    assert value == 0
    single_cylinders.append(str(value))
U, V = sp.symbols('U V')
double = sp.expand(poly4.subs({x:(U if i==0 else V if i==2 else T**primes4[i]) for i,x in enumerate(xs)}))
assert double != 0
left = (xs[0],xs[7],xs[2],xs[5]); right=(xs[1],xs[6],xs[3],xs[4])
pp=sp.Poly(poly4,*left,*right)
row_keys=sorted({mon[:4] for mon,_ in pp.terms()})
col_keys=sorted({mon[4:] for mon,_ in pp.terms()})
matrix=sp.Matrix([[pp.coeff_monomial(r+c) for c in col_keys] for r in row_keys])
assert matrix.shape == (4,4)
assert abs(matrix.det()) == 1

result={
 'checked_utc':datetime.now(timezone.utc).isoformat(),
 'who':'GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1',
 'method':'SymPy exact integer polynomial expansion, primality, and coefficient flattening; no floating point',
 'three_product_primes':primes3,'three_product_curve_zero':True,
 'three_product_cylinder_identity':str(cylinder3),
 'four_product_primes':primes4,'all_eight_single_cylinders_zero':True,
 'two_coordinate_cylinder_nonzero':True,
 'coefficient_flattening':list(map(list,matrix.tolist())),
 'flattening_determinant':int(matrix.det()),
 'all_characteristics':'Integer identities and a determinant of plus or minus one certify these examples in every characteristic.'
}
(root/'i34_example_check.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
print(json.dumps(result,default=int))
