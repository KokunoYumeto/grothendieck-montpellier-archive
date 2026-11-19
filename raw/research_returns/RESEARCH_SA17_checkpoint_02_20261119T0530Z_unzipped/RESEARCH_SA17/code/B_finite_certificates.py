"""Exhaustive finite checks for Part B; no sampling is used.

B_PD: a corrected characteristic-two PD witness for crystalline p-torsion.
B_Kummer: the necessary congruence obstruction over Z/4Z.
B_Delta: ranks of the finite complexes testing the literal comparison in L6.
"""
from functools import lru_cache
from itertools import product
from math import comb, factorial
from time import perf_counter
import json

started = perf_counter()
# F_2-basis of B = F_2[x,y,u,v]/(x^3,x^2y,xy^2,y^3,xu,yu,xv,yv,u^2,v^2).
monomials = [(0,0,0,0),(1,0,0,0),(0,1,0,0),(2,0,0,0),
             (1,1,0,0),(0,2,0,0),(0,0,1,0),(0,0,0,1),(0,0,1,1)]
indices = {m:i for i,m in enumerate(monomials)}
mt = [[indices.get(tuple(a+b for a,b in zip(m,n))) for n in monomials] for m in monomials]

@lru_cache(None)
def mul(a,b):
    ans = 0
    for i in range(9):
        if (a>>i)&1:
            for j in range(9):
                if (b>>j)&1 and mt[i][j] is not None:
                    ans ^= 1<<mt[i][j]
    return ans

def delta2(z):
    # a*x²+b*xy+c*y²+d*u+e*v+f*uv -> a*u+c*v+d*e*uv.
    return (((z>>3)&1)<<6) ^ (((z>>5)&1)<<7) ^ ((((z>>6)&1)*((z>>7)&1))<<8)

@lru_cache(None)
def gamma(z,n):
    if n == 0: return 1
    if n == 1: return z
    if n == 2: return delta2(z)
    if n == 3: return mul(z,delta2(z))
    if n == 4: return delta2(delta2(z))
    return 0

def power(z,n):
    v=1
    for _ in range(n): v=mul(v,z)
    return v

B=range(512)
K=[z for z in B if z & 7 == 0]
checks = {'additivity':0,'scalar':0,'product':0,'composition':0}
for z,w in product(K,repeat=2):
    for n in range(1,9):
        rhs=0
        for i in range(n+1): rhs ^= mul(gamma(z,i),gamma(w,n-i))
        assert gamma(z^w,n)==rhs,(z,w,n,'additivity')
        checks['additivity']+=1
for a,z in product(B,K):
    for n in range(1,5):
        assert gamma(mul(a,z),n)==mul(power(a,n),gamma(z,n)),(a,z,n,'scalar')
        checks['scalar']+=1
for z in K:
    for m,n in product(range(1,5),repeat=2):
        rhs=gamma(z,m+n) if comb(m+n,m)%2 else 0
        assert mul(gamma(z,m),gamma(z,n))==rhs,(z,m,n,'product')
        checks['product']+=1
        coefficient=factorial(m*n)//(factorial(m)*factorial(n)**m)
        rhs=gamma(z,m*n) if coefficient%2 else 0
        assert gamma(gamma(z,n),m)==rhs,(z,m,n,'composition')
        checks['composition']+=1
x,y,u,v=2,4,64,128
tau=mul(gamma(mul(x,x),2),gamma(mul(y,y),2)) ^ power(gamma(mul(x,y),2),2)
assert tau==256
assert delta2(u^v)==mul(u,v)==256
print(json.dumps({'certificate':'B_PD','ring_elements':len(B),'ideal_elements':len(K),
                  'checks':checks,'tau':'uv','tau_nonzero':bool(tau),
                  'uncorrected_Stacks_formula_fails_at':'delta_2(u+v)=0 instead of uv',
                  'scope':'All PD axioms; gamma_n=0 for n>=5, so the displayed finite ranges exhaust nontrivial cases.'}))

roots=[r for r in range(4) if (r*r+1)%4==0]
assert not roots
odd_values=[(r,(r*r+1)%4) for r in range(4) if r%2]
carry_checks=0
for m in [2,4,8,16,32,64]:
    for i,j,k in product(range(m),repeat=3):
        assert (i+j)//m+((i+j)%m+k)//m == (j+k)//m+(i+(j+k)%m)//m
        carry_checks+=1
print(json.dumps({'certificate':'B_Kummer','modulus':4,'square_roots_of_minus_one':roots,
                  'odd_values_of_r_squared_plus_one':odd_values,'carry_associativity_checks':carry_checks,
                  'scope':'The finite congruence obstruction and index carry identity; flatness and BT exactness are proved in the paper.'}))

# At k=F_2, M=k with F=V=p=0, both differentials are zero.
ell_dims={-1:1,0:1}
delta_dims={0:1,1:1}
tensor_dims={}
for i,a in ell_dims.items():
    for j,b in delta_dims.items():tensor_dims[i+j]=tensor_dims.get(i+j,0)+a*b
assert tensor_dims=={-1:1,0:2,1:1}
print(json.dumps({'certificate':'B_Delta','base':'F_2','group':'alpha_2 (also mu_2 for the F-complex)',
                  'co_Lie_cohomology_dimensions':ell_dims,'literal_L6_RHS_dimensions':tensor_dims,
                  'isomorphic':False,'scope':'Derived complexes over D=Z_2[F,V]/(FV-2) for the specified one-dimensional module.'}))
print(json.dumps({'total_seconds':perf_counter()-started}))
