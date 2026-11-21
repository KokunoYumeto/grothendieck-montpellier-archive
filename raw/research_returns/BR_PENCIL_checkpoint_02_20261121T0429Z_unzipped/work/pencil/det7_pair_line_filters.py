#!/usr/bin/env python3
"""Uniform single-line increment and weight-overlap bounds for r=13 two-line cases."""
from pathlib import Path
from itertools import combinations
import argparse,json,numpy as np
from det7_prolongation import data,quad_weight,var_weight,prolong,rank
from det7_typeB_line_conditions import conditions

HERE=Path(__file__).resolve().parent


def matrix_rank(rows,d):
    if not rows:return 0
    return rank(np.array(rows,dtype=np.int64).reshape((-1,d)))[0]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--type',required=True)
    parser.add_argument('--orientation',choices=['A','B'],default='A')
    args=parser.parse_args()
    D=json.loads((HERE/f'det7_type{args.type}_prolongation.json').read_text())
    S=D['subset'];variables,T,blocks,image=data(S,-1)
    U=[T[:,:,c] for c in range(len(variables))]
    orientation=args.orientation
    base=rank(prolong(U,orientation))[0]
    factor=len(S) if orientation=='A' else len(variables)
    allowed=(factor-1)*13-base
    used=sorted({i for case in D['unexcluded'] for i in case['chosen']})
    info={}
    for index in used:
        w,block,dim=blocks[index]
        C=conditions(T,variables,w,block,orientation,S=S,image_character=w in image)
        maxzero=0;maxsets=[]
        for count in range(factor,-1,-1):
            surviving=[]
            for zeros in combinations(range(factor),count):
                equations=[row for j in zeros for row in C[j]['equations']]
                if matrix_rank(equations,dim)<dim:surviving.append(zeros)
            if surviving:
                maxzero=count;maxsets=surviving;break
        info[index]={'conditions':C,'min_increment':factor-maxzero,
                     'maximum_zero_sets':maxsets,'dimension':dim,
                     'weight':w,'coordinates':block}
        print(args.type,orientation,'weight',index,'dim',dim,'min_increment',factor-maxzero,flush=True)
    fw=[tuple(-x for x in quad_weight(q)) for q in S] if orientation=='A' else [var_weight(v) for v in variables]
    excluded=[];remaining=[]
    for case in D['unexcluded']:
        if len(case['chosen'])!=2:
            remaining.append({'pair':case['chosen'],'reason':'same-weight plane'})
            continue
        i,j=case['chosen'];wi,wj=blocks[i][0],blocks[j][0]
        left={tuple(x+y for x,y in zip(wi,w)) for w in fw}
        right={tuple(x+y for x,y in zip(wj,w)) for w in fw}
        overlap=len(left&right)
        lower=info[i]['min_increment']+info[j]['min_increment']-overlap
        entry={'pair':[i,j],'overlapping_weights':overlap,'lower_increment':lower}
        (excluded if lower>allowed else remaining).append(entry)
    output={'type':args.type,'orientation':orientation,'base_rank':base,'allowed_increment':allowed,
            'block_info':info,'excluded':excluded,'remaining':remaining}
    (HERE/f'det7_type{args.type}_{orientation}_filters.json').write_text(json.dumps(output,indent=2)+'\n')
    print('TYPE',args.type,'orientation',orientation,'base',base,'allowed',allowed,
          'excluded',len(excluded),'remaining',len(remaining),flush=True)
    print(json.dumps(remaining,indent=2))


if __name__=='__main__':main()
