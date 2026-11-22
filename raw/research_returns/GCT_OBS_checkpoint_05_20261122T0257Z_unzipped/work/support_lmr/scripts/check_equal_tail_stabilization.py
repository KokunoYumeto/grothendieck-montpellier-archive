#!/usr/bin/env python3
"""Exact outer-degree character tables for the equal-tail-eight/nine gates.

One integral dynamic program counts monomials by their three tail weights
and number of non-pure-first-coordinate coefficient factors. Adding the
pure first coefficient fills the remaining outer degree uniquely. The
24-term GL4 Weyl denominator gives each actual plethysm multiplicity.
No matrix rank, normalization equality or divisibility is assumed.
"""
import argparse
from itertools import permutations
import json
from pathlib import Path
import time


def table(n,cap,degree):
    base=cap+1;size=base**3
    counts=[[0]*size for _ in range(degree+1)];counts[0][0]=1
    for a in range(min(n,cap)+1):
        for b in range(min(n-a,cap)+1):
            for c in range(min(n-a-b,cap)+1):
                if a+b+c==0:continue
                delta=a*base*base+b*base+c
                for k in range(1,degree+1):
                    src=counts[k-1];dest=counts[k]
                    for x in range(a,base):
                        for y in range(b,base):
                            start=(x*base+y)*base+c
                            stop=(x*base+y+1)*base
                            for index in range(start,stop):dest[index]+=src[index-delta]
    for k in range(1,degree+1):
        for index in range(size):counts[k][index]+=counts[k-1][index]
    return counts


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path('work/support_lmr/results/equal_tail_stabilization.json'))
    args=ap.parse_args();start=time.monotonic();n=9;cap=11;degree=27;base=cap+1
    counts=table(n,cap,degree)
    rho=(3,2,1,0)
    signed=[(p,(-1)**sum(p[i]<p[j] for i in range(4) for j in range(i+1,4)))
            for p in permutations(rho)]
    result={}
    for c,stable in [(8,804),(9,2386)]:
        rows=[]
        for d in range(4,3*c+1):
            shape=(n*d-3*c,c,c,c);value=0
            assert shape[0]>=shape[1]
            for p,sign in signed:
                target=tuple(shape[i]+rho[i]-p[i] for i in range(4))
                if min(target)<0:continue
                x,y,z=target[1:]
                value+=sign*counts[d][(x*base+y)*base+z]
            rows.append(dict(degree=d,partition=list(shape),multiplicity=value))
        expected_path=Path('work/support_lmr/results')/('c%d_all_outer_degree_characters.json'%c)
        expected=json.loads(expected_path.read_text())
        assert [r['multiplicity'] for r in rows]==[int(r['multiplicity']) for r in expected]
        assert all(r['multiplicity']==stable for r in rows if r['degree']>=16)
        assert next(r['multiplicity'] for r in rows if r['degree']==15)==stable-3 if c==9 else next(r['multiplicity'] for r in rows if r['degree']==15)==stable-1
        result[str(c)]=dict(rows=rows,first_stable_degree=16,stable_multiplicity=stable)
    output=dict(status='PASS',inner_degree=9,tables=result,
                elapsed_seconds=time.monotonic()-start,
                interpretation='F0 multiplication is injective; equality to the complete centered upper bound at degree16 proves stabilization for all later degrees.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='tables'}))


if __name__=='__main__':main()
