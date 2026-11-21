"""Reproduce all 261425 m=3 equal-middle formula comparisons, n=1..100."""
from pathlib import Path
import csv
from check_degree_three import parts3, form

def p23(r):
    return sum((r-3*v)%2==0 for v in range(max(-1,r//3)+1)) if r>=0 else 0

count=0
rows=[]
for n in range(1,101):
    subtotal=0
    for lam in parts3(3*n):
        a,b,c=lam
        s=min(a-b,b-c)
        predicted=(p23(s-3*(b%2)),p23(s-3*((b+1)%2)),(s+2)//3)
        observed=form(n,lam)
        assert predicted==observed,(n,lam,predicted,observed)
        count+=1;subtotal+=1
    rows.append((n,subtotal,'PASS'))
with Path(__file__).with_name('EQUAL_MIDDLE_M3_CHECK.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['inner_n','partitions_all_three_outer_shapes','outcome']);w.writerows(rows)
print('PASS',count,'partitions; all three outer shapes')
