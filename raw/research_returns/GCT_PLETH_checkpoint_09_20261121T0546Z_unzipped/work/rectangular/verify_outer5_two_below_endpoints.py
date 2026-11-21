"""Independent literal MN audit of the T050 k=2,3,4 endpoint extension."""
from pathlib import Path
import csv
from verify_rectangular import partitions
from verify_outer4_chambers import actual
from verify_outer5_two_below_ray import expected

HERE=Path(__file__).resolve().parent


def main():
    rows=[]
    for n in range(7):
        for k in (2,3,4):
            budget=n+2-k
            if budget<0:continue
            for b in range(budget+1):
                for x in range(budget-b+1):
                    d=budget-b-x
                    if 2*b+x+k<6:continue
                    lam=(d+3*b+2*x+3*k-8,d+b+x+2*k-2,d+b+x,d+x,d)
                    assert min(lam)>=0 and sum(lam)==5*n and tuple(sorted(lam,reverse=True))==lam
                    for mu in partitions(5):
                        value=actual(mu,n,lam)
                        trace=expected(mu,x,b,k,d)
                        assert value==trace,(n,mu,lam,x,b,k,d,value,trace)
                        rows.append(dict(n=n,x=x,b=b,k=k,d=d,
                            outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                            actual_MN=value,pair_corrected_trace=trace,status='PASS'))
        print('PASS n',n,'cumulative cases',len(rows),flush=True)
    with (HERE/'OUTER5_TWO_BELOW_ENDPOINTS_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS',len(rows),'valid endpoint coefficient cases',flush=True)


if __name__=='__main__':main()
