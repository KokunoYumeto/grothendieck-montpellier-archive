#!/usr/bin/env python3
"""Exact linear-Weil endpoint and arithmetic; independent of the GAP scan."""
from pathlib import Path
from fractions import Fraction as F
from math import lcm
import hashlib,json,time
from check_a1_spectra import spectrum,encode
from audit_sporadic_input import abs_square,reduce_poly

BASE=Path(__file__).resolve().parent
P=BASE/'linear_weil/linear_weil_inputs.json'
NAMES=['3.L3(4)','3.L3(4).2_1','3.L3(4).2_2','3.L3(4).2_3','3.L3(4).3','3.L3(4).6']

def equal(x,y):
    if isinstance(x,int) and isinstance(y,int):return x==y
    nx,cx=(1,(x,)) if isinstance(x,int) else x
    ny,cy=(1,(y,)) if isinstance(y,int) else y
    n=lcm(nx,ny);v=[0]*n
    for j,c in enumerate(cx):v[j*(n//nx)]+=c
    for j,c in enumerate(cy):v[j*(n//ny)]-=c
    return reduce_poly(v,n)==(0,)

def main():
    start=time.time();raw=P.read_bytes();data=json.loads(raw)
    ts={t['name']:t for t in data['tables']};assert set(ts)==set(NAMES)
    assert data['simple_extension_info']==['(3x4^2)','D12']
    u=ts[NAMES[0]]
    chars={n:[[encode(v) for v in c] for c in t['characters']] for n,t in ts.items()}
    core_rows=[i for i,c in enumerate(chars[NAMES[0]]) if c[0]==21]
    assert core_rows==[16,17]
    out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
         'method':'independent polynomial restriction selection and complete Ramanujan Fourier',
         'tables':[],'rows':0,'entries':0,'normal_fusions':0}
    for name in NAMES:
        t=ts[name];cs=chars[name]
        assert 'origin: ATLAS of finite groups' in t['information']
        assert sum(t['sizes'])==sum(c[0]**2 for c in cs)==t['order']
        assert len(cs)==len(t['orders'])==len(t['sizes'])
        f=t.get('fusion',list(range(1,len(u['orders'])+1)))
        if 'core' in t:
            assert t['core']==NAMES[0]
            assert [i for i,j in enumerate(f) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],f))
            assert all(sum(s for s,jj in zip(u['sizes'],f) if jj==j)==t['sizes'][j-1] for j in set(f))
            pm={r['prime']:r['map'] for r in t['power_maps']}
            for r in u['power_maps']:
                assert all(f[k-1]==pm[r['prime']][j-1] for j,k in zip(f,r['map']))
            # A/U is cyclic: its full linear-character group has its order,
            # and one retained linear character has a value of that order.
            d=t['order']//u['order'];linear=[c for c in cs if c[0]==1]
            assert len(linear)==d
            assert any(any(sum(v!=0 for v in spectrum(t,c,j))==1 and
                               any(v==1 and lcm(t['orders'][j],k)//k==d
                                   for k,v in enumerate(spectrum(t,c,j)) if k)
                           for j in range(len(c))) for c in linear)
            out['normal_fusions']+=1
        rows=[i for i,c in enumerate(cs) if c[0]==21 and any(
            all(equal(c[j-1],z) for j,z in zip(f,chars[NAMES[0]][k])) for k in core_rows)]
        rr={'table':name,'selected_rows':[i+1 for i in rows],'entries':0,'row_data':[]}
        for i in rows:
            c=cs[i];nus=[]
            for j,z in enumerate(c):
                if abs_square(z)[1]==(441,):continue
                ms=spectrum(t,c,j);nu=21-max(ms);assert nu>=8
                nus.append(nu);rr['entries']+=1;out['entries']+=1
            assert min(nus)==8
            rr['row_data'].append({'row':i+1,'min_nu':min(nus)})
            out['rows']+=1
        out['tables'].append(rr)
    assert out['rows']==24 and out['entries']==1288 and out['normal_fusions']==5
    assert [r['selected_rows'] for r in out['tables']]==[[17,18],[27,28,29,30],[],[],list(range(25,31)),list(range(31,43))]
    # Proved monotonicity extends the two smallest large-parameter witnesses.
    def A(q,n):return (q**n-q)//(q-1)
    def B(q,n):return F(q**(n-1)+q-2,q-1)
    assert A(5,3)-3*B(5,3)==9>6
    assert A(4,4)-3*B(4,4)==18>6
    assert F(13)*3-5*5==14>12
    assert F(12)*(3-F(5,3))==16>12
    assert F(20)*(3-F(5,4))==35>12
    assert 6/(1-3*F(2,7))==42<21**2
    assert 12*8>2*21+6
    for a in [6,14]:
        bound=F(24*a,a+10);assert bound<a*a
        assert 12*((a+3)//4)>2*a+6
    assert F(30,2)+5>12
    out['arithmetic_endpoints']={'q5_n3':9,'q4_n4':18,'q4_n3_degree21_total_cutoff':42,
                                'q2_single_degrees':[6,14],'all_remaining_branch_budgets_contradicted':True}
    out['seconds']=round(time.time()-start,3)
    (BASE/'check_linear_weil.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'},indent=2))

if __name__=='__main__':main()
