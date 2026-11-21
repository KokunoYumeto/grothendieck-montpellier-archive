"""Independent cycle-index/MN check of T040's odd-twist Q family."""
from pathlib import Path
from functools import lru_cache
from collections import Counter
from math import gcd
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual

HERE=Path(__file__).resolve().parent


def chi_u(cyc):
    counts=Counter(cyc)
    m=counts[1]
    return m*(m-1)//2+counts[2]-m


@lru_cache(None)
def sym_u(cyc,k):
    if k<0:return 0
    h=[1]
    for n in range(1,k+1):
        total=0
        for j in range(1,n+1):
            power=tuple(sorted((length//gcd(length,j)
                  for length in cyc for _ in range(gcd(length,j))),reverse=True))
            total+=chi_u(power)*h[n-j]
        assert total%n==0
        h.append(total//n)
    return h[k]


def predicted(mu,k,d):
    total=0
    for cyc in partitions(5):
        e=cyc.count(1)-1
        u=chi_u(cyc)
        sg=(-1)**(5-len(cyc))
        tr=(e*e-1)*sym_u(cyc,k)-sg*e*u*sym_u(cyc,k-1)
        tr+=sg*e*sym_u(cyc,k-2)+sg*sym_u(cyc,k-3)
        total+=(120//z(cyc))*character(mu,cyc)*sg**(d+1)*tr
    assert total%120==0 and total>=0
    return total//120


def main():
    rows=[]
    for n in range(2,7):
        for k in range(n-1):
            d=n-k-2
            lam=(d+3*k+6,d+2*k+2,d+1,d+1,d)
            assert sum(lam)==5*n
            for mu in partitions(5):
                value=actual(mu,n,lam)
                expected=predicted(mu,k,d)
                assert value==expected,(n,k,d,mu,lam,value,expected)
                rows.append(dict(n=n,k=k,d=d,outer=",".join(map(str,mu)),
                    output=",".join(map(str,lam)),cycle_index_MN=value,
                    proposed_module=expected,status="PASS"))
        print("completed n =",n,"cases =",len(rows),flush=True)
    with (HERE/"OUTER5_ODD_Q_INDEPENDENT_CHECK.tsv").open("w",newline="") as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter="\t")
        writer.writeheader();writer.writerows(rows)
    print("PASS",len(rows),"odd Q-family cases")


if __name__=="__main__":main()
