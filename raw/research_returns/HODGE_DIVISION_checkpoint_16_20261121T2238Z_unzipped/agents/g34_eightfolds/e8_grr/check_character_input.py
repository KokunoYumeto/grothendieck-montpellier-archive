#!/usr/bin/env python3
"""Recheck the retained mathematical character input without external source files.

Completeness and character status are published CHEVIE inputs. The independent
checks here establish orthogonality, all class-word matrices/orders/spectra,
the tautological character, and central translation. They do not claim that
orthogonality alone proves an arbitrary integer array is a character table.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd
import json,sys,time
import sympy as S
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT.parent/'runtime_e8_flint'))
from flint import fmpz_mat
d=json.loads((HERE/'character_input.json').read_text());start=time.monotonic()
H=2*S.eye(8)
for i,j in [(1,3),(3,4),(2,4),(4,5),(5,6),(6,7),(7,8)]:H[i-1,j-1]=H[j-1,i-1]=-1
assert H.det()==1
I=S.eye(8);gens=[I-I[:,j]*H[j,:]for j in range(8)]
C=d['characters'];degrees=d['degrees'];classes=d['classes'];sizes=[r['size']for r in classes]
GW=d['real_group_order'];n=len(C)
assert n==112 and all(len(r)==n for r in C)
assert sum(sizes)==sum(x*x for x in degrees)==GW==696729600
assert [r[0]for r in C]==degrees
weighted=fmpz_mat([[C[r][c]*sizes[c]for c in range(n)]for r in range(n)])
assert weighted*fmpz_mat(C).transpose()==fmpz_mat([[GW*int(i==j)for j in range(n)]for i in range(n)])
taut=d['tautological_character_index']-1
x=S.Symbol('x');weights=[[],[]]
for c,cl in enumerate(classes):
    w=I
    for j in cl['real_word']:w=w*gens[j-1]
    o=cl['real_order'];assert w.T*H*w==H and w**o==I
    assert all(w**(o//p)!=I for p in S.factorint(o))
    assert C[taut][c]==S.trace(w)
    exps=[]
    for f,mult in S.factor_list(w.charpoly(x).as_expr(),x)[1]:
        ns=[m for m in range(1,61)if S.Poly(f,x)==S.Poly(S.cyclotomic_poly(m,x),x)]
        assert len(ns)==1;m=ns[0]
        for j in range(m):
            if gcd(j,m)==1:exps += [Q(j,m)]*mult
    assert sorted(exps)==sorted(Q(v)for v in cl['real_eigenvalue_exponents'])
    for phase in [0,1]:
        shifted=[(a+Q(phase,4))%1 for a in exps]
        a=sum((v*(1-v)/2 for v in shifted),Q(0))
        weights[phase].append(str(a))
        assert str(a)==d['weights_by_scalar_exponent'][phase][c]
    neg=cl['negative_class_index']-1
    assert classes[neg]['negative_class_index']==c+1
    for r in range(n):
        assert C[r][1]in[degrees[r],-degrees[r]]
        assert C[r][neg]*degrees[r]==C[r][c]*C[r][1]
    assert weights[0][c]==d['weights_by_scalar_exponent'][0][c]
assert all(Q(d['weights_by_scalar_exponent'][1][c])==Q(d['weights_by_scalar_exponent'][1][cl['negative_class_index']-1])for c,cl in enumerate(classes))
out={'status':'PASS','class_words_reconstructed':112,'character_orthogonality':True,
     'matrix_orders_and_orthogonality':True,'all_weights_from_exact_spectra':True,
     'tautological_character_checked_on_all_classes':True,'central_translation_checked':True,
     'external_input_scope':'Published CHEVIE complete character table and class list; not an independent proof of character-table completeness',
     'elapsed_seconds':time.monotonic()-start}
(HERE/'check_character_input.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
