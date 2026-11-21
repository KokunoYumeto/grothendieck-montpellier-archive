#!/usr/bin/env python3
"""Independent small-matrix checks for the sibling G24/GF4 proof audit.

No sibling implementation is imported.  The quadratic arithmetic is the
independent sparse-exterior certificate's exact Fraction implementation.
This checks displayed group/field identities, not the large group enumeration
or parabolic-period minor reconstruction (those have separate readers).
"""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import json
from semiregular_gaussian_certificate import K

def mat(a):return [[K(x) for x in row] for row in a]
def eye(n):return mat([[int(i==j) for j in range(n)] for i in range(n)])
def mul(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),K()) for j in range(len(b[0]))] for i in range(len(a))]
def dag(a):return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scalar(a,c):return [[x*c for x in row] for row in a]
def col(v):return [[x] for x in v]
def ip(v,w,H):return mul(mul(dag(col(v)),H),col(w))[0][0]
def ref(v,H):return sub(eye(len(v)),scalar(mul(mul(col(v),dag(col(v))),H),K(2)/ip(v,v,H)))
def trace(a):return sum((a[i][i] for i in range(len(a))),K())
def serial(a):return [[x.serial() for x in row] for row in a]

def g24():
    K.d=7;t=K(F(-1,2),F(-1,2));tb=t.conj()
    H=mat([[2,-t,tb],[-tb,2,-t],[t,-tb,2]])
    rr=[ref([K(int(j==i)) for j in range(3)],H) for i in range(3)]
    g=mul(mul(rr[0],rr[1]),rr[2])
    expected=mat([[1+t,1,1],[1,1,-t],[-t,-1-t,-1]])
    assert g==expected
    roots=[mat([v])[0] for v in [[0,-1,1+t],[-1,0,t],[-2,t,1+t],[-1-t,-2,t],[-1,0,0],[-1,-1,t]]]
    assert all(ip(v,v,H)==2 for v in roots)
    assert all(mul(mul(dag(r),H),r)==H and mul(r,r)==eye(3) for r in rr)
    v=roots[0];gv=[row[0] for row in mul(g,col(v))]
    assert ip(v,gv,H)==t
    int_action=mul(sub(eye(3),ref(v,H)),g)
    assert mul(int_action,col(v))==col([t*x for x in v])
    assert trace(g)==1+t
    det=K(-308)-126*t
    assert det*det.conj()==87808
    return {'all_six_norms':2,'g0':serial(g),'trace_g0':trace(g).serial(),'field_action_scalar':t.serial(),'period_minor_norm':87808,'integral_action_identity':True}

def gf4():
    K.d=2;t=K(0,1);H=eye(4)
    Ph=mat([[0,-1,-1,0],[1,0,0,1],[1,0,0,-1],[0,-1,1,0]])
    z=scalar(Ph,t/2)
    assert dag(z)==z and mul(z,z)==H and trace(z)==0
    e1=[K(1),K(),K(),K()];s0=ref(e1,H)
    P=mat([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
    g=mul(P,z)
    assert mul(mul(sub(H,s0),g),col(e1))==col([t,K(),K(),K()])
    assert trace(mul(s0,g))==-t
    roots=[mat([v])[0] for v in [[0,-1,-1,0],[0,-1,0,1],[0,0,0,-1],[F(-1,2),F(1,2),F(-1,2),F(-1,2)],[0,0,-1,1]]]
    ss=[ref(v,H) for v in roots]
    simples=[mat([v])[0] for v in [[0,1,-1,0],[0,0,1,-1],[0,0,0,1],[F(1,2),F(-1,2),F(-1,2),F(-1,2)]]]
    words=[[1,4,1],[4],[2],[0,1,3,1,0]]
    for v,word in zip(simples,words):
        w=H
        for i in word:w=mul(w,ss[i])
        assert w==ref(v,H)
    short=[];long=[]
    for i in range(4):
        for sign in [-1,1]:short.append(tuple(F(sign*int(i==j)) for j in range(4)))
    short.extend(tuple(F(e,2) for e in signs) for signs in product([-1,1],repeat=4))
    for i in range(4):
        for j in range(i+1,4):
            for a,b in product([-1,1],repeat=2):long.append(tuple(F(a*int(k==i)+b*int(k==j)) for k in range(4)))
    def image(v):return tuple(row[0].a for row in mul(Ph,col([K(x) for x in v])))
    assert all(image(v) in long for v in short)
    assert all(tuple(x/2 for x in image(v)) in short for v in long)
    det=(K(256)+640*t)/27
    assert det*det.conj()==F(2**15,3**3)
    return {'short_root_count':len(short),'long_root_count':len(long),'Phi_interchanges_root_lengths':True,'involution_z':True,'four_simple_word_identities':True,'field_action_scalar':t.serial(),'character_trace':trace(mul(s0,g)).serial(),'period_minor_norm':str(F(2**15,3**3))}

if __name__=='__main__':
    out={'scope':__doc__,'g24':g24(),'gf4':gf4()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='scope'},indent=2))
