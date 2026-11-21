"""Independent literal plethysm audits for G021 and T043."""
from pathlib import Path
from functools import lru_cache
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
from verify_outer5_fivepoint_family import sym_standard

HERE=Path(__file__).resolve().parent


def schur_two(cyc,p,q):
    return sym_standard(cyc,p)*sym_standard(cyc,q)-sym_standard(cyc,p+1)*sym_standard(cyc,q-1)


@lru_cache(None)
def expected(mu,x,b,k,t,d):
    result=0;c=2*k+t
    for cyc in partitions(5):
        J=cyc.count(1)*sym_standard(cyc,k-1)
        S0=schur_two(cyc,b+x,b)
        S1=schur_two(cyc,b+x-1,b)+schur_two(cyc,b+x,b-1)
        S2=schur_two(cyc,b+x-1,b-1)
        trace=S0*(sym_standard(cyc,c)-J)
        trace-=S1*(sym_standard(cyc,c-1)-J)
        trace+=S2*(sym_standard(cyc,c-2)-J)
        trace*=(-1)**((5-len(cyc))*(d+b+x))
        result+=(120//z(cyc))*character(mu,cyc)*trace
    assert result%120==0 and result>=0,(mu,x,b,k,t,d,result)
    return result//120


def write(name,rows):
    with (HERE/name).open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)


def main():
    rows=[]
    for n in range(5):
        for x in range(n+1):
            for b in range(n-x+1):
                for k in range(n-x-b+1):
                    for t in range(n-x-b-k+1):
                        d=n-x-b-k-t
                        lam=(d+3*b+2*x+3*k+4*t,d+b+x+2*k+t,d+b+x,d+x,d)
                        assert sum(lam)==5*n
                        for mu in partitions(5):
                            value=actual(mu,n,lam);proposed=expected(mu,x,b,k,t,d)
                            assert value==proposed,('G021',n,x,b,k,t,d,mu,lam,value,proposed)
                            rows.append(dict(n=n,x=x,b=b,k=k,t=t,d=d,
                                outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                                cycle_index_MN=value,two_row_trace=proposed,status='PASS'))
        print('G021 completed n',n,'cases',len(rows),flush=True)
    write('OUTER5_TWO_ROW_BUNDLE_INDEPENDENT_CHECK.tsv',rows)
    print('PASS G021',len(rows),'cases',flush=True)

    rows=[]
    for n in range(1,7):
        for a in range(1,n+1):
            for k in range(n-a+1):
                d=n-a-k
                lam=(d+2*a+3*k+1,d+a+2*k,d+a,d+a-1,d)
                for mu in partitions(5):
                    value=actual(mu,n,lam);proposed=expected(mu,a-1,1,k,0,d)
                    assert value==proposed,('T043',n,a,k,d,mu,lam,value,proposed)
                    rows.append(dict(n=n,a=a,k=k,d=d,
                        outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                        cycle_index_MN=value,hook_bundle_trace=proposed,status='PASS'))
        print('T043 completed n',n,'cases',len(rows),flush=True)
    write('OUTER5_ALL_POWER_HOOK_INDEPENDENT_CHECK.tsv',rows)
    print('PASS T043',len(rows),'cases')


if __name__=='__main__':main()
