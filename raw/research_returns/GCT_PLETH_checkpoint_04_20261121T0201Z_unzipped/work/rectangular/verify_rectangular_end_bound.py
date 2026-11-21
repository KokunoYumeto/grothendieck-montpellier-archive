"""Exact finite checks of the R014 family, including a strict inequality."""
from fractions import Fraction
from pathlib import Path
import csv
from verify_rectangular import partitions,z,character,power_sum_plethysm
rows=[]
for d,n,beta,gamma in [(3,2,2,0),(3,3,3,0),(4,4,2,0)]:
    lam=tuple(x for x in (d*n-(d-2)*beta-gamma,)+(beta,)*(d-2)+(gamma,) if x)
    rectangle=(d,)*n
    g=sum(Fraction(character(lam,cyc)*character(rectangle,cyc)**2,z(cyc))
          for cyc in partitions(d*n))
    a=sum(c*character(lam,cyc) for cyc,c in power_sum_plethysm(d,n).items())
    R=beta-gamma-d*(d-1)//2*(beta%2)
    dp=[1]+[0]*R
    for k in range(2,d+1):
        for j in range(k,R+1):dp[j]+=dp[j-k]
    assert a==dp[R] and g>=a
    rows.append(dict(d=d,n=n,beta=beta,gamma=gamma,partition=','.join(map(str,lam)),
                     plethysm=int(a),rectangular_Kronecker=int(g),polytope_count=dp[R],status='PASS'))
p=Path(__file__).resolve().parent/'RECTANGULAR_END_BOUND_CHECK.tsv'
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print('PASS',rows)
