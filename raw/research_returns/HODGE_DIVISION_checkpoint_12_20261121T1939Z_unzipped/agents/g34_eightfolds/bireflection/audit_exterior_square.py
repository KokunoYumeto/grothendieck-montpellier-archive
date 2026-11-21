#!/usr/bin/env python3
"""Independent exact eigenvalue check of D-EX01, without importing its code."""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
from math import gcd,lcm
from pathlib import Path
import json,hashlib

def parts(n,least=1):
    if n==0: yield (); return
    for a in range(least,n+1):
        for tail in parts(n-a,a): yield (a,)+tail

def main():
    count=checks=0
    for n in range(4,13):
        for ls in parts(n):
            count+=1
            ev=[F(j,a) for a in ls for j in range(a)]
            ev.remove(F(0))
            wedge=Counter((a+b)%1 for a,b in combinations(ev,2))
            m=(n-1)*(n-2)//2; k=n-len(ls)
            denominator=lcm(*ls)
            phases=[F(j,denominator) for j in range(denominator)]
            phases.append(F(1,denominator+1))
            for x in phases:
                e=x.denominator
                fixed=sum(gcd(a,b) for a,b in combinations(ls,2) if lcm(a,b)%e==0)
                for a in ls:
                    if a%e==0:fixed+=(a-1)//2
                    if a%2==0 and (x*(a//2))%1==F(1,2):fixed+=1
                fixed-=sum(a%e==0 for a in ls)
                if x==0:fixed+=1
                assert fixed==wedge.get((-x)%1,0),(n,ls,x,fixed,wedge)
                D=m-fixed
                if x:
                    assert D>=F((n-4)*k,2)+1
                    assert D>=m-((n-1)**2)//4
                elif k:
                    assert D>=F((n-4)*k,2)+F(n,3)
                checks+=1
    out={'status':'PASS','n_range':[4,12],'partitions':count,'phase_checks':checks,
         'method':'independent Fraction eigenvalue pairs and signed orbit formula',
         'original_checker_imported':False,
         'uniform_proof_verified_separately':True,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
