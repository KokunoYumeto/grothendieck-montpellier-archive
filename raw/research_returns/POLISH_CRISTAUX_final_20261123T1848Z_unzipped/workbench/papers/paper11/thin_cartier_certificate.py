"""Exact Cartier checks for even thin systems in characteristic two.

Arithmetic is in F_4=F_2[u]/(u^2+u+1), with inverse Frobenius applied
to coefficients at every iteration. Uniformity in degree and in the
ordinary elliptic parameter is proved in the paper and its companion
proof records; the finite computations here check explicit witnesses.
Newly written code: CC0 1.0. Python standard library only.
"""

from itertools import product
import json

class F4:
    @staticmethod
    def add(a,b): return a^b
    @staticmethod
    def mul(a,b):
        out=0
        while b:
            if b&1: out^=a
            b >>= 1
            a <<= 1
            if a&4: a^=7
        return out
    @classmethod
    def sq(cls,a): return cls.mul(a,a)
    @classmethod
    def sqrt(cls,a): return cls.sq(a)
    @classmethod
    def inv(cls,a):
        assert a
        return cls.sq(a)

F=F4

def basis(m):
    return sorted([(i,0) for i in range(m//2+1)]
                  +[(i,1) for i in range((m-3)//2+1)],
                  key=lambda z:2*z[0]+3*z[1])

def add_term(p,z,a):
    if not a:return
    p[z]=p.get(z,0)^a
    if not p[z]:del p[z]

def monmul(u,v,ordinary,q):
    i=u[0]+v[0];j=u[1]+v[1]
    if j<2:return {(i,j):1}
    if ordinary:return {(i+1,1):1,(i+3,0):1,(i,0):F.sq(q)}
    return {(i,1):1,(i+3,0):1}

def pmul(p,r,ordinary,q):
    ans={}
    for u,a in p.items():
        for v,b in r.items():
            for z,c in monmul(u,v,ordinary,q).items():
                add_term(ans,z,F.mul(F.mul(a,b),c))
    return ans

def moncart(z,ordinary,q):
    i,j=z
    if j==0:
        if ordinary:return {(i//2,0):1} if i%2==0 else {}
        return {((i-1)//2,0):1} if i%2 else {}
    if i%2==0:return {(i//2+1,0):1}
    ans={((i-1)//2,1):1}
    if ordinary:add_term(ans,((i-1)//2,0),q)
    return ans

def pcart(p,ordinary,q):
    ans={}
    for z,a in p.items():
        for v,b in moncart(z,ordinary,q).items():
            add_term(ans,v,F.mul(F.sqrt(a),b))
    return ans

def cmul(u,v,ordinary,q):
    return pcart(monmul(u,v,ordinary,q),ordinary,q)

def witness(m,q):
    t=m//2
    c={(t-2,1):1,(0,1):1}
    f=pcart(c,True,q)
    a=pmul(f,f,True,q)
    add_term(a,(1,0),1)
    return [(z,(0,0),v) for z,v in a.items()]+[((0,0),(1,0),1)]+[(z,(0,1),v) for z,v in c.items()]

def matrix(m,q):
    b=list(product(basis(m),basis(3)))
    ix={z:i for i,z in enumerate(b)}
    ans=[]
    for u,v in b:
        col=[0]*len(b)
        for s1,s2,c in witness(m,q):
            for z,a in cmul(u,s1,True,q).items():
                for w,d in cmul(v,s2,False,0).items():
                    j=ix[z,w]
                    col[j]^=F.mul(F.sqrt(c),F.mul(a,d))
        ans.append(col)
    return ans

def echelon(vectors):
    piv={}
    for original in vectors:
        v=list(original)
        for j in range(len(v)-1,-1,-1):
            if not v[j]:continue
            if j in piv:
                a=v[j]
                v=[x^F.mul(a,y) for x,y in zip(v,piv[j])]
            else:
                a=F.inv(v[j])
                piv[j]=[F.mul(a,x) for x in v]
                break
    return list(piv.values())

def apply(cols,v):
    ans=[0]*len(cols)
    for a,col in zip(v,cols):
        if a:
            b=F.sqrt(a)
            ans=[x^F.mul(b,y) for x,y in zip(ans,col)]
    return ans

def ranks(cols):
    im=echelon(cols);initial=len(im)
    for i in range(len(cols)+1):
        nxt=echelon(apply(cols,v) for v in im)
        if len(nxt)==len(im):return initial,len(nxt),i+1
        im=nxt
    raise AssertionError


def supersingular_witness(m):
    t=m//2
    f={(t//2,0):1} if t%2==0 else {((t-3)//2,1):1}
    a=pmul(f,f,False,0)
    add_term(a,(1,0),1)
    c={(t-2,1):1}
    return [(z,(0,0),v) for z,v in a.items()]+[((0,0),(1,0),1)]+[(z,(0,1),v) for z,v in c.items()]

def matrix_for_section(m,q,ordinary,section):
    b=list(product(basis(m),basis(3)))
    ix={z:i for i,z in enumerate(b)}
    ans=[]
    for u,v in b:
        col=[0]*len(b)
        for s1,s2,c in section:
            for z,a in cmul(u,s1,ordinary,q).items():
                for w,d in cmul(v,s2,False,0).items():
                    col[ix[z,w]]^=F.mul(F.sqrt(c),F.mul(a,d))
        ans.append(col)
    return ans

def certify():
    rows=[]
    for m in [6,8,10,12,18]:
        result=ranks(matrix_for_section(m,0,False,supersingular_witness(m)))
        assert result[:2]==(3*m-2,3*m-2),(m,result)
        rows.append({'type':'supersingular/supersingular','m':m,
                     'rank':result[0],'stable_rank':result[1]})
    for m in [6,8,10]:
        for q in [1,2,3]:
            result=ranks(matrix_for_section(m,q,True,witness(m,q)))
            assert result[:2]==(3*m-2,3*m-2),(m,q,result)
            rows.append({'type':'ordinary/supersingular','m':m,'q_encoding':q,
                         'rank':result[0],'semilinear_stable_rank':result[1]})
    return {'field':'F_2[u]/(u^2+u+1)','outcome':'PASS',
            'scope':'Finite checks of explicit witnesses, not a proof by sampling.',
            'rows':rows}

if __name__=='__main__':
    import argparse
    from pathlib import Path
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    out=json.dumps(certify(),indent=2)+'\n'
    if args.output:args.output.write_text(out)
    else:print(out,end='')
