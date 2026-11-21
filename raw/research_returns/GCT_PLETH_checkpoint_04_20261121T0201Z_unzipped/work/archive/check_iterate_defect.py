"""Exact universal Q_(3,2) verification and split-C3 iterate counterexample."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

def pmul(a,b):
    c=Counter()
    for x,u in a.items():
        for y,v in b.items():c[tuple(i+j for i,j in zip(x,y))]+=u*v
    return {x:v for x,v in c.items() if v}
def psum(*terms):
    c=Counter()
    for k,a in terms:
        for x,v in a.items():c[x]+=k*v
    return {x:v for x,v in c.items() if v}
def elementary(j):
    return {tuple(int(i in S) for i in range(6)):1 for S in combinations(range(6),j)}
e=[elementary(j) for j in range(7)]
edges=list(e[2])
left=Counter(tuple(sum(x[i] for x in S) for i in range(6)) for S in combinations(edges,3))
right=psum((1,pmul(pmul(e[1],e[1]),e[4])),(-2,pmul(e[2],e[4])),(-1,pmul(e[1],e[5])),(1,e[6]),(1,pmul(e[3],e[3])))
assert dict(left)==right
types={}
for x,c in left.items():
    typ=tuple(sorted((v for v in x if v),reverse=True))
    assert typ not in types or types[typ]==c
    types[typ]=c

# Green ring basis is (1,y=J2,x=J3).
def add(a,b):return tuple(a[i]+b[i] for i in range(3))
def neg(a):return tuple(-v for v in a)
def scale(a,n):return tuple(n*v for v in a)
def mul(a,b):
    return (a[0]*b[0]+a[1]*b[1],
            a[0]*b[1]+a[1]*b[0],
            a[0]*b[2]+a[2]*b[0]+a[1]*b[1]+2*(a[1]*b[2]+a[2]*b[1])+3*a[2]*b[2])
def seriesmul(a,b,N):
    c=[(0,0,0)]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N:c[i+j]=add(c[i+j],mul(x,y))
    return c
def lambdas(a,N):
    c=[(1,0,0)]+[(0,0,0)]*N
    polys=[[(1,0,0),(1,0,0)],[(1,0,0),(0,1,0),(1,0,0)],[(1,0,0),(0,0,1),(0,0,1),(1,0,0)]]
    for count,poly in zip(a,polys):
        assert count>=0
        for _ in range(count):c=seriesmul(c,poly,N)
    return c
a=(0,2,1)
v=lambdas(a,7)
actual=lambdas(v[2],3)[3]
required=add(add(add(add(mul(mul(v[1],v[1]),v[4]),scale(mul(v[2],v[4]),-2)),neg(mul(v[1],v[5]))),v[6]),mul(v[3],v[3]))
defect=add(actual,neg(required))
assert actual==(7,0,441)
assert required==(3,-4,445)
assert defect==(4,4,-4)
out={'universal_Q32_verified':True,'monomial_coefficients':{str(k):v for k,v in sorted(types.items())},
     'green_basis':['1','J2','J3'],'input':a,'exterior_coefficients':v,'actual_iterate':actual,
     'universal_polynomial_value':required,'defect':defect}
Path(__file__).with_name('ITERATE_DEFECT_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
