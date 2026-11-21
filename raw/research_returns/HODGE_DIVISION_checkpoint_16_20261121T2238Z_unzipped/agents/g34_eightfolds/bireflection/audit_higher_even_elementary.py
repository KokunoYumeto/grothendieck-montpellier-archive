#!/usr/bin/env python3
"""Independent symbolic checks for the elementary HES replacement.

The universal group/representation proof is reviewed separately. These
checks validate the displayed matrix identities and exact constant bounds;
small matrix sizes are not presented as a proof for all dimensions.
"""
from pathlib import Path
from fractions import Fraction as F
import json,time
import sympy as s

B=Path(__file__).resolve().parent

def zero2(M):
    for z in M:
        p=s.Poly(s.expand(z),*sorted(z.free_symbols,key=str)) if z.free_symbols else None
        if p is None:
            assert int(z)%2==0,z
        else:
            assert all(int(c)%2==0 for c in p.coeffs()),z

def symp(r):
    return s.zeros(r).row_join(s.eye(r)).col_join(s.eye(r).row_join(s.zeros(r)))

def Q(v,c):
    r=len(v)//2;J=symp(r);M=s.eye(2*r+2)
    M[0,1:2*r+1]=(J*v).T
    M[1:2*r+1,2*r+1]=v
    M[0,2*r+1]=c
    return M

def main():
    start=time.perf_counter();checks=[]
    for r in [1,2,3]:
        v=s.Matrix(s.symbols(f'v0:{2*r}'));w=s.Matrix(s.symbols(f'w0:{2*r}'))
        c,d=s.symbols('c d');J=symp(r);G=s.zeros(2*r+2)
        G[0,-1]=G[-1,0]=1;G[1:2*r+1,1:2*r+1]=J
        A=Q(v,c);C=Q(w,d)
        zero2(A.T*G*A-G)
        zero2(A*A-s.eye(2*r+2))
        zero2(A*C-Q(v+w,c+d+(v.T*J*w)[0]))
        zero2(A*C-C*A)
        checks.append(f'line radical generic symplectic/composition/exponent2/commutativity, Wdim{2*r}')
    for r in [1,2,3]:
        X=s.zeros(r);Y=s.zeros(r)
        for i in range(r):
            for j in range(i,r):
                X[i,j]=X[j,i]=s.Symbol(f'b{i}{j}')
                Y[i,j]=Y[j,i]=s.Symbol(f'c{i}{j}')
        T=lambda C:s.eye(r).row_join(C).col_join(s.zeros(r).row_join(s.eye(r)))
        zero2(T(X).T*symp(r)*T(X)-symp(r))
        zero2(T(X)*T(Y)-T(X+Y))
        checks.append(f'generic symmetric-shear identity, Rdim{r}')

    assert F(3,4)+F(1,4*4)==F(13,16)
    assert (1-F(1,3))*(1-F(13,16))==F(1,8)
    assert 16*3**5<9*155**2 and 16*3**6<9*155**2
    assert 16*3**7<9*63**2
    x=s.Symbol('x')
    assert s.expand((2*x-1)**2-3*(x-1)**2)==x*x+2*x-2
    assert 64**2+2*64-2>0
    assert F(3,4)+F(1,4*3)==F(5,6)
    assert (1-F(3,4))/2==F(1,8)
    assert F(6)/(1+10*F(1,8)-2)==24<35
    checks+=['13/16 fixed-space bound','odd-prime weight support1/8',
             'elliptic3/4 initial cases and universal induction polynomial',
             'elliptic prime-order5/6 eigenspace','involution1/8 support','ESD degree ceiling24']
    out={'status':'PASS independent symbolic arithmetic',
         'scope':'Universal mathematical proof separate; finite symbolic matrices do not assert all-rank sufficiency.',
         'checks':checks,'elapsed_seconds':round(time.perf_counter()-start,6)}
    B.joinpath('audit_higher_even_elementary.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
