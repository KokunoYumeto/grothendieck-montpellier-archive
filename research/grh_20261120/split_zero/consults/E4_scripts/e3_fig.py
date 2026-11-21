import os,sys
os.environ['HN']='3'; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'e3_reproduce.py')).read().split('w0=max')[0])
Q=sp.symbols('q')
def fq(p): return sp.factor(sp.simplify(tosym(p).subs(v,sp.sqrt(Q))))
for b2s in (1,-1):
    E={k:L.comb(t) for k,t in basis(b2s).items()}
    for k in ('g1_2','g2_2'):
        co=L.dualcoords(E[k]); vals=sorted({str(fq(p)) for p in co.values()})
        print(b2s,k,len(co),vals[:12])
