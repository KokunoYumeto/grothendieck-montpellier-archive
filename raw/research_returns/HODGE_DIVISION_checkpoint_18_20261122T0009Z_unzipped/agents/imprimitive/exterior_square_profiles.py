#!/usr/bin/env python3
"""Exact permutation-partition spectra for scalar twists of Lambda^2 Std.

Exploratory necessary profiles only.  No tuple generation or period rank is
inferred from feasible aggregate data.  All reported ranks use integer orbit
counts; optional linear programming is a numerical exploratory filter.
"""
from collections import Counter
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path
import argparse, json, time

ROOT=Path(__file__).resolve().parent

def partitions(n, lo=1):
    if n==0:
        yield ()
    for a in range(lo,n+1):
        for p in partitions(n-a,a):
            yield (a,)+p

def fixed(part, phase):
    """Orbit count on wedge^2 permutation minus Std."""
    d=phase.denominator; a=phase.numerator
    counts=Counter(part)
    ans=0
    sizes=sorted(counts)
    for i,x in enumerate(sizes):
        b=counts[x]
        if x%d==0:
            ans+=b*((x-1)//2)
            ans+=b*(b-1)//2*x
        if x%2==0 and (2*a*(x//2)-d)%(2*d)==0:
            ans+=b
        for y in sizes[i+1:]:
            if lcm(x,y)%d==0:
                ans+=b*counts[y]*gcd(x,y)
    ans-=sum(b for x,b in counts.items() if x%d==0)
    ans+=int(phase==0)
    return ans

def rank(part, phase):
    n=sum(part)
    return (n-1)*(n-2)//2-fixed(part,phase)

def direct_spectrum(part, phase):
    ev=[]
    for x in part:
        ev.extend(Fraction(j,x) for j in range(x))
    ev.remove(Fraction(0))
    cnt=Counter((ev[i]+ev[j]+phase)%1 for i in range(len(ev)) for j in range(i+1,len(ev)))
    return cnt

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-n',type=int,default=35)
    ap.add_argument('--output',default='exterior_square_exploration.json')
    ar=ap.parse_args();start=time.time()
    phases=[Fraction(0),Fraction(1,2),Fraction(1,3),Fraction(1,4),Fraction(1,6)]
    rows=[]; direct_checks=0; rank_checks=0
    for n in range(4,ar.max_n+1):
        m=(n-1)*(n-2)//2
        minima={str(q):{'rank':m+1,'linear_defect_twice':10**9} for q in phases}
        count=0; failures=[]
        for p in partitions(n):
            count+=1; ind=n-len(p)
            for q in phases:
                if ind==0 and q==0:continue
                r=rank(p,q)
                rank_checks+=1
                if n<=12:
                    assert direct_spectrum(p,q).get(Fraction(0),0)==m-r
                    direct_checks+=1
                d=2*r-(n-4)*ind
                cur=minima[str(q)]
                if r<cur['rank']:cur.update(rank=r,rank_partition=p)
                if d<cur['linear_defect_twice']:cur.update(linear_defect_twice=d,defect_partition=p)
                if d<0:failures.append([p,str(q),r,ind,d])
                if q==0:assert 3*d>=2*n,(n,p,d)
                if q:
                    assert d>=2,(n,p,q,r,ind,d)
                    assert r>=m-(n-1)**2//4,(n,p,q,r)
        rows.append({'n':n,'m':m,'partitions':count,'minima':minima,'universal_linear_bound_failures':failures})
        print(n, min(x['linear_defect_twice'] for x in minima.values()), {q:x['linear_defect_twice'] for q,x in minima.items()},flush=True)
    # Exact symbolic arithmetic behind the all-n branch-count contradiction.
    import sympy as sp
    v=sp.symbols('v',integer=True,positive=True)
    assert sp.expand(7*v**2-(2*v*(2*v+1)+6))==3*v**2-2*v-6
    assert sp.expand(7*v*(v-1)-(2*v*(2*v-1)+6))==3*v**2-5*v-6
    # Positivity after v=2+w or v=3+w has positive coefficients.
    w=sp.symbols('w',integer=True,nonnegative=True)
    polys=[sp.Poly((3*v**2-2*v-6).subs(v,w+2),w),sp.Poly((3*v**2-5*v-6).subs(v,w+3),w)]
    assert all(all(a>0 for a in p.all_coeffs()) for p in polys)
    n=sp.symbols('n',integer=True,positive=True)
    assert sp.expand((n-4)*(n-1)+2*n+6-((n-1)*(n-2)+6))==2
    out={'status':'PASS exact finite spectral checks and symbolic uniform branch-count arithmetic; no tuple construction or generic period computation',
         'max_n':ar.max_n,'seconds':time.time()-start,'partitions':sum(x['partitions'] for x in rows),
         'rank_checks':rank_checks,'direct_spectrum_checks':direct_checks,
         'uniform_positivity_polynomials':[str(p.as_expr()) for p in polys],
         'all_n_at_least_6_budget_gap':2,'n5_budget_lower':19,'n5_required':18,
         'n4_nonreal_budget_lower':14,'n4_required':12,'rows':rows}
    (ROOT/ar.output).write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
