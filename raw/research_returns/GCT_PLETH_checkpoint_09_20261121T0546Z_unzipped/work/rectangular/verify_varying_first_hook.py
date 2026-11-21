"""T060 independent literal plethysm verification for the varying first hook."""
from pathlib import Path
from fractions import Fraction as F
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
from verify_outer5_fivepoint_family import sym_standard
HERE=Path(__file__).resolve().parent
def main():
    rows=[]
    for m in (3,4,5,6):
        for a in (1,2,3):
            for t in (0,1):
                for n in (a+t,a+t+1):
                    lam=(m*n-a-(m-1)*t-1,a+t,t+1)+(t,)*(m-3)
                    assert min(lam)>=0 and sorted(lam,reverse=True)==list(lam) and sum(lam)==m*n
                    for mu in partitions(m):
                        value=F()
                        for cyc in partitions(m):
                            e=cyc.count(1)-1
                            tr=e*sym_standard(cyc,a)-sym_standard(cyc,a+1)
                            tr*=(-1)**((m-len(cyc))*t)
                            value+=F(character(mu,cyc)*tr,z(cyc))
                        assert value.denominator==1 and value>=0
                        got=actual(mu,n,lam)
                        assert got==value,(m,a,t,n,mu,lam,got,value)
                        rows.append(dict(m=m,a=a,t=t,n=n,outer=','.join(map(str,mu)),
                          output=','.join(map(str,lam)),actual_MN=got,
                          independent_hook_trace=int(value),status='PASS'))
        print('completed first-hook outer size',m,'cases',len(rows),flush=True)
    with (HERE/'VARYING_FIRST_HOOK_MN_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS first-hook actual plethysms',len(rows),flush=True)
if __name__=='__main__':main()

