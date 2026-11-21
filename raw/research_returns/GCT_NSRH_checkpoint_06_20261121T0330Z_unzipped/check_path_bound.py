from pathlib import Path
from itertools import product
import cmath, math, json

def check(p,d,k,t):
    V=list(product(range(p),repeat=d)); s=0j; count=0j
    for xs in product(range(len(V)),repeat=k):
        weight=math.prod(t[i] for i in xs)
        path=sum(sum(a*b for a,b in zip(V[xs[i]],V[xs[i+1]])) for i in range(k-1))%p
        if path==0: count+=weight
        s+=weight*sum(cmath.exp(2j*math.pi*h*path/p) for h in range(1,p))
    M=sum(t); R=p*count-M**k
    bound=(p-1)*p**(d*(k-1)/2)*sum(abs(x)**2 for x in t)*max(map(abs,t))**(k-2)
    assert abs(R-s)<1e-7*max(1,abs(R),abs(s))
    assert abs(R)<=bound+1e-7*max(1,bound)
    return dict(p=p,d=d,k=k,abs_R=abs(R),bound=bound,ratio=abs(R)/bound if bound else 0)

if __name__=='__main__':
    cases=[]
    for p,d in [(2,1),(3,1),(5,1),(7,1),(2,2),(3,2)]:
        for k in range(2,5):
            for t in [[1]*(p**d), [int(i==0) for i in range(p**d)], [complex((i%3)-1,(i%2)) for i in range(p**d)]]:
                cases.append(check(p,d,k,t))
    out={'scope':'Numerical checks of exact identity and inequality, not a formal proof; complex double arithmetic tolerance 1e-7.','passed':len(cases),'cases':cases}
    Path(__file__).with_name('PATH_BOUND_COMPUTATION.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Passed',len(cases),'path-bound checks.')
