"""T065/T066: original cycle-index/MN against literal hook and subset traces."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import csv
from verify_rectangular import partitions, character, z
from verify_outer4_chambers import actual
from verify_first_unstable_hook import schur_standard
from verify_higher_unstable_hook import symmetric_permutation

HERE = Path(__file__).resolve().parent

def jet(cyc,k,r):
    result=0
    for index,ell in enumerate(cyc):
        if ell==1:
            rem=cyc[:index]+cyc[index+1:]
            result+=symmetric_permutation(rem,k-1)*schur_standard((1,)*r,rem)
    return result

def pair(cyc,r):
    if r==0:return 0
    value=0
    # A fixed two-subset consists of one actual 2-cycle or two actual fixed points.
    for size in (1,2):
        for indexes in combinations(range(len(cyc)),size):
            if sum(cyc[i] for i in indexes)!=2:continue
            rem=tuple(x for i,x in enumerate(cyc) if i not in indexes)
            value+=schur_standard((1,)*(r-1),rem)
    return value

def check(statement,parameters):
    rows=[]
    for m,k in parameters:
        a=2*k-(statement=='T066')
        for r in range(m-1):
            if (m-2)*a<m*k+r:continue
            for t in (0,1):
                n=a+t-k
                lam=((m-1)*a+t-m*k-r,a+t)+(t+1,)*r+(t,)*(m-2-r)
                assert sum(lam)==m*n and min(lam)>=0 and sorted(lam,reverse=True)==list(lam)
                for mu in partitions(m):
                    value=F()
                    for cyc in partitions(m):
                        trace=schur_standard((a,)+(1,)*r,cyc)-jet(cyc,k,r)
                        if statement=='T066':trace+=pair(cyc,r)
                        trace*=(-1)**((m-len(cyc))*t)
                        value+=F(character(mu,cyc)*trace,z(cyc))
                    assert value.denominator==1 and value>=0,(statement,m,k,r,t,mu,value)
                    got=actual(mu,n,lam)
                    assert got==value,(statement,m,k,r,t,mu,lam,got,value)
                    rows.append(dict(statement=statement,m=m,k=k,a=a,r=r,t=t,n=n,
                      outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                      actual_MN=got,independent_hook_jet_subset_trace=int(value),status='PASS'))
        print('completed',statement,m,k,'cases',len(rows),flush=True)
    filename='HOOK_JET_ENDPOINT_MN_CHECK.tsv' if statement=='T065' else 'HOOK_JET_PAIR_ENDPOINT_MN_CHECK.tsv'
    with (HERE/filename).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS',statement,len(rows),'pair-active',sum(z['r']>0 for z in rows),flush=True)

if __name__=='__main__':
    check('T065',[(m,k) for m in (4,5,6) for k in (2,3)])
    check('T066',[(5,4),(5,5),(6,3),(6,4),(7,2),(7,3)])
