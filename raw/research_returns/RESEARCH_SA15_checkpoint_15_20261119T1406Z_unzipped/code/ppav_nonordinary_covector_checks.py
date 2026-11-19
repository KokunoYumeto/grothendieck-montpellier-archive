"""Exact local Cartier identities for all surface restricted-Lie types.

The polynomial identities support, but do not replace, the global proof.
All variables are algebraically independent over F2; negative x/y exponents
allow invariant multiplicative differentials. No sampled point is used.
"""
from pathlib import Path
import itertools, json, time
import sympy as sp

started=time.perf_counter()
x,y,a,b,c,e=sp.symbols('x y a b c e'); variables=(x,y,a,b,c,e)
s=a*a+x*b*b+y*c*c+x*y*e*e

def mod2(f):
    answer=0
    for term in sp.expand(f).as_ordered_terms():
        coefficient,rest=term.as_coeff_Mul()
        assert coefficient.q==1
        if int(coefficient)%2: answer+=rest
    return sp.expand(answer)

def cartier_dxdy(f):
    answer=0
    for term in sp.expand(mod2(f)).as_ordered_terms():
        coefficient,rest=term.as_coeff_Mul()
        if not int(coefficient)%2: continue
        powers=rest.as_powers_dict()
        exponents=[int(powers.get(t,0)) for t in variables]
        if exponents[0]%2!=1 or exponents[1]%2!=1: continue
        assert all(q%2==0 for q in exponents[2:])
        output=[(exponents[0]-1)//2,(exponents[1]-1)//2]+[q//2 for q in exponents[2:]]
        answer+=sp.prod(t**q for t,q in zip(variables,output))
    return mod2(answer)

types={
 'ordinary':(lambda f:x*sp.diff(f,x),lambda f:y*sp.diff(f,y),1/(x*y),[0,1,2,3]),
 'mixed':(lambda f:x*sp.diff(f,x),lambda f:sp.diff(f,y),1/x,[None,None,2,3]),
 'superspecial':(lambda f:sp.diff(f,x),lambda f:sp.diff(f,y),sp.Integer(1),[None,None,None,3]),
 'nilpotent_chain':(lambda f:sp.diff(f,x)+x*sp.diff(f,y),lambda f:sp.diff(f,y),sp.Integer(1),[None,2,None,3]),
}
identities=[]
for name,(d1,d2,omega,expected) in types.items():
    operators=[lambda f:f,d1,d2,lambda f:d1(d2(f))]
    images=[mod2(op(s)) for op in operators]
    result=[mod2(cartier_dxdy(s*t*omega)/omega) for t in images]
    targets=[sp.Integer(0) if i is None else images[i] for i in expected]
    assert all(mod2(v-t)==0 for v,t in zip(result,targets)),(name,result,targets)
    assert mod2(d1(d2(s))-d2(d1(s)))==0
    if name=='ordinary': relations=[images[1],images[2]]
    elif name=='mixed': relations=[images[1],0]
    elif name=='superspecial': relations=[0,0]
    else: relations=[images[2],0]
    assert mod2(d1(d1(s))-relations[0])==0
    assert mod2(d2(d2(s))-relations[1])==0
    identities.append(dict(type=name,operator_order=['identity','delta1','delta2','delta1_delta2'],
                           cartier_images=[str(v) for v in result],
                           image_indices=expected,all_identities_passed=True))

def compositions(total,n):
    if n==1:
        yield (total,); return
    for first in range(total+1):
        for tail in compositions(total-first,n-1): yield (first,)+tail

monomial_checks=[]
for dimension in (2,3,4):
    for exponent in (1,2,3,4):
        q=2**exponent
        monomials=list(compositions(q,dimension))
        nonpure=[alpha for alpha in monomials if max(alpha)<q]
        seen={}
        for alpha in nonpure:
            level=min((v&-v).bit_length()-1 for v in alpha if v)
            assert level<exponent
            for i in range(dimension):
                beta=tuple(v+(q if j==i else 0) for j,v in enumerate(alpha))
                assert beta not in seen,(alpha,i,seen.get(beta))
                seen[beta]=(alpha,i)
                assert any(v%(2**(level+1)) for v in beta)
        monomial_checks.append(dict(variables=dimension,q=q,nonpure_monomials=len(nonpure),
                                    unique_product_monomials=len(seen)))

result=dict(all_assertions_passed=True,
            scope='Universal local Laurent-polynomial identities for four Lie types; finite illustrations of the separately proved exponent-elimination argument.',
            local_identities=identities,monomial_elimination_checks=monomial_checks,
            runtime_seconds=time.perf_counter()-started)
destination=Path(__file__).resolve().parents[1]/'outputs/root_ppav_nonordinary_covector_checks.json'
destination.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
