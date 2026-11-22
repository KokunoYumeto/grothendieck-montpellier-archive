#!/usr/bin/env python3
"""Universal characteristic-two contact identities; no global smoothness claim."""
from pathlib import Path
from time import perf_counter
from itertools import product,permutations
import json
import sympy as sp
started=perf_counter()
a,b,c,d,F,T,U,v=sp.symbols('a b c d F T U v')
variables=(b,d,a,c,F,T,U,v)
gb=sp.groebner([b*b+b+a**3,d*d+d+c**3],*variables,modulus=2)
def red(f):return gb.reduce(sp.expand(f))[1]
def zero(f):assert red(f)==0,red(f)
C=T+a;E=U+c*c;D=v+U*c+d*d+F*a*a
B=T*c*c+E*a;A=T*d*d+D*a+F*b
S=sp.Matrix([[A,B,C],[D,E,1],[F,0,0]])
J=sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
QH=sum(S[i,j]**2*S[2-i,2-j] for i in range(3) for j in range(3))
expected=v*v+v+U**3+U*(c**4+c)+F*F*(T+a**4+a)+F*T*T
zero(QH-expected);zero(S.det()-F*T*U)
p=sp.Matrix([1,a,b]);q=sp.Matrix([1,c,d]);dp=sp.Matrix([0,1,a*a]);dq=sp.Matrix([0,1,c*c])
zero((p.T*S*q)[0]);zero((dp.T*S*q)[0]-v);zero((p.T*S*dq)[0])
R=J*S.applyfunc(lambda x:x*x)*J
UN=S*R.T*S
zero(UN[2,2]-F)
zero((p.T*UN*q)[0]-T*v*(v*v+F*F*(a**4+a)))
# Verify the universal inverse-Hessian identity before any contact specialization.
x=sp.symbols('x0:9');X=sp.Matrix(3,3,x);Dx=X.det();Qx=sum(X[i,j]**2*X[2-i,2-j] for i in range(3) for j in range(3))
Y=X*(J*X.applyfunc(lambda z:z*z)*J).T*X
onefactor=[sp.Matrix([[0,1,0],[0,0,1],[0,0,0]]),sp.Matrix([[1,0,0],[0,0,0],[0,0,1]]),sp.Matrix([[0,0,0],[1,0,0],[0,1,0]])]
M=sp.zeros(9,9)
for i,j in product(range(3),repeat=2):M+=x[3*i+j]*sp.kronecker_product(onefactor[i],onefactor[j])
vec=sp.Matrix(list(Y));res=M*vec-Dx*sp.Matrix([z*z for z in x])
quotients=[]
for f in res:
 quo,rem=sp.div(sp.Poly(sp.expand(f),*x,modulus=2),sp.Poly(Qx,*x,modulus=2))
 assert rem.is_zero
 quotients.append(str(quo.as_expr()))
# If eta difference vanished on the AS family, v would have the displayed
# rational expression; its square equation has nonzero U^6 coefficient.
vforced=F/T+U**3+U*(c**4+c)+F*F*T+F*T*T
obstruction=sp.Poly(sp.expand(T*T*(vforced*vforced+F*F*(a**4+a)+F/T)),U,domain=sp.GF(2).frac_field(a,c,F,T))
assert obstruction.degree()==6 and obstruction.LC()==T*T
# Exact rational elliptic addition at O through order two.  In the Y=1
# chart z+z^2=t^3; t^3+t^6+t^12 suffices for the retained coefficients.
t=sp.symbols('t');z=t**3+t**6+t**12;den=t+c*z
numx=z*(1+d*z)**2+t*den**2+c*z*den**2
xc=c+t+c*c*t*t;yc=d+c*c*t+c*t*t
numy=(1+d*z)*numx+den**3+(1+d*z)*t*den**2+z*den**3
for expression,bound in ((numx-xc*z*den**2,8),(numy-yc*z*den**3,9)):
 for exponent in range(bound):
  zero(sp.expand(expression).coeff(t,exponent))
zero(sp.expand(T*(d*d+c*c*xc+yc)).coeff(t,0))
zero(sp.expand(T*(d*d+c*c*xc+yc)).coeff(t,1))
zero(sp.expand(T*(d*d+c*c*xc+yc)).coeff(t,2)-T*(c**4+c))
out={'status':'PASS','scope':'Universal local containment, contact gradient, determinant, Cartier-lift and eta-difference identities only; source global smoothness and other norm collisions are not proved.',
 'parameters':[str(z) for z in variables],'coefficient_matrix':[[str(z) for z in row] for row in S.tolist()],
 'source_Hasse_cubic':str(expected),'determinant':'F*T*U','gradient_at_origin':[1,0],'gradient_at_translation':['v',0],
 'Cartier_lift_numerator':'S*(J*S^[2]*J)^t*S','universal_inverse_Hessian_remainders':0,
 'eta_difference':'(F+T*(v^2+F^2*(a^4+a)))/(F*T*U)',
 'eta_vanishing_obstruction_U_degree':6,'eta_vanishing_obstruction_leading_coefficient':'T^2',
 'simple_contact_coefficient':'T*(c^4+c), in the origin local parameter on the second elliptic factor',
 'global_smoothness_checked':False,'other_kernel_collisions_checked':False,'elapsed_seconds':perf_counter()-started}
pth=Path(__file__).resolve().parent.parent/'outputs'/'supersingular_uniform_contact_identities.json'
pth.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
