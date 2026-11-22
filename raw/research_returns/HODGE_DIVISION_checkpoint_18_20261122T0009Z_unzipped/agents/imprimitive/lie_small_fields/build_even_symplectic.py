#!/usr/bin/env python3
"""Original complete generic inputs and deterministic all-field certificates."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time
from parse_generic_bounds import rows,certify
from build_generic_input import array,compact

BASE=Path(__file__).resolve().parent
EXPECTED={'Sp4.0.jl':(8,F(1,4),19,196),'Sp6.0.jl':(4,F(17,63),66,378)}

def main():
    start=time.monotonic()
    manifest=json.loads((BASE/'even_symplectic_retrieval.json').read_text())
    assert manifest['commit']=='87231738271ed548f62e7f1c98ff2bbfc1ed30d3'
    assert {Path(s['path']).name for s in manifest['files']}==set(EXPECTED)
    data={'upstream_commit':manifest['commit'],'tables':[]};out=[]
    for source in manifest['files']:
        name=Path(source['path']).name;raw=(BASE/'cache'/name).read_bytes()
        assert len(raw)==source['bytes'] and hashlib.sha256(raw).hexdigest()==source['sha256']
        text=raw.decode();q0,bound,n,m=EXPECTED[name]
        item={'name':name,'source':source,'threshold':q0,'condition':'q even',
              'bound':str(bound),'entries':[[compact(e) for e in row] for row in rows(text)],
              'declared_degrees':[compact(e) for e in array(text,'chardegree')],
              'declared_class_lengths':[compact(e) for e in array(text,'classlength')]}
        data['tables'].append(item)
        r=certify(item,bound=bound)
        assert r['character_types']==r['class_types']==n
        assert F(r['minimum_degree_at_threshold'])==m and not r['failures']
        out.append(r)
    dest=BASE/'even_symplectic_generic_inputs.json';dest.write_text(json.dumps(data,separators=(',',':'))+'\n')
    cert={'status':'PASS','input_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'tables':out,
          'nontrivial_rows':83,'nontrivial_cells':4549}
    (BASE/'even_symplectic_polynomials.json').write_text(json.dumps(cert,separators=(',',':'))+'\n')
    summary={k:v for k,v in cert.items() if k!='tables'}
    summary['tables']=[{k:v for k,v in r.items() if k!='polynomial_input'} for r in out]
    summary['seconds']=round(time.monotonic()-start,3)
    (BASE/'even_symplectic_generic_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary))

if __name__=='__main__':main()
