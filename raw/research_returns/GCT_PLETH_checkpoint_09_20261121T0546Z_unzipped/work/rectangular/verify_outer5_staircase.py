"""Independent literal plethysm comparisons for the G023 staircase."""
from pathlib import Path
import csv
from verify_outer4_chambers import actual,transpose

HERE=Path(__file__).resolve().parent
LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
VALUES={0:(1,0,0,0,0,0,0),1:(0,1,1,1,1,1,0),2:(3,9,11,9,9,6,2)}


def main():
    rows=[]
    for r,d in ((0,0),(1,0),(2,0),(1,1)):
        n=d+2*r;lam=tuple(d+(4-i)*r for i in range(5))
        values=[]
        for mu in LABELS:
            nu=transpose(mu) if d%2 else mu
            proposed=VALUES[r][LABELS.index(nu)]
            value=actual(mu,n,lam)
            assert value==proposed,(r,d,mu,lam,value,proposed)
            values.append(value)
            rows.append(dict(r=r,d=d,n=n,outer=','.join(map(str,mu)),
                output=','.join(map(str,lam)),cycle_index_MN=value,
                staircase_trace=proposed,status='PASS'))
        print('PASS r',r,'d',d,values,flush=True)
    with (HERE/'OUTER5_STAIRCASE_INDEPENDENT_CHECK.tsv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS all',len(rows),'staircase cases')


if __name__=='__main__':main()
