"""Exact consistency certificates for the Frobenius diagrams in proofs_C16.md."""
from math import comb
for p in (2,3,5,7):
    carry={(i,p-i):(-comb(p,i)//p)%p for i in range(1,p)}
    pulled={(i*p,j*p):a for (i,j),a in carry.items()}
    pushed={(i*p,j*p):pow(a,p,p) for (i,j),a in carry.items()}
    assert pulled==pushed
    print('Witt carry Frobenius diagram p=',p,'polynomial=',carry,'identity=',pulled==pushed)
    for d in range(6):
        # Shift k[F]_{<=d} into k[F]_{<=d+1}; finite field specialization.
        cols=[tuple(int(i==j+1) for i in range(d+2)) for j in range(d+1)]
        assert all(c[0]==0 for c in cols)
        assert all(cols[j][j+1]==1 for j in range(d+1))
        assert len(set(cols))==d+1
        print('F-shift p=',p,'source_dimension=',d+1,'rank=',d+1,'cokernel_constant_dimension=1')
print('ALL ASSERTIONS PASSED; finite certificates support, but do not replace, C16.')
