#!/usr/bin/env python3
"""Build exact modular/linear certificates for the two det7 bottleneck types."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import json,math
import numpy as np
from sympy import Matrix
from det7_prolongation import data,TYPE_A,TYPE_B,quad_weight,var_weight,prolong,extension,rank,PRIME
from det7_typeB_line_conditions import primitive

HERE=Path(__file__).resolve().parent


def determinant_mod(matrix):
    a=matrix.copy()%PRIME
    n=a.shape[0];det=1
    for c in range(n):
        nz=np.flatnonzero(a[c:,c])
        if not len(nz):return 0
        rr=c+int(nz[0])
        if rr!=c:a[[c,rr]]=a[[rr,c]];det=-det
        pivot=int(a[c,c]);det=det*pivot%PRIME
        a[c,c:]=a[c,c:]*pow(pivot,-1,PRIME)%PRIME
        inds=np.flatnonzero(a[c+1:,c])+c+1
        if len(inds):a[inds,c:]=(a[inds,c:]-a[inds,c,None]*a[c,c:])%PRIME
    return det%PRIME


def line_certificate(S,variables,T,block,image,orientation,minimum,extra_base_coordinates=None):
    w,coordinates,dim=block
    params=coordinates[:-1] if w in image else coordinates
    assert len(params)==dim
    U=[T[:,:,c].copy() for c in range(len(variables))]
    extra_base_coordinates=extra_base_coordinates or []
    for q,v in extra_base_coordinates:
        x=np.zeros(T.shape[:2],dtype=np.int64);x[q,v]=1;U.append(x)
    X=[]
    for q,v in params:
        x=np.zeros(T.shape[:2],dtype=np.int64);x[q,v]=1;X.append(x)
    M0=prolong(U,orientation);MX=prolong(X,orientation)
    aw=[tuple(-x for x in quad_weight(q)) for q in S]
    bw=[var_weight(v) for v in variables]
    ow,fw=(aw,bw) if orientation=='B' else (bw,aw)
    wedge=list(combinations(range(len(fw)),2))
    rowweights=[tuple(x+y+z for x,y,z in zip(q,fw[i],fw[j])) for q in ow for i,j in wedge]
    baseweights=[tuple(-x for x in w0) for w0 in bw]
    baseweights.extend(tuple(x+y for x,y in zip(aw[q],bw[v])) for q,v in extra_base_coordinates)
    colweights=[tuple(x+y for x,y in zip(v,w0)) for w0 in baseweights for v in fw]
    conditions=[];H=[]
    for j,weight in enumerate(fw):
        target=tuple(x+y for x,y in zip(w,weight))
        rows=[i for i,x in enumerate(rowweights) if x==target]
        cols=[i for i,x in enumerate(colweights) if x==target]
        base=Matrix(M0[np.ix_(rows,cols)].tolist()) if cols else Matrix.zeros(len(rows),0)
        annihilator=[primitive(list(v)) for v in base.T.nullspace()]
        ann=np.array(annihilator,dtype=np.int64).reshape((len(annihilator),len(rows)))
        assert not np.any(ann@M0[rows,:])
        Xi=MX[np.ix_(rows,[s*len(fw)+j for s in range(dim)])]
        Hj=ann@Xi
        conditions.append({'factor_index':j,'output_rows':rows,'annihilator':ann.tolist()})
        H.append(Hj)
    forbidden_zeros=len(fw)-minimum+1
    for zeros in combinations(range(len(fw)),forbidden_zeros):
        stacked=np.concatenate([H[j] for j in zeros],axis=0)
        rr,_,_=rank(stacked)
        assert rr==dim,(S,w,orientation,zeros,rr,dim)
    return {'weight':w,'parameter_coordinates':params,'quotient_dimension':dim,
            'orientation':orientation,'minimum_increment':minimum,
            'forbidden_zero_subset_size':forbidden_zeros,'conditions':conditions,
            'extra_base_coordinates':extra_base_coordinates}


def main():
    output={'prime':PRIME,'field_scope':'characteristic zero (all nonzero modular minors certify nonzero integer minors)',
            'target_border_rank_lower_bound':14,'cases':[]}
    for name,S in [('A',TYPE_A),('B',TYPE_B)]:
        variables,T,blocks,image=data(S,-1)
        saturation=json.loads((HERE/f'det7_type{name}_prolongation.json').read_text())
        U=[T[:,:,c].copy() for c in range(len(variables))]
        base_orientation='A' if name=='A' else 'B'
        M0=prolong(U,base_orientation)
        rr,rows,cols=rank(M0)
        expected=72 if name=='A' else 137
        assert rr>=expected
        rows,cols=rows[:expected],cols[:expected]
        base={'orientation':base_orientation,'minor_order':expected,'rows':rows,'cols':cols,
              'determinant_mod_p':determinant_mod(M0[np.ix_(rows,cols)])}
        assert base['determinant_mod_p']!=0
        records=[]
        for i,rec in enumerate(saturation['records']):
            if 'certificate' not in rec:continue
            c=rec['certificate'].copy()
            bs=extension(T,blocks,image,rec['chosen'])
            M=prolong(bs,c['orientation'])
            assert c['minor_order']==M.shape[1]-12
            c['determinant_mod_p']=determinant_mod(M[np.ix_(c['rows'],c['cols'])])
            assert c['determinant_mod_p']!=0
            records.append({'chosen':rec['chosen'],'certificate':c})
        lines={}
        pair_checks=[]
        if name=='A':
            filters=json.loads((HERE/'det7_typeA_line_filters.json').read_text())
            for index,info in filters['block_info'].items():
                i=int(index)
                lines[index]=line_certificate(S,variables,T,blocks[i],image,'A',info['min_increment'])
            assert not filters['remaining']
            pair_checks=filters['excluded']
        else:
            for rec in saturation['unexcluded']:
                index=rec['chosen'][0]
                lines[str(index)]=line_certificate(S,variables,T,blocks[index],image,'B',7)
        case={'name':name,'subset':S,'variables':variables,'r_excluded':13,
              'quotient_dimension':13-len(variables),
              'blocks':[{'weight':w,'coordinates':c,'quotient_dimension':d} for w,c,d in blocks],
              'base_rank_certificate':base,'saturation_certificates':records,
              'line_certificates':lines,'pair_increment_checks':pair_checks}
        output['cases'].append(case)
        print(name,'base',expected,'saturation',len(records),'line_certificates',len(lines),
              'pair_checks',len(pair_checks),flush=True)
    path=HERE/'det7_two_type_certificate.json'
    path.write_text(json.dumps(output,separators=(',',':'))+'\n')
    print('CERTIFICATE',path,'bytes',path.stat().st_size)


if __name__=='__main__':main()
