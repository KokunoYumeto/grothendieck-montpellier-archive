"""Exact small-instance checks for the centered-SV annihilator proof."""
from itertools import combinations
from pathlib import Path
import json
import sympy as sp

reports=[]
for k in (1,2):
    m=k+1; n=3*k+2
    a=list(range(n)); y=sp.symbols('y'); xs=sp.symbols('x1:'+str(n+1))
    conditions=sp.Matrix([[sum(t**(i+j) for t in a)
                           for j in range(2*k+2)] for i in range(m)])
    kernel=conditions.nullspace()[:m]
    assert len(kernel)==m
    qs=[sum(v[j]*y**j for j in range(2*k+2)) for v in kernel]
    U=sp.Matrix([[t**i for t in a] for i in range(m)])
    V=sp.Matrix([[q.subs(y,t) for t in a] for q in qs])
    assert U*V.T == sp.zeros(m)
    assert V.rank()==m
    lam=[sp.prod((y-b)/sp.Rational(a[i]-b) for b in a if b!=a[i])
         for i in range(n)]
    for i in range(m):
        for j in range(m):
            assert sp.expand(sum(a[l]**i*qs[j].subs(y,a[l])*lam[l]
                                 for l in range(n))-y**i*qs[j])==0
    terms=[]; witness=None
    for S in combinations(range(n),m):
        coefficient=U[:,S].det()*V[:,S].det()
        if coefficient:
            witness=witness or S
            terms.append(coefficient*sp.prod(xs[l] for l in S))
    P=sp.expand(sum(terms)); assert P!=0

    minors=[(I,J) for r in range(m+1)
            for I in combinations(range(m),r)
            for J in combinations(range(m),r)]
    pos={IJ:i for i,IJ in enumerate(minors)}; W=len(minors)
    assert W==sp.binomial(2*m,m)
    Ns=[]
    for l in range(n):
        N=sp.zeros(W)
        for row,(I,J) in enumerate(minors):
            for pa,i in enumerate(I):
                for pb,j in enumerate(J):
                    small=(I[:pa]+I[pa+1:],J[:pb]+J[pb+1:])
                    N[row,pos[small]] += (-1)**(pa+pb)*U[i,l]*V[j,l]
        assert N*N==sp.zeros(W)
        Ns.append(N)
    for N,M in combinations(Ns,2): assert N*M==M*N
    state=sp.zeros(W,1);state[pos[((),())],0]=1
    for x,N in zip(xs,Ns): state=(state+x*N*state).applyfunc(sp.expand)
    full=pos[(tuple(range(m)),tuple(range(m)))]
    assert sp.expand(state[full,0]-P)==0
    reports.append({'k':k,'n':n,'width':W,'nonzero_common_minor':witness,
                    'nonzero_monomials':len(terms),'UV_transpose_zero':True,
                    'lagrange_reproduction_degree_bound':3*k+1,
                    'square_zero_and_commutation':True,
                    'minor_state_output_equals_Cauchy_Binet':True})

x=sp.symbols('x1:6'); y,z,t=sp.symbols('y z t')
Q=(3*x[0]*x[1]-4*x[0]*x[2]-15*x[0]*x[3]+16*x[0]*x[4]
   +4*x[1]*x[2]+8*x[1]*x[3]-15*x[1]*x[4]+4*x[2]*x[3]
   -4*x[2]*x[4]+3*x[3]*x[4])
lam=[sp.prod((y-j)/sp.Rational(i-j) for j in range(5) if j!=i)
     for i in range(5)]
assert sp.expand(Q.subs({x[i]:t+z*lam[i] for i in range(5)}))==0
arows=[(1,0),(0,1),(-sp.Rational(28,97),-sp.Rational(4,97)),
       (sp.Rational(3,16),0),(0,0)]
bcols=[(0,0),(3,0),(-4,4),(-15,8),(16,-15)]
word=sp.eye(4)
for xi,ai,bi in zip(x,arows,bcols):
    N=sp.zeros(4)
    N[0,1],N[0,2]=ai;N[1,3],N[2,3]=bi
    assert N**3==sp.zeros(4)
    word=(word*(sp.eye(4)+xi*N)).applyfunc(sp.expand)
assert sp.expand(word[0,3]-Q)==0
data={'general_instances':reports,
      'width4_quadratic':{'centered_SV1_zero':True,
                          'unipotent_width4_output_equals_Q':True},
      'scope':'Exact finite checks, not a general formal proof certificate.'}
out=Path(__file__).with_name('I26_computation_checks.json')
out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
