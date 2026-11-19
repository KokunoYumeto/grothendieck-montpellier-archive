#!/usr/bin/env python3
"""Exact finite data and symbolic maps for work-note Section40."""
from pathlib import Path
from datetime import datetime, timezone
import json,time
import sympy as S
start=datetime.now(timezone.utc).isoformat(); t0=time.perf_counter()
x,y,hstar,hplus,c,z,zbar,Z=S.symbols('x y hstar hplus c z zbar Z')
q=S.symbols('q')
Fstar=y**2-4*x**3+4*x+1
u,Y=-x,S.I*y
Fplus=Y**2-4*u**3+4*u-1
vr,vi,Zr,h,cc=S.symbols('vr vi Zr h cc',real=True)
vv=vr+S.I*vi
ZZ=Zr+S.I*(h-cc)*vi
W=S.expand(ZZ-h*vv-cc*S.conjugate(vv))
eps=q-q**2-q**3
qcoef=S.expand(S.series(1/eps-hplus*eps,q,0,2).removeO()).coeff(q,1)
counts={p:[sum((b*b+b-(a*a*a-a))%p==0 for b in range(p)) for a in range(p)] for p in (2,3)}
orders={p:1+sum(v) for p,v in counts.items()}
fix2=[a for a in range(37) if (a*a+1)%37==0]
fix3=[a for a in range(37) if (a*a+a+1)%37==0]
ram=[(38-len(fix2))//2,2*(38-len(fix3))//3,38-2]
two_g_minus_two=-2*38+sum(ram)
checks={
 'Q_i_curve_isomorphism':S.expand(Fplus+Fstar)==0,
 'holomorphic_differential_factor':S.simplify(S.diff(u,x)/S.I-S.I)==0,
 'second_kind_differential_factor':S.simplify(u*S.diff(u,x)/S.I+S.I*x)==0,
 'q_coefficient':qcoef==2-hplus,
 'twisted_q_coefficient':qcoef.subs(hplus,-hstar)==2+hstar,
 'compact_value_real_component_formula':S.simplify(W-(Zr-(h+cc)*vr))==0,
 'compact_value_twist':S.simplify((-S.I*Z)-(-hstar)*(S.I*z)-c*(-S.I*zbar)+S.I*(Z-hstar*z-c*zbar))==0,
 'good_reduction_orders':orders=={2:5,3:7},
 'coprime_reduction_orders':S.gcd(orders[2],orders[3])==1,
 'elliptic_fixed_points':fix2==[6,31] and fix3==[10,26],
 'Riemann_Hurwitz_genus2':ram==[18,24,36] and two_g_minus_two==2,
}
assert all(checks.values()),checks
elapsed=time.perf_counter()-t0
record={'result':'ELL-ROUTE-40','utc_start':start,'elapsed_seconds':elapsed,
 'software':'SymPy '+S.__version__,
 'inputs':{'curves':['y^2=4x^3-4x-1','Y^2=4u^3-4u+1','v^2+v=u^3-u'],
  'map':['u=-x','Y=i*y'],'point_minimal':[0,-1],'primes':[2,3],'level':37},
 'solution_counts':counts,'group_orders':orders,'order2_fixed_points':fix2,'order3_fixed_points':fix3,
 'ramification_contributions':ram,'checks':checks,
 'scope':'Exact finite normalization, point-count and genus data; transcendence uses the proved compact-point theorem, not numerical recognition.'}
p=Path(__file__);p.with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
output='Section40 finite certificate: '+str(len(checks))+' exact checks PASS\n'+'\n'.join(k+': PASS' for k in checks)+'\nCounts '+repr(counts)+'; orders '+repr(orders)+'\nFixed points '+repr(fix2)+', '+repr(fix3)+'; ramification '+repr(ram)+'\nElapsed seconds: '+str(elapsed)+'\n'
p.with_suffix('.out').write_text(output);print(output,end='')
