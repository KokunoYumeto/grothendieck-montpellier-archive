"""Exact finite supplement for D-OL19, over F9 and a 64-dimensional Clifford algebra.

No imported group package or author/sibling checker.  The universal tensor-ideal,
perfectness, and represented-quotient proofs are separate from this finite test.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time

START=time.perf_counter()
STAMP=datetime.now(timezone.utc).isoformat()

# F9 = F3[t]/(t^2+1), encoded a+3b for a+bt.
def fadd(x,y): return (x%3+y%3)%3+3*((x//3+y//3)%3)
def fneg(x): return (-x%3)%3+3*((-(x//3))%3)
def fsub(x,y): return fadd(x,fneg(y))
def fmul(x,y):
    a,b,c,d=x%3,x//3,y%3,y//3
    return (a*c+2*b*d)%3+3*((a*d+b*c)%3)
def fpow(x,n):
    z=1
    while n:
        if n&1:z=fmul(z,x)
        x=fmul(x,x);n//=2
    return z
def finv(x):
    assert x
    return fpow(x,7)
def frob(x): return fpow(x,3)
def ident(x): return x
def fsum(xs):
    z=0
    for x in xs:z=fadd(z,x)
    return z

assert all(fmul(x,finv(x))==1 for x in range(1,9))
assert all(frob(frob(x))==x for x in range(9))
N=6
Q=[1,2,1,2,1,2]

def cmul_basis(a,b):
    inversions=sum(((b & ((1<<i)-1)).bit_count()) for i in range(N) if a>>i&1)
    c=2 if inversions%2 else 1
    for i in range(N):
        if (a&b)>>i&1:c=fmul(c,Q[i])
    return a^b,c

def cadd(a,b):
    out=a.copy()
    for m,x in b.items():
        out[m]=fadd(out.get(m,0),x)
        if not out[m]:del out[m]
    return out

def cscale(a,x):return {m:fmul(c,x) for m,c in a.items() if fmul(c,x)}

def cmul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            m,z=cmul_basis(i,j)
            out[m]=fadd(out.get(m,0),fmul(fmul(x,y),z))
            if not out[m]:del out[m]
    return out

def reverse(a):
    return {m:fmul(c,2 if (m.bit_count()*(m.bit_count()-1)//2)%2 else 1) for m,c in a.items()}

def mmul(a,b):
    return [[fsum(fmul(a[i][k],b[k][j]) for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def transpose(a):return [list(r) for r in zip(*a)]

def images(h,mu):
    vectors=[{1<<i:h[i][j] for i in range(N) if h[i][j]} for j in range(N)]
    ans=[]
    for m in range(1<<N):
        a={0:1}
        for j in range(N):
            if m>>j&1:a=cmul(a,vectors[j])
        ans.append(cscale(a,fpow(finv(mu),m.bit_count()//2)))
    return ans

def apply(a,imgs,sigma):
    out={}
    for m,c in a.items():out=cadd(out,cscale(imgs[m],sigma(c)))
    return out

mu=4  # 1+t, a nonsquare of norm -1.
assert fpow(mu,4)==2 and fmul(mu,frob(mu))==2
a=fmul(2,fadd(mu,1));b=fmul(2,fsub(mu,1))
H=[[0]*N for _ in range(N)]
for i in range(0,N,2):
    H[i][i]=H[i+1][i+1]=a
    H[i][i+1]=H[i+1][i]=b
gram=[[Q[i] if i==j else 0 for j in range(N)] for i in range(N)]
assert mmul(mmul(transpose(H),gram),H)==[[fmul(mu,x) for x in row] for row in gram]
imgs=images(H,mu)
checks=0
by_parity={"even_even":0,"even_odd":0,"odd_even":0,"odd_odd_twisted":0}
for i in range(1<<N):
    for j in range(1<<N):
        p,q=i.bit_count()%2,j.bit_count()%2
        left=cmul(imgs[i],imgs[j])
        right=apply(cmul({i:1},{j:1}),imgs,frob)
        if p and q:right=cscale(right,mu)
        assert left==right
        key=("even_even" if not p and not q else "even_odd" if not p else "odd_even" if not q else "odd_odd_twisted")
        by_parity[key]+=1;checks+=1

for i in range(1<<N):
    assert apply(reverse({i:1}),imgs,frob)==reverse(imgs[i])
    for x in range(9):
        assert apply({i:x},imgs,frob)==cscale(imgs[i],frob(x))

H2=mmul(H,[[frob(x) for x in row] for row in H])
mu2=fmul(mu,frob(mu))
imgs2=images(H2,mu2)
for i in range(1<<N):
    assert apply(imgs[i],imgs,frob)==imgs2[i]
    assert apply(imgs2[i],imgs2,ident)=={i:1}

# Every linear scalar multiple has the same even map; the odd map scales once.
scalar_checks=0
for s in range(1,9):
    other=images([[fmul(s,x) for x in row] for row in H],fmul(fmul(s,s),mu))
    for i in range(1<<N):
        assert other[i]==cscale(imgs[i],s if i.bit_count()%2 else 1)
        scalar_checks+=1

one={0:1}
vectors=[{1<<i:1} for i in range(N)]
e=cadd(vectors[0],vectors[1])
w=cadd(vectors[2],vectors[4])
ew=cmul(e,w)
assert cmul(e,e)=={} and cmul(ew,ew)=={}
spin_samples=[cmul(vectors[0],vectors[2])]
spin_samples += [cadd(one,cscale(ew,s)) for s in range(9)]
central={63:3}  # t times the volume element; order four and norm one.
spin_samples.append(central)
assert cmul(central,central)=={0:2}
assert apply(central,imgs,frob)==cscale(central,2)
covariance_checks=0
for g in spin_samples:
    assert cmul(reverse(g),g)==one
    gh=apply(g,imgs,frob)
    assert cmul(reverse(gh),gh)==one
    for v in vectors:
        gv=cmul(cmul(g,v),reverse(g))
        assert all(m.bit_count()==1 for m in gv)
        hv=apply(v,imgs,frob)
        left=cmul(cmul(gh,hv),reverse(gh))
        right=apply(gv,imgs,frob)
        assert left==right
        covariance_checks+=1

ROOT=Path(__file__).resolve().parent
proof=ROOT/'spin_even_extension_draft.md'
result={"result":"PASS","started_utc":STAMP,"elapsed_seconds":time.perf_counter()-START,
        "field":"F3[t]/(t^2+1)","natural_dimension":N,"clifford_dimension":1<<N,
        "semilinear_part":"nontrivial Frobenius","multiplier_encoded":mu,"multiplier_is_nonsquare":True,
        "all_basis_product_checks":checks,"product_checks_by_parity":by_parity,
        "reversal_checks":64,"coefficient_semilinearity_checks":576,
        "twisted_composition_and_fourth_power_checks":128,"scalar_rescaling_checks":scalar_checks,
        "norm_one_spin_samples":len(spin_samples),"vector_action_covariance_checks":covariance_checks,
        "central_order_four_element_inverted":True,
        "proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
        "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope":"Finite exact Clifford identities and actual norm-one samples; universal tensor quotient and all group/source statements are separate written proofs, not finite extrapolations."}
(ROOT/'semilinear_clifford_checked.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
