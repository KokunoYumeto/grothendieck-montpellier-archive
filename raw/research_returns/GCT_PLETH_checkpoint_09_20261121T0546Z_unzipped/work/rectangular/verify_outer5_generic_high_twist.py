"""T059: literal JT/subgroup traces versus independent actual plethysm."""
from pathlib import Path
from itertools import product, permutations
from functools import lru_cache
import csv
from verify_rectangular import partitions, character, z, sign
from verify_outer4_chambers import actual
from verify_outer5_fivepoint_family import sym_standard
from verify_outer5_zero_twist_bulk import power_cycle
HERE=Path(__file__).resolve().parent
PERMS=tuple((p,sign(p)) for p in permutations(range(3)))

@lru_cache(None)
def schur_three(cyc,shape):
    return sum(eps*sym_standard(cyc,shape[0]+p[0])*
                   sym_standard(cyc,shape[1]-1+p[1])*
                   sym_standard(cyc,shape[2]-2+p[2])
               for p,eps in PERMS)

@lru_cache(None)
def trunc(cyc,bound):
    return sum(sym_standard(cyc,j) for j in range(bound))

@lru_cache(None)
def trace(cyc,X,B,K,U):
    x=X;b=K+B+1;k=K+U+1;c=K+2*U+1;a=b+x
    alpha=(a+c,b+c,c)
    value=schur_three(cyc,alpha)
    if 1 in cyc:
        rest=list(cyc);rest.remove(1);rest=tuple(rest)
        singleton=0
        for i in range(k):
            for j in range(k-i):
                for l in range(k-i-j):
                    singleton+=schur_three(rest,(alpha[0]-i,alpha[1]-j,alpha[2]-l))
        value-=cyc.count(1)*singleton
    R=K+1
    for mask in range(1<<len(cyc)):
        chosen=tuple(cyc[i] for i in range(len(cyc)) if mask>>i&1)
        if sum(chosen)!=2:continue
        rest=tuple(cyc[i] for i in range(len(cyc)) if not(mask>>i&1))
        if chosen==(1,1):
            pair=sum(trunc(rest,s)*trunc(rest,R-s) for s in range(1,R))
        else:
            assert chosen==(2,)
            pair=-trunc(power_cycle(rest,2),R//2) if R%2==0 else 0
        value+=(-1)**((3-len(rest))*B)*sym_standard(rest,x)*pair
    return value

def main():
    rows=[]
    for n in range(1,7):
        for X,B,K,U in product(range(n),repeat=4):
            d=n-X-B-K-U-1
            if d<0:continue
            b=K+B+1;k=K+U+1;c=K+2*U+1
            lam=(d+2*K+3*B+2*X+3*U+2,
                 d+2*K+B+X+2*U+2,d+K+B+X+1,d+X,d)
            assert tuple(sorted(lam,reverse=True))==lam and sum(lam)==5*n
            ts={cyc:(-1)**((5-len(cyc))*(d+b+X+c))*trace(cyc,X,B,K,U)
                for cyc in partitions(5)}
            for mu in partitions(5):
                num=sum((120//z(cyc))*character(mu,cyc)*ts[cyc] for cyc in partitions(5))
                assert num%120==0
                expected=num//120
                value=actual(mu,n,lam)
                assert value==expected,(n,X,B,K,U,d,mu,lam,value,expected)
                rows.append(dict(n=n,X=X,B=B,K=K,U=U,d=d,
                    outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                    actual_MN=value,independent_JT_induction=expected,status='PASS'))
        print('completed T059 n',n,'coefficient cases',len(rows),flush=True)
    with (HERE/'OUTER5_GENERIC_HIGH_TWIST_MN_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        w.writeheader();w.writerows(rows)
    print('PASS T059 coefficient cases',len(rows),flush=True)
if __name__=='__main__':main()

