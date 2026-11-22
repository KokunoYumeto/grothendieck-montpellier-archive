#!/usr/bin/env python3
"""Exact sparse determinant specialization for the QC-005 nonic covariant.

F=(x0*x1*x2)^2*(x3^3+x0*x1*x3+x0^2*x2) is a 9x9 block determinant.
At weight (15,13,13,13), only the coefficient of A^4 B C contributes.
The five bracket powers are joined at their first two symbolic letters.
Python standard library only. No full 24^13 bracket expansion is needed.
"""
import argparse
from collections import defaultdict
from functools import lru_cache
from itertools import permutations
from math import factorial, prod
import json
import time

P=101
PERMS=list(permutations(range(4)))
UNIT=[1 << (4*i) for i in range(4)]
MASK=(1 << 16)-1
MONOMIALS=[(2,2,2,3),(3,3,2,1),(4,2,3,0)]


def parity(pi):
    return (-1)**sum(pi[i]>pi[j] for i in range(4) for j in range(i+1,4))


def row_code(a):
    return sum(value << (4*i) for i,value in enumerate(a))


def valid(a):
    return all(0 <= x <= 3 for x in a)


def det_power(power):
    terms=[(sum(1 << (16*r+4*pi[r]) for r in range(4)),parity(pi)) for pi in PERMS]
    out={0:1}
    for _ in range(power):
        nxt=defaultdict(int)
        for a,va in out.items():
            for b,vb in terms:
                nxt[a+b] += va*vb
        out={a:v % P for a,v in nxt.items() if v % P}
    return out


def decode_row(code):
    return tuple((code >> (4*k)) & 15 for k in range(4))


def build_tables():
    d3,d4=det_power(3),det_power(4)
    first=defaultdict(list)
    decoded=[]
    for key,value in d4.items():
        rows=tuple((key >> (16*i)) & MASK for i in range(4))
        decoded.append((rows,value))
        first[rows[:2]].append((rows[2],rows[3],value))
    return d3,decoded,first


def coefficient(targets,tables):
    """Coefficient in [0135]^4[1235][2345]^3[0234][0124]^4."""
    d3,terms4,by_first=tables
    codes=list(map(row_code,targets))

    @lru_cache(None)
    def middle(cD,cB,r2,r3,r4,r5):
        # The single brackets are D=[0234], B=[1235]. Their first colors
        # are fixed by the counts of letters0 and1. Remove their other
        # colors, then look up the required coefficient of [2345]^3.
        deficits=list(map(decode_row,(r2,r3,r4,r5)))
        total=0
        for D in PERMS:
            if D[0]!=cD:continue
            v2=list(deficits[0]);v3=list(deficits[1]);v4=list(deficits[2])
            v2[D[1]]-=1;v3[D[2]]-=1;v4[D[3]]-=1
            if not valid(v4) or min(v2)<0 or min(v3)<0:continue
            for B in PERMS:
                if B[0]!=cB:continue
                w2=v2[:];w3=v3[:];w5=list(deficits[3])
                w2[B[1]]-=1;w3[B[2]]-=1;w5[B[3]]-=1
                if not all(map(valid,(w2,w3,w5))):continue
                key=row_code(w2)+(row_code(w3)<<16)+(row_code(v4)<<32)+(row_code(w5)<<48)
                total += parity(D)*parity(B)*d3.get(key,0)
        return total % P

    total,joins=0,0
    for rowsA,a in terms4:
        # A=[0135]. E=[0124] shares the first two letters.
        for cD in range(4):
            need0=tuple(targets[0][k]-((rowsA[0] >> (4*k)) & 15)-(k==cD) for k in range(4))
            if min(need0)<0 or max(need0)>4:continue
            n0=row_code(need0)
            for cB in range(4):
                need1=tuple(targets[1][k]-((rowsA[1] >> (4*k)) & 15)-(k==cB) for k in range(4))
                if min(need1)<0 or max(need1)>4:continue
                n1=row_code(need1)
                for row2,row4,e in by_first.get((n0,n1),[]):
                    base=(row2,rowsA[2],row4,rowsA[3])
                    residual=[]
                    for v,used in zip(range(2,6),base):
                        values=tuple(targets[v][k]-((used >> (4*k)) & 15) for k in range(4))
                        if min(values)<0 or max(values)>5:break
                        residual.append(row_code(values))
                    if len(residual)!=4:continue
                    joins+=1
                    total += a*e*middle(cD,cB,*residual)
    return total % P,joins,middle.cache_info()._asdict()


def check():
    started=time.monotonic()
    tables=build_tables()
    records=[]
    total=0
    for b in range(6):
        for c in range(6):
            if b==c:continue
            targets=[list(MONOMIALS[1] if i==b else MONOMIALS[2] if i==c else MONOMIALS[0])
                     for i in range(6)]
            targets[4][0]-=1;targets[5][0]-=1
            value,joins,cache=coefficient(targets,tables)
            total=(total+value) % P
            record=dict(B_letter=b,C_letter=c,coefficient=value,joins=joins,cache=cache)
            records.append(record)
            print(json.dumps(record),flush=True)
    factor=prod(factorial(a) for a in MONOMIALS[0])**4
    factor*=prod(factorial(a) for a in MONOMIALS[1])*prod(factorial(a) for a in MONOMIALS[2])
    differential=total*factor % P
    assert len(tables[0]) == 1848 and len(tables[1]) == 10147
    assert total == 64 and factor % P == 81 and differential == 33
    return dict(prime=P,det3_power_terms=len(tables[0]),det4_power_terms=len(tables[1]),
                coefficient_sum=total,derivative_factor=factor % P,
                integer_differential_value=differential,
                seconds=round(time.monotonic()-started,3),assignments=records)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output')
    args=parser.parse_args()
    result=check()
    print(json.dumps(result,indent=2),flush=True)
    if args.output:
        with open(args.output,'w') as f:json.dump(result,f,indent=2);f.write('\n')
