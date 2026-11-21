#!/usr/bin/env python3
"""Self-contained exact characteristic-zero certificate for P-21.

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


def quotients(F,blocks):
    return [free_indices(rows,len(blocks[i][1])) for i,rows in enumerate(F)]

def induced(F,pf,i,target,N):
    free=pf[i][1];piv,tf=pf[target]
    return [[Fraction(N[j][c])-sum(F[target][k][j]*N[p][c]
               for k,p in enumerate(piv)) for c in free] for j in tf]

def all_kernels(F,blocks,arrows):
    pf=quotients(F,blocks);answer=[]
    for i,(w,cs) in enumerate(blocks):
        free=pf[i][1]
        if not free:continue
        eq=[]
        for target,N in arrows[i]:eq.extend(induced(F,pf,i,target,N))
        K=nullspace(eq,len(free));lifts=[]
        for x in K:
            v=[Fraction(0) for _ in cs]
            for c,z in zip(free,x):v[c]=z
            lifts.append(tuple(v))
        if lifts:answer.append((i,lifts))
    return answer

def add(F,i,v,blocks):
    G=list(F);G[i]=rowspace(F[i]+(tuple(v),),len(blocks[i][1]));return tuple(G)

def primitive(v):
    den=math.lcm(*(x.denominator if isinstance(x,Fraction) else 1 for x in v))
    z=[int(x*den) for x in v];g=math.gcd(*z)
    if g:z=[x//abs(g) for x in z]
    return z

def minor_record(M,order):
    rc=select_minor(M,order);assert rc is not None
    rows,cols=rc;value=determinant(M[np.ix_(rows,cols)]);assert value
    return {'order':order,'rows':rows,'cols':cols,'determinant_mod_p':value}

def weight_sum(*ws):return tuple(sum(v) for v in zip(*ws))

def projective(v):
    first=next(x for x in v if x);return tuple(Fraction(x,first) for x in v)

def family(S,variables,T,blocks,F,Kblock):
    # A lower bound on the old image and exact annihilators of its weight blocks
    # certify independent new image columns; no generic numerical rank is used.
    a,m=T.shape[:2];E=basis(T,blocks,F);M0=exterior(E,'B')
    base=minor_record(M0,195)
    fw=[vw(v) for v in variables];aw=[tuple(-x for x in qw(q)) for q in S]
    pairs=list(combinations(range(m),2))
    rw=[weight_sum(u,fw[i],fw[j]) for u in aw for i,j in pairs]
    ew=[tuple(-x for x in v) for v in fw]
    ew.extend(blocks[i][0] for i,rows in enumerate(F) for row in rows)
    cw=[weight_sum(e,w) for e in ew for w in fw]
    nz=np.argwhere(M0)
    assert all(rw[int(r)]==cw[int(c)] for r,c in nz)
    kw,kcoords=blocks[Kblock];assert len(kcoords)==2
    X=[]
    for c in kcoords:
        v=np.zeros(a*m,dtype=np.int64);v[c]=1;X.append(v.reshape(a,m))
    MX=exterior(X,'B');conditions=[];records=[]
    xw=[weight_sum(kw,w) for _ in range(2) for w in fw]
    assert all(rw[int(r)]==xw[int(c)] for r,c in np.argwhere(MX))
    for j,w in enumerate(fw):
        weight=weight_sum(kw,w)
        rows=[r for r,u in enumerate(rw) if u==weight]
        cols=[c for c,u in enumerate(cw) if u==weight]
        B=M0[np.ix_(rows,cols)]
        H=[primitive(x) for x in nullspace(B.T.tolist(),len(rows))]
        Z=MX[np.ix_(rows,[j,m+j])]
        for h in H:
            assert all(sum(h[k]*int(B[k,c]) for k in range(len(rows)))==0 for c in range(len(cols)))
        C=[[sum(h[k]*int(Z[k,c]) for k in range(len(rows))) for c in range(2)] for h in H]
        conditions.append(C)
        records.append({'new_column':j,'weight':weight,'base_rows':rows,'base_cols':cols,
                        'annihilator':H,'projected_pair':C})
    ranks=[rowspace(C,2) for C in conditions]
    exceptional=sorted({projective((-R[0][1],R[0][0])) for R in ranks if len(R)==1})
    generic=sum(bool(R) for R in ranks)
    atpoints=[]
    for v in exceptional:
        inc=sum(any(sum(x*y for x,y in zip(row,v)) for row in C) for C in conditions)
        atpoints.append({'point':[str(x) for x in v],'increment':inc})
    minimum=min([generic]+[z['increment'] for z in atpoints])
    assert minimum>=10 and 195+minimum>204
    return {'space':serial(F),'base_minor':base,'new_weight_records':records,
            'generic_increment':generic,'exceptional_points':atpoints,
            'minimum_increment':minimum,'rank_lower_bound':195+minimum}

def main():
    assert P<2**20 and all(P%d for d in range(2,math.isqrt(P)+1))
    S=[0,1,2,3,6,7,9,12,18,19]
    variables,T,blocks,arrows=reconstruct(S);assert len(variables)==13
    F=[() for _ in blocks]
    for i in [56,76]:
        assert len(blocks[i][1])==1;F[i]=((Fraction(1),),)
    F=tuple(F);Kblock=48;assert len(blocks[Kblock][1])==2
    # The starting plane is itself stable.
    for i,rows in enumerate(F):
        for target,N in arrows[i]:
            for v in rows:
                image=tuple(sum(Fraction(N[r][c])*v[c] for c in range(len(v))) for r in range(len(N)))
                assert len(rowspace(F[target]+(image,),len(blocks[target][1])))==len(F[target])
    old=all_kernels(F,blocks,arrows)
    assert [(i,len(K)) for i,K in old]==[(23,1),(27,1),(32,1),(48,2),(58,1),(61,1),(63,1),(70,1),(77,1)]
    assert old[3][1]==[(Fraction(1),Fraction(0)),(Fraction(0),Fraction(1))]
    families=[]
    for i,K in old:
        if i==48:continue
        families.append({'extra_block':i,**family(S,variables,T,blocks,add(F,i,K[0],blocks),48)})
    # If the last quotient line has the same weight as K, the whole K is added.
    full=add(add(F,48,(1,0),blocks),48,(0,1),blocks)
    full_minor=minor_record(exterior(basis(T,blocks,full),'B'),205)
    # Every noncommuting last weight must have a root arrow into K.
    pf=quotients(F,blocks);preimages=[];special=set()
    for i,(w,cs) in enumerate(blocks):
        incoming=[N for target,N in arrows[i] if target==48]
        if not incoming or i==48:continue
        assert len(incoming)==1
        free=pf[i][1];eq=[]
        for target,N in arrows[i]:
            if target!=48:eq.extend(induced(F,pf,i,target,N))
        K=nullspace(eq,len(free));J=induced(F,pf,i,48,incoming[0])
        images=[tuple(sum(row[c]*v[c] for c in range(len(free))) for row in J) for v in K]
        assert len(K)==1 and len(images)==1 and any(images[0])
        point=projective(images[0]);special.add(point)
        lift=[Fraction(0) for _ in cs]
        for c,z in zip(free,K[0]):lift[c]=z
        preimages.append({'block':i,'preimage_basis':[str(x) for x in lift],
                          'root_image':[str(x) for x in images[0]],'required_point':[str(x) for x in point]})
    assert [r['block'] for r in preimages]==[13,38,49,51]
    assert special=={(Fraction(1),Fraction(1)),(Fraction(0),Fraction(1))}
    specials=[]
    for v in sorted(special):
        G=add(F,48,v,blocks);K=all_kernels(G,blocks,arrows)
        assert len(K)==11 and all(len(z)==1 for i,z in K)
        records=[]
        for i,z in K:
            H=add(G,i,z[0],blocks)
            records.append({'space':serial(H),'minor':minor_record(exterior(basis(T,blocks,H),'B'),205)})
        specials.append({'point':[str(x) for x in v],'extensions':records})
    output={'finding':'P-21','status':'PASS','subset':S,'field_scope':'characteristic zero',
            'starting_quotient_space':serial(F),'parameter_weight':blocks[48][0],
            'parameter_block':48,'parameter_coordinates':blocks[48][1],
            'commuting_families':families,'full_parameter_plane_minor':full_minor,
            'noncommuting_preimages':preimages,'special_points':specials,
            'rank_threshold':204,'exclusion_minor_order':205,
            'total_minor_count':8+1+sum(len(z['extensions']) for z in specials),
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=Path(__file__).with_name('early_borel_branch_certificate.json')
    path.write_text(json.dumps(output,indent=2,default=str)+'\n')
    print('PASS: eight commuting families, full plane, four root preimages, two special points with22 rigid extensions;31 modular minors; all B-ranks>204.')
    print('Family increments:',[(r['extra_block'],r['minimum_increment']) for r in families])
    print(path)

if __name__=='__main__':main()
