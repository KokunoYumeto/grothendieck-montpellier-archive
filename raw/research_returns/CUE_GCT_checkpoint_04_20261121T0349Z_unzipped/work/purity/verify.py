from itertools import product, combinations
from pathlib import Path
import sympy as sp
import datetime
out=[]
def record(identifier,description,ok,details):
    assert ok,(identifier,details)
    out.append((identifier,description,'PASS',details))
x1,x2,x3=sp.symbols('x1 x2 x3')
row=sp.Matrix([[1,x1,x1*x1]])
mid=sp.Matrix([[x2,x2*x2,0],[-1,0,x2*x2],[0,-1,-x2]])
col=sp.Matrix([x3*x3,-x3,1])
v=sp.expand((row*mid*col)[0])
expected=(x2-x1)*(x3-x1)*(x3-x2)
record('P-03b','Exact symbolic width-three Vandermonde certificate',sp.expand(v-expected)==0,str(v))
u,b=sp.symbols('u b')
checks=0
for signs in product([-1,1],repeat=3):
    assert sp.expand(v.subs({x1:u+b*signs[0],x2:u+b*signs[1],x3:u+b*signs[2]}))==0
    checks+=1
record('P-03b','Common affine sign sampler annihilation',True,f'{checks} symbolic sign cases')
checks=0
for n in range(1,6):
    cube=list(product([-1,1],repeat=n))
    for a in cube:
        for x in cube:
            val=1
            for ai,xi in zip(a,x):val*=1+ai*xi
            assert (val!=0)==(a==x)
            checks+=1
record('P-03a','Sign-cube unique-value polynomials',True,f'{checks} exact evaluations, n=1..5')
for n,d,s,p in [(2,2,4,13),(3,2,3,11)]:
    supports=list(product(range(d+1),repeat=n))
    weights=[[1+pow(t,i,p) for i in range(1,n+1)] for t in range(p)]
    checks=0
    for S in combinations(supports,s):
        assert any(len({sum(ai*wi for ai,wi in zip(a,w)) for a in S})==s for w in weights)
        checks+=1
    record('P-07','Exhaustive bounded-support weights',True,f'n={n}, d={d}, s={s}, p={p}, {checks} supports')
p=101;n=3
pts=[t for t in range(p) if all((t+i)%p!=0 for i in range(1,n+1))]
def chi(a):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
mat=sp.Matrix([[chi(t+i) for i in range(1,n+1)] for t in pts])
gram=mat.T*mat
record('P-06','Kummer Gram matrix exact positive principal minors',all(gram[:i,:i].det()>0 for i in range(1,n+1)),f'p={p}; Q={len(pts)}; Gram={str(gram).replace(chr(10)," ")}; det={gram.det()}')
text='statement_id\tcheck\toutcome\tdetails\n'+'\n'.join('\t'.join(row) for row in out)+'\n'
Path('work/purity/computation_results.tsv').write_text(text)
print(text)
print('Completed UTC',datetime.datetime.now(datetime.timezone.utc).isoformat())
