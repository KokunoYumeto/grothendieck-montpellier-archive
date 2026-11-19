"""Exact finite checks of exterior divided squares on normalized group cocycles.

For G=(Z/2)^2, evaluate gamma_2 on the shuffle cycles representing
H_*(BC2) tensor H_*(BC2). All arithmetic is over F2.
"""
from itertools import combinations,product
from math import factorial
from time import perf_counter
import json
t=perf_counter(); evaluations=0
def value(vertices, inds, a, q):
    selected=[vertices[i] for i in (0,)+inds]
    steps=[selected[i]^selected[i-1] for i in range(1,len(selected))]
    ans=1
    for j,g in enumerate(steps): ans &= ((g & 1) if j<a else ((g>>1)&1))
    return ans
def divided_square(word,a,q):
    global evaluations
    v=[0]
    for x in word:v.append(v[-1]^x)
    n=2*q; out=0
    for rest in combinations(range(2,n+1),q-1):
        I=(1,)+rest;J=tuple(i for i in range(1,n+1) if i not in I)
        out ^= value(v,I,a,q)&value(v,J,a,q)
        evaluations+=1
    return out
rows=[]
for q in [2,4,6]:
    n=2*q
    for a in range(q+1):
        poly=[]
        for r in range(n+1):
            coeff=0
            for xs in combinations(range(n),r):
                xs=set(xs);word=tuple(1 if j in xs else 2 for j in range(n))
                coeff ^= divided_square(word,a,q)
            if coeff:poly.append([r,n-r])
        expected=[[2*a,2*(q-a)]] if (factorial(2*q)//(2*factorial(q)**2))%2 else []
        rows.append({'q':q,'input_monomial':[a,q-a],'gamma2_terms':poly,'cup_formula_terms':expected,'equal':poly==expected})
        print(json.dumps(rows[-1]),flush=True)
print(json.dumps({'cases':len(rows),'partition_evaluations':evaluations,'seconds':round(perf_counter()-t,4),'all_equal':all(r['equal'] for r in rows)}))
