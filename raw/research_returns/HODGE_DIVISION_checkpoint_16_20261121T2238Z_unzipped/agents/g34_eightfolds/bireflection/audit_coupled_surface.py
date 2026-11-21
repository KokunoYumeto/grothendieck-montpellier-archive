#!/usr/bin/env python3
"""Independent E822 first-jet matrix and exterior norm certificate."""
from pathlib import Path
from itertools import permutations
import hashlib,json,time
import sympy as s

start=time.time()
f,g=s.symbols('f g')
df=s.symbols('f0:4');dg=s.symbols('g0:4')
p=s.symbols('p01 p02 p03 p12 p13 p23')
pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
P=sum(c*(df[i]*dg[j]-df[j]*dg[i]) for c,(i,j) in zip(p,pairs))
records=[]
for m in (1,2,3):
    Es=s.symbols('e0:'+str(m*m));E=s.Matrix(m,m,Es)
    derivatives=[s.Matrix(m,m,s.symbols('u'+str(k)+'_0:'+str(m*m))) for k in range(4)]
    I=s.eye(m);O=s.zeros(m)
    # Construct value and first-jet matrices independently of symbolic functions.
    D=s.zeros(3*m);F=s.zeros(3*m,m)
    jetsD=[s.zeros(3*m) for _ in range(4)]
    jetsF=[s.zeros(3*m,m) for _ in range(4)]
    D[:m,:m]=-g*I;D[m:2*m,:m]=f*I
    D[2*m:,:m]=-E;D[2*m:,m:2*m]=f*I;D[2*m:,2*m:]=g*I
    F[m:2*m,:]=-g*I;F[2*m:,:]=f*I
    for k in range(4):
        jetsD[k][:m,:m]=-dg[k]*I;jetsD[k][m:2*m,:m]=df[k]*I
        jetsD[k][2*m:,:m]=-derivatives[k]
        jetsD[k][2*m:,m:2*m]=df[k]*I;jetsD[k][2*m:,2*m:]=dg[k]*I
        jetsF[k][m:2*m,:]=-dg[k]*I;jetsF[k][2*m:,:]=df[k]*I
    assert D*F==s.zeros(3*m,m)
    C=s.zeros(3*m,m)
    for c,(i,j) in zip(p,pairs):C+=c*(jetsD[i]*jetsF[j]-jetsD[j]*jetsF[i])/2
    C=s.expand(C)
    target=s.zeros(3*m,m);target[2*m:,:]=-P*I
    assert all(s.expand(v)==0 for v in C-target)
    assert not C.free_symbols.intersection(set(Es)|set().union(*(d.free_symbols for d in derivatives)))
    H1=s.Matrix(3*m,3*m,s.symbols('a0:'+str(9*m*m)))
    H2=s.Matrix(3*m,m,s.symbols('b0:'+str(3*m*m)))
    correction=(D*H2+H1*F).subs({f:0,g:0})
    reduced=s.zeros(3*m,m);reduced[2*m:,:]=-E*H2[:m,:]
    assert correction==reduced
    records.append({'rank':m,'ordinary_square_zero':True,'star_square':'bottom -P I',
                    'extension_derivatives_absent':True,'reduced_correction':'bottom -E A'})

# Independent alternating-tuple exterior multiplication. This is not
# the author's bitmask implementation.
def canonical(word):
    if len(set(word))!=len(word):return None,0
    parity=sum(word[i]>word[j] for i in range(len(word)) for j in range(i+1,len(word)))
    return tuple(sorted(word)),(-1)**parity
def wedge(a,b):
    out={}
    for u,x in a.items():
        for v,y in b.items():
            key,sgn=canonical(u+v)
            if sgn:out[key]=s.expand(out.get(key,0)+sgn*x*y)
    return {k:v for k,v in out.items() if v!=0}
theta={(2*j,2*j+1):s.I for j in range(4)}
theta2=wedge(theta,theta)
forms=[{(0,2):1},{(4,6):1}]
conjugates=[{(1,3):1},{(5,7):1}]
gram=s.Matrix([[wedge(wedge(u,v),theta2).get(tuple(range(8)),0)
                for v in conjugates] for u in forms])
assert gram==2*s.eye(2)
tp={(0,1):s.I,(2,3):s.I};tm={(4,5):s.I,(6,7):s.I}
assert wedge(wedge(tp,tp),wedge(tm,tm))[tuple(range(8))]==4

proof=Path(__file__).resolve().parents[2]/'sixfolds/rm_coupled_surface_obstruction_draft.md'
out={'status':'PASS','proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
     'method':'reviewer first-jet matrices and tuple-permutation exterior algebra',
     'local_records':records,'normal_bivector_parameters':6,'norm_gram':str(gram),
     'author_code_imported':False,'seconds':round(time.time()-start,3),
     'scope':'universal local matrix/exterior identities only; sheaf exactness, local lifting, gluing, slope and coherent-action implications audited mathematically'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
