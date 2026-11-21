"""Independent symbolic identities for A31, without importing the F4 checker."""
from pathlib import Path
import json,hashlib
import sympy as s

u,x,t,y=s.symbols('u x t y')
def reduce_mod_u(expr,*variables):
    expr=s.Poly(s.expand(expr),u,*variables,modulus=2).as_expr()
    return s.reduced(expr,[u*u+u+1],u,*variables,modulus=2)[1]

f=x**5+x**4+u*x**3+u**2*x**2+u*x+u
a=x;b=x+u;h=x*x
norm=a*a+a*b*h+b*b*f
norm_remainder=reduce_mod_u(norm-(x+1)**7,x)
assert norm_remainder==0

# Clear t^5 after substituting X=u/t and Y=alpha*y+beta;
# the y terms cancel before using y^2+y=u*t^3+t+u/t.
alpha=u**2/t**2;beta=1/t**2+u**2;X=u/t
g=u*t**3+t+u/t
linear_y=reduce_mod_u(s.cancel(t**4*(alpha**2-X**2*alpha)))
assert linear_y==0
delta=s.cancel(t**5*(alpha**2*g+beta**2+X**2*beta-f.subs(x,X)))
assert s.denom(delta)==1
iso_remainder=reduce_mod_u(delta,t)
assert iso_remainder==0

# The two values of y in the polynomial model over X=1.
curve_at_R=reduce_mod_u(u*u+u+f.subs(x,1))
value_R=reduce_mod_u((1+u)*u+1)
value_conjugate=reduce_mod_u((1+u)*(u+1)+1)
assert curve_at_R==0 and value_R==0 and reduce_mod_u(value_conjugate-u*u)==0
assert reduce_mod_u(s.diff(f,x).subs(x,0))==u

result=dict(result='PASS',backend='SymPy polynomial reduction over F2 in the formal coefficient u, modulo u^2+u+1',
 independence='No imports from the row checker; symbolic polynomial remainders replace encoded F4 bit operations.',
 norm_remainder=str(norm_remainder),cleared_coordinate_remainder=str(iso_remainder),
 residual_y_coefficient=str(linear_y),curve_at_R=str(curve_at_R),F_R=str(value_R),F_iota_R=str(value_conjugate),
 scope='Finite polynomial identities only. Divisors, exact torsion order, Frobenius twist and covering implications use the written proof.',
 source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
