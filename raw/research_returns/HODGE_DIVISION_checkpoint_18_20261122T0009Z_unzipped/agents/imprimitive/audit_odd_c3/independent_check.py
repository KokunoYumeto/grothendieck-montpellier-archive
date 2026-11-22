#!/usr/bin/env python3
"""Independent odd-C3 audit: source extraction, exact polynomials and spectra.

No author parser, arithmetic, selected rows or certificate is imported.
The previously reviewed auditor cyclotomic implementation is reused.
"""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
import ast, hashlib, importlib.util, json, re, time
from flint import fmpq_poly

B = Path(__file__).resolve().parent
A = B.parents[1] / 'g34_eightfolds/bireflection/csp6_odd'
H = B.parent / 'sporadic/verify_quarter_bound.py'
spec = importlib.util.spec_from_file_location('auditor_cyclotomic', H)
cyc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cyc)

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def close(s, i):
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for j in range(i, len(s)):
        c = s[j]
        if c in pairs: stack.append(pairs[c])
        elif c in ')]}':
            assert stack and stack.pop() == c
            if not stack: return j
    raise AssertionError('unclosed delimiter')

def list_body(s, name):
    i = s.index('[', s.index(name + ' ='))
    return s[i+1:close(s, i)]

def commas(s):
    stack = []; start = 0; out = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for i, c in enumerate(s):
        if c in pairs: stack.append(pairs[c])
        elif c in ')]}': assert stack and stack.pop() == c
        elif c == ',' and not stack:
            if s[start:i].strip(): out.append(s[start:i].strip())
            start = i+1
    assert not stack
    if s[start:].strip(): out.append(s[start:].strip())
    return out

@lru_cache(None)
def polynomial(s):
    tree = ast.parse(re.sub(r'\s+', ' ', s.strip()).replace('//','/').replace('^','**'), mode='eval')
    def ev(n):
        if isinstance(n, ast.Constant):
            assert type(n.value) is int
            return fmpq_poly([n.value])
        if isinstance(n, ast.Name):
            assert n.id == 'q'; return fmpq_poly([0,1])
        if isinstance(n, ast.Call):
            assert isinstance(n.func,ast.Name) and n.func.id == 'R' and len(n.args)==1 and not n.keywords
            return ev(n.args[0])
        if isinstance(n,ast.UnaryOp):
            assert isinstance(n.op,(ast.USub,ast.UAdd))
            return -ev(n.operand) if isinstance(n.op,ast.USub) else ev(n.operand)
        assert isinstance(n,ast.BinOp)
        x=ev(n.left)
        if isinstance(n.op,ast.Pow):
            assert isinstance(n.right,ast.Constant) and type(n.right.value) is int and n.right.value>=0
            return x**n.right.value
        y=ev(n.right)
        if isinstance(n.op,ast.Add): return x+y
        if isinstance(n.op,ast.Sub): return x-y
        if isinstance(n.op,ast.Mult): return x*y
        assert isinstance(n.op,ast.Div) and y.degree()==0 and y[0]
        return x/y[0]
    return ev(tree.body)

def shift(p, at=5):
    c=[Q(str(z)) for z in p.coeffs()]
    return [sum(c[j]*comb(j,k)*at**(j-k) for j in range(k,len(c))) for k in range(len(c))]

def parts(s):
    if s=='S()': return []
    assert s.startswith('S(Dict(') and s.endswith('), simplify=false)')
    ans=[]
    for z in commas(s[7:-18]):
        assert z.count('=>')==1
        phase,coeff=z.split('=>')
        assert re.fullmatch(r'[a-zA-Z0-9\s()/*+^\-]+',phase)
        ans.append((phase.strip(), polynomial(coeff)))
    return ans

def generic():
    source=A/'cache/CSp6.1.jl'; raw=source.read_text()
    assert digest(source)=='f5e68e9429054370df7376f174a095bc548cf1ecf7ce44f5446f1eaebba250dc'
    body=list_body(raw,'table'); rows=[]; i=0
    while i<len(body):
        if body[i].isspace() or body[i]==',': i+=1; continue
        assert body[i]=='['; j=close(body,i); rows.append(commas(body[i+1:j])); i=j+1
    degrees=commas(list_body(raw,'chardegree'))
    lengths=commas(list_body(raw,'classlength'))
    types=[list(map(int,m)) for m in re.findall(r'\[\[(\d+), (\d+)\]',list_body(raw,'classinfo'))]
    extracted={'source_sha256':digest(source),'entries':rows,'degrees':degrees,'class_lengths':lengths,'class_type_pairs':types}
    assert extracted==json.loads((A/'generic_inputs.json').read_text())
    assert len(rows)==len(degrees)==100 and len(lengths)==len(types)==90
    assert all(len(row)==90 for row in rows)
    ds=list(map(polynomial,degrees)); ls=list(map(polynomial,lengths))
    assert ds[0]==ls[0]==fmpq_poly([1])
    for p in ls[1:]:
        c=shift(p); assert c[0]>1 and min(c)>=0
    floor=fmpq_poly([-1,0,0,1]); total=0; smallest=None; coefficient_hash=hashlib.sha256()
    for i,row in enumerate(rows):
        center=parts(row[0]); cp=fmpq_poly()
        for phase,p in center:
            assert 'i1' in phase and all(v not in phase for v in ('i2','i3','i4'))
            cp+=p
        assert cp==ds[i]
        if i==0: continue
        assert all(v>=0 for v in shift(ds[i]-floor))
        dc=shift(ds[i]); smallest=dc[0] if smallest is None else min(smallest,dc[0])
        for s in row[1:]:
            tri=[]
            for phase,p in parts(s):
                cs=shift(p); tri += [Q(0)]*max(0,len(cs)-len(tri))
                for k,x in enumerate(cs): tri[k]+=abs(x)
            n=max(len(dc),len(tri))
            diff=[(dc[k] if k<len(dc) else 0)/4-(tri[k] if k<len(tri) else 0) for k in range(n)]
            assert min(diff)>=0
            coefficient_hash.update((','.join(map(str,diff))+';').encode()); total+=1
    assert total==8811 and smallest==124
    return {'status':'PASS','source_sha256':digest(source),'input_sha256':digest(A/'generic_inputs.json'),
            'source_reextraction':'all entries, degrees, class lengths and class types match',
            'character_types':100,'class_types':90,'inequalities':total,'threshold':5,
            'minimum_degree_at_threshold':str(smallest),'all_degree_floors':'q^3-1',
            'difference_coefficients_sha256':coefficient_hash.hexdigest()}

def spectra():
    p=A/'small_inputs.json'; data=json.loads(p.read_text()); tabs={t['name']:t for t in data['tables']}
    assert set(tabs)=={'2.S6(3)','2.S6(3).2'}
    cs={n:[[cyc.key(z) for z in r] for r in t['characters']] for n,t in tabs.items()}
    out=[]; total_rows=total_entries=0
    for name,t in tabs.items():
        assert 'origin: ATLAS of finite groups' in t['information']
        assert sum(c[0]**2 for c in cs[name])==sum(t['sizes'])==t['order']
        rows=[]
        if 'core' in t:
            core=tabs[t['core']]; f=t['fusion']; assert t['order']==2*core['order']
            assert len(f)==len(core['orders'])
            assert all(core['orders'][j]==t['orders'][f[j]-1] for j in range(len(f)))
            assert sum(t['sizes'][j-1] for j in set(f))==core['order']
            for power in core['power_maps']:
                other=next(v['map'] for v in t['power_maps'] if v['prime']==power['prime'])
                assert all(f[power['map'][j]-1]==other[f[j]-1] for j in range(len(f)))
        records=[]; entry_count=0; ratio=Q(1); min_degree=None
        for i,c in enumerate(cs[name]):
            a=c[0]
            if a==1: continue
            if 'core' in t:
                rest=tuple(c[j-1] for j in t['fusion'])
                matches=[k for k,d in enumerate(cs[t['core']]) if tuple(d)==rest]
                if not matches: continue
                assert len(matches)==1
            rows.append(i+1); min_degree=a if min_degree is None else min(min_degree,a)
            rowratio=Q(1); witnesses=[]
            for j,z in enumerate(c):
                if cyc.squared_norm(z)==(a*a,): continue
                ms=cyc.cyclic_multiplicities(t,c,j); nu=a-max(ms); frac=Q(nu,a)
                assert frac>=Q(1,4)
                ratio=min(ratio,frac); entry_count+=1
                if frac<rowratio: rowratio=frac; witnesses=[]
                if frac==rowratio: witnesses.append({'class':j+1,'order':t['orders'][j],'nu':nu,'multiplicities':ms})
            records.append({'row':i+1,'degree':a,'minimum_ratio':str(rowratio),'witnesses':witnesses})
        total_rows+=len(rows); total_entries+=entry_count
        out.append({'name':name,'selected_rows':len(rows),'nonscalar_entries':entry_count,
                    'minimum_degree':min_degree,'minimum_ratio':str(ratio),'records':records})
    assert (total_rows,total_entries)==(228,31428)
    assert [(t['selected_rows'],t['nonscalar_entries'],t['minimum_degree'],t['minimum_ratio']) for t in out]==[(140,19460,13,'2/7'),(88,11968,78,'8/21')]
    return {'status':'PASS','input_sha256':digest(p),'arithmetic_helper_sha256':digest(H),
            'selected_rows':total_rows,'nonscalar_entries':total_entries,'tables':out}

def main():
    start=time.monotonic(); g=generic(); s=spectra()
    out={'status':'PASS','method':'independent flint rational-polynomial parser and auditor cyclotomic Fourier',
         'proof_sha256':digest(A/'csp6_section.tex'),'generic':g,'spectra':s,
         'seconds':round(time.monotonic()-start,6)}
    (B/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({**out,'spectra':{k:v for k,v in s.items() if k!='tables'}},indent=2))

if __name__=='__main__': main()
