from pathlib import Path
import sympy as s

q,u=s.symbols('q u', nonzero=True)
D=q+2+q**-1
c1=(q**6+2*q**5+3*q**4+4*q**3+3*q**2+2*q+1)/q**3
c2=(q**4+q**3+4*q**2+q+1)/q**2
b1=-(q*q+1)**2/q**2
b2=(q+1)**2/q
for lhs,rhs in [(b2,D),(-b1,(D-2)**2),(c1,D*(D-2)**2),(c2,D+(D-2)**2)]:
    assert s.expand(lhs-rhs)==0
c=-(q*q+q+1)*(q-1)**2/q**2
assert s.expand(c-(-q*q+q+q**-1-q**-2))==0
assert s.expand(c.subs(q,u*u)+(u-u**-1)**2*(u*u+1+u**-2))==0
assert s.expand(-c.subs(q,-u)-(u*u+u+u**-1+u**-2))==0
assert s.expand((1+q)**2/q-(q+2+q**-1))==0
# Pure weight one: the line of point weight e occurs in degree e-1.
coeff={2:-1,1:1,-1:1,-2:-1}
for e,ce in coeff.items():
    i=e-1
    assert (1 if i%2==0 else -1)==ce
print('PASS: four presentation identities, both multiplication coefficient expansions, isolated pure-weight-one signs.')
print('h(q)=4(q^(1/2)+q^(-1/2)); joint integrality and purity deductions are proved in the report.')

