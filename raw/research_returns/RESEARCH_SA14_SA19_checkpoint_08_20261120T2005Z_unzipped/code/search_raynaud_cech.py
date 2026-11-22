"""Exact finite-field Cech search on explicit Artin-Schreier Tango curves.

Curve y^p-y=x^(p*r-1); infinity uniformizer t=y/x^r.  Put D=(r*(p-1)-2)infinity.
The extension of O(D) by O has Cech class t^-1: its pth power is
x minus a function vanishing to order p*deg(D).  For Sym^n(E)^vee(c infinity),
unknown coefficient a_i has pole order at most c+i.  Regularity on the
infinity chart gives the explicit linear equations implemented below.
This computes Hom sections, not very ampleness on the resulting surface.
"""
from pathlib import Path
from math import comb
from functools import lru_cache
import json,time

def mul(a,b,p,N):
    out=[0]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b[:N+1-i]):out[i+j]=(out[i+j]+x*y)%p
    return out

def power(a,e,p,N):
    if e<0:
        inv=[1]+[0]*N
        for i in range(1,N+1):inv[i]=-sum(a[j]*inv[i-j] for j in range(1,min(i,len(a)-1)+1))%p
        return power(inv,-e,p,N)
    out=[1]+[0]*N
    while e:
        if e&1:out=mul(out,a,p,N)
        a=mul(a,a,p,N);e//=2
    return out

def rank_sparse(rows,p):
    basis={}
    for row in rows:
        row={j:v%p for j,v in row.items() if v%p}
        while row:
            pivot=min(row)
            if pivot not in basis:
                z=pow(row[pivot],-1,p);basis[pivot]={j:v*z%p for j,v in row.items()};break
            c=row[pivot]
            for j,v in basis[pivot].items():
                value=(row.get(j,0)-c*v)%p
                if value:row[j]=value
                elif j in row:del row[j]
    return len(basis)

@lru_cache(None)
def hom_dimension(p,r,n,c):
    D=r*(p-1)-2;m=p*r-1;q=D+1;T=p*q+1
    if n<0:return dict(dimension=0,variables=0,equations=0)
    # Pole bound c+i follows successively from the triangular transition matrix.
    variables=[(i,a,b) for i in range(n+1) for b in range(p) for a in range(max(-1,(c+i-m*b)//p)+1)]
    if not variables:return dict(dimension=0,variables=0,equations=0)
    N=max(0,(D*n+n+1)//T+1)
    w=[1]+[0]*N
    for _ in range(N+1):w=[1]+power(w,-q,p,N)[:N]
    wp={a+r*b:power(w,a+r*b,p,N) for i,a,b in variables}
    equations={}
    for col,(i,a,b) in enumerate(variables):
        pole=p*a+m*b
        for j in range(i,n+1):
            scalar=comb(j,i)*(-1)**(j-i)%p
            if not scalar:continue
            for k,value in enumerate(wp[a+r*b]):
                exponent=-pole-(j-i)+T*k
                if value and exponent<D*j-c:
                    row=equations.setdefault((j,exponent),{})
                    row[col]=(row.get(col,0)+scalar*value)%p
    rank=rank_sparse(equations.values(),p)
    return dict(dimension=len(variables)-rank,variables=len(variables),equations=len(equations),rank=rank,series_precision=N)

def raynaud(p,ell,r,a,b):
    D=r*(p-1)-2
    assert D>0 and D%ell==0 and (p+1)%ell==0
    d=(p+1)//ell;q,s=divmod(a,ell);summands=[]
    for i in range(ell):
        n=i*d+q-(1 if i<s else 2)
        c=(i*p-b-ell)*(D//ell)
        if n<0:continue
        result=hom_dimension(p,r,n,c)
        summands.append(dict(i=i,n=n,c=c,**result))
    return dict(p=p,ell=ell,r=r,base_genus=(p-1)*(p*r-2)//2,D=D,a=a,b=b,h1=sum(x['dimension'] for x in summands),summands=summands)

if __name__=='__main__':
    start=time.monotonic();results=[]
    for p in [2,3,5,7,11,13]:
        for ell in range(2,p+2):
            if (p+1)%ell:continue
            rr=[r for r in range(1,2*ell+3) if r*(p-1)>2 and (r*(p-1)-2)%ell==0]
            for r in rr[:2]:
                for a in range(1,2*ell+1):
                    for b in range(1,4):results.append(raynaud(p,ell,r,a,b))
    known=[x for x in results if x['a']<x['ell'] and x['b']<=x['ell']-x['a']]
    violations=[x for x in known if not x['h1']]
    new=[x for x in results if x['a']>=x['ell'] and x['h1']]
    out=dict(scope=__doc__,seconds=round(time.monotonic()-start,3),cases=len(results),known_nonvanishing_cases=len(known),known_range_failures=violations,nonvanishing_beyond_published_sufficient_range=new,results=results)
    Path(__file__).with_name('search_raynaud_cech_output.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
