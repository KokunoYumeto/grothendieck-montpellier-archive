#!/usr/bin/env python3
"""Necessary integer log-rank profiles for a two-term diameter identity.

The MILP includes the sign-frame cost bound, mixed-cut slicing, and
rank-change inequalities.  Feasibility is only a relaxation; it is not
a tensor identity.  Solver-reported infeasibility is computational
evidence, not substituted for an exact proof.
"""
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def solve(config):
    D, m = config['dimension'], config['width']
    M, n = 2**(D-1), m*D
    total = 2*M*n
    rr, cc, vv, lower, upper = [], [], [], [], []
    def ix(a,s,t):
        assert 1 <= t <= n
        return (a*M+s)*n+t-1
    def row(items,lb=-np.inf,ub=np.inf):
        r = len(lower)
        for c,v in items:
            rr.append(r); cc.append(c); vv.append(v)
        lower.append(lb); upper.append(ub)
    # x[a,s,t] means ceil(log2 rank(a,s)) >= t.
    for a in range(2):
        for s in range(M):
            for t in range(1,n):
                row([(ix(a,s,t),1),(ix(a,s,t+1),-1)],lb=0)
        row([(ix(a,s,t),1) for s in range(M) for t in range(1,n+1)],
            ub=(m-1)*D*M-1)
    # Quotient sign vectors by simultaneous negation.
    def dist(s,t):
        d=(s^t).bit_count()
        return min(d,D-d)
    for s in range(M):
        for t in range(M):
            h=dist(s,t)
            L=m*(D-h)
            # 2^k+2^l >= 2^L iff max(k,l)>=L or k=l=L-1.
            row([(ix(0,s,L-1),1),(ix(1,t,L),1)],lb=1)
            row([(ix(0,s,L),1),(ix(1,t,L-1),1)],lb=1)
            if h>=1 and 2**(m*h)>m*(D-h)+1:
                row([(ix(0,s,L),1),(ix(1,t,L),1)],lb=1)
            if h == 1:
                delta=2*m
                for a in range(2):
                    for z in range(delta+1,n+1):
                        row([(ix(a,s,z),1),(ix(a,t,z-delta),-1)],ub=0)
    # Symmetry lets one low cut be at s=0 and belong to term0.
    # From total frame cost, k0+k1 <= 2(m-1)D-1 at some cut;
    # unless m=2, target rank forces one k=n and the other <=(m-2)D-1.
    if m >= 3:
        low=(m-2)*D-1
        row([(ix(0,0,low+1),1)],lb=0,ub=0)
    matrix=coo_matrix((vv,(rr,cc)),shape=(len(lower),total)).tocsc()
    started=time.monotonic()
    integral=config.get('integral',True)
    result=milp(np.zeros(total),integrality=np.ones(total) if integral else np.zeros(total),
                bounds=Bounds(np.zeros(total),np.ones(total)),
                constraints=LinearConstraint(matrix,np.array(lower),np.array(upper)),
                options={'time_limit':config.get('seconds',120),'mip_rel_gap':0})
    out={'config':config,'variables':total,'constraints':len(lower),
         'seconds':time.monotonic()-started,'status':int(result.status),
         'message':str(result.message),
         'scope':'necessary integer rank-profile relaxation only'}
    for key in ('mip_node_count','mip_dual_bound','mip_gap'):
        if getattr(result,key,None) is not None:
            out[key]=float(getattr(result,key))
    if result.x is not None and integral:
        x=np.rint(result.x).astype(int).reshape(2,M,n)
        k=x.sum(axis=2)
        assert np.max(np.abs(result.x-np.rint(result.x))) < 1e-5
        assert all(int(v) <= (m-1)*D*M-1 for v in k.sum(axis=1))
        for s in range(M):
            for t in range(M):
                h=dist(s,t)
                assert 2**int(k[0,s])+2**int(k[1,t]) >= 2**(m*(D-h))
                if h>=1 and 2**(m*h)>m*(D-h)+1:
                    assert 2**int(k[0,s])+2**int(k[1,t]) > 2**(m*(D-h))
                for a in range(2):
                    assert abs(int(k[a,s])-int(k[a,t])) <= 2*m*h
        out.update(profiles=k.tolist(),sums=k.sum(axis=1).tolist(),
                   exact_integer_constraints_pass=True)
    elif result.x is not None:
        out['fractional']=True
        out['fractional_sums']=result.x.reshape(2,M,n).sum(axis=(1,2)).tolist()
    return out


if __name__=='__main__':
    config=json.loads(Path(sys.argv[1]).read_text())
    out=solve(config)
    Path(sys.argv[2]).write_text(json.dumps(out,indent=2))
    print(json.dumps(out),flush=True)
