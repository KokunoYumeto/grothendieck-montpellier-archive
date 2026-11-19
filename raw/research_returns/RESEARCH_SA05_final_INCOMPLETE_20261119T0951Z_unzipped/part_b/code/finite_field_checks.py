"""Exact finite checks; the Jordan example is an obstruction model, not geometric."""
from fractions import Fraction
from time import perf_counter
start=perf_counter()

def rank(mat):
    a=[[Fraction(v) for v in row] for row in mat]
    h=len(a);w=len(a[0]) if h else 0;r=0
    for c in range(w):
        pivot=next((i for i in range(r,h) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        z=a[r][c];a[r]=[v/z for v in a[r]]
        for i in range(h):
            if i!=r:
                z=a[i][c];a[i]=[u-z*v for u,v in zip(a[i],a[r])]
        r+=1
        if r==h:break
    return r

q=2
pts=[(x,y) for x in range(q) for y in range(q)
     if (y*y+y-x*x*x+x*x+10*x+20)%q==0]
count=1+len(pts)
trace=q+1-count
print('Curve: y^2+y=x^3-x^2-10x-20 over F_2; point at infinity included.')
print('Affine points:',pts)
print('#C(F_2):',count)
print('Frobenius trace:',trace)
print('Frobenius polynomial coefficients [1,-trace,q]:',[1,-trace,q])
print('Discriminant:',trace*trace-4*q)
F=[[0,-q],[1,trace]]
basis=[[[int(i==r and j==c) for j in range(2)]for i in range(2)]
       for r in range(2) for c in range(2)]
def product(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)]for i in range(2)]
columns=[]
for x in basis:
    a=product(F,x);b=product(x,F)
    columns.append([a[i][j]-b[i][j] for i in range(2) for j in range(2)])
commutator=list(map(list,zip(*columns)))
centralizer=4-rank(commutator)
print('Companion Frobenius matrix:',F)
print('Commutator operator matrix:',commutator)
print('Centralizer dimension over Q (hence over Q_3):',centralizer)
assert count==5 and trace==-2 and centralizer==2

print('\nAbstract obstruction model only: F=[[1,1],[0,1]], M=span(e1).')
JminusI=[[0,1],[0,0]]
Wfixed=2-rank(JminusI)
Mfixed=1;quotientfixed=1
print('dim W^F:',Wfixed,'dim M^F:',Mfixed,'dim (W/M)^F:',quotientfixed)
print('The invariants quotient has dimension',Wfixed-Mfixed,
      'but quotient invariants have dimension',quotientfixed)
print('This verifies the linear obstruction; no geometric realization is asserted.')
assert Wfixed-Mfixed==0 and quotientfixed==1
print('Elapsed seconds:',round(perf_counter()-start,6))
