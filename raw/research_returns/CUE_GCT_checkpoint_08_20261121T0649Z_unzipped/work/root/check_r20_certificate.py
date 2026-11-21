"""Independent checks of R20's fixed algebraic certificate.

Permanents use Ryser's subset formula, not permutation enumeration.
The Fourier coefficient systems are solved after evaluating x/y at
distinct nodes, independently of the original coefficient-matrix code.
This verifies finite symbolic identities, not a growing-rank extrapolation.
"""
from itertools import combinations
from pathlib import Path
from datetime import datetime, timezone
import importlib.util, json
import sympy as s

ep,x,y,z,w,q=s.symbols('epsilon x y z w q')
aa=s.symbols('a0:4');bb=s.symbols('b0:4')
cc={(i,j):s.Symbol(f'c{i}{j}') for i in range(4) for j in range(5) if j not in (i,i+1)}
B=s.Matrix(4,5,lambda i,j:aa[i] if j==i else bb[i] if j==i+1 else ep*cc[i,j])
Bt=B.copy()
for (i,j) in cc: Bt[i,j]*=(-1)**(j-i-1 if j>i+1 else i-j)

def ryser(A):
    n=A.rows;ans=0
    for size in range(1,n+1):
        for S in combinations(range(n),size):
            ans+=(-1)**(n-size)*s.prod(sum(A[i,j] for j in S) for i in range(n))
    return s.expand(ans)

E=[]
for j in range(5):
    cols=[v for v in range(5) if v!=j]
    D=Bt[:,cols].det(method='berkowitz')
    delta=s.Poly(s.expand(ryser(B[:,cols])-D),ep)
    assert delta.nth(0)==delta.nth(1)==0
    E.append(s.expand(delta.nth(2)/2))
assert E[0]==E[4]==0
assert [len(s.Add.make_args(a)) for a in E[1:4]]==[6,9,6]

L=lambda c:x-c*y
V=lambda c:z-c*w
ell=lambda i:L(q**i)
v=lambda i:V(q**i)
M=s.Matrix([
 [ell(0),v(0),ep*L(2),ep*L(3),ep*V(3),0],
 [0,ell(1),v(1),ep*L(4),ep*L(3),ep*V(2)],
 [0,0,ell(2),v(2),ep*V(6),0],
 [0,ep*V(5),0,ell(3),v(3),ep*V(4)],
 [0,ep*L(2),ep*V(7),ep*L(5),ell(4),v(4)]])

forms={};grades={}
for side,A in [('row',M[1:5,1:6]),('column',M[0:5,1:5].T)]:
    sub={**{aa[i]:A[i,i] for i in range(4)},**{bb[i]:A[i,i+1] for i in range(4)},**{c:s.cancel(A[i,j]/ep) for (i,j),c in cc.items()}}
    local=[s.expand(a.subs(sub,simultaneous=True)) for a in E]
    forms[side]=[];grades[side]=[]
    for i in range(4):
        expr=s.expand(A[i,i]*local[i]-A[i,i+1]*local[i+1])
        P=s.Poly(expr,x,y,z,w)
        grade=max(a[2]+a[3] for a,c in P.terms())
        top=s.Add(*(c*x**a[0]*y**a[1]*z**a[2]*w**a[3] for a,c in P.terms() if a[2]+a[3]==grade))
        forms[side].append(s.expand(top));grades[side].append(grade)

agentfile=Path(__file__).parents[1]/'rectangular/staircase5_certificate.py'
spec=importlib.util.spec_from_file_location('agent_r20',agentfile)
agent=importlib.util.module_from_spec(spec);spec.loader.exec_module(agent)
expected=agent.top_forms([2,3,4,5,2,3,4,5,6,7])
assert all(s.expand(f-g)==0 for fs,gs in zip(forms.values(),expected) for f,g in zip(fs,gs))

P=41;Q=6;K=40;X=40
powq=lambda a:pow(Q,a,P)
def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]=(out[i+j]+u*v)%P
    return out
def roots(vals):
    out=[1]
    for val in vals:out=multiply(out,[1,-val%P])
    return out
def solve(A,C):
    n=len(A);width=len(C[0]);T=[[(x%P) for x in a+c] for a,c in zip(A,C)]
    for k in range(n):
        i=next(i for i in range(k,n) if T[i][k]);T[k],T[i]=T[i],T[k]
        inv=pow(T[k][k],-1,P);T[k]=[(v*inv)%P for v in T[k]]
        for i in range(n):
            if i==k:continue
            c=T[i][k];T[i]=[(u-c*v)%P for u,v in zip(T[i],T[k])]
    return [a[n:] for a in T]
def det(A):
    T=[a[:] for a in A];d=1
    for k in range(len(T)):
        ii=[i for i in range(k,len(T)) if T[i][k]%P]
        if not ii:return 0
        i=ii[0]
        if i!=k:T[k],T[i]=T[i],T[k];d=-d
        pivot=T[k][k]%P;d=d*pivot%P
        for i in range(k+1,len(T)):
            c=T[i][k]*pow(pivot,-1,P)%P
            for j in range(k,len(T)):T[i][j]=(T[i][j]-c*T[k][j])%P
    return d%P

matrices={};dets={}
for side,fs in forms.items():
    base=roots([powq(i) for i in range(4)] if side=='row' else [K*powq(i)%P for i in range(-5,-1)])
    columns=[base+[0],[0]+base]
    for F,g in zip(fs,grades[side]):
        a=5-g;indices=list(range(1,a+2) if side=='row' else range(a+1))
        basis=[]
        for j in indices:
            if side=='row':rs=[K*powq(u)%P for u in range(j,a+1)]+[powq(u) for u in range(1,j)]
            else:rs=[powq(u) for u in range(5-j,5)]+[pow(K,-1,P)*powq(5-a+u)%P for u in range(a-j)]
            basis.append(rs)
        # Evaluate binary forms at (x,y)=(0,1),...,(a,1).
        Qeval=[[int(s.prod(node-r for r in rs))%P for rs in basis] for node in range(a+1)]
        rhs=[]
        for node in range(a+1):
            poly=s.Poly(s.expand(F.subs({q:Q,x:node,y:1,z:1})),w)
            rhs.append([int(poly.nth(i))%P for i in range(g+1)])
        C=solve(Qeval,rhs)
        result=[0]*6
        for j,coeff in zip(indices,C):
            if side=='row':
                shift=powq(-j);scalar=pow(X,j,P)
                extra=[powq(u) for u in range(5-j,4)]+[K*powq(u)%P for u in range(-1,a-j)]
            else:
                shift=K*powq(j-5)%P;scalar=pow(X,-j,P)
                extra=[powq(u) for u in range(-a+j,0)]+[K*powq(-5+u)%P for u in range(j)]
            term=multiply([c*pow(shift,i,P)%P for i,c in enumerate(coeff)],roots(extra))
            assert len(term)==6
            result=[(u+scalar*v)%P for u,v in zip(result,term)]
        columns.append(result)
    matrices[side]=[list(r) for r in zip(*columns)];dets[side]=det(matrices[side])

certificate=json.loads(agentfile.with_suffix('.json').read_text())
assert matrices==certificate['matrices']
assert dets=={'row':16,'column':15}
cleared_value=pow(6,580,41)*pow(20,2,41)*16*15%41
assert cleared_value==22
result={'checked_utc':datetime.now(timezone.utc).isoformat(),'method':'independent Ryser permanent and Berkowitz determinant symbolic expansion; independent evaluated-basis Gaussian elimination over F41','all_passed':True,'second_order_nonzero_monomial_counts':[6,9,6],'highest_zw_degrees':grades,'matched_all_normal_forms':8,'matrices':matrices,'determinants':dets,'cleared_polynomial_value_mod41':cleared_value,'scope':'fixed finite polynomial identities and rational-function nonzero certificate, no growing-size rank extrapolation'}
Path(__file__).with_name('r20_certificate_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='matrices'}))
