"""Independent exact derivation of the reversible rows and triple coefficients."""
from pathlib import Path
import datetime,json,time
from sympy import symbols
from sympy.polys.domains import GF
from sympy.polys.rings import ring
started=time.perf_counter(); checks=[]
r_symbol=symbols('r'); base=GF(2).frac_field(r_symbol); r=base.gens[0]
R,w,beta,t,p,L,C,B3=ring('w,beta,t,p,L,C,B3',base)
const=R.ground_new; z=const((r*r+1)/r**3); D=const(r*r)
a=z*z; b=a+z+1; gt=t*t+t+D
ft=(a*t**5+b*t**3).div([gt])[1]
relations=[w*w+w+ft,beta*beta+beta+z+1,gt]
red=lambda q:q.div(relations)[1]
def check(name,q):
    assert not red(q),(name,str(red(q)))
    checks.append(name)
G=z*p*p+(z+1)*p+beta
H=z*(t+const(r))*p*p+(z*t*t+t+const(1/r**2))*p+w
cg=z*D+t; d1=a*p**4+b*p*p
Z=red(H+t*t*G+D*d1+t*cg)
E=red(t*G+H+(t+1)*cg)
B2=(L+C)*G+C*d1+B3
Eh=(L*t+C)*H+C*d1*t+B2*t*t+B3*t**3
Egh=(L*(t+1)+C)*(G+H+cg)+C*d1*(t+1)+B2*(t+1)**2+B3*(t+1)**3
U=D*B3+L*E+C*cg; V=C*Z+L*D*cg
check('arbitrary_section_h_value_row',Eh+t*U+V)
check('arbitrary_section_gh_value_row',Egh+(t+1)*U+V)
# The following independent generic calculation does not impose the Q8 relations.
S,Z,cg,a4,a2,a1,L,j,k,B0,u0=ring('Z,cg,a4,a2,a1,L,j,k,B0,u0',GF(2))
A=a4*L**3+a2*L+a1; Q=a4*L*L+a2
Cubic=Z**3+j*Z*Z+k
Bscaled=B0*cg**4+(cg**4+Q*cg*cg)*Z+a4*Z*Z
Pscaled=Bscaled**2+L*A*Bscaled*cg**4+u0*A*A*cg**8+Z*A*A*cg**6
remainder=Pscaled.div([Cubic])[1]
def coefficient(poly,power):
    return S.from_dict({(0,)+e[1:]:v for e,v in poly.items() if e[0]==power})
P2=cg**4*(cg*cg+Q)**2+a4*a4*j*j+L*A*a4*cg**4
P1=a4*a4*k+cg**6*A*(L*cg*cg+a1)
assert coefficient(remainder,2)==P2
assert coefficient(remainder,1)==P1
checks.extend(['generic_Z_squared_coefficient_is_P2','generic_Z_coefficient_is_P1'])
# A quadratic divisor of the cubic has the stated necessary coefficient identity.
T,Z,h,j,k=ring('Z,h,j,k',GF(2))
quad=Z*Z+h*Z+h*(j+h)
division=(Z**3+j*Z*Z+k).div([quad])[1]
assert division==k+h*(h+j)**2
checks.append('quadratic_cubic_divisibility_obstruction')
record={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-started,'checks':checks,
        'scope':'Universal symbolic rederivation of five proof identities, not a finite-field sample or a stand-alone geometric theorem.'}
out=Path(__file__).resolve().parents[1]/'outputs/root_uniform_seven_symbolic_rederivation.json'
assert not out.exists(); out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
