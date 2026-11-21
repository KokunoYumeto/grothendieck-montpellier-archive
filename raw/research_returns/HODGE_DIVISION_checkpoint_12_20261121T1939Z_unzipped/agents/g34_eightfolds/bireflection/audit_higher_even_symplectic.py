#!/usr/bin/env python3
"""Independent finite/arithmetic audit of the conditional HES argument.

Uses only the frozen original data and this reviewer's polynomial reducer.
It does not verify the still-open GM1998 primary-source premise.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import hashlib,json,time
import sympy as sp
from audit_sporadic_input import reduce_poly

B=Path(__file__).resolve().parent
SOURCE=B.parents[1]/'imprimitive/lie_small_fields/sp2n2_character_inputs_v1.json'


@lru_cache(None)
def reality(n,c):
    v=[0]*n
    for j,x in enumerate(c):
        v[j%n]+=x
        v[-j%n]-=x
    return reduce_poly(v,n)==(0,)


def main():
    start=time.perf_counter()
    raw=SOURCE.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='9117f0b99643c2a44ea135db3435d29b8fa54a643a9aaa9d49071de31a1a45e8'
    data=json.loads(raw)
    ts={t['name']:t for t in data['tables']}
    assert set(ts)=={'S8(2)','S10(2)'}
    result={'status':'PASS conditional arithmetic audit','input_sha256':hashlib.sha256(raw).hexdigest(),
            'tables':[],'all_rows':0,'nonidentity_entries':0,
            'source_boundary':'GM1998 proper-parabolic estimate not verified by this computation.'}
    for name,n,count,minimum,c in [('S8(2)',4,81,35,F(3,5)),('S10(2)',5,198,155,F(17,31))]:
        t=ts[name];cs=t['characters']
        assert 'origin: ATLAS of finite groups' in t['information']
        assert t['extension_info']==['','']
        assert len(cs)==len(t['sizes'])==len(t['orders'])==count
        order=2**(n*n)
        for i in range(1,n+1):order*=2**(2*i)-1
        assert t['order']==sum(t['sizes'])==order==sum(row[0]**2 for row in cs)
        assert min(row[0] for row in cs if row[0]>1)==minimum
        assert len([row for row in cs if row[0]==1])==1
        max_bound=F(0);attained=[];checked=0
        for i,row in enumerate(cs):
            assert len(row)==count
            a=row[0]
            for j,z in enumerate(row):
                if isinstance(z,int):bound=abs(z)
                else:
                    N,coeffs=z
                    assert reality(N,tuple(coeffs))
                    bound=sum(abs(v) for v in coeffs)
                if a==1 or j==0:continue
                ratio=F(bound,a)
                assert ratio<=c
                checked+=1
                if ratio>max_bound:max_bound=ratio;attained=[]
                if ratio==max_bound and isinstance(z,int):
                    attained.append({'row':i+1,'class':j+1,'degree':a,'value':z})
        assert max_bound==c and attained
        result['all_rows']+=count
        result['nonidentity_entries']+=checked
        result['tables'].append({'name':name,'rows':count,'minimum':minimum,
                                 'maximum_certified_ratio':str(max_bound),'attainment':attained,
                                 'checked_nonidentity_entries':checked})
    assert result['all_rows']==279 and result['nonidentity_entries']==45209

    # All-rank inequalities are proved symbolically, with only the true initial
    # cases checked numerically; no claim from a finite sample is made.
    x=sp.Symbol('x')
    assert sp.expand((2*x-1)**2-3*(x-1)**2)==x*x+2*x-2
    assert 64**2+2*64-2>0
    assert all(36*3**n<25*155**2 for n in [5,6])
    assert 36*3**7<25*63**2
    assert F(5,6)+F(1,18)==F(8,9)
    assert (1-F(3,4))/2==F(1,8)
    assert (1-F(3,5))/2==F(1,5)
    assert F(6)/(1+10*F(1,9)-2)==54<155
    assert F(6)/(1+10*F(1,5)-2)==6<35
    result['symbolic_checks']=['elliptic-ratio induction','prime-order8/9','involution7/8',
                               'endpoint4/5','Hurwitz degree54 and6']
    result['elapsed_seconds']=round(time.perf_counter()-start,6)
    B.joinpath('audit_higher_even_symplectic.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
