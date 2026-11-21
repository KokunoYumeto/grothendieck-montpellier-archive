#!/usr/bin/env python3
"""Enumerate G-012's positive monomials and compare with independent G-007."""
from collections import Counter
from pathlib import Path
import csv
from check_degree_three import parts3, form

def run(N=50):
    actual=Counter()
    for epsilon in (0,1):
        for delta in (0,1):
            for e in range((N-3*epsilon-3*delta)//2+1):
                for c in range((N-3*epsilon-3*delta-2*e)//4+1):
                    for b in range((N-3*epsilon-3*delta-2*e-4*c)//2+1):
                        rest=N-3*epsilon-3*delta-2*e-4*c-2*b
                        for a in range(rest+1):
                            n=a+2*b+4*c+2*e+3*epsilon+3*delta
                            lam=(3*a+4*b+6*c+2*e+6*epsilon+4*delta,
                                 2*b+6*c+2*e+3*epsilon+4*delta,
                                 2*e+delta)
                            assert sum(lam)==3*n and lam[0]>=lam[1]>=lam[2]
                            actual[n,lam]+=1
    rows=[]
    for n in range(1,N+1):
        count=0
        for lam in parts3(3*n):
            assert actual[n,lam]==form(n,lam)[0],(n,lam,actual[n,lam],form(n,lam))
            count+=1
        rows.append((n,count,'PASS'))
    with Path(__file__).with_name('RANK_THREE_PRESENTATION_CHECK.tsv').open('w') as f:
        out=csv.writer(f,delimiter='\t')
        out.writerow(['n','all_partitions_checked','status'])
        out.writerows(rows)
    print('PASS:',sum(x[1] for x in rows),'complete coefficients, n=1..',N)

if __name__=='__main__':
    run()
