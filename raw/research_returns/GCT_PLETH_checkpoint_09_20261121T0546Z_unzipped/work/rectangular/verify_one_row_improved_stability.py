"""R048 independent finite characters at the improved row boundary."""
from pathlib import Path
from fractions import Fraction as F
import csv
from verify_rectangular import partitions,character
from verify_tail_moment_stability import stable_power,fixed
HERE=Path(__file__).resolve().parent
def main():
    rows=[]
    for D in range(1,13):
        formal=stable_power(D)
        for nu in partitions(D):
            t=nu[0]
            if (D+t)%2 or sum(v%2 for v in nu)<2:
                continue
            s=(D+t)//2-1
            assert s>=t
            c=sum((v*character(nu,rho) for rho,v in formal.items()),F())
            assert c.denominator==1 and c>=0
            value=fixed(nu,s)
            assert value==c,(nu,s,value,c)
            rows.append(dict(D=D,width=t,tail=','.join(map(str,nu)),odd_parts=sum(v%2 for v in nu),
              improved_row_count=s,finite_Schur_average=value,formal_moment_multiplicity=int(c),status='PASS'))
        print('improved row boundary degree',D,'cases',len(rows),flush=True)
    with (HERE/'ONE_ROW_IMPROVED_STABILITY_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS improved boundary',len(rows),'nonzero',sum(r['finite_Schur_average']>0 for r in rows),flush=True)
if __name__=='__main__':main()

