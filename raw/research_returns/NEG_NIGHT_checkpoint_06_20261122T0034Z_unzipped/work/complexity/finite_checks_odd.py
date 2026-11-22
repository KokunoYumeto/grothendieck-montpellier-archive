#!/usr/bin/env python3
"""Finite checks for NN-C017. Does not implement E's counting algorithm."""
import itertools, json, math, pathlib, random
import sympy as sp

Y = sp.Symbol('Y')
coefficients = {}
def coeffs(ell):
    if ell not in coefficients:
        cur = sp.Poly((1-Y)**ell * sum(sp.binomial(ell+j-1,j)*Y**j for j in range(ell)),Y)
        ans = []
        while cur:
            cur, rem = sp.div(cur, sp.Poly(Y*Y-Y,Y))
            ans.append((int(rem.nth(0)),int(rem.nth(1))))
        ans += [(0,0)]*(ell-len(ans))
        assert len(ans)==ell
        coefficients[ell] = ans
    return coefficients[ell]

def residue_from_lifts(values,p,ell):
    out=[1]+[0]*(ell-1)
    for value in values:
        y=value**(p-1)
        h=y*(y-1)
        e=coeffs(ell)
        factor=[(a+b*y)*h**j for j,(a,b) in enumerate(e)]
        out=[sum(out[t]*factor[j-t] for t in range(j+1)) for j in range(ell)]
    return sum(out)%(p**ell)

results=[]
cases=0
for p in (2,3,5,7):
    for ell in range(1,6):
        for m in range(5):
            for values in itertools.product(range(-2,3),repeat=m):
                got=residue_from_lifts(values,p,ell)
                want=int(all(v%p==0 for v in values))
                assert got==want,(p,ell,values,got,want)
                cases+=1
results.append(dict(finding_id='NN-C017',check='Prime-adic amplifier and shared total-order truncation, including negative integer lifts',cases=cases,result='pass'))

rng=random.Random(20261121)
cases=0
for p in (3,5):
    t=(p-1).bit_length()
    for n in range(1,4):
        monos=[()] + [(i,) for i in range(n)] + [(i,j) for i in range(n) for j in range(i,n)]
        for trial in range(8):
            equations=[]
            for _ in range(n+1):
                equations.append([(rng.randrange(-p+1,p),rng.choice(monos)) for __ in range(3)])
            def evaluate(equation,values):
                return sum(c*math.prod(values[i] for i in mono) for c,mono in equation)
            direct=sum(all(evaluate(eq,values)%p==0 for eq in equations) for values in itertools.product(range(p),repeat=n))
            total=0
            N=t*n
            for bits in itertools.product((0,1),repeat=N):
                values=[sum(bits[t*i+j]*(1<<j) for j in range(t)) for i in range(n)]
                lifts=[evaluate(eq,values) for eq in equations]
                lifts += [int(value>=p) for value in values]
                total += residue_from_lifts(lifts,p,N+1)
            assert total==direct,(p,n,equations,total,direct)
            cases+=1
results.append(dict(finding_id='NN-C017',check='Prime-field sparse quadratic counts equal valid-bit encodings and exact amplified indicators',cases=cases,result='pass'))

out=pathlib.Path(__file__).with_name('FINITE_CHECK_ODD_RESULTS.json')
out.write_text(json.dumps({'purpose':'Finite checks only, not the asymptotic proof or E implementation','results':results,'total_cases':sum(x['cases'] for x in results)},indent=2)+'\n')
print(json.dumps({'result':'pass','total_cases':sum(x['cases'] for x in results),'output':str(out)}))
