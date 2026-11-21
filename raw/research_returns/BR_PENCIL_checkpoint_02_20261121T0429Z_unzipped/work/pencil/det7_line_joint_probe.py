#!/usr/bin/env python3
"""Exact linear zero-pattern intersections for remaining m=12 det7 types."""
from pathlib import Path
from itertools import combinations
import argparse,json,numpy as np
from sympy import Matrix
from det7_prolongation import data,prolong,rank as modrank
from det7_typeB_line_conditions import conditions,primitive

HERE=Path(__file__).resolve().parent


def rank(rows,d):
    if not rows:return 0
    return modrank(np.array(rows,dtype=np.int64).reshape((-1,d)))[0]


def main():
    p=argparse.ArgumentParser();p.add_argument('--type',required=True);args=p.parse_args()
    D=json.loads((HERE/f'det7_type{args.type}_prolongation.json').read_text())
    S=D['subset'];variables,T,blocks,image=data(S,-1)
    U=[T[:,:,c] for c in range(len(variables))]
    base={o:modrank(prolong(U,o))[0] for o in ['A','B']}
    zero={'A':len(S)-((len(S)-1)*13-base['A']),
          'B':len(variables)-((len(variables)-1)*13-base['B'])}
    output=[]
    for rec in D['unexcluded']:
        index=rec['chosen'][0];w,block,dim=blocks[index]
        H={o:conditions(T,variables,w,block,o,S=S,image_character=w in image) for o in ['A','B']}
        candidates={}
        for o,n in [('A',len(S)),('B',len(variables))]:
            cand=[]
            for zeros in combinations(range(n),zero[o]):
                rows=[row for j in zeros for row in H[o][j]['equations']]
                if rank(rows,dim)<dim:cand.append((zeros,rows))
            candidates[o]=cand
        survivors=[]
        for az,arows in candidates['A']:
            for bz,brows in candidates['B']:
                rows=arows+brows
                if rank(rows,dim)<dim:
                    null=Matrix(rows).nullspace() if rows else [Matrix.eye(dim)[:,i] for i in range(dim)]
                    if null:survivors.append({'A_zeros':az,'B_zeros':bz,
                                             'basis':[primitive(list(v)) for v in null]})
        item={'block':index,'weight':w,'coordinates':block,'quotient_dimension':dim,
              'base_ranks':base,'necessary_zero_counts':zero,'conditions':H,
              'separate_survivor_counts':{o:len(v) for o,v in candidates.items()},
              'unexcluded':survivors}
        output.append(item)
        print(args.type,'block',index,'dim',dim,'base',base,'separate',item['separate_survivor_counts'],
              'joint_survivors',len(survivors),flush=True)
        print(json.dumps(survivors[:4]),flush=True)
    (HERE/f'det7_type{args.type}_line_joint_probe.json').write_text(json.dumps(output,indent=2)+'\n')


if __name__=='__main__':main()
