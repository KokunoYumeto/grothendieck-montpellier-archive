"""Universal characteristic-two identities for the genus-two five-self-isogeny.
The geometric divisor/reduced-representative conclusions are proved in TeX.
"""
from pathlib import Path
import sympy as s
import json,time,datetime
start=time.perf_counter()
z,p,beta,X,x,delta,ellvar,mu=s.symbols('z p beta X x delta ell mu')
variables=(beta,z,p,X,x,delta,ellvar,mu)
def red(f):
    q=s.Poly(f,*variables,modulus=2).as_expr()
    q=s.rem(q,beta**2+beta+z+1,beta,domain=s.GF(2).poly_ring(z,p,X,x,delta,ellvar,mu))
    return s.Poly(q,*variables,modulus=2).as_expr()
a=z**2;b=z**2+z+1
F=lambda t:a*t**5+b*t**3
q=lambda t:z*t**2+(z+1)*t+beta
c1=a*p**4+b*p**2
c2=c1+q(p)
ell=a*p+c2**2+a
u=a*X**2+ell*X+b+ell
checks={
'automorphism_curve':red(q(x)**2+q(x)+F(x+1)+F(x)),
'order_four_square':red(q(x+1)+q(x)+1),
'first_derivative':red(s.diff(F(x),x).subs(x,p)-c1),
'interpolation_at_shift':red(c1+c2-q(p)),
'residual_quadratic_factorization':red((c1*X+c2*X**2)**2+(c1*X+c2*X**2)+F(p+X)+F(p)-X**2*(X+1)*u),
'global_residual_coefficients':red(u.subs(X,x+p)-(a*x**2+ell*x+a*p**2+ell*p+b+ell)),
'equal_residual_constant_difference':red((a*(p+delta)**2+ellvar*(p+delta)+b+ellvar)-(a*p**2+ellvar*p+b+ellvar)-delta*(a*delta+ellvar)),
'covering_constant_term':red(((z**2+z+1)**5+mu**5*z**6).subs(z,0)-1),
'covering_degree_ten_leading':red(s.Poly((z**2+z+1)**5+mu**5*z**6,z,domain=s.GF(2).poly_ring(mu)).LC()-1)
}
assert all(v==0 for v in checks.values())
result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'identities':{k:str(v) for k,v in checks.items()},'relations':['beta^2+beta+z+1=0','characteristic=2','z != 0 for geometry'],'c1':str(red(c1)),'c2':str(red(c2)),'ell':str(red(ell)),'residual_quadratic':str(red(u)),'scope':'Nine exact universal polynomial identities. They do not replace the divisor, reduced-representative, normalization and isogeny arguments.'}
out=Path(__file__).resolve().parent.parent/'outputs/nonordinary_uniform_five_self_isogeny_identities.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
