#!/usr/bin/env python3
"""Independent actual permutation-orbit certificate for D-UP small degrees."""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib,json

def partitions(n,least=1):
    if not n: yield (); return
    for q in range(least,n+1):
        for rest in partitions(n-q,q): yield (q,)+rest

def main():
    rows=[]; total_parts=total_phases=0
    for n in range(5,11):
        best=n*n; pc=ph=0
        for ls in partitions(n):
            pc+=1
            perm=list(range(n));offset=0
            for q in ls:
                for j in range(q):perm[offset+j]=offset+(j+1)%q
                offset+=q
            remaining=set(combinations(range(n),2)); pair_eigen=Counter()
            while remaining:
                first=min(remaining);current=first;orbit=[]
                while True:
                    orbit.append(current);remaining.remove(current)
                    current=tuple(sorted((perm[current[0]],perm[current[1]])))
                    if current==first:break
                size=len(orbit)
                pair_eigen.update(F(j,size) for j in range(size))
            letters=Counter(F(j,q) for q in ls for j in range(q))
            W=pair_eigen.copy();W.subtract(letters)
            assert all(v>=0 for v in W.values())
            m=n*(n-3)//2
            assert sum(W.values())==m
            for phase,mult in W.items():
                if not mult:continue
                if ls==(1,)*n and phase==0:continue
                ph+=1
                D=m-mult
                assert D>=n-3,(n,ls,phase,D)
                best=min(best,D)
            best=min(best,m) # all off-spectrum phases
        assert best==n-3 and 12*best>n*(n-3)+6
        rows.append({'n':n,'dimension':n*(n-3)//2,'partitions':pc,
                     'matching_phases':ph,'minimum_moving_rank':best,
                     'twelve_branch_lower_bound':12*best,'sixfold_budget':n*(n-3)+6})
        total_parts+=pc;total_phases+=ph
    result={'status':'PASS','method':'explicit action on unordered pairs and exact orbit spectra',
            'original_implementation_imported':False,'total_partitions':total_parts,
            'total_matching_phases':total_phases,'rows':rows,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
