#!/usr/bin/env python3
"""Exact identities for the residual-trivial dyadic exclusion."""
from pathlib import Path
from time import perf_counter
from itertools import product
import json
import sympy as sp

started=perf_counter()
a,b,i,l=sp.symbols('a b i l')
gb=sp.groebner([a*a-l,b*b+l-1,i*i+1],a,b,i,l)
checks=[]
def check(name,expr):
    numerator=sp.together(expr).as_numer_denom()[0]
    assert gb.reduce(sp.expand(numerator))[1]==0, name
    checks.append(name)
def add(P,Q):
    x,y=P;u,v=Q
    slope=(3*x*x-2*(1+l)*x+l)/(2*y) if P==Q else (v-y)/(u-x)
    X=slope*slope+(1+l)-x-u
    Y=-y+slope*(x-X)
    return X,Y
P=(a,i*a*(a-1));Q=(1+b,b*(1+b))
for name,(x,y) in [('P',P),('Q',Q)]:
    check(name+'_on_curve',y*y-x*(x-1)*(x-l))
for name,point,target in [('doubleP',add(P,P),(0,0)),('doubleQ',add(Q,Q),(1,0)),
                          ('a_sign',add(P,(1,0)),(-a,i*a*(a+1))),
                          ('b_sign',add(Q,(0,0)),(1-b,-b*(1-b)))]:
    check(name+'_x',point[0]-target[0]);check(name+'_y',point[1]-target[1])

I=sp.eye(2);N=sp.Matrix([[0,0],[1,0]])
def mod(M):return M.applyfunc(lambda x:int(x)%2)
gl=[]
for entries in product(range(2),repeat=4):
    C=sp.Matrix(2,2,entries)
    if int(C.det())%2:gl.append(C)
assert len(gl)==6
central=[];projective=[]
for C in gl:
    image=mod(C*N*C.inv())
    if image==N:central.append(C)
    if image in [N,mod(N+I)]:projective.append(C)
assert central==projective and len(central)==2
assert {tuple(C) for C in central}=={tuple(I),tuple(I+N)}
entry_cases=0
for C in central:
    for entries in product(range(2),repeat=4):
        A=sp.Matrix(2,2,entries)
        assert mod(C*A*C.inv())[0,1]==A[0,1]
        entry_cases+=1
excluded=[]
for qprime in [0,2]:
    for epsilon,epsilonprime in product(range(2),repeat=2):
        A=mod(N+epsilon*I);B=mod((qprime%2)*N+epsilonprime*I)
        assert all(mod(C*A*C.inv())!=B for C in gl)
        excluded.append([qprime,epsilon,epsilonprime])
rows=[{'q':q,'discriminant_mod3':(4+2*q)%3,
       'j_valuation':('at_least8' if q==0 else 8-2*q),
       'cubic_special_inertia':q!=1} for q in range(4)]
out={'status':'PASS','scope':'Exact halving, translation, conjugation and valuation identities only; no residual C2 or C3 comparison decided',
     'polynomial_identities':checks,'GL2_F2_matrices':len(gl),
     'projective_nilpotent_centralizer':[list(C) for C in central],
     'upper_right_entry_cases':entry_cases,'scalar_nonscalar_exclusions':excluded,
     'valuation_table':rows,'elapsed_seconds':perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps(out,indent=2,default=int))
