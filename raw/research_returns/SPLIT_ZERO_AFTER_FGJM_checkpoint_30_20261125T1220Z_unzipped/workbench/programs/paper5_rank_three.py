#!/usr/bin/env python3
"""Reconstruct two rank-three lifts by block matrix multiplication.

The method constructs bases of Q(D)×Q(D)×M2(Q(D))×M2(Q(D)),
then solves coordinates of every product. It does not import earlier tables
or the attached search programs. Run: python programs/paper5_rank_three.py
"""
from pathlib import Path
import json
import sympy as sp

D,q=sp.symbols('D q')
WORDS=((0,),(1,),(0,1),(1,0))
NAMES=['1','Sigma']+[f'g{i+1}_{"".join(str(j+1) for j in w)}'
                     for i in range(2) for w in WORDS]

def pack(z,t,A,B):return sp.Matrix([z,t,*list(A),*list(B)])
def matrix(v,k):return sp.Matrix(2,2,list(v[2+4*k:6+4*k]))
def multiply(x,y):return pack(x[0]*y[0],x[1]*y[1],
                               matrix(x,0)*matrix(y,0),matrix(x,1)*matrix(y,1))

def basis(kind):
    lam=[D,(D-2)**2]
    if kind=='trace':
        delta=[lam[0]-lam[1],lam[1]-lam[0]]
        G=[4*D*(D-1),D**2*(D-1)]
        S=4*D**2*(D-1)**2
    elif kind in ('minimal_example','unimodal_example'):
        lam=[D*(4*D-9),3*D**2-10*D+4]
        de=D*(D-3) if kind=='minimal_example' else (D-1)*(D-2)
        delta=[de,de];G=[10*D*de,15*D*de];S=30*D*de**2
    else:
        assert kind in ('window_pairs','window_zeros','window_unimodal')
        de=(D-1)*(D-2) if kind=='window_unimodal' else D*(D-3)
        lam=[4*D**2-15*D+12 if kind=='window_pairs' else D,3*D**2-10*D+4]
        a1,a2,b=(10,15,30) if kind=='window_pairs' else (14,7,14)
        delta=[de,de];G=[a1*D*de,a2*D*de];S=b*D*de**2
    zero=sp.zeros(2);out=[pack(1,1,sp.eye(2),sp.eye(2)),pack(0,S,zero,zero)]
    for i in range(2):
        P=[sp.Matrix([[D,lam[i]],[0,0]]),sp.Matrix([[0,0],[1,D]])]
        for w in WORDS:
            A=sp.eye(2)
            for j in w:A=A*P[j]
            B=[zero,zero];B[i]=delta[i]*A
            out.append(pack(0,D**(len(w)-1)*G[i],*B))
    T=sp.Matrix.hstack(*out)
    assert sp.factor(T.det())!=0
    return out,T

def table(kind):
    b,T=basis(kind);inv=T.inv();out={}
    for i in range(10):
        for j in range(10):
            v=multiply(b[i],b[j]);c=inv*v
            c=c.applyfunc(sp.factor)
            assert (T*c-v).applyfunc(sp.cancel)==sp.zeros(10,1)
            for k,x in enumerate(c):
                if x!=0:
                    assert sp.denom(sp.cancel(x))==1,(kind,i,j,k,x)
                    out[(i,j,k)]=sp.expand(x)
    return out

def laurent(poly):
    expanded=sp.expand(poly.subs(D,q+2+1/q))
    out={}
    for term in sp.Add.make_args(expanded):
        if term==0:continue
        power=int(term.as_powers_dict().get(q,0))
        coeff=sp.cancel(term/q**power)
        assert coeff.is_Rational
        out[power]=out.get(power,0)+coeff
    return {j:c for j,c in out.items() if c}

def symmetric_unimodal(v):
    if not v:return True
    a,b=min(v),max(v)
    if a!=-b:return False
    seq=[v.get(j,0) for j in range(a,b+1)]
    return seq==seq[::-1] and all(seq[j]<=seq[j+1] for j in range(len(seq)//2))

if __name__=='__main__':
    root=Path(__file__).resolve().parents[1];trace=table('trace');ct={k:laurent(v) for k,v in trace.items()}
    failures=[(NAMES[i],NAMES[j],NAMES[k]) for (i,j,k),x in trace.items()
              if sp.expand(x-(D-1)*(D-4)*(D-2)**2)==0]
    assert len(trace)==132,len(trace)
    assert len(failures)==6,len(failures)
    cert={'method':'independent block-matrix coordinate solution',
          'basis':NAMES,'trace_nonzero_constants':len(trace),
          'six_constants':failures,'trace_table':{','.join(map(str,k)):str(v) for k,v in trace.items()},
          'examples':{}}
    for kind in ['minimal_example','unimodal_example','window_pairs','window_zeros','window_unimodal']:
        dim=table(kind);assert set(dim)==set(trace)
        cancel=0;zeros=[];nonuni=[];out={}
        for key,dpoly in dim.items():
            d=laurent(dpoly);c=ct[key];weights=set(d)|set(c)
            for w in weights:
                dv=d.get(w,sp.Integer(0));cv=c.get(w,sp.Integer(0))
                assert dv>=abs(cv),(kind,key,w,dv,cv)
                assert dv.is_Integer and cv.is_Integer
                assert (dv-cv)%2==0
                cancel+=int((dv-abs(cv))/2)
                if cv==0 and dv>0:zeros.append([*key,w,int(dv)])
            if not symmetric_unimodal(d):nonuni.append(key)
            out[','.join(map(str,key))]={'dimension':str(dpoly),'dimension_laurent':{str(w):int(v) for w,v in d.items()}}
        cert['examples'][kind]={'cancel_pairs':cancel,'supported_zero_weight_count':len(zeros),
          'bottom_supported_zero_weight_count':sum(z[2]==1 for z in zeros),
          'supported_zeros':zeros,'nonunimodal_constant_count':len(nonuni),'table':out}
        if kind in ('unimodal_example','window_unimodal'):assert not nonuni
        print(kind, 'cancel_pairs=',cancel,'zero_weights=',len(zeros),
              'bottom_zero_weights=',sum(z[2]==1 for z in zeros),'nonunimodal=',len(nonuni),flush=True)
    f=sp.expand((q+1+1/q)*(q+1/q)**2)
    cert['unimodality_counterexample']={str(w):int(v) for w,v in laurent(f).items()}
    assert [sp.expand(f).coeff(q,j) for j in range(-3,4)]==[1,1,3,2,3,1,1]
    (root/'checks'/'paper5_rank_three_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS: 132 exact trace constants; six named failures; five associative effective lifts verified')
