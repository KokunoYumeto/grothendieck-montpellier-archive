"""Exact finite checks accompanying B-RD26/27.

This checks algebraic identities and integer-range equivalences.  The formal
deformation ring, convergence, equivariant chart, and descent are proved in
the TeX and are not claimed to be computationally instantiated here.
"""
from pathlib import Path
import json
import time
import sympy as sp

started = time.perf_counter()
z, w, t, u, c = sp.symbols('z w t u c')
den = sum((w+j)**2 for j in range(3))
num = sum((w+j)**2*((z+j)-(w+j)) for j in range(3))
assert sp.expand(den) == 3*w*w+6*w+5
assert sp.expand(num-(z-w)*den) == 0
norm = sp.prod(w+j for j in range(3))
assert sp.expand(norm-(w**3-w)) == 3*w*w+3*w
assert sp.Poly(den+1, w, modulus=3).is_zero
assert sp.Poly(norm-(w**3-w), w, modulus=3).is_zero

equivariance_checks = 0
for a in range(1, 45):
    f = w+c*(w**3-w)**a
    assert sp.Poly(f.subs(w,w+1)-f-1, w,c,modulus=3).is_zero
    equivariance_checks += 1
    if a % 2:
        assert sp.expand(f.subs(w,-w)+f) == 0
        equivariance_checks += 1

log = t-u*t**3/sp.Integer(6)
candidate = 3*t+4*u*t**3
assert sp.expand(log.subs(t,candidate)-3*log).coeff(t,3) == 0
x = sp.symbols('x')
assert sp.discriminant(x**3+u*x*x-x,x) == u*u+4
psi3=3*x**4+4*u*x**3-6*x*x-1
psi4_over_psi2=2*x**6+4*u*x**5-10*x**4-10*x*x-4*u*x+2
psi2_squared=4*(x**3+u*x*x-x)
phi3=sp.expand(x*psi3**2-psi4_over_psi2*psi2_squared)
assert sp.Poly(phi3.subs(u,0)-x**9,x,modulus=3).is_zero
assert sp.Poly(psi3.subs(u,0)+1,x,modulus=3).is_zero
f=x**3-x
y_tripling_identity=(f*f-1)*(x-x**9)-f+f**5
assert sp.Poly(y_tripling_identity,x,modulus=3).is_zero
# Over F9=F3[i]/(i^2+1), i is nonzero and i+/-1 cannot vanish.
i=sp.symbols('i')
for sign in (-1,1):
    assert sp.gcd(sp.Poly(i+sign,i,modulus=3),
                  sp.Poly(i*i+1,i,modulus=3)).degree()==0

def vp3(a):
    result = 0
    while a % 3 == 0:
        a //= 3
        result += 1
    return result

def weighted_degree(a,n):
    return 2*3**(n-1)*(a+3**n+sum(2*3**(n-j-1)*min(a,3**(2*j))
                                    for j in range(1,n)))

def admissible(e,n,m):
    s=vp3(e//2)
    return s >= n-1 and m*e >= 8*3**max(2*n-2,4*n-4-s)

def construct(e,n,m):
    s=vp3(e//2)
    r=max(0,2*n-2-s)
    assert r <= n-1
    while r<n-1 and m*e >= 8*3**(2*n+r-1):
        r += 1
    denom=2*3**(2*n-r-2)
    assert m*e % denom == 0
    a=m*e//denom-3**(2*r+1)
    assert a % 3 == 0 and a>=3**(2*r)
    assert r == n-1 or a<3**(2*r+2)
    assert weighted_degree(a,n) == m*e
    primitive_weights = [a,1]+[min(a,3**(2*j)) for j in range(1,n)]
    assert max(primitive_weights)<m*e
    if m==6:
        assert a%2 == 1
    if m==12:
        assert a%4 == 1 and (a//3)%2 == 1
    assert 6*3**(2*n-2)>4
    assert weighted_degree(a,n)>6*3**(2*n-2)
    return {"A":a,"B":1,"region":r,"good_absolute_index":m*e}

constructed=0
index_comparisons=0
for e in range(2,50002,2):
    for n in range(1,9):
        for m in (3,6,12):
            if admissible(e,n,m):
                construct(e,n,m)
                constructed+=1
    s=vp3(e//2)
    ell=0
    while 3**(ell+1)<=e//2:
        ell+=1
    predicted=1+min(s,(ell+1)//2,(ell+s+1)//4)
    actual=max(n for n in range(1,9) if admissible(e,n,12))
    assert predicted==actual
    index_comparisons+=1

samples={}
for e,n,m in ((2,1,12),(4,1,3),(24,2,12),(30,2,12),
              (42,2,12),(48,2,12),(216,3,12),(270,3,12),
              (378,3,12),(432,3,12),(504,3,12),(1944,4,12)):
    assert admissible(e,n,m)
    samples[f"e{e}_n{n}_m{m}"]=construct(e,n,m)

result={
    "status":"PASS",
    "arithmetic":"exact symbolic polynomial and integer arithmetic",
    "scope":"identities and ranges only; formal construction proved separately",
    "trace_denominator":str(sp.expand(den)),
    "trace_numerator_identity":"numerator = (z_x-z_y)*denominator",
    "special_norm":"z_y^3-z_y modulo3",
    "translation_and_tame_equivariance_identities":equivariance_checks,
    "formal_three_series_cubic_coefficient":"4*u",
    "elliptic_discriminant":"16*(u^2+4)",
    "special_tripling_series":"[3](T) = -T^9 modulo (3,u)",
    "special_y_tripling":"y([3]P)=-y^9 checked by exact curve-relation polynomial",
    "boundary_cancellation_avoidance":"c=i in F9 avoids both boundary values +/-1",
    "constructed_integer_arcs":constructed,
    "least_index_comparisons":index_comparisons,
    "absolute_indices_tested":[2,50000],
    "levels_tested":[1,8],
    "samples":samples,
    "elapsed_seconds":time.perf_counter()-started,
}
output=Path(__file__).with_name('verify_wild_trace_arcs.output.json')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
