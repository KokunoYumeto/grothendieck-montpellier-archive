#!/usr/bin/env python3
"""Complete small-cover normalizer spectra and optional triality trace checks."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,importlib.util,json,time
BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cyc',BASE.parent/'sporadic/verify_quarter_bound.py')
cyc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cyc)
raw=(BASE/'g2_triality_small_inputs.json').read_bytes();ts={t['name']:t for t in json.loads(raw)['tables']}
assert set(ts)=={'3.G2(3)','3.G2(3).2','2.G2(4)','2.G2(4).2','3D4(2)','3D4(2).3'}
meta={r['name']:r['extension_info'] for r in json.loads(raw)['metadata']}
assert meta=={'G2(3)':['3','2'],'G2(4)':['2','2'],'3D4(2)':['','3']}
cs={n:[[cyc.key(v) for v in c] for c in t['characters']] for n,t in ts.items()}
start=time.monotonic();out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),'tables':[],'rows':0,'entries':0,'quarter_failures':[]}
for name,t in ts.items():
    assert 'origin: ATLAS of finite groups' in t['information']
    nr=len(cs[name]);assert nr==len(t['orders'])==len(t['sizes'])
    assert sum(c[0]**2 for c in cs[name])==sum(t['sizes'])==t['order']
    if 'core' in t:
        u=ts[t['core']];fusion=t['fusion'];r=3 if name=='3D4(2).3' else 2
        assert t['order']==r*u['order'] and len(fusion)==len(u['orders'])
        assert [i for i,j in enumerate(fusion) if j==1]==[0]
        assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],fusion))
        assert all(sum(s for s,jj in zip(u['sizes'],fusion) if jj==j)==t['sizes'][j-1] for j in set(fusion))
        pm={p['prime']:p['map'] for p in t['power_maps']}
        for p in u['power_maps']:
            assert all(fusion[k-1]==pm[p['prime']][j-1] for j,k in zip(fusion,p['map']))
    rr={'name':name,'selected_rows':[],'minimum_degree':None,'minimum_ratio':'1','maximum_trace_l1_ratio':'0','entries':0,'row_bounds':[]}
    ratios=[];traces=[]
    for i,c in enumerate(cs[name]):
        a=c[0]
        if a==1:continue
        if 'core' in t:
            r=tuple(c[j-1] for j in t['fusion'])
            if r not in {tuple(u) for u in cs[t['core']]}:continue
        rr['selected_rows'].append(i+1);out['rows']+=1
        rr['minimum_degree']=a if rr['minimum_degree'] is None else min(rr['minimum_degree'],a)
        values=[]
        for j,z in enumerate(c):
            if cyc.squared_norm(z)==(a*a,):continue
            out['entries']+=1;rr['entries']+=1
            ms=cyc.cyclic_multiplicities(t,c,j);nu=a-max(ms);values.append(F(nu,a))
            if 4*nu<a:out['quarter_failures'].append({'table':name,'row':i+1,'class':j+1,'degree':a,'nu':nu,'multiplicities':ms})
        if values:rr['row_bounds'].append({'row':i+1,'degree':a,'minimum_ratio':str(min(values))});ratios.extend(values)
    if ratios:rr['minimum_ratio']=str(min(ratios))
    if traces:rr['maximum_trace_l1_ratio']=str(max(traces))
    out['tables'].append(rr)
    print(name,'rows',len(rr['selected_rows']),'min_degree',rr['minimum_degree'],'nu/a',rr['minimum_ratio'],'L1/a',rr['maximum_trace_l1_ratio'],flush=True)
out['seconds']=round(time.monotonic()-start,3)
if out['quarter_failures']:out['status']='EXCEPTIONS'
assert out['rows']==239 and out['entries']==11502 and not out['quarter_failures']
assert [r['minimum_degree'] for r in out['tables']]==[14,14,12,12,26,26]
assert [r['minimum_ratio'] for r in out['tables']]==['3/7','3/7','1/3','1/3','4/13','4/13']
(BASE/'check_g2_triality_small.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='tables'}))
