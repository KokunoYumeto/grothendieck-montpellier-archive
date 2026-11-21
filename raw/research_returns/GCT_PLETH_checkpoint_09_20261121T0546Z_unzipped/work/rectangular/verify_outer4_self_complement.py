"""Independent cycle-index / MN check of the self-complement module formula."""
from pathlib import Path
from functools import lru_cache
import csv
from verify_rectangular import partitions, character, z
from verify_outer4_chambers import actual

HERE = Path(__file__).resolve().parent


@lru_cache(None)
def reciprocal(coefs, degree):
    if degree < 0:
        return 0
    values = [1]
    for n in range(1, degree+1):
        values.append(-sum(coefs[i]*values[n-i]
                           for i in range(1, min(n, len(coefs)-1)+1)))
    return values[degree]


# det(1-t*g) for U=[22] and W=[211], from the actual class eigenvalues.
U = {
    (1,1,1,1): (1,-2,1),
    (2,1,1): (1,0,-1),
    (2,2): (1,-2,1),
    (3,1): (1,1,1),
    (4,): (1,0,-1),
}
W = {
    (1,1,1,1): (1,-3,3,-1),
    (2,1,1): (1,1,-1,-1),
    (2,2): (1,1,-1,-1),
    (3,1): (1,0,0,-1),
    (4,): (1,-1,1,-1),
}


def expected(mu, b, k, d):
    value = 0
    for cyc in partitions(4):
        sg = (-1)**(4-len(cyc))
        tr = sg**d*(reciprocal(U[cyc],k)*reciprocal(W[cyc],b)
               +sg*reciprocal(U[cyc],k-1)*reciprocal(W[cyc],b-1))
        value += (24//z(cyc))*character(mu,cyc)*tr
    assert value % 24 == 0 and value >= 0
    return value//24


def main():
    rows=[]
    for n in range(7):
        for b in range(n+1):
            for k in range(n-b+1):
                d=n-b-k
                lam=(d+2*b+2*k,d+b+2*k,d+b,d)
                assert sum(lam)==4*n and lam[0]-lam[1]==lam[2]-lam[3]==b
                for mu in partitions(4):
                    value=actual(mu,n,lam)
                    proposed=expected(mu,b,k,d)
                    assert value==proposed,(n,b,k,d,mu,lam,value,proposed)
                    rows.append(dict(n=n,b=b,k=k,d=d,
                        outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                        cycle_index_MN=value,proposed_module=proposed,status='PASS'))
        print('completed n =',n,'cases =',len(rows),flush=True)
    with (HERE/'OUTER4_SELF_COMPLEMENT_INDEPENDENT_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS',len(rows),'self-complement cases, including',
          sum(row['b']>0 and row['k']>0 for row in rows),'strict middle-chamber cases')


if __name__=='__main__':
    main()
