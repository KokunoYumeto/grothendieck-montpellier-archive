"""Independent actual plethysm comparison for the full G020 family."""
from pathlib import Path
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
from verify_outer5_fivepoint_family import sym_standard

HERE=Path(__file__).resolve().parent


def expected(mu,a,k,t,d):
    result=0
    for cyc in partitions(5):
        ha=sym_standard(cyc,a);hm=sym_standard(cyc,a-1)
        trace=ha*sym_standard(cyc,2*k+t)-hm*sym_standard(cyc,2*k+t-1)
        trace-=cyc.count(1)*sym_standard(cyc,k-1)*(ha-hm)
        trace*=(-1)**((5-len(cyc))*(d+a))
        result+=(120//z(cyc))*character(mu,cyc)*trace
    assert result%120==0 and result>=0
    return result//120


def main():
    rows=[]
    for n in range(5):
        for a in range(n+1):
            for k in range(n-a+1):
                for t in range(n-a-k+1):
                    d=n-a-k-t
                    lam=(d+2*a+3*k+4*t,d+a+2*k+t,d+a,d+a,d)
                    assert sum(lam)==5*n
                    for mu in partitions(5):
                        value=actual(mu,n,lam)
                        proposed=expected(mu,a,k,t,d)
                        assert value==proposed,(n,a,k,t,d,mu,lam,value,proposed)
                        rows.append(dict(n=n,a=a,k=k,t=t,d=d,
                            outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                            cycle_index_MN=value,direct_module_trace=proposed,status='PASS'))
        print('completed n',n,'cases',len(rows),flush=True)
    with (HERE/'OUTER5_THREE_PARAMETER_INDEPENDENT_CHECK.tsv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS',len(rows),'G020 cases')


if __name__=='__main__':main()
