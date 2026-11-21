#!/usr/bin/env python3
"""Explore exact torus-weight prolongation obstructions for determinant 7-planes."""
from collections import defaultdict,Counter
from itertools import combinations
from pathlib import Path
import argparse,json,math,time
import numpy as np

PRIME=1000003
PAIRS=list(combinations(range(4),2))
RECTS=[(I,J) for I in PAIRS for J in PAIRS]
TYPE_A=[0,1,3,6,7,9,12]
TYPE_B=[0,1,3,6,7,12,13]


def var_weight(v):
    i,j=divmod(v,4)
    return tuple(int(k==i) for k in range(4))+tuple(int(k==j) for k in range(4))


def quad_weight(q):
    I,J=RECTS[q]
    return tuple(int(k in I) for k in range(4))+tuple(int(k in J) for k in range(4))


def data(S,sign):
    variables=sorted({4*i+j for q in S for i in RECTS[q][0] for j in RECTS[q][1]})
    ix={v:i for i,v in enumerate(variables)}
    a,b=len(S),len(variables)
    T=np.zeros((a,b,b),dtype=np.int64)
    for h,q in enumerate(S):
        (r,s),(c,d)=RECTS[q]
        aa,bb,xx,yy=[ix[z] for z in [4*r+c,4*r+d,4*s+c,4*s+d]]
        for i,j,v in [(aa,yy,1),(yy,aa,1),(bb,xx,sign),(xx,bb,sign)]:
            T[h,i,j]=v
    classes=defaultdict(list)
    for q,Q in enumerate(S):
        for v,V in enumerate(variables):
            w=tuple(x-y for x,y in zip(var_weight(V),quad_weight(Q)))
            classes[w].append((q,v))
    image={tuple(-x for x in var_weight(v)):k for k,v in enumerate(variables)}
    blocks=[(w,block,len(block)-(w in image)) for w,block in classes.items()
            if len(block)-(w in image)>0]
    return variables,T,blocks,image


def extension(T,blocks,image,chosen):
    killed={image.get(blocks[i][0]) for i in chosen}
    basis=[T[:,:,c].copy() for c in range(T.shape[2]) if c not in killed]
    for i in chosen:
        w,block,d=blocks[i]
        for q,v in block:
            M=np.zeros(T.shape[:2],dtype=np.int64)
            M[q,v]=1
            basis.append(M)
    return basis


def prolong(basis,orientation):
    bs=basis if orientation=='B' else [M.T for M in basis]
    n1,n2=bs[0].shape
    pairs=list(combinations(range(n2),2))
    M=np.zeros((n1*len(pairs),len(bs)*n2),dtype=np.int64)
    for p,(i,j) in enumerate(pairs):
        for q in range(n1):
            for s,L in enumerate(bs):
                M[q*len(pairs)+p,s*n2+j]=L[q,i]
                M[q*len(pairs)+p,s*n2+i]=-L[q,j]
    return M


def rank(M,prime=PRIME):
    a=M.copy()%prime
    nr,nc=a.shape;rowids=list(range(nr))
    rows=[];cols=[];r=0
    for c in range(nc):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        rr=r+int(nz[0])
        if rr!=r:
            a[[r,rr]]=a[[rr,r]];rowids[r],rowids[rr]=rowids[rr],rowids[r]
        rows.append(rowids[r]);cols.append(c)
        a[r,c:]=a[r,c:]*pow(int(a[r,c]),-1,prime)%prime
        inds=np.flatnonzero(a[r+1:,c])+r+1
        if len(inds):a[inds,c:]=(a[inds,c:]-a[inds,c,None]*a[r,c:])%prime
        r+=1
        if r==nr:break
    return r,rows,cols


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--type',choices=['A','B'],required=True)
    parser.add_argument('--sign',type=int,default=-1)
    parser.add_argument('--subset',type=int,nargs='+')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    S=args.subset if args.subset is not None else (TYPE_A if args.type=='A' else TYPE_B)
    variables,T,blocks,image=data(S,args.sign)
    target=13
    quotient_dimension=target-len(variables)
    if quotient_dimension==1:
        choices=[(i,) for i in range(len(blocks))]
    else:
        assert quotient_dimension==2
        choices=[(i,) for i,x in enumerate(blocks) if x[2]>=2]+list(combinations(range(len(blocks)),2))
    candidates=[];records=[];counts=Counter();start=time.time()
    for pos,chosen in enumerate(choices):
        bs=extension(T,blocks,image,chosen)
        dims=[];certs=[]
        for orientation in ['A','B']:
            M=prolong(bs,orientation);r,rows,cols=rank(M)
            nullity=M.shape[1]-r
            dims.append(nullity)
            if nullity<target:
                needed=M.shape[1]-target+1
                certs.append({'orientation':orientation,'matrix_shape':list(M.shape),
                              'minor_order':needed,'rows':rows[:needed],'cols':cols[:needed],
                              'nullity_upper':nullity})
        rec={'chosen':chosen,'saturated_dimension':len(bs),'kernel_upper_bounds':dims}
        if not certs:candidates.append(rec)
        else:
            c=min(certs,key=lambda x:x['minor_order'])
            rec['certificate']=c
            counts[c['orientation']]+=1
        records.append(rec)
        if pos%100==0:print(args.type,pos,len(choices),'candidates',len(candidates),'seconds',time.time()-start,flush=True)
    output={'subset':S,'sign':args.sign,'r_tested':target,'variables':variables,
            'quotient_dimension':quotient_dimension,'block_count':len(blocks),
            'blocks':[{'weight':w,'coordinates':p,'quotient_dimension':d} for w,p,d in blocks],
            'choices_tested':len(choices),'unexcluded':candidates,'records':records,
            'exclusions_by_orientation':dict(counts),'seconds':time.time()-start}
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ['blocks','records']},indent=2))


if __name__=='__main__':main()
