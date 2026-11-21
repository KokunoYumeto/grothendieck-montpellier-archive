"""Exploratory second-order normals of full finite staircase motifs."""
from itertools import permutations
from pathlib import Path
import json, random
from check_simultaneous_chords import field_for, product_coefficients, rank_columns


def mul(a,b,p):
    c={}
    for e,x in a.items():
      for f,y in b.items():
        g=tuple(e[i]+f[i] for i in range(4));c[g]=(c.get(g,0)+x*y)%p
    return {g:x for g,x in c.items() if x}

def add(a,b,p,scale=1):
    c=dict(a)
    for e,x in b.items():c[e]=(c.get(e,0)+scale*x)%p
    return {e:x for e,x in c.items() if x}

def linear(kind,root,p):
    if kind=='L':return {(1,0,0,0):1,(0,1,0,0):-root%p}
    return {(0,0,1,0):1,(0,0,0,1):-root%p}


def local_normals(b,m,p,q,seed=5, mixed=False):
    rng=random.Random(seed);roots=[pow(q,i,p) for i in range(m)]
    L=[linear('L',roots[i],p) for i in range(b)]
    V=[linear('V',roots[i],p) for i in range(b)]
    motif={}
    for i in range(b):
      for j in range(b+1):
        if j in (i,i+1):continue
        if j==0 or (i==0 and j==b):continue
        motif[i,j]=linear(rng.choice(['L','V']) if mixed else 'V',rng.randrange(1,p),p)
    def E_second(B):
        r=len(B);E=[]
        for missing in range(r+1):
            cols=[j for j in range(r+1) if j!=missing];out={}
            for pp in permutations(range(r)):
                image=[cols[pp[i]] for i in range(r)]
                off=[(i,j) for i,j in enumerate(image) if j not in (i,i+1)]
                if len(off)!=2 or any(not B[i][j] for i,j in off):continue
                inv=sum(pp[i]>pp[j] for i in range(r) for j in range(i+1,r))
                parity=inv+sum((j-i-1 if j>i+1 else i-j) for i,j in off)
                if not parity%2:continue
                term={(0,0,0,0):2}
                for i,j in enumerate(image):term=mul(term,B[i][j],p)
                out=add(out,term,p)
            E.append(out)
        return E
    def entry(i,j):
        if i==j:return L[i]
        if j==i+1:return V[i]
        return motif.get((i,j),{})
    BR=[[entry(i,j) for j in range(1,b+1)] for i in range(1,b)]
    BC=[[entry(i,j) for i in range(b)] for j in range(1,b)]
    ER=E_second(BR);EC=E_second(BC)
    row=[add(mul(L[i],ER[i-1],p),mul(V[i],ER[i],p),p,-1) for i in range(1,b)]
    col=[add(mul(V[i],EC[i],p),mul(L[i+1],EC[i+1],p),p,-1) for i in range(b-1)]
    def top(a):
        g=max(e[2]+e[3] for e in a)
        return g,{e:x for e,x in a.items() if e[2]+e[3]==g}
    return list(map(top,row)),list(map(top,col)),motif


def cols(m,b,k,t,p,q,seed,mixed=False):
    roots=[pow(q,i,p) for i in range(m)]
    pairs=[(r,t-r) for r in range(m-k+1) if 0<=t-r<=k]
    A=product_coefficients(range(k,m),roots,p);B=product_coefficients(range(k-1),roots,p)
    base=[[A[r]*(B[s] if s<len(B) else 0)%p for r,s in pairs],
          [A[r]*(B[s-1] if 1<=s<=len(B) else 0)%p for r,s in pairs]]
    row,col,motif=local_normals(b,m,p,q,seed,mixed)
    out=[]
    for side,nn in [('R',row),('C',col)]:
        for g,F in nn:
            if side=='R':
                s=k+b-g
                ai=[0]+list(range(s+1,m));bi=list(range(b,s))
            else:
                c=m+g-k
                ai=list(range(b,c));bi=list(range(c,m))
            aa=product_coefficients(ai,roots,p);bb=product_coefficients(bi,roots,p)
            out.append([sum(co*aa[r-e[1]]*bb[s-e[3]] for e,co in F.items()
                            if 0<=r-e[1]<len(aa) and 0<=s-e[3]<len(bb))%p for r,s in pairs])
    return base,out,[[g for g,f in row],[g for g,f in col]]


def main():
    data=[]
    for b in [4,5,6]:
        m=6*b;p,q=field_for(m);k=t=m//2
        for seed in range(1,20):
            base,normal,grades=cols(m,b,k,t,p,q,seed)
            rr=rank_columns(base+normal,p)-rank_columns(base,p)
            data.append({'b':b,'m':m,'p':p,'q':q,'seed':seed,'normal_rank':rr,'grades':grades})
            print(json.dumps(data[-1]),flush=True)
            if rr==2*b-2:break
    Path(__file__).with_name('full_staircase_exploration.json').write_text(json.dumps(data,indent=2)+'\n')

if __name__=='__main__':main()
