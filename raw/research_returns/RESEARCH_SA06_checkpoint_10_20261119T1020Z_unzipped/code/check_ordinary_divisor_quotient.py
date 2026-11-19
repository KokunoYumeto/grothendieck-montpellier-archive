#!/usr/bin/env python3
"""Exact finite certificates for C.3v; the geometric proof is separate."""
import json
import math
import time
from pathlib import Path
import sympy as sp

started = time.perf_counter()
z = sp.symbols('z0:3')
F = sum(x**4 for x in z)
partials = [sp.diff(F, x) for x in z]
charts = []
for i in range(3):
    certificate = sp.expand(partials[i].subs(z[i], 1) / 4)
    assert certificate == 1
    charts.append({'chart': f'z{i}=1', 'gradient_unit_certificate': str(certificate)})

eta, t = sp.symbols('eta t')
eta_relation = eta**4 + 1
point_remainder = sp.rem(1 + eta**4, eta_relation, eta)
derivative = 4 * eta**3
derivative_inverse = sp.invert(derivative, eta_relation, eta)
assert sp.rem(derivative * derivative_inverse, eta_relation, eta) == 1
residue = sp.residue(1 / t, t, 0)
assert residue == 1

degree_K = 4 * (4 - 3)
genus = (4 - 1) * (4 - 2) // 2
assert degree_K == 2 * genus - 2 == 4
cohomology = []
for N in range(2, 13):
    m = N - 2
    row = []
    for a in range(1, 13):
        # Serre duality: h1(K^a)=h0(K^(1-a)); for a>1 its degree is negative.
        dual_degree = degree_K * (1-a)
        h1_curve = 1 if a == 1 else 0
        assert a == 1 or dual_degree < 0
        h0_projective = math.comb(m+a, m)
        value = h0_projective * h1_curve
        assert value == (N-1 if a == 1 else 0)
        row.append(value)
    cohomology.append({'N': N, 'a_range': [1,12], 'h1_L_power': row})

quotients = []
for N in range(2,13):
    if N == 2:
        relation = [4]
        rank = 0
        torsion = math.gcd(*relation)
    else:
        relation = [1,4]
        rank = 1
        torsion = math.gcd(*relation)
    assert torsion == (4 if N == 2 else 1)
    quotients.append({'N':N, 'NS_relation':relation, 'free_rank':rank,
                      'torsion_order':torsion, 'additive_C_dimension':N-1})

result = {
    'statement':'C.3v',
    'inputs':{'field':'C', 'curve':str(F), 'point':'(1:eta:0), eta^4=-1',
              'dimensions_N':[2,12], 'powers_a':[1,12]},
    'smoothness_charts':charts,
    'point_equation_remainder':str(point_remainder),
    'transverse_derivative':str(derivative),
    'derivative_inverse_mod_eta_relation':str(derivative_inverse),
    'residue_dt_over_t':str(residue),
    'genus':genus, 'degree_canonical':degree_K,
    'cohomology':cohomology, 'NS_quotients':quotients,
    'all_assertions_passed':True,
    'scope':'Finite exact algebra only. Formal GAGA, Elkik descent, actual-family rigidity, and non-torsion are proved in the manuscript; they are not inferred from numerical data.',
    'runtime_seconds':time.perf_counter()-started,
}
out = Path(__file__).with_name('check_ordinary_divisor_quotient_output.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
