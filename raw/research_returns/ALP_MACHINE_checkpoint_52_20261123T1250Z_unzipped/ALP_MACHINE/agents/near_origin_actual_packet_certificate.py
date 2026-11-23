#!/usr/bin/env python3
"""Exact diagnostics for LIFT41; no global period or Poincare value is computed."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, comb, gcd
from datetime import datetime, timezone
import hashlib, json

ROOT=Path(__file__).resolve().parent
count=0
groups={}
def ck(test,name):
    global count
    assert test,name
    count+=1
    groups[name]=groups.get(name,0)+1

class Quad:
    """Q(sqrt(-7)) with exact rational coordinates."""
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        if not isinstance(o,Quad):o=Quad(o)
        return Quad(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Quad(-self.a,-self.b)
    def __sub__(self,o):return self+-o if isinstance(o,Quad) else self+Quad(-o)
    def __rsub__(self,o):return Quad(o)+-self
    def __mul__(self,o):
        if not isinstance(o,Quad):o=Quad(o)
        return Quad(self.a*o.a-7*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def conj(self):return Quad(self.a,-self.b)
    def norm(self):return self.a*self.a+7*self.b*self.b
    def inv(self):return self.conj()*Quad(1/self.norm())
    def __truediv__(self,o):
        if not isinstance(o,Quad):o=Quad(o)
        return self*o.inv()
    def __eq__(self,o):
        if not isinstance(o,Quad):o=Quad(o)
        return self.a==o.a and self.b==o.b

def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Quad())
             for j in range(len(B[0]))] for i in range(len(A))]
def adj(A):return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def rising(n,j):
    ans=1
    for h in range(j):ans*=n+h
    return ans
def falling(n,j):return factorial(n)//factorial(n-j)

sources=[ROOT/'definite_oscillator_large_t_certificate.json',
         ROOT/'enlarged_gap_admissible_interval_certificate.json']
actual=json.loads(sources[0].read_text())['rows']
gap=json.loads(sources[1].read_text())['hosts']
tuples={
 'J14':(2,40538469,57165115,213693530251813),
 'J56':(2,95192390527,383092671043,12529843548438452388609)}
rows=[]
for row in actual:
    host=row['host'];a=int(row['a']);Q=int(row['g0'])*int(row['g1'])
    D=int(row['D']);T=int(row['T']);k=Q*Q
    pi=Quad(1+2*D,D);pik=pi+Quad(-7*k,2*k)
    R=7*k*(11*k-2);u=tuples[host];w=[Q*x for x in u]
    ck(sum(x*x for x in u)==7*(11*Q*Q-2),'literal four squares')
    ck(sum(x*x for x in w)==R,'actual positive norm')
    ck(pi.norm()==T and pik.norm()==T+R,'exact norm identity')
    ck((pi.a-1).numerator%(Q*Q)==0 and pi.b.numerator%(Q*Q)==0,'actual pi congruence')
    ck((pik.a-1).numerator%Q==0 and pik.b.numerator%Q==0,'actual negative congruence')
    ck(all(x%Q==0 for x in w),'actual positive congruence')
    ck(gcd(T,2*Q)==1 and 0<2*Q<T,'primitive at T and all primes')
    ck(pik.norm()%T==R%T and 0<R<T,'negative T component unit')
    # Work only on the four positive coordinates and the negative line.
    z=[Quad(x)/pi.conj() for x in w]+[pik/pi.conj()]
    J=[[Quad(int(i==j)*(1 if i<4 else -1)) for j in range(5)] for i in range(5)]
    E=[[Quad(int(i==j)) for j in range(5)] for i in range(5)]
    zz=mm(mm(adj([[x] for x in z]),J),[[x] for x in z])[0][0]
    ck(zz==-1,'actual norm-one vector')
    b=z[:];b[-1]=b[-1]-1;c=z[-1]
    ck(c!=1,'nonzero reflection denominator')
    outer=mm([[x] for x in b],mm(adj([[x] for x in b]),J))
    gamma=[[E[i][j]+outer[i][j]/(1-c.conj()) for j in range(5)] for i in range(5)]
    gram=mm(mm(adj(gamma),J),gamma)
    for i in range(5):
        for j in range(5):ck(gram[i][j]==J[i][j],'actual rational unitary matrix')
        ck(gamma[i][-1]==z[i],'actual negative column')
    # Selected positive valuations: bar(pi) is a unit, pi has order one.
    ck(w[0]%T!=0,'actual dual row has exact pole')
    s2=F(R,T)
    radius_bits=813 if host=='J14' else 704
    ck(s2<F(1,2**radius_bits),'actual strict radius bound')
    ck(Q<2**(45 if host=='J14' else 71),'actual Q bit bound')
    ck(T>=2**(1000 if host=='J14' else 995),'actual T bit bound')
    ck(s2<F(1,4),'actual Cartan parameter below one half')
    ck(3**11+1<Q,'translated principal separation norm margin')
    r=19 if host=='J14' else 12
    # The upper gap is reconstructed from the retained exact E_T value.
    grow=next(x for x in gap if x['host']==host)
    # Discover only the documented numerical fields; fail if schema changes.
    ell=int(grow['ell_max']) if 'ell_max' in grow else int(grow['ell_plus'])
    ck(ell<2**485,'actual upper gap bound')
    # Full q interval, including the harmless continuous envelope q=ell.
    dmax=3*ell+1
    ck(dmax+r<2**487 and r<2**5,'top lowering parameters')
    eps=F(r*(dmax+r)*R,T)
    eps_exp=321 if host=='J14' else 212
    ck(eps<F(1,2**eps_exp),'top polynomial error exponent')
    ck(eps<F(1,2),'geometric majorant range')
    # For every word, top N <= A+4a^2 ell and kappa < 2 A.
    A=2**960
    ck(4*a*a*ell+10*ell+2*a+100<A,'top kappa bound')
    cost_exp=148 if host=='J14' else 257
    ck(F(A*R,T)+4*eps<2**cost_exp,'top selected coefficient logarithmic cost')
    rows.append(dict(host=host,a=a,Q=str(Q),D=str(D),T=str(T),u=list(u),
                     R=str(R),sinh_squared_numerator=str(R),sinh_squared_denominator=str(T),
                     radius_upper=f'2^-{radius_bits}',ell_max=str(ell),top_r=r,
                     top_polynomial_error_upper=f'2^-{eps_exp-1}',
                     top_coefficient_lower=f'exp(-2^{cost_exp})'))

# Verify the split principal-frame construction with exact rational data.
for p in (3,5,7,11):
    for n in (2,3,4):
        for t in (1,2,3):
            q=[F(p*(i+1)*t) for i in range(n-1)]+[F(1+p*t)]
            l=[F(p*(i+2)) for i in range(n-1)]
            l.append((1-sum(l[i]*q[i] for i in range(n-1)))/q[-1])
            ck(sum(x*y for x,y in zip(l,q))==1,'split dual pair')
            M=[[F(int(i==j)) for j in range(n-1)]+[q[i]] for i in range(n)]
            for j in range(n-1):M[-1][j]=-l[j]/l[-1]
            ck(all(sum(l[i]*M[i][j] for i in range(n))==int(j==n-1) for j in range(n)),
               'split inverse row')
            ck(all((M[i][j]-int(i==j)).numerator%p==0 and M[i][j].denominator%p!=0
                   for i in range(n) for j in range(n)),'split principal matrix')

# Exact SU(1,1) Gauss formula against an independent power-series action.
for k in range(2,15):
    for n in range(0,18):
        for u in (F(3,5),F(5,13),F(7,25)):
            c2=1/(1-u*u);s2=c2*u*u
            direct=sum((-1)**j*comb(n,j)*rising(k+n,j)*u**(2*j)/factorial(j)
                       for j in range(n+1))
            gauss=(1-u*u)**n*sum((-s2)**j*falling(n,j)*rising(k+n-j,j)/factorial(j)**2
                                for j in range(n+1))
            ck(direct==gauss,'SU11 exact Gauss coefficient')

# Exact GL2 Pieri highest vectors, their derivatives and norm comparison.
for L in range(1,10):
    for N in range(0,11):
        for r in range(min(L,N)+1):
            terms=[]
            for h in range(r+1):
                coeff=(-1)**h*comb(r,h)
                nf=F(factorial(N-r+h)*factorial(r-h),comb(L,h))
                terms.append((r-h,coeff*coeff*nf))
            norm=sum(x[1] for x in terms)
            for j in range(r+1):
                fnorm=sum(weight*F(falling(deg,j)) for deg,weight in terms if deg>=j)
                ck(fnorm<=falling(r,j)*norm,'Pieri last-variable Fischer estimate')
                for d in (2,5,13):
                    hn=fnorm/norm*rising(d+r-j,j)
                    ck(hn<=falling(r,j)*rising(d+r-j,j),'Pieri Hilbert bound')
            ck(all(deg<=r for deg,_ in terms),'Pieri last-variable degree')

out=dict(finding='ALP-LIFT-41',status='PASS',completed_utc=datetime.now(timezone.utc).isoformat(),
         assertions=count,groups=groups,actual_rows=rows,
         input_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
         script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         scope='Exact norm/T/G/primitive arithmetic, rational unitary extension, principal split frame, rank-one Gauss identity, Pieri lowering bounds, actual top-label coefficient costs and translated principal-separation margin. No thick/thin nonzero coefficient, Poincare value, e0 projection, terminal arithmetic row or global period is computed.')
(ROOT/'near_origin_actual_packet_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
