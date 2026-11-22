"""Exact universal-algebra checks for A-S09-13 (three odd parameters)."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import factorial,comb,prod
from pathlib import Path
from time import perf_counter
import json

# Even exponents: z,y1,y2,y3. Odd bits: dz,x1,x2,x3.
ONE={(0,0,0,0,0):F(1)}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def mul(p,q):
    out={}
    for a,v in p.items():
        for b,w in q.items():
            if a[4]&b[4]:continue
            sign=(-1)**sum(1 for i in range(4) for j in range(4)
                           if i>j and a[4]>>i&1 and b[4]>>j&1)
            k=tuple(a[i]+b[i] for i in range(4))+(a[4]|b[4],)
            out[k]=out.get(k,F(0))+sign*v*w
    return {k:v for k,v in out.items() if v}
def power(p,n):
    out=ONE
    for _ in range(n):out=mul(out,p)
    return out
def variable(i,odd=False):
    a=[0]*5
    if odd:a[4]=1<<i
    else:a[i]=1
    return {tuple(a):F(1)}
Z=variable(0);U=variable(0,True)
Y=[variable(i) for i in range(1,4)]
X=[variable(i,True) for i in range(1,4)]
YP=[add(mul(Z,y),mul(U,x)) for x,y in zip(X,Y)]
XP=[mul(Z,x) for x in X]
def differential(p):
    out={}
    for key,c in p.items():
        if key[0] and not(key[4]&1):
            a=list(key);a[0]-=1;a[4]|=1
            out=add(out,{tuple(a):c*key[0]})
        for i in range(1,4):
            if key[4]>>i&1:
                a=list(key);a[i]+=1;a[4]^=1<<i
                sign=(-1)**sum(key[4]>>j&1 for j in range(i))
                out=add(out,{tuple(a):c*sign})
    return out
@lru_cache(None)
def phi(b,prime=False):
    out=ONE
    for a,y in zip(b,YP if prime else Y):out=mul(out,scale(power(y,a),F(1,factorial(a))))
    return out
@lru_cache(None)
def delta(b,prime=False):
    out={}
    for i,a in enumerate(b):
        if a:
            c=list(b);c[i]-=1
            out=add(out,mul(phi(tuple(c),prime),(XP if prime else X)[i]))
    return out
def suffix(entries):return prod(sum(sum(b) for b in entries[i:]) for i in range(len(entries)))
@lru_cache(None)
def image(word):
    out=phi(word[0],True)
    for b in word[1:]:out=mul(out,delta(b,True))
    return scale(out,F(1,suffix(word[1:])))
def multiply_monomials(a,b):
    return tuple(x+y for x,y in zip(a,b)),prod(comb(x+y,x) for x,y in zip(a,b))
def bar_boundary_image(word):
    out={}
    for i in range(len(word)-1):
        b,c=multiply_monomials(word[i],word[i+1])
        merged=word[:i]+(b,)+word[i+2:]
        out=add(out,scale(image(merged),(-1)**i*c))
    return out
def shuffles(a,b):
    if not a:return [(b,1)]
    if not b:return [(a,1)]
    return [((a[0],)+v,s) for v,s in shuffles(a[1:],b)]+[
        ((b[0],)+v,(-1)**len(a)*s) for v,s in shuffles(a,b[1:])]

if __name__=='__main__':
    start=perf_counter();identities=0;integrality=0;chains=0;products=0
    monomials=[b for b in product(range(8),repeat=3) if 1<=sum(b)<=7]
    for b in monomials:
        a=sum(b)
        assert phi(b,True)==add(mul(power(Z,a),phi(b)),mul(mul(power(Z,a-1),U),delta(b)))
        assert delta(b,True)==mul(power(Z,a),delta(b))
        identities+=2
    zero=(0,0,0)
    small=[b for b in product(range(3),repeat=3) if 1<=sum(b)<=2]
    words=[]
    for n in range(4):
        for entries in product(small,repeat=n):
            for b0 in [zero]+small:
                word=(b0,)+entries
                if sum(map(sum,word))>6:continue
                result=image(word)
                assert all((c*prod(factorial(a) for a in key[:4])).denominator==1
                           for key,c in result.items())
                integrality+=1
                assert differential(result)==bar_boundary_image(word)
                chains+=1
                if sum(map(sum,word))<=2:words.append(word)
    for a,b in product(words,repeat=2):
        head,c=multiply_monomials(a[0],b[0]);rhs={}
        for tail,s in shuffles(a[1:],b[1:]):rhs=add(rhs,scale(image((head,)+tail),c*s))
        assert mul(image(a),image(b))==rhs
        products+=1
    answer={'passed':True,'scope':'Universal nonclosed-factor bar integration with three odd parameters',
            'phi_delta_identity_checks':identities,'PD_basis_integrality_checks':integrality,
            'chain_identity_checks':chains,'shuffle_product_checks':products,
            'maximum_monomial_arity':7,'maximum_bar_arity':6,'maximum_bar_length':3,
            'runtime_seconds':perf_counter()-start}
    dest=Path(__file__).resolve().parents[1]/'logs'/'A_cosimplicial_nonclosed_bar.json'
    dest.write_text(json.dumps(answer,indent=2)+'\n')
    print(json.dumps(answer,indent=2))
