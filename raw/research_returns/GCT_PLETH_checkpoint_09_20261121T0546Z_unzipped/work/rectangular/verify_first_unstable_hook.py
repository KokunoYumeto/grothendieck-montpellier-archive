"""T061 independent literal plethysms and original hook/induction traces."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import prod
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
HERE=Path(__file__).resolve().parent

@lru_cache(None)
def standard_power(cyc,k):
    return sum(d for d in cyc if k%d==0)-1

@lru_cache(None)
def schur_standard(shape,cyc):
    result=F()
    for rho in partitions(sum(shape)):
        ch=character(shape,rho)
        if ch:
            result+=F(ch*prod(standard_power(cyc,k) for k in rho),z(rho))
    assert result.denominator==1
    return int(result)

@lru_cache(None)
def deleted_exterior(cyc,r):
    # Induction is the literal sum over fixed deleted points.
    if 1 not in cyc:
        return 0
    remaining=list(cyc);remaining.remove(1)
    return cyc.count(1)*schur_standard((1,)*r,tuple(remaining))

def main():
    rows=[]
    for m in (4,5,6):
        for a in (2,3,4):
            for r in range(m-1):
                if (m-2)*a<m+r:
                    continue
                for t in (0,1):
                    n=a+t-1
                    lam=((m-1)*a+t-m-r,a+t)+(t+1,)*r+(t,)*(m-2-r)
                    assert sum(lam)==m*n and min(lam)>=0 and sorted(lam,reverse=True)==list(lam)
                    hook=(a,)+(1,)*r
                    for mu in partitions(m):
                        value=F()
                        for cyc in partitions(m):
                            tr=schur_standard(hook,cyc)-deleted_exterior(cyc,r)
                            tr*=(-1)**((m-len(cyc))*t)
                            value+=F(character(mu,cyc)*tr,z(cyc))
                        assert value.denominator==1 and value>=0,(m,a,r,t,mu,value)
                        got=actual(mu,n,lam)
                        assert got==value,(m,a,r,t,mu,lam,got,value)
                        if a==2:
                            label=(m-r-2,2)+(1,)*r
                            eff=tuple(sum(v>=k for v in mu) for k in range(1,max(mu)+1)) if t%2 else mu
                            assert got==int(eff==label),(m,r,t,mu,label,got)
                        rows.append(dict(m=m,a=a,r=r,t=t,n=n,outer=','.join(map(str,mu)),
                          output=','.join(map(str,lam)),actual_MN=got,
                          independent_hook_minus_point_trace=int(value),status='PASS'))
        print('completed first unstable hook m',m,'cases',len(rows),flush=True)
    with (HERE/'FIRST_UNSTABLE_HOOK_MN_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS first unstable hook',len(rows),flush=True)
if __name__=='__main__':main()

