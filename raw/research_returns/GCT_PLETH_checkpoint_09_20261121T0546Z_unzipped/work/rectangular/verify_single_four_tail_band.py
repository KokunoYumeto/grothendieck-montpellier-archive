"""R044 independent complete single-four tail coefficient check."""
from pathlib import Path
from itertools import product
import csv
from verify_outer4_chambers import actual
HERE=Path(__file__).resolve().parent

def predicted(a,n,p,q,s):
    if n==3:return int(a==3 and (p,q,s)==(0,0,1))
    if p==0 and s==0:
        return 1+int(a>=4) if q==0 else min(3,max(0,a-q-1))
    if p==1 and s==0:return min(2,max(0,a-q-3))
    if p==0 and s==1:return int(a>=q+3)
    if p==1 and s==1:return int(a>=q+5)
    return 0

def main():
    rows=[]
    for a in range(2,7):
        for n in range(a,7):
            for p,q,s in product(range(a-1),repeat=3):
                if p+q+s>a-2:continue
                tail=(4,)+(3,)*p+(2,)*q+(1,)*s
                first=a*n-sum(tail)
                if first<4:continue
                lam=(first,)+tail
                value=actual((a,),n,lam);source=actual((n,),a,lam)
                want=predicted(a,n,p,q,s)
                assert value==want,(a,n,lam,value,want)
                assert source>=value,(a,n,lam,source,value)
                rows.append(dict(a=a,n=n,p=p,q=q,s=s,
                    output=','.join(map(str,lam)),target_actual_MN=value,
                    target_formula=want,source_actual_MN=source,status='PASS'))
            print('completed single-four band',a,n,'cases',len(rows),flush=True)
    with (HERE/'SINGLE_FOUR_TAIL_BAND_MN_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS single-four band cases',len(rows),flush=True)
if __name__=='__main__':main()

