#!/usr/bin/env python3
"""Original finite checks of rank-one Frobenius digit deflation."""
from random import Random
import json
from sparse_presentation_checks import clean,multiply,homogeneous_monomials,scalar,scalar_from_multiples


def deflate(f,p,e):
    P=p**e
    matrix={}
    for a,c in f.items():
        r=tuple(v%P for v in a);q=tuple(v//P for v in a)
        matrix[(r,q)]=c
    rows=sorted({r for r,q in matrix});cols=sorted({q for r,q in matrix})
    if len(rows)*len(cols)!=len(f):return None
    r0=rows[0];q0=cols[0];pivot=matrix.get((r0,q0),0)
    if not pivot:return None
    U={r:matrix.get((r,q0),0) for r in rows}
    V={q:matrix.get((r0,q),0)*pow(pivot,-1,p)%p for q in cols}
    if not all(U[r]*V[q]%p==c for (r,q),c in matrix.items()):return None
    if not any(sum(q)>0 for q in V):return None
    out=multiply(U,V,p)
    n=len(r0);D=sum(next(iter(f)));Dnew=sum(next(iter(out)))
    assert len(out)<=len(f)
    assert (D-Dnew)*(n+2)>=D
    return out


def repeat(f,p):
    steps=0
    while True:
        maxexp=max(max(a) for a in f)
        e=1;found=None
        while p**e<=maxexp:
            found=deflate(f,p,e)
            if found is not None:break
            e+=1
        if found is None:return f,steps
        f=found;steps+=1


def run():
    rng=Random(194902);tests=0;rejects=0;lists=[]
    for p in (2,3,5):
        g=clean({(0,2,1):1,(0,1,2):1,(3,0,0):1} if p==2 else
                {(0,2,1):1,(3,0,0):-1,(1,0,2):-1},p)
        for e in (2,3,5):
            P=p**e
            for b in (1,2,3):
                ms=list(homogeneous_monomials(3,b))
                for _ in range(4):
                    V=clean({m:rng.randrange(p) for m in rng.sample(ms,min(4,len(ms)))},p)
                    if not V:V={ms[0]:1}
                    VP={tuple(P*a for a in m):c for m,c in V.items()}
                    f=multiply(g,VP,p)
                    out=deflate(f,p,e)
                    assert out is not None
                    # Pivot normalization leaves the product U*V unchanged over F_p.
                    assert out==multiply(g,V,p)
                    tests+=1
            f={(P+1,0,0):1,(0,P+1,0):1}
            assert deflate(f,p,e) is None
            rejects+=1
        for k in (3,8,30):
            P=p**k;rows=((1,1,0),(0,1,1),(1,1,1));forms=[];steps=[]
            for row in rows:
                V={tuple(P if i==j else 0 for i in range(3)):c
                   for j,c in enumerate(row) if c}
                out,count=repeat(multiply(g,V,p),p)
                forms.append(out);steps.append(count)
            got=scalar_from_multiples(forms,p,3)
            assert got==scalar(g,p,3)
            lists.append({'p':p,'initial_power_exponent':P,'steps':steps,'scalar':got})
    return {'status':'passed','exact_deflations':tests,'nonrank_rejections':rejects,
            'saturated_list_scalar_checks':lists}


if __name__=='__main__':print(json.dumps(run(),indent=2))
