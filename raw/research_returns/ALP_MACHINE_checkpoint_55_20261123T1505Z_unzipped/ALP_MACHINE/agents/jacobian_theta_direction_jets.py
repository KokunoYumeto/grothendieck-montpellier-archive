#!/usr/bin/env python3
"""Exact Hurwitz recurrence for D135 Baker=Chern theta; no division by order."""
from fractions import Fraction
from math import comb
from pathlib import Path
import argparse, json
import sympy as sp

class Cyc:
    def __init__(self,p=None):
        self.p=p
        self.zero=(0,)*6
        self.one=(1,0,0,0,0,0)
    def scalar(self,n,d=1):
        v=(n*pow(d,-1,self.p))%self.p if self.p else Fraction(n,d)
        return (v,0,0,0,0,0)
    def zeta(self,n):
        n%=7
        if n<6:return tuple(int(i==n) for i in range(6))
        return tuple((self.p-1) if self.p else -1 for _ in range(6))
    def add(self,a,b):return tuple((x+y)%self.p if self.p else x+y for x,y in zip(a,b))
    def neg(self,a):return tuple((-x)%self.p if self.p else -x for x in a)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        c=[0]*7
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b):
                    if y:c[(i+j)%7]+=x*y
        return tuple((c[i]-c[6])%self.p if self.p else c[i]-c[6] for i in range(6))
    def scale(self,a,n):return tuple((n*x)%self.p if self.p else n*x for x in a)
    def inv(self,a):
        z=sp.Symbol('z')
        f=sum(sp.Rational(x.numerator,x.denominator)*z**i if isinstance(x,Fraction) else x*z**i for i,x in enumerate(a))
        phi=sum(z**i for i in range(7))
        g=sp.Poly(sp.invert(f,phi,z,modulus=self.p),z) if self.p else sp.Poly(sp.invert(f,phi,z),z)
        return tuple(int(g.nth(i))%self.p if self.p else Fraction(g.nth(i)) for i in range(6))
    def show(self,a):return [str(v) for v in a]

class Expr:
    def __init__(self,ctx,op,args=(),initial=None):
        self.ctx,self.op,self.args=ctx,op,args
        self.data=[] if initial is None else [initial]
    def coeff(self,n):
        R=self.ctx
        if self.op=='var':return self.data[n]
        while len(self.data)<=n:
            k=len(self.data)
            if self.op=='const':v=R.zero
            elif self.op=='add':v=R.add(self.args[0].coeff(k),self.args[1].coeff(k))
            elif self.op=='neg':v=R.neg(self.args[0].coeff(k))
            elif self.op=='mul':
                v=R.zero
                for j in range(k+1):v=R.add(v,R.scale(R.mul(self.args[0].coeff(j),self.args[1].coeff(k-j)),comb(k,j)))
            else:raise ValueError(self.op)
            self.data.append(v)
        return self.data[n]
    def __add__(self,b):
        if not isinstance(b,Expr):b=const(self.ctx,b)
        return Expr(self.ctx,'add',(self,b))
    __radd__=__add__
    def __neg__(self):return Expr(self.ctx,'neg',(self,))
    def __sub__(self,b):return self+-b
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if not isinstance(b,Expr):b=const(self.ctx,b)
        return Expr(self.ctx,'mul',(self,b))
    __rmul__=__mul__
    def __pow__(self,n):
        if n==0:return const(self.ctx,1)
        if n==1:return self
        h=self**(n//2)
        return h*h if n%2==0 else h*h*self

def const(R,v):return Expr(R,'const',initial=v if isinstance(v,tuple) else R.scalar(v))

def jets(direction,N,p=None):
    R=Cyc(p)
    x=[Expr(R,'var',initial=R.zeta(j)) for j in (1,3,5)]
    y=[Expr(R,'var',initial=R.zero) for _ in range(3)]
    zz={(j,k):Expr(R,'var',initial=R.inv(R.sub(x[j].data[0],x[k].data[0]))) for j,k in ((0,1),(0,2),(1,2))}
    def iz(j,k):return zz[j,k] if j<k else -zz[k,j]
    q=[]
    for j in range(3):
        m,n=[k for k in range(3) if k!=j]
        v=iz(j,m)*iz(j,n)
        if direction==1:v=v*x[m]*x[n]
        if direction==2:v=-v*(x[m]+x[n])
        q.append(v)
    dx=[y[j]*q[j] for j in range(3)]
    dy=[const(R,R.scalar(7,2))*x[j]**6*q[j] for j in range(3)]
    dz={jk:-z*z*(dx[jk[0]]-dx[jk[1]]) for jk,z in zz.items()}
    quarter=const(R,R.scalar(1,4))
    W33=(x[0]+x[1]+x[2])*quarter
    W23=-(x[0]*x[1]+x[0]*x[2]+x[1]*x[2])*quarter
    W13=x[0]*x[1]*x[2]*quarter
    rhs={}
    for j,k in ((0,1),(0,2),(1,2)):
        a,b=x[j],x[k]
        f=a**3*b**3*(a+b)-2
        rhs[j,k]=(f-2*y[j]*y[k])*iz(j,k)**2*quarter-W13*(a*a+b*b)-W23*(a*a*b+a*b*b)-W33*a*a*b*b
    ta=-(rhs[0,2]-rhs[0,1])*iz(1,2)
    tb=-(rhs[1,2]-rhs[0,1])*iz(0,2)
    W22=(ta-tb)*iz(0,1)
    W12=ta-x[0]*W22
    W11=rhs[0,1]-(x[0]+x[1])*W12-x[0]*x[1]*W22
    Wii={1:W11,2:W22,3:W33}[direction]
    h=[R.zero,R.zero]
    for n in range(N-1):
        h.append(R.neg(Wii.coeff(n)))
        updates=[a.coeff(n) for a in dx+dy]+[a.coeff(n) for a in dz.values()]
        for a,v in zip(x+y+list(zz.values()),updates):a.data.append(v)
    assert all(h[n]==R.zero for n in range(1,N+1,2))
    s=[R.one]
    for n in range(1,N+1):
        v=R.zero
        for k in range(n):v=R.add(v,R.scale(R.mul(h[k+1],s[n-1-k]),comb(n-1,k)))
        s.append(v)
    assert all(s[n]==R.zero for n in range(1,N+1,2))
    return R,h,s

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--prime',type=int)
    parser.add_argument('--order',type=int,default=12)
    parser.add_argument('--directions',default='1,2,3')
    parser.add_argument('--output',default='jacobian_theta_direction_jets.json')
    args=parser.parse_args()
    result={'prime':args.prime,'max_order':args.order,'coefficient_order':'1,zeta,zeta^2,zeta^3,zeta^4,zeta^5','scope':'Exact Hurwitz derivatives, not divided Taylor coefficients; finite computation is not an all-order valuation proof.','directions':{}}
    for d in map(int,args.directions.split(',')):
        R,h,s=jets(d,args.order,args.prime)
        result['directions'][str(d)]={'log_derivatives':{str(n):R.show(v) for n,v in enumerate(h) if v!=R.zero},'theta_derivatives':{str(n):R.show(v) for n,v in enumerate(s) if v!=R.zero}}
        print('completed direction',d,'nonzero derivative orders',[n for n,v in enumerate(s) if v!=R.zero],flush=True)
    target=Path(__file__).resolve().parent/args.output
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(target)
