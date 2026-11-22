from functools import lru_cache
from math import factorial, comb, prod
from collections import Counter
from pathlib import Path
from time import perf_counter
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# A leaf is (); an internal node is a sorted tuple of (child,multiplicity).
LEAF=()
@lru_cache(None)
def wt(t):
    return 1 if t==LEAF else sum(wt(c)*m for c,m in t)
@lru_cache(None)
def dep(t):
    return 0 if t==LEAF else 1+dep(t[0][0])
@lru_cache(None)
def bases(n,W):
    if n==0:return (LEAF,)
    cs=sorted(bases(n-1,W),key=lambda x:(wt(x),repr(x)))
    ans=[]
    def rec(start,rem,sel):
        if sel:ans.append(tuple(sel))
        for i in range(start,len(cs)):
            c=cs[i]
            if wt(c)>rem:break
            for m in range(1,rem//wt(c)+1):
                rec(i+1,rem-m*wt(c),sel+[(c,m)])
    rec(0,W,[])
    return tuple(ans)
def level_nodes(t,l):
    if l==0:return [t]
    return [v for c,m in t for v in level_nodes(c,l-1)]
def nondeg(t):
    return all(any(sum(m for c,m in z)>1 for z in level_nodes(t,l)) for l in range(dep(t)))
def normalize(ms):return tuple(sorted(((c,m) for c,m in ms.items() if m),key=lambda z:(wt(z[0]),repr(z[0]))))
@lru_cache(None)
def collapse(t,k):
    # collapse levels k,k+1, root indexed 0
    if k==0:
        ex=Counter();den=1
        for c,a in t:
            den*=factorial(a)
            for z,b in c:
                ex[z]+=a*b;den*=factorial(b)**a
        num=1
        for e in ex.values():num*=factorial(e)
        assert num%den==0,(t,num,den)
        return num//den,normalize(ex)
    ex=Counter();coef=1;den=1
    for c,a in t:
        v,z=collapse(c,k-1)
        coef*=v**a;ex[z]+=a;den*=factorial(a)
    for a in ex.values():coef*=factorial(a)
    assert coef%den==0
    return coef//den,normalize(ex)
def first(t):
    # derivative under eval to R=Z[T]/(T^2), all higher gamma zero
    ans=[]
    for c,a in t:
        rem=Counter(dict(t));rem[c]-=1
        remaining=[z for z,b in rem.items() for _ in range(b)]
        if not remaining:ans.append((0,c,1))
        elif len(remaining)==1 and wt(remaining[0])==1:ans.append((1,c,1))
    return ans

def calc(W,max_n=None,verbose=False):
    max_n=max_n or W
    BB={n:[(a,t) for a in range(2) for t in bases(n,W-a) if wt(t)+a==W and nondeg(t)] for n in range(max_n+1)}
    # relative quotient removes R dT in degree 0
    BB[0]=[]
    ds={}
    for n in range(1,max_n+1):
        rows={x:i for i,x in enumerate(BB[n-1])};mat=sp.zeros(len(rows),len(BB[n]))
        for j,(a,t) in enumerate(BB[n]):
            for b,c,v in first(t):
                if a+b<2 and (a+b,c) in rows:mat[rows[(a+b,c)],j]+=v
            for k in range(n-1):
                v,c=collapse(t,k)
                if (a,c) in rows:mat[rows[(a,c)],j]+=(-1)**(k+1)*v
        ds[n]=mat
    for n in range(2,max_n+1):assert ds[n-1]*ds[n]==sp.zeros(ds[n-1].rows,ds[n].cols),(W,n)
    ranks={n:ds[n].rank() for n in ds}
    hom=[]
    for n in range(1,max_n):
        s=smith_normal_form(ds[n+1],domain=ZZ)
        diag=[abs(int(s[i,i])) for i in range(min(s.shape)) if s[i,i]]
        tors=[d for d in diag if d>1]
        fr=len(BB[n])-ranks[n]-ranks[n+1]
        if fr or tors:hom.append((n,fr,tors))
    if verbose:print(W, [len(BB[n]) for n in BB],hom,flush=True)
    return BB,ds,hom

def pretty(t):
    if t==LEAF:return 't'
    return '['+', '.join(pretty(c)+(('^'+str(a)) if a!=1 else '') for c,a in t)+']'

def last(t):
    if dep(t)==1:
        return LEAF if wt(t)==1 else None
    out=[]
    for c,a in t:
        z=last(c)
        if z is None:return None
        out.append((z,a))
    return tuple(out)

def face(n,i,a,t):
    ans=Counter()
    if i==0:
        for b,c,v in first(t):
            if a+b<2:ans[(a+b,c)]+=v
    elif i==n:
        c=last(t)
        if c is not None:ans[(a,c)]+=1
    else:
        v,c=collapse(t,i-1);ans[(a,c)]+=v
    return +ans

def apply_face(n,i,z):
    out=Counter()
    for (a,t),v in z.items():
        for key,c in face(n,i,a,t).items():out[key]+=v*c
    return +out

if __name__=='__main__':
    start=perf_counter()
    receipts=[];face_checks=0;vectors=0
    for W in range(2,7):
        BB,ds,hom=calc(W)
        vectors+=sum(map(len,BB.values()))
        receipts.append({'weight':W,'dimensions':[len(BB[n]) for n in BB],
            'homology':[{'degree':n,'free_rank':r,'torsion':t} for n,r,t in hom],
            'basis':{n:[('T*' if a else '')+pretty(t) for a,t in B] for n,B in BB.items()},
            'matrices':{n:M.tolist() for n,M in ds.items()}})
        # Check the individual unnormalized face identities, not just d^2.
        for n in range(2,min(4,W)+1):
            for a in range(2):
                for t in bases(n,W-a):
                    if wt(t)+a!=W:continue
                    for i in range(n):
                        for j in range(i+1,n+1):
                            lhs=apply_face(n-1,i,face(n,j,a,t))
                            rhs=apply_face(n-1,j-1,face(n,i,a,t))
                            assert lhs==rhs,(W,n,i,j,a,t,lhs,rhs)
                            face_checks+=1
    BB,ds,hom=calc(6)
    u=((LEAF,2),);v=((LEAF,4),)
    x=normalize(Counter({u:3}));y=normalize(Counter({u:1,v:1}))
    ix=BB[2].index((0,x));iy=BB[2].index((0,y))
    cycle=sp.zeros(len(BB[2]),1);cycle[ix]=1;cycle[iy]=-1
    middle_1=((u,1),);middle_2=((u,2),)
    z=normalize(Counter({middle_1:1,middle_2:1}))
    iz=BB[3].index((0,z))
    assert ds[2]*cycle==sp.zeros(len(BB[1]),1)
    assert ds[3][:,iz]==-3*cycle
    assert all(int(ds[3][ix,j])%3==0 for j in range(ds[3].cols))
    smith=smith_normal_form(ds[3],domain=ZZ)
    factors=[abs(int(smith[i,i])) for i in range(min(smith.shape)) if smith[i,i]]
    assert factors==[1]*11+[3]
    assert ds[2].rank()==2
    assert (2,0,[3]) in hom
    presentation=sp.Matrix([
        [12,0,9,3,4,3,3,3,2,18,6,12,12,12],
        [0,1,0,0,0,0,0,0,0,-15,-5,-10,-10,-10],
        [0,0,0,0,0,0,0,1,0,0,0,0,0,0]])
    rel=presentation*ds[3]
    assert all(rel[i,j]==0 for i in range(2) for j in range(rel.cols))
    assert all(int(rel[2,j])%3==0 for j in range(rel.cols))
    inverse=sp.zeros(14,3)
    inverse[6,0]=1;inverse[8,0]=-1;inverse[1,1]=1
    inverse[7,2]=1;inverse[6,2]=-1
    assert presentation*inverse==sp.eye(3)
    assert ds[2]*inverse==sp.Matrix([[-5,-6,0],[0,1,0]])
    prime_checks=[];partition_checks=0
    for p in [3,5,7,11,13,17,19]:
        c=prod(range(1,2*p-2,2))//p
        assert prod(range(1,2*p-2,2))%p==0
        left=factorial(2*p)//(factorial(p)*2**p)
        assert left==c*comb(2*p,2)
        middle=factorial(2*p-2)//(factorial(p-1)*2**(p-1))
        assert middle==p*c
        def partitions(rem,start=1,counts=()):
            if rem==0:
                yield counts;return
            for j in range(start,rem+1):
                for a in range(1,rem//j+1):
                    yield from partitions(rem-j*a,j+1,counts+((j,a),))
        checked=0
        for parts in partitions(p):
            if parts in [((1,p),),((p,1),)]:continue
            den=prod(factorial(j)**a*factorial(a) for j,a in parts)
            assert factorial(p)%den==0
            assert (factorial(p)//den)%p==0
            checked+=1
        for a in range(1,p):assert comb(p,a)%p==0
        partition_checks+=checked
        prime_checks.append({'p':p,'weight':2*p,'c_p':c,'partition_coefficients_checked':checked})
    out={'passed':True,'scope':'Relative special PD cotangent of R_2=Gamma_Z(T)/I_2; complete integral weights 2 through 6',
         'normalized_basis_vectors':vectors,'unnormalized_face_identity_checks':face_checks,
         'prime_family_checks':prime_checks,'prime_partition_coefficients_checked':partition_checks,
         'weight6_cycle':{'positive_index':ix,'negative_index':iy,'boundary_word_index':iz,
             'boundary_multiplier':-3,'detector_modulus':3,'smith_d3':factors,
             'rank_d2':2,'H2':'Z/3'},'cases':receipts,
         'runtime_seconds':perf_counter()-start}
    dest=Path(__file__).resolve().parents[1]/'logs'/'A_cosimplicial_pd_cotangent.json'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2,default=int)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2))
