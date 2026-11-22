#!/usr/bin/env python3
"""Deterministic uniform A2/2A2 coefficient certificate, including centers."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
from flint import fmpq_poly
from probe_generic import check_identity

BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
sys.path.insert(0,str(ROOT/'agents/imprimitive/lie_small_fields'))
from parse_generic_bounds import parse_entry,shift,l1_shift,rows
from build_generic_input import array,compact

EXPECTED={'SL3.1.jl':(5,17,10,30),'SL3.n1.jl':(5,8,8,30),
          'SU3.2.jl':(7,17,10,42),'SU3.n2.jl':(7,8,8,42)}

def main():
    raw=(BASE/'generic_inputs.json').read_bytes();data=json.loads(raw)
    assert data['upstream_commit']=='87231738271ed548f62e7f1c98ff2bbfc1ed30d3'
    assert {t['name'] for t in data['tables']}==set(EXPECTED)
    result={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
            'bound':'1/4','nontrivial_rows':0,'noncentral_cells':0,'tables':[]}
    for t in data['tables']:
        name=t['name'];q0,nr,nc,minimum=EXPECTED[name];rs=t['entries']
        assert len(rs)==nr and all(len(r)==nc for r in rs)
        assert t['central_column']==1 and all(e=='S(1)' for e in rs[0])
        ds=[parse_entry(e) for e in t['declared_degrees']]
        ls=[parse_entry(e) for e in t['declared_class_lengths']]
        assert len(ds)==nr and len(ls)==nc
        assert all(set(v.d)=={()} for v in ds+ls)
        assert ds[0].d[()]==ls[0].d[()]==fmpq_poly([1])
        for r,d in zip(rs,ds):check_identity(r[0],d.d[()])
        for l in ls[1:]:
            lc=shift(l.d[()],q0);assert lc[0]>1 and all(c>=0 for c in lc)
        rr={'name':name,'source_sha256':t['source']['sha256'],'threshold':q0,
            'condition':t['condition'],'character_types':nr,'class_types':nc,
            'central_column_excluded':1,'minimum_degree':minimum,'rows':[]}
        mins=[]
        for i,(r,d) in enumerate(zip(rs[1:],ds[1:]),2):
            p=d.d[()];dc=shift(p,q0);mins.append(dc[0])
            assert dc[0]>0 and all(c>=0 for c in dc)
            item={'row':i,'degree_coefficients':[str(c) for c in p.coeffs()],
                  'degree_shifted':[str(c) for c in dc],'entries':[]}
            for j,e in enumerate(r[1:],2):
                v=parse_entry(e);bc=l1_shift(v,q0)
                diff=[(dc[k] if k<len(dc) else F(0))/4-(bc[k] if k<len(bc) else F(0)) for k in range(max(len(dc),len(bc)))]
                assert all(c>=0 for c in diff),(name,i,j)
                item['entries'].append({'column':j,'phase_coefficients':[[str(c) for c in p.coeffs()] for p in v.d.values()],
                                        'shifted_absolute_sum':[str(c) for c in bc],
                                        'quarter_degree_minus_bound':[str(c) for c in diff]})
            rr['rows'].append(item)
        assert min(mins)==minimum
        result['nontrivial_rows']+=nr-1;result['noncentral_cells']+=(nr-1)*(nc-1)
        result['tables'].append(rr)
    assert result['nontrivial_rows']==46 and result['noncentral_cells']==386
    dest=BASE/'generic_certificate.json';dest.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='tables'},indent=2))
    print('certificate_sha256',hashlib.sha256(dest.read_bytes()).hexdigest())

if __name__=='__main__':main()
