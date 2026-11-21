"""Independent literal MN check of T051, including stable three-subset sums."""
from pathlib import Path
from functools import lru_cache
import csv
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import actual
from verify_outer5_fivepoint_family import sym_standard
from verify_outer5_two_row_bundle import schur_two
from verify_outer5_stable_defect import induced_correction

HERE=Path(__file__).resolve().parent


def triple_correction(cyc,x,b,k):
    if (k,b) not in ((3,0),(2,1),(2,0)):
        return 0
    total=0
    for mask in range(1<<len(cyc)):
        selected=tuple(cyc[i] for i in range(len(cyc)) if mask>>i&1)
        if sum(selected)!=3:continue
        rest=tuple(cyc[i] for i in range(len(cyc)) if not mask>>i&1)
        sg3=(-1)**(3-len(selected));sg2=(-1)**(2-len(rest))
        standard3=selected.count(1)-1
        if (k,b)==(3,0):tr=sg3*sg2**x
        elif (k,b)==(2,1):tr=standard3*sg2**(x+1)
        else:tr=(standard3+sg3)*(1+sg2)
        total+=tr
    return total


@lru_cache(None)
def expected(mu,x,b,k,d):
    c=2*k-3;result=0
    for cyc in partitions(5):
        jet=cyc.count(1)*sym_standard(cyc,k-1)
        s0=schur_two(cyc,b+x,b)
        s1=schur_two(cyc,b+x-1,b)+schur_two(cyc,b+x,b-1)
        s2=schur_two(cyc,b+x-1,b-1)
        trace=s0*(sym_standard(cyc,c)-jet)-s1*(sym_standard(cyc,c-1)-jet)+s2*(sym_standard(cyc,c-2)-jet)
        trace+=induced_correction(cyc,x,b,3)
        trace-=triple_correction(cyc,x,b,k)
        trace*=(-1)**((5-len(cyc))*(d+b+x))
        result+=(120//z(cyc))*character(mu,cyc)*trace
    assert result%120==0 and result>=0,(mu,x,b,k,d,result)
    return result//120


def main():
    rows=[]
    for n in range(8):
        for k in range(2,8):
            budget=n+3-k
            if budget<0:continue
            for b in range(budget+1):
                for x in range(budget-b+1):
                    d=budget-b-x
                    if 2*b+x+k<9:continue
                    lam=(d+3*b+2*x+3*k-12,d+b+x+2*k-3,d+b+x,d+x,d)
                    assert min(lam)>=0 and sum(lam)==5*n and tuple(sorted(lam,reverse=True))==lam
                    for mu in partitions(5):
                        value=actual(mu,n,lam);proposed=expected(mu,x,b,k,d)
                        assert value==proposed,(n,mu,lam,x,b,k,d,value,proposed)
                        rows.append(dict(n=n,x=x,b=b,k=k,d=d,
                            outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                            triple_branch=int((k,b) in ((3,0),(2,1),(2,0))),
                            actual_MN=value,pair_minus_triple_trace=proposed,status='PASS'))
        print('PASS n',n,'cumulative cases',len(rows),flush=True)
    with (HERE/'OUTER5_THREE_BELOW_ENDPOINTS_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS',len(rows),'cases;',sum(r['triple_branch'] for r in rows),'with nonzero triple-branch module',flush=True)


if __name__=='__main__':main()
