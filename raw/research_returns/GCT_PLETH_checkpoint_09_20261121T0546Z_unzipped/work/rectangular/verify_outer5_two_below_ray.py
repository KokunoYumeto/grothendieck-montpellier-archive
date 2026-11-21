"""Independent actual plethysm checks for T046, including induced line correction."""
from pathlib import Path
from functools import lru_cache
from math import comb
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
from verify_outer5_fivepoint_family import sym_standard
from verify_outer5_two_row_bundle import schur_two

HERE=Path(__file__).resolve().parent


def induced_correction(cyc,x,b):
    """Literal sum over stable two-subsets; the complement carries h3."""
    result=0;m1=cyc.count(1);m2=cyc.count(2)
    if m1>=2:
        rest=list(cyc);rest.remove(1);rest.remove(1)
        result+=comb(m1,2)*schur_two(tuple(rest),b+x,b)
    if m2:
        rest=list(cyc);rest.remove(2)
        result-=m2*schur_two(tuple(rest),b+x,b)
    return result


@lru_cache(None)
def expected(mu,x,b,k,d):
    c=2*k-2;result=0
    for cyc in partitions(5):
        J=cyc.count(1)*sym_standard(cyc,k-1)
        S0=schur_two(cyc,b+x,b)
        S1=schur_two(cyc,b+x-1,b)+schur_two(cyc,b+x,b-1)
        S2=schur_two(cyc,b+x-1,b-1)
        trace=S0*(sym_standard(cyc,c)-J)-S1*(sym_standard(cyc,c-1)-J)+S2*(sym_standard(cyc,c-2)-J)
        trace+=induced_correction(cyc,x,b)
        trace*=(-1)**((5-len(cyc))*(d+b+x))
        result+=(120//z(cyc))*character(mu,cyc)*trace
    assert result%120==0 and result>=0,(mu,x,b,k,d,result)
    return result//120


def main():
    rows=[]
    for n in range(7):
        for k in range(5,n+3):
            for b in range(n+3-k):
                for x in range(n+3-k-b):
                    d=n+2-k-b-x
                    if 2*b+x+k<6:continue
                    lam=(d+3*b+2*x+3*k-8,d+b+x+2*k-2,d+b+x,d+x,d)
                    assert sum(lam)==5*n and min(lam)>=0 and tuple(sorted(lam,reverse=True))==lam
                    for mu in partitions(5):
                        value=actual(mu,n,lam);proposed=expected(mu,x,b,k,d)
                        assert value==proposed,(n,x,b,k,d,mu,lam,value,proposed)
                        rows.append(dict(n=n,x=x,b=b,k=k,d=d,
                            outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                            cycle_index_MN=value,corrected_bundle_trace=proposed,status='PASS'))
        print('completed n',n,'cases',len(rows),flush=True)
    with (HERE/'OUTER5_TWO_BELOW_RAY_INDEPENDENT_CHECK.tsv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS',len(rows),'valid two-below-ray cases')


if __name__=='__main__':main()
