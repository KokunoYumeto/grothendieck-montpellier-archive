#!/usr/bin/env python3
"""Self-contained exact characteristic-zero certificate for P-17.

Only NumPy and the Python standard library are used.  Quotient spaces and
common root kernels use exact Fraction row reduction.  Exterior-map minors
are selected and independently evaluated modulo the explicitly checked prime.
There is no imported project data, generator, or symbolic rank oracle.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
from fractions import Fraction
from datetime import datetime,timezone
from hashlib import sha256
import json,math,time
import numpy as np

P=1000003
PAIRS=list(combinations(range(4),2));RECTS=[(I,J) for I in PAIRS for J in PAIRS]
CASES=[
 [0,1,2,3,6,7,8,12,13,14],
 [0,1,2,3,4,6,7,8,12,13],
 [0,1,2,3,6,7,8,9,12,13],
 [0,1,2,3,6,7,8,12,13,18],
 [0,1,2,3,4,6,7,8,9,12],
 [0,1,2,3,4,6,7,8,12,18],
 [0,1,2,3,4,6,7,9,12,13],
 [0,1,2,3,4,6,7,12,13,18],
 [0,1,2,3,6,7,9,12,13,15],
 [0,1,2,3,4,6,7,12,18,24]]

def rowspace(rows,d):
    R=[[Fraction(x) for x in row] for row in rows];r=0
    for c in range(d):
        k=next((i for i in range(r,len(R)) if R[i][c]),None)
        if k is None:continue
        R[r],R[k]=R[k],R[r];v=R[r][c];R[r]=[x/v for x in R[r]]
        for i in range(len(R)):
            if i!=r and R[i][c]:
                v=R[i][c];R[i]=[x-v*y for x,y in zip(R[i],R[r])]
        r+=1
        if r==len(R):break
    return tuple(tuple(row) for row in R[:r])

def free_indices(rows,d):
    pivots=[next(j for j,x in enumerate(row) if x) for row in rows]
    return pivots,[j for j in range(d) if j not in pivots]

def nullspace(rows,d):
    R=rowspace(rows,d);piv,free=free_indices(R,d);out=[]
    for c in free:
        v=[Fraction(0) for _ in range(d)];v[c]=1
        for row,p in zip(R,piv):v[p]=-row[c]
        out.append(tuple(v))
    return out

def vw(v):
    r,c=divmod(v,4);return tuple(int(i==r) for i in range(4))+tuple(int(i==c) for i in range(4))

def qw(q):
    I,J=RECTS[q];return tuple(int(i in I) for i in range(4))+tuple(int(i in J) for i in range(4))

def reconstruct(S):
    a=len(S);variables=sorted({4*r+c for q in S for r in RECTS[q][0] for c in RECTS[q][1]});m=len(variables)
    vp={v:i for i,v in enumerate(variables)};sp={q:i for i,q in enumerate(S)};ri={z:i for i,z in enumerate(RECTS)}
    T=np.zeros((a,m,m),dtype=np.int64)
    for h,q in enumerate(S):
        (r,s),(c,d)=RECTS[q];x,y,z,w=[vp[u] for u in [4*r+c,4*r+d,4*s+c,4*s+d]]
        for i,j,v in [(x,w,1),(w,x,1),(y,z,-1),(z,y,-1)]:T[h,i,j]=v
    U=np.stack([T[:,:,c].reshape(-1) for c in range(m)],axis=1)
    classes=defaultdict(list)
    for h,q in enumerate(S):
        for j,v in enumerate(variables):classes[tuple(x-y for x,y in zip(vw(v),qw(q)))].append(h*m+j)
    image={tuple(-x for x in vw(v)):j for j,v in enumerate(variables)}
    blocks=[];pivots={};coordinates=[];owners=[];starts=[]
    for w,cs in classes.items():
        if w in image:
            pivots[image[w]]=cs[-1];assert U[cs[-1],image[w]] in (-1,1);cs=cs[:-1]
        if not cs:continue
        starts.append(len(coordinates));owners.extend([len(blocks)]*len(cs));coordinates.extend(cs);blocks.append((w,cs))
    assert len(pivots)==m and len(coordinates)==(a-1)*m
    X=np.eye(a*m,dtype=np.int64)[:,coordinates];Q=np.eye(a*m,dtype=np.int64)[coordinates,:].copy()
    for c,p in pivots.items():Q[:,p]-=U[coordinates,c]//int(U[p,c])
    assert not np.any(Q@U) and np.array_equal(Q@X,np.eye(len(coordinates),dtype=np.int64))
    operators=[]
    for axis in [0,1]:
        for low in range(3):
            high=low+1;R=np.zeros((a,a),dtype=np.int64);N=np.zeros((m,m),dtype=np.int64)
            for h,q in enumerate(S):
                pair=RECTS[q][axis]
                if high not in pair or low in pair:continue
                repl=tuple(low if x==high else x for x in pair);sgn=1 if repl[0]<repl[1] else -1
                target=list(RECTS[q]);target[axis]=tuple(sorted(repl));target=ri[tuple(target)]
                assert target in sp;R[sp[target],h]=sgn
            for h,v in enumerate(variables):
                rc=list(divmod(v,4))
                if rc[axis]==high:
                    rc[axis]=low;assert 4*rc[0]+rc[1] in vp;N[vp[4*rc[0]+rc[1]],h]=1
            G=np.kron(-R.T,np.eye(m,dtype=np.int64))+np.kron(np.eye(a,dtype=np.int64),N)
            assert np.array_equal(G@U,-U@N.T)
            operators.append(Q@G@X)
    arrows=[]
    for i,(w,cs) in enumerate(blocks):
        start=starts[i];maps=[]
        for G in operators:
            M=G[:,start:start+len(cs)];targets={owners[int(r)] for r in np.flatnonzero(np.any(M,axis=1))}
            assert len(targets)<=1
            if targets:
                j=next(iter(targets));s=starts[j];maps.append((j,M[s:s+len(blocks[j][1]),:].tolist()))
        arrows.append(maps)
    return variables,T,blocks,arrows

def successors(F,blocks,arrows):
    pf=[free_indices(rows,len(blocks[i][1])) for i,rows in enumerate(F)];out=[];tested=0
    for i,(w,cs) in enumerate(blocks):
        _,free=pf[i];d=len(free)
        if not d:continue
        equations=[]
        for target,N in arrows[i]:
            piv,tf=pf[target]
            for j in tf:
                equations.append(tuple(Fraction(N[j][c])-sum(F[target][k][j]*N[p][c] for k,p in enumerate(piv)) for c in free))
        K=nullspace(equations,d);tested+=1
        assert len(K)<=1,('A parameter branch remains',i,F,K)
        if not K:continue
        v=[Fraction(0) for _ in cs]
        for c,x in zip(free,K[0]):v[c]=x
        G=list(F);G[i]=rowspace(F[i]+(tuple(v),),len(cs));out.append(tuple(G))
    return out,tested

def basis(T,blocks,F):
    a,m=T.shape[:2];E=[T[:,:,c].copy() for c in range(m)]
    for i,rows in enumerate(F):
        for row in rows:
            den=math.lcm(*(x.denominator for x in row));v=np.zeros(a*m,dtype=np.int64)
            for c,x in zip(blocks[i][1],row):v[c]=int(x*den)
            E.append(v.reshape(a,m))
    return E

def exterior(E,orientation):
    L=E if orientation=='B' else [M.T for M in E];other,factor=L[0].shape;pairs=list(combinations(range(factor),2))
    M=np.zeros((other*len(pairs),len(L)*factor),dtype=np.int64)
    for h,Q in enumerate(L):
        for q in range(other):
            for k,(i,j) in enumerate(pairs):M[q*len(pairs)+k,h*factor+j]=Q[q,i];M[q*len(pairs)+k,h*factor+i]=-Q[q,j]
    return M

def select_minor(M,order):
    if min(M.shape)<order:return None
    G=M.copy()%P;ids=list(range(M.shape[0]));rows=[];cols=[];r=0
    for c in range(M.shape[1]):
        nz=np.flatnonzero(G[r:,c])
        if not len(nz):continue
        k=r+int(nz[0]);G[[k,r]]=G[[r,k]];ids[k],ids[r]=ids[r],ids[k]
        rows.append(ids[r]);cols.append(c);G[r,c:]=G[r,c:]*pow(int(G[r,c]),-1,P)%P
        ix=np.flatnonzero(G[r+1:,c])+r+1
        if len(ix):G[ix,c:]=(G[ix,c:]-G[ix,c,None]*G[r,c:])%P
        r+=1
        if r==order:return rows,cols
    return None

def determinant(M):
    G=M.copy()%P;n=G.shape[0];assert G.shape==(n,n);value=1
    for k in range(n):
        nz=np.flatnonzero(G[k:,k]);assert len(nz);j=k+int(nz[0])
        if j!=k:G[[j,k]]=G[[k,j]];value=-value
        pivot=int(G[k,k]);value=value*pivot%P;G[k,k:]=G[k,k:]*pow(pivot,-1,P)%P
        ix=np.flatnonzero(G[k+1:,k])+k+1
        if len(ix):G[ix,k:]=(G[ix,k:]-G[ix,k,None]*G[k,k:])%P
    return value%P

def serial(F):
    return [{'block':i,'basis':[[str(x) for x in row] for row in rows]} for i,rows in enumerate(F) if rows]

def main():
    assert P<2**20 and all(P%d for d in range(2,math.isqrt(P)+1));start=time.time();results=[]
    for S in CASES:
        variables,T,blocks,arrows=reconstruct(S);m=len(variables);q=17-m
        layer={tuple(() for _ in blocks)};history=[];minors=[];kernels=0
        for level in range(1,q+1):
            new=set()
            for F in layer:
                generated,n=successors(F,blocks,arrows);new.update(generated);kernels+=n
            layer=set();excluded=0
            for F in sorted(new):
                E=basis(T,blocks,F);certificate=None
                for o,factor in [('A',10),('B',m)]:
                    order=(factor-1)*17+1;M=exterior(E,o);minor=select_minor(M,order)
                    if minor:
                        rows,cols=minor;d=determinant(M[np.ix_(rows,cols)]);assert d
                        certificate={'orientation':o,'order':order,'rows':rows,'cols':cols,'determinant_mod_p':d};break
                if certificate:minors.append({'level':level,'space':serial(F),'minor':certificate});excluded+=1
                else:layer.add(F)
            history.append({'level':level,'rigid_extensions':len(new),'excluded':excluded,'remaining':len(layer)})
        assert not layer
        result={'subset':S,'variables':variables,'quotient_dimension':q,'quotient_blocks':len(blocks),'history':history,'weight_kernel_checks':kernels,'rank_minor_certificates':minors,'status':'PASS','border_rank_lower_bound':18}
        results.append(result);print(S,'PASS','kernels',kernels,'minors',len(minors),'seconds',round(time.time()-start,2),flush=True)
    output={'finding':'P-17','scope':'Ten listed determinant orbits and their transposes; characteristic zero','prime':P,'results':results,'seconds':time.time()-start,'utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=Path(__file__).with_name('det10_borel_certificate.json');path.write_text(json.dumps(output,indent=2)+'\n')
    print('PASS',path,'total minors',sum(len(x['rank_minor_certificates']) for x in results),'total kernels',sum(x['weight_kernel_checks'] for x in results),flush=True)

if __name__=='__main__':main()
