"""R042/R043 independent rational moment and endpoint reconstruction."""
from pathlib import Path
import json
import sympy as s
a,m,n=s.symbols('a m n',positive=True,integer=True)
F1,F2=s.symbols('F1 F2');k=m+1;l=a-k
# Original equality-pattern expectation table divided by k!.
X=Y=F2+(l+1)*F1
Z=l*F1
phi1=s.factor((a*X-k*Y-Z)/a**2)
inside=(1-k/a)*(F1+F2)
phi2=s.factor((inside-phi1)/a)
E=s.Matrix([[s.factor(s.diff(p,z)) for z in (F1,F2)] for p in (phi1,phi2)])
expected=s.Matrix([[l*l/a**2,l/a**2],[k*l/a**3,(a-1)*l/a**3]])
assert all(s.factor(v)==0 for v in E-expected)
det=s.factor(E.det());assert s.factor(det-l*l*(l-1)/a**4)==0
u=n*(n-1)/((n-2)*(n-3));H=s.Matrix([[1,0],[k*u,-6*u]])
endpoint=s.factor(((E*H)*s.Matrix([1,(n-1)/n]))[0].subs({a:m+2,n:m+2},simultaneous=True))
assert s.factor(endpoint-(m*m-3*m-2)/((m+2)*m*(m-1)))==0
cubic=s.factor(a*phi2-(a-1)*phi1)
assert s.factor(cubic+l*(l-1)*F1/a)==0

# Reconstruct R041's moment table, then take the actual cubic combinations.
Q,R,T=s.symbols('Q R T')
UI=Q+R;TI2=R+2*T-Q;UA=R+(l+1)*Q;TA2=R+2*T+(l-1)*Q;TATI=TI2
A=UA-TA2/a
B=UI-2*TATI/a+k*TA2/a**2
Cp=(TI2-UI)/2-(k-1)*TATI/a+k*(k-1)*TA2/(2*a**2)
P1=A/a;P2=(B-P1)/a;P3=(Cp+P1)/a
# Top degree in a fixed varying original row, before P1/P2/P3 conversion.
beta1=(a-1)/a**2
beta2=s.factor((1-2/a+k/a**2-beta1)/a)
beta3=s.factor((-m/a+m*(m+1)/(2*a*a)+beta1)/a)
assert s.factor(beta2-(a*a-3*a+m+2)/a**3)==0
assert s.factor(beta3+(m-1)*(2*a-m-2)/(2*a**3))==0
q2=s.factor((beta1*P2-beta2*P1).subs(m,2))
q3=s.factor((beta1*P3-beta3*P1).subs(m,2))
rows=s.Matrix([[s.factor(s.diff(p,z)) for z in (Q,R,T)] for p in (q2,q3)])
wanted=s.Matrix([[-(a-3)**2/a**3,0,-2*(a-3)/a**4],[(a-3)/a**3,0,(a-3)*(a-2)/a**4]])
assert all(s.factor(v)==0 for v in rows-wanted)
fall=a*(a-1)*(a-2)
scalars=[s.factor(fall*p.subs({Q:-s.Rational(1,216),R:0,T:-s.Rational(1,54)})) for p in (q2,q3)]
assert s.factor(scalars[0]-(a-3)*(a-2)*(a-1)*(a*a-3*a+8)/(216*a**3))==0
assert s.factor(scalars[1]+(a-3)*(a-2)*(a-1)*(5*a-8)/(216*a**3))==0
out={'statements':['R042','R043'],'status':'PASS','method':'independent equality-pattern and raw top-row coefficient reconstruction; exact rational arithmetic; no source implementation imports',
     'mixed_matrix_entries':4,'mixed_determinant':str(det),'mixed_unit_endpoint':str(endpoint),
     'mixed_cubic_expectation':str(cubic),'even_tail_beta':[str(beta1),str(beta2),str(beta3)],
     'even_tail_cubic_coefficient_rows':[[str(v) for v in rows.row(i)] for i in range(2)],
     'even_tail_two_cubic_scalars':[str(z) for z in scalars]}
(Path(__file__).resolve().parent/'MIXED_WIDTH_FOUR_SYMBOLIC_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
