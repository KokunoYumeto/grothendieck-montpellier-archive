"""T055 literal subgroup traces and independent actual-MN coefficients."""
from pathlib import Path
from itertools import combinations
import csv
from verify_rectangular import partitions, character, z
from verify_outer4_chambers import actual
from verify_outer5_two_row_bundle import schur_two
from verify_outer5_fivepoint_family import sym_standard

HERE=Path(__file__).resolve().parent


def schur_three_one(cyc,A,B):
    h=lambda j:sym_standard(cyc,j)
    return h(A)*h(B)*h(1)-h(A)*h(B+1)-h(A+1)*h(B-1)*h(1)+h(A+2)*h(B-1)


def trace(cyc,x,b,k):
    a=b+x
    result=schur_three_one(cyc,a+1,b+1)
    if 1 in cyc:
        rest=list(cyc);rest.remove(1);rest=tuple(rest)
        singleton=(-1)**(4-len(rest))*sum(schur_two(rest,a-i,b-j)
                   for i in range(k) for j in range(k-i))
        singleton+=sum(schur_two(rest,a+1-i,b+1-j)
                   for i in range(k-1) for j in range(k-1-i))
        result-=cyc.count(1)*singleton
    fixed=[i for i,c in enumerate(cyc) if c==1]
    for pair in combinations(fixed,2):
        rest=tuple(c for i,c in enumerate(cyc) if i not in pair)
        result+=2*(-1)**((3-len(rest))*(b+1))*sym_standard(rest,x)*\
            sum(sym_standard(rest,t) for t in range(k))*\
            sum(sym_standard(rest,t) for t in range(k-1))
    return result


def main():
    rows=[]
    for k in (3,4):
        for n in range(8):
            for b in range(3*k-3,n+k):
                for x in range(n+k-b):
                    d=n+k-b-x-1
                    lam=(d+3*b+2*x+4-5*k,d+b+x+1,d+b+x,d+x,d)
                    assert min(lam)>=0 and tuple(sorted(lam,reverse=True))==lam and sum(lam)==5*n
                    ts={cyc:(-1)**((5-len(cyc))*(d+b+x+1))*trace(cyc,x,b,k)
                        for cyc in partitions(5)}
                    for mu in partitions(5):
                        numerator=sum((120//z(cyc))*character(mu,cyc)*ts[cyc] for cyc in partitions(5))
                        assert numerator%120==0
                        expected=numerator//120
                        result=actual(mu,n,lam)
                        assert result==expected,(k,n,x,b,d,mu,lam,result,expected)
                        rows.append(dict(k=k,n=n,x=x,b=b,d=d,outer=','.join(map(str,mu)),
                            output=','.join(map(str,lam)),actual_MN=result,
                            independent_induction=expected,status='PASS'))
            print('completed k,n',k,n,'cases',len(rows),flush=True)
    with (HERE/'OUTER5_ONE_TWIST_BULK_MN_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS T055 all actual coefficients',len(rows),flush=True)


if __name__=='__main__':main()
