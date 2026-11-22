#!/usr/bin/env python3
"""Find minimal non-dominant nested profiles and their stabilized multiplicities.

This is a finite character calculation, not a determinant rank calculation.
The centered generators are Sym^2 C^3 through Sym^n C^3. Only standard
Python is used; a single bounded knapsack handles every requested profile.
"""
from itertools import combinations_with_replacement, permutations
import argparse,json,time


def count(p):
    b,c,e=p
    return sum(b-u+1 for z in range(e+1) for u in range(z,c+1))


def table(n):
    caps=(n+2,n+1,n)
    B,C,E=caps;sy=E+1;sx=(C+1)*sy
    values=[0]*((B+1)*sx);values[0]=1
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                if a+b+c<2:continue
                delta=a*sx+b*sy+c
                for i in range(a,B+1):
                    for j in range(b,C+1):
                        first=i*sx+j*sy
                        for k in range(c,E+1):
                            index=first+k
                            values[index]+=values[index-delta]
    return values,sx,sy


def multiplicity(profile,tab):
    values,sx,sy=tab
    result=0;terms=[]
    for perm in permutations(range(3)):
        alpha=tuple(profile[j]+perm[j]-j for j in range(3))
        parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        value=0 if min(alpha)<0 else values[alpha[0]*sx+alpha[1]*sy+alpha[2]]
        result+=parity*value
        terms.append(dict(weight=alpha,sign=parity,count=value))
    assert result>=0
    return result,terms


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('n',type=int,choices=(9,23));p.add_argument('--output',required=True)
    args=p.parse_args();start=time.monotonic();n=args.n
    profiles=[v[::-1] for v in combinations_with_replacement(range(n+1),3)]
    bad={v for v in profiles if count(v)>2*n*n+2}
    minimal=[v for v in sorted(bad) if not any(
        tuple(v[j]-int(j==i) for j in range(3)) in bad for i in range(3))]
    tab=table(n);results=[]
    for profile in minimal:
        a,terms=multiplicity(profile,tab);d=sum(profile)
        results.append(dict(profile=profile,coordinates=count(profile),
           stabilized_degree=d,partition=(n*d-d,)+profile,
           ambient_multiplicity=a,centered_weyl_terms=terms))
    out=dict(n=n,dimension_bound=2*n*n+2,minimal_nondominant_profiles=len(minimal),
             results=results,elapsed_seconds=round(time.monotonic()-start,3))
    with open(args.output,'w') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({**out,'results':[{k:v for k,v in t.items() if k!='centered_weyl_terms'} for t in results]}))


if __name__=='__main__':main()
