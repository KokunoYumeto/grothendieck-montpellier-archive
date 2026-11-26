#!/usr/bin/env python3
"""Exact dual certificates after marking both profile minima.

The coordinate group preserving both marked cuts is S_h x S_(D-h).
Its folded-cube orbits are indexed by the two block weights, modulo
simultaneous complementation.  All rows remain necessary inequalities.
"""
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, vstack

import sh_radial_rank_certificate as base


def rectangular_violation(ka,kb,D,m,h):
    r,s=2**ka,2**kb
    p,q=2**(m*(D-h)),2**(m*h)
    if q>=2:
        if r+3*s<2*p:return ["three",0,2]
        if 3*r+s<2*p:return ["three",1,2]
    for orientation in range(2):
        a,b=(r,s) if orientation==0 else (s,r)
        z=p//(2*b)
        for t in sorted({1,q,max(1,min(q,z)),max(1,min(q,z+1))}):
            if a+t*t*b<t*p:return ["square",orientation,t]
    return None



def system(config):
    D,m,h=config['dimension'],config['width'],config['marked_distance']
    lo,other=config['low_value'],config['other_low_value']
    assert 0<=h<=D//2 and 0<=lo<=(m-2)*D-1 and lo<=other<(m-1)*D
    assert 2**lo+2**other>=2**(m*(D-h))
    n=m*D;M=2**(D-1)
    def canon(a,b):return min((a,b),(h-a,D-h-b))
    orbit_keys=sorted({canon(a,b) for a in range(h+1) for b in range(D-h+1)})
    index={k:i for i,k in enumerate(orbit_keys)}
    weights=[]
    for a,b in orbit_keys:
        w=math.comb(h,a)*math.comb(D-h,b)
        if (a,b)==(h-a,D-h-b):w//=2
        weights.append(w)
    assert sum(weights)==M
    O=len(orbit_keys);nv=2*O*n;rows=[]
    def ix(term,o,t):
        assert 1<=t<=n
        return (term*O+o)*n+t-1
    def row(label,items,b):
        d={}
        for j,v in items:d[j]=d.get(j,0)+v
        rows.append((label,{j:v for j,v in d.items() if v},b))
    for term in range(2):
        for o in range(O):
            for t in range(1,n):
                row(['monotone',term,o,t],[(ix(term,o,t+1),1),(ix(term,o,t),-1)],0)
        row(['budget',term],[(ix(term,o,t),weights[o])
                            for o in range(O) for t in range(1,n+1)],
            (m-1)*D*M-1)
    triples=set()
    for o,(a,b) in enumerate(orbit_keys):
        for p,(c,d) in enumerate(orbit_keys):
            for i in range(max(0,a+c-h),min(a,c)+1):
                for j in range(max(0,b+d-(D-h)),min(b,d)+1):
                    raw=a+c-2*i+b+d-2*j
                    triples.add((o,p,min(raw,D-raw)))
    frontiers={}
    for dist in range(1,D//2+1):
        frontiers[dist]=[]
        for ka in range(n):
            kb=0
            while kb<=n and rectangular_violation(ka,kb,D,m,dist) is not None:kb+=1
            if kb:
                witness=rectangular_violation(ka,kb-1,D,m,dist)
                assert witness is not None and kb<=n
                frontiers[dist].append((ka,kb-1,witness))
    for o,p,dist in sorted(triples):
        L=m*(D-dist)
        row(['mixed',o,p,dist,0],[(ix(0,o,L-1),-1),(ix(1,p,L),-1)],-1)
        row(['mixed',o,p,dist,1],[(ix(0,o,L),-1),(ix(1,p,L-1),-1)],-1)
        if dist>=1 and 2**(m*dist)>m*(D-dist)+1:
            row(["strict_mixed",o,p,dist],[(ix(0,o,L),-1),(ix(1,p,L),-1)],-1)
        for ka,kb,witness in frontiers.get(dist,[]):
            row(["rectangular_forbidden",o,p,dist,ka,kb]+witness,[(ix(0,o,ka+1),-1),(ix(1,p,kb+1),-1)],-1)
        if dist==1:
            for term in range(2):
                for t in range(2*m+1,n+1):
                    row(['lipschitz',term,o,p,t],
                        [(ix(term,o,t),1),(ix(term,p,t-2*m),-1)],0)
    marked=[index[canon(0,0)],index[canon(h,0)]]
    for term,minimum in enumerate((lo,other)):
        row(['minimum_upper',term,marked[term],minimum],
            [(ix(term,marked[term],minimum+1),1)],0)
        if minimum:
            for o in range(O):
                row(['minimum_lower',term,o,minimum],[(ix(term,o,minimum),-1)],-1)
    for j in range(nv):
        row(['upper',j],[(j,1)],1);row(['lower',j],[(j,-1)],0)
    return dict(D=D,m=m,M=M,n=n,nv=nv,orbits=orbit_keys,weights=weights,
                marked_orbits=marked,marked_distance=h,low_value=lo,
                other_low_value=other,rectangular_strict=True,unbalanced_fold=True,rows=rows)


def main():
    config=json.loads(Path(sys.argv[1]).read_text());outpath=Path(sys.argv[2])
    data=system(config)
    if config.get('verify_file'):
        saved=json.loads(Path(config['verify_file']).read_text())
        print(json.dumps(base.verify(data,saved['certificate'])),flush=True);return
    A,b=base.sparse_matrix(data)
    eq=vstack((A.T,coo_matrix(b.reshape(1,-1)))).tocsc()
    result=linprog(np.ones(A.shape[0]),A_eq=eq,
                   b_eq=np.concatenate((np.zeros(data['nv']),[-1.])),
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
        try:checks=base.verify(data,entries)
        except AssertionError:
            entries=base.bounded_rational_certificate(data,result.x)
            checks=base.verify(data,entries)
            mode='common-grid rounding and exact box-row residual cancellation'
        out.update(certificate=entries,verification=checks,reconstruction_mode=mode,
                   claim='Exact nonnegative combination gives zero <= minus one.')
    outpath.write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k!='certificate'}),flush=True)


if __name__=='__main__':main()
