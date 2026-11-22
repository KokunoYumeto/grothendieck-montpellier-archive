# Cross-check every structure constant from e3_fast.py against the tensor realization in H_3 (x) H_3, at exact v = 2 and v = 3/7
import os,sys,json
os.environ['HN']='3'; here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
import e4lib as L, sympy as sp
from fractions import Fraction as Fr
v=sp.symbols('v')
exec(open(os.path.join(here,'e3_fast.py')).read().split('names=list(B)')[0].split("B={'Sigma'")[0])
src=open(os.path.join(here,'e3_fast.py')).read()
exec("B={'Sigma'"+src.split("B={'Sigma'")[1].split('names=list(B)')[0])
names=list(B)
R=json.load(open(os.path.join(here,'e3_constants.json')))
def ev(p,x): return sum(Fr(c)*x**e for e,c in p.items())
def tens_of(nm,x):
    X={}
    for w,c in B[nm].items():
        cv=Fr(str(sp.nsimplify(sp.sympify(c).subs(v,sp.Rational(x.numerator,x.denominator)))))
        for k,p in L.word_elt(w).items(): X[k]=X.get(k,0)+cv*ev(p,x)
    return X
bad=0
for x in (Fr(2),Fr(3,7)):
    T={nm:tens_of(nm,x) for nm in names}
    for b in names:
        for bp in names:
            # product as tensor: T[b] * (element bp): multiply T[b] (numeric) by word elements of bp
            P={}
            Xb={k:{0:1} for k in []}
            # numeric product: use L.tmulP on a Laurent-free representation: wrap numbers as constant 'polys'
            for w,c in B[bp].items():
                cv=Fr(str(sp.nsimplify(sp.sympify(c).subs(v,sp.Rational(x.numerator,x.denominator)))))
                Y={k:{0:val} for k,val in T[b].items()}  # treat numbers as constant Laurent polys (Fractions allowed)
                for i in w: Y=L.tmulP(Y,L.S[i-1])
                for k,p in Y.items(): P[k]=P.get(k,0)+cv*ev(p,x)
            Q={}
            for r in R:
                if r['b']==b and r['bp']==bp:
                    cv=Fr(str(sp.nsimplify(sp.sympify(r['c']).subs(v,sp.Rational(x.numerator,x.denominator)))))
                    for k,val in T[r['bpp']].items(): Q[k]=Q.get(k,0)+cv*val
            diff={k:P.get(k,0)-Q.get(k,0) for k in set(P)|set(Q)}
            if any(d!=0 for d in diff.values()): bad+=1; print('MISMATCH',b,bp,x)
print('products checked: 2 x',len(names)**2,'mismatches:',bad)
