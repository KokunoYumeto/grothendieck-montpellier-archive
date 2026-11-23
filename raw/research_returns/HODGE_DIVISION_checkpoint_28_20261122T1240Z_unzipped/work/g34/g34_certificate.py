#!/usr/bin/env python3
"""Independent exact G34 and parabolic-monodromy certificate.

Candidate roots and intervals: Severn 2610.00387v2, Appendix A.
Only this input data is used; no printed cohomology basis or logarithm is used.
Arithmetic is in Q[w]/(w*w+w+1), using Python Fraction.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from collections import deque
from pathlib import Path
import json, time

@dataclass(frozen=True)
class K:
    a: F = F(0)
    b: F = F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a))
        object.__setattr__(self,'b',F(self.b))
    @staticmethod
    def c(v): return v if isinstance(v,K) else K(v)
    def __add__(s,t):
        t=K.c(t); return K(s.a+t.a,s.b+t.b)
    __radd__=__add__
    def __neg__(s): return K(-s.a,-s.b)
    def __sub__(s,t): return s+-K.c(t)
    def __rsub__(s,t): return K.c(t)+-s
    def __mul__(s,t):
        t=K.c(t); return K(s.a*t.a-s.b*t.b,s.a*t.b+s.b*t.a-s.b*t.b)
    __rmul__=__mul__
    def bar(s): return K(s.a-s.b,-s.b)
    def __truediv__(s,t):
        t=K.c(t); n=(t*t.bar()).a
        if not n: raise ZeroDivisionError
        r=s*t.bar(); return K(r.a/n,r.b/n)
    def __rtruediv__(s,t): return K.c(t)/s
    def __bool__(s): return bool(s.a or s.b)
    def __str__(s): return f'({s.a})+({s.b})w'
    def pair(s): return [str(s.a),str(s.b)]

z=K(); o=K(1); w=K(0,1)
def zero(m,n): return [[z for _ in range(n)] for _ in range(m)]
def eye(n): return [[K(i==j) for j in range(n)] for i in range(n)]
def transpose(A): return [list(x) for x in zip(*A)]
def add(A,B): return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def neg(A): return [[-x for x in r] for r in A]
def sub(A,B): return add(A,neg(B))
def mul(A,B):
    Bt=transpose(B)
    return [[sum((x*y for x,y in zip(a,b) if x and y),z) for b in Bt] for a in A]
def mv(A,v): return [sum((x*y for x,y in zip(a,v) if x and y),z) for a in A]
def cols(A,js): return [[r[j] for j in js] for r in A]
def hcat(*As): return [sum((list(A[i]) for A in As),[]) for i in range(len(As[0]))]
def iszero(A): return not any(any(r) for r in A)
def rref(A):
    A=[list(r) for r in A]; p=[]; r=0
    for j in range(len(A[0])):
        k=next((i for i in range(r,len(A)) if A[i][j]),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]; c=A[r][j]; A[r]=[x/c for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][j]:
                c=A[i][j]; A[i]=[x-c*y for x,y in zip(A[i],A[r])]
        p.append(j); r+=1
        if r==len(A): break
    return A,p
def rank(A): return len(rref(A)[1])
def det(A):
    A=[list(row) for row in A]; n=len(A); out=o
    assert all(len(row)==n for row in A)
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        if k is None: return z
        if k!=j: A[j],A[k]=A[k],A[j]; out=-out
        p=A[j][j]; out=out*p
        for i in range(j+1,n):
            c=A[i][j]/p
            for l in range(j+1,n): A[i][l]=A[i][l]-c*A[j][l]
    return out
def null(A):
    R,p=rref(A); free=[i for i in range(len(A[0])) if i not in p]
    out=zero(len(A[0]),len(free))
    for j,f in enumerate(free):
        out[f][j]=o
        for i,pi in enumerate(p): out[pi][j]=-R[i][f]
    return out
def inv(A):
    n=len(A); R,p=rref(hcat(A,eye(n))); assert p[:n]==list(range(n))
    assert cols(R,list(range(n)))==eye(n)
    return cols(R,list(range(n,2*n)))
def rowbasis_inverse(A):
    # A has independent columns. Return J with J A = I.
    piv=rref(transpose(A))[1]; B=[A[i] for i in piv]; Bi=inv(B)
    J=zero(len(piv),len(A))
    for i in range(len(piv)):
        for j,p in enumerate(piv): J[i][p]=Bi[i][j]
    assert mul(J,A)==eye(len(piv)); return J
def hermdot(v,u): return sum((x.bar()*y for x,y in zip(v,u)),z)

roots=[
 [1,-1-w,1,w,-1-w,w],
 [1,0,0,1+w,0,0],
 [0,1,1+w,0,0,0],
 [1,w,-1-w,w,-1-w,1],
 [1,-1-w,-1-w,-1-w,-1-w,w],
 [1,-1-w,w,w,w,w],
 [0,0,1,0,0,-1],
 [1,w,w,-1-w,1,-1-w],
 [1,-w,0,0,0,0],
 [0,1,0,0,0,-1],
]
roots=[tuple(K.c(x) for x in v) for v in roots]
norms=[hermdot(v,v) for v in roots]
def reflection(v):
    n=hermdot(v,v)
    return [[K(i==j)-2*v[i]*v[j].bar()/n for j in range(6)] for i in range(6)]
gens=[reflection(v) for v in roots]
intervals=[(1,8),(1,18),(2,8),(3,8),(4,8),(5,6),(5,8),(7,8),
 (9,10),(9,12),(9,16),(9,17),(9,18),(11,12),(13,14),(13,16),(15,16)]
def serialize(A): return [[x.pair() for x in row] for row in A]

def main():
    start=time.time(); report={}
    assert all(mul(s,s)==eye(6) for s in gens)
    report['root_norms']=[str(x.a) for x in norms]
    report['root_span_rank']=rank(transpose(roots)); assert report['root_span_rank']==6
    adj=[[j for j,u in enumerate(roots) if j!=i and hermdot(v,u)] for i,v in enumerate(roots)]
    seen={0}; todo=[0]
    while todo:
        for j in adj[todo.pop()]:
            if j not in seen: seen.add(j); todo.append(j)
    assert len(seen)==10
    report['nonorthogonality_graph_connected']=True

    # Faithful action on the orbit of one norm-2 root.
    orbit=[roots[1]]; lookup={roots[1]:0}; pos=0
    while pos<len(orbit):
        v=orbit[pos]; pos+=1
        for root,norm in zip(roots,norms):
            c=2*hermdot(root,v)/norm
            v2=tuple(x-c*y for x,y in zip(v,root))
            if v2 not in lookup: lookup[v2]=len(orbit); orbit.append(v2)
        assert len(orbit)<10000
    report['root_orbit_size']=len(orbit); assert len(orbit)==756
    report['root_orbit_span_rank']=rank(transpose(orbit)); assert report['root_orbit_span_rank']==6
    print('orbit 756 completed',flush=True)
    import sympy, sys
    from sympy.combinatorics import Permutation, PermutationGroup
    report['python_version']=sys.version.split()[0]
    report['sympy_version']=sympy.__version__
    perms=[]
    for root,norm in zip(roots,norms):
        perm=[]
        for v in orbit:
            c=2*hermdot(root,v)/norm
            v2=tuple(x-c*y for x,y in zip(v,root)); perm.append(lookup[v2])
        perms.append(Permutation(perm))
    group=PermutationGroup(perms)
    report['group_order']=int(group.order()); assert report['group_order']==39191040
    report['schreier_sims_base']=[int(i) for i in group.base]
    report['basic_orbit_sizes']=[len(orb) for orb in group.basic_orbits]
    from math import prod
    assert prod(report['basic_orbit_sizes'])==report['group_order']
    report['scalar_membership']={}
    for unit in [o,-o,w,-w,w*w,-w*w]:
        perm=Permutation([lookup[tuple(unit*x for x in v)] for v in orbit])
        report['scalar_membership'][str(unit)]=bool(group.contains(perm))
    assert all(report['scalar_membership'].values())
    print('order and scalar units checked',flush=True)

    # Cocycle scalar vectors x_1,...,x_20.
    assert len(intervals)==20-3 and len(set(intervals))==len(intervals)
    assert all(2 <= b-a+1 <= 18 for a,b in intervals)
    assert all(b<c or d<a or (a<=c and d<=b) or (c<=a and b<=d)
               for a,b in intervals for c,d in intervals)
    report['laminar_maximal_interval_system']=True
    vr=[v for v in roots for _ in range(2)]; gs=[s for s in gens for _ in range(2)]
    pref=eye(6); relcols=[]
    for v,s in zip(vr,gs):
        relcols.append(mv(pref,v)); pref=mul(pref,s)
    assert pref==eye(6)
    C=transpose(relcols); Z=null(C)
    B=[[-2*x.bar()/hermdot(v,v) for x in v] for v in vr]
    assert iszero(mul(C,B)); assert rank(B)==6
    report['relation_rank']=rank(C); report['cocycle_dimension']=len(Z[0]); report['coboundary_rank']=rank(B)
    assert report['relation_rank']==6 and report['cocycle_dimension']==14
    comb=hcat(B,Z); piv=rref(comb)[1]; assert piv[:6]==list(range(6)) and len(piv)==14
    Q=cols(comb,piv[6:]); E=hcat(B,Q); J=rowbasis_inverse(E); PJ=J[6:]
    assert iszero(mul(PJ,B)) and mul(PJ,Q)==eye(8)
    report['quotient_dimension']=8
    report['quotient_basis_scalar_cocycles']=serialize(Q)
    logs=[]; returns=[]
    for a,b in intervals:
        a-=1; b-=1
        c=eye(6); H=zero(6,20)
        for i in range(a,b+1):
            v=mv(c,vr[i])
            for j in range(6): H[j][i]=v[j]
            c=mul(c,gs[i])
        if c==eye(6): k=1; Hk=H
        else:
            assert mul(c,c)==eye(6); k=2; Hk=mul(add(eye(6),c),H)
            assert any(mul(c,gs[i])!=mul(gs[i],c) for i in range(a,b+1))
        returns.append(k)
        M=eye(20)
        for i in range(a,b+1):
            v=vr[i]; d=[2*x.bar()/hermdot(v,v) for x in v]
            row=mul([d],Hk)[0]
            M[i]=[x+y for x,y in zip(M[i],row)]
        assert iszero(mul(C,mul(M,Z)))
        assert mul(M,B)==B
        T=mul(PJ,mul(M,Q)); N=sub(T,eye(8))
        assert iszero(mul(N,N)); logs.append(N)
    report['return_powers']=returns
    report['log_ranks']=[rank(N) for N in logs]
    assert report['log_ranks']==[4,1,3,3,2,1,2,1,1,2,4,4,4,1,1,2,1]
    assert all(iszero(mul(N,M)) for N in logs for M in logs)
    report['all_pairwise_products_zero']=True
    report['common_image_dimension']=rank(hcat(*logs)); assert report['common_image_dimension']==4
    S=zero(8,8)
    for N in logs: S=add(S,N)
    report['sum_log_rank']=rank(S); assert report['sum_log_rank']==4
    flat=[sum(N,[]) for N in logs]
    report['K_span_rank']=rank(flat); assert report['K_span_rank']==16
    qflat=[[K(t) for x in row for t in [x.a,x.b]] for row in flat]
    report['Q_span_rank']=rank(qflat); assert report['Q_span_rank']==16
    logrows=rref(transpose(flat))[1]
    report['independent_log_indices']=[i+1 for i in logrows]
    independent=[flat[i] for i in logrows]
    entrycols=rref(independent)[1]
    minor=cols(independent,entrycols); minor_det=det(minor)
    assert minor_det
    report['span_minor']={'matrix_rows':report['independent_log_indices'],
                         'entries_row_column_1_based':[[i//8+1,i%8+1] for i in entrycols],
                         'determinant':minor_det.pair()}
    report['logarithms']= [serialize(N) for N in logs]
    report['elapsed_seconds']=round(time.time()-start,3)
    p=Path(__file__).with_name('g34_certificate.json'); p.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['quotient_basis_scalar_cocycles','logarithms']},indent=2))

if __name__=='__main__': main()
