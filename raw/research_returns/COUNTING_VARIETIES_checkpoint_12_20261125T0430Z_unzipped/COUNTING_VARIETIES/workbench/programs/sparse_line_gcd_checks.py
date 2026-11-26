#!/usr/bin/env python3
"""Finite checks of line-gcd cofactor interpolation with high-degree other rows.
Original stdlib-only code. This is evidence, not a proof.
"""
from itertools import product
from math import comb,prod
import json
from sparse_presentation_checks import clean,multiply,power,ev,scalar,homogeneous_monomials,rank


def trim(a,p):
    a=[v%p for v in a]
    while a and not a[-1]:a.pop()
    return a


def plus(a,b,p):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))],p)


def times(a,b,p):
    c=[0]*max(0,len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return trim(c,p)


def division(a,b,p):
    a=trim(a,p);b=trim(b,p)
    assert b
    q=[0]*max(0,len(a)-len(b)+1)
    inv=pow(b[-1],-1,p)
    while a and len(a)>=len(b):
        k=len(a)-len(b);c=a[-1]*inv%p;q[k]=c
        for j,v in enumerate(b):a[j+k]=(a[j+k]-c*v)%p
        a=trim(a,p)
    return trim(q,p),a


def gcd(a,b,p):
    a=trim(a,p);b=trim(b,p)
    while b:a,b=b,division(a,b,p)[1]
    return [v*pow(a[-1],-1,p)%p for v in a] if a else []


def modpower(a,e,m,p):
    out=[1]
    while e:
        if e&1:out=division(times(out,a,p),m,p)[1]
        e//=2
        if e:a=division(times(a,a,p),m,p)[1]
    return out


def line_restrict(f,a,v,p,modulus=None):
    out=[]
    for ex,c in f.items():
        term=[c]
        for e,x,y in zip(ex,a,v):
            if modulus is None:
                fac=[comb(e,k)*pow(x,e-k,p)*pow(y,k,p)%p for k in range(e+1)]
            else:fac=modpower([x,y],e,modulus,p)
            term=times(term,fac,p)
            if modulus is not None:term=division(term,modulus,p)[1]
        out=plus(out,term,p)
        if modulus is not None:out=division(out,modulus,p)[1]
    return out


def cofactor_value(forms,j,a,z,p):
    v=tuple(y-x for x,y in zip(a,z))
    q=line_restrict(forms[j],a,v,p)
    assert q and q[0]
    d=q
    for i,f in enumerate(forms):
        if i!=j:d=gcd(d,line_restrict(f,a,v,p,q),p)
    quotient,remainder=division(q,d,p)
    assert not remainder and quotient[0]
    return sum(quotient)*pow(quotient[0],-1,p)%p


def interpolate(forms,j,a,B,p):
    n=len(a)-1
    exps=[]
    for k in range(B+1):exps.extend(homogeneous_monomials(n,k))
    pts=[(1,)+e for e in exps]
    values=[cofactor_value(forms,j,a,z,p) for z in pts]
    matrix=[[prod(pow(x,e,p) for x,e in zip(z[1:],m))%p for m in exps]+[val]
            for z,val in zip(pts,values)]
    reduced,piv=rank(matrix,p,len(exps))
    assert len(piv)==len(exps)
    return clean({(B-sum(m),)+m:row[-1] for m,row in zip(exps,reduced)},p)


def translated_scalar(f,h,a,p):
    n=len(a)
    numerator=multiply(power(f,p-1,p,n),h,p)
    c=ev(h,a,p)
    ans=0
    for ex,v in numerator.items():
        if any(e<p-1 for e in ex[1:]):continue
        ans+=v*prod(comb(e,p-1)*pow(x,e-p+1,p) for e,x in zip(ex[1:],a[1:]))
    return ans*pow(c,-p,p)%p


def run():
    out=[];queries=0;interpolations=0
    for p in (2,3,5,7):
        if p==2:g={(0,2,1):1,(0,1,2):1,(3,0,0):1}
        else:g={(0,2,1):1,(3,0,0):-1,(1,0,2):-1}
        g=clean(g,p)
        for B,h in ((1,{(1,0,0):1,(0,1,0):1,(0,0,1):1}),
                    (2,{(2,0,0):1,(0,1,1):1})):
            h=clean(h,p);E=p**30+1
            rows=((1,1,0),(0,1,1),(1,1,1))
            high=[]
            for row in rows:
                hi={tuple(E if i==j else 0 for i in range(3)):c for j,c in enumerate(row) if c}
                high.append(multiply(g,hi,p))
            forms=[multiply(g,h,p)]+high
            points=[(1,)+z for z in product(range(p),repeat=2)]
            a=next(z for z in reversed(points) if ev(forms[0],z,p))
            for z in points:
                actual=cofactor_value(forms,0,a,z,p)
                expected=ev(h,z,p)*pow(ev(h,a,p),-1,p)%p
                assert actual==expected,(p,B,a,z,actual,expected)
                queries+=1
            if p>B:
                recovered=interpolate(forms,0,a,B,p)
                scale=pow(ev(h,a,p),-1,p)
                assert recovered==clean({e:c*scale for e,c in h.items()},p)
                interpolations+=1
            got=translated_scalar(forms[0],h,a,p)
            assert got==scalar(g,p,3),(p,B,got,scalar(g,p,3))
            out.append({'p':p,'cofactor_degree':B,'large_other_degree':E,
                        'anchor':a,'scalar':got,'queries':len(points)})
    return {'status':'passed','oracle_queries':queries,'dense_interpolations':interpolations,
            'translated_scalar_checks':len(out),'cases':out}


if __name__=='__main__':print(json.dumps(run(),indent=2))
