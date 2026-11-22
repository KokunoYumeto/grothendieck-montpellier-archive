"""Exact sixfold period-map and degree certificates; no floating-point steps.
HODGE_DIVISION /root/sixfolds; 2026-11-21.
The calculations verify the finite data in Schoen1998 Lemma13 and
Koike2004 equations(2),(6),(7), and the corrected full-norm-fibre degree.
They are algebraic certificates, not a proof that a selected coefficient
point defines a smooth curve. Published generic smoothness is used.
"""
from itertools import product, combinations
from math import factorial
from pathlib import Path
import json
import sympy as sp

def schoen_characters():
    holomorphic=[]
    for c in product(range(3),repeat=3):
        alpha=[(-sum(c))%3,*c]
        num=sum((-a)%3 for a in alpha)
        assert num%3==0
        mult=0 if c==(0,0,0) else -1+num//3
        assert mult>=0
        holomorphic += [c]*mult
    assert len(holomorphic)==10
    plus=[c for c in holomorphic if (c[0]+c[1])%3==1]
    minus=[c for c in holomorphic if (c[0]+c[1])%3==2]
    assert len(plus)==len(minus)==3
    products=[[tuple((a+b)%3 for a,b in zip(c,d)) for d in minus]for c in plus]
    assert len(set(sum(products,[])))==9
    return dict(holomorphic=holomorphic,plus=plus,minus=minus,products=products,rank=9)

def koike_identities():
    s,t,x,y=sp.symbols('s t x y'); I=sp.I
    a1=s+t+x+y;a2=s*t+t*x+x*y+y*s;a3=t*x*y+s*x*y+s*t*y+s*t*x
    a4=s*x+t*y;a5=s*t*x*y;a6=sp.Integer(1)
    b1=s-t+x-y;b2=s*t-t*x+x*y-y*s;b3=t*x*y-s*x*y+s*t*y-s*t*x;b4=s*x-t*y
    c1=s-I*t-x+I*y;c2=s*t-I*t*x-x*y+I*y*s;c3=t*x*y-I*s*x*y-s*t*y+I*s*t*x
    d1=s+I*t-x-I*y;d2=s*t+I*t*x-x*y-I*y*s;d3=t*x*y+I*s*x*y-s*t*y-I*s*t*x
    relations=[
      b1**2-(a1*a1-4*a2*a6),
      b2**2-(a2*a2-4*(a1*a3-a2*a4)+16*a5*a6),
      b3**2-(a3*a3-4*a2*a5),b1*b3-(a1*a3-2*a2*a4),
      b1*b4-(a1*a4-2*a3*a6),b3*b4-(-a3*a4+2*a1*a5),b4*b4-(a4*a4-4*a5*a6),
      c1*d1-(a1*a1-2*a2*a6-4*a4*a6),c3*d3-(a3*a3-2*a2*a5-4*a4*a5),
      c2*d2-(a2*a2-2*a1*a3+2*a2*a4),
      (c1*d3+c3*d1)/2-(-a1*a3+a2*a4+8*a5*a6),
      I*(c1*d3-c3*d1)/2-b2*b4,
      (c1*d2-I*c2*d1)/(1-I)-(a1*a2-4*a3*a6),
      (c1*d2+I*c2*d1)/(1+I)-b1*b2,
      (c2*d3+I*c3*d2)/(1+I)-(-a2*a3+4*a1*a5),
      -I*(c2*d3-I*c3*d2)/(1+I)-b2*b3]
    assert all(sp.expand(r)==0 for r in relations)
    return len(relations)

def koike_matrices():
    u,v,w=sp.symbols('u v w')
    mon=[u*u,v*v,w*w,u*v,u*w,v*w]
    mat=lambda ps:sp.Matrix([[sp.Poly(sp.expand(p),u,v,w).coeff_monomial(m)for m in mon]for p in ps])
    M0=mat([u*u,v*v-2*u*w,w*w,u*v,-u*w,-v*w])
    assert M0.det()==1
    a1,a2,a3=u,v,w
    a4=u+2*v+3*w;a5=2*u+3*v+5*w;a6=3*u+5*v+7*w
    b=[a1*a1-4*a2*a6,a2*a2-4*(a1*a3-a2*a4)+16*a5*a6,a3*a3-4*a2*a5,
       a1*a3-2*a2*a4,a1*a4-2*a3*a6,-a3*a4+2*a1*a5,a4*a4-4*a5*a6]
    gam=[a1*a1-2*a2*a6-4*a4*a6,a2*a2-2*a1*a3+2*a2*a4,
         a3*a3-2*a2*a5-4*a4*a5,a1*a2-4*a3*a6,-a1*a3+a2*a4+8*a5*a6,-a2*a3+4*a1*a5]
    M,B=mat(gam),mat(b)
    assert M.det()==-389639
    assert B.rank()==6
    rows=next(rows for rows in combinations(range(7),6)if B[list(rows),:].det()!=0)
    return dict(M0=M0.tolist(),det_M0=1,M=M.tolist(),det_M=int(M.det()),B=B.tolist(),
                B_minor_rows=rows,B_minor=int(B[list(rows),:].det()),rank=9)

def degrees():
    out={}
    for n in [2,3]:
        W=3**(2*n)*factorial(4*n+1)//factorial(2*n+1)
        T=3**(3*n)*factorial(3*n)*4**n
        D=sp.Rational(2**n*W*T,3**n)
        assert D.q==1
        out['gaussian_n'+str(n)]=dict(W_3Theta=W,T_3Theta=T,principal_detector_bound=int(D))
    W=3**6*factorial(10)//factorial(4)
    T=3**6*factorial(6)*27
    D=W*T//27
    assert D==57854793024000
    out['eisenstein_n3']=dict(W_3Theta=W,T_3Theta=T,detector_bound=D)
    return out

if __name__=='__main__':
    result=dict(schoen=schoen_characters(),koike_identity_count=koike_identities(),koike=koike_matrices(),degrees=degrees())
    rendered=json.dumps(result,indent=2,default=int)+'\n'
    print(rendered)
    Path(__file__).with_name('sixfold_certificates_output.json').write_text(rendered)
