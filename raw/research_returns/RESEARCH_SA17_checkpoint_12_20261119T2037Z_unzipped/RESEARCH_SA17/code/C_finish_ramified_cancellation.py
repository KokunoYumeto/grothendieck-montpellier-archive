"""Exact finite cyclotomic ring certificate for rank-one cancellation sequences."""
from pathlib import Path
from time import perf_counter
import json
start=perf_counter()
runs=[]
for p in (3,5,7,11):
    mod=p*p; d=p-1
    zero=((0,)*d,0)
    one=((1,)+(0,)*(d-1),0)
    zeta=((0,1)+(0,)*(d-2),0)
    def add(x,y): return (tuple((a+b)%mod for a,b in zip(x[0],y[0])),(x[1]+y[1])%p)
    def neg(x): return (tuple(-a%mod for a in x[0]),-x[1]%p)
    def sub(x,y): return add(x,neg(y))
    def mul(x,y):
        c=[0]*(2*d-1)
        for i,a in enumerate(x[0]):
            for j,b in enumerate(y[0]): c[i+j]+=a*b
        for j in range(2*d-2,d-1,-1):
            a=c[j]; c[j]=0
            for i in range(d): c[j-d+i]-=a
        return (tuple(a%mod for a in c[:d]),(sum(x[0])*y[1]+sum(y[0])*x[1])%p)
    def eps(a): return ((0,)*d,a%p)
    I=[[one,zero],[zero,one]]
    def mm(A,B):
        return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
    def power(A,n):
        B=I
        for _ in range(n): B=mm(B,A)
        return B
    Z=[[zeta,zero],[zero,one]]
    assert power(Z,p)==I
    assert mul(sub(zeta,one),eps(1))==zero
    identities=0
    for s in range(p):
        Ts=[[add(one,eps(s)),one],[zero,zeta]]
        assert power(Ts,p)==I
        for t in range(p):
            P=[[one,zero],[eps(t-s),one]]
            Pi=[[one,zero],[eps(s-t),one]]
            assert mm(P,Pi)==I and mm(Pi,P)==I
            expected=[[add(one,eps(t)),one],[zero,add(zeta,eps(s-t))]]
            assert mm(mm(Pi,Ts),P)==expected
            identities+=1
    g=[(j+1)%p for j in range(p)]
    h=[2*j%p for j in range(p)]
    hi=[pow(2,-1,p)*j%p for j in range(p)]
    assert [h[g[hi[j]]] for j in range(p)]==[(j+2)%p for j in range(p)]
    for x in range(p):
        assert mul(add(one,eps(x)),add(one,eps(x)))==add(one,eps(2*x))
    runs.append({'p':p,'coefficient_ring':'(Z/p^2)[zeta]/Phi_p semidirect F_p',
                 'rank_two_Cp_actions':p,'free_line_conjugacy_exact_sequences':identities,
                 'normalizer_permutation_entries':p,'scalar_twists':p})
report={'status':'PASS','scope':'Exact arithmetic in finite cyclotomic square-zero rings; powers, invertible free-line changes of basis, triangular quotients and normalizer conjugation. Formal Grothendieck-group cancellation follows in the written proof.',
        'runs':runs,'total_actions':sum(r['rank_two_Cp_actions'] for r in runs),
        'total_exact_sequences':sum(r['free_line_conjugacy_exact_sequences'] for r in runs),
        'runtime_seconds':round(perf_counter()-start,6)}
root=Path(__file__).resolve().parents[1]
(root/'logs/C_finish_ramified_cancellation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
