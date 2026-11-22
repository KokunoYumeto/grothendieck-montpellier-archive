#!/usr/bin/env python3
"""Exact finite checks only; no stack or geometric proof is certified here."""
import argparse
import hashlib
import json
from pathlib import Path
import time

ap=argparse.ArgumentParser()
ap.add_argument('--output',default='parts/D/post18_research/output/residual_Frobenius_labels.json')
args=ap.parse_args()
started=time.perf_counter()
checks=0

def check(value):
    global checks
    assert value
    checks+=1

prime_powers=[(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(7,2)]
for p,f in prime_powers:
    q=p**f
    n=q-1
    labels=[1+n*j for j in range(n)]
    image=[]
    for j,c in enumerate(labels):
        out=q*c%(n*n)
        check(out==(1+n*((j+1)%n))%(n*n))
        check(out%n==1%n)
        image.append(((out-1)//n)%n)
    check(sorted(image)==list(range(n)))
    orbit=[]
    j=0
    while j not in orbit:
        orbit.append(j)
        j=(j+1)%n
    check(len(orbit)==n and j==0)

for n in range(2,18):
    for depth in range(1,6):
        for a in range(n):
            exponents=[e for e in range(n*depth) if e%n==a]
            check(exponents==[a+n*b for b in range(depth)])
            check(len(exponents)==depth)
            for c in range(n):
                carry=(a+c)//n
                check(carry in (0,1))
                check(a+c==(a+c)%n+n*carry)
            for p in (2,3,5,7):
                if n%p==0:
                    continue
                carry=p*a//n
                check(0<=carry<=p-1)
                check(p*a==(p*a)%n+n*carry)

record={'id':'D:residual-twisted-Frobenius-transport','status':'PASS','assertions':checks,'seconds':time.perf_counter()-started,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite weight-label translations and graded slot/carry arithmetic only; excludes gerbe geometry, category descent, and the unresolved global atlas.'}
out=Path(args.output)
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
