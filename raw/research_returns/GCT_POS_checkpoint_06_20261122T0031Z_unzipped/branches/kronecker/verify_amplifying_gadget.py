"""Integer/Fraction certificate replay for K-018, independent of all searches.

The all-dimensional induction is in AMPLIFYING_GADGET.tex.  This file
checks its finite gadget, the explicit n=9 witness, and three recursive
instances including exact determinants. No LP or floating point is used.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from math import gcd,lcm
import json

root=Path(__file__).resolve().parent
g=json.loads((root/'amplifying_gadget_q8.json').read_text())
E=list(map(tuple,g['support']));p=g['intercept_numerators'];u=g['slope_numerators']
boundary=tuple(g['boundary']);D=256

def det_bareiss(a):
    a=[row[:] for row in a];n=len(a);previous=1;sign=1
    for k in range(n-1):
        pivot=next((j for j in range(k,n)if a[j][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        value=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                top=a[i][j]*value-a[i][k]*a[k][j]
                assert top%previous==0
                a[i][j]=top//previous
            a[i][k]=0
        previous=value
    return sign*a[-1][-1]

def incidence(n,support):
    return [[int(edge[a]==i)for edge in support]for a in range(3)for i in range(n)]

def free(support):
    return all(len(set((e[i],e[j])for e in support))==len(support)for i,j in [(0,1),(0,2),(1,2)])

A=incidence(8,E)
assert len(E)==22 and free(E)
for a in range(3):
    for i in range(8):
        assert sum(p[j]for j,e in enumerate(E)if e[a]==i)==(0 if i==boundary[a]else 256)
        assert sum(u[j]for j,e in enumerate(E)if e[a]==i)==(256 if i==boundary[a]else 0)
assert det_bareiss([row for i,row in enumerate(A)if i not in g['minor_omitted_rows']])==256
assert all(11*x+3*y>=0 and 61*x+37*y>=0 and not(11*x+3*y==61*x+37*y==0)for x,y in zip(p,u))
assert E[2]==(0,5,6) and p[2]==131 and u[2]==-43
lo=F(3,11);hi=F(37,61)
assert lo<F(25,61)<F(41,88)<hi and lo<F(1,2)<hi
assert (131-43*lo)/256==F(41,88) and (131-43*hi)/256==F(25,61)

support=[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
masses=[F(1,2)]*4;n=2;selected=(0,0,0);receipts=[]
for k in range(4):
    period=2*256**k
    assert n==2+7*k and len(support)==3*n-2 and free(support)
    assert all(x>0 for x in masses)
    assert all(sum(x for edge,x in zip(support,masses)if edge[a]==i)==1 for a in range(3)for i in range(n))
    denominator=lcm(*(x.denominator for x in masses))
    assert denominator==period
    selected_mass=masses[support.index(selected)]
    assert selected_mass.denominator==period and selected_mass.numerator%2
    assert lo<selected_mass<hi
    matrix=incidence(n,support)
    rows=[row for i,row in enumerate(matrix)if i not in(2*n-1,3*n-1)]
    determinant=det_bareiss(rows)
    assert abs(determinant)==period
    receipt={'k':k,'n':n,'period':period,'support_size':len(support),
             'selected_mass':str(selected_mass),'minor_determinant':determinant}
    receipts.append(receipt)
    if k==1:
        witness=json.loads((root/'n9_period512_counterexample.json').read_text())
        assert support==list(map(tuple,witness['support']))
        assert masses==[F(x,512)for x in witness['mass_numerators']]
        W=witness['W']
        assert sum(map(sum,W))%512==219 and gcd(219,512)==1
        assert all(len(set(v))==9 for v in W)
        full=[edge for edge in product(range(9),repeat=3)if sum(W[a][edge[a]]for a in range(3))%512==0]
        assert set(full)==set(support)
        receipt['full_fixed_support_size']=len(full)
        receipt['character_exponent']=219
    if k==3:break
    index=support.index(selected);r=masses[index]
    support.pop(index);masses.pop(index)
    maps=[]
    for a in range(3):
        others=[i for i in range(8)if i!=boundary[a]]
        maps.append({boundary[a]:selected[a],**{v:n+j for j,v in enumerate(others)}})
    added=[tuple(maps[a][edge[a]]for a in range(3))for edge in E]
    support.extend(added);masses.extend(F(x+y*r,256)for x,y in zip(p,u))
    selected=added[2];n+=7
(root/'amplifying_gadget_checks.json').write_text(json.dumps({
    'scope':'Exact finite data and recursive instances for the separate all-n proof K-018',
    'gadget_integer_identities':'PASS','positivity_interval':'PASS',
    'recurrence_interval':'PASS','receipts':receipts},indent=2))
print('PASS K-018: exact gadget determinant256, margins, positivity, invariant interval; n2/9/16/23 determinants and masses; explicit n9 fullfixedsupport and primitiveχ512')
