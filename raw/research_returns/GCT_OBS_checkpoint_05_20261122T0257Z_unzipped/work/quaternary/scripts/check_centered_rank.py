#!/usr/bin/env python3
"""Plain scalar Gaussian rank/minor check of the centered evaluation matrix.

Python standard library only. This intentionally uses ordinary scalar
arithmetic, independently of all packed-lane arithmetic in other checkers.
The input matrix must first be certified by verify_centered_evaluations.py.
"""
import argparse
import hashlib
import json
from pathlib import Path
from time import monotonic


def rank_and_minor(matrix,prime):
    a=[list(row) for row in matrix]
    rows=len(a);columns=len(a[0])
    rank=0;determinant=1;selected=[]
    for column in range(columns):
        pivot=next((i for i in range(rank,rows) if a[i][column]),None)
        if pivot is None:continue
        if pivot!=rank:
            a[pivot],a[rank]=a[rank],a[pivot]
            determinant=-determinant % prime
        value=a[rank][column]
        determinant=determinant*value % prime
        inverse=pow(value,prime-2,prime)
        pivot_tail=[v*inverse % prime for v in a[rank][column+1:]]
        for i in range(rank+1,rows):
            factor=a[i][column]
            if factor:
                a[i][column+1:]=[(v-factor*w)%prime
                                 for v,w in zip(a[i][column+1:],pivot_tail)]
                a[i][column]=0
        selected.append(column);rank+=1
        if rank==rows:break
    return rank,selected,determinant


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir',type=Path,default=Path('work/support_lmr/results/bracket_evaluation'))
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--expected-dimension',type=int,default=804)
    parser.add_argument('--first-columns',type=int)
    args=parser.parse_args();started=monotonic()
    metadata=json.loads((args.data_dir/'matrix.json').read_text())
    raw=(args.data_dir/'matrix.bin').read_bytes();r,c=metadata['shape']
    assert len(raw)==r*c
    used_columns=min(c,args.first_columns) if args.first_columns else c
    matrix=[raw[i*c:i*c+used_columns] for i in range(r)]
    assert all(v<metadata['prime'] for row in matrix for v in row)
    rank,columns,determinant=rank_and_minor(matrix,metadata['prime'])
    result=dict(prime=metadata['prime'],shape=[r,c],tested_columns=used_columns,rank=rank,
                full_row_rank=rank==r,complete_gate=r==args.expected_dimension,
                selected_columns=columns,
                minor_mod_prime=determinant if rank==r else None,
                matrix_sha256=hashlib.sha256(raw).hexdigest(),
                seconds=round(monotonic()-started,3))
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='selected_columns'}),flush=True)
