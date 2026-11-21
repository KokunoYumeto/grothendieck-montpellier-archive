import sympy as s

D=s.symbols('D')
a=D-2; d=D**2; A=D**2-8*D+8
x=(D-2)**2; y=4*(D-1)
assert s.expand(x+y-d)==0 and s.expand(x-y-A)==0
R1=s.Matrix([[d,D*a,D*a,2*a*a],[0,0,0,-D*a],[0,0,0,-D*a],[0,0,0,d]])
R2=s.Matrix([[d,0,0,0],[-D*a,0,0,0],[-D*a,0,0,0],[2*a*a,D*a,D*a,d]])
B=s.Matrix.hstack(s.Matrix([d,-D*a,-D*a,d]),s.Matrix([0,1,-1,0]),
                  s.Matrix([A,-D*a,-D*a,d]),s.Matrix([d,-D*a,-D*a,A]))
S1=s.Matrix([[x,y,0,0],[x,y,0,0],[0,0,y,x],[0,0,y,x]])
S2=s.Matrix([[x,0,y,0],[0,y,0,x],[x,0,y,0],[0,y,0,x]])
C=s.Matrix.hstack(s.ones(4,1),s.Matrix([y,-x,-x,y]),
                  s.Matrix([1,1,-1,-1]),s.Matrix([1,-1,1,-1]))
N1=s.diag(d,0,s.Matrix([[d,A],[0,0]]))
N2=s.diag(d,0,s.Matrix([[0,0],[A,d]]))
zero=lambda M: all(s.factor(z)==0 for z in M)
assert zero(S1*C-C*N1) and zero(S2*C-C*N2)
assert zero(R1*B-B*N1) and zero(R2*B-B*N2)
assert s.factor(C.det()+8*d)==0
T=(B*C.inv()).applyfunc(s.factor)
assert zero(R1*T-T*S1) and zero(R2*T-T*S2)
assert s.factor(T.det()+16*(D-2)*(D-1)**2/D)==0
E=s.Rational(1,2)*s.Matrix([[1,0,0,-1],[0,1,-1,0],[0,-1,1,0],[-1,0,0,1]])
assert zero(E*C-C*s.diag(0,0,1,1))
assert zero(E*E-E) and zero(E*S1-S1*E) and zero(E*S2-S2*E)
assert s.factor(s.trace(E*S1*S2)-A*A)==0
assert zero(S1*S1-d*S1) and zero(S2*S2-d*S2)
v=s.symbols('v',nonzero=True)
Dv=(v+v**-1)**2
assert s.expand(x.subs(D,Dv)-(v**4+2+v**-4))==0
assert s.expand(y.subs(D,Dv)-(4*v*v+4+4*v**-2))==0
assert s.factor(T.det().subs(D,4))!=0
print('PASS: named actual R-to-S intertwining, detC=-8D^2, regular T, projector, inserted trace and quadratics.')
print('PASS: x=v^4+2+v^-4; y=4v^2+4+4v^-2; both effective and even.')
print('det(T)=',s.factor(T.det()))
print('E=',E)

