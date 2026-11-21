"""Exact algebraic certificate for a five-row staircase motif.

This evaluates fixed rational-function matrices, not a growing-size
Jacobian extrapolation. The associated degree argument is in R20.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

x,y,z,w,q=sp.symbols('x y z w q')


def top_forms(parameters):
    A,B,C,D,E,F,G,H,I,J=parameters
    L=lambda c:x-c*y
    V=lambda c:z-c*w
    ell=lambda i:x-q**i*y
    v=lambda i:z-q**i*w
    R=[
      -v(1)*v(2)*(L(B)*V(H)*v(4)+V(E)*V(H)*ell(4)+V(E)*L(A)*v(3)),
      -v(1)*v(2)*v(4)*V(H)*V(I),
      ell(3)*v(1)*v(4)*V(H)*V(I)-v(2)*v(3)*V(G)*(ell(1)*V(J)+L(A)*v(1)),
      ell(4)*v(2)*V(G)*(ell(1)*V(J)+L(A)*v(1)),
    ]
    S=[
      -ell(1)*L(A)*v(2)*(ell(4)*V(H)+L(A)*v(3)),
      v(1)*L(A)*v(2)*(ell(4)*V(H)+L(A)*v(3))-ell(2)*L(C)*v(0)*v(3)*V(J),
      L(C)*v(0)*v(2)*v(3)*V(J),
      v(3)*(L(D)*V(I)*v(0)*v(1)+L(B)*V(J)*v(0)*v(2)+ell(1)*V(J)*V(F)*v(2)+L(A)*V(F)*v(1)*v(2)),
    ]
    return list(map(sp.expand,R)),list(map(sp.expand,S))


def conv(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
      for j,v in enumerate(b):c[i+j]=(c[i+j]+u*v)%p
    return c


def product(roots,p):
    out=[1]
    for root in roots:out=conv(out,[1,-root%p],p)
    return out


def qpow(qv,e,p):return pow(qv,e,p)


def normalize(F,side,qv,K,X,p):
    poly=sp.Poly(F.subs(q,qv),x,y,z,w)
    grades={e[2]+e[3] for e,c in poly.terms()}
    assert len(grades)==1
    g=grades.pop();a=5-g
    coeff=[[0]*(g+1) for _ in range(a+1)]
    for (ex,ey,ez,ew),c in poly.terms():coeff[ey][ew]=int(c)%p
    Q=[]
    if side=='row':
        indices=range(1,a+2)
        for j in indices:
            Q.append(product([K*qpow(qv,h,p)%p for h in range(j,a+1)]+
                             [qpow(qv,h,p) for h in range(1,j)],p))
    else:
        indices=range(a+1)
        for j in indices:
            Q.append(product([qpow(qv,h,p) for h in range(5-j,5)]+
                             [pow(K,-1,p)*qpow(qv,5-a+h,p)%p for h in range(a-j)],p))
    Qmat=sp.Matrix([[Q[j][i] for j in range(a+1)] for i in range(a+1)])
    qdet=int(Qmat.det())%p
    if not qdet:return None,{'a':a,'g':g,'basis_determinant':0}
    Cs=Qmat.inv_mod(p)*sp.Matrix(coeff)
    out=[0]*6
    for jj,j in enumerate(indices):
        if side=='row':
            shift=qpow(qv,-j,p)
            scale=pow(X,j,p)
            extra=[qpow(qv,h,p) for h in range(5-j,4)]
            extra += [K*qpow(qv,h,p)%p for h in range(-1,a-j)]
        else:
            shift=K*qpow(qv,j-5,p)%p
            scale=pow(X,-j,p)
            extra=[qpow(qv,h,p) for h in range(-a+j,0)]
            extra += [K*qpow(qv,-5+h,p)%p for h in range(j)]
        shifted=[int(Cs[jj,s])*pow(shift,s,p)%p for s in range(g+1)]
        term=conv(shifted,product(extra,p),p)
        assert len(term)==6
        out=[(u+scale*v)%p for u,v in zip(out,term)]
    return out,{'a':a,'g':g,'basis_determinant':qdet}


def certificate(parameters,qv=6,K=40,X=40,p=41):
    R,S=top_forms(parameters)
    matrices={};meta={}
    for side,forms in [('row',R),('column',S)]:
        roots=([qpow(qv,i,p) for i in range(4)] if side=='row'
               else [K*qpow(qv,i,p)%p for i in range(-5,-1)])
        bb=product(roots,p)
        columns=[bb+[0],[0]+bb]
        details=[]
        for f in forms:
            c,d=normalize(f,side,qv,K,X,p)
            if c is None:return None
            columns.append(c);details.append(d)
        M=sp.Matrix.hstack(*(sp.Matrix(c) for c in columns))
        matrices[side]=[[int(v)%p for v in M.row(i)] for i in range(6)]
        meta[side]={'determinant':int(M.det())%p,'forms':details}
    return {'parameters':parameters,'prime':p,'q':qv,'K':K,'X':X,'matrices':matrices,'metadata':meta}


def main():
    choices=[[2,3,4,5,2,3,4,5,6,7],
             [20,26,5,39,4,10,13,14,18,24],
             [0,1,2,3,0,1,2,3,4,5]]
    for parameters in choices:
        result=certificate(parameters)
        print(json.dumps({'parameters':parameters,'row_det':result['metadata']['row']['determinant'],
                          'column_det':result['metadata']['column']['determinant']}),flush=True)
        if result['metadata']['row']['determinant'] and result['metadata']['column']['determinant']:
            Path(__file__).with_name('staircase5_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
            R,S=top_forms(parameters)
            for i,f in enumerate(R):print('R',i,sp.factor(f))
            for i,f in enumerate(S):print('S',i,sp.factor(f))
            break
    else:raise AssertionError('No successful certificate')

if __name__=='__main__':main()
