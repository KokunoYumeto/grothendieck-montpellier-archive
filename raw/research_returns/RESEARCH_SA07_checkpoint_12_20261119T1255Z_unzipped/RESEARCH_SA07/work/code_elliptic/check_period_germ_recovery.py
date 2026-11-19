#!/usr/bin/env python3
"""Exact calculations for work note 43; no arithmetic period conjecture assumed."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as S

started = datetime.now(timezone.utc).isoformat()
timer = time.perf_counter()
tau, J1, J2, J3 = S.symbols('tau J1 J2 J3')
s = S.symbols('s', nonzero=True)
Dtau = lambda f: S.diff(f,tau) + J2*S.diff(f,J1) + J3*S.diff(f,J2)
Dj = lambda f: Dtau(f)/J1
R1 = J2/J1**S.Rational(3,2)
R2 = tau*R1 + 2/S.sqrt(J1)
checks = {
 'twice_j_derivative_first_period': S.simplify(2*Dj(S.sqrt(J1))-R1)==0,
 'twice_j_derivative_second_period_plus_sign': S.simplify(2*Dj(tau*S.sqrt(J1))-R2)==0,
 'printed_minus_differs_by_nonzero_4_over_sqrtJ1': S.simplify(2*Dj(tau*S.sqrt(J1))-(tau*R1-2/S.sqrt(J1))-4/S.sqrt(J1))==0,
}
R1s = (tau**4*J2+2*tau**3*s**2)/(tau*s)**3
R2plus = tau*J2/s**3+2/s
R2s = (-1/tau)*R1s+2/(tau*s)
checks['S_transformation_R1_is_R2plus'] = S.simplify(R1s-R2plus)==0
checks['S_transformation_R2plus_is_minus_R1'] = S.simplify(R2s+J2/s**3)==0

u,a,b,c,d = S.symbols('u a b c d', nonzero=True)
P0=S.Matrix([[a,b],[c,d]])
row=(S.Matrix([[u,u*tau]])*P0.inv())
phi=(a*tau-b)/(d-c*tau)
checks['exact_changed_flat_basis_projective_map'] = S.simplify(row[1]/row[0]-phi)==0
checks['changed_coordinate_value_zero'] = S.simplify(phi.subs(tau,b/a))==0
checks['changed_coordinate_first_derivative_one'] = S.simplify(S.diff(phi,tau).subs(tau,b/a)*(a*d-b*c)/a**2-1)==0

x=S.symbols('x')
t=3+x
N=12
A=S.Matrix([[0,1],[1/(4*t*(1-t)),(2*t-1)/(t*(1-t))]])
Ak=[A.applyfunc(lambda q,k=k:S.expand(S.series(q,x,0,N+1).removeO()).coeff(x,k)) for k in range(N)]
Fc=[S.eye(2)]
for n in range(N):
    Fc.append(sum((Ak[k]*Fc[n-k] for k in range(n+1)),S.zeros(2))/(n+1))
F=sum((Fc[n]*x**n for n in range(N+1)),S.zeros(2))
checks['rational_normalized_fundamental_coefficients'] = all(v.is_Rational for m in Fc for v in m)
checks['fundamental_initial_identity'] = F.subs(x,0)==S.eye(2)
res=F.diff(x)-A*F
checks['Picard_Fuchs_system_through_degree_11'] = all(S.series(q,x,0,N).removeO()==0 for q in res)
checks['Wronskian_exact_formula_through_degree_12'] = S.series(F.det()+6/(t*(1-t)),x,0,N+1).removeO()==0
phiser=S.series(F[0,1]/F[0,0],x,0,N+1).removeO().expand()
checks['projective_germ_initial_zero_derivative_one'] = phiser.subs(x,0)==0 and S.diff(phiser,x).subs(x,0)==1
checks['projective_germ_first_12_coefficients_rational'] = all(phiser.coeff(x,n).is_Rational for n in range(N+1))
j3=S.Rational(256)*(1-3+3**2)**3/(3**2*(1-3)**2)
checks['Legendre_3_j_exact_noninteger'] = j3==S.Rational(21952,9) and j3.q!=1
g2,g3,w,pi,j=S.symbols('g2 g3 w pi j',nonzero=True)
E4=3*w**4*g2/(4*pi**4)
E6=27*w**6*g3/(8*pi**6)
jprime=-2*pi*S.I*j*E6/E4
checks['BPT_holomorphic_form_scale_squared'] = S.simplify(jprime/w**2+9*S.I*j*g3/(pi*g2))==0
assert all(checks.values()), checks
elapsed=time.perf_counter()-timer
record={
 'result':'Work note 43; exact functional-period comparison audit',
 'utc_start':started,'elapsed_seconds':elapsed,'sympy_version':S.__version__,
 'inputs':{'basepoint':3,'order':N,'family':'y^2=4x(x-1)(x-t)',
  'companion_matrix':str(A),'initial_matrix':'identity',
  'jprime_identity':'jprime=-2*pi*i*j*E6/E4'},
 'checks':checks,'j_at_basepoint':str(j3),'normalized_projective_series':str(phiser),
 'scope':'Exact derivative, basis-change and finite Taylor certificates. Infinite Taylor rationality follows from the recurrence proved in note 43; no H1 converse is claimed.'}
path=Path(__file__)
path.with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
output='Work note 43 certificate: '+str(len(checks))+' exact checks PASS\n'+'\n'.join(k+': PASS' for k in checks)+'\n'
output+='j(3)='+str(j3)+'\nphi(t)='+str(phiser)+'+O((t-3)^13), x=t-3\nElapsed seconds: '+str(elapsed)+'\n'
path.with_suffix('.out').write_text(output)
print(output,end='')
