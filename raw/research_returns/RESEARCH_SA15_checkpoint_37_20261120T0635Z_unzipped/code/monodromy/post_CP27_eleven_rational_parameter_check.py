from sympy.polys.domains import GF
from sympy import symbols
v=symbols('v');K=GF(2).frac_field(v);v=K.gens[0];r=v*v+v;t=v*v
alpha=t/r**2; beta=alpha+1
gamma=(r**6+r**5+r+1)*t/r**4+(r**3+r+1)/r**2
for name,q in [('alpha',alpha),('beta',beta),('gamma',gamma),('P10',r**10+r**8+r**7+r**5+r**3+r+1)]:
 print(name, q)
 print('numerator factors',q.numer.factor_list())
 print('denominator factors',q.denom.factor_list())
