#!/usr/bin/env python3
"""Exact ambient multiplicities for candidates outside the certified jet region.
This is a candidate sieve, NOT a multiplicity-obstruction certificate.
"""
from itertools import product
import argparse
import json
import time
from plethysm_four_rows import weight_table, multiplicity


def partitions4(total):
    for e in range(1,total//4+1):
        for c in range(e,(total-e)//3+1):
            for b in range(c,(total-c-e)//2+1):
                yield (total-b-c-e,b,c,e)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('n',type=int,choices=(9,23))
    p.add_argument('degrees',type=int,nargs='+')
    p.add_argument('--output',required=True)
    args=p.parse_args()
    out=[]
    coefficient_tails=[(b,c,e) for b in range(args.n+1)
                       for c in range(args.n-b+1) for e in range(args.n-b-c+1)]
    for d in args.degrees:
        started=time.monotonic()
        total=args.n*d
        table=weight_table(args.n,d,(total//2+2,total//3+1,total//4))
        candidates=[]; zeros=0; ambient_total=0
        for lam in partitions4(total):
            a=multiplicity(args.n,d,lam,table)['multiplicity']
            assert a>=0
            ambient_total+=a
            if not a:
                zeros+=1
                continue
            count=sum(b+c+e<=lam[1] and c+e<=lam[2] and e<=lam[3]
                      for b,c,e in coefficient_tails)
            if count<=2*args.n**2+2:
                continue
            candidates.append(dict(partition=lam,ambient=a,support_coordinates=count))
        result=dict(n=args.n,degree=d,four_row_ambient_multiplicity_sum=ambient_total,
                    zero_multiplicity_partitions=zeros,remaining=len(candidates),
                    remaining_multiplicity_one=sum(x['ambient']==1 for x in candidates),
                    candidates=candidates,elapsed_seconds=round(time.monotonic()-started,3))
        out.append(result)
        with open(args.output,'w') as f:
            json.dump(out,f,indent=2);f.write('\n')
        print(json.dumps({k:v for k,v in result.items() if k!='candidates'}),flush=True)


if __name__=='__main__':main()
