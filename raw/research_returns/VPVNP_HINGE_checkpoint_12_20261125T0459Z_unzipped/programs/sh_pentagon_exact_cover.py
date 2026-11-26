#!/usr/bin/env python3
"""Integer coefficient certificates for a binary two-term pentagon cover.

Also verifies the general exterior-square identity, whose term count
is1+binom(q,2).  Neither identity has subexponential overhead under the
specified binary tensor-power amplification.
"""
import itertools
import json
import sys
from pathlib import Path
import numpy as np


def source_target(q):
    src=np.zeros((q*q,)*3+(q**3,)*2,dtype=np.int64)
    target=np.zeros((q*q,)*3+(q,)*2,dtype=np.int64)
    for v in itertools.product(range(q),repeat=6):
        L=tuple(v[2*i]*q+v[2*i+1] for i in range(3))
        R=((v[0]*q+v[2])*q+v[4],(v[1]*q+v[3])*q+v[5])
        src[L+R]=1
    for x,y,z,u in itertools.product(range(q),repeat=4):
        target[x*q+y,x*q+z,y*q+z,u,u]=1
    return src,target


def maps(q,J=None):
    left=np.eye(q*q,dtype=np.int64)
    if J is not None:
        left=np.zeros_like(left)
        for a,b in itertools.product(range(q),repeat=2):left[b*q+a,a*q+b]=1
    r0=np.zeros((q,q**3),dtype=np.int64);r1=np.zeros_like(r0)
    for u,a,b,c in itertools.product(range(q),repeat=4):
        k=(a*q+b)*q+c
        if J is None:
            r0[u,k]=int(a==b and c==u)
            r1[u,k]=int(b==c and a==u)
        else:
            r0[u,k]=int(b==c)*J[a,u]
            r1[u,k]=int(a==b)*J[c,u]
    return [left.copy() for _ in range(3)]+[r0,r1]


def wedges(q):
    result=[]
    for a in range(q):
        for b in range(a+1,q):
            J=np.zeros((q,q),dtype=np.int64);J[a,b]=1;J[b,a]=-1
            result.append(J)
    return result


def main():
    cfg=json.loads(Path(sys.argv[1]).read_text());out=Path(sys.argv[2]);results=[]
    for q in cfg['core_dimensions']:
        Js=wedges(q)
        for x,y,u,v in itertools.product(range(q),repeat=4):
            lhs=int(x==y and u==v)
            rhs=int(x==v and y==u)+sum(int(J[x,u])*int(J[y,v]) for J in Js)
            assert lhs==rhs,(q,x,y,u,v,lhs,rhs)
        results.append(dict(q=q,core_entries=q**4,terms=1+len(Js),integer_core_identity=True))
    full=[]
    for q in cfg['full_dimensions']:
        src,target=source_target(q);table_sets=[maps(q)]+[maps(q,J) for J in wedges(q)]
        terms=[np.einsum('ai,bj,ck,dl,em,ijklm->abcde',*ms,src,optimize=True)
               for ms in table_sets]
        total=sum(terms);assert np.array_equal(total,target)
        save={'source':src,'target':target,'sum':total}
        for a,(ms,term) in enumerate(zip(table_sets,terms)):
            save[f'term_{a}']=term
            for i,mat in enumerate(ms):save[f'map_{a}_{i}']=mat
        np.savez_compressed(str(out.with_suffix(''))+f'_q{q}_tables.npz',**save)
        full.append(dict(q=q,terms=len(terms),output_entries=int(target.size),
                         source_nonzeros=int(np.count_nonzero(src)),
                         target_nonzeros=int(np.count_nonzero(target)),
                         maximum_coefficient_error=int(np.max(np.abs(total-target))),
                         local_coefficients=sorted({int(v) for ms in table_sets for mat in ms for v in mat.ravel()}),
                         valid_over_integers_and_every_field=True))
    result=dict(config=cfg,core_checks=results,full_checks=full,
                binary_tensor_power_terms='2^N=q for q=2^N',
                overhead_log2_per_source_copy=1,
                scope='Exact finite cover identities; neither a strict shortening nor subexponential cover is proved.')
    out.write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)


if __name__=='__main__':main()
