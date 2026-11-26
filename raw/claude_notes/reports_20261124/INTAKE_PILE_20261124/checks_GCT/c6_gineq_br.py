import numpy as np, itertools, sympy as sp
# GINEQ F-05: M_2 = sum e_ij (x) e_jk (x) e_ki in (C^4)^{(x)3}; Frobenius^2 = 8, spectral norm = 1 => nuclear = 8.
n=2
T=np.zeros((4,4,4))
for i,j,k in itertools.product(range(n),repeat=3):
    T[i*n+j,j*n+k,k*n+i]=1
print("Frobenius^2:",(T**2).sum())
rng=np.random.default_rng(3); best=0
for trial in range(200):
    a,b,c=[rng.standard_normal(4) for _ in range(3)]
    for it in range(200):
        a=np.einsum('ijk,j,k->i',T,b,c); a/=np.linalg.norm(a)
        b=np.einsum('ijk,i,k->j',T,a,c); b/=np.linalg.norm(b)
        c=np.einsum('ijk,i,j->k',T,a,b); c/=np.linalg.norm(c)
    best=max(best,abs(np.einsum('ijk,i,j,k',T,a,b,c)))
print("spectral norm (alternating maximisation, 200 starts):",round(best,10))
print("=> nuclear >= <T,T>/spec = 8; nuclear <= 8 (8 unit atoms); nuclear^2/Frob^2 = 64/8 = 8 > rank 7")
# BR_PENCIL: q = dim of image of the 2|2 flattening of det_4 / per_4 = span of second partials = 2x2 minors / permanents
X=sp.Matrix(4,4,lambda i,j: sp.Symbol(f"x{i}{j}")); vs=list(X)
for name,f in (("det4",X.det()),("per4",X.per())):
    sec=[sp.Poly(sp.diff(f,a,b),*vs) for a,b in itertools.combinations_with_replacement(vs,2)]
    mons=sorted({m for P in sec for m in P.monoms()})
    M=sp.Matrix([[P.as_dict().get(m,0) for m in mons] for P in sec])
    print(name,"2|2 flattening rank:",M.rank())
js={2:6,3:8,4:9,5:11,6:12,7:14,8:15,9:16}
print("chain 36-j+mu_j:",{j:36-j+m for j,m in js.items()}," mu_j-j:",[m-j for j,m in js.items()])
