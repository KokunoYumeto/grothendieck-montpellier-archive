"""R049 independent finite Schur versus formal-moment refined stability."""
from pathlib import Path
from fractions import Fraction as F
import csv
from verify_rectangular import partitions,character
from verify_tail_moment_stability import stable_power,fixed
HERE=Path(__file__).resolve().parent
def main():
    rows=[]
    for D in range(2,15):
        formal=stable_power(D)
        for nu in partitions(D):
            t=nu[0]
            if t<2:continue
            odd=sum(v%2 for v in nu);epsilon=t%2
            q=(odd-epsilon+2)//3
            M=(D+t-q)//2
            assert q>=0 and M>=t
            c=sum((v*character(nu,rho) for rho,v in formal.items()),F())
            assert c.denominator==1 and c>=0
            value=fixed(nu,M)
            assert value==c,(nu,M,value,c)
            rows.append(dict(D=D,width=t,tail=','.join(map(str,nu)),odd_parts=odd,
              q=q,refined_row_count=M,old_row_count=(D+t)//2,
              finite_Schur_average=value,formal_moment_multiplicity=int(c),status='PASS'))
        print('refined occupied-row boundary degree',D,'cases',len(rows),flush=True)
    with (HERE/'ODD_PART_OCCUPANCY_STABILITY_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS refined boundary',len(rows),'improved',sum(r['refined_row_count']<r['old_row_count'] for r in rows),
      'positive_improved',sum(r['refined_row_count']<r['old_row_count'] and r['finite_Schur_average']>0 for r in rows),flush=True)
if __name__=='__main__':main()

