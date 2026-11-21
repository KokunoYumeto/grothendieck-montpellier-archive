#!/usr/bin/env python3
"""Certificates for two further m=12 determinant seven-plane types."""
from pathlib import Path
import json,numpy as np
from det7_prolongation import data,prolong,extension,rank,PRIME
from build_det7_certificate import line_certificate,determinant_mod

HERE=Path(__file__).resolve().parent


def main():
    output={'prime':PRIME,'field_scope':'characteristic zero',
            'target_border_rank_lower_bound':14,'cases':[]}
    for name in ['C','D']:
        saturation=json.loads((HERE/f'det7_type{name}_prolongation.json').read_text())
        S=saturation['subset'];variables,T,blocks,image=data(S,-1)
        U=[T[:,:,c] for c in range(len(variables))]
        M0=prolong(U,'A');r,rows,cols=rank(M0)
        assert r>=74;rows,cols=rows[:74],cols[:74]
        base={'orientation':'A','minor_order':74,'rows':rows,'cols':cols,
              'determinant_mod_p':determinant_mod(M0[np.ix_(rows,cols)])}
        assert base['determinant_mod_p']!=0
        records=[]
        for rec in saturation['records']:
            if 'certificate' not in rec:continue
            c=rec['certificate'].copy()
            bs=extension(T,blocks,image,rec['chosen'])
            M=prolong(bs,c['orientation'])
            c['determinant_mod_p']=determinant_mod(M[np.ix_(c['rows'],c['cols'])])
            assert c['determinant_mod_p']!=0
            records.append({'chosen':rec['chosen'],'certificate':c})
        lines={}
        for rec in saturation['unexcluded']:
            i=rec['chosen'][0]
            lines[str(i)]=line_certificate(S,variables,T,blocks[i],image,'A',5)
        output['cases'].append({'name':name,'subset':S,'variables':variables,'r_excluded':13,
                               'quotient_dimension':1,
                               'blocks':[{'weight':w,'coordinates':c,'quotient_dimension':d} for w,c,d in blocks],
                               'base_rank_certificate':base,'saturation_certificates':records,
                               'line_certificates':lines,'pair_increment_checks':[]})
        print(name,'saturation',len(records),'lines',len(lines),flush=True)
    path=HERE/'det7_extra_m12_certificate.json'
    path.write_text(json.dumps(output,separators=(',',':'))+'\n')
    print('CERTIFICATE',path,'bytes',path.stat().st_size)


if __name__=='__main__':main()
