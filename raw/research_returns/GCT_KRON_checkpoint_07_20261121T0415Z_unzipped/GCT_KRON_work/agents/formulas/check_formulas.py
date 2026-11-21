#!/usr/bin/env python3
"""Exact checks for GCT_KRON F-series. No floating point arithmetic.
Run: python check_formulas.py; prints a machine-readable JSON certificate.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import product, combinations_with_replacement
from collections import Counter
from pathlib import Path
import json, math, time

@lru_cache(None)
def partitions(n, maxpart=None):
    if n==0: return ((),)
    if maxpart is None or maxpart>n: maxpart=n
    out=[]
    for k in range(maxpart,0,-1):
        out.extend((k,)+tail for tail in partitions(n-k,k))
    return tuple(out)

def zpart(p):
    return math.prod(k**v*math.factorial(v) for k,v in Counter(p).items())

def mul_poly(a,b,cap=None):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if cap is None or i+j<=cap:out[i+j]+=x*y
    return out if cap is None else out[:cap+1]

@lru_cache(None)
def two_row_chars(p):
    n=sum(p); a=[1]
    for k in p:
        b=[0]*(k+1);b[0]=b[-1]=1
        a=mul_poly(a,b)
    return tuple(a[r]-(a[r-1] if r else 0) for r in range(n//2+1))

@lru_cache(None)
def hook_chars(p):
    n=sum(p); a=[1]
    for k in p:
        b=[0]*(k+1);b[0]=1;b[-1]=(-1)**(k+1)
        a=mul_poly(a,b)
    h=[]
    for k in range(n):h.append(a[k]-(h[-1] if h else 0))
    assert a[-1]==h[-1]
    return tuple(h)

def kron_classsum(n,a,b,c,hook=False):
    chars=hook_chars if hook else two_row_chars
    total=sum((Fraction(chars(p)[a]*chars(p)[b]*chars(p)[c],zpart(p)) for p in partitions(n)),Fraction(0))
    assert total.denominator==1
    return total.numerator

def two_row_interval(n,a,b,c):
    a,b,c=sorted((a,b,c),reverse=True)
    low=max(0,(a+b+c-n+1)//2)
    up=(b+c-a)//2
    return max(0,up-low+1)

def hook_indicator(n,a,b,c):
    return int(max(a,b,c)<=a+b+c-max(a,b,c) and a+b+c<=2*n-2)

@lru_cache(None)
def binary_tables(n,a,b,c):
    if min(n,a,b,c)<0:return ()
    ans=[]
    # Four free entries with at least two memberships determine the table.
    # Index 4*i+2*j+k corresponds to membership vector (i,j,k).
    for x111 in range(min(a,b,c)+1):
      for x110 in range(min(a-x111,b-x111)+1):
       for x101 in range(min(a-x111-x110,c-x111)+1):
        for x011 in range(min(b-x111-x110,c-x111-x101)+1):
         x100=a-x111-x110-x101
         x010=b-x111-x110-x011
         x001=c-x111-x101-x011
         x000=n-(x111+x110+x101+x011+x100+x010+x001)
         if x000>=0:ans.append((x000,x001,x010,x011,x100,x101,x110,x111))
    return tuple(ans)

def down_matrix(n,a,b,c):
    import sympy as s
    src=binary_tables(n,a,b,c);targets=[]
    for axis,r in enumerate((a,b,c)):
        if r:
            ms=[a,b,c];ms[axis]-=1
            targets.extend((axis,t) for t in binary_tables(n,*ms))
    rows={v:i for i,v in enumerate(targets)}
    M=s.zeros(len(rows),len(src))
    for col,table in enumerate(src):
      for axis,bit in enumerate((4,2,1)):
       for j,count in enumerate(table):
        if j&bit and count:
         target=list(table);target[j]-=1;target[j-bit]+=1
         M[rows[(axis,tuple(target))],col]+=count
    return M

def rational_identity_certificate():
    import sympy as s
    t,x,y,z=s.symbols('t x y z');vv=(t,x,y,z);xyz=(x,y,z);K=t*t*x*y*z
    EE=list(product((0,1),repeat=3))
    PP=[s.prod(u**e for u,e in zip(xyz,E)) for E in EE]
    FF=[s.Poly(1-t*p,*vv) for p in PP]
    num=s.Poly(0,*vv)
    for i,E in enumerate(EE):
        term=s.Poly((-1)**sum(E)*PP[i]*(1+K*t*PP[i]),*vv)
        for j in range(8):
            if i!=j:term*=FF[j]
        for u,e in zip(xyz,E):term*=s.Poly(1-K*u**(1-2*e),*vv)
        num+=term
    rhs=s.Poly((1-x)*(1-y)*(1-z)*(1-K*K),*vv)
    for u in xyz:
        rhs*=s.Poly(1-K/u,*vv)
        rhs*=s.Poly(1-K*u,*vv)
    residual=num-rhs
    assert residual.is_zero
    # Separate hook-series factorization certificate.
    AA=(1+t*x)*(1+t*y)*(1+t*z)*(1+t*x*y*z)
    BB=(1-t)*(1-t*x*y)*(1-t*x*z)*(1-t*y*z)
    hook_res=s.Poly(AA-BB-t*(1+x)*(1+y)*(1+z)*(1+t*t*x*y*z),*vv)
    assert hook_res.is_zero
    return {'two_row_cleared_denominator_residual':'0','hook_factorization_residual':'0','arithmetic':'Z[t,x,y,z] via sympy.Poly exact integer coefficients'}

def main():
    started=time.time();counts={}
    counts.update(rational_identity_certificate())
    ntr=0
    for n in range(1,19):
      for a,b,c in combinations_with_replacement(range(n//2+1),3):
       direct=kron_classsum(n,a,b,c)
       assert direct==two_row_interval(n,a,b,c),(n,a,b,c,direct)
       ntr+=1
    counts['all_two_row_triples_N_1_to_18']=ntr
    nh=0
    for n in range(1,15):
      for a,b,c in combinations_with_replacement(range(n),3):
       direct=kron_classsum(n,a,b,c,hook=True)
       assert direct==hook_indicator(n,a,b,c),(n,a,b,c,direct)
       nh+=1
    counts['all_hook_triples_N_1_to_14']=nh
    nr=0;maxcols=0
    for n in range(1,8):
      for a,b,c in combinations_with_replacement(range(n//2+1),3):
       M=down_matrix(n,a,b,c);value=M.cols-M.rank()
       assert value==two_row_interval(n,a,b,c),(n,a,b,c,value)
       nr+=1;maxcols=max(maxcols,M.cols)
    counts['incidence_nullities_all_two_row_triples_N_1_to_7']=nr
    counts['maximum_incidence_columns']=maxcols
    # Hook product zero set and palindromicity, using multiplication only.
    for m in range(1,101):
      coeff=[1]
      for i in range(2,m+1):
       f=[0]*(2*i);f[0]=f[-1]=1;coeff=mul_poly(coeff,f)
      assert len(coeff)==m*m and coeff==coeff[::-1]
      if m>=7:
       zeros={i for i,v in enumerate(coeff) if v==0}
       expected={1,2,4,6,m*m-7,m*m-5,m*m-3,m*m-2}
       assert zeros==expected,(m,zeros^expected)
    counts['rectangular_hook_product_support_m_1_to_100']='passed; m>=7 zero set exactly eight reflected exceptions'
    counts['elapsed_seconds']=round(time.time()-started,3)
    print(json.dumps(counts,indent=2))
    Path(__file__).with_name('formula_certificate.json').write_text(json.dumps(counts,indent=2)+'\n')

if __name__=='__main__':main()
