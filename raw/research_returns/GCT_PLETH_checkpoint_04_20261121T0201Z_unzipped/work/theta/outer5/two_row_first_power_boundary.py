#!/usr/bin/env python3
"""T045: k=1,c=1,b=B+1; exact fixed two-variable boundary certificate."""
from pathlib import Path
from math import comb
import hashlib,json
import numpy as np
import sympy as sp
from two_row_ray_certificate import LABELS,CLASSES,WEIGHTS,schur_terms

HERE=Path(__file__).resolve().parent

def trace(g,x,B):
    a,b,c=schur_terms(g,x,B+1);e=CLASSES[g].count(1)-1
    return -a+e*b-(e+1)*c

def main():
    x,B=sp.symbols('x B');b=B+1;a=b+x
    P=(x+1)*(b+x+2)*(b+1)*(2*(b+3)*(b+x+4)-30)
    poly=sp.Poly(P,x,B)
    assert all(v>0 for e,v in poly.terms())
    assert poly.total_degree()==5 and poly.degree(x)==3 and poly.degree(B)==4
    arrays=[np.array([[trace(g,xx,bb) for bb in range(300)] for xx in range(240)],dtype=np.int64) for g in range(7)]
    bound=max(sum(abs(w)*int(np.abs(v).max()) for w,v in zip(row,arrays)) for row in WEIGHTS)
    assert bound*2**7<2**63
    summary={};total=0;negative=[]
    for mu,weights in zip(LABELS,WEIGHTS):
        key=','.join(map(str,mu));values=sum(w*v for w,v in zip(weights,arrays))
        assert np.all(values%120==0);values//=120
        assert values.min()>=0
        minimum={};maximum={};hasher=hashlib.sha256();zeros=[]
        for i in range(4):
            for j in range(5):
                value=np.zeros((60,60),dtype=np.int64)
                for u in range(i+1):
                    for v in range(j+1):
                        value+=(-1)**(i+j-u-v)*comb(i,u)*comb(j,v)*values[60*u:60*(u+1),60*v:60*(v+1)]
                lo=int(value.min());hi=int(value.max());slot=f'{i},{j}'
                minimum[slot]=lo;maximum[slot]=hi
                hasher.update(value.astype('<i8',copy=False).tobytes(order='C'));total+=value.size
                if lo<0:negative.append(dict(label=key,orders=[i,j],minimum=lo))
                if i==j==0:zeros=[list(map(int,p)) for p in np.argwhere(value==0)]
        summary[key]=dict(minima=minimum,maxima=maximum,zero_pairs=zeros,table_sha256=hasher.hexdigest())
    result=dict(statement='T-045 first-power boundary',parameters='x>=0,b=B+1>=1,k=1,c=1',
                verified_entries=total,negative_blocks=negative,summary=summary,signed64_bound=bound*2**7,
                hash_order='i=0..3,j=0..4; residue x,B C order; little-endian signed64')
    (HERE/'TWO_ROW_FIRST_POWER_SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
    message=f'PASS: {total} exact nonnegative mixed Newton constants; {len(negative)} negative blocks.\n'
    for key,row in summary.items():message+=f'{key}: zeros {row["zero_pairs"]}.\n'
    (HERE/'TWO_ROW_FIRST_POWER_CHECK.txt').write_text(message);print(message,flush=True)
    assert not negative

if __name__=='__main__':main()
