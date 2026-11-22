# Reproduce GCT VIII's E^opp(3) (TeX lines 1860-1880) and its structure constants; HN=3
import os,sys,itertools,json
os.environ['HN']='3'; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import e4lib as L, sympy as sp
from classify import classify, v
def lp(expr):  # sympy Laurent expr in v -> dict
    expr=sp.expand(expr*v**40); P=sp.Poly(expr,v)
    return {m[0]-40:int(c) for m,c in P.terms()}
def tosym(p): return sum(c*v**e for e,c in p.items())
q=v**2
c1=(q**6+2*q**5+3*q**4+4*q**3+3*q**2+2*q+1)/q**3; c2=(q**4+q**3+4*q**2+q+1)/q**2
b1=-(q**2+1)**2/q**2; b2=(q+1)**2/q
def basis(b2s):
    B={'Sigma':[(lp(c1),(1,)),(lp(-c2),(1,2,1)),({0:1},(1,2,1,2,1))],'mu':[({0:1},())]}
    for i,b in ((1,b1),(2,b2s*b2)):
        B[f'g{i}_1']=[(lp(b),(1,)),({0:1},(1,2,1))]
        B[f'g{i}_12']=[(lp(b),(1,2)),({0:1},(1,2,1,2))]
        B[f'g{i}_2']=[(lp(b),(2,)),({0:1},(2,1,2))]
        B[f'g{i}_21']=[(lp(b),(2,1)),({0:1},(2,1,2,1))]
    return B
w0=max(L.G,key=L.length)
for b2s in (1,-1):
    B=basis(b2s); E={k:L.comb(t) for k,t in B.items()}
    neg={k:sum(1 for p in L.dualcoords(X).values() if any(c<0 for c in p.values())) for k,X in E.items()}
    print('b2 sign',b2s,': C(x)C coords with a negative coefficient, per element:',neg)
# Sigma vs C'_w0 (x) C'_w0
B=basis(1); Sig=L.comb(B['Sigma']); W=L.tensorCp(w0,w0)
keys=set(Sig)|set(W)
ratios={tuple(sorted(Sig.get(k,{}).items())) for k in keys}
num=sp.cancel(tosym(Sig[(w0,w0)])/tosym(W[(w0,w0)]))
prop=all(sp.cancel(tosym(Sig.get(k,{}))-num*tosym(W.get(k,{})))==0 for k in keys)
print('Sigma proportional to C\'_w0 (x) C\'_w0:',prop,' factor',sp.factor(num))
