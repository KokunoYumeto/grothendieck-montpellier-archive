#!/usr/bin/env python3
"""Peer reconstruction of root's complete A2/2A2 arithmetic.

Original generic expressions -> this reviewer's Fraction AST parser.
Original finite inputs -> restriction inner products and reviewer Fourier.
No author certificates, selected-row lists or spectrum outputs are imported.
The Fourier helper was originally authored by this reviewer and was also
subsequently reused by root; the original GAP spectrum scan is separate.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import ast,hashlib,json,re,time
import sympy as sp
from audit_g2_triality import parse,shifted,plain,block,comma_parts
from audit_sporadic_input import abs_square,rational_mean_abs_square
from check_a1_spectra import spectrum,encode

B=Path(__file__).resolve().parent
SRC=B.parents[2]/'research/a2_cores'
EXPECT={'SL3.1.jl':(5,17,10,30),'SL3.n1.jl':(5,8,8,30),
        'SU3.2.jl':(7,17,10,42),'SU3.n2.jl':(7,8,8,42)}


def phase_at_identity(node):
    if isinstance(node,ast.Constant):
        assert type(node.value)==int
        return sp.Integer(node.value)
    if isinstance(node,ast.Name):
        assert re.fullmatch(r'[a-z][a-z0-9]*',node.id)
        return sp.Integer(0) if node.id=='a' else sp.Symbol(node.id)
    if isinstance(node,ast.Call):
        assert isinstance(node.func,ast.Name) and node.func.id=='R'
        assert len(node.args)==1 and not node.keywords
        return phase_at_identity(node.args[0])
    if isinstance(node,ast.UnaryOp):
        assert isinstance(node.op,(ast.UAdd,ast.USub))
        return (-1 if isinstance(node.op,ast.USub) else 1)*phase_at_identity(node.operand)
    assert isinstance(node,ast.BinOp)
    a,b=phase_at_identity(node.left),phase_at_identity(node.right)
    if isinstance(node.op,ast.Add):return a+b
    if isinstance(node.op,ast.Sub):return a-b
    if isinstance(node.op,ast.Mult):return a*b
    if isinstance(node.op,ast.Div):return a/b
    assert isinstance(node.op,ast.Pow) and isinstance(node.right,ast.Constant)
    assert type(node.right.value)==int and node.right.value>=0
    return a**int(b)


def identity_degree(expression):
    tree=ast.parse(expression.replace(';',',').replace('//','/').replace('^','**'),mode='eval')
    for n in ast.walk(tree):
        if isinstance(n,ast.keyword):
            assert n.arg=='exponent' and sp.cancel(phase_at_identity(n.value))==0
    d={}
    for (k,u),v in parse(expression).items():d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}


def main():
    start=time.perf_counter()
    raw=(SRC/'generic_inputs.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='4df14adc254b80d4d7a03ea18e9449c1e05c1ba72f2ad8b713067c8f252b01a2'
    data=json.loads(raw)
    assert data['upstream_commit']=='87231738271ed548f62e7f1c98ff2bbfc1ed30d3'
    assert {t['name'] for t in data['tables']}==set(EXPECT)
    out={'status':'PASS','generic_input_sha256':hashlib.sha256(raw).hexdigest(),
         'generic_rows':0,'generic_cells':0,'generic_tables':[]}
    for t in data['tables']:
        q0,nr,nc,minimum=EXPECT[t['name']]
        original=(SRC/'cache'/t['name']).read_bytes()
        assert hashlib.sha256(original).hexdigest()==t['source']['sha256']
        text=original.decode()
        rows=[comma_parts(x) for x in re.findall(r'\[([^\[\]]*)\]',block(text,text.index('table =')))]
        assert rows==t['entries'] and len(rows)==nr and all(len(r)==nc for r in rows)
        for key,var in [('declared_degrees','chardegree'),('declared_class_lengths','classlength')]:
            assert comma_parts(block(text,text.index(var+' =')))==t[key]
        degrees=[parse(s) for s in t['declared_degrees']]
        assert all(r=='S(1)' for r in rows[0]) and t['central_column']==1
        assert [identity_degree(r[0]) for r in rows]==[plain(d) for d in degrees]
        for j,s in enumerate(t['declared_class_lengths']):
            p=plain(shifted(parse(s),q0))
            if j==0:assert p=={0:F(1)}
            else:assert p[0]>1 and all(v>=0 for v in p.values())
        minima=[]
        for row,d in zip(rows[1:],degrees[1:]):
            degree=plain(shifted(d,q0));minima.append(degree[0])
            assert all(v>=0 for v in degree.values())
            for expression in row[1:]:
                bound={}
                for (k,phase),v in shifted(parse(expression),q0).items():
                    bound[k]=bound.get(k,F(0))+abs(v)
                assert all(degree.get(k,F(0))/4>=bound.get(k,F(0))
                           for k in set(degree)|set(bound))
                out['generic_cells']+=1
            out['generic_rows']+=1
        assert min(minima)==minimum
        out['generic_tables'].append({'name':t['name'],'q0':q0,'rows':nr-1,
                                      'cells':(nr-1)*(nc-1),'minimum':minimum,'ratio':'1/4'})
    assert (out['generic_rows'],out['generic_cells'])==(46,386)

    raw=(SRC/'small_inputs.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='3f356063efc3a3987126ddbbb6d12b0540fd71151f93eb4e83f4c3f6c26607e8'
    data=json.loads(raw);ts={t['name']:t for t in data['tables']}
    assert len(ts)==len(data['tables'])==47
    chars={n:[[encode(z) for z in row] for row in t['characters']] for n,t in ts.items()}
    out.update(small_input_sha256=hashlib.sha256(raw).hexdigest(),
               small_rows=0,small_spectra=0,normal_fusions=0,small_tables=[])
    for name,t in ts.items():
        cs=chars[name]
        if name=='(4^2x3).L3(4)':
            assert t['information']=="constructed using `PossibleCharacterTablesOfTypeV4G'"
        else:
            assert 'origin: ATLAS of finite groups' in t['information']
        assert len(cs)==len(t['sizes'])==len(t['orders'])
        assert sum(t['sizes'])==t['order']==sum(c[0]**2 for c in cs)
        assert all(len(c)==len(cs) for c in cs)
        if 'core' in t:
            core=ts[t['core']];fusion=t['fusion'];d=t['order']//core['order']
            assert d in (2,3,4,6) and len(fusion)==len(core['orders'])
            assert [i for i,j in enumerate(fusion) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(core['orders'],fusion))
            assert all(sum(s for s,k in zip(core['sizes'],fusion) if k==j)==t['sizes'][j-1] for j in set(fusion))
            powers={p['prime']:p['map'] for p in t['power_maps']}
            for p in core['power_maps']:
                assert all(fusion[k-1]==powers[p['prime']][j-1] for j,k in zip(fusion,p['map']))
            linear=[c for c in cs if c[0]==1]
            assert len(linear)==d
            assert all(all(c[j-1]==1 for j in fusion) for c in linear)
            assert any(any(any(m==1 and t['orders'][j]//gcd(k,t['orders'][j])==d
                               for k,m in enumerate(spectrum(t,c,j)))
                           for j in range(len(cs))) for c in linear)
            out['normal_fusions']+=1
        selected=[];count=0;minimum=10**100;ratio=F(1)
        for i,c in enumerate(cs):
            a=c[0]
            if a<=1:continue
            if 'core' in t:
                norm=sum(s*rational_mean_abs_square(c[j-1]) for s,j in zip(core['sizes'],fusion))/core['order']
                assert norm.denominator==1
                if norm!=1:continue
            selected.append(i+1);minimum=min(minimum,a)
            for j,z in enumerate(c):
                if abs_square(z)[1]==(a*a,):continue
                ms=spectrum(t,c,j)
                assert all(type(v)==int and v>=0 for v in ms) and sum(ms)==a
                nu=a-max(ms);assert 4*nu>=a
                ratio=min(ratio,F(nu,a));count+=1
        assert selected and minimum>=6
        out['small_rows']+=len(selected);out['small_spectra']+=count
        out['small_tables'].append({'name':name,'rows':len(selected),'spectra':count,
                                    'minimum_degree':minimum,'minimum_support_ratio':str(ratio)})
    assert (out['small_rows'],out['small_spectra'],out['normal_fusions'])==(1603,141024,34)
    assert min(t['minimum_degree'] for t in out['small_tables'])==6
    cyclic_cores=['L3(4)','2.L3(4)','3.L3(4)','4_1.L3(4)','4_2.L3(4)',
                  '6.L3(4)','12_1.L3(4)','12_2.L3(4)']
    assert min(t['minimum_degree'] for t in out['small_tables'] if t['name'] in cyclic_cores)==6
    out['provenance_note']='46 ATLAS-origin tables; the universal cover is a corroborating CTblLib construction. The essential projective minimum6 is checked from the eight cyclic-center core tables.'
    assert F(1)-F(1,4)==F(3,4) and (1-F(1,4))/4==F(3,16)
    assert F(6)/(12*F(3,16)-2)==24<36
    assert 12*2>2*6+6
    out['elapsed_seconds']=round(time.perf_counter()-start,6)
    B.joinpath('audit_a2_cores.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['generic_tables','small_tables']},indent=2))


if __name__=='__main__':main()
