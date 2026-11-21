#!/usr/bin/env python3
"""Refine final Borel-flag parameter lines by exact joint wedge arrangements."""
from pathlib import Path
from itertools import combinations
import argparse,json,time
import numpy as np
from sympy import Matrix,Rational
from determinant_borel_module import make
from determinant_borel_extensions import ambient_basis,canonical,serialize
from det7_prolongation import prolong,quad_weight,var_weight
from audit_support9_sevenplanes import arrangements,integer_rows
from bigraded_prolongation import primitive

def decode(M,sp):
    F=[() for _ in M['blocks']]
    for b in sp:F[b['block']]=tuple(tuple(Rational(x) for x in row) for row in b['basis'])
    return tuple(F)

def maps(M,F,branch):
    E=ambient_basis(M,F);a,m=M['T'].shape[:2];block=branch['block'];w,cs,d=M['blocks'][block]
    bs=[primitive([Rational(x) for x in v]) for v in branch['basis']]
    X=[(M['X'][:,M['starts'][block]:M['starts'][block]+d]@np.array(v,dtype=np.int64)).reshape(a,m) for v in bs]
    aw=[tuple(-x for x in quad_weight(q)) for q in M['S']];bw=[var_weight(v) for v in M['variables']]
    ew=[tuple(-x for x in v) for v in bw]
    ew.extend(M['blocks'][i][0] for i,rows in enumerate(F) for row in rows)
    conditions=[];baseline={}
    for o in ['A','B']:
        fw,ow=(aw,bw) if o=='A' else (bw,aw);pairs=list(combinations(range(len(fw)),2))
        rowweights=[tuple(x+y+z for x,y,z in zip(v,fw[i],fw[j])) for v in ow for i,j in pairs]
        colweights=[tuple(x+y for x,y in zip(v,u)) for v in ew for u in fw]
        M0=prolong(E,o);MX=prolong(X,o);baseline[o]=0
        for weight in set(colweights):
            rows=[i for i,v in enumerate(rowweights) if v==weight];cols=[i for i,v in enumerate(colweights) if v==weight]
            B=Matrix(M0[np.ix_(rows,cols)].tolist()) if rows else Matrix.zeros(0,len(cols))
            baseline[o]+=len(B.rref()[1])
        for j,v in enumerate(fw):
            weight=tuple(x+y for x,y in zip(w,v));rows=[i for i,z in enumerate(rowweights) if z==weight];cols=[i for i,z in enumerate(colweights) if z==weight]
            B=Matrix(M0[np.ix_(rows,cols)].tolist()) if cols else Matrix.zeros(len(rows),0)
            H=Matrix([primitive(v) for v in B.T.nullspace()]) if B.rows-len(B.rref()[1]) else Matrix.zeros(0,len(rows))
            assert H*B==Matrix.zeros(H.rows,B.cols)
            Z=Matrix(MX[np.ix_(rows,[s*len(fw)+j for s in range(len(X))])].tolist()) if rows else Matrix.zeros(0,len(X))
            conditions.append(integer_rows(H*Z))
    return conditions,baseline,bs

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--support',type=int,required=True);args=pa.parse_args();here=Path(__file__).resolve().parent
    source=json.loads((here/f'det10_borel_support{args.support}.json').read_text());out=[];start=time.time()
    for rec in source:
        M=make(rec['subset']);a,m=M['T'].shape[:2];results=[]
        for number,item in enumerate(rec['continuous_branches']):
            if item['level']!=rec['quotient_dimension']:continue
            F=decode(M,item['parent']);branch=item['branch'];conditions,base,bs=maps(M,F,branch);d=len(bs)
            states=arrangements(conditions,d);remaining=[]
            for st in states:
                incA=a-sum(j<a for j in st['zero_columns']);incB=m-sum(j>=a for j in st['zero_columns'])
                if base['A']+incA>(a-1)*17 or base['B']+incB>(m-1)*17:continue
                r={'dimension':st['dimension'],'basis':st['basis'],'zero_columns':sorted(st['zero_columns']),'increments':[incA,incB]}
                if st['dimension']==1:
                    v=list(Matrix.hstack(*(Matrix(x) for x in bs))*Matrix(st['basis'][0]));i=branch['block'];G=list(F);G[i]=canonical(F[i]+(tuple(v),),M['blocks'][i][2]);r['fixed_space']=serialize(G)
                remaining.append(r)
            results.append({'branch_index':number,'parent':item['parent'],'branch':branch,'baseline':base,'state_count':len(states),'survivors':remaining})
            print(rec['subset'],'branch',number,'states',len(states),'survivors',[(x['dimension'],x['increments']) for x in remaining],'time',round(time.time()-start,2),flush=True)
        out.append({'subset':rec['subset'],'early_branch_count':sum(x['level']!=rec['quotient_dimension'] for x in rec['continuous_branches']),'refinements':results})
        (here/f'det10_final_lines_support{args.support}.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
    print('DONE',time.time()-start,flush=True)

if __name__=='__main__':main()
