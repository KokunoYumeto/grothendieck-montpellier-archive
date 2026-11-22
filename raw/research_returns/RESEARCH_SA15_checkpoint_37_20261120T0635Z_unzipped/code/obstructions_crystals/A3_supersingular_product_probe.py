#!/usr/bin/env python3
"""Exact finite-field Cartier probe; not a uniform generic-rank theorem.

E/F2: y^2+y=x^3, omega=dx, L_m=O_E(m O).
T(x^(2a))=0, T(x^(2a+1))=x^a,
T(x^(2a)y)=x^(a+1), T(x^(2a+1)y)=x^a y.
These follow from y=y^2+x^3 and Cartier semilinearity.
"""
import itertools,json,random,time
from pathlib import Path
started=time.perf_counter()

def add_term(out,term):
    if term in out: out.remove(term)
    else: out.add(term)

def mul(a,b):
    i,j=a;u,v=b
    if j+v<2:return {(i+u,j+v)}
    return {(i+u,1),(i+u+3,0)}

def cartier(poly):
    ans=set()
    for i,j in poly:
        if not j:
            if i%2:add_term(ans,((i-1)//2,0))
        elif i%2:add_term(ans,((i-1)//2,1))
        else:add_term(ans,(i//2+1,0))
    return ans

def rank(cols):
    piv={}
    for a in cols:
        while a:
            n=a.bit_length()-1
            if n in piv:a^=piv[n]
            else:piv[n]=a;break
    return len(piv)

def apply(cols,v):
    z=0
    while v:
        q=v&-v;v^=q;z^=cols[q.bit_length()-1]
    return z

def stable_rank(cols):
    n=len(cols);power=list(cols);previous=n;seq=[n]
    while True:
        r=rank(power);seq.append(r)
        if r==previous:return r,seq
        previous=r;power=[apply(cols,v) for v in power]

assert cartier({(0,0)})==set()
assert cartier({(1,0)})=={(0,0)}
assert cartier({(0,1)})=={(1,0)}
results=[]
for d in range(1,7):
    m=3*d
    B=[(i,0) for i in range(m//2+1)]+[(i,1) for i in range((m-3)//2+1)]
    assert len(B)==m
    bi={b:i for i,b in enumerate(B)}
    T=list(itertools.product(range(m),repeat=2));n=m*m
    one=[[[bi[z] for z in cartier(mul(a,b))] for b in B] for a in B]
    matrices=[]
    for a,b in T:
        matrices.append([sum(1<<(m*i+j) for i in one[a][u] for j in one[b][v]) for u,v in T])
    def matrix(s):
        C=[0]*n
        while s:
            q=s&-s;s^=q
            C=[a^b for a,b in zip(C,matrices[q.bit_length()-1])]
        return C
    rng=random.Random(2026111900+d)
    best=-1;cert=None;hist={}
    for attempt in range(1,1001):
        s=rng.getrandbits(n);C=matrix(s)
        assert apply(C,s)==0
        sr,seq=stable_rank(C);hist[sr]=hist.get(sr,0)+1
        if sr>best:
            best=sr;cert={'section_bits':s,'rank_sequence':seq,'columns':C,'attempt':attempt}
        if sr==n-1:break
    results.append({'degree':d,'factor_degree':m,'matrix_dimension':n,'best_stable_rank':best,
                    'maximal_candidate':n-1,'attempts':attempt,'histogram':hist,'certificate':cert})
    print(json.dumps({k:v for k,v in results[-1].items() if k!='certificate'}),flush=True)
out={'status':'probe_complete','curve':'y^2+y=x^3 over F2','ambient':'E x E',
     'scope':'Exact finite Cartier computations only; smoothness and uniform degree statements not inferred.',
     'results':results,'elapsed_seconds':time.perf_counter()-started}
dest=Path(__file__).with_name('A3_supersingular_product_probe_output.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print('elapsed_seconds',out['elapsed_seconds'],flush=True)
