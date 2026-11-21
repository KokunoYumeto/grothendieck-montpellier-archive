"""T064 focused original-MN checks at ideal orders three and four."""
from pathlib import Path
from fractions import Fraction as F
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
from verify_first_unstable_hook import schur_standard
HERE=Path(__file__).resolve().parent
def symmetric_permutation(cyc,degree):
    coeff=[1]+[0]*degree
    for ell in cyc:
        for j in range(ell,degree+1):
            coeff[j]+=coeff[j-ell]
    return coeff[degree]
def main():
    rows=[]
    for k,m,alist in ((3,4,(7,8)),(3,5,(7,8)),(4,4,(9,))):
        for a in alist:
            for r in range(m-1):
                if (m-2)*a<m*k+r:continue
                for t in (0,1):
                    n=a+t-k
                    lam=((m-1)*a+t-m*k-r,a+t)+(t+1,)*r+(t,)*(m-2-r)
                    assert min(lam)>=0 and sorted(lam,reverse=True)==list(lam) and sum(lam)==m*n
                    for mu in partitions(m):
                        value=F()
                        for cyc in partitions(m):
                            jets=0
                            for index,ell in enumerate(cyc):
                                if ell!=1:continue
                                rem=cyc[:index]+cyc[index+1:]
                                jets+=symmetric_permutation(rem,k-1)*schur_standard((1,)*r,rem)
                            tr=schur_standard((a,)+(1,)*r,cyc)-jets
                            tr*=(-1)**((m-len(cyc))*t)
                            value+=F(character(mu,cyc)*tr,z(cyc))
                        assert value.denominator==1 and value>=0,(k,m,a,r,t,mu,value)
                        got=actual(mu,n,lam)
                        assert got==value,(k,m,a,r,t,mu,got,value)
                        rows.append(dict(k=k,m=m,a=a,r=r,t=t,n=n,outer=','.join(map(str,mu)),
                          output=','.join(map(str,lam)),actual_MN=got,
                          independent_hook_minus_jets_trace=int(value),status='PASS'))
        print('completed fixed-order hook k,m',k,m,'cases',len(rows),flush=True)
    with (HERE/'HIGHER_UNSTABLE_HOOK_MN_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS higher unstable hook',len(rows),flush=True)
if __name__=='__main__':main()

