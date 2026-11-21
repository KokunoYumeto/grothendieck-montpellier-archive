"""Independent character checks for T030 and the two T031 binary faces."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
import csv
from verify_rectangular import partitions,character
from verify_endsector_schur import plethysm
HERE=Path(__file__).resolve().parent
@lru_cache(None)
def actual(mu,n,lam):
    value=sum((c*character(tuple(x for x in lam if x),cyc)
               for cyc,c in plethysm(mu,n).items()),Fraction())
    assert value.denominator==1
    return int(value)
def P(q):
    return sum(2*u+3*v==q for u in range(max(q//2+1,0))
               for v in range(max(q//3+1,0)))
@lru_cache(None)
def F4(N,K):
    if N<0 or K<0 or K>2*N:return 0
    count=0
    for eps in range(2):
     for d in range(N//3+1):
      for c in range(N//2+1):
       for b in range(N//2+1):
        a=N-2*b-2*c-3*d-3*eps
        count+=a>=0 and 2*b+4*c+6*d+3*eps==K
    return count
rows=[]
for n in range(7):
 for b in range(n+1):
  a=2*n-b;r=n-b;lam=(a,a,b,b)
  for mu in partitions(4):
   if mu==(4,):expected=P(r-3*(b%2))
   elif mu==(1,1,1,1):expected=P(r-3*((b+1)%2))
   elif mu==(2,2):expected=(r+2)//3
   else:expected=0
   value=actual(mu,n,lam);assert value==expected,(n,mu,lam,value,expected)
   rows.append(dict(statement='T030',n=n,outer=','.join(map(str,mu)),
                    output=','.join(map(str,lam)),character_value=value,
                    proposed_count=expected,status='PASS'))
 for part in partitions(4*n):
  if len(part)>4:continue
  lam=part+(0,)*(4-len(part));value=actual((4,),n,lam)
  if lam[2]==lam[3]:
   t=lam[2];N=n-t;K=lam[1]-t
   expected=F4(N-3*(t%2),K-6*(t%2));assert value==expected
   rows.append(dict(statement='T031_lower',n=n,outer='4',output=','.join(map(str,lam)),
                    character_value=value,proposed_count=expected,status='PASS'))
  if lam[0]==lam[1]:
   H=lam[0];N=H-n;K=H-lam[2]
   expected=F4(N-3*(H%2),K-6*(H%2));assert value==expected
   rows.append(dict(statement='T031_upper',n=n,outer='4',output=','.join(map(str,lam)),
                    character_value=value,proposed_count=expected,status='PASS'))
with (HERE/'OUTER4_PAIRED_AND_PROPER_CHECK.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
from collections import Counter
print('PASS',len(rows),'coefficient cases',dict(Counter(r['statement'] for r in rows)))
