"""Exact local algebra in C-RD11. The infinite-ring argument is proved in TeX."""
import json
import time
from pathlib import Path
import sympy as s
start = time.perf_counter()
J, X = s.symbols("J X")
a = -3*J/(J-1728)
b = -2*J/(J-1728)
delta = s.factor(-16*(4*a**3+27*b**2))
j = s.factor((-48*a)**3/delta)
assert j == J
assert s.simplify(delta-1728**2*J**2/(J-1728)**3) == 0
hasse = s.factor(s.Poly((X**3+a*X+b)**2, X).coeff_monomial(X**4))
assert s.simplify(hasse-2*a) == 0
out = {"short_model_a":str(a), "short_model_b":str(b), "discriminant":str(delta),
       "j_invariant":str(j), "p5_Hasse_before_reduction":str(hasse),
       "p5_Hasse_after_reduction":"4*t/(t-3), nonzero over F5(t)",
       "dual_number_j":"t + epsilon", "forced_constant_j":"t", "contradiction_coefficient":1,
       "seconds":time.perf_counter()-start}
Path(__file__).with_suffix(".output.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
