"""Universal characteristic-two identities for the direct trigonal exclusion.

The proof of the geometric implication is in the companion candidate. This
program checks polynomial identities over F2, not a finite parameter sample.
"""
from pathlib import Path
import datetime,json,time,hashlib
import sympy as sp
started=time.perf_counter()
x,z,u,a,b,c,t,e=sp.symbols('x z u a b c t e')
variables=(x,z,u,a,b,c,t,e)
def zero(expr):
    poly=sp.Poly(sp.expand(expr),*variables,modulus=2)
    assert poly.is_zero, str(poly)
    return True

ysub=z*x**3+1+(c+t)*x+e*x**2
f=u*x**5+a*x**3+(e+c**2+c*t)*x**2+c*x
cubic=z**2*x**3+u*x**2+(e**2+t*z)*x+z+a+t*e
checks={}
checks['elimination_after_cancelling_x_cubed']=zero(ysub**2+(1+t*x)*ysub+f+x**3*cubic)

D=e**4+u*a+u*t*e
A=t*e**2+u
P=t*z**3+e**2*z**2+u**2
R=t**2*z**2+u*z+D
R1=t**2*D+u*A
R0=u**2*t**3+A*D
R2=A**2+u*t**5
S=u**2+a**2*t**4+u*t**5+a*t**7+e*t**8
checks['denominator_cleared_cubic_quadratic_division']=zero(t**3*P+(t**2*z+A)*R+R1*z+R0)
checks['remainder_relations_imply_second_constraint']=zero(t**2*R0+A*R1+u*R2)
checks['universal_singularity_identity']=zero(u**2*S+R1**2+u*t**5*R1+e**4*t**2*R2)

fp=u*x**4+a*x**2+c
singular_at_h_root=sp.cancel(t**8*(fp.subs(x,1/t)**2+t**2*f.subs(x,1/t)))
checks['singularity_test_at_h_root']=zero(singular_at_h_root+S)
checks['constant_h_has_at_most_one_extra_value']=zero(P.subs(t,0)+(e*z+u)**2)

# A triple root of the displayed cubic has x-coordinate u/z^2.
# These are the two denominator-cleared coefficient conditions.
root=u/z**2
triple=sp.expand(z**2*(x+root)**3)
coeffx=sp.expand(cubic-triple).coeff(x,1)
checks['triple_root_linear_coefficient']=zero(sp.cancel(z**2*coeffx)+P)
const=sp.expand(cubic-triple).coeff(x,0)
Q=z**5+(a+t*e)*z**4+u**3
checks['triple_root_constant_coefficient']=zero(sp.cancel(z**4*const)+Q)
checks['P_and_Q_imply_R']=zero(P**2+u*Q+z**4*R)

result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-started,'ring':'F2[x,z,u,a,b,c,t,e]',
        'checks':checks,'count':len(checks),
        'geometric_localization':'The t!=0 branch uses u and t invertible; the separate t=0 branch is also checked. No numerical parameter is substituted.',
        'scope':'Universal polynomial identities only. Riemann--Roch, coordinate normalization, ramification and smoothness implications are proved separately in the candidate.',
        'singularity_identity':'u^2*S = R1^2 + u*t^5*R1 + e^4*t^2*R2 over F2'}
w=Path(__file__).resolve().parents[1]
out=w/'outputs/nonordinary_trigonal_direct_certificate.json'
assert not out.exists()
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
