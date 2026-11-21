"""Independent standard-library arithmetic check for K17-K12-VANISH."""
from math import isqrt, prod
from pathlib import Path
import json

p = 7
e = 6
target_numerator = p**(2*e) + p**e + 1
u3_eigenvalue = 157899
gl2_target = 1 + p**(2*e)
polynomial_value = (
    gl2_target**3 + 73002*gl2_target**2
    - 10736848500*gl2_target + 248682833875000
)
assert polynomial_value == (gl2_target-40250)**2*(gl2_target+153502)
u3_difference = target_numerator-u3_eigenvalue
integer = u3_difference*polynomial_value
factors = {2: 15, 3: 19, 7: 1, 13: 5, 37: 1, 43: 3, 47: 3, 61: 1, 271: 3}
assert integer == 36703455074769833036351681539319447519232
assert integer == prod(q**v for q, v in factors.items())
assert all(q > 1 and all(q % d for d in range(2, isqrt(q)+1)) for q in factors)
assert max(factors) == 271 < 2**31
output = {
    "status": "PASS",
    "target_numerator": target_numerator,
    "u3_difference": u3_difference,
    "gl2_polynomial_value": polynomial_value,
    "integer": integer,
    "prime_factorization": factors,
    "scope": "Exact arithmetic only; mathematical trace coverage is proved in the audited sections."
}
Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
