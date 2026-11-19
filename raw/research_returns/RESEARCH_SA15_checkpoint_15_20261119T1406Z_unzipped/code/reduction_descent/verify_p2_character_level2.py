#!/usr/bin/env python3
"""Exact certificate for E[4] = mu_4 + Z/4 over Q_2(zeta_3).

All arithmetic is in Q(a,i), a^2=-3, i^2=-1. No p-adic approximation
is used. The ramification and reduction implications are proved in TeX.
"""
from fractions import Fraction as F
import json
import time

start = time.perf_counter()

class K:
    def __init__(self, a=0, b=0):
        if isinstance(a, K):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = F(a), F(b)
    def __add__(self, v):
        v=K(v); return K(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,v): return self+-K(v)
    def __rsub__(self,v): return K(v)+-self
    def __mul__(self,v):
        v=K(v); return K(self.a*v.a-3*self.b*v.b,self.a*v.b+self.b*v.a)
    __rmul__=__mul__
    def inv(self):
        n=self.a*self.a+3*self.b*self.b
        if n==0: raise ZeroDivisionError
        return K(self.a/n,-self.b/n)
    def __truediv__(self,v): return self*K(v).inv()
    def __eq__(self,v):
        v=K(v); return self.a==v.a and self.b==v.b
    def __hash__(self): return hash((self.a,self.b))
    def __repr__(self): return f'({self.a})+({self.b})*a'

class L:
    def __init__(self,c=0,d=0):
        if isinstance(c,L): self.c,self.d=c.c,c.d
        else: self.c,self.d=K(c),K(d)
    def __add__(self,v):
        v=L(v); return L(self.c+v.c,self.d+v.d)
    __radd__=__add__
    def __neg__(self): return L(-self.c,-self.d)
    def __sub__(self,v): return self+-L(v)
    def __rsub__(self,v): return L(v)+-self
    def __mul__(self,v):
        v=L(v); return L(self.c*v.c-self.d*v.d,self.c*v.d+self.d*v.c)
    __rmul__=__mul__
    def inv(self):
        n=self.c*self.c+self.d*self.d
        if n==0: raise ZeroDivisionError
        return L(self.c/n,-self.d/n)
    def __truediv__(self,v): return self*L(v).inv()
    def __pow__(self,n):
        if n<0: return self.inv()**(-n)
        r=L(1); a=self
        while n:
            if n&1: r=r*a
            a=a*a; n//=2
        return r
    def __eq__(self,v):
        v=L(v); return self.c==v.c and self.d==v.d
    def __hash__(self): return hash((self.c,self.d))
    def conjugate_i(self): return L(self.c,-self.d)
    def __repr__(self): return f'[{self.c}]+[{self.d}]*i'

O=None
a=L(K(0,1)); i=L(0,1)
assert a*a==-3 and i*i==-1

def add(P,Q):
    if P is O: return Q
    if Q is O: return P
    x,y=P; u,v=Q
    if x==u and y+v==0: return O
    slope=(v-y)/(u-x) if x!=u else (3*x*x+4*x-3)/(2*y)
    w=slope*slope-2-x-u
    return w,-y+slope*(x-w)

def mul(n,P):
    R=O
    while n:
        if n&1: R=add(R,P)
        P=add(P,P); n//=2
    return R

def neg(P): return O if P is O else (P[0],-P[1])
def sigma(P): return O if P is O else tuple(c.conjugate_i() for c in P)

P=(a,i*a*(a-1)); Q=(L(3),L(6))
assert add(P,P)==(L(0),L(0))
assert add(Q,Q)==(L(1),L(0))
assert sigma(P)==neg(P) and sigma(Q)==Q
points={add(mul(r,P),mul(s,Q)) for r in range(4) for s in range(4)}
assert len(points)==16
for R in points:
    if R is not O:
        x,y=R
        assert y*y==x*(x-1)*(x+3)
    assert mul(4,R)==O
assert all(add(R,S) in points for R in points for S in points)
assert all(sigma(add(R,S))==add(sigma(R),sigma(S)) for R in points for S in points)

b2,b4,b6,b8=8,-6,0,-9
c4=b2*b2-24*b4
Delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
j=F(c4**3,Delta)
assert c4==16*13 and Delta==2**8*3**2 and j==F(16*13**3,9)

out={
  'input':{'p':2,'K':'Q_2(zeta_3)','e':1,'residue_field':'F_4',
           'curve':'y^2=x*(x-1)*(x+3)','a':'1+2*zeta_3; a^2=-3','i':'sqrt(-1)'},
  'basis':{'P':'(a, i*a*(a-1))','Q':'(3,6)'},
  'doubling':{'2P':'(0,0)','2Q':'(1,0)'},
  'basis_generates':len(points),'all_points_on_curve':True,
  'all_points_killed_by_4':True,'all_256_additions_checked':True,
  'conjugation':{'i':'-i','a':'a','P':'-P','Q':'Q'},
  'all_256_galois_compatibilities_checked':True,
  'Galois_module':'E[4] = mu_4 direct_sum Z/4',
  'invariants':{'c4':c4,'discriminant':Delta,'j':str(j),
                'v2_discriminant':8,'v2_c4':4,'v2_j':4},
  'proof_implications':'Delta valuation 8 is minimal (<12); j integral gives potential good. Every good extension has 12|8m, hence 3|m. A special order-3 automorphism has trace -1, whereas the split good BT group has trace 2.',
  'scope':'Exact characteristic-zero finite group arithmetic and invariant identities; the local ramification and Dieudonne arguments are proved separately in B_p2_character_gate.tex.',
  'elapsed_seconds':time.perf_counter()-start
}
print(json.dumps(out,indent=2))
