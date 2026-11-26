#!/usr/bin/env python3
"""Reproducible checks for sparse presentations and bounded-cofactor recovery.
Run: python3 sparse_presentation_checks.py
No external packages are required. This is finite evidence, not a proof.
"""
from itertools import product, combinations
from math import prod
from random import Random
import json


def clean(f,p):
    return {e:c%p for e,c in f.items() if c%p}


def add(f,g,p):
    out=dict(f)
    for e,c in g.items(): out[e]=(out.get(e,0)+c)%p
    return clean(out,p)


def multiply(f,g,p):
    out={}
    for a,c in f.items():
        for b,d in g.items():
            e=tuple(x+y for x,y in zip(a,b))
            out[e]=(out.get(e,0)+c*d)%p
    return clean(out,p)


def power(f,k,p,r):
    out={(0,)*r:1}
    for _ in range(k): out=multiply(out,f,p)
    return out


def ev(f,x,p):
    return sum(c*prod(pow(a,e,p) for a,e in zip(x,m)) for m,c in f.items())%p


def rank(rows,p,columns):
    a=[[v%p for v in row] for row in rows]
    piv=[]
    for j in range(columns):
        i=next((i for i in range(len(piv),len(a)) if a[i][j]),None)
        if i is None: continue
        k=len(piv);a[k],a[i]=a[i],a[k]
        u=pow(a[k][j],-1,p);a[k]=[(u*v)%p for v in a[k]]
        for i in range(len(a)):
            if i!=k and a[i][j]:
                u=a[i][j];a[i]=[(x-u*y)%p for x,y in zip(a[i],a[k])]
        piv.append(j)
    return a,piv


def kernel(rows,p,n):
    a,piv=rank(rows,p,n)
    ans=[]
    for j in range(n):
        if j in piv: continue
        v=[0]*n;v[j]=1
        for i,k in enumerate(piv):v[k]=-a[i][j]%p
        ans.append(v)
    return ans


def homogeneous_monomials(r,e):
    if r==1:
        yield (e,);return
    for k in range(e+1):
        for tail in homogeneous_monomials(r-1,e-k):yield (k,)+tail


def recover_cofactors(forms,p,degree):
    """Solve f_0 h_i-f_i h_0=0 at the prescribed cofactor degrees."""
    r=len(next(iter(forms[0])))
    bs=[sum(next(iter(f)))-degree for f in forms]
    monos=[list(homogeneous_monomials(r,b)) for b in bs]
    columns=[(i,m) for i,ms in enumerate(monos) for m in ms]
    index={col:j for j,col in enumerate(columns)}
    equations={}
    for i in range(1,len(forms)):
        for m in monos[i]:
            for e,c in forms[0].items():
                key=(i,tuple(a+b for a,b in zip(m,e)))
                row=equations.setdefault(key,{})
                col=index[(i,m)];row[col]=(row.get(col,0)+c)%p
        for m in monos[0]:
            for e,c in forms[i].items():
                key=(i,tuple(a+b for a,b in zip(m,e)))
                row=equations.setdefault(key,{})
                col=index[(0,m)];row[col]=(row.get(col,0)-c)%p
    matrix=[[row.get(j,0) for j in range(len(columns))] for row in equations.values()]
    ker=kernel(matrix,p,len(columns))
    assert len(ker)==1,(p,bs,len(ker))
    v=ker[0]
    hs=[{} for _ in forms]
    for c,(i,m) in zip(v,columns):
        if c:hs[i][m]=c
    return hs


def scalar_from_multiples(forms,p,degree):
    r=len(next(iter(forms[0])))
    hs=recover_cofactors(forms,p,degree)
    j=next(i for i,h in enumerate(hs) if h.get((sum(next(iter(h))),)+(0,)*(r-1),0))
    h=hs[j];b=sum(next(iter(h)));c=h.get((b,)+(0,)*(r-1),0)
    f=multiply(power(forms[j],p-1,p,r),h,p)
    coefficient=sum(v for e,v in f.items() if all(a==p-1 for a in e[1:]))%p
    return coefficient*pow(c,-p,p)%p


def projective_points(p,r):
    for j in range(r):
        for tail in product(range(p),repeat=r-j-1):yield (0,)*j+(1,)+tail


def scalar(f,p,r):return power(f,p-1,p,r).get((p-1,)*r,0)


def zero_count(forms,p,r):
    return sum(all(ev(f,x,p)==0 for f in forms) for x in projective_points(p,r))


def sparse_cone_residue(forms,p,r):
    indicator={(0,)*r:1}
    for f in forms:
        indicator=multiply(indicator,add({(0,)*r:1},{e:-c for e,c in power(f,p-1,p,r).items()},p),p)
    return (-1)**r*sum(c for e,c in indicator.items() if all(a>0 and a%(p-1)==0 for a in e))%p


def restricted_support_residue(rows,forms,p,r):
    basis=kernel(rows,p,r);m=len(basis)
    indicator={(0,)*r:1}
    for f in forms:
        indicator=multiply(indicator,add({(0,)*r:1},{e:-c for e,c in power(f,p-1,p,r).items()},p),p)
    result=0
    for exponents,c in indicator.items():
        support=[i for i,e in enumerate(exponents) if e]
        projection=[[b[j] for b in basis] for j in support]
        _,piv=rank(projection,p,m)
        if len(piv)<m:continue
        for z in product(range(p),repeat=m):
            x=[sum(z[k]*basis[k][j] for k in range(m))%p for j in support]
            result+=c*prod(pow(v,exponents[j],p) for j,v in zip(support,x))
    return result%p


def truncated_product_coefficient(rows,exponents,p,m):
    """Direct expansion in F_p[z_1,...,z_m]/(z_i^p)."""
    out={(0,)*m:1}
    for row,e in zip(rows,exponents):
        linear={tuple(int(i==j) for i in range(m)):a%p
                for j,a in enumerate(row) if a%p}
        for _ in range(e):
            out={a:c for a,c in multiply(out,linear,p).items()
                 if all(v<p for v in a)}
    return out.get((p-1,)*m,0)


def syndrome_coefficient(rows,exponents,p,m):
    """Top coefficient via weighted additive syndromes after choosing a basis."""
    chosen=[];chosen_ids=[]
    for i,row in enumerate(rows):
        _,piv=rank(chosen+[row],p,m)
        if len(piv)>len(chosen):chosen.append(row);chosen_ids.append(i)
        if len(chosen)==m:break
    if len(chosen)<m:return 0
    augmented=[list(row)+[int(i==j) for j in range(m)] for i,row in enumerate(chosen)]
    reduced,piv=rank(augmented,p,m)
    assert piv==list(range(m))
    inverse=[row[m:] for row in reduced]
    extra_ids=[i for i in range(len(rows)) if i not in chosen_ids]
    extra=[[sum(rows[i][a]*inverse[a][b] for a in range(m))%p
            for b in range(m)] for i in extra_ids]
    k=len(extra);distribution={(0,)*k:1}
    for i,original_i in enumerate(chosen_ids):
        nxt={}
        for syndrome,weight in distribution.items():
            for z in range(p):
                target=tuple((s+z*row[i])%p for s,row in zip(syndrome,extra))
                nxt[target]=(nxt.get(target,0)+weight*pow(z,exponents[original_i],p))%p
        distribution={s:c for s,c in nxt.items() if c}
    return (-1)**m*sum(weight*prod(pow(s,exponents[i],p)
                                  for s,i in zip(syndrome,extra_ids))
                      for syndrome,weight in distribution.items())%p


def ternary_hypersurface(permanent=False):
    count=0
    categories={'slope_nonzero':0,'slope_zero_offset_zero':0,'slope_zero_offset_nonzero':0}
    for x in product(range(3),repeat=8):
        a,b,t,u,*pad=x
        P=(a+b)**2 if permanent else b*(a+b)
        A=(-t*t*P+u*u*a*b)*prod(pad)+a**8
        for y in range(3):
            slope=(y*A-a)%3;offset=(y*y+sum(z*z for z in x))%3
            if slope:
                categories['slope_nonzero']+=1;count+=1
            elif offset==0:
                categories['slope_zero_offset_zero']+=1;count+=3
            else:categories['slope_zero_offset_nonzero']+=1
    return {'cone':count,'projective':(count-1)//2,'categories':categories}


def distributed_ternary_hypersurface(matrix):
    count=0
    for x in product(range(3),repeat=8):
        a,b,t,u,v1,v2,v3,v4=x
        P=(matrix[0][0]*a+matrix[0][1]*b)*(matrix[1][0]*a+matrix[1][1]*b)
        A=-t*t*P*v1*v1*v2*v2+u*u*a*b*v3*v3*v4*v4+a**8
        for y in range(3):
            slope=(y*A-a)%3;offset=(y*y+sum(z*z for z in x))%3
            count+=1 if slope else (3 if offset==0 else 0)
    permanent=(matrix[0][0]*matrix[1][1]+matrix[0][1]*matrix[1][0])%3
    projective=(count-1)//2
    assert projective%3==(1+permanent)%3
    return {'matrix':matrix,'scalar':permanent,'cone':count,'projective':projective}


def distributed_coefficient_check(matrix,p):
    """Expand after imposing row equations; only the pth-power truncation is used."""
    original_r=len(matrix)
    r=((original_r+p-2)//(p-1))*(p-1)
    padded=[row+[0]*(r-original_r) for row in matrix]
    padded += [[int(i==j) for j in range(r)] for i in range(original_r,r)]
    u=r+p-1;Q=p
    while Q<u+2:Q*=p
    m=Q-1;b=(m-u)//(p-1)
    assert m-u==(p-1)*b
    P={(0,)*m:1}
    for row in padded:
        linear={tuple(int(i==j) for i in range(m)):a%p for j,a in enumerate(row) if a%p}
        P=multiply(P,linear,p)
    G={}
    for j in range(p-1):
        multiplier=[0]*m;multiplier[r+j]=p-1
        for i in range(u+j*b,u+(j+1)*b):multiplier[i]=p-1
        summand=P if j==0 else {tuple(int(i<r) for i in range(m)):1}
        for exp,c in summand.items():
            shifted=tuple(a+z for a,z in zip(exp,multiplier))
            G[shifted]=(G.get(shifted,0)+(-1 if j==0 else 1)*c)%p
    out={(0,)*m:1}
    for _ in range(p-1):
        out={exp:c for exp,c in multiply(out,G,p).items() if all(e<p for e in exp)}
    value=out.get((p-1,)*m,0)
    expected=truncated_product_coefficient(padded,[1]*r, p, r) if p==2 else None
    # The squarefree coefficient of the row product is the permanent.
    row_product={(0,)*r:1}
    for row in padded:
        linear={tuple(int(i==j) for i in range(r)):a%p for j,a in enumerate(row) if a%p}
        row_product={exp:c for exp,c in multiply(row_product,linear,p).items() if max(exp)<=1}
    expected=row_product.get((1,)*r,0)
    assert value==expected,(matrix,p,value,expected)
    sigma=r+b+3;d=m+2
    assert (p-1)*sigma-d==(p-2)*(r+2)
    return value



def binary_precision(rows,forms,r,b):
    factors=[]
    for f in forms:
        terms=[{j for j,e in enumerate(m) if e} for m,c in f.items() if c%2]
        choices=[(1,set())]
        for k in range(1,min(b,len(terms))+1):
            for inds in combinations(range(len(terms)),k):
                choices.append(((-1)**k*2**(k-1),set().union(*(terms[i] for i in inds))))
        factors.append(choices)
    total=0
    for choice in product(*factors):
        coeff=prod(c for c,_ in choice)
        pins=set().union(*(v for _,v in choice))
        eqs=[list(row)+[0] for row in rows]
        eqs += [[int(i==j) for i in range(r)]+[1] for j in pins]
        a,pivs=rank(eqs,2,r+1)
        if r in pivs:continue
        total+=coeff*2**(r-len(pivs))
    return (total-1)%(2**b)


def run():
    rng=Random(20261124)
    checked=0
    for p in (2,3,5):
        for r in (2,3,4):
            for _ in range(15):
                forms=[]
                for j in range(1+rng.randrange(2)):
                    d=1+rng.randrange(4);ms=list(homogeneous_monomials(r,d))
                    f={m:rng.randrange(1,p) for m in rng.sample(ms,min(len(ms),1+rng.randrange(3)))}
                    forms.append(f)
                direct=zero_count(forms,p,r)
                assert (1-sparse_cone_residue(forms,p,r))%p==direct%p
                rows=[[rng.randrange(p) for _ in range(r)] for j in range(rng.randrange(r))]
                cone=sum(all(sum(a*b for a,b in zip(row,x))%p==0 for row in rows) and all(ev(f,x,p)==0 for f in forms) for x in product(range(p),repeat=r))
                assert restricted_support_residue(rows,forms,p,r)==cone%p
                checked+=1
    precisions=0
    for r in range(2,7):
        for _ in range(12):
            rows=[[rng.randrange(2) for _ in range(r)] for j in range(rng.randrange(r))]
            forms=[]
            for j in range(rng.randrange(3)):
                d=2+rng.randrange(3);ms=list(homogeneous_monomials(r,d))
                forms.append({m:1 for m in rng.sample(ms,min(len(ms),1+rng.randrange(4)))})
            direct=sum(all(sum(a*b for a,b in zip(row,x))%2==0 for row in rows) and all(ev(f,x,2)==0 for f in forms) for x in projective_points(2,r))
            for b in (1,2,3,4):
                assert binary_precision(rows,forms,r,b)==direct%(2**b)
                precisions+=1
    recovery=0
    for p in (2,3,5):
        for r in (3,4):
            ms=list(homogeneous_monomials(r,r))
            for _ in range(8):
                g={m:rng.randrange(1,p) for m in rng.sample(ms,min(5,len(ms)))}
                for B in (1,2):
                    # Cofactors include every coordinate Bth power: no projective common zero.
                    hs=[{tuple(B if i==j else 0 for i in range(r)):1} for j in range(r)]
                    extra=add(hs[0],hs[-1],p);hs.append(extra)
                    forms=[multiply(g,h,p) for h in hs]
                    assert scalar_from_multiples(forms,p,r)==scalar(g,p,r)
                    recovery+=1
    syndrome_cases=0
    for p in (2,3,5,7):
        for m in range(1,5):
            for _ in range(20):
                t=rng.randrange(m,min(m*(p-1),m+3)+1)
                exponents=[1]*t
                for _ in range(m*(p-1)-t):
                    choices=[i for i,e in enumerate(exponents) if e<p-1]
                    exponents[rng.choice(choices)]+=1
                rows=[[rng.randrange(p) for _ in range(m)] for j in range(t)]
                expected=truncated_product_coefficient(rows,exponents,p,m)
                assert syndrome_coefficient(rows,exponents,p,m)==expected
                syndrome_cases+=1
    cubic={(0,2,1):1,(3,0,0):-1,(1,0,2):-1}
    quartics=[{tuple(a+int(i==j) for i,a in enumerate(e)):c for e,c in cubic.items()} for j in range(3)]
    assert scalar(cubic,5,3)==2
    assert zero_count([cubic],5,3)==4
    assert scalar_from_multiples(quartics,5,3)==2
    unit=ternary_hypersurface(False);perm=ternary_hypersurface(True)
    assert unit['projective']==9953 and perm['projective']==10065
    distributed_cases=0
    for p in (3,5,7):
        for r in (1,2,3):
            for _ in range(5):
                distributed_coefficient_check([[rng.randrange(p) for _ in range(r)] for j in range(r)],p)
                distributed_cases+=1
    distributed_points=[distributed_ternary_hypersurface(matrix) for matrix in
                        ([[1,0],[0,1]],[[1,1],[1,1]],[[0,0],[1,1]],[[1,1],[1,0]])]
    return {'status':'passed','general_and_support_systems':checked,'binary_precision_cases':precisions,'bounded_cofactor_recoveries':recovery,'support_strip_syndrome_cases':syndrome_cases,'distributed_padding_coefficient_cases':distributed_cases,'distributed_padding_F3_points':distributed_points,'plane_cubic':{'scalar':2,'points':4,'quartic_multiples_recovered_scalar':2},'positive_unit_clause_F3':unit,'permanent_example_F3':perm}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
