"""Independent arithmetic check for A20 using a 4x4 integer companion matrix."""
from pathlib import Path
import json
from sympy import Matrix, Poly, eye, symbols

T = symbols('T')
weil = T**4+T**3+2*T+4
C = Matrix([[0,0,0,-4], [1,0,0,-2], [0,1,0,0], [0,0,1,-1]])
assert C.charpoly(T).as_expr() == weil
mod3 = Poly(weil, T, modulus=3)
gcd = mod3.gcd(mod3.diff())
remainder = Poly(T**20-1, T, modulus=3).rem(mod3)
assert gcd.degree() == 0 and remainder.is_zero
power_mod3 = (C**20).applyfunc(lambda a: int(a) % 3)
assert power_mod3 == eye(4)
h = int((eye(4)-C**20).det())
v3, cofactor = 0, h
while cofactor % 3 == 0:
    cofactor //= 3
    v3 += 1
assert h == 1099812538656 and v3 == 4
result = dict(status='PASS',weil_polynomial=str(weil),
              method='det(I-C^20), C the integer companion matrix, not a claimed Tate-basis matrix',
              gcd_mod3=str(gcd.as_expr()), remainder_T20_minus_1_mod3=str(remainder.as_expr()),
              companion_20_mod3=[[int(v) for v in row] for row in power_mod3.tolist()], jacobian_order=h,
              valuation_at_3=v3, cofactor_after_3_part=cofactor,
              logical_use='P divides T^20-1 modulo3; Cayley-Hamilton gives Frobenius^20=1 on J[3]. With v3(h)=4, rational 3-primary torsion is exactly J[3].')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
