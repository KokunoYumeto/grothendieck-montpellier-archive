#!/usr/bin/env python3
"""Independent finite arithmetic audit of HD-E8-01.

Uses Sympy's QQ(i) domain matrices, rather than the author's Gaussian helper.
Reconstructs words, obtains b(g) by deflating characteristic polynomials,
and obtains the moving Gram determinant directly from independent columns.
Published representative-list completeness remains an external input.
"""
from pathlib import Path
from fractions import Fraction
import json,math
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy import QQ_I

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
data=json.loads((ROOT/'research/e8_class_exploration.json').read_text())
reported=json.loads((ROOT/'research/e8_gaussian_local.json').read_text())
H=2*S.eye(8)
for a,b in [(1,3),(3,4),(2,4),(4,5),(5,6),(6,7),(7,8)]:H[a-1,b-1]=H[b-1,a-1]=-1
assert H.det()==1
Id=S.eye(8);gens=[Id-Id[:,j]*H[j,:]for j in range(8)];x=S.Symbol('x')
def domain(A):return DomainMatrix.from_Matrix(A.applyfunc(S.expand)).convert_to(QQ_I)
def exactdet(A):return QQ_I.to_sympy(domain(A).det())
def inert(q):
    a,b=S.fraction(q);p={}
    for v,sgn in [(a,1),(b,-1)]:
        for r,k in S.factorint(v).items():p[int(r)]=p.get(int(r),0)+sgn*k
    return sorted(r for r,k in p.items()if r%4==3 and k%2)
rows=[]
for item in data['classes']:
    w=Id
    for j in item['word']:w=w*gens[j-1]
    assert w.tolist()==item['matrix'] and w.T*H*w==H
    for e in [0,1]:
        g=w if e==0 else S.I*w
        A=Id-g;piv=domain(A).rref()[1];k=len(piv)
        U=A[:,list(piv)]
        gram=U.conjugate().T*H*U
        gd=exactdet(gram)if k else S.Integer(1)
        poly=S.Poly(g.charpoly(x).as_expr(),x,domain=QQ_I)
        for _ in range(8-k):poly,rem=S.div(poly,S.Poly(x-1,x,domain=QQ_I));assert rem.is_zero
        b=S.expand(poly.eval(1));re,im=b.as_real_imag();assert not re or not im
        q=S.cancel(gd/(abs(re)if re else abs(im)));assert q.is_Rational and q>0
        bad=inert(q)
        row={'index':item['index'],'name':item['name'],'scalar_exponent':e,
             'moving_rank':k,'gramdet':str(gd),'b':str(b),'q':str(q),'inert_odd_valuations':bad}
        if e:
            r=reported['classes'][item['index']-1]
            assert k==r['moving_rank'] and str(gd)==r['gramdet'] and str(q)==r['positive_local_q']
            assert bad==r['inert_odd_valuations']
            assert [str(re),str(im)]==r['det_one_minus_moving']
            exps=[]
            for fp,mult in S.factor_list(w.charpoly(x).as_expr(),x)[1]:
                ns=[j for j in range(1,61)if S.Poly(fp,x)==S.Poly(S.cyclotomic_poly(j,x),x)]
                assert len(ns)==1
                n=ns[0]
                for j in range(n):
                    if math.gcd(j,n)==1:exps += [(Fraction(j,n)+Fraction(1,4))%1]*mult
            assert [str(v)for v in sorted(exps)]==r['eigenvalue_exponents']
            assert str(sum(exps,Fraction(0))-Fraction(k,2))==r['age_imbalance']
        else:assert not bad
        rows.append(row)
out={'status':'PASS','independent_method':'Sympy QQ_I domain elimination and determinant; characteristic-polynomial deflation; no author-code import',
     'whole_proof_read':True,'published_class_completeness_used':True,'local_class_checks':len(rows),
     'all_real_classes_norm':True,'all_reported_iW_invariants_match':True,
     'nonnorm_indices':[r['index']for r in rows if r['inert_odd_valuations']],
     'rank4_iW_indices':[r['index']for r in rows if r['scalar_exponent']==1 and r['moving_rank']==4],
     'classes':rows}
(HERE/'audit_e8_local.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='classes'}))
