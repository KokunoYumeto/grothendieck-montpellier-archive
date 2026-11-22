#!/usr/bin/env python3
"""Independent exact checks for the prime-conductor cyclic-sextic comparison.

These checks verify finite algebra and rational constants.  They do not verify
the imported analytic number theory or run a proof assistant.
"""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
A, B, C, a, c, x, y = s.symbols('A B C a c x y')
columns = [
    [A, -A, A, -A, A, -A],
    [B, C, -B-C, B, C, -B-C],
    [C, -B-C, B, C, -B-C, B],
    [a, a+c, c, -a, -a-c, -c],
    [a+c, c, -a, -a-c, -c, a],
]
matrix = s.Matrix.hstack(*(s.Matrix(v[:5]) for v in columns))
determinant = s.factor(matrix.det())
expected = 12*A*(B*B+B*C+C*C)*(a*a+a*c+c*c)
assert s.expand(determinant-expected) == 0
q = x*x+y*y-x*y
identities = [
    (q-s.Rational(3,4)*x*x, (y-x/2)**2),
    (q-s.Rational(3,4)*y*y, (x-y/2)**2),
    (q-s.Rational(3,4)*(x-y)**2, (x+y)**2/4),
]
assert all(s.expand(lhs-rhs) == 0 for lhs, rhs in identities)
gras_difference = 4*a*a+20-(3*a*a+4*a+10+4/a+3/a**2)
gras_positive = ((a-1)**4+4*(a-1)*(a+1))/a**2
assert s.factor(gras_difference-gras_positive) == 0

# Analytic class-number factors: 32/(2*4)=4, then R6/(R2R3)=12R*/Q.
class_factor = Fraction(32, 2*4)*12
assert class_factor == 48
combined_factor = Fraction(12,48)*Fraction(1,4)/Fraction(3,16)
assert combined_factor == Fraction(1,3)
coarse_factor = combined_factor*Fraction(21,18)**2
assert coarse_factor == Fraction(49,108) < 1
assert 31*Fraction(2,3) > 20

files = {
    'class_product_proof': ROOT/'evidence/main_gate/sextic_class_product.tex',
    'gras_primary': ROOT/'evidence/lean_chain/primary/sextic_followup/Gras_1986.pdf',
    'louboutin_2002_primary': ROOT/'evidence/lean_chain/primary/sextic_followup/Louboutin_2002_even.pdf',
    'louboutin_2004_primary': ROOT/'evidence/lean_chain/primary/sextic_followup/Louboutin_2004.pdf',
}
report = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'Exact finite algebra and rational constants only; no Lean execution.',
    'determinant': str(determinant),
    'quadratic_completions': 'three exact square identities passed',
    'gras_elementary_bound': 'exact nonnegative-polynomial identity passed',
    'class_number_factor': str(class_factor),
    'combined_L_regulator_factor': str(combined_factor),
    'large_prime_upper_factor': str(coarse_factor),
    'threshold_log_argument': 'log(2)>2/3 implies log(2^31)>20; log(5)<2; kappa0<1',
    'files': {name: {'path': str(path), 'sha256': sha256(path.read_bytes()).hexdigest()}
              for name, path in files.items()},
    'result': 'PASS',
}
(HERE/'independent_checks.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
