#!/usr/bin/env python3
"""Exploratory all-parameter polynomial bounds for the four A2 tables.

Only frozen mathematical entries are parsed; downloaded Julia is never run.
This is not yet a theorem or a complete normalizer calculation.
"""
from pathlib import Path
from fractions import Fraction as F
import ast, hashlib, json, re, sys
import sympy as sp
from flint import fmpq_poly

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
sys.path.insert(0,str(ROOT/'agents/imprimitive/lie_small_fields'))
from parse_generic_bounds import rows, parse_entry, matching, split_top, shift, l1_shift
from build_generic_input import array, compact

CONDITIONS={'SL3.1.jl':'q = 1 mod 3','SL3.n1.jl':'q != 1 mod 3',
            'SU3.2.jl':'q = 2 mod 3','SU3.n2.jl':'q != 2 mod 3'}

def identity_exponent(expr):
    """Interpret a phase exponent safely, setting the central parameter a=0."""
    node=ast.parse(expr.replace('//','/').replace('^','**'),mode='eval').body
    names={s:sp.Symbol(s) for s in ('q','m','n','b')};names['a']=sp.Integer(0)
    def val(n):
        if isinstance(n,ast.Constant):
            assert isinstance(n.value,int);return sp.Integer(n.value)
        if isinstance(n,ast.Name):return names[n.id]
        if isinstance(n,ast.Call):
            assert isinstance(n.func,ast.Name) and n.func.id=='R' and len(n.args)==1 and not n.keywords
            return val(n.args[0])
        if isinstance(n,ast.UnaryOp):
            assert isinstance(n.op,(ast.UAdd,ast.USub));return -val(n.operand) if isinstance(n.op,ast.USub) else val(n.operand)
        assert isinstance(n,ast.BinOp)
        a,b=val(n.left),val(n.right)
        if isinstance(n.op,ast.Add):return a+b
        if isinstance(n.op,ast.Sub):return a-b
        if isinstance(n.op,ast.Mult):return a*b
        if isinstance(n.op,ast.Div):return a/b
        assert isinstance(n.op,ast.Pow) and isinstance(n.right,ast.Constant) and n.right.value>=0
        return a**int(b)
    return sp.cancel(val(node))

def check_identity(entry,degree):
    pos=0
    while True:
        pos=entry.find('S(',pos)
        if pos<0:break
        end=matching(entry,pos+1)
        args=split_top(entry[pos+2:end],';')
        if len(args)>1:
            assert len(args)==2 and args[1].startswith('exponent=')
            assert identity_exponent(args[1][len('exponent='):])==0
        pos=end+1
    z=parse_entry(entry)
    assert sum(z.d.values(),fmpq_poly())==degree

def main():
    manifest=json.loads((BASE/'retrieval.json').read_text())
    assert manifest['commit']=='87231738271ed548f62e7f1c98ff2bbfc1ed30d3'
    inputs={'upstream_commit':manifest['commit'],'tables':[]};results=[]
    for src in manifest['files']:
        name=Path(src['path']).name;raw=(BASE/'cache'/name).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==src['sha256'] and len(raw)==src['bytes']
        text=raw.decode();rs=[[compact(e) for e in r] for r in rows(text)]
        degs=[compact(e) for e in array(text,'chardegree')]
        lengths=[compact(e) for e in array(text,'classlength')]
        assert len(rs)==len(degs) and len(rs[0])==len(lengths)
        assert all(e=='S(1)' for e in rs[0])
        ds=[parse_entry(e) for e in degs];ls=[parse_entry(e) for e in lengths]
        assert all(set(v.d)=={()} for v in ds+ls)
        assert ls[0].d[()]==fmpq_poly([1])
        for r,d in zip(rs,ds):check_identity(r[0],d.d[()])
        ps=[[parse_entry(e) for e in r] for r in rs]
        item={'name':name,'source':src,'condition':CONDITIONS[name],
              'entries':rs,'declared_degrees':degs,'declared_class_lengths':lengths,
              'central_column':1,'identity_parameter':'a=0 in the central class type'}
        inputs['tables'].append(item)
        probes=[]
        for q0 in (3,4,5,6,7,8,9,11,13):
            dc=[shift(d.d[()],q0) for d in ds]
            assert all(c[0]>0 and all(x>=0 for x in c) for c in dc)
            lc=[shift(v.d[()],q0) for v in ls[1:]]
            assert all(c[0]>1 and all(x>=0 for x in c) for c in lc)
            fail=[]
            for i,r in enumerate(ps[1:],1):
                for j,v in enumerate(r[1:],1):
                    bc=l1_shift(v,q0);d=dc[i]
                    diff=[(d[k] if k<len(d) else 0)/4-(bc[k] if k<len(bc) else 0) for k in range(max(len(d),len(bc)))]
                    if any(x<0 for x in diff):fail.append({'row':i+1,'column':j+1,'degree':str(d[0]),'entry_bound':str(bc[0] if bc else 0),'negative_coefficients':[k for k,x in enumerate(diff) if x<0]})
            probes.append({'q0':q0,'minimum_degree':str(min(c[0] for c in dc[1:])),'failures':fail})
        results.append({'name':name,'character_types':len(rs),'class_types':len(rs[0]),'probes':probes})
    (BASE/'generic_inputs.json').write_text(json.dumps(inputs,separators=(',',':'))+'\n')
    (BASE/'generic_probes.json').write_text(json.dumps({'scope':'Exploratory all-q polynomial inequalities; no normalizer or geometric theorem yet.','tables':results},indent=2)+'\n')
    print(json.dumps([{'name':t['name'],'rows':t['character_types'],'columns':t['class_types'],'probes':[{'q0':p['q0'],'minimum_degree':p['minimum_degree'],'failures':len(p['failures'])} for p in t['probes']]} for t in results],indent=2))

if __name__=='__main__':main()
