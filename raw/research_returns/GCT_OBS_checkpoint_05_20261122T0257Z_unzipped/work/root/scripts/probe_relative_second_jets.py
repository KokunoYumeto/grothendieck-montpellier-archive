#!/usr/bin/env python3
"""Exploratory exact-modular second-jet gate for determinant coefficient fibers.

NumPy accelerates exact bounded integer matrix arithmetic. A successful
probe still requires an independent standard-library certificate checker.
No multiplicity conclusion is asserted by this file alone.
"""
from pathlib import Path
from time import monotonic
import argparse
import json
import numpy as np
from check_binary_jets import pencil

def labels(j):
    return [(j-y-z,y,z) for y in range(j+1) for z in range(j-y+1)]

def setup(n,s,p,seed):
    a,b=pencil(n,p,seed)
    matrices=[np.diag(np.arange(1,n+1,dtype=np.int64)),
              np.array(a,dtype=np.int64).reshape(n,n),np.array(b,dtype=np.int64).reshape(n,n)]
    coordinates=[labels(j) for j in range(s+1)];maps=[None]
    for j in range(1,s+1):
        index={a:i for i,a in enumerate(coordinates[j-1])};level=[]
        for k in range(3):
            dest=[];source=[]
            for i,alpha in enumerate(coordinates[j]):
                if alpha[k]:
                    beta=list(alpha);beta[k]-=1
                    dest.append(i);source.append(index[tuple(beta)])
            level.append((np.array(dest),np.array(source)))
        maps.append(level)
    eye=np.eye(n,dtype=np.int64);base=[eye[None,:,:]];jacobian=[]
    for j in range(1,s+1):
        total=np.zeros((len(coordinates[j]),n,n),dtype=np.int64)
        row=np.zeros((len(coordinates[j]),3,n,n),dtype=np.int64)
        for k,(dest,source) in enumerate(maps[j]):
            previous=base[-1][source]
            total[dest]+=matrices[k]@previous
            row[dest,k]=previous.transpose(0,2,1)
        elementary=np.trace(total,axis1=1,axis2=2)*pow(j,-1,p)%p
        base.append((elementary[:,None,None]*eye-total)%p)
        jacobian.append(row.reshape(len(coordinates[j]),3*n*n))
    return matrices,coordinates,maps,base,np.concatenate(jacobian)

def echelon(matrix,limit,p):
    a=matrix.copy();rank=0;pivots=[]
    for column in range(limit):
        candidates=np.flatnonzero(a[rank:,column])
        if not len(candidates):continue
        chosen=rank+int(candidates[0])
        if chosen!=rank:a[[chosen,rank]]=a[[rank,chosen]]
        a[rank,column:]=a[rank,column:]*pow(int(a[rank,column]),-1,p)%p
        if rank+1<len(a):
            values=a[rank+1:,column].copy()
            a[rank+1:,column:]=(a[rank+1:,column:]-values[:,None]*a[rank,column:])%p
        pivots.append(column);rank+=1
        if rank==len(a):break
    return a,pivots

def linear_data(jac,lower_count,p):
    width=jac.shape[1];low=jac[:lower_count]
    aug=np.concatenate((low,np.eye(lower_count,dtype=np.int64)),axis=1)
    reduced,pivots=echelon(aug,width,p)
    assert len(pivots)==lower_count
    top=jac[lower_count:];s=len(top)
    out=np.concatenate((top,np.zeros((s,lower_count),dtype=np.int64),np.eye(s,dtype=np.int64)),axis=1)
    for i,column in enumerate(pivots):
        values=out[:,column].copy()
        out[:,:width+lower_count]=(out[:,:width+lower_count]-values[:,None]*reduced[i])%p
    result,next_pivots=echelon(out,width,p)
    normal=result[len(next_pivots):,width:]
    assert not np.any(result[len(next_pivots):,:width])
    assert not np.any((normal@jac)%p)
    return reduced[:,:width],pivots,normal,lower_count+len(next_pivots)

def direction(reduced,pivots,p,state):
    width=reduced.shape[1];chosen=set(pivots);v=np.zeros(width,dtype=np.int64)
    for j in range(width):
        if j in chosen:continue
        state=(1664525*state+1013904223)%2**32
        v[j]=(state>>16)%p
    for i in range(len(pivots)-1,-1,-1):
        col=pivots[i]
        v[col]=-int(reduced[i,col+1:]@v[col+1:])%p
    return v,state

def second_jet(matrices,coordinates,maps,base,vector,p):
    n=matrices[0].shape[0];s=len(coordinates)-1
    variation=vector.reshape(3,n,n);eye=np.eye(n,dtype=np.int64)
    first=np.zeros((1,n,n),dtype=np.int64);second=first.copy();output=[]
    for j in range(1,s+1):
        t1=np.zeros((len(coordinates[j]),n,n),dtype=np.int64);t2=t1.copy()
        for k,(dest,source) in enumerate(maps[j]):
            t1[dest]+=matrices[k]@first[source]+variation[k]@base[j-1][source]
            t2[dest]+=matrices[k]@second[source]+variation[k]@first[source]
        e1=np.trace(t1,axis1=1,axis2=2)*pow(j,-1,p)%p
        e2=np.trace(t2,axis1=1,axis2=2)*pow(j,-1,p)%p
        first=(e1[:,None,None]*eye-t1)%p
        second=(e2[:,None,None]*eye-t2)%p
        output.append(e2)
    return np.concatenate(output)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--n',type=int,default=23);ap.add_argument('--last-jet',type=int,default=17)
    ap.add_argument('--directions',type=int,default=90)
    ap.add_argument('--output',type=Path,default=Path('work/root/results/det23_relative_second_jets'))
    args=ap.parse_args();p=101;seed=20261122;n=args.n;s=args.last_jet
    start=monotonic();args.output.mkdir(parents=True,exist_ok=True)
    matrices,coordinates,maps,base,jac=setup(n,s,p,seed)
    lower_count=sum(len(coordinates[j]) for j in range(1,s))
    reduced,pivots,normal,rank=linear_data(jac,lower_count,p)
    assert rank==2*n*n+1,('full normalized determinant dimension not reached',rank)
    print(json.dumps(dict(stage='linear',jacobian_shape=jac.shape,lower_rank=lower_count,full_rank=rank,normal_dimension=len(normal),seconds=monotonic()-start)),flush=True)
    vectors=[];seconds=[];columns=[];state=seed
    np.savez_compressed(args.output/'linear_data.npz',jacobian=jac.astype(np.uint8),
                        normal=normal.astype(np.uint8),pivots=np.array(pivots),reduced=reduced.astype(np.uint8))
    for i in range(args.directions):
        v,state=direction(reduced,pivots,p,state)
        assert not np.any((jac[:lower_count]@v)%p)
        h=second_jet(matrices,coordinates,maps,base,v,p)
        z=normal@h%p
        vectors.append(v);seconds.append(h);columns.append(z)
        _,current=echelon(np.array(columns),len(normal),p)
        result=dict(status='EXPLORATORY',n=n,last_jet=s,prime=p,seed=seed,
                    lower_rank=lower_count,full_rank=rank,normal_dimension=len(normal),
                    directions=i+1,second_normal_rank=len(current),seconds=monotonic()-start)
        np.savez_compressed(args.output/'direction_data.npz',directions=np.array(vectors,dtype=np.uint8),
                            second_jets=np.array(seconds,dtype=np.uint8),normal_columns=np.array(columns,dtype=np.uint8))
        (args.output/'status.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result),flush=True)
        if len(current)==len(normal):break

if __name__=='__main__':main()
