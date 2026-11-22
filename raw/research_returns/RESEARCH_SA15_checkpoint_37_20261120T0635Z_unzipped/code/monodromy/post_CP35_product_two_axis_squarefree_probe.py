"""Bounded exact full determinant and transverse-line search for a product twist.

The twist is the explicit nontrivial order-three point (0,0) on each
supersingular elliptic factor.  A squarefree degree-nine line restriction,
if found, certifies squarefreeness of this particular homogeneous full
determinant.  It does not imply uniformity in twists or in ppav moduli.
"""
from pathlib import Path
from datetime import datetime, timezone
import json,random,time,traceback,signal
import sympy as sp
from sympy.polys.matrices import DomainMatrix

start=time.perf_counter()
output=Path(__file__).with_suffix('.output.json')
record={'status':'RUNNING','actual_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'One explicit product twist nontrivial on both axes; bounded exact determinant and line search only.'}
def save():
    record['runtime_seconds']=time.perf_counter()-start
    output.write_text(json.dumps(record,indent=2)+'\n')
def mul(a,b):
    out=0
    while b:
        if b&1:out^=a
        a<<=1;b>>=1
    return out
def divmod2(a,b):
    assert b
    q=0
    while a and a.bit_length()>=b.bit_length():
        s=a.bit_length()-b.bit_length();q^=1<<s;a^=b<<s
    return q,a
def egcd(a,b):
    ua,va,ub,vb=1,0,0,1
    while b:
        q,r=divmod2(a,b)
        a,b=b,r;ua,ub=ub,ua^mul(q,ub);va,vb=vb,va^mul(q,vb)
    return a,ua,va
def derivative(p):
    return sum(1<<(i-1) for i in range(1,p.bit_length(),2) if (p>>i)&1)
def line_eval(terms,u,v):
    powers=[]
    for a,b in zip(u,v):
        poly=a+2*b
        row=[1]
        for _ in range(9):row.append(mul(row[-1],poly))
        powers.append(row)
    ans=0
    for exponent in terms:
        term=1
        for i,e in enumerate(exponent):term=mul(term,powers[i][e])
        ans^=term
    return ans
def alarm(signum,frame):raise TimeoutError('Bounded 60-second exact line search')
signal.signal(signal.SIGALRM,alarm);signal.alarm(60)
save()
try:
    xs=sp.symbols('x00 x01 x02 x10 x11 x12 x20 x21 x22')
    A=[sp.Matrix([[1,0,0],[0,0,0],[0,1,0]]),
       sp.Matrix([[0,0,1],[0,1,0],[1,0,0]]),
       sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])]
    matrix=sum((xs[3*i+j]*sp.kronecker_product(A[i],A[j]) for i in range(3) for j in range(3)),sp.zeros(9))
    domain=sp.GF(2).poly_ring(*xs)
    d=DomainMatrix.from_Matrix(matrix).convert_to(domain).det()
    poly=sp.Poly(domain.to_sympy(d),*xs,modulus=2)
    terms=[tuple(m) for m,c in poly.terms() if int(c)%2]
    assert poly.total_degree()==9 and all(sum(m)==9 for m in terms)
    record['full_determinant_terms']=[list(m) for m in terms]
    record['full_determinant_term_count']=len(terms)
    save()
    rng=random.Random(350035)
    witness=None
    degrees={}
    for attempt in range(1024):
        u=[rng.randrange(2) for _ in range(9)]
        v=[rng.randrange(2) for _ in range(9)]
        p=line_eval(terms,u,v)
        degrees[p.bit_length()-1]=degrees.get(p.bit_length()-1,0)+1
        if p.bit_length()!=10:continue
        dp=derivative(p)
        g,U,V=egcd(p,dp)
        if g==1:
            assert mul(U,p)^mul(V,dp)==1
            witness={'attempt':attempt+1,'u':u,'v':v,'polynomial_bits':p,
                     'polynomial_exponents':[i for i in range(10) if (p>>i)&1],
                     'derivative_bits':dp,'bezout_U_bits':U,'bezout_V_bits':V,
                     'gcd':1,'leading_coefficient':1}
            break
    record['line_degree_counts']=degrees
    record['squarefree_degree_nine_line']=witness
    record['status']='PASS-SQUAREFREE-WITNESS' if witness else 'BOUNDED-NO-WITNESS'
except Exception as exc:
    record['status']='FAILED_OR_TIMEOUT';record['error']=str(exc);record['traceback']=traceback.format_exc()
finally:
    signal.alarm(0);save()
    print(json.dumps({k:v for k,v in record.items() if k!='full_determinant_terms'},indent=2))
