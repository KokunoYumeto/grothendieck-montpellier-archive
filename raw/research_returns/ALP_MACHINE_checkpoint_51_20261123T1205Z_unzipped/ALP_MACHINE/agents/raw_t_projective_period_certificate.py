"""Exact finite normalization diagnostics for LIFT24; no p-adic classification proof."""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
from math import prod
import json

def det(A,q):
    n=len(A);A=[r[:] for r in A];z=1
    for j in range(n):
        p=next((i for i in range(j,n) if A[i][j]%q),None)
        if p is None:return 0
        if p!=j:A[j],A[p]=A[p],A[j];z=-z
        a=A[j][j]%q;z=z*a%q;inv=pow(a,-1,q)
        for i in range(j+1,n):
            c=A[i][j]*inv%q
            for l in range(j,n):A[i][l]=(A[i][l]-c*A[j][l])%q
    return z%q
def order_gl(n,q):
    return q**(n*(n-1)//2)*prod(q**i-1 for i in range(1,n+1))
def root(q):
    return next(g for g in range(1,q) if len({pow(g,i,q) for i in range(q-1)})==q-1)
def ring_root(e,q):
    # q3: roots±1; q5: roots±1,±i.
    e%=q-1
    return ((1,0),(-1,0))[e] if q==3 else ((1,0),(0,1),(-1,0),(0,-1))[e]
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def vecmul(x,h,q):return tuple(sum(x[i]*h[i][j] for i in range(len(x)))%q for j in range(len(x)))
def compact_case(q,n):
    logs={pow(root(q),i,q):i for i in range(q-1)}
    gl=[]
    for a in product(range(q),repeat=n*n):
        h=[list(a[i*n:(i+1)*n]) for i in range(n)]
        if det(h,q):gl.append(h)
    assert len(gl)==order_gl(n,q)
    J=[h for h in gl if not any(h[-1][:-1])]
    H=[h for h in J if h[-1][-1]==1]
    dn=(q**n-1)//(q-1)
    assert len(J)*dn==len(gl)
    assert len(H)*(q**n-1)==len(gl)
    def f0(x):
        return ring_root(logs[x[-1]],q) if not any(x[:-1]) and x[-1] else(0,0)
    checks=0
    for x in product(range(q),repeat=n):
        if not any(x):continue
        su=(0,0);sn=(0,0)
        for h in H:su=add(su,f0(vecmul(x,h,q)))
        for h in J:
            sn=add(sn,mul(ring_root(-logs[h[-1][-1]],q),f0(vecmul(x,h,q))))
        expected=f0(x)
        assert su==(len(H)*expected[0],len(H)*expected[1])
        assert sn==(len(J)*expected[0],len(J)*expected[1])
        assert sn==((q-1)*su[0],(q-1)*su[1])
        checks+=1
    return dict(q=q,n=n,group_order=len(gl),H_order=len(H),J_order=len(J),
                exact_vector_checks=checks,raw_compact_scalar=str(F(len(H),len(gl))),
                line_norm_squared=str(F(1,dn)))

def schur_case(q,depth):
    mod=q**depth
    units=[x for x in range(mod) if x%q]
    Cvals=list(range(0,mod,q))
    checks=0;det_checks=0
    for Aprime,B,C,e in product(range(mod),range(mod),Cvals,units):
        inv=pow(e,-1,mod)
        A=(Aprime+B*inv*C)%mod
        assert (A-B*inv*C)%mod==Aprime
        assert (A*e-B*C)%mod==(Aprime*e)%mod
        checks+=1
        if Aprime%q:det_checks+=1
    # n2, exact Haar change factor after rank1 conversion.
    c1=F(q-1,q);c2=c1*F(q*q-1,q*q)
    haar=c1/c2*F(1,q)*c1
    assert haar==F(q-1,q*q-1)
    return dict(q=q,depth=depth,exact_schur_checks=checks,
                unit_determinant_checks=det_checks,normalized_Haar_factor=str(haar))

def vp(x,p):
    c=0
    while x%p==0:x//=p;c+=1
    return c
def v_power_minus_one(q,n,p):
    o=next(i for i in range(1,p) if pow(q,i,p)==1)
    if n%o:return 0
    return vp(pow(q,o)-1,p)+vp(n//o,p)

compact=[compact_case(3,2),compact_case(5,2),compact_case(3,3)]
schur=[schur_case(3,2),schur_case(5,2)]
cst=json.loads(Path("work/checks/explicit_t_prime_and_stabilizer_certificate.json").read_text())
actual=[]
for item in cst["cases"]:
    a,n,m,q=item["a"],item["b"],item["c"],item["T"]
    d=n-a
    assert m==n+d and d>a
    # Twice the exponent after evaluation at z0=(d+1)/2.
    initial=d-a+3
    inserted=[2+2*j for j in range(d)]
    assert initial>2 and min(inserted)==2
    first_val=v_power_minus_one(q,a,11)
    second_val=v_power_minus_one(q,n,11)
    actual.append(dict(name=item["name"],a=a,d=d,n=n,m=m,
                       min_initial_twice_decay=initial,
                       min_inserted_twice_decay=min(inserted),
                       v11_first_Haar_denominator=first_val,
                       v11_second_Haar_denominator=second_val,
                       note="L-factor valuations are not computed or discarded"))
out=dict(status="PASS",scope="compact and block normalization; no theta quotient simulation",
         compact=compact,schur=schur,actual_ranks=actual,
         exact_vector_checks=sum(x["exact_vector_checks"] for x in compact),
         exact_schur_checks=sum(x["exact_schur_checks"] for x in schur))
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

