"""R047 independent finite multiplicity profile for (4^h,3,2^j,1)."""
from pathlib import Path
import csv
from verify_outer4_chambers import actual
HERE=Path(__file__).resolve().parent
def main():
    rows=[]
    for h in range(1,4):
        for j in range(4):
            for a in range(h+j+3,9):
                tail=(4,)*h+(3,)+(2,)*j+(1,)
                for n in (4,5):
                    lam=(a*n-sum(tail),)+tail
                    assert lam[0]>=4
                    want=min(h,max(0,a-h-j-3))
                    value=actual((a,),n,lam)
                    assert value==want,(h,j,a,n,lam,value,want)
                    rows.append(dict(h=h,j=j,a=a,n=n,output=','.join(map(str,lam)),
                       actual_MN=value,finite_profile=want,status='PASS'))
        print('completed repeated-four mixed h',h,'cases',len(rows),flush=True)
    with (HERE/'REPEATED_FOUR_MIXED_PROFILE_MN_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS repeated-four mixed profile',len(rows),flush=True)
if __name__=='__main__':main()

