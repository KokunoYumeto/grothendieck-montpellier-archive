"""R050: independent truncated-moment, finite-row and original plethysm checks."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict,Counter
from math import comb
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual,power_sum
HERE=Path(__file__).resolve().parent

def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)

def support_counts(s,D):
    dp={(0,0):1}
    for d in range(2,s+1):
        out=defaultdict(int)
        for (e,k),v in dp.items():
            for b in range((D-e)//d+1):out[e+b*d,k+(b>0)]+=v
        dp=out
    return dp

@lru_cache(None)
def complete_exterior(cyc,D):
    h=[1]+[0]*D
    for ell in cyc:
        for j in range(ell,D+1):h[j]+=h[j-ell]
    h=[h[j]-(h[j-1] if j else 0) for j in range(D+1)]
    e=[1]+[0]*D
    for ell in cyc:
        for j in range(D,ell-1,-1):e[j]+=(-1)**(ell+1)*e[j-ell]
    for j in range(1,D+1):e[j]-=e[j-1]
    return h,e

def finite_hook(s,t,r):
    D=t+r;value=F()
    for cyc in partitions(s):
        h,e=complete_exterior(cyc,D)
        tr=sum((-1)**j*h[t+j]*e[r-j] for j in range(r+1))
        value+=F(tr,z(cyc))
    assert value.denominator==1 and value>=0
    return int(value)

def main():
    rows=[]
    for s in range(1,11):
        dp=support_counts(s,30)
        for D in range(1,31):
            for r in range(D):
                t=D-r
                expected=sum(v*comb(k-1,r) for (e,k),v in dp.items()
                             if e==D and k>=r+1)
                got=finite_hook(s,t,r)
                assert got==expected,(s,t,r,got,expected)
                rows.append(dict(s=s,D=D,t=t,r=r,finite_cycle_JT=got,
                  formal_moment_support_count=expected,status='PASS'))
        print('checked finite-row hook faithfulness s',s,'cases',len(rows),flush=True)
    write('HOOK_MOMENT_FINITE_ROW_CHECK.tsv',rows)
    print('PASS finite-row hooks',len(rows),flush=True)
    rows=[]
    for D in range(2,13):
        for rho in partitions(D):
            if 1 in rho:continue
            term={():F(1)}
            for d,b in Counter(rho).items():
                nxt=defaultdict(F)
                for x,c in term.items():
                    for y,e in power_sum((b,),d).items():
                        nxt[tuple(sorted(x+y,reverse=True))]+=c*e
                term=nxt
            k=len(set(rho))
            for r in range(D):
                nu=(D-r,)+(1,)*r
                got=sum((c*character(nu,cyc) for cyc,c in term.items()),F())
                expected=comb(k-1,r) if r<k else 0
                assert got==expected,(rho,nu,got,expected)
                rows.append(dict(moment_degrees=','.join(map(str,rho)),tail=','.join(map(str,nu)),
                  cycle_index_MN=str(got),support_binomial=expected,status='PASS'))
    write('HOOK_MOMENT_MULTIDEGREE_CHECK.tsv',rows)
    print('PASS moment multidegrees',len(rows),flush=True)
    rows=[]
    for a in range(2,7):
        for n in range(a,7):
            for r in range(max(a,n)-1):
                for t in range(1,a*n//2+1):
                    if a*n-t-r<t:continue
                    lam=(a*n-t-r,t)+(1,)*r
                    x=actual((a,),n,lam);y=actual((n,),a,lam)
                    assert x==y,(a,n,t,r,lam,x,y)
                    rows.append(dict(a=a,n=n,t=t,r=r,output=','.join(map(str,lam)),
                      actual_target_MN=x,actual_source_MN=y,status='PASS'))
            print('checked original hook-tail reciprocity',a,n,'cases',len(rows),flush=True)
    write('HOOK_TAIL_RECIPROCITY_MN_CHECK.tsv',rows)
    print('PASS hook-tail reciprocity',len(rows),'positive',sum(q['actual_target_MN']>0 for q in rows),flush=True)

if __name__=='__main__':main()
