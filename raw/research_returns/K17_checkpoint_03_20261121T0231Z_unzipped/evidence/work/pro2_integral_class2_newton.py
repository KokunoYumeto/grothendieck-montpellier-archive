"""Exact class-two Newton correction test; no full all-weight theorem.

At cutoff W=2*r+2, the odd linear nodes are a_i=u**(2*i+3), i<r.
The relation f_r(gamma)=prod(gamma-a_i) is implemented as the ordered
group product prod_t h_t**c_t. Its central logarithm is computed exactly.
It belongs to the commutator lattice iff its coefficients in the
triangular Newton-wedge basis are 2-integral. This is a structural
second-generator-length test, not an extension of the full weight18
certificate to the displayed larger cutoffs.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from time import monotonic
import argparse
import json


def v2(x):
    x=Q(x)
    if not x:
        return None
    def vint(n):
        n=abs(n)
        return (n & -n).bit_length()-1
    return vint(x.numerator)-vint(x.denominator)


def polynomial(roots):
    c=[1]
    for a in roots:
        d=[0]*(len(c)+1)
        for i,b in enumerate(c):
            d[i]-=a*b
            d[i+1]+=b
        c=d
    return c


def compute(r,u=5):
    start=monotonic()
    nodes=[u**(2*i+3) for i in range(r)]
    pairs=sorted([(i,j) for i,j in combinations(range(r),2)
                  if i+j<=r-2], key=lambda ij:(sum(ij),ij))
    coefficients=polynomial(nodes)
    linear=[0]*r
    central=[0]*len(pairs)
    powers=[[a**t for t in range(r+1)] for a in nodes]
    geometric=[[(p-1)//(a-1) for p in ps]
               for a,ps in zip(nodes,powers)]
    for t,c in enumerate(coefficients):
        for n,(i,j) in enumerate(pairs):
            twice_b=-(powers[j][t]*geometric[i][t]
                      -powers[i][t]*geometric[j][t])
            twice_cross=c*(linear[i]*powers[j][t]
                           -linear[j]*powers[i][t])
            twice_add=c*twice_b+twice_cross
            assert twice_add%2==0
            central[n]+=twice_add//2
        for i in range(r):
            linear[i]+=c*powers[i][t]
    assert all(x==0 for x in linear)

    # A second formula checks the entire relation central vector.
    for n,(i,j) in enumerate(pairs):
        a,b=nodes[i],nodes[j]
        fab=1
        for root in nodes:
            fab*=a*b-root
        total=Q(a-b,2*(a-1)*(b-1))*fab
        total+=sum(Q(coefficients[x]*coefficients[y],2)*
                   (powers[i][x]*powers[j][y]
                    -powers[j][x]*powers[i][y])
                   for x in range(r+1) for y in range(x+1,r+1))
        assert total==central[n]

    # values[k][i]=f_i(a_k), triangular with diagonal delta_i.
    values=[]
    for a in nodes:
        row=[1]
        for root in nodes:
            row.append(row[-1]*(a-root))
        values.append(row)
    residual=list(map(Q,central))
    result=[]
    for n,(i,j) in enumerate(pairs):
        diagonal=values[i][i]*values[j][j]
        c=residual[n]/diagonal
        result.append({'pair_indices':[i,j],
                       'pair_weights':[2*i+3,2*j+3],
                       'coefficient':str(c),'valuation':v2(c)})
        for k in range(n,len(pairs)):
            a,b=pairs[k]
            wedge=(values[a][i]*values[b][j]
                   -values[a][j]*values[b][i])
            residual[k]-=c*wedge
        assert residual[n]==0
    assert all(x==0 for x in residual)
    finite=[x['valuation'] for x in result if x['valuation'] is not None]
    return {'r':r,'class2_cutoff':2*r+2,'u':u,
            'central_dimension':len(pairs),
            'minimum_coefficient_valuation':min(finite) if finite else None,
            'integral':all(v>=0 for v in finite),
            'coefficients':result,'seconds':monotonic()-start}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('r',nargs='+',type=int)
    parser.add_argument('--output',default='work/pro2_integral_class2_newton.json')
    args=parser.parse_args()
    data=[]
    for r in args.r:
        d=compute(r)
        data.append(d)
        Path(args.output).write_text(json.dumps(data,indent=2))
        print({k:v for k,v in d.items() if k!='coefficients'},flush=True)


if __name__=='__main__':
    main()
