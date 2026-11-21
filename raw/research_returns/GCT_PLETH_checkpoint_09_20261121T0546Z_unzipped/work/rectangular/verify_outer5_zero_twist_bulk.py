"""T054 independent literal subgroup induction and actual MN comparison."""
from pathlib import Path
from math import gcd
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
from verify_outer5_two_row_bundle import schur_two
from verify_outer5_fivepoint_family import sym_standard

HERE=Path(__file__).resolve().parent


def power_cycle(cyc,p):
    return tuple(sorted((length//gcd(length,p)
                         for length in cyc for _ in range(gcd(length,p))),reverse=True))


def trace(cyc,x,b,k):
    a=b+x
    value=schur_two(cyc,a,b)
    if 1 in cyc:
        rest=list(cyc);rest.remove(1);rest=tuple(rest)
        value-=cyc.count(1)*sum(schur_two(rest,a-i,b-j)
                               for i in range(k) for j in range(k-i))
    for mask in range(1<<len(cyc)):
        chosen=tuple(cyc[i] for i in range(len(cyc)) if mask>>i&1)
        if sum(chosen)!=2:continue
        rest=tuple(cyc[i] for i in range(len(cyc)) if not(mask>>i&1))
        trunc=1
        for length in chosen:
            powered=power_cycle(rest,length)
            trunc*=sum(sym_standard(powered,t) for t in range(k))
        value+=(-1)**(2-len(chosen)+(3-len(rest))*b)*sym_standard(rest,x)*trunc
    return value


def main():
    rows=[]
    for k in (3,4):
        for n in range(8):
            for b in range(3*k-2,n+k+1):
                for x in range(n+k-b+1):
                    if 2*b+x<5*k:continue
                    d=n+k-b-x
                    lam=(d+3*b+2*x-5*k,d+b+x,d+b+x,d+x,d)
                    assert min(lam)>=0 and tuple(sorted(lam,reverse=True))==lam and sum(lam)==5*n
                    ts={cyc:(-1)**((5-len(cyc))*(d+b+x))*trace(cyc,x,b,k)
                        for cyc in partitions(5)}
                    for mu in partitions(5):
                        numerator=sum((120//z(cyc))*character(mu,cyc)*ts[cyc] for cyc in partitions(5))
                        assert numerator%120==0
                        expected=numerator//120
                        result=actual(mu,n,lam)
                        assert result==expected,(k,n,x,b,d,mu,lam,result,expected)
                        rows.append(dict(k=k,n=n,x=x,b=b,d=d,outer=','.join(map(str,mu)),
                                         output=','.join(map(str,lam)),actual_MN=result,
                                         independent_induction=expected,status='PASS'))
            print('completed n',n,'cases',len(rows),flush=True)
    with (HERE/'OUTER5_ZERO_TWIST_BULK_MN_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS T054 all actual coefficients',len(rows),flush=True)


if __name__=='__main__':main()
