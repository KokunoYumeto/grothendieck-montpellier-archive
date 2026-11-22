#!/usr/bin/env python3
"""Exact inverse-series and normalization checks for S-007; stdlib only.

The proof is uniform in m,n. This checker independently forms the truncated
inverse series for each basis coefficient B_j and multiplies it back by
(1+l*t)^(n-m), so every coefficient identity is checked symbolically in l.
"""
import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path


def check_pair(m,n):
    r=n-m
    assert m%2==0 and n>m
    rows=[]
    for j in range(m+1):
        quotient=[0]*(m+1)
        for k in range(j,m+1):
            quotient[k]=(-1)**(k-j)*comb(r+k-j-1,k-j)
        product=[sum(comb(r,i)*quotient[k-i]
                     for i in range(min(r,k)+1) if 0<=k-i<=m)
                 for k in range(m+2)]
        assert product[:m+1]==[int(k==j) for k in range(m+1)]
        ordinary=(-1)**(m-j)*comb(n-j,m+1-j)
        assert product[m+1]==ordinary
        normalized=Fraction(ordinary*comb(n,j),comb(n,m+1))
        assert normalized==(-1)**(m-j)*comb(m+1,j)
        rows.append(dict(input_jet=j,ordinary=ordinary,normalized=int(normalized)))
    return dict(m=m,n=n,coefficients=rows)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('work/support_lmr/results/even_padding.json'))
    args=parser.parse_args()
    pairs=[(m,n) for m in (2,4,8,16) for n in (m+1,m+2,2*m+3)]
    pairs.append((16,23))
    result=dict(statement='S-007',pairs=[check_pair(m,n) for m,n in pairs],
                total_coefficient_identities=sum(m+1 for m,n in pairs),passed=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='pairs'}))


if __name__=='__main__':main()
