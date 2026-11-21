"""Exact exploratory class-two calculation; no all-weight certificate.

Canonical rational coordinates: u=5, h=exp(sum s_m),
gamma=exp(-sum s_m/2)u, with m odd >=3. The class-two
quotient is the entire free Lie algebra through weight10.
The accompanying mathematical finite-generation justification still
requires its own whole-proof check before an arithmetic conclusion.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

def valuation(x):
    x=F(x)
    if not x: return 100000
    def vp(a):
        a=abs(a);n=0
        while a%2==0: n+=1;a//=2
        return n
    return vp(x.numerator)-vp(x.denominator)

def compute(W,u=5):
    weights=list(range(3,W+1,2))
    pairs=[(i,j) for i,j in combinations(range(len(weights)),2)
           if weights[i]+weights[j]<=W]
    def h(x):
        v=[F(u**(m*x)) for m in weights]
        z=[-F(1,2)*(F(u**(n*x)*(u**(m*x)-1),u**m-1)
                    -F(u**(m*x)*(u**(n*x)-1),u**n-1))
           for i,j in pairs for m,n in [(weights[i],weights[j])]]
        return v,z
    def mul(a,b):
        v,z=a;w,t=b
        return ([x+y for x,y in zip(v,w)],
                [z[k]+t[k]+F(1,2)*(v[i]*w[j]-v[j]*w[i])
                 for k,(i,j) in enumerate(pairs)])
    def power(a,n): return ([n*x for x in a[0]],[n*x for x in a[1]])
    def relation(roots):
        coeff=[1]
        for m in roots:
            q=[0]*(len(coeff)+1)
            for i,c in enumerate(coeff): q[i]-=u**m*c;q[i+1]+=c
            coeff=q
        r=([F(0)]*len(weights),[F(0)]*len(pairs))
        for i,c in enumerate(coeff): r=mul(r,power(h(i),c))
        return r,coeff
    r,coeff=relation(weights)
    assert all(x==0 for x in r[0])
    cols=[]
    for i,j in combinations(range(len(weights)),2):
        v,w=h(i)[0],h(j)[0]
        cols.append([v[a]*w[b]-v[b]*w[a] for a,b in pairs])
    for t in range(len(pairs)):
        cols.append([x*u**(t*(weights[a]+weights[b]))
                     for x,(a,b) in zip(r[1],pairs)])
    out={'weight_cutoff':W,'u':u,'odd_weights':weights,
         'central_pairs':[(weights[i],weights[j]) for i,j in pairs],
         'relation_coefficients':coeff,
         'relation_central_valuations':[valuation(x) for x in r[1]],
         'column_valuations':[[valuation(x) for x in c] for c in cols]}
    if len(pairs)==1:
        out['central_lattice_valuation']=min(valuation(c[0]) for c in cols)
    elif len(pairs)==2:
        vfirst=min(valuation(c[0]) for c in cols)
        vdet=min(valuation(a[0]*b[1]-a[1]*b[0]) for a,b in combinations(cols,2))
        out.update(first_projection_valuation=vfirst,
                   determinant_ideal_valuation=vdet,
                   second_filtration_valuation=vdet-vfirst)
    if W==10:
        r3,_=relation([3,5,7])
        out['odd9_candidate_linear_valuations']=[valuation(x) for x in r3[0]]
        out['odd9_candidate_central_valuations']=[valuation(x) for x in r3[1]]
    return out

if __name__=='__main__':
    data=[compute(W) for W in [8,10]]
    print(json.dumps(data,indent=2))
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2))
