"""Independent G030 actual plethysm checks against reconstructed traces."""
from pathlib import Path
import csv,sys
from verify_rectangular import partitions
from verify_outer4_chambers import actual
from verify_second_power_zero_twist_certificate import multiplicities

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'root'))
import second_power_zero_twist_positive as positive


def main():
    rows=[]
    for n in range(7):
        for b in range(n+3):
            for x in range(n+3-b):
                d=n+2-b-x
                if 2*b+x<10:continue
                lam=(d+3*b+2*x-10,d+b+x,d+b+x,d+x,d)
                assert sum(lam)==5*n and tuple(sorted(lam,reverse=True))==lam
                values=[v[0,0] for v in multiplicities([x],[b])]
                if (d+b+x)%2:values=values[::-1]
                for mu,expected in zip(partitions(5),values):
                    result=actual(mu,n,lam)
                    proposed=positive.coefficient(x,b,d,mu)
                    assert result==expected==proposed,(n,b,x,d,mu,result,expected,proposed)
                    rows.append(dict(n=n,x=x,b=b,d=d,outer=','.join(map(str,mu)),
                                     output=','.join(map(str,lam)),actual_MN=result,
                                     independent_trace=expected,positive_evaluator=proposed,status='PASS'))
        print('completed n',n,'cases',len(rows),flush=True)
    with (HERE/'SECOND_POWER_ZERO_TWIST_MN_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS all actual plethysm comparisons',len(rows),flush=True)


if __name__=='__main__':main()
