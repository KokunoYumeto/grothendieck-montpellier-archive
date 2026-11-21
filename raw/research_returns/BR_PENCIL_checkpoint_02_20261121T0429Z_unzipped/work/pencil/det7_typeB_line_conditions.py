#!/usr/bin/env python3
"""Exact finite linear-arrangement test for the three remaining det7 weight lines."""
from pathlib import Path
from itertools import combinations
import json,math
from functools import reduce
import numpy as np
from sympy import Matrix,ilcm,igcd
from det7_prolongation import data,TYPE_B,quad_weight,var_weight,prolong


def primitive(v):
    denominator=1
    for x in v:denominator=ilcm(denominator,x.q)
    integers=[int(x*denominator) for x in v]
    divisor=reduce(math.gcd,integers,0)
    if not divisor:return []
    integers=[x//divisor for x in integers]
    first=next(x for x in integers if x)
    if first<0:integers=[-x for x in integers]
    return integers


def canonical_rows(rows,d):
    if not rows:return []
    m=Matrix(rows)
    reduced,piv=m.rref()
    result=[]
    for i in range(len(piv)):
        row=primitive(list(reduced.row(i)))
        if row:result.append(row)
    return result


def rank(rows,d):
    if not rows:return 0
    # Very small exact matrix; each parameter dimension is at most five.
    return len(Matrix(rows).rref()[1])


def conditions(T,variables,w,block,orientation,S=TYPE_B,image_character=True):
    # Quotient coordinate basis: omit the final coordinate, since U's
    # nonzero weight vector has nonzero coefficient there.
    params=block[:-1] if image_character else block
    basis=[T[:,:,c] for c in range(T.shape[2])]
    xs=[]
    for q,v in params:
        x=np.zeros(T.shape[:2],dtype=np.int64);x[q,v]=1;xs.append(x)
    M0=prolong(basis,orientation)
    MX=prolong(xs,orientation)
    Aweights=[tuple(-x for x in quad_weight(q)) for q in S]
    Bweights=[var_weight(v) for v in variables]
    otherweights,factorweights=(Aweights,Bweights) if orientation=='B' else (Bweights,Aweights)
    wedge=list(combinations(range(len(factorweights)),2))
    rowsweights=[tuple(x+y+z for x,y,z in zip(ow,factorweights[i],factorweights[j]))
                 for ow in otherweights for i,j in wedge]
    sourceweights=[tuple(x-y for x,y in zip(fw,Bweights[c]))
                   for c in range(len(Bweights)) for fw in factorweights]
    output=[]
    for j,wfactor in enumerate(factorweights):
        target=tuple(x+y for x,y in zip(w,wfactor))
        rows=[i for i,weight in enumerate(rowsweights) if weight==target]
        cols=[i for i,weight in enumerate(sourceweights) if weight==target]
        base=Matrix(M0[np.ix_(rows,cols)].tolist()) if cols else Matrix.zeros(len(rows),0)
        images=Matrix(MX[np.ix_(rows,[s*len(factorweights)+j for s in range(len(xs))])].tolist())
        null=base.T.nullspace()
        equations=[]
        for n in null:
            eq=primitive(list((n.T*images).row(0)))
            if eq:equations.append(eq)
        equations=canonical_rows(equations,len(xs))
        output.append({'factor_index':j,'equations':equations,
                       'base_shape':[base.rows,base.cols],'base_rank':base.rank(),
                       'target_weight':target})
    return output


def main():
    variables,T,blocks,image=data(TYPE_B,-1)
    results=[]
    for index in [3,4,14]:
        w,block,dim=blocks[index]
        assert w in image and dim==len(block)-1
        A=conditions(T,variables,w,block,'A')
        B=conditions(T,variables,w,block,'B')
        survivors=[];basecount=0
        for zeros in combinations(range(12),6):
            equations=[row for j in zeros for row in B[j]['equations']]
            if rank(equations,dim)==dim:
                basecount+=1
                continue
            for a in range(7):
                eq=equations+A[a]['equations']
                if rank(eq,dim)<dim:
                    null=Matrix(eq).nullspace() if eq else [Matrix.eye(dim)[:,i] for i in range(dim)]
                    survivors.append({'B_zero_columns':zeros,'A_zero_column':a,
                                      'kernel_basis':[primitive(list(v)) for v in null]})
        item={'block_index':index,'weight':w,'coordinates':block,'quotient_dimension':dim,
              'A_conditions':A,'B_conditions':B,'B_only_excluded':basecount,
              'unexcluded':survivors}
        results.append(item)
        print('block',index,'dim',dim,'B_only_excluded',basecount,'survivors',len(survivors),flush=True)
        for s in survivors[:10]:print(s,flush=True)
    path=Path(__file__).with_name('det7_typeB_line_conditions.json')
    path.write_text(json.dumps(results,indent=2)+'\n')


if __name__=='__main__':main()
