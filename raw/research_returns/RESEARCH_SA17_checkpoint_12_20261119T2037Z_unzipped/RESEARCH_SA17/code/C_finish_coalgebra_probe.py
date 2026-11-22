"""Initial exact O3 coordinate Groebner feasibility probe, before the full certificate."""
import sympy as s
import time
import json
x = s.symbols('x0:9')
X = s.Matrix(3, 3, x)
f = X.T*X-s.eye(3)
t = time.perf_counter()
g = s.groebner([f[i, j] for i in range(3) for j in range(i, 3)],
               *x, order='grevlex', modulus=3)
print(json.dumps({'basis_size': len(g.polys), 'seconds': time.perf_counter()-t,
                  'leading_degrees': [sum(h.LM(order=g.order).exponents) for h in g.polys]}))
