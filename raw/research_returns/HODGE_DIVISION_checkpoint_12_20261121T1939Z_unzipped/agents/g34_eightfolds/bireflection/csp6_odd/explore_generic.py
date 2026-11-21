#!/usr/bin/env python3
"""Explore exact bounds from complete frozen CSp6.1 mathematical data.

Original Julia code is not executed. No Sp restriction or theorem is
asserted by this exploratory coefficient calculation.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_g2_triality import parse,plain,shifted,block,comma_parts

B=Path(__file__).resolve().parent

def scalar_poly(s):
    s=s.strip()
    if s.startswith('R('):assert s.endswith(')');s=s[2:-1]
    return parse(s)

def entry_parts(s):
    s=s.strip()
    if s=='S()':return []
    assert s.startswith('S(Dict(') and s.endswith('), simplify=false)'),s
    text=s[len('S(Dict('):-len('), simplify=false)')]
    parts=[]
    for term in comma_parts(text):
        assert term.count('=>')==1,term
        phase,coeff=term.split('=>')
        assert re.fullmatch(r'[a-zA-Z0-9\s()/*+^\-]+',phase)
        parts.append((phase.strip(),scalar_poly(coeff)))
    return parts

def main():
    start=time.perf_counter();raw=(B/'cache/CSp6.1.jl').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='f5e68e9429054370df7376f174a095bc548cf1ecf7ce44f5446f1eaebba250dc'
    text=raw.decode();body=block(text,text.index('table ='))
    rows=[comma_parts(x) for x in re.findall(r'\[([^\[\]]*)\]',body)]
    degrees=comma_parts(block(text,text.index('chardegree =')))
    lengths=comma_parts(block(text,text.index('classlength =')))
    cls=[list(map(int,t)) for t in re.findall(r'\[\[(\d+), (\d+)\]',block(text,text.index('classinfo =')))]
    assert len(rows)==len(degrees)==100 and len(cls)==len(lengths)==90
    assert all(len(r)==90 for r in rows)
    cells=[[entry_parts(s) for s in r] for r in rows]
    ds=[scalar_poly(x) for x in degrees];ls=[scalar_poly(x) for x in lengths]
    assert plain(ds[0])=={0:F(1)} and plain(ls[0])=={0:F(1)}
    for row,d in zip(cells,ds):
        p={}
        for phase,c in row[0]:
            assert 'i1' in phase and not any(v in phase for v in ('i2','i3','i4'))
            for (k,atom),v in c.items():
                assert not atom;p[k,()]=p.get((k,()),F(0))+v
        assert {k:v for k,v in p.items() if v}==d
    semisimple=[j for j,c in enumerate(cls) if c[1]==0 and j!=0]
    out={'scope':'Exploratory exact CSp6 bounds only; no restriction or geometric theorem claimed.',
         'rows':100,'columns':90,'noncentral_semisimple_columns':[j+1 for j in semisimple],'probes':[]}
    for q0 in [3,5,7,9,11,17]:
        deg=[plain(shifted(d,q0)) for d in ds]
        assert all(all(v>=0 for v in d.values()) for d in deg)
        failures=[];all_fail=[]
        for i,row in enumerate(cells[1:],1):
            for j,parts in enumerate(row[1:],1):
                tri={}
                for phase,p in parts:
                    for k,v in plain(shifted(p,q0)).items():tri[k]=tri.get(k,F(0))+abs(v)
                bad=any(tri.get(k,F(0))>deg[i].get(k,F(0))/4 for k in set(tri)|set(deg[i]))
                if bad:
                    rr={'row':i+1,'column':j+1,'class':cls[j],
                        'ratio_at_threshold':str(tri.get(0,F(0))/deg[i][0])}
                    all_fail.append(rr)
                    if j in semisimple:failures.append(rr)
        out['probes'].append({'q0':q0,'semisimple_quarter_failures':failures,
                              'all_noncentral_quarter_failures':all_fail,
                              'minimum_CSp_degree':str(min(d[0] for d in deg[1:]))})
    inp={'source_sha256':hashlib.sha256(raw).hexdigest(),'entries':rows,
         'degrees':degrees,'class_lengths':lengths,'class_type_pairs':cls}
    (B/'generic_inputs.json').write_text(json.dumps(inp,separators=(',',':'))+'\n')
    out['seconds']=round(time.perf_counter()-start,6)
    (B/'generic_exploration.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({**out,'probes':[{**p,'all_noncentral_quarter_failures':len(p['all_noncentral_quarter_failures'])} for p in out['probes']]},indent=2))

if __name__=='__main__':main()
