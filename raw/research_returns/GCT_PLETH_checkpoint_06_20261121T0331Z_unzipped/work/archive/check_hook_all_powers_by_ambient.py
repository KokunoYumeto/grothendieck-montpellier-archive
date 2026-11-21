"""T043 fixed table reconstructed from ambient Schur sections minus jets."""
from pathlib import Path
from functools import lru_cache
from itertools import product
from math import comb
import hashlib,json,sys
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
THETA=HERE.parent/"theta"/"outer5"
sys.path.insert(0,str(HERE.parent/"rectangular"))
from verify_rectangular import character,z as centralizer
CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
SIZES=tuple(120//centralizer(cycle) for cycle in CLASSES)
CHARS=tuple(tuple(character(mu,cycle) for cycle in CLASSES) for mu in LABELS)


@lru_cache(None)
def h(g,n):
    if n<0:return 0
    if g==0:return comb(n+3,3)
    if g==1:return (n//2+1)*((n+1)//2+1)
    if g==2:return n//2+1 if n%2==0 else 0
    if g==3:return n//3+1
    if g==4:return (1,-1,1,0,0,0)[n%6]
    if g==5:return int(n%4==0)
    return (1,-1,0,0,0)[n%5]


def ambient_trace(g,x,k):
    a=x+1
    H=lambda n:h(g,n)
    cofactor0=H(a)*H(x)-H(a+1)*H(x-1)
    cofactor1=H(a-1)*H(x)-H(a+1)*H(x-2)
    cofactor2=H(a-1)*H(x-1)-H(a)*H(x-2)
    ambient=(1,-1,1,1,-1,-1,1)[g]**a * (
        H(a+2*k)*cofactor0-H(a+2*k+1)*cofactor1+H(a+2*k+2)*cofactor2)
    HW=lambda n:H(n)-H(n-1)
    fiber=HW(a)*HW(1)-HW(a+1)*HW(0)
    return ambient-CLASSES[g].count(1)*H(k-1)*fiber


arrays=[]
for g in range(7):
    rows=[[ambient_trace(g,x,k) for k in range(240)] for x in range(240)]
    assert max(abs(value) for row in rows for value in row)<2**63
    arrays.append(np.array(rows,dtype=np.int64))
weights=[tuple(size*ch for size,ch in zip(SIZES,row)) for row in CHARS]
bound=max(sum(abs(weight)*int(np.abs(array).max())
              for weight,array in zip(row,arrays)) for row in weights)*2**6
assert bound<2**63
target=json.loads((THETA/"HOOK_ALL_POWERS_TABLE.json").read_text())["labels"]
table_hashes={}
zeros={}
checked=0
minimum=None
maximum=0
for mu,row in zip(LABELS,weights):
    key=",".join(map(str,mu))
    values=sum(weight*array for weight,array in zip(row,arrays))
    assert np.all(values%120==0)
    values//=120
    assert values.min()>=0
    expected=np.array(target[key],dtype=np.int64)
    table=np.empty((60,60,16),dtype=np.int64)
    for i,j in product(range(4),repeat=2):
        diff=np.zeros((60,60),dtype=np.int64)
        for u in range(i+1):
            for v in range(j+1):
                diff+=((-1)**(i+j-u-v)*comb(i,u)*comb(j,v)*
                       values[60*u:60*(u+1),60*v:60*(v+1)])
        assert np.array_equal(diff,expected[:,:,4*i+j]),(mu,i,j)
        assert diff.min()>=0
        if (i,j)==(3,3):assert not np.any(diff)
        elif i+j:
            assert diff.min()>0
            minimum=int(diff.min()) if minimum is None else min(minimum,int(diff.min()))
        maximum=max(maximum,int(diff.max()))
        table[:,:,4*i+j]=diff
        checked+=diff.size
    zeros[key]=[list(map(int,p)) for p in np.argwhere(table[:,:,0]==0)]
    table_hashes[key]=hashlib.sha256(table.astype("<i8").tobytes()).hexdigest()
assert checked==403200 and minimum==941 and maximum==1213066800

# Verify each rational factor's proper common denominator from the literal
# seven cycle polynomials; no supplied rational-factor list is called.
z,t=sp.symbols("z t")
factor_checks=[]
def even_to_t(poly):
    out=0
    for (power,),coefficient in sp.Poly(sp.expand(poly),z).terms():
        assert power%2==0
        out+=coefficient*t**(power//2)
    return out
for g,cycle in enumerate(CLASSES):
    D=sp.cancel(sp.prod(1-z**ell for ell in cycle)/(1-z))
    H=1/D
    den=even_to_t(D*D.subs(z,-z))
    even=sp.cancel(even_to_t((D+D.subs(z,-z))/2)/den)
    odd=sp.cancel(even_to_t(sp.cancel((D.subs(z,-z)-D)/(2*z)))/den)
    fixed=cycle.count(1);e=fixed-1
    J=fixed*t*H.subs(z,t)
    factors=(sp.cancel(((e-1/z)*H+1/z)/z),
             sp.cancel(even-J).subs(t,z),H,
             sp.cancel(t*even-e*t*odd+(e-1)*J).subs(t,z))
    for index,factor in enumerate(factors):
        num=sp.cancel(factor*(1-z**60)**4)
        numerator,denominator=sp.fraction(num)
        assert sp.Poly(denominator,z).degree()==0
        degree=sp.Poly(numerator,z).degree()
        assert degree<=239
        factor_checks.append([g,index,int(degree) if degree!=sp.S.NegativeInfinity else -1])
assert len(factor_checks)==28
receipt={
    "statement":"T043 independent ambient-Schur and jet reconstruction",
    "status":"PASS","fixed_coefficients_compared":checked,
    "method":"3x3 Jacobi-Trudi ambient module, actual fat-point jets, elementary closed traces",
    "minimum_positive_order_constant":minimum,"maximum_constant":maximum,
    "signed64_intermediate_bound":bound,"proper_denominator_checks":factor_checks,
    "zero_pairs":zeros,"constant_table_sha256":table_hashes,
}
(HERE/"HOOK_ALL_POWERS_AMBIENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({key:value for key,value in receipt.items()
                  if key not in ("proper_denominator_checks","zero_pairs","constant_table_sha256")},indent=2))
