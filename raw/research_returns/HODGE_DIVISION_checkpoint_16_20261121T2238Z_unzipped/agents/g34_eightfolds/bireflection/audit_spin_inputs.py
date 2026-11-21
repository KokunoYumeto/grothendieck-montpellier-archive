#!/usr/bin/env python3
"""Independent finite input check for the root HD-SPIN-01 proof."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import sympy as sp
from audit_sporadic_input import encode,abs_square,reduce_poly,ramanujan,cyclo

BASE=Path(__file__).resolve().parent
P=BASE.parent.parent/'imprimitive/sporadic/alternating_cover_inputs.json'
raw=P.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='d41d9bcb33344ce8d655dd83aa90f4a58ffc4f00a5cd22271c72895c22e7d26c'
data=json.loads(raw)
assert {t['name'] for t in data['tables']}=={'2.A6','2.A8','2.A9','2.A10','2.A11'}

def conjugate_difference(z):
    if isinstance(z,int):return (0,)
    n,c=z;v=[0]*n
    for j,a in enumerate(c):v[j]+=a;v[-j%n]-=a
    return reduce_poly(v,n)

def mean(z):
    if isinstance(z,int):return F(z)
    n,c=z
    return F(sum(a*ramanujan(n,j) for j,a in enumerate(c)),int(sp.totient(n)))

def relation_minus7(z):
    if isinstance(z,int):return True
    n,c=z;assert n==7
    b=reduce_poly([0,1,1,0,1,0,0],7)
    v=reduce_poly(c,7);dim=len(cyclo(7))-1
    b=list(b)+[0]*(dim-len(b));v=list(v)+[0]*(dim-len(v))
    j=next(j for j in range(1,dim) if b[j])
    scale=F(v[j],b[j]);shift=F(v[0])-scale*b[0]
    assert all(F(v[k])==scale*b[k]+(shift if k==0 else 0) for k in range(dim))
    return True

out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),'tables':[]}
for t in data['tables']:
    assert 'origin: ATLAS of finite groups' in t['information']
    chars=[[encode(z) for z in c] for c in t['characters']]
    assert sum(t['sizes'])==t['order']==sum(c[0]**2 for c in chars)
    cent=[j for j,(o,s) in enumerate(zip(t['orders'],t['sizes'])) if o==2 and s==1]
    assert len(cent)==1;z=cent[0]
    rows=[i for i,c in enumerate(chars) if c[z]==-c[0]]
    assert [i+1 for i in rows]==t['faithful_rows']
    rec={'table':t['name'],'faithful_rows':[i+1 for i in rows],
         'faithful_degrees':[chars[i][0] for i in rows],'degree24':[]}
    if t['name']=='2.A6':
        checked=0
        for i in rows:
            c=chars[i];d=c[0]
            for j,v in enumerate(c):
                if t['sizes'][j]==1:continue
                _,a=abs_square(v)
                assert 4*sum(abs(x) for x in a)<=d*d
                checked+=1
        rec['all_nonscalar_trace_half_checks']=checked
    m2=next(a['map'] for a in t['power_maps'] if a['prime']==2)
    for i in rows:
        c=chars[i]
        if c[0]!=24:continue
        nr=[j+1 for j,v in enumerate(c) if conjugate_difference(v)!=(0,)]
        fs=sum(s*mean(c[j-1]) for s,j in zip(t['sizes'],m2))/t['order']
        assert nr and fs==0
        assert all(relation_minus7(v) for v in c)
        rec['degree24'].append({'row':i+1,'nonreal_classes':nr,'Frobenius_Schur':str(fs)})
    out['tables'].append(rec)
assert [x['row'] for x in out['tables'][1]['degree24']]==[16,17]
assert not any(r['degree24'] for r in out['tables'] if r['table']!='2.A8')
# Exact minimal polynomial of b7=ζ+ζ²+ζ⁴.
b=[0,1,1,0,1,0,0];v=[0]*13
for i,a in enumerate(b):
    for j,c in enumerate(b):v[i+j]+=a*c
for j,a in enumerate(b):v[j]+=a
v[0]+=2
assert reduce_poly(v,7)==(0,)
out['degree24_field']='Q(sqrt(-7))'
out['b7_minimal_polynomial']='x^2+x+2'
out['ESD_degree_budget']=[e for e in range(9,25) if 2*((e+1)//2)+10*((e+7)//8)<=2*e+6]
assert out['ESD_degree_budget']==[14,15,16,24]
out['after_D_BI09']=[24]
out['two_factor_minimum']=8*8
assert 2**(12//2-1)>24
(BASE/'audit_spin_inputs.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='tables'}))
