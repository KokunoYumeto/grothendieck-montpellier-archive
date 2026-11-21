"""Literal cycle-index/MN audit of T047; reconstruct the pair stabilizer sum."""
from pathlib import Path
from functools import lru_cache
from math import comb
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
from verify_outer5_fivepoint_family import sym_standard
from verify_outer5_two_row_bundle import schur_two

HERE=Path(__file__).resolve().parent


def pair_trace(rest,swapped,x,b,s):
    total=0
    for j in range(s-1):
        for u in range(min(x,s-2-j)+1):
            for v in range(min(b,s-2-j-u)+1):
                q=s-j-u-v-2
                p_trace=int(q%2==0) if swapped else q+1
                det_trace=(-1)**(u+v+1) if swapped else 1
                total+=det_trace*p_trace*sym_standard(rest,j)*schur_two(rest,b+x-u,b-v)
    return total


def induced_correction(cyc,x,b,s):
    """Sum over fixed unordered pairs, with their literal two-letter action."""
    total=0
    if cyc.count(1)>=2:
        rest=list(cyc);rest.remove(1);rest.remove(1)
        total+=comb(cyc.count(1),2)*pair_trace(tuple(rest),False,x,b,s)
    if cyc.count(2):
        rest=list(cyc);rest.remove(2)
        total+=cyc.count(2)*pair_trace(tuple(rest),True,x,b,s)
    return total


@lru_cache(None)
def expected(mu,x,b,k,d,s):
    c=2*k-s;result=0
    for cyc in partitions(5):
        jet=cyc.count(1)*sym_standard(cyc,k-1)
        s0=schur_two(cyc,b+x,b)
        s1=schur_two(cyc,b+x-1,b)+schur_two(cyc,b+x,b-1)
        s2=schur_two(cyc,b+x-1,b-1)
        trace=s0*(sym_standard(cyc,c)-jet)-s1*(sym_standard(cyc,c-1)-jet)+s2*(sym_standard(cyc,c-2)-jet)
        trace+=induced_correction(cyc,x,b,s)
        trace*=(-1)**((5-len(cyc))*(d+b+x))
        result+=(120//z(cyc))*character(mu,cyc)*trace
    assert result%120==0 and result>=0,(mu,x,b,k,d,s,result)
    return result//120


def main():
    rows=[]
    for s,nmax in [(3,7),(4,8)]:
        for n in range(nmax+1):
            for k in range(3*s-1,n+s+1):
                for b in range(n+s-k+1):
                    for x in range(n+s-k-b+1):
                        d=n+s-k-b-x
                        if 2*b+x+k<3*s:continue
                        lam=(d+3*b+2*x+3*k-4*s,d+b+x+2*k-s,d+b+x,d+x,d)
                        assert sum(lam)==5*n and min(lam)>=0 and tuple(sorted(lam,reverse=True))==lam
                        for mu in partitions(5):
                            value=actual(mu,n,lam);formula=expected(mu,x,b,k,d,s)
                            assert value==formula,(s,n,x,b,k,d,mu,lam,value,formula)
                            rows.append(dict(s=s,n=n,x=x,b=b,k=k,d=d,outer=','.join(map(str,mu)),output=','.join(map(str,lam)),cycle_index_MN=value,directional_pair_trace=formula,status='PASS'))
            print('completed s,n',s,n,'cases',len(rows),flush=True)
    with (HERE/'OUTER5_STABLE_DEFECT_INDEPENDENT_CHECK.tsv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t');writer.writeheader();writer.writerows(rows)
    print('PASS',len(rows),'stable-defect actual plethysms')


if __name__=='__main__':main()
