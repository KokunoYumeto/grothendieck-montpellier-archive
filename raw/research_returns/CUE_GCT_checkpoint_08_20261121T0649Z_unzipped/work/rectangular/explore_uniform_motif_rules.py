"""Bounded exploration of uniform type rules; no extrapolated theorem."""
from itertools import permutations
from pathlib import Path
import json
from explore_full_staircase import mul,add,linear
from check_simultaneous_chords import field_for,product_coefficients,rank_columns


def local(b,m,p,q,rule):
    L=[linear('L',pow(q,i,p),p) for i in range(b)]
    V=[linear('V',pow(q,i,p),p) for i in range(b)]
    motif={}
    for i in range(b):
      for j in range(b+1):
        if j in (i,i+1) or j==0 or (i==0 and j==b):continue
        typ=rule(i,j,b)
        if typ:motif[i,j]=linear(typ,(i*i+3*i+5*j+7)%p,p)
    def entry(i,j):return L[i] if j==i else V[i] if j==i+1 else motif.get((i,j),{})
    def es(B):
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
    ER=es([[entry(i,j) for j in range(1,b+1)] for i in range(1,b)])
    EC=es([[entry(i,j) for i in range(b)] for j in range(1,b)])
    rr=[add(mul(L[i],ER[i-1],p),mul(V[i],ER[i],p),p,-1) for i in range(1,b)]
    cc=[add(mul(V[i],EC[i],p),mul(L[i+1],EC[i+1],p),p,-1) for i in range(b-1)]
    def top(f):
      if not f:return 0,{}
      g=max(e[2]+e[3] for e in f);return g,{e:c for e,c in f.items() if e[2]+e[3]==g}
    return list(map(top,rr)),list(map(top,cc))


def test(b,rule):
 m=8*b;p,q=field_for(m);k=t=m//2
 roots=[pow(q,i,p) for i in range(m)];pairs=[(r,t-r) for r in range(m-k+1) if 0<=t-r<=k]
 aa=product_coefficients(range(k,m),roots,p);bb=product_coefficients(range(k-1),roots,p)
 base=[[aa[r]*(bb[s] if s<len(bb) else 0)%p for r,s in pairs],[aa[r]*(bb[s-1] if 1<=s<=len(bb) else 0)%p for r,s in pairs]]
 row,col=local(b,m,p,q,rule);out=[]
 for side,nn in [('R',row),('C',col)]:
  for g,F in nn:
   if side=='R':v=k+b-g;ai=[0]+list(range(v+1,m));bi=list(range(b,v))
   else:v=m+g-k;ai=list(range(b,v));bi=list(range(v,m))
   a1=product_coefficients(ai,roots,p);b1=product_coefficients(bi,roots,p)
   out.append([sum(c*a1[r-e[1]]*b1[s-e[3]] for e,c in F.items() if 0<=r-e[1]<len(a1) and 0<=s-e[3]<len(b1))%p for r,s in pairs])
 return {'rank':rank_columns(base+out,p)-rank_columns(base,p),'target':2*b-2,'grades':[[g for g,f in row],[g for g,f in col]]}

rules={
 'upperL_lowerV':lambda i,j,b:'L' if j>i else 'V',
 'upperV_lowerL':lambda i,j,b:'V' if j>i else 'L',
 'checkerboard':lambda i,j,b:'L' if (i+j)%2 else 'V',
 'row_alternating':lambda i,j,b:'L' if i%2 else 'V',
 'column_alternating':lambda i,j,b:'L' if j%2 else 'V',
 'diagonal_mod3':lambda i,j,b:'L' if (j-i)%3 else 'V',
 'row_mod3':lambda i,j,b:'L' if i%3 else 'V',
 'column_mod3':lambda i,j,b:'L' if j%3 else 'V',
}
results=[]
for b in [4,5,6,7]:
 for name,rule in rules.items():
  v=test(b,rule);v.update(b=b,rule=name);results.append(v);print(json.dumps(v),flush=True)
Path(__file__).with_name('uniform_motif_rule_exploration.json').write_text(json.dumps(results,indent=2)+'\n')
