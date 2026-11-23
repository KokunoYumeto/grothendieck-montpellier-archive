"""Exact finite flag/class and arithmetic diagnostic for LIFT22."""
from fractions import Fraction as F
from itertools import product
from math import prod
from pathlib import Path
import json

def gl(n,q):return q**(n*(n-1)//2)*prod(q**i-1 for i in range(1,n+1))
def par_index(a,d,q):return F(gl(a+d,q),gl(a,q)*gl(d,q)*q**(a*d))

def case(q,k):
    t,d,r=1,2,k+1
    b,N=k+d,k+2*d
    # Literal first PhiGS/PhiG after entB, tested at X0.
    def first_ok(y,sharp):
        M=[[int(i==j) for j in range(k)]+[y[i]] for i in range(b)]
        for j in range(r):
            if M[j][j]!=1:return False
            for i in range(b):
                if i>j and M[i][j]!=0:return False
        if sharp and any(M[i][k]!=(1 if i==k else 0) for i in range(b)):return False
        return True
    ys=list(product(range(q),repeat=b))
    sharpY=[y for y in ys if first_ok(y,True)]
    plainY=[y for y in ys if first_ok(y,False)]
    assert sharpY==[tuple(int(i==k) for i in range(b))]
    assert len(plainY)==q**k

    upper=[(i,j) for i in range(r) for j in range(i+1,r)]
    H=[]
    for a in product(range(q),repeat=len(upper)):
        U=[[int(i==j) for j in range(r)] for i in range(r)]
        for ij,x in zip(upper,a):U[ij[0]][ij[1]]=x
        for A in product(range(q),repeat=r):
            for h in range(1,q):H.append([U[i]+[A[i]] for i in range(r)]+[[0]*r+[h]])
    def flag_ok(B):
        # flagS: bd5(k,0,k)=0; all other prefix thresholds are s.
        for s in range(r):
            threshold=0 if s==k else s
            if any(B[i][s]!=(1 if i==s else 0) for i in range(threshold,b)):return False
            if any(B[i][j] for i in range(threshold,b) for j in range(threshold)):return False
        if any(B[i][j] for i in range(r,b) for j in range(r)):return False
        return True
    Hs=[B for B in H if flag_ok(B)]
    assert len(Hs)==len(H)//q**k
    assert all(all(B[i][k]==(1 if i==k else 0) for i in range(b)) for B in Hs)
    joining_counts=[0]*q
    for B in H:
        # Identity Q_(k,d)-cell vector: Q radical is trivial.
        first_add=-sum(B[i][i+1] for i in range(k-1))%q
        full_input=-sum(B[i][i+1] for i in range(r-1))%q
        joining_counts[(first_add-full_input)%q]+=1
        if flag_ok(B):
            assert first_add==full_input
    assert joining_counts==[len(H)//q]*q
    Uq=q**(k*(k-1)//2)
    aq=F(Uq,gl(k,q));vj=F(len(Hs),gl(b,q))
    J0,J1=par_index(k,d,q),par_index(b,d,q)
    first_scale=aq**2/J0
    second_scale=q**b*vj**2/J1
    raw1=F(Uq,q**(b*k));raw2=F(len(Hs),q**(N*b-b))
    composite=first_scale*second_scale
    expected=F(q**b,J0*J1)*(aq*vj)**2
    assert composite==expected
    unit1=F(q**(b*k)*Uq,gl(k,q)**2*J0)
    unit2=F(q**(N*b)*len(Hs),gl(b,q)**2*J1)
    assert composite/(raw1*raw2)==unit1*unit2
    assert aq*vj==F(q**(k*(k-1)+(k+1)*t)*gl(t,q),gl(k,q)*gl(b,q))
    return {'q':q,'k':k,'t':t,'Y_classes_checked':len(ys),
            'unique_sharp_Y':sharpY[0],'nonsharp_Y_count':len(plainY),
            'middle_H_matrices_checked':len(H),'forced_sharp_H_order':len(Hs),
            'generic_joining_projector_zero':True,
            'composed_double_identity_scalar':str(aq*vj),
            'composed_induced_norm_scale_squared':str(composite),
            'unit_finite_composed_scale_squared':str(unit1*unit2)}

def vp(n,p):
    v=0
    while n and n%p==0:n//=p;v+=1
    return v
def fac_vp(n,p):
    r=0
    while n:n//=p;r+=n
    return r
def D(n,q):
    h=next(i for i in range(1,11) if pow(q,i,11)==1)
    c=vp(q**h-1,11)
    r=n//h
    return c*r+fac_vp(r,11)
costs=[]
for host,k,t,qs in [('J14',42,1759,(4615409,5276377)),('J56',168,1633,(22285932761,64072175441))]:
    b=k+t+1
    for q in qs:costs.append({'host_label':host,'k':k,'t':t,'b':b,'q':q,
        'first_v11':-D(k,q),'terminal_v11':D(t,q)-D(b,q),
        'composite_v11':-D(k,q)+D(t,q)-D(b,q)})
out={'status':'PASS','cases':[case(5,1),case(3,2)],'local_Haar_content_cases':costs,
     'scope':'Finite flag/class and exact arithmetic checks. No full source rank, global norm or global row-lattice claim.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
