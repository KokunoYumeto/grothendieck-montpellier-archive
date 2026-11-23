"""Finite exact certificate for ALP-LIFT-19; not a proof of global theta-image saturation."""
from itertools import product
from fractions import Fraction
from math import factorial

def det(a,p):
    n=len(a)
    b=[list(r) for r in a]
    z=1
    for i in range(n):
        k=next((k for k in range(i,n) if b[k][i]%p),None)
        if k is None:return 0
        if k!=i:b[i],b[k]=b[k],b[i];z=-z
        v=b[i][i]%p;z=z*v%p
        iv=pow(v,-1,p)
        for k in range(i+1,n):
            t=b[k][i]*iv%p
            for c in range(i,n):b[k][c]=(b[k][c]-t*b[i][c])%p
    return z%p

def inv(a,p):
    n=len(a);b=[list(r)+[int(i==j) for j in range(n)] for i,r in enumerate(a)]
    for i in range(n):
        k=next(k for k in range(i,n) if b[k][i]%p)
        b[i],b[k]=b[k],b[i]
        t=pow(b[i][i]%p,-1,p)
        b[i]=[x*t%p for x in b[i]]
        for k in range(n):
            if k!=i:
                t=b[k][i]
                b[k]=[(x-t*y)%p for x,y in zip(b[k],b[i])]
    return tuple(tuple(row[n:]) for row in b)

def mm(a,b,p):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))%p for j in range(len(b[0]))) for i in range(len(a)))

def mv(a,x,p):
    return tuple(sum(ai*xi for ai,xi in zip(row,x))%p for row in a)

def line(x,p):
    t=pow(next(a for a in x if a%p),-1,p)
    return tuple(a*t%p for a in x)

def eta(x,p):
    assert x%p
    return 1 if pow(x,(p-1)//2,p)==1 else -1

def projective_lines(p):
    return sorted({line(x,p) for x in product(range(p),repeat=3) if any(x)})

def section(l,p):
    # g_l^{-1} takes e1 to the selected vector of l.
    if l[2]==0 and l[1]!=0:
        s=l[0]*pow(l[1],-1,p)%p
        return ((0,1,0),(1,-s%p,0),(0,0,1))
    if l==(1,0,0):return ((1,0,0),(0,1,0),(0,0,1))
    es=[(1,0,0),(0,1,0),(0,0,1)]
    for y in es:
        for z in es:
            b=tuple(tuple(v[i] for v in (l,y,z)) for i in range(3))
            if det(b,p):return inv(b,p)
    raise AssertionError

def concrete_column(p,generic):
    ls=projective_lines(p)
    gs={l:section(l,p) for l in ls}
    gis={l:inv(g,p) for l,g in gs.items()}
    fs={}
    for l in ls:
        if generic and l[2]==0 and l[1]!=0:
            s=l[0]*pow(l[1],-1,p)%p
            fs[l]=2*s%(2*p)
        elif not generic and l==(1,0,0):fs[l]=0
        else:fs[l]=None
    coeff=[0]*p
    total=0
    for x,y,z,c in product(range(p),range(p),range(p),range(1,p)):
        h=((1,x,y),(0,1,z),(0,0,c));hi=inv(h,p)
        lam=(-2*x if generic else 0)+(p if eta(c,p)<0 else 0)
        for l in ls:
            l2=line(mv(hi,l,p),p)
            a=mm(mm(gs[l],h,p),gis[l2],p)
            assert a[1][0]==a[2][0]==0
            character=eta(det(a,p)*pow(a[0][0],-1,p)%p,p)
            lhs=None if fs[l2] is None else (fs[l2]+(p if character<0 else 0))%(2*p)
            rhs=None if fs[l] is None else (fs[l]+lam)%(2*p)
            assert lhs==rhs,(p,generic,h,l,lhs,rhs)
        # Exact trace of lambda projector via fixed lines; eta(det h) cancels.
        for l in ls:
            hl=mv(h,l,p)
            if line(hl,p)==l:
                pivot=next(i for i,v in enumerate(l) if v)
                a=hl[pivot]*pow(l[pivot],-1,p)%p
                coeff[x if generic else 0]+=eta(a,p)
        total+=1
    assert all(coeff[r]==coeff[-1] for r in range(1,p))
    multiplicity=Fraction(coeff[0]-coeff[-1],total)
    assert multiplicity==(1 if generic else 2),(p,generic,multiplicity,coeff)
    support=sum(v is not None for v in fs.values())
    assert support==(p if generic else 1)
    assert Fraction(support,len(ls))==Fraction(p if generic else 1,p*p+p+1)
    return total*len(ls)

def transport_count(k,j,t):
    qorder=[("A",i) for i in range(k)]
    for s in range(j):
        qorder += [("L",s)]+[("T",(s,i)) for i in range(t)]
    porder=[("A",i) for i in range(k)]+[("L",s) for s in range(j)]
    for s in range(j):porder += [("T",(s,i)) for i in range(t)]
    def qb(x):return 0 if x[0]=="A" else (x[1]+1 if x[0]=="L" else x[1][0]+1)
    def pb(x):return 0 if x[0]!="T" else x[1][0]+1
    excluded=0
    for a in porder:
        for b in porder:
            if pb(a)<pb(b) and qb(a)>qb(b):excluded+=1
    assert excluded==t*j*(j-1)//2
    assert len(qorder)==len(porder)==k+j*(t+1)
    assert set(qorder)==set(porder)

def val(n,p=11):
    z=0
    while n%p==0:z+=1;n//=p
    return z

def order(q,p=11):
    for h in range(1,p):
        if pow(q,h,p)==1:return h
    raise AssertionError

def gaussian_index(q,k,d,j):
    top=1
    for s in range(1,k+j*d+1):top*=q**s-1
    bot=1
    for s in range(1,k+1):bot*=q**s-1
    for s in range(1,d+1):bot*=(q**s-1)**j
    assert top%bot==0
    return top//bot

checks=sum(concrete_column(p,g) for p in (3,5) for g in (False,True))
for k,j,t in product(range(1,6),range(1,5),range(1,6)):
    transport_count(k,j,t)
for q,k,d,j in product((3,5,29,113,281,337),range(1,9),range(2,9),range(4)):
    h=order(q);c=val(q**h-1)
    def D(n):r=n//h;return c*r+val(factorial(r))
    index=gaussian_index(q,k,d,j)
    assert val(index)==D(k+j*d)-D(k)-j*D(d)
print("PASS: exact lambda^{-1} covariance, generic multiplicity1 / omitted-root multiplicity2, primitive support and norm for GL3(F3/F5);",checks,"matrix-line checks.")
print("PASS: 100 transport root-count cases and 1344 exact Gaussian-index 11-valuations.")

