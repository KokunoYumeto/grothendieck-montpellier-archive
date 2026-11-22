"""Exploratory Euler-characteristic search; not a certificate of geometry.

X = P(F^* U^vee) over Gr(2,n), dim X=2n-3, with H the relative
class and B the Pluecker class. H+B is the standard very ample class.
For a>=0, use the K-theoretic Adams character of Sym^a(F^*U^vee)
and the Weyl Euler polynomial on Gr(2,n). The formulas must be
independently audited before a positive search result is used.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb
from pathlib import Path
import time,json,itertools
@lru_cache(None)
def chi_gr(n,l1,l2):
    weights=[l1,l2]+[0]*(n-2);q=Fraction(1)
    for i in range(n):
        for j in range(i+1,n):q*=Fraction(weights[i]-weights[j]+j-i,j-i)
    assert q.denominator==1
    return q.numerator
@lru_cache(None)
def chi_x_nonnegative(n,p,a,b):
    assert a>=0
    total=0
    for j in range(p*a//2+1):
        coefficient=(1 if j%p==0 else 0)-(1 if j>0 and (j-1)%p==0 else 0)
        if coefficient:total+=coefficient*chi_gr(n,p*a-j+b,j+b)
    return total
@lru_cache(None)
def chi_x(n,p,a,b):
    if a==-1:return 0
    if a>=0:return chi_x_nonnegative(n,p,a,b)
    return -chi_x_nonnegative(n,p,-a-2,-b+p-n)
def chi_surface_negative(n,p,cut_h,cut_b,target_h,target_b):
    c=2*n-5
    return sum((-1)**j*comb(c,j)*chi_x(n,p,-target_h-j*cut_h,-target_b-j*cut_b) for j in range(c+1))
def main():
    start=time.monotonic();count=0;hits=[];minimum=None;tests=[]
    # n=3 is the Frobenius incidence hypersurface of bidegree (p,1)
    # in P2_x x P2_y, with B=O_x(1), H=O_y(1).
    def binom2(a):return (a+1)*(a+2)//2
    incidence_checks=0
    for p,a,b in itertools.product([2,3,5],range(-4,5),range(-4,5)):
        expected=binom2(b)*binom2(a)-binom2(b-p)*binom2(a-1)
        assert chi_x(3,p,a,b)==expected,(p,a,b,chi_x(3,p,a,b),expected)
        incidence_checks+=1
    for n,p in itertools.product(range(3,9),[2,3,5,7,11,13]):
        assert chi_x(n,p,0,0)==1
        assert chi_x(n,p,-1,0)==0
        assert chi_x(n,p,-2,p-n)==-1
        tests.append((n,p))
    for n,p,ch,cb,th,tb in itertools.product(range(3,9),[2,3,5,7,11,13],range(1,5),range(1,5),range(1,5),range(1,5)):
        value=chi_surface_negative(n,p,ch,cb,th,tb);count+=1
        item=dict(n=n,p=p,cut=[ch,cb],target=[th,tb],chi_negative=value)
        if minimum is None or value<minimum['chi_negative']:minimum=item
        if value<0:hits.append(item)
    out=dict(seconds=round(time.monotonic()-start,3),tuples=count,negative_hits=hits,minimum=minimum,
             direct_checks=len(tests),incidence_hypersurface_checks=incidence_checks,scope='Finite exploratory search using unpromoted K-theoretic Euler formulas; no universal nonexistence inference.')
    dest=Path(__file__).with_name('search_homogeneous_sections_output.json');dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
