#!/usr/bin/env python3
"""All-scalar exact S^(n-2,2) spectral certificate, n=5,...,10.

For each partition, every scalar that can have a fixed vector is tested;
all other scalar phases have moving rank equal to the entire dimension.
Two separate eigenvalue constructions are compared exactly.  This proves
infeasibility of the necessary twelve-branch rank budget in these degrees,
not existence of tuples or any period-map dominance.
"""
from collections import Counter
from fractions import Fraction
from math import gcd,lcm
from pathlib import Path
import argparse,json,time

ROOT=Path(__file__).resolve().parent

def partitions(n,lo=1):
    if n==0:yield ()
    for a in range(lo,n+1):
        for p in partitions(n-a,a):yield (a,)+p

def add_regular(out,order,times=1):
    for j in range(order):out[Fraction(j,order)]+=times

def pair_orbit_spectrum(part):
    out=Counter()
    for i,a in enumerate(part):
        add_regular(out,a,(a-1)//2)
        if a%2==0:add_regular(out,a//2)
        for b in part[i+1:]:add_regular(out,lcm(a,b),gcd(a,b))
    for a in part:add_regular(out,a,-1)
    assert all(v>=0 for v in out.values())
    return Counter({q:v for q,v in out.items() if v})

def symmetric_standard_spectrum(part):
    perm=[]
    for a in part:perm.extend(Fraction(j,a) for j in range(a))
    std=perm.copy();std.remove(Fraction(0))
    out=Counter((std[i]+std[j])%1 for i in range(len(std)) for j in range(i,len(std)))
    for q in perm:out[q]-=1
    assert all(v>=0 for v in out.values())
    return Counter({q:v for q,v in out.items() if v})

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-n',type=int,default=10)
    ar=ap.parse_args();start=time.time();rows=[];checks=0;total=0
    for n in range(5,ar.max_n+1):
        m=n*(n-3)//2; minimum=m; witness=None;pc=0
        for part in partitions(n):
            pc+=1;total+=1;k=n-len(part)
            spec=pair_orbit_spectrum(part)
            assert spec==symmetric_standard_spectrum(part)
            assert sum(spec.values())==m
            for eig,mult in spec.items():
                if eig==0 and k==0:continue
                phase=(-eig)%1;D=m-mult;checks+=1
                assert D>0,(n,part,phase)
                if phase==0:assert 4*D>=2*(n-5)*k+n,(n,part,phase,D)
                else:assert 2*D>=(n-5)*k+n-4,(n,part,phase,D)
                if D<minimum:minimum=D;witness={'partition':part,'scalar_phase':str(phase),'spectrum':{str(q):v for q,v in sorted(spec.items())}}
            # Phases not among negatives of eigenvalues have D=m.
            assert 2*m>=(n-5)*k+n-4
        if n<=10:
            assert minimum==n-3
            assert 12*minimum>2*m+6
        rows.append({'n':n,'dimension':m,'partitions':pc,'minimum_moving':minimum,'twelve_branch_lower':12*minimum,'required_moving':2*m+6,'witness':witness})
    out={'status':'PASS exact all-scalar partition spectra and finite necessary-budget obstruction','max_n':ar.max_n,'partitions':total,'all_matching_scalar_checks':checks,'seconds':time.time()-start,'rows':rows,
         'off_spectrum_scalars':'moving rank equals full dimension; checked separately',
         'n4':'dimension2; cohomological multiplicity6 forces at most10 branches on P1, hence rank<=7',
         'all_n_at_least_11':'proved symbolically in accompanying text; budget gap at least(n-10)/2>0'}
    (ROOT/'unordered_pair_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
