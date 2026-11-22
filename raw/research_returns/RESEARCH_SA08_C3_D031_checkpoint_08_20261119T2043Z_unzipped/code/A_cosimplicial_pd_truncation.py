"""Integral cotriple faces and the two filtrations for R_N=Gamma(T)/I_N.

This independently checks A-S09-12's chain comparisons at N=3,
including a complete weight-seven complex through degree three.
The general theorem uses the written filtration proof, not extrapolation.
"""
from collections import Counter
from functools import lru_cache
from math import factorial, comb
from pathlib import Path
from time import perf_counter
import json


@lru_cache(None)
def weight(t):
    return t if isinstance(t, int) else sum(weight(c)*a for c, a in t)


@lru_cache(None)
def depth(t):
    return 0 if isinstance(t, int) else 1+depth(t[0][0])


def letters(t):
    return 1 if isinstance(t, int) else sum(letters(c)*a for c, a in t)


def canonical(counts):
    return tuple(sorted(((c,a) for c,a in counts.items() if a),
                        key=lambda z:(weight(z[0]),repr(z[0]))))


@lru_cache(None)
def basis(N,n,W):
    if n==0:
        return tuple(range(1,min(N,W+1)))
    children=sorted(basis(N,n-1,W),key=lambda c:(weight(c),repr(c)))
    out=[]
    def rec(start,left,selected):
        if selected:
            out.append(tuple(selected))
        for i in range(start,len(children)):
            c=children[i]
            if weight(c)>left:
                break
            for a in range(1,left//weight(c)+1):
                rec(i+1,left-a*weight(c),selected+[(c,a)])
    rec(0,W,[])
    return tuple(out)


def level(t,l):
    if l==0:
        return [t]
    return [z for c,a in t for z in level(c,l-1)]


def nondegenerate(t):
    return all(any(sum(a for c,a in z)>1 for z in level(t,l))
               for l in range(depth(t)))


@lru_cache(None)
def substitute(t,k):
    if k==0:
        counts=Counter(); den=1
        for c,a in t:
            den*=factorial(a)
            for z,b in c:
                counts[z]+=a*b
                den*=factorial(b)**a
        num=1
        for a in counts.values():
            num*=factorial(a)
        assert num%den==0
        return num//den,canonical(counts)
    counts=Counter();num=1;den=1
    for c,a in t:
        v,z=substitute(c,k-1)
        num*=v**a;counts[z]+=a;den*=factorial(a)
    for a in counts.values():
        num*=factorial(a)
    assert num%den==0
    return num//den,canonical(counts)


@lru_cache(None)
def evaluate(N,t):
    if not t:
        return 1,0
    if weight(t)>=N:
        return 0,weight(t)
    if isinstance(t,int):
        return 1,t
    num=factorial(weight(t));den=1
    for c,a in t:
        v,w=evaluate(N,c)
        num*=v**a;den*=factorial(a)*factorial(w)**a
    assert num%den==0
    return num//den,weight(t)


@lru_cache(None)
def last_face(N,t):
    if depth(t)==1:
        v,w=evaluate(N,t)
        return (v,w) if v else (0,None)
    counts=Counter();num=1;den=1
    for c,a in t:
        v,z=last_face(N,c)
        if not v:
            return 0,None
        num*=v**a;counts[z]+=a;den*=factorial(a)
    for a in counts.values():
        num*=factorial(a)
    assert num%den==0
    return num//den,canonical(counts)


def face(N,n,i,a,t):
    out=Counter()
    if i==0:
        for c,m in t:
            counts=Counter(dict(t));counts[c]-=1
            v,b=evaluate(N,canonical(counts))
            if v and a+b<N:
                out[(a+b,c)]+=v*comb(a+b,a)
    elif i==n:
        v,z=last_face(N,t)
        if v:
            out[(a,z)]+=v
    else:
        v,z=substitute(t,i-1)
        out[(a,z)]+=v
    return out


def apply_face(N,n,i,vector):
    out=Counter()
    for (a,t),v in vector.items():
        for z,c in face(N,n,i,a,t).items():
            out[z]+=v*c
    return {z:c for z,c in out.items() if c}


def rank_mod(columns,p):
    pivots={}
    for col in columns:
        d={r:v%p for r,v in col.items() if v%p}
        while d:
            r=min(d);v=d[r]
            if r not in pivots:
                inv=pow(v,-1,p)
                pivots[r]={j:a*inv%p for j,a in d.items()}
                break
            for j,a in pivots[r].items():
                z=(d.get(j,0)-v*a)%p
                if z:
                    d[j]=z
                elif j in d:
                    del d[j]
    return len(pivots)


def normalized_complex(N,W,last_degree):
    B={};D={}
    for n in range(last_degree+1):
        B[n]=[(a,t) for a in range(N) for t in basis(N,n,W-a)
              if a+weight(t)==W and nondegenerate(t)
              and not(n==0 and t==1)]
        if n:
            rows={z:i for i,z in enumerate(B[n-1])};columns=[]
            for a,t in B[n]:
                col=Counter()
                for i in range(n+1):
                    for z,c in face(N,n,i,a,t).items():
                        if z in rows:
                            col[rows[z]]+=(-1)**i*c
                columns.append({r:v for r,v in col.items() if v})
            D[n]=columns
    return B,D


if __name__=='__main__':
    start=perf_counter();face_checks=0;filtration_checks=0
    for N in [2,3,4]:
        for W in range(2,7):
            for n in range(2,4):
                for a in range(N):
                    for t in basis(N,n,W-a):
                        if a+weight(t)!=W:
                            continue
                        for i in range(n):
                            for j in range(i+1,n+1):
                                left=apply_face(N,n-1,i,face(N,n,j,a,t))
                                right=apply_face(N,n-1,j-1,face(N,n,i,a,t))
                                assert left==right,(N,W,n,i,j,a,t,left,right)
                                face_checks+=1
                        if nondegenerate(t):
                            for (b,z),v in face(N,n,0,a,t).items():
                                assert b>a
                                filtration_checks+=1
                            for i in range(1,n):
                                for (b,z),v in face(N,n,i,a,t).items():
                                    assert b==a and letters(z)==letters(t)
                                    filtration_checks+=1
                            for (b,z),v in face(N,n,n,a,t).items():
                                assert b==a and letters(z)<letters(t)
                                filtration_checks+=1
    B,D=normalized_complex(3,7,3)
    square_checks=0
    for n in [2,3]:
        for col in D[n]:
            total=Counter()
            for j,v in col.items():
                for i,c in D[n-1][j].items():
                    total[i]+=v*c
            assert all(v==0 for v in total.values())
            square_checks+=1
    ranks={n:rank_mod(cols,7) for n,cols in D.items()}
    assert len(B[1])-ranks[1]-ranks[2]==1
    answer={'passed':True,'scope':'R_N integral face identities and both filtrations; N=3 weight7 H1 modulo7',
            'face_identity_checks':face_checks,'filtration_checks':filtration_checks,
            'weight7_N3_dimensions':{n:len(b) for n,b in B.items()},
            'ranks_mod7':ranks,'H1_dimension_mod7':1,'d_squared_columns_checked':square_checks,
            'basis':{n:[repr(z) for z in b] for n,b in B.items()},
            'sparse_integer_differential_columns':D,'runtime_seconds':perf_counter()-start}
    dest=Path(__file__).resolve().parents[1]/'logs'/'A_cosimplicial_pd_truncation.json'
    dest.write_text(json.dumps(answer,indent=2)+'\n')
    print(json.dumps({k:v for k,v in answer.items() if k not in ['basis','sparse_integer_differential_columns']},indent=2))
