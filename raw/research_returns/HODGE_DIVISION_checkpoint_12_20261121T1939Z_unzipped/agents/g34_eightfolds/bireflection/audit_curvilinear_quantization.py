#!/usr/bin/env python3
"""Independent E820 Pluecker/Leibniz and full exterior-character checks."""
from pathlib import Path
from itertools import permutations
from math import factorial
import hashlib,json
import sympy as s

def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
g=s.symbols('a0:16');q=s.symbols('q');G=[list(g[4*i:4*i+4]) for i in range(4)]
det=sum(sign(p)*s.prod(G[i][p[i]] for i in range(4)) for p in permutations(range(4)))
def minor(i,j,a,b):return q**((i==0)+(j==0))*(G[i][a]*G[j][b]-G[i][b]*G[j][a])
p={(i,j):minor(i,j,0,1) for i in range(4) for j in range(i+1,4)}
r={(i,j):minor(i,j,2,3) for i in range(4) for j in range(i+1,4)}
def pairing(p,r):
    return (p[0,1]*r[2,3]+p[2,3]*r[0,1]-p[0,2]*r[1,3]
            -p[1,3]*r[0,2]+p[0,3]*r[1,2]+p[1,2]*r[0,3])
assert s.expand(pairing(p,p))==0
assert s.expand(pairing(r,r))==0
assert s.expand(pairing(p,r)-q*det)==0

def clean(a):return {k:s.simplify(v) for k,v in a.items() if s.simplify(v)!=0}
def add(*xs):
    a={}
    for x in xs:
        for k,v in x.items():a[k]=a.get(k,0)+v
    return clean(a)
def scale(a,c):return clean({k:c*v for k,v in a.items()})
def wedge(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():
            if i&j:continue
            inv=sum((j&((1<<k)-1)).bit_count() for k in range(8) if i>>k&1)
            c[i|j]=c.get(i|j,0)+(-1)**inv*x*y
    return clean(c)
def exp(a):
    out={0:1};power={0:1}
    for k in range(1,5):power=wedge(power,a);out=add(out,scale(power,s.Rational(1,factorial(k))))
    return out
def theta(H):
    return add(*[scale(wedge({1<<(2*i):1},{1<<(2*j+1):1}),H[i,j]) for i in range(4) for j in range(4)])
U=s.diag(s.Matrix([[1,1],[1,-1]]),s.Matrix([[1,1],[1,-1]]))
S=s.diag(1,1,-1,-1);Id=s.eye(4)
tp=theta((Id+U/s.sqrt(2))/2);tm=theta((Id-U/s.sqrt(2))/2)
X=theta(S);Y=theta(U*S);Zp=add(X,Y);Zm=add(X,scale(Y,-1))
H=add({0:24},scale(add(exp(X),exp(scale(X,-1))),2),
      exp(Zp),exp(scale(Zp,-1)),exp(Zm),exp(scale(Zm,-1)))
v=wedge(add({0:1},scale(wedge(tp,tp),s.Rational(-1,4))),
        add({0:1},scale(wedge(tm,tm),s.Rational(-1,4))))
assert H==scale(v,32)
assert H[0]==32 and H[255]==8 and wedge(H,H)[255]==1024
proof=Path(__file__).resolve().parents[2]/'sixfolds/rm_curvilinear_quantization_obstruction_draft.md'
out={'status':'PASS','proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
     'method':'own 2x2 minors and24-term Leibniz determinant; full256-coordinate exterior algebra',
     'generic_variables':16,'mixed_identity':'Pplus wedge Pminus=q detG',
     'both_self_wedges_zero':True,'rank':32,'top_character_integral':8,'self_Euler':1024,
     'entire_character':{str(k):str(v) for k,v in H.items()},
     'extension_dimension':'6*m*m*ell','author_code_imported':False,
     'scope':'exact formal identities and actual example; universal lifting/unit/socle proof audited separately'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='entire_character'},indent=2))
