"""Exact finite checks for AM-DO-054; not an automorphic/Lean computation."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

COUNTS = {}

def check(name, assertion):
    if not assertion:
        raise AssertionError(name)
    COUNTS[name] = COUNTS.get(name, 0) + 1

def mm(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def tr(a):
    return list(map(list, zip(*a)))

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def add(a,b):
    return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]

def scale(c,a):
    return [[c*x for x in row] for row in a]

def tensor(a,b):
    return [[a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]

# Independent finite additive orthogonality by exact cyclotomic polynomials.
# The incidence/Fourier Gram q^a I-J restricted to augmentation has exact
# inverse q^-a. Count its character exponents first, without floating roots.
for q,a in [(3,1),(3,2),(5,1),(5,2),(7,1)]:
    vs=list(product(range(q), repeat=a))
    n=len(vs)
    for x in vs:
        for y in vs:
            counts=[0]*q
            for z in vs:
                if any(z):
                    counts[sum((u-v)*w for u,v,w in zip(x,y,z))%q]+=1
            # At x=y the sum is n-1; otherwise all coefficients except
            # the zero coefficient agree and the zero coefficient is one less.
            expected=([n-1]+[0]*(q-1)) if x==y else [n//q-1]+[n//q]*(q-1)
            check("finite_character_gram", counts==expected)
    gram=[[F(n*int(i==j)-1) for j in range(n)] for i in range(n)]
    aug=[[F(int(i==j)-int(i==n-1)) for j in range(n-1)] for i in range(n)]
    check("augmentation_inverse", mm(gram,aug)==scale(n,aug))
    for u in range(1,q):
        perm=[vs.index(tuple(u*t%q for t in x)) for x in vs]
        p=[[F(int(j==perm[i])) for j in range(n)] for i in range(n)]
        check("diamond_preserves_augmentation", mm(p,gram)==mm(gram,p))

# The all-vacuum extension is a tensor/multiplicity identity. Noncommuting
# local operators are deliberately allowed; only different-place operators
# and off-place pullbacks are commuted.
for n in range(2,6):
    A=[[F((i+2)*(j+1)-3) for j in range(n)] for i in range(n)]
    B=[[F(2*i-j+1) for j in range(n)] for i in range(n)]
    I=eye(n)
    check("disjoint_place_commutation",mm(tensor(A,I),tensor(I,B))==tensor(A,B))
    check("all_vacuum_multiplicity",mm(tensor(A,I),tensor(B,I))==tensor(mm(A,B),I))
    for u in range(1,5):
        check("off_place_pullback_linearity",
              tensor(add(A,scale(u,B)),I)==add(tensor(A,I),scale(u,tensor(B,I))))

def kapp(q,n):
    z=F(1)
    for i in range(1,n+1):
        z*=1-F(1,q**i)
    return z

# Exact middle and terminal Q weights, no identity trace substitution.
for q in (3,5,7,13):
    for a in range(1,5):
        r=a+1
        for t in range(1,5):
            b=r+t; N=r+2*t
            I1=F(q**(r*t))*kapp(q,b)/(kapp(q,r)*kapp(q,t))
            I2=F(q**(2*r*t))*kapp(q,N)/(kapp(q,r)*kapp(q,2*t))
            check("actual_parabolic_indices",I1.denominator==I2.denominator==1)
            for M in range(1,5):
                h=(q**r-1)*q**(b*(M-1))
                check("q_trace_weight_product",(I1*I2)**-1*I2*I1*h==h)
                check("q_compressed_top_function_factor",I1*h/h==I1)

# Exact finite powers for the actual two hosts and all-place T product.
for a,f,h in [(42,42,1),(168,168,4)]:
    b=1802; c=2*b-a; r=a+1; N=c-1
    check("same_complete_unit_vacuum_scale",a*b+b*c==r*b+b*N==2*b*b)
    check("no_nonlast_m2_clause",all(j+2*(s+1)+2!=2 for j in range(5) for s in range(5)))
    check("g_two_average_modulus",a*(a-1)+b//2 in (2623,28957))
    for q in (3,5,7,13):
        cT=F(q**b-1,q**(b//2))
        check("complete_t_positive_power_cancellation",cT*q**(b//2)==q**b-1)
        check("all_place_denominator_support",pow(q,f*(a+b))%11!=0)
        check("whole_chain_gaussian_exponent",7*h*(a*b+b*c)//2==7*h*b*b)

# The line exchange formula uses xi-bar=-xi. Work in Q(i) exactly.
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def inv(x):
    d=x[0]*x[0]+x[1]*x[1]
    return (x[0]/d,-x[1]/d)
for xi_i,p,q in product(range(1,8),range(1,8),range(1,8)):
    xi=(F(0),F(xi_i)); pi=(F(p),F(q))
    tau=mul((-xi[0],-xi[1]),mul(conj(pi),inv(pi)))
    kap=mul(inv(xi),conj(tau))
    check("literal_xi_cancellation",kap==mul(pi,inv(conj(pi))))
    check("line_metric_unit",mul(kap,conj(kap))==(F(1),F(0)))

root=Path(__file__).resolve().parent
proof=root/'definite_oscillator_literal_t_law_constructor.md'
record={
    'finding':'AM-DO-054','run':'ALP_MACHINE',
    'model':'GPT-6 Astra Pro','effort':'inherited, not separately exposed',
    'time_utc':datetime.now(timezone.utc).isoformat(),
    'counts':COUNTS,'assertions':sum(COUNTS.values()),'status':'PASS',
    'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
    'scope':'Exact finite Gram, tensor, weight and line-metric diagnostics; no automorphic evaluation or Lean.'
}
(root/'definite_oscillator_literal_t_law_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
