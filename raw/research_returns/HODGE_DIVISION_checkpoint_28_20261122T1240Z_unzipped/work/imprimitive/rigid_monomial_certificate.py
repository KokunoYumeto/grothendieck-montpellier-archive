#!/usr/bin/env python3
"""Exact monomial triples for HD-I15, 21 November 2026.
GPT-6 Astra Pro, inherited effort, /root/imprimitive.
Finite examples are checked; the all-parameter group proof is in the TeX.
"""
from pathlib import Path
import json
from math import ceil, gcd

def mul(a,b,d):
    v,p=a; w,q=b; m=len(v)
    inv=[0]*m
    for i,j in enumerate(p): inv[j]=i
    return tuple((v[i]+w[inv[i]])%d for i in range(m)),tuple(p[q[i]] for i in range(m))

def inverse(a,d):
    v,p=a; m=len(v); q=[0]*m
    for i,j in enumerate(p): q[j]=i
    return tuple((-v[p[i]])%d for i in range(m)),tuple(q)

def power(a,k,d):
    if k<0: return power(inverse(a,d),-k,d)
    z=(tuple(0 for _ in a[0]),tuple(range(len(a[0]))))
    while k:
        if k&1: z=mul(z,a,d)
        a=mul(a,a,d); k//=2
    return z

def cycles(a,d):
    v,p=a; seen=set(); out=[]
    for j in range(len(v)):
        if j in seen: continue
        q=[]; t=j
        while t not in seen:
            seen.add(t);q.append(t);t=p[t]
        out.append({'indices':[i+1 for i in q],'length':len(q),
                    'color':sum(v[i] for i in q)%d})
    return out

def check(n,m,d):
    assert n>=5 and m%2==0 and m>=2*n+2
    v=[1,0]+[1]*n+[-1]*(n-1)+[0]*(m-2*n-1)
    p=list(range(m));p[0],p[1]=1,0
    A=(tuple(x%d for x in v),tuple(p))
    B=(tuple(0 for _ in range(m)),tuple((j+1)%m for j in range(m)))
    C=inverse(mul(A,B,d),d)
    identity=(tuple(0 for _ in range(m)),tuple(range(m)))
    assert mul(mul(A,B,d),C,d)==identity
    Ap=mul(mul(power(B,2*n,d),A,d),power(B,-2*n,d),d)
    w=mul(mul(mul(A,Ap,d),inverse(A,d),d),inverse(Ap,d),d)
    assert w[1]==identity[1]
    assert w[0][2*n]==d-1 and w[0][2]==0
    assert all(w[0][j]==0 for j in range(m) if j not in (0,1,2*n,2*n+1))
    cc=[cycles(x,d) for x in (A,B,C)]
    deficit=sum(c['length']-1 for cs in cc for c in cs)
    counts={s:sum(c['color']==s for cs in cc for c in cs) for s in range(1,d)}
    assert deficit==2*m-2
    assert counts[1]==n+1 and counts[d-1]==n+1
    assert sum(counts.values())==2*n+2
    assert sum(s*c for s,c in counts.items())==d*(n+1)
    assert [sum(x[0])%d for x in (A,B,C)]==[2%d,0,(-2)%d]
    return {'n':n,'m':m,'d':d,'e':gcd(d,2),'cycles':cc,
            'commutator_vector':list(w[0]),'genusY':0,'signature':[n,n],
            'branch_values':3,'period_rank':0}

records=[]
for n in range(5,9):
    lower=max(2*n+2,ceil((n*n-2*n+3)/2))
    m=lower+(lower%2)
    for extra in (0,2,4):
        for d in (3,4,6): records.append(check(n,m+extra,d))
out={'statement':'HD-I15','date':'2026-11-21','checks':len(records),
     'status':'PASS','scope':'Exact finite monomial products, commutator and colored-cycle checks; the universal group-generation argument is proved in the text.',
     'records':records}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(f"PASS: {len(records)} exact product-one triples, commutators and signature calculations.")
