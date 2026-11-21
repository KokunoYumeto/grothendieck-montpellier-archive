"""Exact rational projectors onto Weil determinant spaces for Q(omega).

Run with Python 3 and SymPy. All arithmetic is rational/integer.
omega^2 + omega + 1 = 0, a = 3 + omega, Norm(a) = 7.
The polynomial acts only on H^{m}, m=4 or 8.
"""
from pathlib import Path
import json
import sympy as s

X = s.Symbol('T')

def mul(x,y):
    u,v=x; r,t=y
    return (u*r-v*t,u*t+v*r-v*t)

def power(x,n):
    r=(1,0)
    for _ in range(n):
        r=mul(r,x)
    return r

def conjugate(x):
    u,v=x
    return (u-v,-v)

def factor_for(x):
    u,v=x
    return s.Poly(X**2-(2*u-v)*X+(u*u-u*v+v*v),X,domain=s.QQ)

def compute(n):
    m=2*n
    eigen=[mul(power((3,1),j),power((2,-1),m-j)) for j in range(m+1)]
    assert len(set(eigen))==m+1
    q0=factor_for(eigen[0])
    rest=s.Poly(X-7**n,X,domain=s.QQ)
    for j in range(1,n):
        rest*=factor_for(eigen[j])
    inv=s.invert(rest,q0)
    P=inv*rest
    M=q0*rest
    assert (P*P-P).rem(M).is_zero
    assert (P-1).rem(q0).is_zero
    assert P.rem(rest).is_zero
    delta=s.ilcm(*[c.q for c in P.all_coeffs()])
    intP=s.Poly(delta*P.as_expr(),X,domain=s.ZZ)
    coeff=[int(intP.nth(j)) for j in range(m+1)]
    weighted=sum(abs(c)*7**(n*j) for j,c in enumerate(coeff))
    deg_graph=int(s.factorial(n)*2**n)
    return {
        'n':n, 'dimension':m, 'cohomology_degree':m,
        'a':'3+omega','norm_a':7,
        'eigenvalues_a_plus_b_omega':eigen,
        'q0':str(q0.as_expr()),'rest':str(rest.as_expr()),
        'inverse_rest_mod_q0':str(inv.as_expr()),
        'projector':str(P.as_expr()),
        'denominator':int(delta),
        'denominator_factorization':{str(p):int(k) for p,k in s.factorint(delta).items()},
        'integer_coefficients_ascending':coeff,
        'weighted_coefficient_sum':int(weighted),
        'graph_degree':deg_graph,
        'degree_bound_each_sign_after_clearing':int(deg_graph*weighted),
        'checks':{'distinct_eigenvalues':True,'idempotent_mod_minimal_polynomial':True,
                  'identity_on_extremes':True,'zero_on_other_summands':True}
    }

out=[compute(2),compute(4)]
dest=Path(__file__).parent/'projectors.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
for row in out:
    print(json.dumps(row,indent=2))
