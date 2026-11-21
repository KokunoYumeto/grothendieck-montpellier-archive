"""Independent arbitrary-outer-Schur end-sector checks."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from functools import lru_cache
import csv
from verify_rectangular import partitions,z,character

HERE=Path(__file__).resolve().parent

def transpose(lam):
    return tuple(sum(x>=j for x in lam) for j in range(1,max(lam,default=0)+1))

@lru_cache(None)
def plethysm(mu,n):
    result=defaultdict(Fraction)
    for rho in partitions(sum(mu)):
        ch=character(mu,rho)
        if not ch:continue
        term={():Fraction(ch,z(rho))}
        for k in rho:
            nxt=defaultdict(Fraction)
            for old,c in term.items():
                for beta in partitions(n):
                    cyc=tuple(sorted(old+tuple(k*j for j in beta),reverse=True))
                    nxt[cyc]+=c/z(beta)
            term=nxt
        for cyc,c in term.items():result[cyc]+=c
    return dict(result)

@lru_cache(None)
def comaj_values(lam):
    m=sum(lam);r=len(lam);values=[]
    def visit(shape,rows):
        if len(rows)==m:
            values.append(sum(m-i for i in range(1,m) if rows[i]>rows[i-1]))
            return
        for i in range(r):
            if shape[i]<lam[i] and (i==0 or shape[i]<shape[i-1]):
                z=list(shape);z[i]+=1;visit(tuple(z),rows+(i,))
    visit((0,)*r,())
    return tuple(values)

@lru_cache(None)
def restricted_parts(m,R):
    if R<0:return 0
    dp=[1]+[0]*R
    for k in range(2,m+1):
        for j in range(k,R+1):dp[j]+=dp[j-k]
    return dp[R]

rows=[]
for m,maxn in [(3,4),(4,3)]:
 for n in range(maxn+1):
  for beta in range(m*n//(m-1)+1):
   for gamma in range(beta+1):
    alpha=m*n-(m-2)*beta-gamma
    if alpha<beta:continue
    lam=(alpha,)+(beta,)*(m-2)+(gamma,)
    S=beta-gamma-m*max(0,beta-n)
    for mu in partitions(m):
     actual=sum((c*character(tuple(x for x in lam if x),cyc)
                 for cyc,c in plethysm(mu,n).items()),Fraction())
     assert actual.denominator==1
     nu=transpose(mu) if beta%2 else mu
     expected=sum(restricted_parts(m,S-c) for c in comaj_values(nu))
     assert actual==expected,(m,n,mu,lam,actual,expected)
     minimum=sum(i*row for i,row in enumerate(nu))
     corners=sum(nu[i]>(nu[i+1] if i+1<len(nu) else 0) for i in range(len(nu)))
     Q=S-minimum
     support=Q==0 or Q>=2 or (Q==1 and corners>=2)
     assert (actual>0)==support,(m,n,mu,lam,actual,Q,corners)
     rows.append(dict(m=m,n=n,outer_partition=','.join(map(str,mu)),
                      output_partition=','.join(map(str,lam)),S=S,
                      cycle_index_MN=int(actual),tableau_polytope=expected,status='PASS'))
with (HERE/'ENDSECTOR_SCHUR_INDEPENDENT_CHECK.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print('PASS arbitrary-outer-Schur end sector:',len(rows),'coefficient cases')
