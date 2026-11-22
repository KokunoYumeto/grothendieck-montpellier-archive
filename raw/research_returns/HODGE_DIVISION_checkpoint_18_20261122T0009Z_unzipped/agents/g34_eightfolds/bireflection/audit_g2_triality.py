#!/usr/bin/env python3
"""Independent original-expression parser, all-q inequalities and small spectra."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import ast,re,hashlib,json,time
from check_a1_spectra import spectrum,encode
from audit_sporadic_input import abs_square,rational_mean_abs_square

B=Path(__file__).resolve().parent
SRC=B.parents[1]/'imprimitive/lie_small_fields'
EXPECTED={'G2.01.jl':(27,5,126),'G2.02.jl':(27,5,124),
 'G2.101.jl':(28,5,280),'G2.103.jl':(28,5,280),
 'G2.111.jl':(31,5,126),'G2.113.jl':(31,5,126),
 'G2.121.jl':(31,5,124),'G2.123.jl':(31,5,124),
 '3D4.0.jl':(29,3,219),'3D4.11.jl':(33,3,219),'3D4.13.jl':(33,3,219)}

# Sparse polynomials: (degree of q, multiset of formal phase atoms) -> rational.
def tidy(d):return {k:v for k,v in d.items() if v}
def add(a,b,sgn=1):
    d=a.copy()
    for k,v in b.items():d[k]=d.get(k,F(0))+sgn*v
    return tidy(d)
def mul(a,b):
    d={}
    for (i,u),x in a.items():
        for (j,v),y in b.items():
            k=(i+j,tuple(sorted(u+v)));d[k]=d.get(k,F(0))+x*y
    return tidy(d)
class RemoveRingCoercion(ast.NodeTransformer):
    def visit_Call(self,node):
        assert isinstance(node.func,ast.Name) and node.func.id=='R' and len(node.args)==1 and not node.keywords
        return self.visit(node.args[0])
def value(n):
    if isinstance(n,ast.Constant):
        assert type(n.value)==int;return tidy({(0,()):F(n.value)})
    if isinstance(n,ast.Name):
        assert n.id=='q';return {(1,()):F(1)}
    if isinstance(n,ast.UnaryOp):
        assert isinstance(n.op,(ast.UAdd,ast.USub))
        return {k:(-v if isinstance(n.op,ast.USub) else v) for k,v in value(n.operand).items()}
    if isinstance(n,ast.Call):
        assert isinstance(n.func,ast.Name) and n.func.id=='S' and len(n.args)==1
        p=value(n.args[0]);assert len(n.keywords)<=1
        if not n.keywords:return p
        kw=n.keywords[0];assert kw.arg=='exponent'
        phase=RemoveRingCoercion().visit(kw.value)
        for t in ast.walk(phase):
            assert isinstance(t,(ast.BinOp,ast.UnaryOp,ast.Constant,ast.Name,ast.Load,
                                  ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Pow,ast.USub,ast.UAdd)),ast.dump(t)
            if isinstance(t,ast.Constant):assert type(t.value)==int
            if isinstance(t,ast.Name):assert re.fullmatch(r'[a-z][a-z0-9]*',t.id)
        atom=ast.dump(phase,include_attributes=False)
        return {(j,tuple(sorted(u+(atom,)))):c for (j,u),c in p.items()}
    assert isinstance(n,ast.BinOp)
    a=value(n.left)
    if isinstance(n.op,ast.Pow):
        assert isinstance(n.right,ast.Constant) and type(n.right.value)==int and n.right.value>=0
        p={(0,()):F(1)}
        for _ in range(n.right.value):p=mul(p,a)
        return p
    b=value(n.right)
    if isinstance(n.op,ast.Add):return add(a,b)
    if isinstance(n.op,ast.Sub):return add(a,b,-1)
    if isinstance(n.op,ast.Mult):return mul(a,b)
    assert isinstance(n.op,ast.Div) and set(b)=={(0,())}
    return {k:v/b[0,()] for k,v in a.items()}
def parse(txt):
    return value(ast.parse(txt.replace(';',',').replace('//','/').replace('^','**'),mode='eval').body)
def shifted(p,q0):
    d={}
    for (j,u),v in p.items():
        for k in range(j+1):d[k,u]=d.get((k,u),F(0))+v*comb(j,k)*q0**(j-k)
    return tidy(d)
def plain(p):
    assert all(not u for j,u in p)
    return {j:v for (j,u),v in p.items()}
def block(text,start):
    i=text.index('[',start);depth=0
    for j in range(i,len(text)):
        depth+=(text[j]=='[')-(text[j]==']')
        if depth==0:return text[i+1:j]
    raise AssertionError('bracket')
def comma_parts(text):
    depth=0;last=0;out=[]
    for j,c in enumerate(text):
        depth+=(c=='(')-(c==')')
        if c==',' and depth==0:out.append(text[last:j]);last=j+1
    out.append(text[last:])
    return [re.sub(r'\s+',' ',x).strip() for x in out if x.strip()]

def main():
    start=time.time();raw=(SRC/'generic_character_entries.json').read_bytes();data=json.loads(raw)
    assert hashlib.sha256(raw).hexdigest()=='66ad9b13d457d141d424084336787b3bb1f9d53818475b806f7a6cc24eb3664b'
    assert {t['name'] for t in data['tables']}==set(EXPECTED)
    output={'status':'PASS','method':'new sparse Fraction AST parser from original expressions; own Ramanujan small spectra',
            'generic_input_sha256':hashlib.sha256(raw).hexdigest(),'generic_tables':[],'generic_rows':0,'generic_cells':0}
    for t in data['tables']:
        n,q0,mindeg=EXPECTED[t['name']];assert t['threshold']==q0
        original=(SRC/'cache'/t['name']).read_bytes()
        assert hashlib.sha256(original).hexdigest()==t['source']['sha256']
        text=original.decode();tablebody=block(text,text.index('table ='))
        rs=[comma_parts(x) for x in re.findall(r'\[([^\[\]]*)\]',tablebody)]
        assert rs==t['entries'] and len(rs)==n and all(len(r)==n for r in rs)
        for key,var in [('declared_degrees','chardegree'),('declared_class_lengths','classlength')]:
            assert comma_parts(block(text,text.index(var+' =')))==t[key]
        ps=[[parse(x) for x in r] for r in rs]
        assert all(p=={(0,()):F(1)} for p in ps[0])
        assert [parse(x) for x in t['declared_degrees']]==[r[0] for r in ps]
        for j,z in enumerate(t['declared_class_lengths']):
            length=plain(shifted(parse(z),q0))
            if j==0:assert length=={0:F(1)}
            else:assert length[0]>1 and all(v>=0 for v in length.values())
        mins=[]
        for row in ps[1:]:
            d=plain(shifted(row[0],q0));assert all(x>=0 for x in d.values());mins.append(d[0])
            for p in row[1:]:
                bound={}
                for (k,u),v in shifted(p,q0).items():bound[k]=bound.get(k,F(0))+abs(v)
                assert all(d.get(k,F(0))>=4*bound.get(k,F(0)) for k in set(d)|set(bound))
                output['generic_cells']+=1
            output['generic_rows']+=1
        assert min(mins)==mindeg
        output['generic_tables'].append({'name':t['name'],'minimum_degree':mindeg,'threshold':q0})
    assert output['generic_rows']==318 and output['generic_cells']==9242
    smallraw=(SRC/'g2_triality_small_inputs.json').read_bytes();small=json.loads(smallraw)
    assert hashlib.sha256(smallraw).hexdigest()=='e4a8aefbf5a4a32a5b31b217143ccae03db8b9f3753cc2e91a6169d0364b6a7c'
    ts={t['name']:t for t in small['tables']}
    assert set(ts)=={'3.G2(3)','3.G2(3).2','2.G2(4)','2.G2(4).2','3D4(2)','3D4(2).3'}
    output.update(small_rows=0,small_spectra=0,small_tables=[])
    for name,t in ts.items():
        cs=[[encode(v) for v in c] for c in t['characters']]
        assert sum(c[0]**2 for c in cs)==sum(t['sizes'])==t['order']
        if 'core' in t:
            u=ts[t['core']];f=t['fusion'];assert len(f)==len(u['orders'])
            assert [i for i,j in enumerate(f) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],f))
            assert all(sum(s for s,jj in zip(u['sizes'],f) if jj==j)==t['sizes'][j-1] for j in set(f))
            pm={x['prime']:x['map'] for x in t['power_maps']}
            for r in u['power_maps']:assert all(f[k-1]==pm[r['prime']][j-1] for j,k in zip(f,r['map']))
        ratios=[];degrees=[];selected=[]
        for i,c in enumerate(cs):
            a=c[0]
            if a<=1:continue
            if 'core' in t:
                norm=sum(s*rational_mean_abs_square(c[j-1]) for s,j in zip(u['sizes'],f))/u['order']
                assert norm.denominator==1
                if norm!=1:continue
            selected.append(i+1);degrees.append(a);output['small_rows']+=1
            for j,z in enumerate(c):
                if abs_square(z)[1]==(a*a,):continue
                ms=spectrum(t,c,j);nu=a-max(ms);assert 4*nu>=a
                ratios.append(F(nu,a));output['small_spectra']+=1
        output['small_tables'].append({'name':name,'selected_rows':selected,'minimum_degree':min(degrees),'minimum_ratio':str(min(ratios))})
    assert output['small_rows']==239 and output['small_spectra']==11502
    assert [(t['minimum_degree'],t['minimum_ratio']) for t in output['small_tables']]==[(14,'3/7'),(14,'3/7'),(12,'1/3'),(12,'1/3'),(26,'4/13'),(26,'4/13')]
    output['proof_sha256']=hashlib.sha256((SRC/'g2_triality_section.tex').read_bytes()).hexdigest()
    output['author_program_imported']=False;output['seconds']=round(time.time()-start,3)
    (B/'audit_g2_triality.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if not k.endswith('tables')},indent=2))

if __name__=='__main__':main()
