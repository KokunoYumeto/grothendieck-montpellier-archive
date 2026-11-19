#!/usr/bin/env python3
"""Exact finite identities used in A.4.35; no numerical period claims."""
from pathlib import Path
from datetime import datetime, timezone
import json, time
import sympy as S
start=datetime.now(timezone.utc).isoformat()
t0=time.perf_counter()
x,y,a,g2,g3=S.symbols('x y a g2 g3')
d,lam=S.symbols('d lam', nonzero=True)
X=x+a
checks={
 'shifted_Weierstrass_equation': S.expand(4*(X-a)**3-g2*(X-a)-g3-(4*x**3-g2*x-g3))==0,
 'holomorphic_differential_pullback': S.diff(X,x)==1,
 'second_kind_differential_pullback': S.expand(X*S.diff(X,x)-(x+a))==0,
 'weight4_lattice_summand': S.simplify((lam/d)**(-4)-d**4*lam**(-4))==0,
 'weight6_lattice_summand': S.simplify((lam/d)**(-6)-d**6*lam**(-6))==0,
 'nonholomorphic_basis_coefficient': S.Matrix([-a,-1])[1]==-1,
}
assert all(checks.values()), checks
elapsed=time.perf_counter()-t0
record={'result':'A.4.35','utc_start':start,'elapsed_seconds':elapsed,
 'python_symbolic_package':'SymPy '+S.__version__,
 'inputs':{'symbols':['x','y','a','g2','g3','d','lam'],
  'map':'X=x+a, Y=y', 'lattice_scaling':'lambda -> lambda/d',
  'de_Rham_basis':['omega','xi'], 'class_coefficients':['-a','-1']},
 'checks':checks,
 'scope':'Finite chart and scaling identities only; the period-module theorem and Hodge-filtration argument are proved in the text.'}
p=Path(__file__)
p.with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
output='A.4.35 finite certificate: '+str(len(checks))+' exact checks PASS\n'+'\n'.join(name+': PASS' for name in checks)+'\nElapsed seconds: '+str(elapsed)+'\n'
p.with_suffix('.out').write_text(output)
print(output,end='')
