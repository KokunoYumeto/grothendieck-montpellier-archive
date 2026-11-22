"""Exact finite cyclotomic unit and Hasse readout checks for C034."""
from pathlib import Path
from math import comb,isqrt
import sympy as sp
import json
T=sp.Symbol('T')
stats={'cyclotomic_quotients':0,'node_unit_identities':0,'difference_unit_identities':0,
       'integer_hasse_readout_cases':0,'monomial_readouts':0,'maximum_observed_integer_bits':0}

def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def choose(Q):
    if Q==1:return 2,3
    return next(n for n in range(Q+1,2*Q) if prime(n)),next(n for n in range(2*Q+1,4*Q) if prime(n))

class Ring:
    def __init__(self,p,q):
        self.N=p*q
        f,rem=sp.div((T**self.N-1)*(T-1),(T**p-1)*(T**q-1),domain=sp.ZZ)
        assert rem==0 and f.subs(T,1)==1
        self.f=[int(x) for x in reversed(sp.Poly(f,T).all_coeffs())]
        self.a=len(self.f)-1
        self.zero=(0,)*self.a;self.one=(1,)+(0,)*(self.a-1)
        self.z=self.reduce([0,1])
        U,rem=sp.div(f-1,T-1,domain=sp.ZZ);assert rem==0
        self.U=[int(x) for x in reversed(sp.Poly(U,T).all_coeffs())]
    def reduce(self,v):
        v=list(v)
        for k in range(len(v)-1,self.a-1,-1):
            c=v[k]
            if c:
                for j in range(self.a):v[k-self.a+j]-=c*self.f[j]
        v=(v+[0]*self.a)[:self.a]
        stats['maximum_observed_integer_bits']=max(stats['maximum_observed_integer_bits'],max(abs(x).bit_length() for x in v))
        return tuple(v)
    def add(self,a,b):return tuple(x+y for x,y in zip(a,b))
    def neg(self,a):return tuple(-x for x in a)
    def scale(self,a,c):return tuple(c*x for x in a)
    def mul(self,a,b):
        v=[0]*(2*self.a-1)
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b):
                    if y:v[i+j]+=x*y
        return self.reduce(v)
    def power(self,a,n):
        out=self.one
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n>>=1
        return out
    def evalU(self,a):
        out=self.zero
        for c in reversed(self.U):out=self.add(self.mul(out,a),self.scale(self.one,c))
        return out
    def diff_inverse(self,i,j):
        # alpha_i-alpha_j=z^j(z^(i-j)-1); (1-z^d) U(z^d)=1.
        d=(i-j)%self.N
        return self.neg(self.mul(self.power(self.z,(-j)%self.N),self.evalU(self.power(self.z,d))))

for Q in range(1,6):
    p,q=choose(Q);A=Ring(p,q);stats['cyclotomic_quotients']+=1
    nodes=[A.power(A.z,i) for i in range(1,Q+1)]
    assert A.power(A.z,A.N)==A.one
    inverses={}
    for i,alpha in enumerate(nodes,1):
        assert A.mul(alpha,A.power(A.z,A.N-i))==A.one
        stats['node_unit_identities']+=1
        for j,beta in enumerate(nodes,1):
            if i==j:continue
            inv=A.diff_inverse(i,j);inverses[i,j]=inv
            assert A.mul(A.add(alpha,A.neg(beta)),inv)==A.one
            stats['difference_unit_identities']+=1
    if Q not in (2,3):continue
    for J in (1,2,3,4):
        readout={}
        for i,alpha in enumerate(nodes,1):
            b=[A.one]+[A.zero]*(J-1);B0=A.one
            for j,beta in enumerate(nodes,1):
                if i==j:continue
                inv=inverses[i,j]
                for repeat in range(J):
                    for k in range(J-1,0,-1):b[k]=A.add(b[k],A.mul(b[k-1],inv))
                    B0=A.mul(B0,A.mul(A.neg(beta),inv))
            c=[A.one]
            for k in range(1,J):
                value=A.zero
                for l in range(1,k+1):value=A.add(value,A.mul(b[l],c[k-l]))
                c.append(A.neg(value))
            for k in range(J):
                value=A.zero
                for l in range(k,J):value=A.add(value,A.mul(c[l-k],A.power(A.neg(alpha),l)))
                readout[i,k]=A.mul(B0,value)
        for u in range(Q*J):
            value=A.zero
            for i,alpha in enumerate(nodes,1):
                for k in range(min(u,J-1)+1):
                    jet=A.scale(A.power(alpha,u-k),comb(u,k))
                    value=A.add(value,A.mul(readout[i,k],jet))
            assert value==(A.one if u==0 else A.zero)
            stats['monomial_readouts']+=1
        stats['integer_hasse_readout_cases']+=1
stats['status']='PASS'
stats['scope']='Exact finite quotient-ring and Hasse-readout identities only; not a proof of E or of the asymptotic circuit bound.'
Path(__file__).with_name('FINITE_CHECK_INTEGRAL_INTERPOLATION_RESULTS.json').write_text(json.dumps(stats,indent=2)+'\n')
print(json.dumps(stats,indent=2))
