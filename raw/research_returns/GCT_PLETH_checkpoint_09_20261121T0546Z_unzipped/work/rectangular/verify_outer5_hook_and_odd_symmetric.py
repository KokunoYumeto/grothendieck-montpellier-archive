"""Independent actual plethysm checks for T041 and T042.

Actual values come from the power-sum cycle index and rim-hook MN.
Proposed values use direct standard-representation cycle traces, not
the fixed numerator, Newton table, or evaluator under review.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
import csv

from verify_rectangular import partitions, character, z
from verify_outer4_chambers import actual
from verify_outer5_fivepoint_family import sym_standard

HERE=Path(__file__).resolve().parent


@lru_cache(None)
def expected_hook(mu,a,d):
    value=0
    for cyc in partitions(5):
        counts=Counter(cyc)
        m1=counts[1]
        chU=m1*(m1-1)//2+counts[2]-m1
        hook=(m1-1)*sym_standard(cyc,a)-sym_standard(cyc,a+1)
        trace=(-1)**((5-len(cyc))*(d+a))*chU*hook
        value+=(120//z(cyc))*character(mu,cyc)*trace
    assert value%120==0 and value>=0
    return value//120


@lru_cache(None)
def expected_odd_symmetric(mu,a,k,d):
    value=0
    for cyc in partitions(5):
        m1=cyc.count(1)
        c0=sym_standard(cyc,2*k)-m1*sym_standard(cyc,k-1)
        c1=sym_standard(cyc,2*k+1)-m1*sym_standard(cyc,k-1)
        trace=c1*sym_standard(cyc,a)-c0*sym_standard(cyc,a-1)
        trace*=(-1)**((5-len(cyc))*(d+a))
        value+=(120//z(cyc))*character(mu,cyc)*trace
    assert value%120==0 and value>=0
    return value//120


def write(name,rows):
    with (HERE/name).open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)


def main():
    hook_rows=[];symmetric_rows=[]
    for n in range(1,7):
        for a in range(1,n):
            d=n-a-1
            lam=(d+2*a+4,d+a+2,d+a,d+a-1,d)
            assert sum(lam)==5*n and tuple(sorted(lam,reverse=True))==lam
            for mu in partitions(5):
                value=actual(mu,n,lam)
                expected=expected_hook(mu,a,d)
                assert value==expected,('T041',n,a,d,mu,lam,value,expected)
                hook_rows.append(dict(n=n,a=a,d=d,outer=','.join(map(str,mu)),
                    output=','.join(map(str,lam)),cycle_index_MN=value,
                    direct_module_trace=expected,status='PASS'))
        for a in range(n):
            for k in range(n-a):
                d=n-a-k-1
                lam=(d+2*a+3*k+4,d+a+2*k+1,d+a,d+a,d)
                assert sum(lam)==5*n and tuple(sorted(lam,reverse=True))==lam
                for mu in partitions(5):
                    value=actual(mu,n,lam)
                    expected=expected_odd_symmetric(mu,a,k,d)
                    assert value==expected,('T042',n,a,k,d,mu,lam,value,expected)
                    symmetric_rows.append(dict(n=n,a=a,k=k,d=d,
                        outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                        cycle_index_MN=value,direct_module_trace=expected,status='PASS'))
        print('completed n',n,'T041',len(hook_rows),'T042',len(symmetric_rows),flush=True)
    write('OUTER5_HOOK_INDEPENDENT_CHECK.tsv',hook_rows)
    write('OUTER5_ODD_SYMMETRIC_INDEPENDENT_CHECK.tsv',symmetric_rows)
    print('PASS T041',len(hook_rows),'T042',len(symmetric_rows))


if __name__=='__main__':main()
