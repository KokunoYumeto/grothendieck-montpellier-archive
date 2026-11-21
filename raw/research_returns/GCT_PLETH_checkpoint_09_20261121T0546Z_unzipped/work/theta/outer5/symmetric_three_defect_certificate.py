#!/usr/bin/env python3
"""T048 b=0 branch: s=3,k=K+8; exact 403200-constant certificate."""
from pathlib import Path
from math import comb
import hashlib,json
import numpy as np
import sympy as sp
from two_row_ray_certificate import LABELS,CLASSES,WEIGHTS,h
from stable_defect_correction import trace_from_fixed_pairs

HERE=Path(__file__).resolve().parent

def correction(g,x,b=0):
    if b:
        if g==0:return 60*(x+1)
        if g==1:return 6*(-1)**b*int(x%2==0)
        return 0
    if g==0:return 50*x+40
    if g==1:return 1+3*int(x%2==0)-x
    if g==2:return 2*int(x%2==1)
    if g in (3,4):return -(1,-1,0)[(x+1)%3]
    return 0

def main():
    for x in range(120):
        for b in range(4):
            for g in range(7):assert correction(g,x,b)==trace_from_fixed_pairs(x,b,3,g)
    x,K=sp.symbols('x K');k=K+8;c=2*K+13
    P=(x+1)*(x+2)*((c+1)*(c+2)*(x+c+3)-5*k*(k+1)*(k+2))+12*(50*x+40)
    pol=sp.Poly(P,x,K)
    assert all(v>0 for e,v in pol.terms())
    assert pol.total_degree()==5 and pol.degree_list()==(3,3)
    traces=[];classbounds=[]
    for g,cyc in enumerate(CLASSES):
        hx=np.array([h(g,v) for v in range(240)],dtype=np.int64)
        hp=np.array([h(g,v-1) for v in range(240)],dtype=np.int64)
        C=np.array([h(g,2*v+13)-cyc.count(1)*h(g,v+7) for v in range(240)],dtype=np.int64)
        B=np.array([h(g,2*v+12)-cyc.count(1)*h(g,v+7) for v in range(240)],dtype=np.int64)
        corr=np.array([correction(g,v) for v in range(240)],dtype=np.int64)
        bound=int(np.abs(hx).max())*int(np.abs(C).max())+int(np.abs(hp).max())*int(np.abs(B).max())+int(np.abs(corr).max())
        assert bound<2**63
        traces.append(hx[:,None]*C[None,:]-hp[:,None]*B[None,:]+corr[:,None]);classbounds.append(bound)
    bound=max(sum(abs(w)*v for w,v in zip(row,classbounds)) for row in WEIGHTS)*64
    assert bound<2**63
    result={};total=0;bad=[]
    for label,row in zip(LABELS,WEIGHTS):
        values=sum(w*v for w,v in zip(row,traces));assert np.all(values%120==0);values//=120
        assert values.min()>=0
        low={};high={};hasher=hashlib.sha256();zeros=[]
        for i in range(4):
            for j in range(4):
                val=sum((-1)**(i+j-u-v)*comb(i,u)*comb(j,v)*values[60*u:60*(u+1),60*v:60*(v+1)] for u in range(i+1) for v in range(j+1))
                if i==j==3:assert not np.any(val)
                lo=int(val.min());hi=int(val.max());slot=f'{i},{j}';low[slot]=lo;high[slot]=hi
                if lo<0:bad.append((label,i,j,lo))
                hasher.update(val.astype('<i8',copy=False).tobytes(order='C'));total+=val.size
                if i==j==0:zeros=[list(map(int,p)) for p in np.argwhere(val==0)]
        result[','.join(map(str,label))]=dict(minima=low,maxima=high,zero_pairs=zeros,table_sha256=hasher.hexdigest())
    summary=dict(statement='T-048 b=0',verified_entries=total,negative_blocks=bad,summary=result,
                 signed64_intermediate_bound=bound,hash_order='i,j=0..3; residues x,K C order; signed64littleendian')
    (HERE/'SYMMETRIC_THREE_DEFECT_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    message=f'PASS: {total} exact Newton constants; {len(bad)} negative blocks;3360 closed-correction comparisons.\n'
    for key,row in result.items():message+=f'{key}: zeros{row["zero_pairs"]}.\n'
    (HERE/'SYMMETRIC_THREE_DEFECT_CHECK.txt').write_text(message);print(message,flush=True)
    assert not bad

if __name__=='__main__':main()
