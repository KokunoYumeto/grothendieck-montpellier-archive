"""Literal T053 row-weight polytopes and direct standard-monomial counts."""
from itertools import product
from functools import lru_cache
import argparse
import json


@lru_cache(None)
def compositions(n,m):
    if n<0:return ()
    if m==1:return ((n,),)
    return tuple((a,)+tail for a in range(n+1)
                 for tail in compositions(n-a,m-1))


def polytopes(m,eta,k):
    r=len(eta)
    if not (m>=3 and 1<=r<=m-2 and k>=0 and all(a>=0 for a in eta)):
        raise ValueError('Require m>=3,1<=len(eta)<=m-2,k>=0,eta>=0.')
    names=[f'u_{a+1}_{i+1}' for a in range(r) for i in range(m)]
    names += [f'v_{i+1}' for i in range(m)]
    nv=len(names); result=[]
    for mask in range(1<<r):
        eq=[];rhs=[];ge=[];ge_rhs=[]
        for a in range(r):
            row=[0]*nv
            for i in range(m):row[a*m+i]=1
            eq.append(row);rhs.append(eta[a])
        for i in range(m):
            row=[0]*nv
            for a in range(r):row[a*m+i]=1
            row[r*m+i]=-1;eq.append(row);rhs.append(k)
        for a in range(r):
            row=[0]*nv
            if (mask>>a)&1:
                row[a*m+a]=1;eq.append(row);rhs.append(0)
                row=[0]*nv;row[r*m+a]=1;ge.append(row);ge_rhs.append(1)
            else:
                row[r*m+a]=1;eq.append(row);rhs.append(0)
        result.append({'tag':[a+1 for a in range(r) if (mask>>a)&1],
            'variables':names,'integer':True,'lower_bounds':[0]*nv,
            'upper_bounds':[eta[a] for a in range(r) for _ in range(m)]+[sum(eta)]*m,
            'A_eq':eq,'b_eq':rhs,'A_ge':ge,'b_ge':ge_rhs})
    return result


def standard_monomials(m,eta,k):
    r=len(eta);out=[]
    for rows in product(*(compositions(a,m) for a in eta)):
        u=sum(rows,());v=tuple(sum(rows[a][i] for a in range(r))-k for i in range(m))
        if min(v)<0:continue
        if any(rows[a][a] and v[a] for a in range(r)):continue
        mask=sum((v[a]>0)<<a for a in range(r))
        out.append((mask,u+v))
    return out


def count(m,eta,k):
    ans=[0]*(1<<len(eta))
    for mask,_ in standard_monomials(m,eta,k):ans[mask]+=1
    return {'total':sum(ans),'tag_counts':ans}


def main():
    p=argparse.ArgumentParser();p.add_argument('--m',type=int,required=True)
    p.add_argument('--eta',type=int,nargs='+',required=True)
    p.add_argument('--k',type=int,required=True);p.add_argument('--count',action='store_true')
    a=p.parse_args();out={'polytopes':polytopes(a.m,tuple(a.eta),a.k)}
    if a.count:out.update(count(a.m,tuple(a.eta),a.k))
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
