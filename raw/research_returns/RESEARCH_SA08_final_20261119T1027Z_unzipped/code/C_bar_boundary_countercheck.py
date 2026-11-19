"""Finite normalized certificate for C31, using surjection value strings.

This independently constructs the relevant exterior and tensor squares of
K(Z,2). Quotient-normalized basis vectors are those pairs for which there
is no common repeated step. All face operations are literal vertex deletion.
"""
from itertools import product, combinations
from pathlib import Path
from math import gcd
from functools import reduce
import time
import json
import sympy as sp

start=time.monotonic()
ROOT=Path(__file__).resolve().parents[1]

def cuts(v):
    return [i for i in range(1,len(v)) if v[i]!=v[i-1]]

def labels(n):
    return sorted([v for v in product(range(3),repeat=n+1)
            if set(v)=={0,1,2} and all(a<=b for a,b in zip(v,v[1:]))],key=cuts)

def normalized_pair(a,b):
    return not any(a[i]==a[i+1] and b[i]==b[i+1] for i in range(len(a)-1))

def basis(n,kind):
    out=[]
    for a in labels(n):
        for b in labels(n):
            if kind=='exterior' and cuts(a)>=cuts(b): continue
            if normalized_pair(a,b):out.append((a,b))
    return out

def matrix(n,kind):
    src=basis(n,kind);dst=basis(n-1,kind);index={v:i for i,v in enumerate(dst)}
    out=sp.zeros(len(dst),len(src))
    for col,(a,b) in enumerate(src):
        for i in range(n+1):
            aa=a[:i]+a[i+1:];bb=b[:i]+b[i+1:]
            if set(aa)!={0,1,2} or set(bb)!={0,1,2}:continue
            c=(-1)**i
            if kind=='exterior':
                if aa==bb:continue
                if cuts(aa)>cuts(bb):aa,bb=bb,aa;c=-c
            if normalized_pair(aa,bb):out[index[(aa,bb)],col]+=c
    return out

def minor_gcd(m,r):
    vals=[abs(int(m.extract(rows,cols).det()))
          for rows in combinations(range(m.rows),r)
          for cols in combinations(range(m.cols),r)]
    return reduce(gcd,vals,0)

records={}
for kind in ['exterior','tensor']:
    mats={n:matrix(n,kind) for n in range(2,6)}
    for n in range(3,6):assert mats[n-1]*mats[n]==sp.zeros(mats[n-1].rows,mats[n].cols)
    assert not basis(5,kind)
    records[kind]={str(n):{'basis':[[cuts(a),cuts(b)] for a,b in basis(n,kind)],
                         'boundary':[[int(v) for v in row] for row in mats[n].tolist()], 'rank':int(mats[n].rank())}
                   for n in range(2,5)}
    if kind=='exterior':
        m=mats[4]
        assert m.shape==(3,3) and abs(int(m.det()))==2
        assert minor_gcd(m,1)==minor_gcd(m,2)==1
        assert mats[3].rows==0
        records[kind]['certificate']={'smith_invariants':[1,1,2],
                                     'H3':'Z/2','H4':0,'determinant':int(m.det())}
    else:
        d3,d4=mats[3],mats[4]
        assert d3.shape==(1,6) and d4.shape==(6,6)
        assert minor_gcd(d3,1)==1 and d4.rank()==5 and minor_gcd(d4,5)==1
        records[kind]['certificate']={'d3_surjective':True,'d4_rank':5,
                                     'd4_image_primitive':True,'H3':0,'H4':'Z'}
# Alternation is a chain map, independently on these finite normalizations.
for n in range(2,5):
    eb=basis(n,'exterior');tb=basis(n,'tensor');ti={v:i for i,v in enumerate(tb)}
    alt=sp.zeros(len(tb),len(eb))
    for j,(a,b) in enumerate(eb):alt[ti[(a,b)],j]=1;alt[ti[(b,a)],j]=-1
    if n>2:
        assert matrix(n,'tensor')*alt==prev*matrix(n,'exterior')
    prev=alt
report={'statement':'C31','method':'literal monotone surjection strings; quotient normalization; integral determinantal divisors',
        'all_checks_passed':True,'seconds':time.monotonic()-start,'records':records}
(ROOT/'logs/C_bar_boundary_countercheck.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'seconds':report['seconds'],
                  'exterior_d4':records['exterior']['4']['boundary'],
                  'exterior_H3':'Z/2','tensor_H3':0},indent=2))
