"""Exact Q(i) matrix arithmetic, adapted from the quadratic-field certificate. No group data."""
from fractions import Fraction as Q
from itertools import product,combinations
import json,time
from pathlib import Path

class F:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        if isinstance(a,F): self.a,self.b=a.a,a.b
        else: self.a,self.b=Q(a),Q(b)
    def __add__(x,y):
        y=F(y);return F(x.a+y.a,x.b+y.b)
    __radd__=__add__
    def __neg__(x):return F(-x.a,-x.b)
    def __sub__(x,y):return x+-F(y)
    def __rsub__(x,y):return F(y)+-x
    def __mul__(x,y):
        y=F(y);return F(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a)
    __rmul__=__mul__
    def inv(x):
        d=x.a*x.a+x.b*x.b
        if d==0:raise ZeroDivisionError
        return F(x.a/d,-x.b/d)
    def __truediv__(x,y):return x*F(y).inv()
    def __rtruediv__(x,y):return F(y)*x.inv()
    def conj(x):return F(x.a,-x.b)
    def __bool__(x):return bool(x.a or x.b)
    def __eq__(x,y):
        try:y=F(y)
        except:return False
        return x.a==y.a and x.b==y.b
    def __hash__(x):return hash((x.a,x.b))
    def __repr__(x):return str(x.a) if not x.b else f'({x.a})+({x.b})*w'
    def pair(x):return [str(x.a),str(x.b)]
Z=F();ONE=F(1);w=F(0,1)

def mat(a):return [[F(x) for x in row] for row in a]
def zero(r,c):return [[Z for _ in range(c)]for _ in range(r)]
def eye(n):return [[F(i==j)for j in range(n)]for i in range(n)]
def tr(a):return [list(x)for x in zip(*a)]
def star(a):return [[x.conj()for x in row]for row in tr(a)]
def add(a,b):return [[x+y for x,y in zip(r,s)]for r,s in zip(a,b)]
def sub(a,b):return [[x-y for x,y in zip(r,s)]for r,s in zip(a,b)]
def scale(a,c):return [[x*c for x in r]for r in a]
def mul(a,b):
    bt=tr(b);return [[sum((x*y for x,y in zip(row,col)),Z)for col in bt]for row in a]
def mv(a,v):return [sum((x*y for x,y in zip(row,v)),Z)for row in a]
def outer(v,u):return [[x*y for y in u]for x in v]
def dot(v,u):return sum((x.conj()*y for x,y in zip(v,u)),Z)
def rref(a):
    a=[r[:]for r in a];pivs=[];rr=0
    for j in range(len(a[0])):
        piv=next((i for i in range(rr,len(a))if a[i][j]),None)
        if piv is None:continue
        a[rr],a[piv]=a[piv],a[rr]
        a[rr]=[x/a[rr][j]for x in a[rr]]
        for i in range(len(a)):
            if i!=rr and a[i][j]:
                c=a[i][j];a[i]=[x-c*y for x,y in zip(a[i],a[rr])]
        pivs.append(j);rr+=1
        if rr==len(a):break
    return a,pivs

def rank(a):return len(rref(a)[1])
def inv(a):
    n=len(a);rr,p=rref([r+s for r,s in zip(a,eye(n))]);assert p[:n]==list(range(n));return [r[n:]for r in rr]
def det(a):
    a=[r[:]for r in a];d=ONE;n=len(a)
    for j in range(n):
        p=next((i for i in range(j,n)if a[i][j]),None)
        if p is None:return Z
        if p!=j:a[j],a[p]=a[p],a[j];d=-d
        d=d*a[j][j]
        for i in range(j+1,n):
            c=a[i][j]/a[j][j]
            for k in range(j+1,n):a[i][k]=a[i][k]-c*a[j][k]
    return d

def serialize(a):return [[x.pair()for x in row]for row in a]
def iszero(a):return all(not x for row in a for x in row)

def nullspace(a):
    rr,p=rref(a);free=[j for j in range(len(a[0]))if j not in p];vs=[]
    for f in free:
      v=[Z]*len(a[0]);v[f]=ONE
      for i,j in enumerate(p):v[j]=-rr[i][f]
      vs.append(v)
    return tr(vs)

