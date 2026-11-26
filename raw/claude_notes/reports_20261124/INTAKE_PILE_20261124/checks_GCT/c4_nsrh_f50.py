# GCT_NSRH F50 step: d_k = (h/2)^k U_k(1/h) squarefree over F_p (p odd) when p does not divide k+1.
import sympy as sp
from math import comb
h=sp.Symbol('h')
def Pk(k):  # h^k U_k(1/h) = sum (-1)^j C(k-j,j) 2^(k-2j) h^(2j)
    return sum((-1)**j*comb(k-j,j)*2**(k-2*j)*h**(2*j) for j in range(k//2+1))
# sanity: tridiagonal determinant with diagonal 1 and off-diagonal h/2? check d_k recursion d_k = d_{k-1} - (h/2)^2 d_{k-2}
bad=[];sharp=[]
for p in [3,5,7,11,13]:
    for k in range(1,41):
        P=sp.Poly(Pk(k)*sp.Rational(1,1),h,modulus=p)
        if P.degree()<=0: continue
        g=sp.gcd(P,P.diff(h))
        sqf = g.degree()==0
        if (k+1)%p!=0 and not sqf: bad.append((p,k))
        if (k+1)%p==0: sharp.append((p,k,sqf))
print("failures of 'p not dividing k+1 => squarefree':",bad)
print("cases p|k+1 that are squarefree anyway:",[x for x in sharp if x[2]][:10], "of",len(sharp))
# tridiagonal model: det of k x k matrix with 1 on diagonal and h/2 off-diagonal
for k in range(1,9):
    T=sp.Matrix(k,k,lambda i,j: 1 if i==j else (h/2 if abs(i-j)==1 else 0))
    assert sp.expand(T.det()*2**k - Pk(k))==0, k
print("2^k * det(tridiag(h/2,1,h/2)) = h^k U_k(1/h) for k<=8")
