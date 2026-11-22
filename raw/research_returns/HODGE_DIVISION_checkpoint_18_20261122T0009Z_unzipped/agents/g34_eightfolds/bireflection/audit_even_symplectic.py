#!/usr/bin/env python3
"""Independent ESC reconstruction, importing only this reviewer's prior code."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import hashlib,json,re,time
from audit_g2_triality import parse,shifted,plain,block,comma_parts
from check_a1_spectra import spectrum,encode
from audit_sporadic_input import abs_square,rational_mean_abs_square

B=Path(__file__).resolve().parent
SRC=B.parents[1]/'imprimitive/lie_small_fields'
EXPECTED={'Sp4.0.jl':(19,8,F(1,4),196),'Sp6.0.jl':(66,4,F(17,63),378)}

def main():
    start=time.time()
    raw=(SRC/'even_symplectic_generic_inputs.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='49ecbe27ad97b8cfe0204f96ef463ef1e8e0626ce6987bcccb0d8b33041e4fa0'
    data=json.loads(raw)
    assert data['upstream_commit']=='87231738271ed548f62e7f1c98ff2bbfc1ed30d3'
    assert {t['name'] for t in data['tables']}==set(EXPECTED)
    out={'status':'PASS','method':'reviewer sparse Fraction AST parser and reviewer exact Ramanujan Fourier',
         'generic_input_sha256':hashlib.sha256(raw).hexdigest(),
         'generic_rows':0,'generic_cells':0,'generic_tables':[]}
    for t in data['tables']:
        n,q0,c,minimum=EXPECTED[t['name']]
        assert t['threshold']==q0 and F(t['bound'])==c
        original=(SRC/'cache'/t['name']).read_bytes()
        assert hashlib.sha256(original).hexdigest()==t['source']['sha256']
        text=original.decode();body=block(text,text.index('table ='))
        rows=[comma_parts(x) for x in re.findall(r'\[([^\[\]]*)\]',body)]
        assert rows==t['entries'] and len(rows)==n and all(len(r)==n for r in rows)
        for key,var in [('declared_degrees','chardegree'),('declared_class_lengths','classlength')]:
            assert comma_parts(block(text,text.index(var+' =')))==t[key]
        ps=[[parse(x) for x in r] for r in rows]
        assert all(p=={(0,()):F(1)} for p in ps[0])
        assert [parse(x) for x in t['declared_degrees']]==[r[0] for r in ps]
        for j,z in enumerate(t['declared_class_lengths']):
            length=plain(shifted(parse(z),q0))
            if j==0:assert length=={0:F(1)}
            else:assert length[0]>1 and all(v>=0 for v in length.values())
        minima=[]
        for row in ps[1:]:
            degree=plain(shifted(row[0],q0))
            assert all(v>=0 for v in degree.values());minima.append(degree[0])
            for entry in row[1:]:
                triangle={}
                for (k,phase),v in shifted(entry,q0).items():
                    triangle[k]=triangle.get(k,F(0))+abs(v)
                assert all(c*degree.get(k,F(0))>=triangle.get(k,F(0))
                           for k in set(degree)|set(triangle))
                out['generic_cells']+=1
            out['generic_rows']+=1
        assert min(minima)==minimum
        out['generic_tables'].append({'name':t['name'],'rows':n-1,'cells':(n-1)**2,
                                     'q0':q0,'ratio':str(c),'minimum_degree':minimum})
    assert (out['generic_rows'],out['generic_cells'])==(83,4549)

    raw=(SRC/'even_symplectic_small_inputs.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='b51fae6eaa904bb5a1bdcac2f6aa85a940c9968ddba912bf115faa750e772fe2'
    data=json.loads(raw);ts={t['name']:t for t in data['tables']}
    assert set(ts)=={'S4(4)','S4(4).2','S4(4).4','2.S6(2)'}
    assert {m['name']:m['extension_info'] for m in data['metadata']}=={'S4(4)':['','4'],'S6(2)':['2','']}
    chars={name:[[encode(z) for z in c] for c in t['characters']] for name,t in ts.items()}
    out.update(small_input_sha256=hashlib.sha256(raw).hexdigest(),small_rows=0,small_spectra=0,
               normal_fusions=0,small_tables=[])
    for name,t in ts.items():
        cs=chars[name];assert 'origin: ATLAS of finite groups' in t['information']
        assert len(cs)==len(t['orders'])==len(t['sizes'])
        assert sum(c[0]**2 for c in cs)==sum(t['sizes'])==t['order']
        if 'core' in t:
            u=ts[t['core']];fusion=t['fusion'];d=t['order']//u['order']
            assert d in (2,4) and len(fusion)==len(u['orders'])
            assert [i for i,j in enumerate(fusion) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],fusion))
            assert all(sum(s for s,k in zip(u['sizes'],fusion) if k==j)==t['sizes'][j-1] for j in set(fusion))
            pm={p['prime']:p['map'] for p in t['power_maps']}
            for p in u['power_maps']:
                assert all(fusion[k-1]==pm[p['prime']][j-1] for j,k in zip(fusion,p['map']))
            linear=[c for c in cs if c[0]==1];assert len(linear)==d
            assert all(all(c[j-1]==1 for j in fusion) for c in linear)
            assert any(any(any(m==1 and t['orders'][j]//gcd(k,t['orders'][j])==d
                               for k,m in enumerate(spectrum(t,c,j)))
                           for j in range(len(t['orders']))) for c in linear)
            out['normal_fusions']+=1
        record={'name':name,'rows':[],'spectra':0,'quarter_failures':[]}
        for i,c in enumerate(cs):
            a=c[0]
            if a<=1:continue
            if 'core' in t:
                # Select by restriction inner product, not author row indices.
                norm=sum(s*rational_mean_abs_square(c[j-1]) for s,j in zip(u['sizes'],fusion))/u['order']
                assert norm.denominator==1
                if norm!=1:continue
                assert tuple(c[j-1] for j in fusion) in {tuple(r) for r in chars[t['core']]}
            out['small_rows']+=1;ratios=[]
            for j,z in enumerate(c):
                if abs_square(z)[1]==(a*a,):continue
                ms=spectrum(t,c,j);ratios.append(F(a-max(ms),a))
                out['small_spectra']+=1;record['spectra']+=1
            minimum=min(ratios)
            if name!='2.S6(2)':assert minimum>=F(1,3)
            elif a==7:
                assert minimum==F(1,7) and all(isinstance(z,int) for z in c)
                squares=next(p['map'] for p in t['power_maps'] if p['prime']==2)
                indicator=F(sum(s*c[j-1] for s,j in zip(t['sizes'],squares)),t['order'])
                assert indicator==t['indicators'][i]==1
            else:
                assert minimum>=F(2,9)
                if a==8:assert minimum>=F(1,4)
            rr={'row':i+1,'degree':a,'minimum_ratio':str(minimum)}
            record['rows'].append(rr)
            if minimum<F(1,4):record['quarter_failures'].append(rr)
        out['small_tables'].append(record)
    assert (out['small_rows'],out['small_spectra'],out['normal_fusions'])==(104,3442,2)
    assert [len(t['rows']) for t in out['small_tables']]==[26,20,16,42]
    assert [t['spectra'] for t in out['small_tables']]==[676,580,464,1722]
    last=out['small_tables'][-1]
    assert [(r['row'],r['degree'],r['minimum_ratio']) for r in last['quarter_failures']]==[(2,7,'1/7'),(5,21,'5/21'),(6,27,'2/9')]
    assert [r['degree'] for r in last['rows'] if r['degree']<=9]==[7,8]
    assert all(min(r['degree'] for r in t['rows'])==18 for t in out['small_tables'][:3])
    v=(1-F(17,63))/4;assert v==F(23,126)
    assert 6/(12*v-2)==F(63,2)<min(196,378,18**2)
    assert 6/(12*F(2,9)-2)==9 and 12*2>2*8+6
    assert 6/(1+10*F(1,7)-2)==14<7**2
    out.update(author_code_or_scan_imported=False,proof_sha256=hashlib.sha256((SRC/'even_symplectic_section.tex').read_bytes()).hexdigest(),seconds=round(time.time()-start,3))
    (B/'audit_even_symplectic.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('small_tables','generic_tables')},indent=2))

if __name__=='__main__':main()
