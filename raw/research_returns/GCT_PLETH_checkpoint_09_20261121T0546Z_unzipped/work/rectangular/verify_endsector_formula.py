"""Independent cycle-index/Murnaghan--Nakayama test of theta's end sector."""
from pathlib import Path
from fractions import Fraction
import csv
from verify_rectangular import power_sum_plethysm,character

HERE=Path(__file__).resolve().parent

def count_parts(m,R):
    if R<0:return 0
    dp=[1]+[0]*R
    for part in range(2,m+1):
        for i in range(part,R+1):dp[i]+=dp[i-part]
    return dp[R]

rows=[]
for m,maxn in [(4,6),(5,4),(6,3)]:
    for n in range(maxn+1):
        N=m*n
        ps=power_sum_plethysm(m,n)
        tested=0
        for beta in range(N//(m-1)+1):
            for gamma in range(beta+1):
                alpha=N-(m-2)*beta-gamma
                if alpha<beta:continue
                lam=(alpha,)+(beta,)*(m-2)+(gamma,)
                actual=sum((c*character(tuple(x for x in lam if x),cyc)
                            for cyc,c in ps.items()),Fraction())
                assert actual.denominator==1
                R=beta-gamma-m*(m-1)//2*(beta%2)-m*max(0,beta-n)
                expected=count_parts(m,R)
                assert actual==expected,(m,n,lam,actual,expected,R)
                rows.append(dict(m=m,n=n,partition=','.join(map(str,lam)),
                                 residual_R=R,cycle_index_MN=int(actual),
                                 polytope_count=expected,status='PASS'))
                tested+=1
        print('PASS',m,n,tested,flush=True)
with (HERE/'ENDSECTOR_INDEPENDENT_CHECK.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
    w.writeheader();w.writerows(rows)
print('PASS total',len(rows),'coefficient cases',flush=True)
