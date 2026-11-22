"""Exact finite certificates for the shallow S3 structural lemmas.

The universal arguments are in C_finish_shallow_S3_draft.tex.  This program
checks finite matrix identities and all single-copy fixed cocycles, rather
than claiming that a finite rank bound proves the all-rank statements.
"""
from pathlib import Path
from itertools import product
from time import perf_counter
import json
import numpy as np

exec(Path('code/C_finish_shallow_curvature_probe.py').read_text().split('\nroots=[')[0])
exec(Path('code/C_finish_modp2_Bockstein.py').read_text().split('def homology(')[0])
start = perf_counter()

def rep(A):
    return (np.array([[redq(x[0]+x[1]) for x in row] for row in A], dtype=np.int64),
            np.array([[redq(x[1]) for x in row] for row in A], dtype=np.int64),
            np.zeros((len(A), len(A[0])), dtype=np.int64))
def em(U): return np.zeros_like(U), np.zeros_like(U), U % 3
def aa(A,B): return tuple((a+b) % 3 for a,b in zip(A,B))
def am(A,B):
    return (A[0]@B[0] % 3, (A[0]@B[1]+A[1]@B[0]) % 3,
            (A[0]@B[2]+A[2]@B[0]) % 3)
def eq(A,B): return all(np.array_equal(a,b) for a,b in zip(A,B))
def eye(n): return rep(ident(n))
def units(n):
    for i in range(n):
        for j in range(n):
            U=np.zeros((n,n), dtype=np.int64); U[i,j]=1
            yield U
def normal(U,a,b):
    """Return the canonical representative and H with U+[N,H]=normal."""
    n=2*a+b; N=np.zeros((n,n),dtype=np.int64); N[:a,a:2*a]=np.eye(a,dtype=np.int64)
    E=slice(0,a); Ff=slice(a,2*a); Y=slice(2*a,n)
    H=np.zeros_like(U)
    H[Ff,E]=-U[E,E]; H[Ff,Ff]=-U[E,Ff]
    H[Ff,Y]=-U[E,Y]; H[Y,E]=U[Y,Ff]
    W=(U+N@H-H@N)%3
    expected=np.zeros_like(U)
    expected[Ff,Ff]=(U[E,E]+U[Ff,Ff])%3
    expected[Ff,Y]=U[Ff,Y]; expected[Y,E]=U[Y,E]; expected[Y,Y]=U[Y,Y]
    assert np.array_equal(W,expected%3)
    return W,H%3

tangent_runs=[]; tangent_basis_count=inversion_basis_count=commuting_basis_count=0
for a,b in ((0,1),(1,0),(1,1),(2,1),(1,2),(2,2)):
    n=2*a+b; N=np.zeros((n,n),dtype=np.int64);N[:a,a:2*a]=np.eye(a,dtype=np.int64)
    P=np.diag([-1]*a+[1]*(a+b))
    us=list(units(n)); G=np.column_stack([(N@H-H@N).ravel() for H in us])%3
    tangent=[U for U in us if not np.any(N@U@N%3)]
    assert len(tangent)==n*n-a*a
    assert rank(G,3)==len(tangent)-(a+b)**2
    for U in tangent:
        W,H=normal(U,a,b); tangent_basis_count+=1
        Ui=P@(-U+N@U+U@N)@P%3
        Wi,_=normal(Ui,a,b)
        expected=-W%3; expected[2*a:,:a]=W[2*a:,:a]
        assert np.array_equal(Wi,expected); inversion_basis_count+=1
    Cc=ker(G,3)
    images=[]
    for j in range(Cc.shape[1]):
        U=Cc[:,j].reshape(n,n);W,_=normal(U,a,b)
        assert not np.any(W[a:2*a,2*a:]) and not np.any(W[2*a:,:a])
        images.append(W.ravel()); commuting_basis_count+=1
    assert rank(np.column_stack(images),3)==a*a+b*b
    tangent_runs.append({'a':a,'b':b,'rank':n,'tangent_dimension':len(tangent),
                         'gauge_dimension':rank(G,3),'quotient_dimension':(a+b)**2})

D=mat([[1,0,0],[0,zeta,0],[0,0,power(zeta,2)]])
swap=mat([[1,0,0],[0,0,1],[0,1,0]])
BF=mat([[0,1,pi],[pi,1,0],[neg(pi),1,0]])
BQ=mat([[0,0,1],[pi,1,F(-1,2)],[pi,-1,F(-1,2)]])
fixed_runs=[]; exhaustive_actions=coefficient_actions=conjugacies=flags=0
for name,B,sgn,arrow in [('full_gluing',BF,[-1,1,1],'B'),
                         ('sum_zero_plane',BQ,[1,-1,1],'A')]:
    T0=conjugate(D,B);s0=conjugate(swap,B)
    assert s0==mat(np.diag(sgn).tolist())
    assert mm(mm(T0,T0),T0)==ident(3)
    assert mm(mm(s0,T0),s0)==mm(T0,T0)
    assert all(valuation(x)>=0 for row in T0 for x in row)
    if arrow=='B':assert all(T0[i][2]==(one if i==2 else zero) for i in range(3))
    else:assert all(T0[2][i]==(one if i==2 else zero) for i in range(3))
    for mult in (1,2):
        # E,F,Y block order, rather than copy order.
        t0=tuple(np.kron(c,np.eye(mult,dtype=np.int64)) for c in rep(T0))
        s=np.kron(np.diag(sgn),np.eye(mult,dtype=np.int64))%3
        sr=(s,np.zeros_like(s),np.zeros_like(s));n=3*mult;I=eye(n)
        N=(t0[0]-np.eye(n,dtype=np.int64))%3
        def invol(U):return -s@(np.eye(n,dtype=np.int64)-N)@U@(np.eye(n,dtype=np.int64)-N)@s%3
        us=list(units(n))
        cond=np.column_stack([np.concatenate(((N@U@N).ravel(),(invol(U)-U).ravel())) for U in us])%3
        K=ker(cond,3);dim=K.shape[1]
        assert dim==3*mult*mult
        if mult==1:
            params=product(range(3),repeat=dim)
            trialtype='every fixed tangent cocycle'
        else:
            params=[np.zeros(dim,dtype=np.int64)]+[np.eye(dim,dtype=np.int64)[j]*c for j in range(dim) for c in (1,2)]
            trialtype='zero and both nonzero multiples of each coefficient basis vector'
        count=0
        for par in params:
            U=(K@np.array(par,dtype=np.int64)%3).reshape(n,n)
            W,H0=normal(U,mult,mult)
            if arrow=='B':
                expect=np.zeros_like(W);expect[2*mult:,:mult]=W[2*mult:,:mult]
            else:
                expect=np.zeros_like(W);expect[mult:2*mult,2*mult:]=W[mult:2*mult,2*mult:]
            assert np.array_equal(W,expect)
            Wa=2*(W+invol(W))%3
            assert np.array_equal(invol(Wa),Wa)
            diff=(U-Wa)%3
            _,H=normal(diff,mult,mult)
            H=-H%3;H=2*(H+s@H@s)%3
            assert np.array_equal((N@H-H@N)%3,diff)
            assert np.array_equal(s@H%3,H@s%3)
            P=aa(I,em(-H));Pi=aa(I,em(H));t=aa(t0,em(U));tw=aa(t0,em(Wa))
            assert eq(am(P,Pi),I) and eq(am(am(Pi,t),P),tw)
            assert eq(am(am(t,t),t),I) and eq(am(am(sr,t),sr),am(t,t))
            if arrow=='B':
                assert not np.any(Wa[:2*mult,:]) and not np.any(Wa[:,2*mult:])
            else:
                assert not np.any(Wa[2*mult:,:]) and not np.any(Wa[:,:2*mult])
            count+=1;conjugacies+=1;flags+=1
        if mult==1:exhaustive_actions+=count
        else:coefficient_actions+=count
        fixed_runs.append({'type':name,'multiplicity':mult,'rank':n,'fixed_cocycle_dimension':dim,
                           'scope':trialtype,'actions':count})

# The residual classification's averaging lift is checked on all GL2(F3)
# changes of basis for each involution normal form. The written finite-ring
# argument is what lifts this identity through the whole endomorphism radical.
average_count=0
for signs in ((1,1),(1,-1),(-1,-1)):
    s0=np.diag(signs)%3
    for flat in product(range(3),repeat=4):
        P0=np.array(flat,dtype=np.int64).reshape(2,2)
        if rank(P0,3)<2:continue
        invP=rr(np.column_stack((P0,np.eye(2,dtype=np.int64))),3)[0][:,2:]
        s=invP@s0@P0%3
        P=2*(P0+s0@P0@s)%3
        assert np.array_equal(P,P0) and np.array_equal(P@s%3,s0@P%3)
        average_count+=1

report={'status':'PASS',
 'scope':'Six block sizes through rank6: every tangent and commutant coefficient basis, canonical gauge quotient and inversion. Exact Q(zeta3) integral inversion bases for L012 and Q. Every single-copy fixed cubic cocycle for both types; zero and each coefficient direction for multiplicity2; exact order3, S3 conjugation, averaged gauge conjugacy and constant subquotient flags. Residual involution averaging through all GL2(F3) bases. No enumeration or classification of mixed isotypic shallow deformations is claimed.',
 'tangent_runs':tangent_runs,'tangent_coefficient_checks':tangent_basis_count,
 'inversion_coefficient_checks':inversion_basis_count,'commutant_coefficient_checks':commuting_basis_count,
 'fixed_runs':fixed_runs,'exhaustive_single_copy_actions':exhaustive_actions,
 'multiplicity_two_coefficient_actions':coefficient_actions,'averaged_gauge_conjugacies':conjugacies,
 'constant_subquotient_flags':flags,'residual_involution_averages':average_count,
 'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_shallow_S3.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
