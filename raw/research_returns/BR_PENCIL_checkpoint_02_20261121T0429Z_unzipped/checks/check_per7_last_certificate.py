#!/usr/bin/env python3
"""Self-contained exact certificate for P-19, the final permanent seven-plane.

Every object is reconstructed from seven displayed rectangles.  Exact rational
linear algebra proves the weight and arrangement reductions.  Modular pivots
only select minors; their final determinants are evaluated over the integers.
No project data or project modules are imported.
"""
from collections import defaultdict,Counter
from datetime import datetime,timezone
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations,combinations_with_replacement
from math import gcd,lcm,isqrt
from pathlib import Path
import json,time
import numpy as np
from sympy import Matrix
from sympy.polys.matrices import DomainMatrix

RECTANGLES=[((0,1),(0,1)),((0,1),(0,2)),((0,1),(0,3)),
            ((0,2),(0,1)),((0,2),(0,2)),((1,2),(0,1)),((1,2),(0,2))]
VARIABLES=list(range(11))
PRIME=1000003

def primitive(values):
    values=list(values)
    denominator=1
    for v in values:denominator=lcm(denominator,int(v.q) if hasattr(v,'q') else Fraction(v).denominator)
    integers=[int(v*denominator) for v in values]
    divisor=0
    for v in integers:divisor=gcd(divisor,v)
    if not divisor:return ()
    integers=[v//abs(divisor) for v in integers]
    if next(v for v in integers if v)<0:integers=[-v for v in integers]
    return tuple(integers)


def integer_rows(M):
    return tuple(row for row in (primitive(M.row(i)) for i in range(M.rows)) if row)


@lru_cache(None)
def row_span(rows,d):
    if not rows:return ()
    R,pivots=Matrix(rows).rref()
    return tuple(primitive(R.row(i)) for i in range(len(pivots)))


def rank_q(M):
    """Small exact rank computation over Q, independently of SymPy rank."""
    rows=[[Fraction(int(x)) if isinstance(x,(int,np.integer)) else Fraction(str(x)) for x in row] for row in M]
    if not rows:return 0
    r=0
    for c in range(len(rows[0])):
        pivot=next((i for i in range(r,len(rows)) if rows[i][c]),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        v=rows[r][c];rows[r]=[x/v for x in rows[r]]
        for i in range(r+1,len(rows)):
            if rows[i][c]:
                v=rows[i][c];rows[i]=[x-v*y for x,y in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows):break
    return r


def arrangements(conditions,d):
    """All exact simultaneous zero patterns of linear maps on P^(d-1)."""
    spaces={()}
    for C in conditions:
        new=set()
        for E in spaces:
            F=row_span(E+C,d)
            if len(F)<d:new.add(F)
        spaces.update(new)
    states=[]
    for E in sorted(spaces):
        zeros=frozenset(j for j,C in enumerate(conditions) if len(row_span(E+C,d))==len(E))
        null=Matrix(E).nullspace() if E else [Matrix.eye(d)[:,i] for i in range(d)]
        basis=tuple(primitive(v) for v in null)
        assert len(basis)==d-len(E)
        K=Matrix.hstack(*(Matrix(v) for v in basis))
        EQ=Matrix(E) if E else Matrix.zeros(0,d)
        assert EQ*K==Matrix.zeros(EQ.rows,K.cols) and rank_q(K.tolist())==K.cols
        states.append({'equations':E,'zero_columns':zeros,'basis':basis,'dimension':len(basis)})
    return states



def wedge_matrix(basis,orientation):
    matrices=basis if orientation=='B' else [M.T for M in basis]
    n1,n2=matrices[0].shape
    pairs=list(combinations(range(n2),2))
    out=np.zeros((n1*len(pairs),len(basis)*n2),dtype=np.int64)
    for p,(i,j) in enumerate(pairs):
        for q in range(n1):
            for s,L in enumerate(matrices):
                out[q*len(pairs)+p,s*n2+j]=L[q,i]
                out[q*len(pairs)+p,s*n2+i]=-L[q,j]
    return out




def var_weight(v):
    r,c=divmod(v,4)
    return tuple(int(k==r) for k in range(4))+tuple(int(k==c) for k in range(4))


def quad_weight(rect):
    I,J=rect
    return tuple(int(k in I) for k in range(4))+tuple(int(k in J) for k in range(4))


def plus(a,b):return tuple(x+y for x,y in zip(a,b))


def construct():
    T=np.zeros((7,11,11),dtype=np.int64)
    for q,((r,s),(c,d)) in enumerate(RECTANGLES):
        a,b,x,y=4*r+c,4*r+d,4*s+c,4*s+d
        for i,j in [(a,y),(y,a),(b,x),(x,b)]:T[q,i,j]=1
    U=[T[:,:,c] for c in range(11)]
    assert rank_q(np.stack(U,axis=-1).reshape(77,11).tolist())==11
    aw=[tuple(-x for x in quad_weight(q)) for q in RECTANGLES]
    bw=[var_weight(v) for v in VARIABLES]
    classes=defaultdict(list)
    for q,a in enumerate(aw):
        for v,b in enumerate(bw):classes[plus(a,b)].append((q,v))
    image={tuple(-x for x in b):v for v,b in enumerate(bw)}
    blocks=[(w,coords,len(coords)-int(w in image)) for w,coords in classes.items() if len(coords)-int(w in image)]
    assert len(blocks)==47 and sum(d for w,c,d in blocks)==66
    basis=list(U);weights=[tuple(-x for x in b) for b in bw];owners=[-1]*11;starts={};parameters={}
    for i,(w,coords,d) in enumerate(blocks):
        starts[i]=len(basis);params=coords[:-1] if w in image else coords;parameters[i]=params
        if w in image:assert U[image[w]][coords[-1]]!=0
        assert len(params)==d
        for q,v in params:
            M=np.zeros((7,11),dtype=np.int64);M[q,v]=1;basis.append(M);weights.append(w);owners.append(i)
    assert len(basis)==77
    maps={};tables={};summary={}
    for ori,fw in [('A',aw),('B',bw)]:
        nf=len(fw);M=wedge_matrix(basis,ori);groups=defaultdict(list)
        for i,w in enumerate(weights):
            for j,u in enumerate(fw):groups[plus(w,u)].append(i*nf+j)
        quotients={};ranktables=[];baseline=0;rowsets=[]
        for w,cols in groups.items():
            rows=list(map(int,np.flatnonzero(np.any(M[:,cols],axis=1))));rowsets.append(set(rows))
            cs0=[c for c in cols if c//nf<11]
            B=Matrix(M[np.ix_(rows,cs0)].tolist()) if cs0 else Matrix.zeros(len(rows),0)
            r=rank_q(B.tolist());baseline+=r
            null=B.T.nullspace();H=Matrix([primitive(v) for v in null]) if null else Matrix.zeros(0,len(rows))
            assert H*B==Matrix.zeros(H.rows,B.cols) and rank_q(H.tolist())==H.rows and H.rows==len(rows)-r
            quotients[w]=(rows,H)
            local=M[np.ix_(rows,cols)];os=[owners[c//nf] for c in cols];optional=sorted(set(os)-{-1});lookup={};idx={q:i for i,q in enumerate(optional)}
            for n in range(min(2,len(optional))+1):
                for chosen in combinations(range(len(optional)),n):
                    mask=sum(1<<j for j in chosen);chosen_cols=[j for j,o in enumerate(os) if o<0 or mask>>idx[o]&1]
                    lookup[mask]=len(chosen_cols)-rank_q(local[:,chosen_cols].tolist())
            ranktables.append((optional,lookup))
        assert sum(map(len,rowsets))==M.shape[0] and set.union(*rowsets)==set(range(M.shape[0]))
        assert baseline==(70 if ori=='A' else 115)
        line_maps={}
        for i,(w,coords,d) in enumerate(blocks):
            line_maps[i]=[]
            for j,u in enumerate(fw):
                target=plus(w,u);rows,H=quotients[target]
                C=Matrix(M[np.ix_(rows,[(starts[i]+k)*nf+j for k in range(d)])].tolist()) if rows else Matrix.zeros(0,d)
                line_maps[i].append((target,H*C))
        maps[ori]=line_maps;tables[ori]=ranktables;summary[ori]={'full_shape':list(M.shape),'baseline_rank':baseline,'output_weights':len(groups)}
    return T,U,blocks,parameters,maps,tables,summary


def saturation_nullity(tables,mask):
    return sum(lookup[sum(((mask>>w)&1)<<j for j,w in enumerate(optional))] for optional,lookup in tables)


def integer_minor(M,order):
    M=np.array(M,dtype=np.int64);a=M.copy()%PRIME;rowids=list(range(a.shape[0]));rs=[];cs=[];r=0
    for c in range(a.shape[1]):
        nonzero=np.flatnonzero(a[r:,c])
        if not len(nonzero):continue
        k=r+int(nonzero[0])
        if k!=r:a[[r,k]]=a[[k,r]];rowids[r],rowids[k]=rowids[k],rowids[r]
        rs.append(rowids[r]);cs.append(c);a[r,c:]=a[r,c:]*pow(int(a[r,c]),-1,PRIME)%PRIME
        ids=np.flatnonzero(a[r+1:,c])+r+1
        if len(ids):a[ids,c:]=(a[ids,c:]-a[ids,c,None]*a[r,c:])%PRIME
        r+=1
        if r==order:break
    assert r==order
    determinant=int(DomainMatrix.from_Matrix(Matrix(M[np.ix_(rs,cs)].tolist())).det())
    assert determinant!=0
    return {'order':order,'rows':rs,'cols':cs,'determinant_Z':determinant}


def main():
    start=time.time();assert all(PRIME%d for d in range(2,isqrt(PRIME)+1))
    T,U,blocks,parameters,maps,tables,summary=construct();counts=Counter();surviving=[];line_info={}
    for size in [1,2]:
        for inds in combinations(range(len(blocks)),size):
            if sum(blocks[i][2] for i in inds)<2:continue
            counts['supports_tested']+=1;mask=sum(1<<i for i in inds)
            nullity={o:saturation_nullity(tables[o],mask) for o in ['A','B']}
            if min(nullity.values())<13:counts['saturation_excluded']+=1
            else:assert size==2;surviving.append(inds)
    assert counts['supports_tested']==1095 and counts['saturation_excluded']==971 and len(surviving)==124
    # Complete joint column arrangements give the uniform single-line minima.
    for i,(w,coords,d) in enumerate(blocks):
        cond=[integer_rows(Q) for o in ['A','B'] for target,Q in maps[o][i]]
        states=arrangements(cond,d)
        minima={'A':min(7-sum(j<7 for j in st['zero_columns']) for st in states),
                'B':min(11-sum(j>=7 for j in st['zero_columns']) for st in states)}
        line_info[i]={'conditions':cond,'states':states,'minimum':minima}
    pairs=[]
    for i,j in surviving:
        excluded=False
        for o,limit in [('A',8),('B',15)]:
            W1={w for w,Q in maps[o][i]};W2={w for w,Q in maps[o][j]}
            lower=line_info[i]['minimum'][o]+line_info[j]['minimum'][o]-len(W1&W2)
            if lower>limit:excluded=True;break
        if excluded:counts['line_overlap_excluded']+=1
        else:pairs.append((i,j))
    expected=[(1,23),(5,23),(19,23),(20,23),(21,23),(22,23),(23,24),(23,25)]
    assert pairs==expected and counts['line_overlap_excluded']==116
    # Every remaining pair has the same fixed one-dimensional quotient block.
    assert blocks[23][2]==1 and parameters[23]==[(2,8)]
    fixed=np.zeros((7,11),dtype=np.int64);fixed[2,8]=1
    conditional=[];fixed_extensions=[]
    for pair in pairs:
        variable=next(i for i in pair if i!=23);d=blocks[variable][2];conds=[];fixed_increment={}
        for o in ['A','B']:
            fw={w:Q for w,Q in maps[o][23]};fixed_increment[o]=sum(rank_q(Q.tolist()) for Q in fw.values())
            for w,Q in maps[o][variable]:
                F=fw.get(w)
                if F is not None and F.rows:
                    null=F.T.nullspace();H=Matrix([primitive(v) for v in null]) if null else Matrix.zeros(0,F.rows)
                    assert H*F==Matrix.zeros(H.rows,F.cols) and rank_q(H.tolist())==H.rows
                    Q=H*Q
                conds.append(integer_rows(Q))
        assert fixed_increment=={'A':2,'B':8}
        candidates=[]
        for st in arrangements(conds,d):
            incA=7-sum(z<7 for z in st['zero_columns']);incB=11-sum(z>=7 for z in st['zero_columns'])
            if incA>6 or incB>7:continue
            assert st['dimension']==1
            coefficients=st['basis'][0];X=np.zeros((7,11),dtype=np.int64)
            for c,(q,v) in zip(coefficients,parameters[variable]):X[q,v]+=c
            nonzero=np.argwhere(X);assert nonzero.shape==(1,2) and int(nonzero[0,0])==2
            v=int(nonzero[0,1]);assert X[2,v]==1
            candidates.append({'extra_variable':v,'parameter_vector':list(coefficients),'increment_A':incA,'increment_B':incB})
            fixed_extensions.append((v,U+[fixed,X]))
        assert len(candidates)==1
        conditional.append({'pair':pair,'variable_block':variable,'parameter_coordinates':parameters[variable],'conditions':conds,'candidates':candidates})
    assert {v for v,E in fixed_extensions}=={1,2,3,5,6,7,9,10}
    # Compute P12(E), then its A-prolongation P22(E), with integer certificates.
    higher=[];sympairs=list(combinations_with_replacement(range(11),2))
    for v,E in sorted(fixed_extensions):
        M12=wedge_matrix(E,'B');M=Matrix(M12.tolist());kernel=M.nullspace();assert len(kernel)==13
        N=Matrix.hstack(*(Matrix(primitive(k)) for k in kernel))
        assert M*N==Matrix.zeros(385,13)
        baseline_minor=integer_minor(M12,130);kernel_minor=integer_minor(np.array(N.tolist(),dtype=np.int64),13)
        F12=[]
        for k in range(13):
            coeff=[int(x) for x in N[:,k]];tensor=np.zeros((7,11,11),dtype=np.int64)
            for s,L in enumerate(E):
                for j in range(11):tensor[:,:,j]+=coeff[s*11+j]*L
            assert np.array_equal(tensor,tensor.transpose(0,2,1))
            F12.append(np.stack([tensor[:,i,j] for i,j in sympairs],axis=1))
        M22=wedge_matrix(F12,'A');assert M22.shape==(1386,91)
        last_minor=integer_minor(M22,79)
        higher.append({'extra_variable':v,'P12_matrix_shape':list(M12.shape),'P12_rank_minor':baseline_minor,
                       'P12_kernel_basis':[[int(x) for x in N.row(i)] for i in range(N.rows)],'kernel_independence_minor':kernel_minor,
                       'P22_matrix_shape':list(M22.shape),'P22_rank_minor':last_minor,'P22_nullity_upper':12})
        print('candidate',v,'integer determinants',baseline_minor['determinant_Z'],kernel_minor['determinant_Z'],last_minor['determinant_Z'],flush=True)
    output={'status':'PASS','finding':'P-19','statement':'The last permanent seven-plane [0,1,2,6,7,18,19] has border rank at least14 in characteristic zero',
            'rectangles':RECTANGLES,'variables':VARIABLES,'matrix_summary':summary,'counts':dict(counts),
            'remaining_pairs':pairs,'conditional_refinement':conditional,'higher_prolongation_certificates':higher,
            'utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'seconds':time.time()-start,
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('per7_last_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ['conditional_refinement','higher_prolongation_certificates']},indent=2))

if __name__=='__main__':main()
