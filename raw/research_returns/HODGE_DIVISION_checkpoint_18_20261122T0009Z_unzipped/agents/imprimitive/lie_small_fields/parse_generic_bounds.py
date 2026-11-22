#!/usr/bin/env python3
"""Safe arithmetic parser and coefficient bounds for published generic tables.

This certificate executes no downloaded Julia code. It interprets
only polynomial arithmetic and formal roots of unity in the table entries.
Every formal phase is assigned absolute value one; positive shifted
coefficient comparisons certify bounds at all real q >= the threshold.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import ast,hashlib,json,re,time
from flint import fmpq_poly,fmpq

BASE=Path(__file__).resolve().parent

def matching(text,pos,left='(',right=')'):
    depth=0
    for j in range(pos,len(text)):
        if text[j]==left:depth+=1
        elif text[j]==right:
            depth-=1
            if depth==0:return j
    raise ValueError('unmatched delimiter')

def split_top(text,delim=','):
    depth=0;start=0;out=[]
    for j,c in enumerate(text):
        if c=='(':depth+=1
        elif c==')':depth-=1
        elif c==delim and depth==0:out.append(text[start:j].strip());start=j+1
    out.append(text[start:].strip())
    return [s for s in out if s]

def rows(text):
    pos=text.index('[',text.index('table ='))
    end=matching(text,pos,'[',']');body=text[pos+1:end];out=[];j=0
    while j<len(body):
        if body[j].isspace():j+=1;continue
        assert body[j]=='['
        k=matching(body,j,'[',']');out.append(split_top(body[j+1:k]));j=k+1
    assert out and len({len(r) for r in out})==1
    return out

class FreeUnits:
    def __init__(self,d):self.d={k:v for k,v in d.items() if v}
    @classmethod
    def scalar(cls,x):return cls({():x if isinstance(x,fmpq_poly) else fmpq_poly([x])})
    def __add__(self,b):
        d=self.d.copy()
        for k,v in b.d.items():d[k]=d.get(k,fmpq_poly())+v
        return FreeUnits(d)
    def __neg__(self):return FreeUnits({k:-v for k,v in self.d.items()})
    def __sub__(self,b):return self+-b
    def __mul__(self,b):
        d={}
        for k,v in self.d.items():
            for l,w in b.d.items():
                kl=tuple(sorted(k+l));d[kl]=d.get(kl,fmpq_poly())+v*w
        return FreeUnits(d)
    def __truediv__(self,b):
        assert set(b.d)=={()} and b.d[()].degree()==0
        c=b.d[()][0];assert c
        return FreeUnits({k:v/c for k,v in self.d.items()})
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        v=FreeUnits.scalar(1)
        for _ in range(k):v=v*self
        return v

def parse_entry(entry):
    phases={};s='';j=0
    while j<len(entry):
        if entry[j:j+2]=='S(':
            k=matching(entry,j+1);args=split_top(entry[j+2:k],';')
            if len(args)==1:s+='('+args[0]+')'
            else:
                assert len(args)==2 and args[1].startswith('exponent=')
                key=re.sub(r'\s+','',args[1]);idx=phases.setdefault(key,len(phases))
                s+='(('+args[0]+')*Z'+str(idx)+')'
            j=k+1
        else:s+=entry[j];j+=1
    s=s.replace('//','/').replace('^','**')
    node=ast.parse(re.sub(r'\s+',' ',s).strip(),mode='eval').body
    def evaluate(n):
        if isinstance(n,ast.Constant):
            assert isinstance(n.value,int)
            return FreeUnits.scalar(n.value)
        if isinstance(n,ast.Name):
            if n.id=='q':return FreeUnits.scalar(fmpq_poly([0,1]))
            assert re.fullmatch(r'Z\d+',n.id)
            return FreeUnits({(int(n.id[1:]),):fmpq_poly([1])})
        if isinstance(n,ast.UnaryOp):
            assert isinstance(n.op,(ast.UAdd,ast.USub));v=evaluate(n.operand)
            return -v if isinstance(n.op,ast.USub) else v
        assert isinstance(n,ast.BinOp)
        a=evaluate(n.left)
        if isinstance(n.op,ast.Pow):
            assert isinstance(n.right,ast.Constant)
            return a**n.right.value
        b=evaluate(n.right)
        if isinstance(n.op,ast.Add):return a+b
        if isinstance(n.op,ast.Sub):return a-b
        if isinstance(n.op,ast.Mult):return a*b
        assert isinstance(n.op,ast.Div)
        return a/b
    return evaluate(node)

def shift(poly,q0):
    c=[F(str(x)) for x in poly.coeffs()]
    return [sum(c[j]*comb(j,k)*q0**(j-k) for j in range(k,len(c))) for k in range(len(c))]

def l1_shift(value,q0):
    out=[]
    for poly in value.d.values():
        c=shift(poly,q0)
        out += [F(0)]*(len(c)-len(out))
        for j,x in enumerate(c):out[j]+=abs(x)
    return out

def certify(item,bound=F(1,4)):
    name=item['name'];q0=item['threshold'];rs=item['entries']
    assert len({len(r) for r in rs})==1
    assert all(e=='S(1)' for e in rs[0])
    parsed=[[parse_entry(e) for e in row] for row in rs]
    declared=[parse_entry(e) for e in item['declared_degrees']]
    assert len(declared)==len(parsed)
    assert all(a.d==b[0].d for a,b in zip(declared,parsed))
    lengths=[parse_entry(e) for e in item['declared_class_lengths']]
    assert len(lengths)==len(rs[0])
    assert lengths[0].d=={():fmpq_poly([1])}
    for v in lengths[1:]:
        assert set(v.d)=={()}
        c=shift(v.d[()],q0)
        assert c[0]>1 and all(x>=0 for x in c)
    failures=[];minimum_degree=None;input_data=[]
    for i,row in enumerate(parsed[1:],1):
        degree=row[0];assert set(degree.d)=={()}
        deg=degree.d[()];dc=shift(deg,q0)
        assert dc[0]>0 and all(x>=0 for x in dc)
        minimum_degree=dc[0] if minimum_degree is None else min(minimum_degree,dc[0])
        entries=[]
        for j,value in enumerate(row[1:],1):
            bc=l1_shift(value,q0);length=max(len(dc),len(bc))
            diff=[bound*(dc[k] if k<len(dc) else 0)-(bc[k] if k<len(bc) else 0) for k in range(length)]
            if any(x<0 for x in diff):failures.append({'row':i+1,'column':j+1,'degree_at_threshold':str(dc[0]),'bound_at_threshold':str(bc[0] if bc else 0),'negative_coefficients':[k for k,x in enumerate(diff) if x<0]})
            entries.append([[str(c) for c in p.coeffs()] for p in value.d.values()])
        input_data.append({'row':i+1,'degree_coefficients':[str(c) for c in deg.coeffs()],'entry_coefficient_polynomials':entries})
    return {'name':name,'source_sha256':item['source']['sha256'],'character_types':len(rs),'class_types':len(rs[0]),'threshold':q0,'target_ratio':str(bound),'minimum_degree_at_threshold':str(minimum_degree),'failures':failures,'polynomial_input':input_data}

def main():
    start=time.monotonic();out=[]
    raw=(BASE/'generic_character_entries.json').read_bytes()
    data=json.loads(raw)
    expected={'G2.01.jl':27,'G2.02.jl':27,'G2.101.jl':28,'G2.103.jl':28,
              'G2.111.jl':31,'G2.113.jl':31,'G2.121.jl':31,'G2.123.jl':31,
              '3D4.0.jl':29,'3D4.11.jl':33,'3D4.13.jl':33}
    assert {t['name'] for t in data['tables']}==set(expected)
    for item in data['tables']:
        assert item['threshold']==(3 if item['name'].startswith('3D4.') else 5)
        r=certify(item);out.append(r)
        assert r['character_types']==r['class_types']==expected[r['name']]
        assert not r['failures']
        print(r['name'],r['character_types'],'q0',r['threshold'],'min_degree',r['minimum_degree_at_threshold'],'failures',len(r['failures']),flush=True)
    result={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),'bound':'1/4',
            'nontrivial_row_types':sum(r['character_types']-1 for r in out),
            'nontrivial_cells':sum((r['character_types']-1)*(r['class_types']-1) for r in out),
            'tables':out,'seconds':round(time.monotonic()-start,3)}
    assert result['nontrivial_row_types']==318 and result['nontrivial_cells']==9242
    # The retained mathematical certificate is deterministic.  Timings belong
    # only to the run summary, so a fresh verifier cannot change its hash.
    certificate={k:v for k,v in result.items() if k!='seconds'}
    (BASE/'generic_polynomial_bounds.json').write_text(json.dumps(certificate,separators=(',',':'))+'\n')
    summary={k:v for k,v in result.items() if k!='tables'}
    summary['tables']=[{k:v for k,v in r.items() if k!='polynomial_input'} for r in out]
    (BASE/'generic_bounds_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(result['status'],result['seconds'])

if __name__=='__main__':main()
