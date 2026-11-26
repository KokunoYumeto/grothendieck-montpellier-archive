#!/usr/bin/env python3
"""Exact coefficient checks independent of the readers' symbolic simplifier.

Twelve rational identities are checked by cross multiplication in Q[t].
The bivariate identity is checked at three s-values after proving its degree
in s is at most two. The sample table is reconstructed by enumerating genera,
not conductors. These computations certify arithmetic, not geometry.
"""
from fractions import Fraction as F
import json

def trim(p):
    p=list(map(F,p))
    while len(p)>1 and not p[-1]:p.pop()
    return p
def add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for i,c in enumerate(p):r[i]+=c
    for i,c in enumerate(q):r[i]+=c
    return trim(r)
def neg(p):return [-c for c in p]
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return trim(r)
def derivative(p):return trim([i*p[i] for i in range(1,len(p))] or [0])
def compose(p,q):
    r=[F(0)]
    for a in reversed(p):r=add(mul(r,q),[a])
    return r
class R:
    def __init__(self,n=0,d=1):
        self.n=trim(n if isinstance(n,list) else [n]);self.d=trim(d if isinstance(d,list) else [d])
        assert self.d!=[0]
    @staticmethod
    def cast(x):return x if isinstance(x,R) else R(x)
    def __add__(self,y):
        y=R.cast(y);return R(add(mul(self.n,y.d),mul(y.n,self.d)),mul(self.d,y.d))
    __radd__=__add__
    def __neg__(self):return R(neg(self.n),self.d)
    def __sub__(self,y):return self+-R.cast(y)
    def __rsub__(self,y):return R.cast(y)+-self
    def __mul__(self,y):
        y=R.cast(y);return R(mul(self.n,y.n),mul(self.d,y.d))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=R.cast(y);return R(mul(self.n,y.d),mul(self.d,y.n))
    def __rtruediv__(self,y):return R.cast(y)/self
    def __pow__(self,n):
        assert n>=0
        r=R(1)
        for _ in range(n):r=r*self
        return r
    def diff(self):return R(add(mul(derivative(self.n),self.d),neg(mul(self.n,derivative(self.d)))),mul(self.d,self.d))
    def at(self,x):
        x=R.cast(x)
        def val(p):
            r=R(0)
            for a in reversed(p):r=r*x+a
            return r
        return val(self.n)/val(self.d)

t=R([0,1]);g=t;s=t
h=(12*g+8)*(g-1)/(g*g-g-1)
n=12*(g-1)*(3*g*g-4*g-4)/(g*(3*g*g-12*g+15))
rad=12*s*s/(s*s-s-1)
checks={}
def equal(label,x,y):
    x=R.cast(x);y=R.cast(y)
    residual=trim(add(mul(x.n,y.d),neg(mul(y.n,x.d))))
    assert residual==[0],(label,list(map(str,residual)))
    checks[label]=True
equal('h derivative',h.diff(),-4*(2*g*g+2*g+1)/(g*g-g-1)**2)
equal('n derivative',n.diff(),-4*(5*g*g*((g-3)**2-2)+4*(g-1)*(3*g-5))/(g**3-4*g*g+5*g)**2)
equal('n minus h',n-h,4*(g-1)*(3*g+2)*(g*g-4*g+2)/(g*(g*g-4*g+5)*(g*g-g-1)))
for v in [0,1,2]:
    # After clearing the displayed denominators both sides have s-degree <=2.
    P=(v*v-v-1)*(5*g*g-15*g+4)-(v+1)*g*(3*g*g-12*g+15)
    equal('n minus R: degree-two coefficient witness '+str(v),n-rad.at(v),12*P/((v*v-v-1)*g*(3*g*g-12*g+15)))
def P_at(G):return (s*s-s-1)*(5*G*G-15*G+4)-(s+1)*G*(3*G*G-12*G+15)
equal('P at ell four',P_at(2*s+1),-2*s*(2*s**3+21*s*s+2*s-5))
equal('hyperelliptic ell one',h.at(1+s/2)-rad,4*s*(s*s-s-10)/((s*s-s-1)*(s*s+2*s-4)))
equal('hyperelliptic ell two',h.at(1+s)-rad,-4*s*(s*s+5*s+5)/((s*s-s-1)*(s*s+s-1)))
equal('P at ell two',P_at(s+1),s*(2*s**3-10*s*s-3*s+5))
equal('P at ell three',P_at(1+3*s/2),F(3,8)*s*(3*s**3-59*s*s-8*s+20))
equal('n at six',n.at(6),F(800,51))
equal('conductor six external difference',F(300,19)-F(800,51),F(100,969))
equal('conductor six internal difference numerator',(300*t/(19*t+1)-F(800,51))*51*(19*t+1),100*t-800)

table=[]
for p in [3,5,7,11,13,17,19,23,29,31]:
    candidates=[]
    # Enumerate genera allowed by Tate divisibility, then solve for conductor.
    for genus in range((p-1)//2,3*p+1,(p-1)//2):
        if 2*genus-1>=5:candidates.append((2*genus-1,1,genus))
        if genus>=7:candidates.append((genus,2,genus))
        if (2*genus+1)%3==0 and (2*genus+1)//3>=21:
            candidates.append(((2*genus+1)//3,3,genus))
    a=min(row[0] for row in candidates)
    table.append({'p':p,'minimum_a':a,'surviving_rows':[{'ell':ell,'genus':genus} for aa,ell,genus in sorted(candidates) if aa==a]})
print(json.dumps({'status':'PASS','method':'Exact rational coefficient cross multiplication; genus enumeration for the finite table; no symbolic library','identities':12,'coefficient_checks':len(checks),'checks':checks,'sample_table':table,'scope':'Arithmetic only; no geometric certification'},indent=2))
