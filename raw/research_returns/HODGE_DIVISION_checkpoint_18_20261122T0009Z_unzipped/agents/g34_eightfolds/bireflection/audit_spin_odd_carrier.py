#!/usr/bin/env python3
"""Independent order-four carrier reconstruction for D-OL22--24.
Actual finite-field matrices and separate exact cyclotomic trace counts.
No author checker or selected cases are imported.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,itertools,time
import numpy as np
from flint import nmod_mat

BASE=Path(__file__).resolve().parent
start=datetime.now(timezone.utc).isoformat();timer=time.perf_counter()
def eye(n,p):return nmod_mat([[int(i==j) for j in range(n)] for i in range(n)],p)
def mat(a,p=3):return nmod_mat(np.asarray(a,dtype=int).tolist(),p)
def arr(a):return np.array(a.tolist(),dtype=np.int64)
def block(*aa):
    n=sum(x.shape[0] for x in aa);out=np.zeros((n,n),dtype=np.int64);i=0
    for x in aa:
        j=i+x.shape[0];out[i:j,i:j]=x;i=j
    return out
R=np.array([[0,1],[2,0]],dtype=np.int64)
counts={'all_dual_maps':0,'fixed_dual_maps':0,'weyl_matrix_covariances':0,'exact_trace_terms':0,'full_square_linear_characters':0}
models=[]
for N in (3,5,11,21):
    h=block(np.ones((1,1),dtype=np.int64),*([R]*((N-1)//2)))
    H=mat(h);assert H*H*H*H==eye(N,3)
    natural=block(R,h,R)
    gram=np.zeros((N+4,N+4),dtype=np.int64)
    gram[:2,N+2:]=gram[N+2:,:2]=np.eye(2,dtype=np.int64)
    gram[2:N+2,2:N+2]=np.eye(N,dtype=np.int64)
    G=mat(natural);B=mat(gram)
    assert G.transpose()*B*G==B and int(G.det())==1
    minus_ref=-np.eye(N+4,dtype=np.int64);minus_ref[2,2]=1
    assert G*G==mat(minus_ref)
    Q=mat(np.kron(R,h))
    fixed=[2*N-(Q**j-eye(2*N,3)).rank() for j in (1,2,3)]
    assert fixed==[N-1,2*N-2,N-1]
    if N<=5:
        yy=np.array(list(itertools.product(range(3),repeat=2*N)),dtype=np.int64).reshape(-1,N,2)
        hy=np.einsum('ij,kjl->kil',h,yy)%3
        ya=np.einsum('kij,jl->kil',yy,R)%3
        keep=yy[np.all(hy==ya,axis=(1,2))]
        assert len(keep)==3**(N-1)
        for y in keep:assert mat(y).rank()==(2 if np.any(y) else 0)
        counts['all_dual_maps']+=len(yy);counts['fixed_dual_maps']+=len(keep)
    models.append({'N':N,'fixed_dimensions':fixed})

# Work modulo 13, which contains distinct primitive third/fourth roots.
# These computations certify those matrix identities; complex multiplicities
# are separately reconstructed below by exact root counts, not inferred
# solely from a modular trace.
spectra=[]
for N in (3,5):
    h=block(np.ones((1,1),dtype=np.int64),*([R]*((N-1)//2)))
    vv=np.array(list(itertools.product(range(3),repeat=N)),dtype=np.int64)
    a=len(vv);ph=(vv@h@vv.T)%3
    z=3;sqrt3=4;assert pow(z,3,13)==1 and sqrt3*sqrt3%13==3
    scale=pow(pow(sqrt3,N,13),-1,13)
    K=nmod_mat([[scale*pow(z,int(c),13)%13 for c in row] for row in ph],13)
    I=eye(a,13);assert K**4==I
    ii=(1+2*z)*pow(sqrt3,-1,13)%13;assert ii*ii%13==12
    modular=[a-(K-lam*I).rank() for lam in (1,12,ii,(-ii)%13)]
    diag=[int(np.count_nonzero(np.diag(ph)==j)) for j in range(3)]
    assert diag==[3**(N-1),2*3**(N-1),0]
    # Every entry of the unnormalised complex square is a sum of one
    # linear additive character on F3^N. It equals a precisely where
    # its coefficient is zero and vanishes elsewhere. Check all pairs
    # by coefficients, rather than importing the author's convolution.
    cc=((vv@h)[:,None,:]+(vv@h.T)[None,:,:])%3
    zeros=np.all(cc==0,axis=2)
    expected=((-h@h@vv.T).T)%3
    target=np.all(expected[:,None,:]==vv[None,:,:],axis=2)
    assert np.array_equal(zeros,target) and np.all(zeros.sum(axis=1)==1)
    counts['full_square_linear_characters']+=a*a
    # 1+2 zeta_3=i sqrt(3). Exact characteristic-zero traces of K:
    # tr(K)=i*3^((N-1)/2), tr(K^2)=3^(N-1), tr(K^3)=conj tr(K).
    # The square kernel identity is independently checked by each root count.
    square_fixed=0
    for x in range(a):
        counts['exact_trace_terms']+=a
        ex=(ph[x,:]+ph[:,x])%3
        cc=[int(np.count_nonzero(ex==j)) for j in range(3)]
        assert cc==[a,0,0] or cc==[a//3]*3
        square_fixed+=int(cc==[a,0,0])
    assert square_fixed==3**(N-1)
    b=3**((N-1)//2);c=3**(N-1)
    exact=[F(a+c,4),F(a+c,4),F(a-c+2*b,4),F(a-c-2*b,4)]
    assert all(x.denominator==1 and x>=0 for x in exact)
    exact=[int(x) for x in exact]
    assert modular==exact and sum(exact)==a and max(exact)<F(9*a,16)
    if N==3:
        pos={tuple(x):i for i,x in enumerate(vv)}
        def weyl(u,v):
            out=np.zeros((a,a),dtype=np.int64)
            for j,x in enumerate(vv):
                k=pos[tuple((x+u)%3)]
                out[k,j]=pow(z,int((v@x+2*(v@u))%3),13)
            return mat(out,13)
        Ki=K**3
        for u in vv:
            for v in vv:
                assert K*weyl(u,v)*Ki==weyl((-h@v)%3,(h@u)%3)
                counts['weyl_matrix_covariances']+=1
    spectra.append({'N':N,'degree':a,'exact_complex_multiplicities':exact,
                    'mod13_kernel_multiplicities':modular,'trace_phase_counts':diag})

# A different primitive eighth-root 2x2 model over F3.
C=mat([[0,1],[1,2]])
assert C**4==-eye(2,3) and C**8==eye(2,3)
J=block(arr(C),arr(C.inv().transpose()))
g8=mat(block(np.ones((1,1),dtype=np.int64),J,J))
half=np.zeros((4,4),dtype=np.int64);half[:2,2:]=half[2:,:2]=np.eye(2,dtype=np.int64)
B8=mat(block(np.ones((1,1),dtype=np.int64),half,half))
assert g8.transpose()*B8*g8==B8 and int(g8.det())==1
minus_r=-np.eye(9,dtype=np.int64);minus_r[0,0]=1
assert g8**4==mat(minus_r)
restricted=[9-(g8**2-s*eye(9,3)).rank() for s in (1,-1)]
assert restricted==[1,0]
beta=F(4997,30000);delta=(1-F(19,20)**9)/2
assert F(1,6)<delta<F(3,16)<F(7,32)
assert 13*beta-2>F(1,7) and 11*beta+delta-2>F(1,60)
assert 2*beta*(1-beta)>F(1,4)
assert F(1,4)*(1+F(1,3)+F(2,3**11))<F(9,16)
assert F(4,3**19)<F(1,8)
proof=BASE.parent.parent/'imprimitive/spin_odd/spin_odd_extension_section.tex'
result={'status':'PASS','started_utc':start,'completed_utc':datetime.now(timezone.utc).isoformat(),
        'elapsed_seconds':time.perf_counter()-timer,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'counts':counts,'natural_models':models,'carrier_spectra':spectra,
        'order_eight_square_restricted_dimensions':restricted,
        'scope':'Independent finite natural/matrix/carrier identities and exact rational constants; no universal group, field classification, Clifford lift, or source theorem inferred from finite cases.'}
(BASE/'audit_spin_odd_carrier.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
