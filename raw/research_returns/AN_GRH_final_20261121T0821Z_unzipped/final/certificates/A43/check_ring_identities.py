#!/usr/bin/env python3
"""Exact integer-coefficient checks in Z[T,u]/(T^2+T-1,u^2+u+1).

This checks algebraic identities only. It is not a formal verification of
A43's geometry. Inverses of pi are handled by clearing powers of pi, never
by cancelling multiplication by two on geometric points.
"""
import json
from pathlib import Path
from dataclasses import dataclass
BASIS=((0,0),(1,0),(0,1),(1,1))
TP=({0:1},{1:1},{0:1,1:-1})
UP=({0:1},{1:1},{0:-1,1:-1})
@dataclass(frozen=True)
class R:
    c: tuple
    def __add__(self,b):
        if isinstance(b,int): b=R((b,0,0,0))
        return R(tuple(x+y for x,y in zip(self.c,b.c)))
    __radd__=__add__
    def __neg__(self): return R(tuple(-x for x in self.c))
    def __sub__(self,b): return self+-b
    def __rsub__(self,b): return -self+b
    def __mul__(self,b):
        if isinstance(b,int): return R(tuple(b*x for x in self.c))
        z={ij:0 for ij in BASIS}
        for (i,j),a in zip(BASIS,self.c):
            for (k,l),v in zip(BASIS,b.c):
                for m,r in TP[i+k].items():
                    for n,s in UP[j+l].items(): z[m,n]+=a*v*r*s
        return R(tuple(z[ij] for ij in BASIS))
    __rmul__=__mul__
    def __pow__(self,n):
        z=ONE
        for _ in range(n): z=z*self
        return z
ZERO=R((0,0,0,0));ONE=R((1,0,0,0));T=R((0,1,0,0));u=R((0,0,1,0))
pi=T-u;V=T+1+u
@dataclass(frozen=True)
class L:
    a: R
    e: int=0
    def __add__(self,b):
        n=max(self.e,b.e)
        return L(self.a*pi**(n-self.e)+b.a*pi**(n-b.e),n)
    def __neg__(self): return L(-self.a,self.e)
    def __sub__(self,b): return self+-b
    def mul(self,b): return L(self.a*b,self.e)
checks={}
def ck(name,a):
    if isinstance(a,R): a=L(a)
    checks[name]={'cleared_pi_power':a.e,'integer_coefficients':list(a.a.c)}
    assert a.a==ZERO,(name,a)
ck('pi_times_V_is_two',pi*V-2)
ck('u_dagger_times_u_is_one',(-1-u)*u-1)
ck('T_minus_Vu',T-V*u+u**2*pi**2)
ck('T_plus_Vu',T+V*u+T*pi)
ck('T_pi_plus_one',T*pi*(pi+1)+2*u)
ck('one_plus_two_u_squared', (1+2*u)**2+3)
def F(a,b,t): return (a-t).mul(T)-b
for label,t,a,b,c in [
    ('first',L(-pi),L(ONE),L(-u,1),L(u**2,1)),
    ('second',L(ONE),L(-pi),L(u,1),L(u**2,1))]:
    ck(label+'_F_a_b_equals_b',F(a,b,t)-b)
    ck(label+'_F_c_b_equals_c',F(c,b,t)-c)
    ck(label+'_F_b_c_equals_a',F(b,c,t)-a)
a,b,c=L(-pi),L(u,1),L(u**2,1)
ck('second_pi_a_minus_b', (a-b).mul(pi)-L(T*(1+2*u)))
ck('second_pi_a_minus_c', (a-c).mul(pi)-L((T+1)*(1+2*u)))
ck('second_pi_b_minus_c', (b-c).mul(pi)-L(1+2*u))
assert (4*4159)%3!=0
out={'status':'PASS','scope':'Exact ring arithmetic only; geometry is separately proof-read.','basis':['1','T','u','T*u'],'relations':['T^2+T-1','u^2+u+1'],'identities':checks,'identity_count':len(checks),'rational_J_order':4*4159,'rational_J_order_mod3':(4*4159)%3}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'identity_count':len(checks),'output':str(path)},indent=2))
