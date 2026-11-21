#!/usr/bin/env python3
"""Exact tuple checks for D-IM-08, without enumerating the full groups."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd
import json

M=12
def mul(g,h,d):
    p,c=g;q,b=h
    return tuple(p[q[j]] for j in range(M)),tuple((b[j]+c[q[j]])%d for j in range(M))
def inv(g,d):
    p,c=g;q=[p.index(j) for j in range(M)]
    return tuple(q),tuple(-c[q[j]]%d for j in range(M))
def power(g,n,d):
    out=(tuple(range(M)),(0,)*M)
    for _ in range(n):out=mul(out,g,d)
    return out
def cycles(g,d):
    p,c=g;seen=set();out=[]
    for j in range(M):
        if j in seen:continue
        inds=[];k=j
        while k not in seen:seen.add(k);inds.append(k);k=p[k]
        out.append((inds,sum(c[k] for k in inds)%d))
    return out
def age(g,d):return sum((F(len(c)-1,2)+F(a,d) for c,a in cycles(g,d)),F())
def fixed(g,d):return sum(a==0 for c,a in cycles(g,d))
def transposition(i,j):
    p=list(range(M));p[i],p[j]=p[j],p[i]
    return tuple(p),(0,)*M
def comm(g,h,d):return mul(mul(mul(g,h,d),inv(g,d),d),inv(h,d),d)

def case(d,e):
    ap=tuple(list(range(1,M))+[0]);ac=[0]*M
    k=7 if e==d else 6;bp=list(range(M));bp[:k]=list(range(1,k))+[0];bc=[0]*M
    bc[0]=1;bc[k-1 if e==d else 1]=-1
    if e<d:ac[-1]=e
    a=ap,tuple(x%d for x in ac);b=tuple(bp),tuple(x%d for x in bc)
    tt=[a,inv(a,d),b,inv(b,d)]
    identity=(tuple(range(M)),(0,)*M);prod=identity
    for x in tt:
        assert sum(x[1])%e==0 and x!=identity
        prod=mul(prod,x,d)
    assert prod==identity
    a0=a[0],(0,)*M;b0=b[0],(0,)*M
    triple=mul(mul(mul(inv(b0,d),a0,d),b0,d),inv(a0,d),d)
    nontrivial=[c for c,col in cycles(triple,d) if len(c)>1]
    assert len(nontrivial)==1 and set(nontrivial[0])=={0,k-1,k}
    # Connected support hypergraph certifies A_12 by the elementary lemma.
    adjacency=[set() for _ in range(M)];cg=triple
    for _ in range(M):
        support=[i for i in range(M) if cg[0][i]!=i]
        for i in support:adjacency[i].update(support)
        cg=mul(mul(a0,cg,d),inv(a0,d),d)
    reached={0}
    while True:
        enlarged=reached|set().union(*(adjacency[i] for i in reached))
        if enlarged==reached:break
        reached=enlarged
    assert len(reached)==M
    c=mul(inv(a,d),b,d)
    if e==d:
        D=power(c,6,d);expected=[6]+[0]*5+[-1]*6;sigma=transposition(1,6)
    else:
        D=power(c,7,d);expected=[7,-7]+[0]*3+[-e]*7;sigma=transposition(0,2)
    assert D[0]==tuple(range(M)) and D[1]==tuple(x%d for x in expected)
    root=comm(D,sigma,d);nz=[x for x in root[1] if x]
    assert len(nz)==2 and sum(nz)%d==0 and gcd(nz[0],d)==1
    # sigma models conjugation by any H-lift; no unproved lift word is used.
    hol=-M+sum((age(g,d) for g in tt),F())
    anti=-M+sum((age(inv(g,d),d) for g in tt),F())
    assert hol==anti==5
    A=sum(len(c)-1 for g in tt for c,col in cycles(g,d))
    R=sum(col!=0 for g in tt for c,col in cycles(g,d))
    h=1-M+F(A,2)
    assert (h,R)==((6,0) if e==d else (5,2))
    graph_mult=M-fixed(a,d)-fixed(b,d)
    assert graph_mult==5
    return {'d':d,'e':e,'m':M,'branch_count':4,'signature':[int(hol),int(anti)],
            'fixed_dimensions':[fixed(a,d),fixed(b,d)],'base_genus':int(h),'cyclic_branch_count':R,
            'diagonal_power':list(D[1]),'primitive_commutator':list(root[1]),
            'projection_three_cycle_support':[i+1 for i in nontrivial[0]],
            'support_hypergraph_connected':True,'graph_natural_multiplicity':graph_mult,
            'source_dimension':1,'exact_period_image_dimension_by_proof':1}

if __name__=='__main__':
    out={'method':__doc__,'cases':[case(d,e) for d in [3,4,6] for e in range(1,d+1) if d%e==0]}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    for c in out['cases']:print({k:c[k] for k in ['d','e','signature','base_genus','cyclic_branch_count','graph_natural_multiplicity','exact_period_image_dimension_by_proof']})
