#!/usr/bin/env python3
"""Exhaustive finite certificates for SA08 B.7 and a coefficient-operation error.

All computations are exact integers modulo 2 or 4.  A degree cutoff does not
replace an infinite claim: the accompanying proof explains why all divided
powers of index >=3 vanish in these finite examples.
"""
from itertools import product
from math import comb, factorial
from time import perf_counter
import json

started = perf_counter()
B = list(product(range(4), range(2), range(4)))
zero = (0, 0, 0)
one = (1, 0, 0)
t = (0, 1, 0)
u = (0, 0, 1)
def add(x,y): return ((x[0]+y[0])%4,(x[1]+y[1])%2,(x[2]+y[2])%4)
def neg(x): return ((-x[0])%4,(-x[1])%2,(-x[2])%4)
def mul(x,y):
    a,b,c=x; d,e,f=y
    return (a*d%4,(a*e+d*b)%2,(a*f+d*c+2*b*e)%4)
def scale(n,x): return (n*x[0]%4,n*x[1]%2,n*x[2]%4)
def powb(x,n):
    y=one
    for _ in range(n): y=mul(y,x)
    return y
def gamma(n,x):
    assert x[0]==0
    if n==0: return one
    if n==1: return x
    if n==2: return (0,0,x[1]**2%4)
    return zero
J=[x for x in B if x[0]==0]
tors=[x for x in B if scale(2,x)==zero]
Jtors=[x for x in J if scale(2,x)==zero]
counts={}
for x,y,z in product(B,repeat=3):
    assert mul(mul(x,y),z)==mul(x,mul(y,z))
    assert mul(x,add(y,z))==add(mul(x,y),mul(x,z))
counts['ring_associativity']=len(B)**3
counts['ring_distributivity']=len(B)**3
for x,y in product(B,repeat=2): assert mul(x,y)==mul(y,x)
counts['ring_commutativity']=len(B)**2
for x in B:
    assert mul(x,one)==x and add(x,neg(x))==zero
for n,x,y in product(range(1,7),J,J):
    rhs=zero
    for j in range(n+1):rhs=add(rhs,mul(gamma(j,x),gamma(n-j,y)))
    assert gamma(n,add(x,y))==rhs
counts['base_pd_addition']=6*len(J)**2
for n,a,x in product(range(1,7),B,J):
    assert gamma(n,mul(a,x))==mul(powb(a,n),gamma(n,x))
counts['base_pd_scalar']=6*len(B)*len(J)
for m,n,x in product(range(1,7),range(1,7),J):
    assert mul(gamma(m,x),gamma(n,x))==scale(comb(m+n,m),gamma(m+n,x))
    coeff=factorial(m*n)//(factorial(m)*factorial(n)**m)
    assert gamma(m,gamma(n,x))==scale(coeff,gamma(m*n,x))
counts['base_pd_product']=36*len(J)
counts['base_pd_iteration']=36*len(J)

# Tensor words for A=k*1+(k/2)*e.  Words containing e have coefficients mod2.
def norm_tensor(d):
    return {w:c%(2 if any(w) else 4) for w,c in d.items()
            if c%(2 if any(w) else 4)}
def delta_basis(bit,nonprimitive):
    if bit==0:return {(0,0):1}
    d={(1,0):1,(0,1):1}
    if nonprimitive:d[(1,1)]=1
    return d
for np in (False,True):
    for bit in (0,1):
        dl={};dr={}
        for (a,b),c in delta_basis(bit,np).items():
            for (a0,a1),d in delta_basis(a,np).items():
                w=(a0,a1,b);dl[w]=dl.get(w,0)+c*d
            for (b0,b1),d in delta_basis(b,np).items():
                w=(a,b0,b1);dr[w]=dr.get(w,0)+c*d
        assert norm_tensor(dl)==norm_tensor(dr)
        d=delta_basis(bit,np)
        assert norm_tensor(d)==norm_tensor({(b,a):c for (a,b),c in d.items()})
        # Applying epsilon to either coordinate leaves precisely the input.
        assert norm_tensor({(b,):c for (a,b),c in d.items() if a==0})=={(bit,):1}
        assert norm_tensor({(a,):c for (a,b),c in d.items() if b==0})=={(bit,):1}
counts['coalgebra_basis_checks']=4

# The nonprimitive coalgebra admits no convolution divided powers.
f_at_one=zero; f_at_e=t
f_squared_at_e=mul(t,t)
assert f_squared_at_e==(0,0,2) and f_squared_at_e!=zero
assert all(scale(2,z)==zero for z in tors)
counts['nonprimitive_obstruction_targets']=len(tors)

# The primitive coalgebra has two natural divided-power structures.
H=list(product(B,tors))
IH=list(product(J,Jtors))
hzero=(zero,zero);hone=(one,zero)
def hadd(x,y):return (add(x[0],y[0]),add(x[1],y[1]))
def hmul(x,y):return (mul(x[0],y[0]),add(mul(x[0],y[1]),mul(y[0],x[1])))
def hscale(n,x):return (scale(n,x[0]),scale(n,x[1]))
def hpow(x,n):
    y=hone
    for _ in range(n):y=hmul(y,x)
    return y
def hgamma(n,x,variant):
    b,z=x
    if n==0:return hone
    if n==1:return x
    tangent=mul(gamma(n-1,b),z)
    if variant:tangent=add(tangent,mul(gamma(n-2,b),mul(z,z)))
    return (gamma(n,b),tangent)
for variant in (False,True):
    for n,x,y in product(range(1,7),IH,IH):
        rhs=hzero
        for j in range(n+1):rhs=hadd(rhs,hmul(hgamma(j,x,variant),hgamma(n-j,y,variant)))
        assert hgamma(n,hadd(x,y),variant)==rhs
    counts[f'primitive_pd_addition_{variant}']=6*len(IH)**2
    for n,a,x in product(range(1,7),H,IH):
        assert hgamma(n,hmul(a,x),variant)==hmul(hpow(a,n),hgamma(n,x,variant))
    counts[f'primitive_pd_scalar_{variant}']=6*len(H)*len(IH)
    for m,n,x in product(range(1,7),range(1,7),IH):
        assert hmul(hgamma(m,x,variant),hgamma(n,x,variant))==hscale(comb(m+n,m),hgamma(m+n,x,variant))
        coeff=factorial(m*n)//(factorial(m)*factorial(n)**m)
        assert hgamma(m,hgamma(n,x,variant),variant)==hscale(coeff,hgamma(m*n,x,variant))
    counts[f'primitive_pd_product_{variant}']=36*len(IH)
    counts[f'primitive_pd_iteration_{variant}']=36*len(IH)
    assert all(hgamma(3,x,variant)==hzero for x in IH)
witness=(zero,t)
assert hgamma(2,witness,False)==hzero
assert hgamma(2,witness,True)==(zero,(0,0,2))

# The two written u-relations alone fail uniqueness already for A=F2.
def a(n,canonical):return 1 if canonical or n<=1 else 0
for canonical in (False,True):
    for m,n in product(range(1,17),repeat=2):
        assert (comb(m+n,m)*(a(m,canonical)*a(n,canonical)-a(m+n,canonical)))%2==0
        assert (a(m,canonical)*a(n,canonical)**m-a(m*n,canonical))%2==0
counts['weak_u_relation_pairs']=2*16**2

# Polynomial Witt cocycles c_p, verified as polynomial identities, not only
# on F_p-valued points.  A homogeneous degree-p 1-cochain is a*x^p and has
# zero coboundary modulo p, so the displayed nonzero cocycle is not a boundary.
def padd(x,y,p):
    out=dict(x)
    for m,c in y.items():out[m]=(out.get(m,0)+c)%p
    return {m:c for m,c in out.items() if c}
def pscale(x,c,p):return {m:(c*v)%p for m,v in x.items() if (c*v)%p}
def pmul(x,y,p):
    out={}
    for m,c in x.items():
        for n,d in y.items():
            key=tuple(a+b for a,b in zip(m,n))
            out[key]=(out.get(key,0)+c*d)%p
    return {m:c for m,c in out.items() if c}
def ppow(x,n,p):
    out={(0,0,0):1}
    for _ in range(n):out=pmul(out,x,p)
    return out
def witt(x,y,p):
    out={}
    for j in range(1,p):
        out=padd(out,pscale(pmul(ppow(x,j,p),ppow(y,p-j,p),p),comb(p,j)//p,p),p)
    return out
X={(1,0,0):1};Y={(0,1,0):1};Z={(0,0,1):1}
for p in (2,3,5,7):
    coboundary=padd(witt(Y,Z,p),pscale(witt(padd(X,Y,p),Z,p),-1,p),p)
    coboundary=padd(coboundary,witt(X,padd(Y,Z,p),p),p)
    coboundary=padd(coboundary,pscale(witt(X,Y,p),-1,p),p)
    assert coboundary=={}
    assert witt(X,Y,p)
    assert all(comb(p,j)%p==0 for j in range(1,p))
counts['witt_polynomial_cocycles']=4

# Scan374 coefficient-natural Sq^2 differs from scalar extension over R=F2[t]/t2.
# In H*(CP2;R)=F2[t,u]/(t2,u3), deg u=2, (tu)^2=0 but t Sq^2(u)=tu2!=0.
monomials=[(i,j) for i in range(2) for j in range(3)]
def poly_mul(x,y):
    out=set()
    for a,b in x:
        for c,d in y:
            if a+c<2 and b+d<3:
                z=(a+c,b+d)
                if z in out:out.remove(z)
                else:out.add(z)
    return out
assert poly_mul({(1,1)},{(1,1)})==set()
assert poly_mul({(1,0)},{(0,2)})=={(1,2)}

# Direct normalized group-bar computation refuting unstabilized H_2=direct-sum G_a.
def rank_mod(matrix,p):
    if not matrix:return 0
    a=[row[:] for row in matrix]; row=0
    for col in range(len(a[0])):
        pivot=next((r for r in range(row,len(a)) if a[r][col]%p),None)
        if pivot is None:continue
        a[row],a[pivot]=a[pivot],a[row]
        inv=pow(a[row][col],-1,p)
        a[row]=[(x*inv)%p for x in a[row]]
        for r in range(row+1,len(a)):
            if a[r][col]:
                fac=a[r][col]
                a[r]=[(x-fac*y)%p for x,y in zip(a[r],a[row])]
        row+=1
        if row==len(a):break
    return row
bar_results=[]
for p in (2,3):
    for dim in (1,2):
        group=list(product(range(p),repeat=dim)); ident=(0,)*dim
        nz=[g for g in group if g!=ident]
        bases={n:list(product(nz,repeat=n)) for n in (1,2,3)}
        ranks={}
        for n in (2,3):
            target=bases[n-1]; idx={x:i for i,x in enumerate(target)}
            mat=[[0 for _ in bases[n]] for _ in target]
            for j,g in enumerate(bases[n]):
                faces=[g[1:]]
                for i in range(n-1):
                    summed=tuple((a+b)%p for a,b in zip(g[i],g[i+1]))
                    faces.append(g[:i]+(summed,)+g[i+2:])
                faces.append(g[:-1])
                for i,face in enumerate(faces):
                    if ident not in face:
                        mat[idx[face]][j]=(mat[idx[face]][j]+(-1)**i)%p
            ranks[n]=rank_mod(mat,p)
        h2=len(bases[2])-ranks[2]-ranks[3]
        assert h2==dim*(dim+1)//2
        bar_results.append({'p':p,'vector_dimension':dim,'group_size':len(group),
                            'chain_dimensions':{str(n):len(bases[n]) for n in bases},
                            'differential_ranks':ranks,'H2_dimension':h2})
counts['finite_group_H2_bar_calculations']=len(bar_results)

print(json.dumps({'result':'all assertions passed','ring_cardinality':len(B),
                  'pd_ideal_cardinality':len(J),'coalgebra_cardinality':8,
                  'primitive_convolution_ring_cardinality':len(H),
                  'primitive_convolution_ideal_cardinality':len(IH),
                  'checks':counts,'bar_homology':bar_results,'elapsed_seconds':perf_counter()-started},indent=2))
