"""Exact rational verification for BR_PENCIL's SDP example.
No numerical optimizer; all computations use SymPy rational arithmetic.
"""
from pathlib import Path
import json
import sympy as s

N=6
def ket(i,j):
    out=s.zeros(N,1); out[3*i+j]=1; return out

def outer(v): return v*v.T

def pt(m):
    out=s.zeros(N)
    for i in range(2):
      for j in range(3):
       for k in range(2):
        for l in range(3): out[3*i+l,3*k+j]=m[3*i+j,3*k+l]
    return out

u0=ket(0,0)+ket(1,1)
u1=ket(0,1)+ket(1,2)
P=(outer(u0)+outer(u1))/2
av=[2*ket(0,0)-ket(1,1),ket(0,1)-2*ket(1,2)]
bv=[ket(0,1)-2*ket(1,0),2*ket(0,2)-ket(1,1)]
X=sum((outer(v) for v in av),s.zeros(N))/16
Y=3*sum((outer(v) for v in bv),s.zeros(N))/16
assert P*P==P and s.trace(P)==2
assert s.Rational(3,4)*s.eye(N)-P==X+pt(Y)
assert sorted(X.eigenvals().items())==[(s.Integer(0),4),(s.Rational(5,16),2)]
assert sorted(Y.eigenvals().items())==[(s.Integer(0),4),(s.Rational(15,16),2)]
z=s.Matrix([1,2,1,1,2,1]); rho=outer(z)/12
assert s.trace(rho)==1 and rho.rank()==1 and pt(rho)==rho
assert s.trace(P*rho)==s.Rational(3,4)
assert X*z==s.zeros(N,1) and Y*z==s.zeros(N,1)
# Karatsuba rank-three decomposition, exact integral coefficient arrays.
T=s.MutableDenseNDimArray.zeros(2,2,3)
for ijk in [(0,0,0),(0,1,1),(1,0,1),(1,1,2)]: T[ijk]=1
terms=[([1,0],[1,0],[1,-1,0]),([0,1],[0,1],[0,-1,1]),([1,1],[1,1],[0,1,0])]
S=s.MutableDenseNDimArray.zeros(2,2,3)
for a,b,c in terms:
 for i in range(2):
  for j in range(2):
   for k in range(3): S[i,j,k]+=a[i]*b[j]*c[k]
assert S==T
flat=s.Matrix(3,4,lambda k,l:T[l//2,l%2,k])
assert flat.rank()==3
out={
 'certificate':'exact rational PPT primal/dual',
 'alpha':'3/4',
 'dual_lambda':'3/4',
 'projector':str(P),
 'X_psd_gram_vectors':[[str(x) for x in v] for v in av],
 'X_scale':'1/16',
 'Y_psd_gram_vectors':[[str(x) for x in v] for v in bv],
 'Y_scale':'3/16',
 'primal_product_state_numerator':[int(x) for x in z],
 'primal_density_denominator':12,
 'duality_gap':0,
 'karatsuba_tensor_rank':3,
 'karatsuba_tensor_border_rank':3,
 'all_assertions':'PASS'
}
Path(__file__).with_name('certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
