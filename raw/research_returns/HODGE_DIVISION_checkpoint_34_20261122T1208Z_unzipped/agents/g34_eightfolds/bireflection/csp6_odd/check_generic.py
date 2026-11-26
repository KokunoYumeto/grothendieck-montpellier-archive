#!/usr/bin/env python3
"""All-parameter coefficient certificate for the complete CSp6.1 table.

The immutable mathematical data are parsed, never executed. The normalizer
and geometric applications are proved separately in the authored section.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re,time
from explore_generic import entry_parts,scalar_poly,plain,shifted,block,comma_parts

B=Path(__file__).resolve().parent

def main():
    start=time.perf_counter();raw=(B/'generic_inputs.json').read_bytes();D=json.loads(raw)
    assert D['source_sha256']=='f5e68e9429054370df7376f174a095bc548cf1ecf7ce44f5446f1eaebba250dc'
    original=(B/'cache/CSp6.1.jl').read_bytes()
    assert hashlib.sha256(original).hexdigest()==D['source_sha256']
    text=original.decode()
    # Re-extract all mathematical input from the frozen original. The JSON
    # source tag alone is not treated as proof of input/source agreement.
    rows=[comma_parts(x) for x in re.findall(r'\[([^\[\]]*)\]',block(text,text.index('table =')))]
    degrees=comma_parts(block(text,text.index('chardegree =')))
    lengths=comma_parts(block(text,text.index('classlength =')))
    classes=[list(map(int,t)) for t in re.findall(r'\[\[(\d+), (\d+)\]',block(text,text.index('classinfo =')))]
    assert D['entries']==rows and D['degrees']==degrees
    assert D['class_lengths']==lengths and D['class_type_pairs']==classes
    assert len(D['entries'])==len(D['degrees'])==100
    assert len(D['class_lengths'])==len(D['class_type_pairs'])==90
    q0=5;degs=[plain(shifted(scalar_poly(x),q0)) for x in D['degrees']]
    floor=plain(shifted(scalar_poly('q^3-1'),q0));assert floor[0]==124
    assert degs[0]=={0:F(1)}
    for d in degs[1:]:
        assert all(d.get(k,F(0))>=floor.get(k,F(0)) for k in set(d)|set(floor))
    for j,x in enumerate(D['class_lengths']):
        d=plain(shifted(scalar_poly(x),q0))
        assert all(v>=0 for v in d.values())
        if j==0:assert d=={0:F(1)}
        else:assert d[0]>1
    cert={'q0':5,'bound':'1/4','row_types':99,'noncentral_class_types':89,
          'coefficient_inequalities':[],'degree_floor':'q^3-1',
          'input_sha256':hashlib.sha256(raw).hexdigest()}
    for i,row in enumerate(D['entries'][1:],1):
        assert len(row)==90
        for j,entry in enumerate(row[1:],1):
            tri={}
            for phase,p in entry_parts(entry):
                for k,v in plain(shifted(p,q0)).items():tri[k]=tri.get(k,F(0))+abs(v)
            ks=sorted(set(degs[i])|set(tri))
            diff=[degs[i].get(k,F(0))/4-tri.get(k,F(0)) for k in range(max(ks)+1)]
            assert all(v>=0 for v in diff),(i+1,j+1)
            cert['coefficient_inequalities'].append({'row':i+1,'column':j+1,'coefficients':[str(v) for v in diff]})
    assert len(cert['coefficient_inequalities'])==8811
    (B/'generic_certificate.json').write_text(json.dumps(cert,separators=(',',':'))+'\n')
    run={'status':'PASS','original_reextraction':'all entries, degrees, class lengths and class-type pairs identical',
         'rows':99,'inequalities':8811,'q0':5,'minimum_CSp_degree':'q^3-1',
         'seconds':round(time.perf_counter()-start,6)}
    (B/'generic_run.json').write_text(json.dumps(run,indent=2)+'\n');print(json.dumps(run))

if __name__=='__main__':main()
