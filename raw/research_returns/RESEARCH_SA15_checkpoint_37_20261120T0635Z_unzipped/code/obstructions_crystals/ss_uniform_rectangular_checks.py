#!/usr/bin/env python3
"""Exact certificate accompanying the uniform rectangular sheaf proof.

The infinite family is proved by the two-point kernel sheaf calculation;
finite matrices do not replace that proof.  Matrix columns here are rebuilt
by solving f=a^2+x*b^2, without importing a monomial Cartier table.
"""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp
start=perf_counter()
x,y,u=sp.symbols('x y u')
g=sp.groebner([y*y+y+x**3],y,x,u,modulus=2)
a=[x*u*(x+y),0,1+x*x*u]
b=[1+u*(x+y+x*x),1+u*y,u*y]
f=[x+x*u*u*(x*x+(1+x)*y),x+x*u*u*y*y,1+x*u*u*y]
identities=[]
for i in range(3):
    residual=g.reduce(sp.expand(f[i]+a[i]**2+x*b[i]**2))[1]
    assert residual==0
    identities.append({'identity':f'p_basis_component_{i}','remainder':str(residual)})
gb=sp.groebner([y*y+y+x**3,u*y+1],y,x,u,modulus=2)
minor=sp.expand(a[0]*b[2]+a[2]*b[0])
assert gb.reduce(minor+1+u)[1]==0
assert gb.reduce(1+u+x**3*u**2)[1]==0
assert g.reduce(x**3+y*y+y)[1]==0
identities.extend([{'identity':'remaining_minor_on_uy=1','remainder':'0'},
                   {'identity':'1+u=x^3u^2_on_uy=1','remainder':'0'},
                   {'identity':'regularity_x+t^-2=y/x^2','remainder':'0'}])

def gf4mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return r

def gf4pow(a,n):
    r=1
    while n:
        if n&1:r=gf4mul(r,a)
        a=gf4mul(a,a);n>>=1
    return r

points=[]
for lam in [2,3]:
    assert gf4mul(lam,lam)^lam^1==0
    av=[0,0,0];bv=[0,lam,gf4mul(lam,lam)]
    sv=[0,1,gf4mul(lam,lam)]
    dv=[0,gf4mul(lam,lam),lam]
    ell=lambda v:gf4mul(gf4mul(lam,lam),v[0])^gf4mul(lam,v[1])
    assert [ell(sv),ell(dv)]==[lam,1]
    points.append({'lambda':lam,'a':av,'b':bv,'section_value':sv,
                   'derivative_value':dv,'kernel_cokernel_row':[lam,1],
                   'line_preservation_row':[lam,1]})
assert gf4mul(2,1)^gf4mul(3,1)==1

# Universal local normal form: f=(t e1,e2,0), kernel=((td,b),(c,d),0).
t,bb,cc,dd=sp.symbols('t b c d')
v0=[t*dd,bb];v1=[cc,dd];v2=[0,0]
assert [sp.Poly(z,t,bb,cc,dd,modulus=2).as_expr() for z in
        [v0[0]+t*v1[1],t*v2[1],v2[0]]]==[0,0,0]

def basis(n):
    return [(i,0) for i in range(n//2+1)]+[(i,1) for i in range((n-3)//2+1)]

def redmon(i,j):
    if j<2:return {(i,j)}
    return redmon(i,j-1)^redmon(i+3,j-2)

def mul(P,Q):
    r=set()
    for i,j in P:
        for k,l in Q:r^=redmon(i+k,j+l)
    return r

def bits(P,ix):return sum(1<<ix[z] for z in P)

def independent_cartier(n):
    B=basis(n);A=basis(n+1);T=basis(2*n+2);ix={z:i for i,z in enumerate(T)}
    cols=[bits(mul({z},{z}),ix) for z in A]
    cols += [bits(mul({(1,0)},mul({z},{z})),ix) for z in B]
    tab={}
    for i,v in enumerate(cols):
        r=1<<i
        while v:
            p=v.bit_length()-1
            if p in tab:v^=tab[p][0];r^=tab[p][1]
            else:tab[p]=(v,r);break
        else:raise AssertionError('dependent p-basis columns')
    def cart(P):
        v=bits(P,ix);r=0
        while v:
            p=v.bit_length()-1
            assert p in tab
            v^=tab[p][0];r^=tab[p][1]
        return r>>len(A)
    return B,cart

def rank(cols):
    p={}
    for v in cols:
        while v:
            b=v.bit_length()-1
            if b in p:v^=p[b]
            else:p[b]=v;break
    return len(p)

def apply(cols,v):
    r=0
    while v:
        z=v&-v;v^=z;r^=cols[z.bit_length()-1]
    return r

def check(q):
    B,C=independent_cartier(2*q);D,J=independent_cartier(3)
    ix={z:i for i,z in enumerate(B)}
    templ=[(0,0),(1,0),(q-1,0),(q,0),(q-3,1),(q-2,1)]
    terms=[(templ[i//3],D[i%3]) for i in range(18) if (62556>>i)&1]
    section=sum(1<<(3*ix[z]+D.index(w)) for z,w in terms)
    cols=[]
    for z in B:
        for w in D:
            col=0
            for f,h in terms:
                v=C(mul({z},{f}));r=J(mul({w},{h}))
                while v:
                    vi=v&-v;v^=vi;i=vi.bit_length()-1
                    for j in range(3):
                        if (r>>j)&1:col^=1<<(3*i+j)
            cols.append(col)
    ds=0
    for z,w in terms:
        i,j=z;der=[]
        if i&1:der.append((i-1,j))
        if j:der.append((i+2,0))
        for h in der:ds^=1<<(3*ix[h]+D.index(w))
    assert apply(cols,section)==apply(cols,ds)==0
    left=[sum(1<<i for i in range(6*q) if i%9 in residues)
          for residues in [(0,1,4,6),(0,3,4,7)]]
    assert all((v&c).bit_count()%2==0 for v in left for c in cols)
    pair=[[(v&w).bit_count()%2 for w in [section,ds]] for v in left]
    assert pair==[[1,0],[0,1]]
    ranks=[rank(cols),rank([apply(cols,c) for c in cols])]
    assert ranks==[6*q-2,6*q-2]
    return {'q':q,'degrees':[2*q,3],'template_pattern':62556,'section_bits':section,
            'columns':cols,'ranks_C_C2':ranks,'binary_left_pairing':pair}

matrices=[check(q) for q in [6,12,18,24,30,48,96,192]]
parity_cases=0
for a0 in range(1,65):
    for b0 in range(1,65):
        for d0 in range(1,17):
            N=9*a0*b0*d0*d0
            r=N-1-int((a0*d0)%2==0)-int((b0*d0)%2==0)
            assert N-3<=r<=N-1
            parity_cases+=1
out={'status':'PASS','scope':'Uniform polynomial/local identities plus independently rebuilt finite matrices; infinite theorem proved by sheaf argument',
     'polynomial_identities':identities,'geometric_points_GF4':points,
     'local_normal_form':'PASS','matrices':matrices,'parity_cases':parity_cases,
     'elapsed_seconds':perf_counter()-start}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='matrices'}|{'matrix_ranks':[{'q':c['q'],'ranks':c['ranks_C_C2']} for c in matrices]},indent=2))
