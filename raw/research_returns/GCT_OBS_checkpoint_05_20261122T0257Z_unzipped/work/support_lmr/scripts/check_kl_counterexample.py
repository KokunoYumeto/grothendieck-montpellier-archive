#!/usr/bin/env python3
"""Integer polynomial verification of the version-scoped S-009 counterexample."""
import argparse
from collections import Counter
import json
from pathlib import Path

ZERO=(0,0,0,0)

def clean(p):return {m:c for m,c in p.items() if c}
def add(*polys):
    out=Counter()
    for p in polys:
        for m,c in p.items():out[m]+=c
    return clean(out)
def scale(p,c):return clean({m:c*v for m,v in p.items()})
def mul(p,q):
    out=Counter()
    for a,u in p.items():
        for b,v in q.items():out[tuple(x+y for x,y in zip(a,b))]+=u*v
    return clean(out)
def power(p,k):
    out={ZERO:1}
    for _ in range(k):out=mul(out,p)
    return out
def variable(i):
    m=[0]*4;m[i]=1
    return {tuple(m):1}
def raising(p):
    out=Counter()
    for m,c in p.items():
        for i in range(1,4):
            if m[i]:
                e=list(m);e[i]-=1;e[i-1]+=1
                out[tuple(e)]+=c*m[i]*(4-i)
    return clean(out)
def evaluate(p,point):
    return sum(c*product(v**e for v,e in zip(point,m)) for m,c in p.items())
def product(values):
    out=1
    for v in values:out*=v
    return out
def substitute(p,images):
    out={}
    for m,c in p.items():
        term={ZERO:c}
        for image,k in zip(images,m):term=mul(term,power(image,k))
        out=add(out,term)
    return out
def weight(p):
    return sorted({(sum((3-i)*m[i] for i in range(4)),
                    sum(i*m[i] for i in range(4))) for m in p})
def binary_weight(d,k):
    return sum(1 for e3 in range(d+1) for e2 in range(d-e3+1)
               for e1 in range(d-e3-e2+1) if e1+2*e2+3*e3==k)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path('work/support_lmr/results/kl_counterexample.json'))
    args=ap.parse_args()
    a,b,c,d=[variable(i) for i in range(4)]
    H=add(power(b,2),scale(mul(a,c),-3))
    Delta=add(mul(power(b,2),power(c,2)),scale(mul(a,power(c,3)),-4),
              scale(mul(power(b,3),d),-4),scale(mul(power(a,2),power(d,2)),-27),
              scale(mul(mul(a,b),mul(c,d)),18))
    P=mul(power(a,2),Delta);Q=power(H,3)
    assert not raising(H) and not raising(Delta)
    assert not raising(P) and not raising(Q)
    assert weight(P)==[(12,6)]==weight(Q)
    assert all(sum(m)==6 for poly in (P,Q) for m in poly)
    # Images are ordinary cubic coefficients of (u*x+v*y)^2*(s*x+t*y).
    u,v,s,t=[variable(i) for i in range(4)]
    images=[mul(power(u,2),s),
            add(mul(power(u,2),t),scale(mul(mul(u,v),s),2)),
            add(scale(mul(mul(u,v),t),2),mul(power(v,2),s)),
            mul(power(v,2),t)]
    assert not substitute(Delta,images)
    assert evaluate(P,(1,0,0,1))==-27
    assert evaluate(P,(0,1,0,0))==0
    assert evaluate(Q,(0,1,0,0))==1
    counts=[binary_weight(6,k) for k in (6,5)]
    assert counts==[7,5]
    result=dict(statement='S-009',source='arXiv:1204.4693v1 Theorem 1.3',
                n=3,m=1,outer_degree=6,partition=[12,6],weight_counts=counts,
                ambient_multiplicity=2,padded_multiplicity=1,ideal_multiplicity=1,
                P_at_x3_plus_y3=-27,Q_at_x2y=1,raising_zero=True,
                repeated_factor_substitution_zero=True,passed=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
