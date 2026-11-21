"""Independent cycle-index/MN check of theta's T039 five-point family."""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import csv
from verify_rectangular import partitions, character, z
from verify_outer4_chambers import actual

HERE=Path(__file__).resolve().parent


@lru_cache(None)
def sym_standard(cyc,degree):
    if degree<0:return 0
    vals=[1]+[0]*degree
    for k in cyc:
        for j in range(k,degree+1):vals[j]+=vals[j-k]
    return vals[degree]-(vals[degree-1] if degree else 0)


def expected(mu,a,d):
    value=0
    for cyc in partitions(5):
        counts=Counter(cyc);m1=counts[1]
        # The action on unordered pairs minus the action on singletons is [32].
        ch32=m1*(m1-1)//2+counts[2]-m1
        sg=(-1)**(5-len(cyc))
        tr=sg**(d+a)*(ch32*sym_standard(cyc,a)+sym_standard(cyc,a-1))
        value+=(120//z(cyc))*character(mu,cyc)*tr
    assert value%120==0 and value>=0
    return value//120


def main():
    rows=[]
    for n in range(1,7):
        for a in range(n):
            d=n-a-1
            lam=(d+2*a+3,d+a+2,d+a,d+a,d)
            assert sum(lam)==5*n
            for mu in partitions(5):
                value=actual(mu,n,lam)
                proposed=expected(mu,a,d)
                assert value==proposed,(n,a,d,mu,lam,value,proposed)
                rows.append(dict(n=n,a=a,d=d,outer=','.join(map(str,mu)),
                    output=','.join(map(str,lam)),cycle_index_MN=value,
                    proposed_module=proposed,status='PASS'))
        print('completed n =',n,'cases =',len(rows),flush=True)
    with (HERE/'OUTER5_FIVEPOINT_INDEPENDENT_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS',len(rows),'five-point cases')


if __name__=='__main__':main()
