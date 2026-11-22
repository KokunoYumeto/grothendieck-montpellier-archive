#!/usr/bin/env python3
"""Rebuild the W(E8) character table from the author's CHEVIE v=1 data.

No rStation character packet, class product, weight or volume is imported.
The central-product extension to <W(E8),i> is handled in the proof and
in the volume program; only rational W-character transforms are needed.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd
import hashlib,json,sys
import sympy as S
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT.parent/'runtime_e8_flint'))
from flint import fmpz_mat

def gap_list(txt,token):
    p=txt.index('[',txt.index(token))
    def read():
        nonlocal p
        while txt[p].isspace():p+=1
        if txt[p]!='[':
            if txt.startswith('false',p):p+=5;return False
            if txt.startswith('true',p):p+=4;return True
            q=p
            if txt[p]=='-':p+=1
            while txt[p].isdigit():p+=1
            if p==q:raise ValueError(txt[p:p+100])
            return int(txt[q:p])
        p+=1;out=[];expect=True
        while True:
            while txt[p].isspace():p+=1
            if txt[p]==']':p+=1;return out
            if txt[p]==',':
                if expect:out.append(None)
                p+=1;expect=True;continue
            assert expect
            out.append(read());expect=False
    return read()

source=ROOT/'research/sources/chevie/weyle8.g';txt=source.read_text()
data=json.loads((ROOT/'research/e8_class_exploration.json').read_text())
p=gap_list(txt,'CHEVIE.AddData("vpolheckeirreducibles"')
assert len(p)<=112
p += [None]*(112-len(p))
chars=[]
for j,row in enumerate(p):
    if row is None:
        assert p[j-1]is not None
        vals=[v*(-1)**len(c['word'])for v,c in zip(chars[-1],data['classes'])]
    else:
        assert len(row)==112
        vals=[sum(x[0])for x in row]
    chars.append(vals)
sizes=[c['class_size']for c in data['classes']]
degrees=[r[0]for r in chars];G=696729600
assert sum(sizes)==sum(d*d for d in degrees)==G
C=fmpz_mat(chars);weighted=fmpz_mat([[chars[r][c]*sizes[c]for c in range(112)]for r in range(112)])
assert weighted*C.transpose()==fmpz_mat([[G*int(i==j)for j in range(112)]for i in range(112)])
central=[r[1]//d for r,d in zip(chars,degrees)]
assert all(r[1]in[d,-d]for r,d in zip(chars,degrees))
columns={tuple(chars[r][c]for r in range(112)):c for c in range(112)}
assert len(columns)==112
neg=[columns[tuple(central[r]*chars[r][c]for r in range(112))]for c in range(112)]
assert all(neg[neg[c]]==c for c in range(112))
taut=[j for j,r in enumerate(chars)if all(r[c]==sum(item['matrix'][a][a]for a in range(8))for c,item in enumerate(data['classes']))]
assert len(taut)==1 and degrees[taut[0]]==8
x=S.Symbol('x');classes=[];weights=[[],[]]
for c,item in enumerate(data['classes']):
    exps=[]
    poly=S.Matrix(item['matrix']).charpoly(x).as_expr()
    for f,mult in S.factor_list(poly,x)[1]:
        ns=[n for n in range(1,61)if S.Poly(f,x)==S.Poly(S.cyclotomic_poly(n,x),x)]
        assert len(ns)==1;n=ns[0]
        for k in range(n):
            if gcd(k,n)==1:exps += [Q(k,n)]*mult
    assert len(exps)==8
    for e in [0,1]:
        roots=[(a+Q(e,4))%1 for a in exps]
        weight=sum((a*(1-a)/2 for a in roots),Q(0));weights[e].append(str(weight))
    classes.append({'index':c+1,'name':item['name'],'size':sizes[c],
                    'real_order':item['order'],'real_word':item['word'],
                    'negative_class_index':neg[c]+1,'real_eigenvalue_exponents':[str(a)for a in sorted(exps)]})
assert weights[0][65]=='1/8' and weights[1][5]=='1/2' and weights[1][56]=='17/24'
assert all(weights[1][c]==weights[1][neg[c]]for c in range(112))
out={'status':'PASS','source_url':'https://raw.githubusercontent.com/jmichel7/gap3-jm/master/pkg/chevie/tbl/weyle8.g',
     'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'source_scope':'Published author CHEVIE table specialized at q=v=1; rational W(E8) character table, no unrefereed packet',
     'real_group_order':G,'full_group_order':2*G,'real_class_count':112,'full_class_count':224,
     'characters':chars,'degrees':degrees,'central_negative_identity_signs':central,
     'tautological_character_index':taut[0]+1,'classes':classes,
     'weights_by_scalar_exponent':weights,
     'branch_classes':{'root':{'scalar_exponent':1,'W_class_index':57},
                       'special_leaf':{'scalar_exponent':1,'W_class_index':6},
                       'reflection_leaf':{'scalar_exponent':0,'W_class_index':66},'reflection_count':10},
     'checks':{'full_character_orthogonality':True,'degree_square_sum':True,'class_size_sum':True,
               'central_translation_permutation':True,'tautological_character_vs_every_matrix_trace':True,
               'all_weights_from_exact_matrix_spectra':True}}
(HERE/'character_input.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['status','real_class_count','full_class_count','tautological_character_index','checks']}))
