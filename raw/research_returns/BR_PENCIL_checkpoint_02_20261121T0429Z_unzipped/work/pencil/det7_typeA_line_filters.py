#!/usr/bin/env python3
"""Necessary single-line increment ranks and overlap filter for det7 type A."""
from pathlib import Path
from itertools import combinations
import json
from sympy import Matrix
from det7_prolongation import data,TYPE_A,quad_weight
from det7_typeB_line_conditions import conditions,rank


def main():
    variables,T,blocks,image=data(TYPE_A,-1)
    saturation=json.loads(Path(__file__).with_name('det7_typeA_prolongation.json').read_text())
    used=sorted({i for pair in saturation['unexcluded'] for i in pair['chosen']})
    info={}
    for index in used:
        w,block,dim=blocks[index]
        A=conditions(T,variables,w,block,'A',S=TYPE_A,image_character=w in image)
        maxzero=0;maxspaces=[]
        for count in range(7,-1,-1):
            surviving=[]
            for zeros in combinations(range(7),count):
                eq=[row for j in zeros for row in A[j]['equations']]
                if rank(eq,dim)<dim:surviving.append(zeros)
            if surviving:
                maxzero=count;maxspaces=surviving;break
        info[index]={'conditions':A,'min_increment':7-maxzero,
                     'maximum_zero_sets':maxspaces,'dimension':dim,
                     'weight':w,'coordinates':block}
        print('block',index,'dim',dim,'minAincrement',7-maxzero,flush=True)
    Aweights=[tuple(-x for x in quad_weight(q)) for q in TYPE_A]
    remaining=[];excluded=[]
    for case in saturation['unexcluded']:
        i,j=case['chosen']
        wi,wj=blocks[i][0],blocks[j][0]
        cols_i=[tuple(x+y for x,y in zip(wi,a)) for a in Aweights]
        cols_j=[tuple(x+y for x,y in zip(wj,a)) for a in Aweights]
        overlap=len(set(cols_i)&set(cols_j))
        lower=info[i]['min_increment']+info[j]['min_increment']-overlap
        out={'pair':[i,j],'overlapping_A_weights':overlap,'lower_A_increment':lower}
        (excluded if lower>6 else remaining).append(out)
    path=Path(__file__).with_name('det7_typeA_line_filters.json')
    path.write_text(json.dumps({'block_info':info,'excluded':excluded,'remaining':remaining},indent=2)+'\n')
    print('excluded',len(excluded),'remaining',len(remaining),flush=True)
    print(json.dumps(remaining,indent=2))


if __name__=='__main__':main()
