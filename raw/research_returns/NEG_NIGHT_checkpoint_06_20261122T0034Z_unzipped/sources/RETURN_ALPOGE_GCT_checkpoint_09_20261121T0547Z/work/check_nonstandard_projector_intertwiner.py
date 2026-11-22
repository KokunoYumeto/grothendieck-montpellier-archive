"""Independent finite verification for the actual source/TL multiplicity identification.
Uses the original Figure1 matrix, not the quarantined printed 2x2 blocks.
"""
from pathlib import Path
exec(Path('work/verify_nonstandard_central_word.py').read_text().split('\nS = ')[0])

def qi(i): return sum(q**(i-1-2*j) for j in range(i))
E=s.zeros(4); K=s.diag(q**3,q,q**-1,q**-3)
for i in range(1,4): E[i-1,i]=qi(i)*qi(4-i)
E2=s.kronecker_product(E,s.eye(4))+s.kronecker_product(K,E)
assert zero_matrix(P*E2-E2*P)
print('PASS: original Figure1 projection commutes with standard coproduct E.',flush=True)
T=[(i,j,k) for i in range(4) for j in range(4) for k in range(4) if i+j+k==3]
T2=[(i,j,k) for i in range(4) for j in range(4) for k in range(4) if i+j+k==2]
A=s.zeros(len(T)); B=s.zeros(len(T)); EE=s.zeros(len(T2),len(T))
for c,(i,j,k) in enumerate(T):
 for r,(ip,jp,kp) in enumerate(T):
  if k==kp: A[r,c]=Q[4*ip+jp,4*i+j]
  if i==ip: B[r,c]=Q[4*jp+kp,4*j+k]
 for v,co in [((i-1,j,k),qi(i)*qi(4-i)),((i,j-1,k),q**(3-2*i)*qi(j)*qi(4-j)),((i,j,k-1),q**(6-2*i-2*j)*qi(k)*qi(4-k))]:
  if v in T2: EE[T2.index(v),c]+=co
# All symbolic vectors and kernel operations below use rational functions.
ker=EE.nullspace()
assert len(ker)==4
H=s.Matrix.hstack(*ker)
print('PASS: weight3 highest-vector space has dimension4.',flush=True)
# A row minor selects coordinates without solving a full rational system.
rows=tuple(H.T.rref()[1])
Hminor=H[list(rows),:]
AA=(Hminor.inv()*A[list(rows),:]*H).applyfunc(s.cancel)
BB=(Hminor.inv()*B[list(rows),:]*H).applyfunc(s.cancel)
assert zero_matrix(A*H-H*AA) and zero_matrix(B*H-H*BB)
GG=(f*f*s.eye(4)-(AA-BB)**2).applyfunc(s.cancel)
L=3*(q**8+q**-8)+4*(q**4+q**-4)-2*(q**2+q**-2)+10
N0=(q**4-q**2+1)**2*(q**12+q**10+2*q**8+2*q**4+q**2+1)**2/q**16
assert zero_matrix(GG**2-L*GG+N0*s.eye(4))
assert s.cancel(s.trace(GG)-2*L)==0
assert AA.rank()==2 and BB.rank()==2
print('PASS: actual tensor highest-space action has the exact source quadratic G, each root twice.',flush=True)
# The channel-zero vector in the first two factors, tensored with x0.
v=s.Matrix([(-1)**i*q**(-3*i+i*(i-1)) if j==3-i and k==0 else 0 for i,j,k in T])
# Solve coproduct recurrence exactly instead of guessing a normalization.
v=s.zeros(len(T),1); v[T.index((0,3,0))]=1
for i in range(3):
 co=-q**(3-2*i)*qi(3-i)*qi(1+i)/(qi(i+1)*qi(3-i))
 v[T.index((i+1,2-i,0))]=s.cancel(co*v[T.index((i,3-i,0))])
assert zero_matrix(EE*v)
assert zero_matrix(A*v-f*v)
vcoord=(Hminor.inv()*v[list(rows),:]).applyfunc(s.cancel)
g3=q**4+2+q**-4;g4=q**6+2+q**-6;g5=q**10+2+q**-10
h=(GG-g3*s.eye(4))*(GG-g4*s.eye(4))*(GG-g5*s.eye(4))
v0=((2*GG-L*s.eye(4))*h*AA*vcoord).applyfunc(s.cancel)
assert any(z!=0 for z in v0)
# A faithful orbit spans four dimensions, verified by a rational nonzero minor
# at q=2; the exact polynomial identities above give its invariant target.
vv=s.Matrix.hstack(v0,GG*v0,BB*v0,GG*BB*v0)
det2=s.cancel(vv.subs(q,2).det())
assert det2!=0
print('PASS: explicit channel-zero evaluation gives an invertible four-vector source intertwiner; rational determinant at q2 is nonzero.',flush=True)
Path('work/nonstandard_projector_intertwiner_certificate.txt').write_text('Highest basis indices: '+repr(T)+'\nPivot rows: '+repr(rows)+'\nchannel0 coefficients: '+repr(list(v))+'\nFour-vector determinant at q=2: '+str(det2)+'\n')
