"""R045 independent multiset-block reconstruction, split maps and endpoints."""
from pathlib import Path
from collections import Counter,defaultdict
from itertools import product
from functools import lru_cache
from math import comb
import sympy as s
import json,time
start=time.monotonic();HERE=Path(__file__).resolve().parent
a,n=s.symbols('a n')
types=tuple((p,d-p) for d in range(1,5) for p in range(d+1))
raw={t:s.Symbol('r%d%d'%t) for t in types}
mom={t:s.Symbol('m%d%d'%t) for d in range(2,9) for t in ((p,d-p) for p in range(d+1))}

def generators(M):
    A,B,C=M[2,0],M[1,1],M[0,2]
    P,Q,R,T=M[3,0],M[2,1],M[1,2],M[0,3]
    D,E,F,G,H=M[4,0],M[3,1],M[2,2],M[1,3],M[0,4]
    return ((A*C-B*B)**2,
      C*C*D-4*C*B*E+(2*A*C+4*B*B)*F-4*A*B*G+A*A*H,
      2*(C*(P*R-Q*Q)-B*(P*T-Q*R)+A*(Q*T-R*R)),
      2*(D*H-4*E*G+3*F*F))

def centered(p,q):
    return s.expand(sum(comb(p,i)*comb(q,j)*(-raw[1,0]/a)**(p-i)*(-raw[0,1]/a)**(q-j)*
                        (raw[i,j] if i+j else a) for i in range(p+1) for j in range(q+1)))

@lru_cache(None)
def blocks(pattern):
    """Choose the block containing the first labeled factor, by submultisets."""
    if not pattern:return (((),1),)
    first=pattern[0];counts=Counter(pattern[1:]);keys=tuple(counts)
    out=defaultdict(int)
    for choice in product(*(range(counts[t]+1) for t in keys)):
        total=(first[0]+sum(v*t[0] for t,v in zip(keys,choice)),
               first[1]+sum(v*t[1] for t,v in zip(keys,choice)))
        if sum(total)==1:continue
        remaining=tuple(sorted(t for t,v in zip(keys,choice) for _ in range(counts[t]-v)))
        multiplicity=1
        for t,v in zip(keys,choice):multiplicity*=comb(counts[t],v)
        for rest,coefficient in blocks(remaining):
            out[tuple(sorted((total,)+rest))]+=multiplicity*coefficient
    return tuple(out.items())

central={t:centered(*t) for t in types if sum(t)>=2}
polys=[s.Poly(s.expand(f),*(raw[t] for t in types)) for f in generators(central)]
formal=[s.expand(f) for f in generators(mom)]
fall=[s.prod(a-j for j in range(r)) for r in range(9)]
pick=(((1,1),)*4,tuple(sorted(((0,2),(0,2),(4,0)))),
      tuple(sorted(((0,2),(3,0),(1,2)))),tuple(sorted(((4,0),(0,4)))))
rows=[];all_residuals=[]
for P in polys:
    coefficients=defaultdict(lambda:s.Integer(0))
    for powers,q in P.terms():
        pattern=tuple(sorted(t for t,e in zip(types,powers) for _ in range(e)))
        for partition,number in blocks(pattern):coefficients[partition]+=q*number*fall[len(partition)]
    coefficients={p:s.factor(v) for p,v in coefficients.items() if s.factor(v)!=0}
    assert all(sum(t)<=4 for p in coefficients for t in p)
    actual=sum(v*s.prod(mom[t] for t in p) for p,v in coefficients.items())
    selected=[coefficients.get(p,0)/d for p,d in zip(pick,(1,1,2,2))]
    assert s.expand(actual-sum(q*f for q,f in zip(selected,formal)))==0
    rows.append([s.factor(q/fall[3]) for q in selected]);all_residuals.append(0)
C=s.Matrix(rows)
source=json.loads((HERE.parent/'rectangular'/'DOUBLE_FOUR_MOMENT_MATRIX.json').read_text())
expected=s.Matrix([[s.sympify(v,locals={'a':a}) for v in row] for row in source['matrix']])
assert all(s.factor(z)==0 for z in C-expected)
assert s.factor(C.det()-(a-5)*(a-4)**2*(a-3)**3/a**6)==0

# Literal Wick substitution in all four independent formal polynomials.
A,B,D=mom[2,0],mom[1,1],mom[0,2]
wick={(4,0):3*A*A,(3,1):3*A*B,(2,2):A*D+2*B*B,(1,3):3*B*D,(0,4):3*D*D}
N2=n*(n-1);N3=N2*(n-2);N4=N3*(n-3)
replacement={t:-mom[t]/N2 for t in types if sum(t)==2}
replacement.update({t:2*mom[t]/N3 for t in types if sum(t)==3})
replacement.update({t:(wick[t]-6*mom[t])/N4 for t in types if sum(t)==4})
substituted=generators(replacement)
u=N2*N2/N4;v=N2**3/N3**2
H=s.Matrix([[1,0,0,0],[8*u,-6*u,0,0],[0,0,-4*v,0],[24*u*u,-36*u*u,0,36*u*u]])
for i in range(4):assert s.factor(substituted[i]*N2**4-sum(H[i,j]*formal[j] for j in range(4)))==0
assert s.factor(H.det()-864*u**3*v)==0

relations={3:[[-s.Rational(4,3),1,0,0],[s.Rational(2,3),0,1,0],[-s.Rational(2,3),0,0,1]],
           4:[[-2,2,1,0],[0,-s.Rational(1,2),0,1]],
           5:[[s.Rational(4,5),-s.Rational(13,10),-s.Rational(2,5),1]]}
for count,R in relations.items():
    matrix=C.subs(a,count)
    assert s.Matrix(R)*matrix==s.zeros(len(R),4) and matrix.rank()==count-2
finite=[]
for aa,nn,want in [(3,4,16),(3,5,s.Rational(320,27)),(4,4,-s.Rational(27,4)),
                   (4,5,-s.Rational(110,27)),(5,5,-s.Rational(32768,28125))]:
    P=C.subs(a,aa)*H.subs(n,nn)*C.subs(a,nn);rank=aa-2
    got=s.factor(P[:rank,:rank].det());assert got==want and P.rank()==rank
    finite.append({'a':aa,'n':nn,'rank':rank,'minor':str(got)})
J=s.Matrix([[2,0,a,0]])
K=s.Matrix([[2*(a-2)*(a*a-3*a+6),-2*a*(a*a-3*a+3),0,a*a*(a-1)]])
jrow=s.simplify(J*C);krow=s.simplify(K*C)
assert jrow==s.Matrix([[2*(a-3),0,a-3,0]])
assert s.simplify(krow-s.Matrix([[2*(a-3)*(a**3-9*a*a+24*a-12),0,4*(a-3)**2,0]]))==s.zeros(1,4)
assert s.factor(C[:2,[1,3]].det()-(a-4)*(a-3)*(a-1)/(2*a**4))==0
for aa,multiple in [(4,4),(5,8)]:assert (K.subs(a,aa)-multiple*J.subs(a,aa))*C.subs(a,aa)==s.zeros(1,4)
cs=[s.factor(fall[3]*(r[0]/1296+r[2]/81)) for r in (jrow,krow)]
assert s.factor(cs[0]-fall[3]*(a-3)/72)==0
assert s.factor(cs[1]-fall[3]*(a-3)*(a**3-9*a*a+56*a-108)/648)==0
out={'statement':'R045 independent full polynomial matrix and endpoint reconstruction','status':'PASS',
     'method':'submultiset recursion for block containing first labeled raw factor; exact rational reconstruction; independent full Wick substitution',
     'raw_monomial_counts':[len(P.terms()) for P in polys],'matrix_entries':16,'full_polynomial_residuals':all_residuals,
     'determinant':str(s.factor(C.det())),'split_rows':4,'split_determinant':str(s.factor(H.det())),
     'finite_relations_checked':6,'finite_canonical_minors':finite,'cubic_scalars':[str(z) for z in cs],
     'elapsed_seconds':time.monotonic()-start}
(HERE/'DOUBLE_FOUR_INDEPENDENT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
