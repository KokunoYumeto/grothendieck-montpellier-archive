# CUE_GCT G-06 (input of R-14): the quaternary determinantal image {det(x1A1+..+x4A4)} has dimension 2n^2+2
# (capped by C(n+3,3)). Jacobian of params -> values at N generic sample points (N >= C(n+3,3)), d det = tr(adj dM).
import numpy as np
from math import comb
rng=np.random.default_rng(7)
def adj(M):
    return np.linalg.det(M)*np.linalg.inv(M)
for n in range(2,9):
    N=comb(n+3,3)
    A=rng.standard_normal((4,n,n))+1j*rng.standard_normal((4,n,n))
    pts=rng.standard_normal((N+10,4))+1j*rng.standard_normal((N+10,4))
    J=np.zeros((N+10,4*n*n),dtype=complex)
    for r,x in enumerate(pts):
        M=np.tensordot(x,A,axes=1)
        ad=adj(M)   # d det(M) / dM_{jk} = adj(M)_{kj}
        for i in range(4):
            J[r,i*n*n:(i+1)*n*n]=(x[i]*ad.T).reshape(-1)
    s=np.linalg.svd(J,compute_uv=False)
    s=s/s[0]
    rank=int((s>1e-9).sum())
    print(f"n={n}: Jacobian rank {rank}; 2n^2+2={2*n*n+2}; C(n+3,3)={N}; min={min(2*n*n+2,N)}; gap sv {s[rank-1]:.2e} -> {s[rank] if rank<len(s) else 0:.2e}")
for n in range(2,30):
    assert comb(n+3,3)-(2*n*n+2)==comb(n-1,3)
print("identity C(n+3,3)-(2n^2+2)=C(n-1,3) holds n=2..29")
# R-14 threshold arithmetic: c_m=4m^2-2m+2 (m>=17); c_m+3>2n^2+2 <=> n^2<=2m^2-m+1
for m in range(17,200):
    c=min(comb(m+3,3),4*m*m-2*m+2)
    for n in range(m,3*m):
        assert (c+3>2*n*n+2)==(n*n<=2*m*m-m+1),(m,n)
print("threshold equivalence checked m=17..199")
print("c_16:",comb(19,3),4*256-32+2," c_17:",comb(20,3),4*289-34+2)
