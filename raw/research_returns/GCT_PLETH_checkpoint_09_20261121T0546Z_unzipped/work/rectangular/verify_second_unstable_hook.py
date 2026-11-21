"""Independent original plethysms for the second unstable hook jets."""
from pathlib import Path
from fractions import Fraction as F
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
from verify_first_unstable_hook import schur_standard
HERE=Path(__file__).resolve().parent
def main():
    rows=[]
    for m in (4,5,6):
        for a in (5,6):
            for r in range(m-1):
                if (m-2)*a<2*m+r:
                    continue
                for t in (0,1):
                    n=a+t-2
                    lam=((m-1)*a+t-2*m-r,a+t)+(t+1,)*r+(t,)*(m-2-r)
                    assert min(lam)>=0 and sorted(lam,reverse=True)==list(lam) and sum(lam)==m*n
                    for mu in partitions(m):
                        value=F()
                        for cyc in partitions(m):
                            jets=0
                            for index,part in enumerate(cyc):
                                if part!=1:continue
                                rem=cyc[:index]+cyc[index+1:]
                                tangent=rem.count(1)-1
                                jets+=(1+tangent)*schur_standard((1,)*r,rem)
                            tr=schur_standard((a,)+(1,)*r,cyc)-jets
                            tr*=(-1)**((m-len(cyc))*t)
                            value+=F(character(mu,cyc)*tr,z(cyc))
                        assert value.denominator==1 and value>=0,(m,a,r,t,mu,value)
                        got=actual(mu,n,lam)
                        assert got==value,(m,a,r,t,mu,got,value)
                        rows.append(dict(m=m,a=a,r=r,t=t,n=n,outer=','.join(map(str,mu)),
                          output=','.join(map(str,lam)),actual_MN=got,
                          independent_hook_minus_jets_trace=int(value),status='PASS'))
        print('completed second unstable hook m',m,'cases',len(rows),flush=True)
    with (HERE/'SECOND_UNSTABLE_HOOK_MN_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS second unstable hook',len(rows),flush=True)
if __name__=='__main__':main()

