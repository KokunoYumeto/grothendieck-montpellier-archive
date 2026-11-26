#!/usr/bin/env python3
"""Independent rank-three check using only word reduction and closed formulas.
No matrix coordinate solution, attached program, or Paper 5 program is imported.
"""
import json
from pathlib import Path


def add(a,b):
    c=a.copy()
    for j,v in b.items():c[j]=c.get(j,0)+v
    return {j:v for j,v in c.items() if v}

def neg(a):return {j:-v for j,v in a.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    c={}
    for i,u in a.items():
        for j,v in b.items():c[i+j]=c.get(i+j,0)+u*v
    return {j:v for j,v in c.items() if v}

def power(a,n):
    assert n>=0
    b={0:1}
    for _ in range(n):b=mul(b,a)
    return b

def scale(n,a):return {j:n*v for j,v in a.items() if n*v}
def const(n):return {0:n} if n else {}
D={-1:1,0:2,1:1}
words=((1,),(2,),(1,2),(2,1))

def reduce_word(w):
    w=list(w);a=b=0
    while len(w)>2 or (len(w)==2 and w[0]==w[1]):
        repeat=next((i for i in range(len(w)-1) if w[i]==w[i+1]),None)
        if repeat is not None:
            w.pop(repeat);a+=1
        else:
            assert w[0]==w[2]
            w=w[:1]+w[3:];b+=1
    assert tuple(w) in words and b<=1
    return tuple(w),a,b

def params(kind):
    if kind=='trace':
        delta=mul(sub(D,const(1)),sub(D,const(4)))
        return {'delta':[neg(delta),delta], 'lam':[D,power(sub(D,const(2)),2)],
            'G':[scale(4,mul(D,sub(D,const(1)))),mul(power(D,2),sub(D,const(1)))],
            'S':scale(4,mul(power(D,2),power(sub(D,const(1)),2))),
            'W':D,'U':[D,D],'V':[sub(scale(5,D),const(4)),add(sub(scale(2,power(D,2)),scale(5,D)),const(4))]}
    de=mul(D,sub(D,const(3))) if kind=='first' else mul(sub(D,const(1)),sub(D,const(2)))
    return {'delta':[de,de], 'lam':[mul(D,sub(scale(4,D),const(9))),add(sub(scale(3,power(D,2)),scale(10,D)),const(4))],
        'G':[scale(10,mul(D,de)),scale(15,mul(D,de))], 'S':scale(30,mul(D,power(de,2))),
        'W':scale(5,D),'U':[scale(3,D),scale(7,D)],
        'V':[mul(D,add(scale(2,D),const(3))),sub(add(scale(6,power(D,2)),scale(5,D)),const(2))]}

def table(kind, parameters=None):
    p=params(kind) if parameters is None else parameters;T={}
    basis=['one','Sigma']+[(i,w) for i in range(2) for w in words]
    for x in basis:
        T['one',x,x]=const(1);T[x,'one',x]=const(1)
    T['Sigma','Sigma','Sigma']=p['S']
    for i in range(2):
        for x in words:
            g=(i,x);gx=mul(power(D,len(x)-1),p['G'][i])
            T[g,'Sigma','Sigma']=gx;T['Sigma',g,'Sigma']=gx
            for j in range(2):
                for y in words:
                    h=(j,y)
                    if i!=j:
                        T[g,h,'Sigma']=mul(power(D,len(x)+len(y)-2),p['W'])
                    else:
                        z,a,b=reduce_word(x+y)
                        assert len(x)+len(y)==len(z)+a+2*b
                        T[g,h,(i,z)]=mul(mul(p['delta'][i],power(D,a)),power(p['lam'][i],b))
                        if b==0:T[g,h,'Sigma']=mul(power(D,len(z)+a-2),p['U'][i])
                        else:T[g,h,'Sigma']=mul(power(D,len(z)+a-1),p['V'][i])
    assert len(T)==132 and all(T.values())
    return T

def uni(p):
    a,b=min(p),max(p)
    return a==-b and all(p.get(j,0)==p.get(-j,0) for j in p) and all(p.get(j,0)<=p.get(j+1,0) for j in range(a,0))

if __name__=='__main__':
    ct=table('trace');report={'method':'closed multiplication formulas with direct two-letter word reduction','nonzero_constants':len(ct),'examples':{}}
    for kind in ('first','second'):
        dt=table(kind);assert set(dt)==set(ct)
        zeros=[];pairs=0;nonuni=0
        for key,d in dt.items():
            c=ct[key]
            for j in set(c)|set(d):
                cv,dv=c.get(j,0),d.get(j,0)
                assert dv>=abs(cv) and (dv-cv)%2==0
                pairs+=(dv-abs(cv))//2
                if cv==0 and dv>0:zeros.append((key,j,dv))
            nonuni+=not uni(d)
        report['examples'][kind]={'supported_zero_weights':len(zeros),'bottom_supported_zero_weights':sum(k[2]=='Sigma' for k,j,dv in zeros),'cancelling_pairs':pairs,'nonunimodal_dimension_constants':nonuni}
    assert report['examples']['first']['supported_zero_weights']==54
    assert report['examples']['second']['supported_zero_weights']==58
    assert report['examples']['first']['cancelling_pairs']==7952
    assert report['examples']['second']['cancelling_pairs']==11764
    assert report['examples']['second']['nonunimodal_dimension_constants']==0
    path=Path(__file__).resolve().parents[1]/'checks'/'paper1_rank_three_crosscheck.json'
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
