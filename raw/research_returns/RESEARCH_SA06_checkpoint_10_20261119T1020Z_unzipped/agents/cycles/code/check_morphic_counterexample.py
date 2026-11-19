"""Finite algebraic certificates for the specified E.3u construction.

The proof, not this finite computation, supplies generic smoothness,
Lawson nonvanishing, the Hodge-theoretic cylinder and N-nonvanishing.
"""
from pathlib import Path
from datetime import datetime, timezone
from math import comb
import json
import time
import sympy as s

start=time.perf_counter()
root = Path(__file__).resolve().parents[1]
x = s.symbols('x0:4')
y = s.symbols('y0:4')
q = sum(x[j]*y[j] for j in range(4))
pi_plus = {xx:0 for xx in x}
pi_minus = {y[0]:0, x[1]:0, x[2]:0, x[3]:0}
assert s.expand(q.subs(pi_plus)) == 0
assert s.expand(q.subs(pi_minus)) == 0
assert [s.diff(q, xx) for xx in x] == list(y)
assert [s.diff(q, yy) for yy in y] == list(x)
assert s.expand(q.subs({x[1]:0,x[2]:0,x[3]:0})) == x[0]*y[0]
t=s.symbols('t')
self_intersection=s.expand(s.series((1+t)**4/(1+2*t),t,0,4).removeO()).coeff(t,3)
assert self_intersection == 0
mixed_intersection = 1 - self_intersection
zeta_square=2*self_intersection-2*mixed_intersection
assert zeta_square == -2
D=14
basis_count=comb(D+7,7)-comb(D+5,7)
assert basis_count > 1
assert D >= 6 and D >= 12
n,r,j=5,2,1
u_degree=2*n-2*r+2*j
cycle_degree=2*n-2*r
assert (u_degree,cycle_degree) == (8,6)
required_relative=max(u_degree+1,cycle_degree+1)
assert required_relative == 9 and required_relative <= 2*n
omega=s.Matrix([[0,1],[-1,0]])
assert omega.det()==1
dual_checks=0
for a in range(-5,6):
 for b in range(-5,6):
  if a==b==0: continue
  v=s.Matrix([a,b])
  w=s.Matrix([0,1]) if a else s.Matrix([1,0])
  assert (v.T*omega*w)[0] != 0
  dual_checks += 1
u=s.symbols('u')
assert s.discriminant(u**3-u,u)==4
weierstrass_discriminant=-16*(4*(-1)**3+27*0**2)
assert weierstrass_discriminant==64
record={
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'all finite algebraic assertions passed',
 'quadric_dimension':6,'ambient_projective_dimension':7,
 'quadric_gradient':'partials are y0,...,y3,x0,...,x3; no common projective zero',
 'plane_dimensions':[3,3], 'plane_self_intersection':int(self_intersection),
 'plane_mixed_intersection':int(mixed_intersection),'zeta_square':int(zeta_square),
 'hypersurface_degree':D,'degree14_basis_count':basis_count,
 'independent_coefficient_count':basis_count-1,
 'Y_dimension':5,'X_dimension':6,'gamma_dimension':2,'cycle_codimension':4,
 'Nagel_conditions':{'C':[D,6],'C0':[D,12]},
 'Friedlander_cohomology_degrees':[u_degree,cycle_degree],
 'relative_degree_required':required_relative,'relative_degree_available':2*n,
 'elliptic_discriminant':weierstrass_discriminant,
 'elliptic_pairing_determinant':int(omega.det()),'finite_pairing_checks':dual_checks,
 'scope':'Lawson nonvanishing, arbitrary-field witness transfer, countability and nontorsion modulo N are established in the proof; no extrapolation from the finite checks is used.'
}
record['runtime_seconds']=time.perf_counter()-start
(root/'output/check_morphic_counterexample.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
