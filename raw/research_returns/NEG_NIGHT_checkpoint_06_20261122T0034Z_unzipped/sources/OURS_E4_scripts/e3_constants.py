# All multiplicative structure constants c(b,b';b'') of GCT VIII's E^opp(3), with b2 = -(q+1)^2/q (the sign matching VIII's Figure fw1w2)
import os,sys,json,random
os.environ['HN']='3'; here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
exec(open(os.path.join(here,'e3_reproduce.py')).read().split('w0=max')[0])
B=basis(-1); names=list(B); E={k:L.comb(B[k]) for k in names}
keys=sorted({k for X in E.values() for k in X},key=str)
M=sp.Matrix([[tosym(E[nm].get(k,{})) for nm in names] for k in keys])
# choose independent rows
Mn=M.subs(v,sp.Rational(7,5)); rows=[]
for i in range(len(keys)):
    if sp.Matrix([Mn.row(j) for j in rows+[i]]).rank()>len(rows): rows.append(i)
    if len(rows)==len(names): break
Ms=sp.Matrix([M.row(i) for i in rows]); Minv=Ms.inv(method='LU'); Minv=Minv.applyfunc(sp.cancel)
out=[]
for x in names:
    for y in names:
        P=L.rmul_comb(E[x],B[y])
        rhs=sp.Matrix([tosym(P.get(keys[i],{})) for i in rows])
        sol=(Minv*rhs).applyfunc(sp.cancel)
        # verify full product
        full=sp.Matrix([tosym(P.get(k,{})) for k in keys])-M*sol
        assert all(sp.cancel(z)==0 for z in full), (x,y)
        for k,c in zip(names,sol):
            if c!=0:
                r=classify(c); out.append({'b':x,'bp':y,'bpp':k,'c':str(sp.factor(c)),**{kk:(str(vv) if kk=='f' else vv) for kk,vv in r.items()}})
json.dump(out,open(os.path.join(here,'e3_constants.json'),'w'),indent=0)
from collections import Counter
print('nonzero constants:',len(out))
print('by a:',sorted(Counter(r['a'] for r in out).items()))
bad=[r for r in out if not (r['laurent'] and r['bar'] and r['nonneg'] and r['unimodal'])]
print('failing VIII form:',len(bad)); [print(r) for r in bad[:10]]
