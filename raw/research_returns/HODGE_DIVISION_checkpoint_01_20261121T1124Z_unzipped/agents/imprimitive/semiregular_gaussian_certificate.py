#!/usr/bin/env python3
"""Exact exterior-algebra verification of D-SR-03.

No analytic approximation, symbolic simplifier, or imported exterior-algebra
implementation is used. Coefficients are Q[u]/(u^2+d). One symplectic-plane
Fourier transform is reconstructed from the original exponential and integrated
over its two fibre generators. Three copies are then multiplied, the B field is
removed, and the complete output is compared with the claimed Weil+polynomial
formula. Cases d=4m for the nine class-number-one radicands are arithmetic checks
of a formula proved symbolically in the text; they do not enumerate the very
large cyclic subgroup used in D-SR-01.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json


class K:
    d = 4
    def __init__(self, a=0, b=0):
        if isinstance(a, K):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = F(a), F(b)
    def __add__(self, other):
        o = K(other); return K(self.a+o.a, self.b+o.b)
    __radd__ = __add__
    def __neg__(self): return K(-self.a, -self.b)
    def __sub__(self, other): return self+-K(other)
    def __rsub__(self, other): return K(other)+-self
    def __mul__(self, other):
        o = K(other)
        return K(self.a*o.a-self.d*self.b*o.b,
                 self.a*o.b+self.b*o.a)
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = K(other); den = o.a*o.a+self.d*o.b*o.b
        return self*K(o.a/den, -o.b/den)
    def __eq__(self, other):
        o = K(other); return self.a == o.a and self.b == o.b
    def __bool__(self): return bool(self.a or self.b)
    def conj(self): return K(self.a, -self.b)
    def serial(self): return [str(self.a), str(self.b)]


def clean(x): return {m:c for m,c in x.items() if c}
def add(x,y):
    z=dict(x)
    for m,c in y.items(): z[m]=z.get(m,K())+c
    return clean(z)
def scale(x,c): return clean({m:v*c for m,v in x.items()})
def wedge(x,y):
    z={}
    for a,ca in x.items():
        for b,cb in y.items():
            if a&b: continue
            inversions=sum((b&((1<<i)-1)).bit_count()
                           for i in range(a.bit_length()) if (a>>i)&1)
            c=ca*cb*(-1 if inversions&1 else 1)
            z[a|b]=z.get(a|b,K())+c
    return clean(z)
def power(x,n):
    z={0:K(1)}
    for _ in range(n): z=wedge(z,x)
    return z
def exp2(x,dimension):
    z={0:K(1)}; term={0:K(1)}
    for j in range(1,dimension+1):
        term=scale(wedge(term,x),F(1,j)); z=add(z,term)
    return z
def generator(i): return {1<<i:K(1)}
def pair(i,j): return wedge(generator(i),generator(j))
def equal(x,y): return not add(x,scale(y,-1))


def one_plane(s,t):
    # Order a,b,c,d,U,V, with c,d the integrated fibre variables.
    a,b,c,d,U,V=[generator(i) for i in range(6)]
    form=add(scale(wedge(add(a,c),add(b,d)),s),scale(wedge(c,d),-t))
    form=add(form,scale(wedge(c,V),-1))
    form=add(form,wedge(d,U))
    expanded=exp2(form,3)
    out={}; fibre=(1<<2)|(1<<3); keep=[0,1,4,5]
    for mask,coef in expanded.items():
        if mask&fibre != fibre: continue
        # Moving c,d past the surviving generators produces an even sign;
        # explicitly compute it rather than assuming the convention.
        rest=mask^fibre
        sign=sum(1 for i in [2,3] for j in keep if (rest>>j)&1 and i>j)
        target=sum(1<<j for j,i in enumerate(keep) if (rest>>i)&1)
        out[target]=out.get(target,K())+coef*(-1 if sign&1 else 1)
    expected={0:s-t}
    expected=add(expected,scale(pair(0,1),-s*t))
    expected=add(expected,scale(pair(1,2),-s))
    expected=add(expected,scale(pair(2,3),-1))
    expected=add(expected,scale(pair(0,3),s))
    expected=add(expected,{15:-s})
    assert equal(out,expected), "One-plane Fourier formula failed"
    return out


def embed(x,block): return {mask<<(4*block):coef for mask,coef in x.items()}
def three_planes(local):
    z={0:K(1)}
    for b in range(3): z=wedge(z,embed(local,b))
    return z
def qroot(s):
    z={0:K(1)}
    for b in range(3):
        a,beta,U,V=[generator(4*b+j) for j in range(4)]
        z=wedge(z,wedge(add(scale(a,s),scale(U,-1)),
                        add(scale(beta,s),scale(V,-1))))
    return z
def serialize(x):
    return [[m,*x[m].serial()] for m in sorted(x)]


def case(d):
    K.d=d; N=d+1; u=K(0,1)
    s=K(-1,1); sb=s.conj()
    a=(K(1)+K(1)/u)/2; ab=a.conj()
    # Reconstruct v=1-N theta^2/2+N theta^3/3 as a pair of exponentials.
    for degree,desired in [(0,1),(1,0),(2,F(-N,2)),(3,F(N,3))]:
        ps=K(1); pb=K(1)
        for _ in range(degree): ps=ps*s; pb=pb*sb
        assert (a*ps+ab*pb)/factorial(degree)==desired
    transformed={}
    for root1,coeff1 in [(s,a),(sb,ab)]:
        for root2,coeff2 in [(s,a),(sb,ab)]:
            transformed=add(transformed,
                scale(three_planes(one_plane(root1,root2)),coeff1*coeff2/F(N)))
    theta={}; thhat={}; gamma={}
    for b in range(3):
        theta=add(theta,pair(4*b,4*b+1))
        thhat=add(thhat,pair(4*b+2,4*b+3))
        gamma=add(gamma,pair(4*b,4*b+3))
        gamma=add(gamma,scale(pair(4*b+1,4*b+2),-1))
    H=add(add(scale(theta,N),thhat),gamma)
    actual=wedge(exp2(scale(gamma,F(-1,2)),6),transformed)
    weil=scale(add(scale(qroot(s),a*a),scale(qroot(sb),ab*ab)),F(-1,N))
    polynomial=add(add(scale(H,2),scale(power(H,3),F(-1,12*d))),
                   scale(power(H,5),F(1,960*d*d)))
    expected=add(weil,polynomial)
    assert equal(actual,expected), "Full twelve-generator character failed"
    assert all(c.b==0 for c in actual.values()), "Character is not rational"
    assert all(c.b==0 for c in weil.values()), "Weil term is not rational"
    assert weil and all(mask.bit_count()==6 for mask in weil)
    assert 0 not in actual, "Rank is not zero"
    assert equal(wedge(H,weil),{}), "Weil class not H-primitive"
    payload=serialize(actual)
    digest=hashlib.sha256(json.dumps(payload,separators=(',',':')).encode()).hexdigest()
    return {
        'd':d,'N':N,'delta':str(F(1,N)),
        'one_plane_integrals_checked':4,
        'output_dimension':12,
        'rank':0,
        'coefficient_count':len(actual),
        'weil_coefficient_count':len(weil),
        'full_character_equal':True,
        'H_times_weil_zero':True,
        'all_coefficients_rational':True,
        'normalized_character_sha256':digest,
        'normalized_character':payload,
        'weil_character':serialize(weil),
    }


if __name__=='__main__':
    cases=[case(4*m) for m in [1,2,3,7,11,19,43,67,163]]
    output={'method':'exact Q[u]/(u^2+d) sparse exterior arithmetic; original exponential integrated plane by plane',
            'scope':'checks the algebraic formula, not construction/enumeration of J[N]',
            'cases':cases}
    path=Path(__file__).with_name('semiregular_gaussian_certificate.json')
    path.write_text(json.dumps(output,indent=2)+'\n')
    for c in cases:
        print({k:c[k] for k in ['d','N','rank','coefficient_count','weil_coefficient_count','normalized_character_sha256']})
