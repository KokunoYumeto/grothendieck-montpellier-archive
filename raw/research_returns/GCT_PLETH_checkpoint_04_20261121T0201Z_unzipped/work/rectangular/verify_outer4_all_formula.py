"""Independent full-rank-four plethysm checks of T037's positive module formula.

Actual: s_mu[h_n] cycle-index / Murnaghan--Nakayama.
Proposed: exact S4 class traces of the stated Sym(U), H_C,b modules,
with induction computed by fixed points of a literal permutation.
"""
from pathlib import Path
import csv
from verify_rectangular import partitions, character, z
from verify_outer4_chambers import actual, transpose
from verify_outer4_self_complement import reciprocal, U, W

HERE = Path(__file__).resolve().parent


def induced(cyc,b):
    if b<0:return 0
    if cyc==(1,1,1,1):return 4*(b+1)
    if cyc==(2,1,1):return 2*reciprocal((1,0,-1),b)
    if cyc==(3,1):return reciprocal((1,1,1),b)
    return 0


def H(cyc,C,b):
    sg=(-1)**(4-len(cyc))
    sb=reciprocal(W[cyc],b)
    if C==0:return sb
    if C==1:
        return sg*(reciprocal(W[cyc],1)*sb-reciprocal(W[cyc],b-1))
    if C==2:return induced(cyc,b)+sg*reciprocal(W[cyc],b-1)
    return induced(cyc,b)


def expected(mu,n,lam):
    original=(mu,n,lam)
    complemented=lam[0]-lam[1]<lam[2]-lam[3]
    if complemented:
        height=lam[0]
        lam=(height-lam[3],height-lam[2],height-lam[1],0)
        n=height-n
        if height%2:mu=transpose(mu)
    a,b,c,d=lam[0]-lam[1],lam[2]-lam[3],lam[1]-lam[2],lam[3]
    k=max(0,lam[1]-n)
    assert a>=b and c>=2*k,(original,a,b,c,d,k)
    value=0
    for cyc in partitions(4):
        sg=(-1)**(4-len(cyc))
        tr=sum(reciprocal(U[cyc],j)*H(cyc,c-2*j,b)
               for j in range(k,c//2+1))
        if c==2*k:
            tr+=sg*reciprocal(U[cyc],k-1)*reciprocal(W[cyc],b-1)
        tr*=sg**d
        value+=(24//z(cyc))*character(mu,cyc)*tr
    assert value%24==0 and value>=0,(original,value)
    return value//24,complemented,k


def main():
    rows=[]
    for n in range(7):
        for part in partitions(4*n):
            if len(part)>4:continue
            lam=part+(0,)*(4-len(part))
            for mu in partitions(4):
                value=actual(mu,n,lam)
                proposed,complemented,k=expected(mu,n,lam)
                assert value==proposed,(n,mu,lam,value,proposed)
                rows.append(dict(n=n,outer=','.join(map(str,mu)),
                    output=','.join(map(str,lam)),complemented=int(complemented),
                    normalized_k=k,strict_central=int(lam[1]>n>lam[2]),
                    cycle_index_MN=value,proposed_module=proposed,status='PASS'))
        print('completed n =',n,'cases =',len(rows),flush=True)
    with (HERE/'OUTER4_ALL_FORMULA_INDEPENDENT_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS',len(rows),'full-rank-four cases; strict central =',
          sum(row['strict_central'] for row in rows))


if __name__=='__main__':
    main()
