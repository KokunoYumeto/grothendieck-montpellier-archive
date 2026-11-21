"""Exact finite corroboration of MT-ART05/06, not a formal proof assistant."""
from itertools import permutations, product
from collections import Counter
import json
from sympy import Matrix

def mul(a,b): return tuple(a[b[i]] for i in range(5))
def inv(a): return tuple(a.index(i) for i in range(5))
def even(a): return sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))%2==0
identity=tuple(range(5))
G=[a for a in permutations(range(5)) if even(a)]
def cycle(*letters):
    a=list(identity)
    for i,j in zip(letters,letters[1:]+letters[:1]): a[i]=j
    return tuple(a)
def closure(*generators):
    H={identity}; todo=[identity]
    while todo:
        x=todo.pop()
        for g in generators:
            y=mul(x,g)
            if y not in H:H.add(y);todo.append(y)
    return sorted(H)
def order(g):
    x=g;n=1
    while x!=identity:x=mul(x,g);n+=1
    return n
def theta(g):return {1:3,2:-1,3:0,5:3}[order(g)]
def chi4(g):return sum(g[i]==i for i in range(5))-1
subgroups={
 'A4':closure(cycle(0,1,2),cycle(0,1,3)),
 'D5':closure(cycle(0,1,2,3,4),mul(cycle(1,4),cycle(2,3))),
 'S3':closure(cycle(0,1,2),mul(cycle(0,1),cycle(3,4))),
}
spectra={}
for name,H in subgroups.items():
    M=Matrix([[theta(mul(g,inv(h))) for h in H] for g in H])
    vals=M.eigenvals()
    assert all(v.is_nonnegative for v in vals)
    spectra[name]={'order':len(H),'exact_eigenvalue_multiplicities':{str(k):int(v) for k,v in vals.items()}}
v=[chi4(g) for g in G]
quad=sum(v[i]*theta(mul(g,inv(h)))*v[j]
         for i,g in enumerate(G) for j,h in enumerate(G))
assert quad==-900
assert sum(theta(g)*chi4(g) for g in G)==-60
A=[(1,0,0,0,0),(0,0,0,0,1),(1,0,0,1,0),(0,1,1,0,0),
   (0,1,0,1,1),(0,0,1,1,1),(0,1,1,1,0)]
d=(1,3,3,4,5)
small={}
for r in range(5):
    bad=[]
    for coeff in product(range(-r,r+1),repeat=5):
        if sum(x*x for x in coeff)>r*r or sum(x*y for x,y in zip(d,coeff))!=r:continue
        if all(sum(x*y for x,y in zip(row,coeff))>=0 for row in A) and min(coeff)<0:bad.append(coeff)
    small[str(r)]=bad
assert small['0']==small['1']==small['2']==[]
assert small['3']==[(1,1,1,-1,0)]
print(json.dumps({'statements':['MT-ART05','MT-ART06'],'group_order':len(G),
 'degree3_counterexample_class_values_by_order':{'1':3,'2':-1,'3':0,'5':3},
 'proper_maximal_subgroup_spectra':spectra,'chi4_inner_product':-1,
 'negative_global_quadratic_form':quad,'small_degree_virtual_obstructions':small,
 'scope':'Exact rational/integer computations. General cone and pole bounds have symbolic proofs. No claim of an actual Artin divisor-order realization.'},indent=2))
