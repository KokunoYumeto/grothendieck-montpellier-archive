#!/usr/bin/env python3
"""Absorb the fixed weight line in the final Type F pair, then test its P1."""
from pathlib import Path
from itertools import combinations
import json,numpy as np
from sympy import Matrix
from det7_prolongation import data,prolong,rank,quad_weight,var_weight
from det7_typeB_line_conditions import primitive,canonical_rows

HERE=Path(__file__).resolve().parent


def main():
    D=json.loads((HERE/'det7_typeF_prolongation.json').read_text())
    S=D['subset'];V,T,blocks,image=data(S,-1)
    U=[T[:,:,c] for c in range(len(V))]
    wx,cx,dx=blocks[11];wy,cy,dy=blocks[14]
    assert dx==1 and dy==2
    px=cx[:-1] if wx in image else cx
    py=cy[:-1] if wy in image else cy
    X=np.zeros(T.shape[:2],dtype=np.int64);X[tuple(px[0])]=1
    base=U+[X]
    Y=[]
    for q,v in py:
        m=np.zeros(T.shape[:2],dtype=np.int64);m[q,v]=1;Y.append(m)
    aw=[tuple(-x for x in quad_weight(q)) for q in S]
    bw=[var_weight(v) for v in V]
    baseweights=[tuple(-x for x in w) for w in bw]+[wx]
    cases={};conditions_all={}
    for orientation in ['A','B']:
        fw,ow=(aw,bw) if orientation=='A' else (bw,aw)
        M0=prolong(base,orientation);MY=prolong(Y,orientation)
        r0=rank(M0)[0];allowed=(len(fw)-1)*13-r0;zero=len(fw)-allowed
        wedge=list(combinations(range(len(fw)),2))
        rowweights=[tuple(x+y+z for x,y,z in zip(w,fw[i],fw[j])) for w in ow for i,j in wedge]
        colweights=[tuple(x+y for x,y in zip(w,f)) for w in baseweights for f in fw]
        conditions=[]
        for j,f in enumerate(fw):
            target=tuple(x+y for x,y in zip(wy,f))
            rows=[i for i,w in enumerate(rowweights) if w==target]
            cols=[i for i,w in enumerate(colweights) if w==target]
            block=Matrix(M0[np.ix_(rows,cols)].tolist()) if cols else Matrix.zeros(len(rows),0)
            images=Matrix(MY[np.ix_(rows,[s*len(fw)+j for s in range(2)])].tolist())
            equations=[]
            for n in block.T.nullspace():
                v=primitive(list((n.T*images).row(0)))
                if v:equations.append(v)
            conditions.append(canonical_rows(equations,2))
        survivors=[]
        for zeros in combinations(range(len(fw)),zero):
            equations=[row for j in zeros for row in conditions[j]]
            matrix=Matrix(equations) if equations else Matrix.zeros(0,2)
            null=matrix.nullspace()
            if null:survivors.append({'zero_columns':zeros,'equations':equations,
                                     'kernel':[primitive(list(v)) for v in null]})
        cases[orientation]={'base_rank':r0,'allowed_increment':allowed,'needed_zeros':zero,
                            'survivors':survivors}
        conditions_all[orientation]=conditions
        print(orientation,'base',r0,'allowed',allowed,'zeros',zero,'survivors',len(survivors),flush=True)
        print(json.dumps(survivors[:8]),flush=True)
    joint=[]
    for a in cases['A']['survivors']:
        for b in cases['B']['survivors']:
            eq=a['equations']+b['equations']
            matrix=Matrix(eq) if eq else Matrix.zeros(0,2)
            null=matrix.nullspace()
            if null:joint.append({'A':a['zero_columns'],'B':b['zero_columns'],
                                  'kernel':[primitive(list(v)) for v in null]})
    out={'subset':S,'fixed_weight':wx,'fixed_coordinate':px[0],
         'variable_weight':wy,'variable_coordinates':py,'cases':cases,
         'conditions':conditions_all,'joint_survivors':joint}
    (HERE/'det7_typeF_last_pair.json').write_text(json.dumps(out,indent=2)+'\n')
    print('joint',len(joint),json.dumps(joint[:8]),flush=True)


if __name__=='__main__':main()
