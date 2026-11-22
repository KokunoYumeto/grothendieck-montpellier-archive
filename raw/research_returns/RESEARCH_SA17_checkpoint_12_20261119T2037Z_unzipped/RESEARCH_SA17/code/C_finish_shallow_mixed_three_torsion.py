"""Exact certificate for commuting translations and mixed full-support rotation.

This verifies the finite matrix identities used in the all-rank proof; it
is not a search claiming that a possible three-torsion class vanishes.
A=Z_3[zeta3] constants are computed exactly in Q(zeta3). All first-order
identities are F3-linear, so basis checks certify each tested rank tuple.
"""
from pathlib import Path
from time import perf_counter
import json
import numpy as np
exec(Path('code/C_finish_shallow_curvature_probe.py').read_text().split('\nroots=[')[0])
start=perf_counter()
D=mat([[1,0,0],[0,zeta,0],[0,0,power(zeta,2)]])
P=mat([[0,1,0],[0,0,1],[1,0,0]])
BL=mat([[0,1,pi],[pi,1,0],[neg(pi),1,0]])
BQ=mat([[0,0,1],[pi,1,F(-1,2)],[pi,-1,F(-1,2)]])
base={name:(conjugate(D,B),conjugate(P,B)) for name,B in [('L',BL),('Q',BQ)]}
for T,R in base.values():
    assert all(valuation(x)>=0 for M in (T,R,mi(R)) for row in M for x in row)
    assert mm(mm(T,T),T)==ident(3)
    assert mm(mm(mi(R),scale(T,zeta)),R)==T
assert [[residue(x) for x in row] for row in base['L'][1]]==[[1,0,1],[0,1,0],[0,0,1]]
assert [[residue(x) for x in row] for row in base['Q'][1]]==[[1,0,0],[0,1,0],[0,1,1]]
runs=[]
for r,s in [(1,0),(0,1),(1,1),(2,1),(1,2)]:
    a=r+s;n=3*a;names=['L']*r+['Q']*s
    T0=[[zero for _ in range(n)] for _ in range(n)]
    R=[[zero for _ in range(n)] for _ in range(n)]
    for c,name in enumerate(names):
        for i in range(3):
            for j in range(3):
                T0[i*a+c][j*a+c]=base[name][0][i][j]
                R[i*a+c][j*a+c]=base[name][1][i][j]
    assert mm(mm(mi(R),scale(T0,zeta)),R)==T0
    N=np.zeros((n,n),dtype=np.int64);N[:a,a:2*a]=np.eye(a,dtype=np.int64)
    T=np.eye(n,dtype=np.int64)+N
    Rbar=np.array([[residue(x) for x in row] for row in R],dtype=np.int64)
    C0=np.diag([1]*r+[0]*s);D0=np.diag([0]*r+[1]*s)
    K=Rbar-np.eye(n,dtype=np.int64)
    assert not np.any(K@K%3)
    Rinv=(np.eye(n,dtype=np.int64)-K)%3
    Us=[];Hs=[]
    for i in range(a):
        for j in range(a):
            for b0,b1 in [(1,1),(1,2),(2,0),(2,2)]:
                U=np.zeros((n,n),dtype=np.int64);U[b0*a+i,b1*a+j]=1;Us.append(U)
            for coords in [[(0,0),(1,1)],[(0,1)],[(0,2)],[(2,1)],[(2,2)]]:
                H=np.zeros((n,n),dtype=np.int64)
                for b0,b1 in coords:H[b0*a+i,b1*a+j]=1
                Hs.append(H)
    gauge_count=0
    for U in Us:
        assert not np.any(N@U@N%3)
        V=Rinv@U@Rbar%3
        S=U[a:2*a,a:2*a];A=U[a:2*a,2*a:];B=U[2*a:,:a];C=U[2*a:,2*a:]
        DS=(A@D0-C0@B)%3;DC=(B@C0-D0@A)%3
        assert np.array_equal((V[:a,:a]+V[a:2*a,a:2*a])%3,(S+DS)%3)
        assert np.array_equal(V[a:2*a,2*a:]%3,A)
        assert np.array_equal(V[2*a:,:a]%3,B)
        assert np.array_equal(V[2*a:,2*a:]%3,(C+DC)%3)
        H=np.zeros((n,n),dtype=np.int64);H[:a,:a]=2*DS%3;H[a:2*a,a:2*a]=2*DS%3;H[2*a:,2*a:]=DC
        assert not np.any((N@H-H@N)%3)
        diff=(V-U-H)%3;G=np.zeros((n,n),dtype=np.int64)
        G[a:2*a,:a]=diff[:a,:a]
        G[a:2*a,a:2*a]=diff[:a,a:2*a]
        G[a:2*a,2*a:]=diff[:a,2*a:]
        G[2*a:,:a]=-diff[2*a:,a:2*a]
        assert np.array_equal((N@G-G@N)%3,diff)
        assert np.trace(H)%3==0
        gauge_count+=1
    E0=[[zero for _ in range(2*n)] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            E0[i][j]=T0[i][j];E0[i+n][j+n]=mul(zeta,T0[i][j])
        E0[i][i+n]=one
    assert mm(mm(E0,E0),E0)==ident(2*n)
    E=np.array([[residue(x) for x in row] for row in E0],dtype=np.int64)
    E2=E@E%3;translations=0
    for k,U in enumerate(Us):
        K0=Hs[k%len(Hs)]
        V=(U+K0)%3
        A1=np.zeros((2*n,2*n),dtype=np.int64);A1[:n,:n]=U;A1[n:,n:]=V
        assert not np.any((E2@A1+E@A1@E+A1@E2)%3)
        for H in Hs:
            assert not np.any((N@H-H@N)%3)
            G=np.zeros((2*n,2*n),dtype=np.int64);G[n:,:n]=H
            A2=(A1+E@G-G@E)%3
            expected=np.zeros_like(A2);expected[:n,:n]=(U+H)%3;expected[n:,n:]=(V-H)%3
            assert np.array_equal(A2,expected)
            assert not np.any((E2@A2+E@A2@E+A2@E2)%3)
            translations+=1
    runs.append({'L_copies':r,'Q_copies':s,'rank':n,'tangent_basis_vectors':len(Us),'commutant_basis_vectors':len(Hs),'rotation_gauge_checks':gauge_count,'actual_first_order_cubic_extension_and_shear_checks':translations})
report={'status':'PASS','scope':'Exact Q(zeta3) constant rotations and cubic extensions; F3-linear tangent and commutant basis identities for the five displayed rank tuples. This is a certificate of identities used in the all-rank proof, not a vanishing test and not evidence of nonzero three-torsion. Arbitrary J and all multiplicities are covered by the written block proof, not by finite enumeration.','runs':runs,'rotation_gauge_checks':sum(x['rotation_gauge_checks'] for x in runs),'extension_shear_checks':sum(x['actual_first_order_cubic_extension_and_shear_checks'] for x in runs),'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_shallow_mixed_three_torsion.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
