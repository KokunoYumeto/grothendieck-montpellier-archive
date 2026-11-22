"""Exact checks for Part E; these checks certify displayed examples, not the general theorem."""
from time import perf_counter
import sympy as s
start=perf_counter()
a,b,c,d,e,f,x,y,z,lam=s.symbols('a b c d e f x y z lam')
H=s.Matrix([[2*a,d,e],[d,2*b,f],[e,f,2*c]])
D=s.expand(H.det()/2)
print('Universal ternary quadratic divided discriminant:',D)
q=x*x+y*z
print('Characteristic-two example: q=x^2+y*z')
print('Naive Hessian determinant over Z:',H.det().subs({a:1,b:0,c:0,d:0,e:0,f:1}))
print('Divided discriminant over Z:',D.subs({a:1,b:0,c:0,d:0,e:0,f:1}))
for u in [x,y,z]:
    rels=[q,s.diff(q,x),s.diff(q,y),s.diff(q,z),u-1]
    G=s.groebner(rels,x,y,z,modulus=2)
    assert list(G)==[1]
    print(f'Chart {u}=1, singular-locus Groebner basis over F_2:',list(G))
print('All three affine charts have empty geometric singular locus.')
N=3;k=3
content_exp=((k-1)**N-(-1)**N)//k
res=(k*lam)**(N*(k-1)**(N-1))
disc=s.expand(res/k**content_exp)
print('Plane Fermat cubic: Res(partials of lam*(x^3+y^3+z^3)) =',res)
print('Normalization divisor:',k**content_exp)
print('Divided discriminant:',disc)
print('Coefficient scaling degree:',s.degree(disc,lam))
assert s.degree(disc,lam)==12
print('Original proposed degree:',(k-1)*N)
print('Elapsed seconds:',perf_counter()-start)
