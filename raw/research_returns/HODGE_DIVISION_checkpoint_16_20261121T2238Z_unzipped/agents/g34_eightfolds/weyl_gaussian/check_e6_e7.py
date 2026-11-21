#!/usr/bin/env python3
"""Exact Gaussian local invariants for all published CHEVIE E6/E7 class words.

Completeness is the published Carter classification plus the author's CHEVIE
class-word data, not an independently enumerated 2.9-million-element group.
The retained input JSON contains just mathematical witness words and Cartan
matrices, with source hashes. All matrices/local determinants are recomputed.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import ast,hashlib,json,sys
import sympy as S

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'g31'))
import gaussian_exact as M
from check_local_discriminants import cyclotomic,divide,trim,inert_parities

def bracket_after(txt,token):
    start=txt.index('[',txt.index(token));depth=0;quoted=False;escape=False
    for j in range(start,len(txt)):
        c=txt[j]
        if quoted:
            if escape:escape=False
            elif c=='\\':escape=True
            elif c=='"':quoted=False
            continue
        if c=='"':quoted=True
        elif c=='[':depth+=1
        elif c==']':
            depth-=1
            if not depth:return ast.literal_eval(txt[start:j+1])
    raise ValueError(token)

def prepare(n):
    dest=HERE/f'E{n}_witness_input.json'
    if dest.exists():return json.loads(dest.read_text())
    source=HERE.parents[2]/'research/sources/chevie'/f'weyle{n}.g'
    txt=source.read_text()
    token='classtext:=' if n==6 else 'CHEVIE.AddData("WordsClassRepresentatives"'
    words=bracket_after(txt,token)
    if n==7:words=[[j for k in w for j in ([7,6,5,4,3,2,1] if k==0 else [k])]for w in words]
    out={'source_url':f'https://raw.githubusercontent.com/jmichel7/gap3-jm/master/pkg/chevie/tbl/weyle{n}.g',
         'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'source_scope':'Carter complete class labels and CHEVIE author class words; all following arithmetic recomputed',
         'rank':n,'cartan':bracket_after(txt,'CHEVIE.AddData("CartanMat"'),
         'words':words,'names':bracket_after(txt,'CHEVIE.AddData("ClassNames"'),
         'orders':bracket_after(txt,'orders:='),'sizes':bracket_after(txt,'classes:=')}
    dest.write_text(json.dumps(out,indent=2)+'\n');return out

def spectrum(g,order):
    n=len(g);N=lcm(order,4);phi=list(cyclotomic(N));powers=[];a=M.eye(n)
    for j in range(order):
        powers.append(sum((a[i][i] for i in range(n)),M.Z));a=M.mul(a,g)
    assert a==M.eye(n)
    counts=[]
    for k in range(order):
        p=[Q(0)]*N
        for j,z in enumerate(powers):
            e=(-k*j*(N//order))%N;p[e]+=z.a/order;p[(e+N//4)%N]+=z.b/order
        _,r=divide(trim(p),phi)
        assert len(r)==1 and r[0].denominator==1 and r[0]>=0
        counts.append(int(r[0]))
    assert sum(counts)==n
    return counts

def local(g,H,order):
    n=len(g);I=M.eye(n);a=M.sub(I,g);cols=M.rref(a)[1];k=len(cols)
    if k:
        U=M.tr([M.tr(a)[j]for j in cols]);rows=M.rref(M.tr(U))[1]
        action=M.mul(M.inv([U[j]for j in rows]),[M.mul(g,U)[j]for j in rows])
        assert M.mul(U,action)==M.mul(g,U)
        gram=M.mul(M.star(U),M.mul(H,U));gd=M.det(gram)
        b=M.det(M.sub(M.eye(k),action))
    else:U=[[]for _ in range(n)];gram=[];gd=b=M.ONE
    assert not gd.b and gd.a>0
    # A Gaussian determinant may have phase an odd multiple of pi/4.
    # Remove its possible sqrt(2) absolute factor. In any product-one tuple
    # the number of these factors is even; their remaining power of 2 is a norm.
    assert not b.a or not b.b or abs(b.a)==abs(b.b)
    half_phase=bool(b.a and b.b)
    q=gd.a/(abs(b.a)if b.a else abs(b.b));bad=inert_parities(q)
    counts=spectrum(g,order)
    assert n-counts[0]==k
    age=sum((Q(j*c,order)for j,c in enumerate(counts)),Q(0))
    return {'moving_rank':k,'moving_basis':M.serialize(U),
            'moving_gram':M.serialize(gram),'gramdet':gd.pair(),'b':b.pair(),
            'half_phase':half_phase,'normalized_positive_local_q':str(q),
            'inert_odd_valuations':bad,'is_norm':not bad,
            'eigenvalue_multiplicities':counts,'age':str(age),'age_imbalance':str(age-Q(k,2))}

def run(n):
    raw=prepare(n);H=M.mat(raw['cartan']);I=M.eye(n)
    expected_count,expected_order=(25,51840)if n==6 else(60,2903040)
    assert len(raw['words'])==len(raw['names'])==len(raw['orders'])==len(raw['sizes'])==expected_count
    assert sum(raw['sizes'])==expected_order
    assert M.det(H)==M.F(3 if n==6 else 2)
    gens=[M.sub(I,M.outer([M.F(i==j)for i in range(n)],H[j]))for j in range(n)]
    assert all(M.mul(g,g)==I and M.mul(M.star(g),M.mul(H,g))==H for g in gens)
    rows=[]
    for index,(word,name,order,size)in enumerate(zip(raw['words'],raw['names'],raw['orders'],raw['sizes']),1):
        a=I
        for j in word:a=M.mul(a,gens[j-1])
        assert M.mul(M.star(a),M.mul(H,a))==H
        rational=S.Matrix([[S.Rational(z.a.numerator,z.a.denominator)for z in row]for row in a])
        assert rational**order==S.eye(n)
        assert all(rational**(order//p)!=S.eye(n)for p in S.factorint(order))
        row={'index':index,'name':name,'word':word,'real_order':order,'class_size':size,
             'real_matrix':[[str(z.a)for z in r]for r in a],
             'characteristic_polynomial':str(rational.charpoly().as_expr()),'scalars':{}}
        for exponent,scalar in enumerate([M.ONE,M.w,-M.ONE,-M.w]):
            g=M.scale(a,scalar)
            data=local(g,H,lcm(order,4));data['scalar_exponent']=exponent
            row['scalars'][str(exponent)]=data
        rows.append(row)
    outside=[(r['index'],r['name'],e,d)for r in rows for e,d in r['scalars'].items()if int(e)%2]
    minimum=min(d['moving_rank']for _,_,_,d in outside)
    minimal=[(i,name,e,d)for i,name,e,d in outside if d['moving_rank']==minimum]
    reflections=[(r,e,d)for r in rows for e,d in r['scalars'].items()if d['moving_rank']==1]
    assert all(int(e)%2==0 and d['is_norm']for r,e,d in reflections)
    out={'status':'PASS','all_arithmetic_exact':True,'published_class_completeness_used':True,
         'rank':n,'real_group_order':expected_order,'class_count':expected_count,
         'cartan':raw['cartan'],'source_url':raw['source_url'],'source_sha256':raw['source_sha256'],
         'minimum_outside_moving_rank':minimum,
         'all_reflection_local_invariants_are_norms':True,
         'minimal_outside_classes':[{'index':i,'name':name,'scalar_exponent':int(e),
              'q':d['normalized_positive_local_q'],'is_norm':d['is_norm'],'imbalance':d['age_imbalance']}for i,name,e,d in minimal],
         'classes':rows}
    (HERE/f'E{n}_local_invariants.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k]for k in ['status','rank','class_count','minimum_outside_moving_rank','minimal_outside_classes']}))
    return out

if __name__=='__main__':run(6);run(7)
