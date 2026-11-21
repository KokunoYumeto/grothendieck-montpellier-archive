#!/usr/bin/env python3
"""Build P-16's three permanent seven-plane certificates.

Discovery input is supplied by the root agent.  The final verifier rebuilds
every tensor and matrix from the subset/sign and imports none of this code.
"""
from pathlib import Path
import json,numpy as np
from det7_prolongation import data,prolong,extension,rank,PRIME
from build_det7_certificate import line_certificate,determinant_mod
from build_det7_extra_m11 import base_certificate

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'root'
EXCLUDED=[0,1,2,6,7,18,19]

def main():
    sources=json.loads((ROOT/'per7_small_prolongation.json').read_text())['records']
    filters=json.loads((ROOT/'per7_m11_line_filters.json').read_text())
    conditional=json.loads((ROOT/'per7_m11_conditional.json').read_text())
    output={'prime':PRIME,'field_scope':'characteristic zero',
            'target_border_rank_lower_bound':14,'cases':[]}
    for f in filters:
        S=f['subset']
        if S==EXCLUDED:continue
        saturation=next(r for r in sources if r['subset']==S)
        conditioned=next(r for r in conditional if r['subset']==S)
        assert not conditioned['unresolved']
        variables,T,blocks,image=data(S,1)
        assert len(variables)==11
        U=[T[:,:,c].copy() for c in range(11)]
        base=base_certificate(U,'A',f['baseline']['A'])
        records=[]
        for rec in saturation['saturation_certificates']:
            c=rec['certificate'];bs=extension(T,blocks,image,rec['choice'])
            M=prolong(bs,c['factor']);assert c['size']==M.shape[1]-12
            value=determinant_mod(M[np.ix_(c['rows'],c['cols'])]);assert value
            records.append({'chosen':rec['choice'],'certificate':{
                'orientation':c['factor'],'minor_order':c['size'],
                'rows':c['rows'],'cols':c['cols'],'determinant_mod_p':value}})
        used=sorted({i for rec in f['excluded'] for i in rec['pair']})
        lines={str(i):line_certificate(S,variables,T,blocks[i],image,'A',
                        f['block_info'][str(i)]['factors']['A']['minimum_increment'])
               for i in used}
        pairs=[]
        for rec in f['excluded']:
            p=next(p for p in rec['proofs'] if p['factor']=='A')
            pairs.append({'pair':rec['pair'],'overlapping_A_weights':p['overlap'],
                          'lower_A_increment':p['increment']})
        condition_checks=conditioned['conditioned_pair_checks']
        assert sorted(f['remaining'])==sorted(x['pair'] for x in condition_checks)
        output['cases'].append({'name':'per_m11_'+str(len(output['cases'])+1),'sign':1,
            'subset':S,'variables':variables,'r_excluded':13,'quotient_dimension':2,
            'blocks':[{'weight':w,'coordinates':c,'quotient_dimension':d} for w,c,d in blocks],
            'base_rank_certificate':base,'saturation_certificates':records,
            'line_certificates':lines,'pair_increment_checks':pairs,
            'conditioned_pair_checks':condition_checks})
        print(S,'baseline',f['baseline']['A'],'weights',len(blocks),'saturation',len(records),
              'lines',len(lines),'pairs',len(pairs),'conditional',len(condition_checks),flush=True)
    assert len(output['cases'])==3
    path=HERE/'per7_m11_certificate.json'
    path.write_text(json.dumps(output,separators=(',',':'))+'\n')
    print(path,path.stat().st_size,flush=True)

if __name__=='__main__':main()
