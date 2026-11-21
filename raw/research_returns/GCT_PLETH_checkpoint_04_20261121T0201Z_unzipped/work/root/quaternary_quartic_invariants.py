#!/usr/bin/env python3
"""Exact SL4 multiplicities in Sym^k(Sym^4 C4), through k=20."""
from itertools import permutations
from pathlib import Path
import csv

def sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))

def main(K=20):
    top=K+3
    base=top+1
    steps=(base**3,base**2,base,1)
    size=base**4
    coeff=[0]*size
    coeff[0]=1
    weights=[(a,b,c,4-a-b-c) for a in range(5) for b in range(5-a) for c in range(5-a-b)]
    for idx,w in enumerate(weights):
        delta=sum(x*y for x,y in zip(w,steps))
        for a in range(w[0],top+1):
            for b in range(w[1],top+1):
                for c in range(w[2],top+1):
                    prefix=((a*base+b)*base+c)*base
                    dmin=w[3]
                    dmax=min(top,4*K-a-b-c)
                    for d in range(dmin,dmax+1):
                        if (a+b+c+d)%4==0:
                            j=prefix+d
                            coeff[j]+=coeff[j-delta]
        print('factor',idx+1,'of',len(weights),flush=True)
    rho=(3,2,1,0)
    pp=[(p,sign(p)) for p in permutations(range(4))]
    rows=[]
    for k in range(K+1):
        multiplicity=0
        for p,sgn in pp:
            w=tuple(k+rho[i]-rho[p[i]] for i in range(4))
            if min(w)>=0:
                multiplicity+=sgn*coeff[sum(x*y for x,y in zip(w,steps))]
        assert multiplicity>=0,(k,multiplicity)
        rows.append((k,multiplicity))
    path=Path(__file__).with_name('QUATERNARY_QUARTIC_INVARIANTS.tsv')
    with path.open('w') as f:
        out=csv.writer(f,delimiter='\t')
        out.writerow(['degree','SL4_invariant_multiplicity'])
        out.writerows(rows)
    print(rows)

if __name__=='__main__':
    main()
