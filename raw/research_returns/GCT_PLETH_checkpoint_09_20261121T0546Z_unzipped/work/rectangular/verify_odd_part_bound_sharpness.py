"""R051: independent literal cycle/Jacobi-Trudi averages."""
from pathlib import Path
from fractions import Fraction as F
import csv
from verify_rectangular import partitions,z
HERE=Path(__file__).resolve().parent

def determinant(matrix):
    a=[list(v) for v in matrix];previous=1;sign=1
    for k in range(len(a)-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,len(a)) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                numerator=pivot*a[i][j]-a[i][k]*a[k][j]
                assert numerator%previous==0
                a[i][j]=numerator//previous
        for i in range(k+1,len(a)):a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

def main():
    nu=(6,5,4,3,2,1);rows=[]
    for s,expected in ((11,318),(12,331),(13,332),(14,332),(21,332)):
        value=F()
        for cyc in partitions(s):
            raw=[1]+[0]*12
            for ell in cyc:
                for j in range(ell,len(raw)):raw[j]+=raw[j-ell]
            h=[raw[j]-(raw[j-1] if j else 0) for j in range(len(raw))]
            matrix=[[h[d] if (d:=nu[i]-i+j)>=0 else 0 for j in range(6)] for i in range(6)]
            value+=F(determinant(matrix),z(cyc))
        assert value==expected,(s,value,expected)
        rows.append(dict(row_count=s,tail=','.join(map(str,nu)),cycle_JT_multiplicity=int(value),status='PASS'))
        print(s,value,flush=True)
    assert rows[2]['cycle_JT_multiplicity']-rows[1]['cycle_JT_multiplicity']==1
    with (HERE/'ODD_PART_BOUND_SHARPNESS_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS sharpness',len(rows),flush=True)

if __name__=='__main__':main()
