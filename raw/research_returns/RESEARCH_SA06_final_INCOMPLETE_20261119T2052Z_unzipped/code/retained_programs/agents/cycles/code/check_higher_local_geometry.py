"""Finite symbolic checks accompanying the proved C.3ae geometry.

The matrix and base-point certificates have separate retained scripts.
This script does not replace the conormal, Chow, or family arguments.
"""
from pathlib import Path
from itertools import product
from datetime import datetime, timezone
import json
import time
import sympy as sp

start = time.perf_counter()
base = Path(__file__).resolve().parents[1]
w = sp.symbols('w0:4')
z = sp.symbols('z0:3')
eta, v, u, q, r, m = sp.symbols('eta v u q r m')
FW = sum(x**4 for x in w)
FC = sum(x**4 for x in z)
G = sum(z[i]**2*z[j]**2 for i in range(3) for j in range(i+1,3))
eta_relation = sp.groebner([eta**4+1], eta, q, r)
line_value = eta_relation.reduce(FW.subs({w[0]:eta*q,w[1]:q,w[2]:eta*r,w[3]:r}))[1]
curve_value = sp.rem(FC.subs({z[0]:u,z[1]:v,z[2]:1}), v**4+1+u**4, v)
base_value = sp.rem(FC.subs({z[0]:1,z[1]:eta,z[2]:0}), eta**4+1, eta)
jac = sp.groebner([x**3 for x in z],*z)
curve_basis = [jac.reduce(x*G)[1] for x in z]
expected = [z[0]*z[1]**2*z[2]**2,z[0]**2*z[1]*z[2]**2,z[0]**2*z[1]**2*z[2]]
mon3 = [e for e in product(range(3),repeat=4) if sum(e)==3]
mon4 = [e for e in product(range(3),repeat=4) if sum(e)==4]
factorable = all(any(e[j]>0 and tuple(e[k]-(1 if k==j else 0) for k in range(4)) in mon3
                     for j in range(4)) for e in mon4)
tau_H = 4*1-4
tau_D = 4*(-2)-1
assert line_value==curve_value==base_value==0
assert curve_basis==expected
assert (len(mon3),len(mon4))==(16,19)
assert factorable and tau_H==0 and tau_D==-9
rank_record = json.loads((base/'output/test_quartic_obstruction_rank.json').read_text())
base_record = json.loads((base/'output/check_quartic_sections_basepoints.json').read_text())
record = {
    'utc':datetime.now(timezone.utc).isoformat(),
    'line_substitution_zero':line_value==0,
    'curve_generic_point_zero':curve_value==0,
    'curve_base_point_zero':base_value==0,
    'Fermat_gradients':[str(sp.diff(FW,x)) for x in w],
    'Fermat_gradient_argument':'In characteristic zero these vanish simultaneously only at the excluded projective origin.',
    'curve_boundary_basis':[str(x) for x in curve_basis],
    'Jacobian_dimensions':[len(mon3),len(mon4)],
    'every_degree4_monomial_is_variable_times_degree3':factorable,
    'intersection_tau_H':tau_H,'intersection_tau_D':tau_D,
    'dimensions':{'dim_W':2,'dim_C':1,'dim_S':3,'dim_V':'m+3','dim_Z':'m+4=N',
                  'rank_E':'m','dim_H':'m+2','minimal_m':3,'minimal_N':7},
    'rank_certificate_full_column_rank':rank_record['full_column_rank_found'],
    'basepoint_certificate_file':'output/check_quartic_sections_basepoints.json',
    'scope':'Finite polynomial and intersection-arithmetic checks only. The full proof separately establishes localization, Chern obstruction and actual-family compatibility.',
    'runtime_seconds':time.perf_counter()-start
}
(base/'output/check_higher_local_geometry.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
