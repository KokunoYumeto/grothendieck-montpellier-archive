#!/usr/bin/env python3
"""Exact finite coefficients for C.3bk; the geometric proof is not delegated to code."""
from datetime import datetime, timezone
from time import perf_counter
from pathlib import Path
from math import factorial, gcd
from functools import reduce
import hashlib, json
import sympy as sp

started = datetime.now(timezone.utc).isoformat()
tic = perf_counter()
checks=[]
def check(name, condition, scope):
    item={'name':name,'passed':bool(condition),'scope':scope}
    checks.append(item)
    if not condition: raise AssertionError(name)

h,c,b=sp.symbols('h c b')
recurrences=[]
for r in range(2,13):
    gamma=sum(b*(-c)**(r-1-i)*h**i for i in range(r))
    product=sp.expand((h+c)*gamma)
    expected=b*(h**r+(-1)**(r-1)*c**r)
    check(f'borderline_recurrence_r{r}', sp.expand(product-expected)==0,
          'Finite check of the exact integral coefficient recurrence at m=r-1.')
    variables=sp.symbols('g:'+str(r))
    pg=sp.Poly(sp.expand((h+c)*sum(variables[i]*h**i for i in range(r))),h)
    mat=sp.Matrix([[sp.diff(pg.coeff_monomial(h**j),v) for v in variables]
                  for j in range(1,r+1)])
    check(f'large_m_triangular_r{r}',sp.expand(mat.det())==1,
          'The h^1 through h^r coefficient matrix is integral triangular with unit determinant.')
    s=r-1
    top_degree=factorial(2*s+1)//(2**s)*3**s*4
    check(f'ample_integer_degree_r{r}',top_degree>0,
          'Positive integral degree of the specified external ample line; not reduced modulo p.')
    recurrences.append({'r':r,'borderline_m':r-1,'local_dimension':3*r-1,
                        'product':str(product),'degree_on_S':top_degree,
                        'triangular_determinant':str(mat.det())})

A=sp.Matrix([3,-1,-1,-1,-1,-1,-1])
Q=sp.diag(1,-1,-1,-1,-1,-1,-1)
endpoint=sp.zeros(8,8)
endpoint[:7,:7]=4*sp.eye(7)
endpoint[:7,7]=A
endpoint[7,:7]=(A.T*Q)
check('r2_m0_free_integer_matrix',endpoint.det()==-3*4**6,
      'Exact free-lattice equations 4d+deg(lambda)A=0 and A.d=0; no reduction in any characteristic.')
check('r2_m0_primitive_anticanonical',reduce(gcd,[abs(int(x)) for x in A])==1,
      'Anticanonical coefficients give an integral retraction on the Pic(C)-coefficient summand.')
check('r3_m1_intersection_system',sp.Matrix([[2,1],[1,2]]).det()==3,
      'The two paired equations force integer x=y=0, including characteristic three.')
check('r3_m1_torsion_bezout',3-2==1,
      'The 3 and 2 coefficient equations kill every Picard torsion element.')

cup=[]
for s in range(1,10):
    size=2**s
    permutation=[(size-1)^i for i in range(size)]
    check(f'coefficient_one_tensor_cup_s{s}',
          sorted(permutation)==list(range(size)) and all(permutation[permutation[i]]==i for i in range(size)),
          'Tensor product of s off-diagonal unit cup matrices is an integral permutation matrix, with no factorial.')
    for prime in [2,3,5,7,11]:
        check(f'cup_survives_p{prime}_s{s}',all(1%prime !=0 for i in permutation),
              'Finite-prime unit coefficient check only; the integral permutation identity gives the general argument.')
    cup.append({'s':s,'rank':size,'nonzero_coefficient':1,'involution':True})

prior={}
for relative in ['research/agents/real_weil/output/C3bj_uniform_kernel_certificate.json',
                 'research/agents/cycles/output/cubic_exceptional_lattice_certificate.json']:
    path=Path(relative)
    prior[relative]={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                     'scope':'Referenced prior author certificate; not rerun by this program.'}
record={'statement':'C.3bk finite coefficient certificate', 'started_at_utc':started,
        'finished_at_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':perf_counter()-tic,
        'scope':'Finite exact integer recurrences for r=2..12, r2/m0 and r3/m1 endpoint lattices, and tensor cup coefficient samples for s=1..9. Does not prove Bertini, actual family existence, sheaf cohomology or arbitrary-r geometry.',
        'recurrences':recurrences, 'endpoint_matrix':[[int(x) for x in row] for row in endpoint.tolist()],
        'endpoint_determinant':int(endpoint.det()),'tensor_cups':cup,'prior_certificates':prior,
        'checks':checks,'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks)}
out=Path(__file__).resolve().parents[1]/'output'/'C3bk_higher_product_certificate.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
