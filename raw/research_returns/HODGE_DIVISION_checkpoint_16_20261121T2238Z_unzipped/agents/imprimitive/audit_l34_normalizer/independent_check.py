#!/usr/bin/env python3
"""Independent abstract-dihedral reconstruction of the BMO multiplier count.
No author program, selected kernel, or character-table input is imported.
"""
import itertools,json,hashlib
from pathlib import Path
M=tuple(itertools.product(range(4),range(4),range(3)))
A=tuple(itertools.product(range(6),range(2)))
one=(0,0)
def mul(g,h):return ((g[0]+(-1)**g[1]*h[0])%6,(g[1]+h[1])%2)
def inv(g):return ((-(-1)**g[1]*g[0])%6,g[1])
def matmul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))%4 for j in range(2)) for i in range(2))
I=((1,0),(0,1));R=((0,1),(3,1));S=((1,3),(0,3))
def matpow(a,n):
    o=I
    for _ in range(n):o=matmul(o,a)
    return o
def matrix(g):return matmul(matpow(R,g[0]),matpow(S,g[1]))
def action(g,x):
    m=matrix(g);a,b,c=x
    return ((m[0][0]*a+m[0][1]*b)%4,(m[1][0]*a+m[1][1]*b)%4,((-1)**g[1]*c)%3)
assert len({(matrix(g),g[1]) for g in A})==12
assert all(matrix(mul(g,h))==matmul(matrix(g),matrix(h)) for g in A for h in A)
assert all(action(mul(g,h),x)==action(g,action(h,x)) for g in A for h in A for x in M)
Kset={frozenset(x for x in M if (3*a*x[0]+3*b*x[1]+4*c*x[2])%12==0) for a,b,c in M}
assert len(Kset)==20
def actK(g,K):return frozenset(action(g,x) for x in K)
def cyclic(g):
    out={one};h=g
    while h!=one:out.add(h);h=mul(g,h)
    return frozenset(out)
Cset={cyclic(g) for g in A}
def conjugate(g,H):return frozenset(mul(mul(g,h),inv(g)) for h in H)
remaining=set(Kset);korbits=[]
while remaining:
    K=min(remaining,key=lambda k:(len(k),sorted(k)))
    O={actK(g,K) for g in A};remaining-=O
    stab={g for g in A if actK(g,K)==K}
    korbits.append([48//len(K),len(O),len(stab)])
assert sorted(korbits)==[[1,1,12],[2,3,4],[3,1,12],[4,3,4],[4,3,4],[6,3,4],[12,3,4],[12,3,4]]
pairs={(K,H) for K in Kset for H in Cset if all(actK(g,K)==K for g in H)}
orbits=[]
while pairs:
    K,H=min(pairs,key=lambda x:(len(x[0]),sorted(x[0]),len(x[1]),sorted(x[1])))
    O={(actK(g,K),conjugate(g,H)) for g in A};assert O<=pairs;pairs-=O
    orbits.append([48//len(K),len(H),len(O)])
assert len(orbits)==36
profile={}
for k,h,_ in orbits:profile[f'{k}:{h}']=profile.get(f'{k}:{h}',0)+1
assert profile=={'1:1':1,'1:2':3,'1:3':1,'1:6':1,'2:1':1,'2:2':3,'3:1':1,'3:2':3,'3:3':1,'3:6':1,'4:1':2,'4:2':6,'6:1':1,'6:2':3,'12:1':2,'12:2':6}
Ka=frozenset((x,0,z) for x in range(4) for z in range(3))
Kab2=frozenset((x,2*x%4,z) for x in range(4) for z in range(3))
def trivial_mod(g,K):
    return all(tuple((y-x)%m for x,y,m in zip(v,action(g,v),(4,4,3))) in K for v in M)
assert not trivial_mod((0,1),Ka) and trivial_mod((0,1),Kab2)
out={'status':'PASS','method':'abstract D12 multiplication and explicit 2x2 matrices over Z4; no author code imported',
     'kernels':20,'kernel_orbits':sorted(korbits),'simultaneous_orbits':36,'profile':profile,
     'label_discrepancy_independently_confirmed':True,
     'scope':'Structural kernel/outer count only; no character-spectrum rerun'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
