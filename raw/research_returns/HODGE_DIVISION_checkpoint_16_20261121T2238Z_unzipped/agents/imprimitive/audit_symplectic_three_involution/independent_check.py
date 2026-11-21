"""Independent HOS17--19 form counts by quadratic Gauss sums.

No author arithmetic or row classifications are imported.  The author code
has been read, so this is independent reconstruction, not a blind audit.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from math import prod
from pathlib import Path
import json
import time
import numpy as np
from flint import nmod_mat

start=time.perf_counter()
here=Path(__file__).resolve().parent
parent=here.parent.parent/'g34_eightfolds'/'bireflection'
proof=parent/'higher_odd_symplectic_three_involution_section.tex'
assert sha256(proof.read_bytes()).hexdigest()=='f976dad03ec875a46b3c25e39da81bd7af7240d6ffc2f0029e9343c61b2a8d46'

def all_digits(width):
    return ((np.arange(3**width,dtype=np.int64)[:,None]
             // (3**np.arange(width,dtype=np.int64))[None,:])%3).astype(np.int16)

def geometry(n):
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    points=all_digits(n)
    feature=np.stack([(points[:,i]*points[:,j]*(1 if i==j else 2))%3
                      for i,j in pairs],axis=1)
    A=np.zeros((n,n),dtype=np.int16)
    for i in range(0,n,2):
        A[i,i+1]=2
        A[i+1,i]=1
    transformed=(points@A.T)%3
    permutation=transformed@(3**np.arange(n,dtype=np.int64))
    return pairs,feature,A,permutation

def gauss_labels(values,n):
    counts=[np.sum(values==i,axis=1,dtype=np.int64) for i in range(3)]
    alpha=counts[0]-counts[2]
    beta=counts[1]-counts[2]
    norm=alpha*alpha-alpha*beta+beta*beta
    rank=np.full(len(values),-1,dtype=np.int16)
    disc=np.zeros(len(values),dtype=np.int16)
    for r in range(n+1):
        mask=norm==3**(2*n-r)
        rank[mask]=r
        if r%2==0:
            assert np.all(beta[mask]==0)
            base=(-1)**(r//2)*3**(n-r//2)
        else:
            assert np.all(beta[mask]==2*alpha[mask])
            base=(-1)**((r-1)//2)*3**(n-(r+1)//2)
        assert np.all(np.abs(alpha[mask])==abs(base))
        disc[mask]=np.where(alpha[mask]==base,1,2)
    assert np.all(rank>=0)
    return rank,disc

def gl(n,q):
    return prod(q**n-q**i for i in range(n))

def unitary(n,q):
    return q**(n*(n-1)//2)*prod(q**i-(-1)**i for i in range(1,n+1))

def orthogonal(rank,disc,q=3):
    if rank==0:return 1
    m=rank//2
    if rank%2:
        return 2*q**(m*m)*prod(q**(2*i)-1 for i in range(1,m+1))
    sign=(-1)**m*(1 if disc==1 else -1)
    return 2*q**(m*(m-1))*(q**m-sign)*prod(q**(2*i)-1 for i in range(1,m))

def subspaces(n,k,q):
    z=Fraction(prod(q**(n-i)-1 for i in range(k)),
               prod(q**(k-i)-1 for i in range(k)))
    assert z.denominator==1
    return z.numerator

def hermitian_forms(rank):
    z=Fraction(gl(rank,9),unitary(rank,3))
    assert z.denominator==1
    return z.numerator

tables=[]
for n in (2,4):
    pairs,features,A,perm=geometry(n)
    coefficients=all_digits(len(pairs))
    values=(coefficients@features.T)%3
    ranks,discs=gauss_labels(values,n)
    fixed=np.all(values==values[:,perm],axis=1)
    assert np.count_nonzero(fixed)==3**((n//2)**2)
    counts=Counter(zip(map(int,ranks),map(int,discs)))
    fixes=Counter(zip(map(int,ranks[fixed]),map(int,discs[fixed])))
    records=[]
    for (r,disc),total in sorted(counts.items()):
        den=orthogonal(r,disc)
        nondegenerate=Fraction(gl(r,3),den)
        assert nondegenerate.denominator==1
        assert total==subspaces(n,r,3)*nondegenerate.numerator
        count=fixes[(r,disc)]
        if count and r:
            assert r%2==0 and disc==1
            erank=r//2
            assert count==subspaces(n//2,erank,9)*hermitian_forms(erank)
            if n>=4: assert Fraction(count,total)<=Fraction(1,39)
        records.append({'rank':r,'discriminant':disc,'all':total,'fixed':count})
    tables.append({'dimension':n,'forms':len(coefficients),'fixed':int(fixed.sum()),
                   'classification':'quadratic-value Gauss norm and sign',
                   'records':records})

# Independently solve the linear fixed-form equations in dimension six.
# This uses neither Hermitian block coordinates nor the author's list.
n=6
pairs,features,A,perm=geometry(n)
t=len(pairs)
action=np.zeros((t,t),dtype=np.int16)
for k,(i,j) in enumerate(pairs):
    B=np.zeros((n,n),dtype=np.int16)
    B[i,j]=B[j,i]=1
    C=(A.T@B@A)%3
    action[:,k]=[C[x,y] for x,y in pairs]
equations=nmod_mat(((action-np.eye(t,dtype=np.int16))%3).tolist(),3)
ker,nullity=equations.nullspace()
assert nullity==9
basis=np.array([[int(ker[i,j]) for j in range(nullity)] for i in range(t)],dtype=np.int16)
all_coefficients=(all_digits(nullity)@basis.T)%3
assert np.all((all_coefficients@action.T)%3==all_coefficients)
hermitian_counts=Counter()
for offset in range(0,len(all_coefficients),1000):
    values=(all_coefficients[offset:offset+1000]@features.T)%3
    ranks,discs=gauss_labels(values,n)
    assert np.all(ranks%2==0) and np.all(discs==1)
    hermitian_counts.update(map(int,ranks//2))
assert sum(hermitian_counts.values())==19683
for erank,count in hermitian_counts.items():
    assert count==subspaces(3,erank,9)*hermitian_forms(erank)

# Reconstruct the nondegenerate ratios directly from full group orders.
R={r:Fraction(hermitian_forms(r),Fraction(gl(2*r,3),orthogonal(2*r,1)))
   for r in (1,2,3,4)}
assert R[1]==Fraction(1,3) and R[2]==Fraction(1,351)
for r in (1,2,3):
    assert R[r+1]/R[r]==Fraction(3**r+(-1)**r,
                                3**(r+1)*(3**(2*r+1)-1))<1
assert Fraction(subspaces(2,1,9),subspaces(4,2,3))*R[1]==Fraction(1,39)
assert Fraction(subspaces(3,1,9),subspaces(6,2,3))*R[1]==Fraction(1,363)

assert 81>64 # cubed form of 3^(-4/3)<1/4.
even=Fraction(1,2)*Fraction(38,39)*Fraction(1,2)
odd=Fraction(1,2)*Fraction(38,39)*Fraction(3,8)
assert even==Fraction(19,78)>Fraction(2,9)
assert odd==Fraction(19,104)>Fraction(1,6)
assert 6/(12*Fraction(2,9)-2)==9<3**3
assert 6/(12*odd-2)==Fraction(156,5)<3**4

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'elapsed_seconds':time.perf_counter()-start,
     'author_arithmetic_imported':False,'author_code_previously_read':True,
     'all_symmetric_forms':tables,
     'dimension_six_fixed_equation_nullity':nullity,
     'dimension_six_all_fixed_forms':dict(sorted(hermitian_counts.items())),
     'dimension_six_fixed_forms_total':sum(hermitian_counts.values()),
     'nondegenerate_ratios':{str(k):str(v) for k,v in R.items()},
     'even_support':str(even),'odd_support':str(odd),
     'source_ceilings':['9','156/5'],
     'proof_sha256':sha256(proof.read_bytes()).hexdigest(),
     'scope':'Independent exact finite-form counts and constants, not a substitute for universal proof/source audit',
     'model':'GPT-6 Astra Pro','effort':'inherited/not exposed','run':'HODGE_DIVISION'}
(here/'independent_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
