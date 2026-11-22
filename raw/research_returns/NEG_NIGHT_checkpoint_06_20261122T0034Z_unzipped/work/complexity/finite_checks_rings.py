#!/usr/bin/env python3
"""Finite exact tests of NN-C018's digit and finite-ring reductions."""
import itertools, json, math, pathlib, random
from fractions import Fraction

rng=random.Random(20261121)
def mul(a,b):
    out={}
    for s,c in a.items():
        for t,d in b.items(): out[s|t]=out.get(s|t,0)+c*d
    return {s:c for s,c in out.items() if c}
def evaluate(poly,x): return sum(c for s,c in poly.items() if s&x==s)
def generalized_binom(n,k):
    return math.prod(n-j for j in range(k))//math.factorial(k)
def digit_polynomial(poly,d):
    out={0:Fraction(1,math.factorial(d))}
    for h in range(d):
        factor=dict(poly);factor[0]=factor.get(0,0)-h
        out=mul(out,factor)
    assert all(c.denominator==1 for c in out.values())
    return {s:int(c) for s,c in out.items()}

results=[];cases=0
for n in range(1,6):
    monos=[s for s in range(1<<n) if s.bit_count()<=2]
    for p,a in ((2,1),(2,2),(2,3),(3,1),(3,2),(5,1)):
        for _ in range(12):
            poly={s:rng.randrange(-5,6) for s in rng.sample(monos,min(4,len(monos)))}
            digits=[digit_polynomial(poly,p**j) for j in range(a)]
            for x in range(1<<n):
                v=evaluate(poly,x)
                for j,digit in enumerate(digits):
                    got=evaluate(digit,x)%p
                    assert got==generalized_binom(v,p**j)%p
                    assert got==(v%(p**a)//(p**j))%p
                assert all(evaluate(d,x)%p==0 for d in digits)==(v%(p**a)==0)
                cases+=1
results.append(dict(finding_id='NN-C018',check='Integer-valued binomial digit polynomials become integral after sparse Boolean multilinear reduction; negative values included',cases=cases,result='pass'))

def multiply_coords(x,y,dual):
    if dual: return (x[0]*y[0],x[0]*y[1]+x[1]*y[0])
    return (x[0]*y[0],)
def equation_value(eq,variables,dual):
    dim=2 if dual else 1
    out=[0]*dim
    for coefficient,indices in eq:
        term=coefficient
        for i in indices: term=multiply_coords(term,variables[i],dual)
        for j in range(dim): out[j]+=term[j]
    return tuple(out)
def count_mod(equations,n,mod,dual):
    dim=2 if dual else 1
    elements=list(itertools.product(range(mod),repeat=dim))
    return sum(all(all(v%mod==0 for v in equation_value(eq,x,dual)) for eq in equations) for x in itertools.product(elements,repeat=n))

cases=0
for mod,p,a,dual in ((4,2,2,False),(8,2,3,False),(9,3,2,False),(2,2,1,True),(4,2,2,True)):
    dim=2 if dual else 1;t=(mod-1).bit_length()
    for n in (1,2):
        monos=[()]+[(i,) for i in range(n)]+[(i,j) for i in range(n) for j in range(i,n)]
        for _ in range(10):
            equations=[[(tuple(rng.randrange(mod) for j in range(dim)),rng.choice(monos)) for __ in range(3)] for _ in range(n)]
            direct=count_mod(equations,n,mod,dual)
            encoded=0
            for codes in itertools.product(range(1<<t),repeat=dim*n):
                if any(c>=mod for c in codes): continue
                variables=[tuple(codes[dim*i+j] for j in range(dim)) for i in range(n)]
                vals=[v for eq in equations for v in equation_value(eq,variables,dual)]
                if all(generalized_binom(v,p**j)%p==0 for v in vals for j in range(a)):
                    encoded+=1
            assert direct==encoded,(mod,dual,n,direct,encoded)
            cases+=1
results.append(dict(finding_id='NN-C018',check='Prime-power residue rings and dual-number rings preserve exact counts under coordinate/digit encoding',cases=cases,result='pass'))

cases=0
for mod,powers in ((6,(2,3)),(12,(4,3)),(18,(2,9))):
    for n in (1,2):
        monos=[()]+[(i,) for i in range(n)]+[(i,j) for i in range(n) for j in range(i,n)]
        for _ in range(12):
            equations=[[((rng.randrange(mod),),rng.choice(monos)) for __ in range(3)] for _ in range(n)]
            direct=count_mod(equations,n,mod,False)
            split=math.prod(count_mod(equations,n,q,False) for q in powers)
            assert direct==split,(mod,n,direct,split)
            cases+=1
results.append(dict(finding_id='NN-C018',check='Mixed-prime unweighted solution counts multiply under the primary ring decomposition',cases=cases,result='pass'))

out=pathlib.Path(__file__).with_name('FINITE_CHECK_RING_RESULTS.json')
out.write_text(json.dumps({'purpose':'Finite checks only; not execution of E or an asymptotic proof','results':results,'total_cases':sum(x['cases'] for x in results)},indent=2)+'\n')
print(json.dumps({'result':'pass','total_cases':sum(x['cases'] for x in results),'output':str(out)}))
