# The trivial-block element Sigma_r of nsH_r (x * P_i = D x for all i), at exact rational v; signs of its C(x)C coordinates.
import os,sys
from fractions import Fraction as Fr
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
import e4lib as L
exec(open(os.path.join(here,'dims.py')).read().split('r=L.n')[0])
def ev(p,x): return sum(Fr(c)*x**e for e,c in p.items())
def nullvec(rows,ncols):
    # rows: list of dict col->Fr ; returns one nonzero null vector (dict) or None
    piv={}; R=[]
    for row in rows:
        row=dict(row)
        for pc,(r) in list(piv.items()):
            if row.get(pc,0)!=0:
                f=row[pc]/r[pc]
                for k,val in r.items(): row[k]=row.get(k,0)-f*val
                row={k:val for k,val in row.items() if val!=0}
        if row:
            pc=next(iter(row));
            # eliminate pc from existing rows (reduced echelon)
            for qc in list(piv):
                r=piv[qc]
                if r.get(pc,0)!=0:
                    f=r[pc]/row[pc]
                    for k,val in row.items(): r[k]=r.get(k,0)-f*val
                    piv[qc]={k:val for k,val in r.items() if val!=0}
            piv[pc]=row
    free=[j for j in range(ncols) if j not in piv]
    return free,piv
def run(x):
    _,elts=rank_words(Fr(2))
    words=list(elts)
    D=(x+1/x)**2
    # columns = word coefficients; equations: for each i and each tensor key, sum_j c_j (w_j P_i - D w_j)[key] = 0
    eqs={}
    for j,w in enumerate(words):
        Xw=elts[w]
        for i in range(1,len(L.S)+1):
            Y=L.tmulP(Xw,L.S[i-1])
            for k in set(Y)|set(Xw):
                val=ev(Y.get(k,{}),x)-D*ev(Xw.get(k,{}),x)
                if val!=0: eqs.setdefault((i,k),{})[j]=val
    free,piv=nullvec(list(eqs.values()),len(words))
    assert len(free)==1, ('null space dim',len(free))
    fj=free[0]; c={fj:Fr(1)}
    for pc,row in piv.items():
        c[pc]=-row.get(fj,0)/row[pc]
    S={}
    for j,cj in c.items():
        if cj==0: continue
        for k,p in elts[words[j]].items(): S[k]=S.get(k,0)+cj*ev(p,x)
    # C(x)C coordinates at x: convert via Tinv evaluated
    co={}
    for (a,b),val in S.items():
        if val==0: continue
        for y,p in L.Tinv[a].items():
            for z,qq in L.Tinv[b].items():
                co[(y,z)]=co.get((y,z),0)+val*ev(p,x)*ev(qq,x)*(-1)**(L.length(y)+L.length(z))
    vals=[t for t in co.values() if t!=0]
    pos=sum(1 for t in vals if t>0); neg=len(vals)-pos
    return len(vals),pos,neg
for x in (Fr(2),Fr(3,2)):
    print('r=',L.n,'v=',x,'nonzero C(x)C coords, positive, negative:',run(x)); sys.stdout.flush()
