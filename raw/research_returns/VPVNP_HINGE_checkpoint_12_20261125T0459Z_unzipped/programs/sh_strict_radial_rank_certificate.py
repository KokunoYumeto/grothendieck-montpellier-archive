#!/usr/bin/env python3
"""Exact Farkas certificates with the rectangular Clifford strict-fold constraints.

SciPy only proposes the dual coefficients.  Fractions/integer arithmetic
then verifies their signs, complete cancellation, and negative RHS.
"""
import json
import math
import sys
from fractions import Fraction
from functools import reduce
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, vstack


def system(D,m=4,low_value=None,global_min=False,minimum_both=False):
    M,n=2**(D-1),m*D
    layers=D//2+1
    nv=2*layers*n
    weights=[math.comb(D,a) if 2*a<D else math.comb(D,a)//2
             for a in range(layers)]
    assert sum(weights)==M
    rows=[]
    def ix(term,a,t):
        assert 1<=t<=n
        return (term*layers+a)*n+t-1
    def row(label,items,b):
        d={}
        for k,v in items:d[k]=d.get(k,0)+v
        rows.append((label,{k:v for k,v in d.items() if v},b))
    for term in range(2):
        for a in range(layers):
            for t in range(1,n):
                row(['monotone',term,a,t],[(ix(term,a,t+1),1),(ix(term,a,t),-1)],0)
        row(['budget',term],[(ix(term,a,t),weights[a])
                            for a in range(layers) for t in range(1,n+1)],
            (m-1)*D*M-1)
    def dist(s,t):
        d=(s^t).bit_count()
        return min(d,D-d)
    triples=sorted({(a,b,min(a+b-2*j,D-a-b+2*j))
                    for a in range(layers) for b in range(layers)
                    for j in range(max(0,a+b-D),min(a,b)+1)})
    if D<=9:
        enumerated={(dist(s,0),dist(t,0),dist(s,t))
                    for s in range(M) for t in range(M)}
        assert set(triples)==enumerated
    for a,b,h in triples:
        L=m*(D-h)
        row(['mixed',a,b,h,0],[(ix(0,a,L-1),-1),(ix(1,b,L),-1)],-1)
        row(['mixed',a,b,h,1],[(ix(0,a,L),-1),(ix(1,b,L-1),-1)],-1)
        if h>=1 and 2**(m*h)>m*(D-h)+1:
            row(['strict_mixed',a,b,h],[(ix(0,a,L),-1),(ix(1,b,L),-1)],-1)
        if h==1:
            for term in range(2):
                for t in range(2*m+1,n+1):
                    row(['lipschitz',term,a,b,t],
                        [(ix(term,a,t),1),(ix(term,b,t-2*m),-1)],0)
    row(['low_cut'],[(ix(0,0,(m-2)*D),1)],0)
    if low_value is not None:
        assert 0<=low_value<=(m-2)*D-1
        row(['exact_low_upper',low_value],[(ix(0,0,low_value+1),1)],0)
        if low_value:
            hs=range(layers) if global_min else [0]
            for a in hs:
                row(['exact_low_lower',a,low_value],[(ix(0,a,low_value),-1)],-1)
            if minimum_both:
                assert global_min
                for a in range(layers):
                    row(['other_global_lower',a,low_value],[(ix(1,a,low_value),-1)],-1)
    for j in range(nv):
        row(['upper',j],[(j,1)],1)
        row(['lower',j],[(j,-1)],0)
    return dict(D=D,m=m,M=M,n=n,layers=layers,nv=nv,weights=weights,
                rectangular_strict=True,low_value=low_value,global_min=global_min,
                minimum_both=minimum_both,rows=rows)


def sparse_matrix(data):
    ri,ci,va=[],[],[]
    for i,(_,row,_) in enumerate(data['rows']):
        for j,v in row.items():ri.append(i);ci.append(j);va.append(v)
    A=coo_matrix((va,(ri,ci)),shape=(len(data['rows']),data['nv'])).tocsc()
    b=np.array([r[2] for r in data['rows']],dtype=float)
    return A,b


def verify(data,entries):
    accum=[Fraction(0) for _ in range(data['nv'])]
    rhs=Fraction(0)
    for entry in entries:
        i=entry['row']
        coefficient=Fraction(entry['numerator'],entry['denominator'])
        assert coefficient>=0
        label,row,b=data['rows'][i]
        assert label==entry['label']
        for j,v in row.items():accum[j]+=coefficient*v
        rhs+=coefficient*b
    assert all(x==0 for x in accum),[(i,str(x)) for i,x in enumerate(accum) if x]
    assert rhs<0,rhs
    denominator=math.lcm(*(e['denominator'] for e in entries))
    numerators=[e['numerator']*(denominator//e['denominator']) for e in entries]
    divisor=reduce(math.gcd,numerators)
    return dict(exact_cancellation=True,exact_rhs=str(rhs),
                integer_scale=denominator//math.gcd(denominator,divisor),
                max_denominator=max(e['denominator'] for e in entries),
                max_numerator=max(abs(e['numerator']) for e in entries))


def bounded_rational_certificate(data,proposal):
    """Repair rational residuals using the explicitly included box rows.

    All arithmetic after rounding the proposal is integer arithmetic.
    The exact verification, not a tolerance, decides validity.
    """
    scale=10**12
    multipliers={i:max(0,round(float(v)*scale))
                 for i,v in enumerate(proposal) if v>0}
    accum=[0]*data['nv']
    upper={row[0][1]:i for i,row in enumerate(data['rows']) if row[0][0]=='upper'}
    lower={row[0][1]:i for i,row in enumerate(data['rows']) if row[0][0]=='lower'}
    for i,c in multipliers.items():
        for j,v in data['rows'][i][1].items():accum[j]+=c*v
    for j,c in enumerate(accum):
        if c>0:
            i=lower[j];multipliers[i]=multipliers.get(i,0)+c
        elif c<0:
            i=upper[j];multipliers[i]=multipliers.get(i,0)-c
    rhs=sum(c*data['rows'][i][2] for i,c in multipliers.items())
    assert rhs<0,('rounded dual cannot be certified',rhs)
    entries=[]
    for i,c in sorted(multipliers.items()):
        if c:
            f=Fraction(c,-rhs)
            entries.append(dict(row=i,label=data['rows'][i][0],
                                numerator=f.numerator,denominator=f.denominator))
    return entries


def main():
    config=json.loads(Path(sys.argv[1]).read_text())
    outfile=Path(sys.argv[2])
    data=system(config['dimension'],config.get('width',4),
                config.get('low_value'),config.get('global_min',False),
                config.get('minimum_both',False))
    if config.get('verify_file'):
        saved=json.loads(Path(config['verify_file']).read_text())
        checks=verify(data,saved['certificate'])
        print(json.dumps(checks),flush=True)
        return
    A,b=sparse_matrix(data)
    eq=vstack((A.T,coo_matrix(b.reshape(1,-1)))).tocsc()
    eqrhs=np.concatenate((np.zeros(data['nv']),[-1.0]))
    result=linprog(np.ones(A.shape[0]),A_eq=eq,b_eq=eqrhs,
                   bounds=(0,None),method='highs',
                   options={'time_limit':config.get('seconds',120),
                            'dual_feasibility_tolerance':1e-9,
                            'primal_feasibility_tolerance':1e-9})
    out={k:v for k,v in data.items() if k!='rows'}
    out.update(constraints=len(data['rows']),solver_status=int(result.status),
               solver_message=str(result.message),
               claim='No claim unless exact rational verification passes.')
    if result.x is not None:
        entries=[]
        for i,v in enumerate(result.x):
            if v>1e-9:
                f=Fraction(float(v)).limit_denominator(10**8)
                entries.append(dict(row=i,label=data['rows'][i][0],
                                    numerator=f.numerator,denominator=f.denominator))
        mode='direct rational reconstruction'
        try:
            checks=verify(data,entries)
        except AssertionError:
            entries=bounded_rational_certificate(data,result.x)
            checks=verify(data,entries)
            mode='common-grid rounding and exact box-row residual cancellation'
        out.update(certificate=entries,verification=checks,
                   reconstruction_mode=mode,
                   claim='Exact nonnegative combination of necessary inequalities gives 0 <= a negative rational.')
    outfile.write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k!='certificate'}),flush=True)


if __name__=='__main__':main()
