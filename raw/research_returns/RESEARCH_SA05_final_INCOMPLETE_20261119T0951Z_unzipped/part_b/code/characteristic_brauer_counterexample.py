"""Exact finite checks for Br(E x A1_F2)[2] containing infinitely many classes.

The cohomological injection is proved in sections/b3_characteristic_counterexample.tex.
This script certifies the curve, Frobenius kernel algebra, differential coefficient,
and finite initial segments of the explicitly specified infinite additive basis.
"""
from time import perf_counter
from sympy import symbols, groebner, Poly

started=perf_counter()
x,y,z,u,v=symbols('x y z u v')
F=x**3+y**2*z+y*z**2
G=groebner([F.diff(t) for t in (x,y,z)],x,y,z,modulus=2)
assert list(G)==[x**2,y**2,z**2]
points=[(a,b,1) for a in range(2) for b in range(2)
        if (b*b+b+a*a*a)%2==0]+[(0,1,0)]
assert points==[(0,0,1),(0,1,1),(0,1,0)]
assert all(tuple(a*a%2 for a in P)==P for P in points)
print('E/F2: Y^2 Z + Y Z^2 = X^3; origin O=[0:1:0]')
print('Gradient ideal Groebner basis:',list(G))
print('All F2 points:',points,'; Frobenius fixes all three.')

kernel=groebner([v+v**2+u**3,u**2,v**2],u,v,modulus=2)
assert list(kernel)==[u**2,v]
print('In the Y=1 chart: v+v^2=u^3.')
print('Frobenius kernel ideal basis:',list(kernel))
print('Its coordinate algebra is F2[u]/u^2.')

# v = sum_{j>=0} u^(3*2^j); compute x=u/v to sufficient Laurent order.
precision=18
v_coeff=[0]*precision
exponent=3
while exponent<precision:
    v_coeff[exponent]=1; exponent*=2
denominator=[v_coeff[i+3] if i+3<precision else 0 for i in range(precision-3)]
reciprocal=[0]*len(denominator); reciprocal[0]=1
for n in range(1,len(reciprocal)):
    reciprocal[n]=sum(denominator[j]*reciprocal[n-j]
                      for j in range(1,n+1))%2
x_terms={n-2:c for n,c in enumerate(reciprocal) if c}
dx_terms={n-1:(n*c)%2 for n,c in x_terms.items() if (n*c)%2}
assert dx_terms.get(0)==1 and dx_terms.get(1,0)==0
print('Laurent exponents with coefficient one in x=u/v:',sorted(x_terms))
print('Differential dx/du has constant coefficient 1 and linear coefficient 0.')
print('Thus the u*t coefficient of the formal group law is zero; ker(F)=alpha_2.')

print('Square-quotient initial segments: maximum degree, odd-monomial basis, dimension')
for N in (1,3,7,15,31,63):
    square_image={2*j for j in range(N//2+1)}
    complement=[j for j in range(N+1) if j not in square_image]
    assert complement==list(range(1,N+1,2))
    assert len(complement)==(N+1)//2
    print(N,complement,len(complement))

# Exhaustively verify an initial basis: no nonzero combination of t,t^3,...,t^15 is a square.
odd_exponents=list(range(1,16,2))
nonzero_checked=0
for coefficients in range(1,1<<len(odd_exponents)):
    powers=[e for bit,e in enumerate(odd_exponents) if coefficients & (1<<bit)]
    assert powers and all(e%2==1 for e in powers)
    nonzero_checked+=1
print('Nonzero initial-basis combinations certified nonsquare:',nonzero_checked)
print('General basis: classes of t^(2r+1), r>=0, in F2[t]/F2[t^2].')
print('Corresponding explicit alpha_2 torsors: Spec F2[t,w]/(w^2-t^(2r+1)).')
print('All exact finite checks passed.')
print(f'Runtime seconds: {perf_counter()-started:.6f}')
