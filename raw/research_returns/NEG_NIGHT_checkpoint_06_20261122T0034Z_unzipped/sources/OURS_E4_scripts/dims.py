# dim of nsH_r generic (v=2) and at v=1, from P-words in H_r (x) H_r; HN=r
import os,sys
from fractions import Fraction as Fr
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
import e4lib as L
def ev(p,x): return sum(Fr(c)*x**e for e,c in p.items())
def rank_words(x,maxlen=30):
    keys={}; basis=[]  # echelon rows: dict col->Fr with pivot
    piv=[]
    words=[()]; elts={():L.ONE_T}; frontier=[()]; count=0
    def reduce(vec):
        for (pc,row) in piv:
            if vec.get(pc,0)!=0:
                f=vec[pc]/row[pc]
                for k,val in row.items(): vec[k]=vec.get(k,0)-f*val
                vec={k:val for k,val in vec.items() if val!=0}
        return vec
    def add(X):
        vec={k:ev(p,x) for k,p in X.items()}; vec={k:val for k,val in vec.items() if val!=0}
        vec=reduce(vec)
        if vec:
            pc=next(iter(vec)); piv.append((pc,vec)); return True
        return False
    add(L.ONE_T); length=0
    while frontier and length<maxlen:
        nf=[]
        for w in frontier:
            for i in range(1,len(L.S)+1):
                if w and w[-1]==i: continue
                nw=w+(i,); X=L.tmulP(elts[w],L.S[i-1])
                if add(X): elts[nw]=X; nf.append(nw)
        frontier=nf; length+=1
    return len(piv), elts
r=L.n
d2,elts=rank_words(Fr(2))
print('r=',r,'dim at v=2:',d2)
# at v=1 use the same spanning words
def rank_at(x,elts):
    piv=[]
    for X in elts.values():
        vec={k:Fr(sum(c*x**e for e,c in p.items())) for k,p in X.items()}; vec={k:val for k,val in vec.items() if val!=0}
        for (pc,row) in piv:
            if vec.get(pc,0)!=0:
                f=vec[pc]/row[pc]
                for k,val in row.items(): vec[k]=vec.get(k,0)-f*val
                vec={k:val for k,val in vec.items() if val!=0}
        if vec: piv.append((next(iter(vec)),vec))
    return len(piv)
print('dim of the span of these words at v=1:',rank_at(Fr(1),elts),' (number of words kept:',len(elts),')')
