#!/usr/bin/env python3
"""Independent exact checks of root finding G-08, not a general certificate."""
from itertools import product
from math import comb
from pathlib import Path
import sympy as sp

def exponents(k,m):
    return sorted((a for a in product(range(m+1),repeat=k) if sum(a)<=m),
                  key=lambda a:(sum(a),a))

def construction(m,k):
    a=k//2;b=k-a
    xx=sp.symbols(f'x0:{k}'); ell=sp.Symbol('ell')
    left=exponents(a,m);right=list(reversed(exponents(b,m)))
    li={u:i for i,u in enumerate(left)}
    ri={v:i+len(left) for i,v in enumerate(right)}
    size=len(left)+len(right)
    A=sp.zeros(size)
    for u in left:
        if sum(u):
            j=max(i for i,z in enumerate(u) if z)
            p=list(u);p[j]-=1
            A[li[tuple(p)],li[u]]=xx[j]
    for v in right:
        if sum(v):
            j=max(i for i,z in enumerate(v) if z)
            p=list(v);p[j]-=1
            A[ri[v],ri[tuple(p)]]=xx[a+j]
    coeff=[];q=0
    for u in left:
        for v in right:
            if sum(u)+sum(v)==m:
                c=sp.Symbol(f'c{len(coeff)}');coeff.append(c)
                A[li[u],ri[v]]=c
                q+=c*sp.prod(x**e for x,e in zip(xx,u+v))
    M=(sp.eye(size)-A).minor_submatrix(size-1,0)
    if (size+1)%2:
        M[0,:]=-M[0,:]
    zero={x:0 for x in xx}
    M=M.applyfunc(lambda e:sp.expand(e+(ell-1)*e.subs(zero)))
    B=comb(m+a,a)+comb(m+b,b)-1
    assert M.rows==B
    return xx,ell,coeff,q,M,B

def det_mod(M,p):
    A=[[int(e)%p for e in M.row(i)] for i in range(M.rows)]
    d=1
    for k in range(len(A)):
        q=next((i for i in range(k,len(A)) if A[i][k]),None)
        if q is None:return 0
        if q!=k:A[k],A[q]=A[q],A[k];d=-d
        pivot=A[k][k];d=d*pivot%p; inv=pow(pivot,-1,p)
        for i in range(k+1,len(A)):
            c=A[i][k]*inv%p
            for j in range(k+1,len(A)):A[i][j]=(A[i][j]-c*A[k][j])%p
    return d%p

lines=[]
for m,k in [(1,2),(2,2),(2,3)]:
    xx,ell,cc,q,M,B=construction(m,k)
    assert sp.expand(M.det(method='domain-ge')-ell**(B-m)*q)==0
    lines.append(f'G-08: exact universal symbolic identity verified for m={m},k={k},B={B}.')
for m,k in [(3,4),(4,4),(2,5)]:
    xx,ell,cc,q,M,B=construction(m,k)
    for j in range(1,6):
        p=101
        sub={c:((i+1)**2+7*j)%p for i,c in enumerate(cc)}
        sub.update({x:(2*i+3*j+1)%p for i,x in enumerate(xx)})
        sub[ell]=j+1
        assert det_mod(M.subs(sub),p)==int((ell**(B-m)*q).subs(sub))%p
    lines.append(f'G-08: five exact F_101 evaluations verified for m={m},k={k},B={B}.')
lines.append('These are independent finite checks; the full proof was read separately.')
print('\n'.join(lines))
Path(__file__).with_name('G08_computation_checks.txt').write_text('\n'.join(lines)+'\n')
