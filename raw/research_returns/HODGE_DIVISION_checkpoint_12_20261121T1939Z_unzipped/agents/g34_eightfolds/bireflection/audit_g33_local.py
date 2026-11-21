"""Independent G33 local audit in Q[t]/(t^4-t^2+1), t=zeta12."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
import json,hashlib
HERE=Path(__file__).resolve().parent
SRC=HERE.parents[1]/'imprimitive'/'g33'
Z=(Q(0),)*4
O=(Q(1),Q(0),Q(0),Q(0))
T=(Q(0),Q(1),Q(0),Q(0))
I=(Q(0),Q(0),Q(0),Q(1))
def scalar(n):return (Q(n),Q(0),Q(0),Q(0))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    v=[Q(0)]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]+=x*y
    for k in range(6,3,-1):v[k-2]+=v[k];v[k-4]-=v[k]
    return tuple(v[:4])
def nonzero(a):return a!=Z
@lru_cache(None)
def inv(a):
    assert nonzero(a)
    cols=[mul(a,tuple(Q(i==j) for i in range(4))) for j in range(4)]
    m=[[cols[j][i] for j in range(4)]+[Q(i==0)] for i in range(4)]
    for j in range(4):
        k=next(k for k in range(j,4) if m[k][j]);m[j],m[k]=m[k],m[j]
        z=m[j][j];m[j]=[x/z for x in m[j]]
        for k in range(4):
            if k!=j:
                z=m[k][j];m[k]=[x-z*y for x,y in zip(m[k],m[j])]
    out=tuple(m[i][-1] for i in range(4))
    assert mul(a,out)==O
    return out
TC=sub(T,I)
conjp=[O,TC,mul(TC,TC),mul(mul(TC,TC),TC)]
def conj(a):
    out=Z
    for x,b in zip(a,conjp):out=add(out,mul(scalar(x),b))
    return out
def fpair(a):return (Q(a[0])-Q(a[1]),Q(0),Q(a[1]),Q(0))
def fsource(a):
    a,b,c,d=map(Q,a)
    return (a-b,-d,b,c)
def eye(n):return [[O if i==j else Z for j in range(n)] for i in range(n)]
def mm(a,b):
    return [[sumf(mul(x,y) for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def sumf(a):
    v=Z
    for x in a:v=add(v,x)
    return v
def star(a):return [[conj(x) for x in col] for col in zip(*a)]
def det(a):
    a=[row[:] for row in a];v=O
    for j in range(len(a)):
        k=next((k for k in range(j,len(a)) if nonzero(a[k][j])),None)
        if k is None:return Z
        if k!=j:a[j],a[k]=a[k],a[j];v=neg(v)
        pivot=a[j][j];v=mul(v,pivot);ip=inv(pivot)
        for k in range(j+1,len(a)):
            z=mul(a[k][j],ip)
            for l in range(j+1,len(a)):a[k][l]=sub(a[k][l],mul(z,a[j][l]))
    return v
def pivots(a):
    a=[row[:] for row in a];i=0;out=[]
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if nonzero(a[k][j])),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i];ip=inv(a[i][j])
        a[i]=[mul(x,ip) for x in a[i]]
        for k in range(i+1,len(a)):
            z=a[k][j]
            for l in range(j,len(a[k])):a[k][l]=sub(a[k][l],mul(z,a[i][l]))
        out.append(j);i+=1
        if i==len(a):break
    return out
data=json.loads((SRC/'g33_classes.json').read_text())
local=json.loads((SRC/'g33_local_forms.json').read_text())
H=[[fpair(x) for x in row] for row in data['gram']]
assert det(H)==scalar(2)
E=eye(5)
lookup={(r['R_class'],r['scalar']):r for r in local['classes']}
count=0;outside=[]
for c in data['classes']:
    w=[[fpair(x) for x in row] for row in c['matrix']]
    assert mm(mm(star(w),H),w)==H
    for name,phase in [('1',O),('i',I)]:
        g=[[mul(x,phase) for x in row] for row in w]
        A=[[sub(E[i][j],g[i][j]) for j in range(5)] for i in range(5)]
        cols=pivots(A);d=len(cols)
        C=[[row[j] for j in cols] for row in A]
        gd=det(mm(mm(star(C),H),C)) if d else O
        b=sumf(det([[A[i][j] for j in inds] for i in inds])
               for inds in combinations(range(5),d))
        r=lookup[c['class'],name]
        assert d==r['moving_rank']
        assert gd==fsource(r['moving_gram_determinant'])
        assert b==fsource(r['det_one_minus_moving'])
        if name=='i' and d==3:
            outside.append(c['class'])
            z=fsource(r['moving_determinant_over_eight_norm_witness'])
            assert gd==mul(scalar(8),mul(z,conj(z)))
        count+=1
assert count==80 and outside==[27,35]
assert mul(add(O,I),conj(add(O,I)))==scalar(2)
assert 1+103680*Q(9,4)==233281
assert 5*5-5*4-2==3
out={'status':'PASS','field_basis':'1,t,t^2,t^3; t^4=t^2-1; omega=t^2-1; i=t^3',
     'classes_checked':count,'outside_rank_three_classes':outside,
     'method':'Fresh cyclotomic arithmetic, independent column elimination, b from principal-minor sums, direct Gram determinants',
     'source_sha256':hashlib.sha256((SRC/'g33_classes.json').read_bytes()).hexdigest(),
     'scope':'All local matrices checked independently; closure is a separate fresh rerun of reviewed C++ source; component exclusion is the written geometric proof.'}
(HERE/'audit_g33_local.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'classes_checked':count,'outside_rank_three_classes':outside}))
