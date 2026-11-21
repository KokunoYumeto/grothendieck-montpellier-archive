#!/usr/bin/env python3
"""Certificates for the final two support-11 determinant seven-plane types."""
from pathlib import Path
import json,numpy as np
from det7_prolongation import data,prolong,extension,rank,PRIME
from build_det7_certificate import line_certificate,determinant_mod

HERE=Path(__file__).resolve().parent


def base_certificate(basis,orientation,order):
    M=prolong(basis,orientation);r,rows,cols=rank(M)
    assert r>=order;rows,cols=rows[:order],cols[:order]
    value=determinant_mod(M[np.ix_(rows,cols)])
    assert value!=0
    return {'orientation':orientation,'minor_order':order,'rows':rows,'cols':cols,
            'determinant_mod_p':value}


def main():
    output={'prime':PRIME,'field_scope':'characteristic zero',
            'target_border_rank_lower_bound':14,'cases':[]}
    for name,baseline in [('E',75),('F',71)]:
        saturation=json.loads((HERE/f'det7_type{name}_prolongation.json').read_text())
        filters=json.loads((HERE/f'det7_type{name}_A_filters.json').read_text())
        S=saturation['subset'];variables,T,blocks,image=data(S,-1)
        U=[T[:,:,c] for c in range(len(variables))]
        base=base_certificate(U,'A',baseline)
        records=[]
        for rec in saturation['records']:
            if 'certificate' not in rec:continue
            c=rec['certificate'].copy()
            bs=extension(T,blocks,image,rec['chosen'])
            M=prolong(bs,c['orientation'])
            c['determinant_mod_p']=determinant_mod(M[np.ix_(c['rows'],c['cols'])])
            assert c['determinant_mod_p']!=0
            records.append({'chosen':rec['chosen'],'certificate':c})
        used=sorted({i for rec in filters['excluded'] for i in rec['pair']})
        lines={}
        for i in used:
            info=filters['block_info'][str(i)]
            lines[str(i)]=line_certificate(S,variables,T,blocks[i],image,'A',info['min_increment'])
        pair_checks=[{'pair':rec['pair'],'overlapping_A_weights':rec['overlapping_weights'],
                      'lower_A_increment':rec['lower_increment']} for rec in filters['excluded']]
        conditioned=[]
        if name=='E':
            assert not filters['remaining']
        else:
            assert [rec['pair'] for rec in filters['remaining']]==[[11,14]]
            fixed=11;variable=14
            w,coords,d=blocks[fixed]
            assert d==1
            params=coords[:-1] if w in image else coords
            coordinate=list(params[0])
            x=np.zeros(T.shape[:2],dtype=np.int64);x[tuple(coordinate)]=1
            fixed_base=U+[x]
            c=base_certificate(fixed_base,'B',125)
            line=line_certificate(S,variables,T,blocks[variable],image,'B',6,
                                  extra_base_coordinates=[coordinate])
            conditioned=[{'pair':[11,14],'fixed_index':11,'variable_index':14,
                          'fixed_coordinate':coordinate,'base_rank_certificate':c,
                          'line_certificate':line}]
        output['cases'].append({'name':name,'subset':S,'variables':variables,'r_excluded':13,
                               'quotient_dimension':2,
                               'blocks':[{'weight':w,'coordinates':c,'quotient_dimension':d} for w,c,d in blocks],
                               'base_rank_certificate':base,'saturation_certificates':records,
                               'line_certificates':lines,'pair_increment_checks':pair_checks,
                               'conditioned_pair_checks':conditioned})
        print(name,'saturation',len(records),'lines',len(lines),'pairs',len(pair_checks),
              'conditioned',len(conditioned),flush=True)
    path=HERE/'det7_extra_m11_certificate.json'
    path.write_text(json.dumps(output,separators=(',',':'))+'\n')
    print('CERTIFICATE',path,'bytes',path.stat().st_size)


if __name__=='__main__':main()
