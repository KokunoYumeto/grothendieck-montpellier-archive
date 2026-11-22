#!/usr/bin/env python3
"""NN-C020 examples: denominators, nonfield quotients and huge formal degree."""
import itertools,json,pathlib

def add(a,b,M): return tuple((x+y)%M for x,y in zip(a,b))
def neg(a,M): return tuple(-x%M for x in a)
def scale(a,c,M): return tuple(c*x%M for x in a)
def mul(a,b,M):
    # Q(sqrt(3)); monic defining polynomial T^2-3.
    return ((a[0]*b[0]+3*a[1]*b[1])%M,(a[0]*b[1]+a[1]*b[0])%M)

cases=0
for n in range(1,9):
    w=n+1;D=15;M=D*(1<<(w+1))+1
    inv3=(-(D//3)*(1<<(w+1)))%M
    inv5=(-(D//5)*(1<<(w+1)))%M
    assert 3*inv3%M==1 and 5*inv5%M==1
    a=(inv3,inv3)    # (1+sqrt(3))/3
    b=(-inv5%M,inv5) # (-1+sqrt(3))/5
    factor=add(scale(mul(a,b,M),15,M),(-1%M,0),M)
    assert factor==(1,0) # 15ab-1=1
    huge=(1,1)
    for _ in range(200): huge=mul(huge,huge,M)
    vanishing=add(huge,neg(huge,M),M)
    for bits in itertools.product((0,1),repeat=n):
        g=(1,0)
        for bit in bits: g=scale(g,1+bit,M)
        out=add(mul(g,factor,M),vanishing,M)
        assert out==(1<<sum(bits),0)
        cases+=1

# A composite, nonreduced quotient: M=9, T^2=3, with no chosen root.
M=9
assert mul((0,1),(0,1),M)==(3,0)
assert mul((3,0),(3,0),M)==(0,0)
assert (3,0)!=(0,0)
cases+=1
out=pathlib.Path(__file__).with_name('FINITE_CHECK_MODULAR_RESULTS.json')
out.write_text(json.dumps({'finding_id':'NN-C020','cases':cases,'result':'pass','formal_degree_test':'200 repeated squarings create formal degree at least2^200; only quotient coordinates evaluated','quotient_test':'Z/9[T]/(T^2-3), including nonzero nilpotent scalar3','limitation':'Finite examples supplement the homomorphism proof; no claim to verify arbitrary algebra presentations'},indent=2)+'\n')
print({'cases':cases,'result':'pass'})
