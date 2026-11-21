"""R041 independent moment-table reconstruction of C and finite endpoint blocks."""
from pathlib import Path
import json
import sympy as s
a,m,n=s.symbols('a m n',positive=True,integer=True)
Q,R,T=s.symbols('Q R T')
k=m+1;l=a-k
UI=Q+R
TI2=R+2*T-Q
UA=R+(l+1)*Q
TA2=R+2*T+(l-1)*Q
TATI=TI2
A=UA-TA2/a
B=UI-2*TATI/a+k*TA2/a**2
Cp=(TI2-UI)/2-(k-1)*TATI/a+k*(k-1)*TA2/(2*a**2)
P1=A/a
P2=(B-P1)/a
P3=(Cp+P1)/a
actual=s.Matrix([[s.factor(s.diff(p,z)) for z in (Q,R,T)] for p in (P1,P2,P3)])
expected=s.Matrix([
[(a*a-a*m-a+m+2)/a**2,(a-1)/a**2,-2/a**2],
[(m+2)*(2*a-m-2)/a**3,(a*a-3*a+m+2)/a**3,-2*(2*a-m-2)/a**3],
[(m-1)*(m+2)*(a-m-2)/(2*a**3),-(m-1)*(2*a-m-2)/(2*a**3),(a*a-2*a*m+m*m+m-2)/a**3]])
assert all(s.factor(v)==0 for v in actual-expected)
det=s.factor(actual.det())
assert s.factor(det-(a-m-2)*(a-m-1)**2/a**5)==0
minor=s.factor(actual[:2,:2].det().subs(a,m+2))
assert s.factor(minor-(m-1)/(m+2)**3)==0
u=n*(n-1)/((n-2)*(n-3));v=n*(n-1)/(n-2)**2
D=s.Matrix([[1,0,0],[(m+2)*u,-6*u,0],[0,0,-4*v]])
M=actual*D
finite1=s.Matrix([1,(n-1)/n,(2-n)/(2*n)])
finite2=s.Matrix([[1,0],[0,1],[s.Rational(1,2),-1]])
end1=s.factor((M*finite1)[0].subs({a:m+1,n:m+1},simultaneous=True))
assert s.factor(end1-(m-2)/(m-1))==0
end2=s.factor((M[:2,:]*finite2).det().subs({a:m+2,n:m+2},simultaneous=True))
assert s.factor(end2+2*(m+1)*(3*m+2)/(m**3*(m+2)))==0
end12=s.factor((M*finite2)[0,1].subs({a:m+1,n:m+2},simultaneous=True))
assert s.factor(end12+2*(m+2)**2*(3*m-2)/(m*m*(m-1)*(m+1)))==0
out={'statement':'R041 independent exact moment-matrix and endpoint reconstruction','status':'PASS',
     'matrix_entries':9,'moment_matrix_determinant':str(det),'finite_row_independence_minor':str(minor),
     'one_dimensional_square':str(end1),'two_dimensional_square_determinant':str(end2),
     'mixed_endpoint_coefficient':str(end12),'method':'independent formal expectation table; symbolic rational arithmetic; no source implementation imported'}
path=Path(__file__).resolve().parent/'FOUR_EVEN_TAIL_SYMBOLIC_RECEIPT.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
