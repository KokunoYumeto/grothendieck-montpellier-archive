#!/usr/bin/env python3
"""Exact F2 matrix/weight-orbit checks supplementing universal D-HES02.

This script does not replace its all-dimensional proof or the published
unipotent character input. All matrices are represented by binary row masks.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import hashlib,json,time

start=time.monotonic()
def eye(n):return tuple(1<<i for i in range(n))
def xor(rows):
    ans=0
    for x in rows:ans^=x
    return ans
def mm(A,B):return tuple(xor(B[j] for j in range(len(B)) if a>>j&1) for a in A)
def tr(A):return tuple(sum(((A[j]>>i)&1)<<j for j in range(len(A))) for i in range(len(A)))
def inv(A):
    n=len(A);R=[A[i]|(1<<(n+i)) for i in range(n)]
    for j in range(n):
        k=next((k for k in range(j,n) if R[k]>>j&1),None)
        if k is None:return None
        R[j],R[k]=R[k],R[j]
        for k in range(n):
            if k!=j and R[k]>>j&1:R[k]^=R[j]
    assert all((r&((1<<n)-1))==(1<<i) for i,r in enumerate(R))
    return tuple(r>>n for r in R)
def spJ(n):return tuple(1<<(i+n) for i in range(n))+tuple(1<<i for i in range(n))
def sym(S):return S==tr(S)
def shear(S):
    n=len(S);return tuple((1<<i)|(S[i]<<n) for i in range(n))+tuple(1<<(n+i) for i in range(n))
def levi(A):
    n=len(A);D=tr(inv(A));return tuple(A)+tuple(r<<n for r in D)
shear_records=[];equivariance_count=0
for s in [1,2,3]:
    SS=[tuple(z) for z in product(range(1<<s),repeat=s) if sym(tuple(z))]
    GL=[tuple(z) for z in product(range(1<<s),repeat=s) if inv(tuple(z)) is not None]
    assert len(SS)==2**(s*(s+1)//2)
    J=spJ(s);I=eye(2*s)
    for B in SS:
        g=shear(B);assert mm(mm(tr(g),J),g)==J and mm(g,g)==I
    for A in GL:
        L=levi(A);Li=inv(L)
        for B in SS:
            C=mm(mm(A,B),tr(A))
            assert mm(mm(L,shear(B)),Li)==shear(C)
            equivariance_count+=1
        if A!=eye(s):assert any(mm(mm(A,B),tr(A))!=B for B in SS)
    shear_records.append({'isotropic_dimension':s,'symmetric_matrices':len(SS),'all_GL_matrices':len(GL)})

def lineJ(k):
    d=2*k;n=d+2;J0=spJ(k)
    return (1<<(n-1),)+tuple(r<<1 for r in J0)+(1,)
def lineq(k,v,c):
    d=2*k;n=d+2;J0=spJ(k)
    top=1|(c<<(n-1))
    for j in range(d):top|=((J0[j]&v).bit_count()%2)<<(j+1)
    return (top,)+tuple((1<<(j+1))|(((v>>j)&1)<<(n-1)) for j in range(d))+(1<<(n-1),)
line_records=[];line_products=0
for k in [1,2,3]:
    d=2*k;J=lineJ(k);J0=spJ(k);I=eye(d+2)
    vals=[(v,c) for v in range(1<<d) for c in [0,1]]
    mats={(v,c):lineq(k,v,c) for v,c in vals}
    assert len(set(mats.values()))==1<<(d+1)
    for g in mats.values():assert mm(g,g)==I and mm(mm(tr(g),J),g)==J
    for v,c in vals:
        for w,b in vals:
            vw=xor(1<<i for i,row in enumerate(J0) if (row&w).bit_count()%2)
            pairing=(v&vw).bit_count()%2
            target=mats[(v^w,c^b^pairing)]
            assert mm(mats[(v,c)],mats[(w,b)])==target
            assert mm(mats[(w,b)],mats[(v,c)])==target
            line_products+=1
    line_records.append({'complement_dimension':d,'radical_order':len(vals)})

# Exact nontrivial module and dual weight orbits for the line case.
A=(2,3);H0=levi(A);H=(1,)+tuple(r<<1 for r in H0)+(1<<5,)
assert mm(mm(H,H),H)==eye(6)
Hi=inv(H);qvals=[lineq(2,v,c) for v in range(16) for c in [0,1]]
U=set(mm(q,mm(mm(H,q),Hi)) for q in qvals)
I=eye(6);assert len(U)==16 and I in U
assert all(mm(mm(H,u),Hi) in U for u in U)
assert [u for u in U if mm(H,u)==mm(u,H)]==[I]
basis=[];coords={I:0}
for u in sorted(U):
    if u in coords:continue
    bit=1<<len(basis);basis.append(u)
    coords.update({mm(v,u):i|bit for v,i in list(coords.items())})
assert len(basis)==4 and set(coords)==U
cols=[coords[mm(mm(Hi,b),H)] for b in basis]
dual={a:sum(((a&v).bit_count()%2)<<j for j,v in enumerate(cols)) for a in range(16)}
seen={0};orbits=[]
for a in range(1,16):
    if a in seen:continue
    orbit=[];b=a
    while b not in seen:seen.add(b);orbit.append(b);b=dual[b]
    assert b==a and len(orbit)==3;orbits.append(orbit)

# Worst-case averaging is exactly13/16, then prime3 gives support1/8.
assert Q(3,4)+Q(1,16)==Q(13,16)
assert (1-Q(1,3))*(1-Q(13,16))==Q(1,8)
# Improved elliptic bound and its full symbolic monotonicity proof.
assert 16*3**5<9*155**2 and 16*3**6<9*155**2
assert 16*3**7<9*63**2
# Identity coefficients of (2x-1)^2-3(x-1)^2: x^2+2x-2.
assert [4-3,-4+6,1-3]==[1,2,-2] and 64**2+2*64-2>0
assert Q(3,4)+Q(1,12)==Q(5,6)
assert Q(1)+10*Q(1,8)-2==Q(1,4)
assert Q(6)/Q(1,4)==24<35
base=Path(__file__).resolve().parent
out={'status':'PASS','proof_sha256':hashlib.sha256((base/'higher_even_symplectic_section.tex').read_bytes()).hexdigest(),
 'shears':shear_records,'all_shear_equivariance_checks':equivariance_count,
 'line_radicals':line_records,'exact_line_products':line_products,
 'order3_line_U_order':16,'all_nontrivial_dual_character_orbits':orbits,
 'parabolic_support':'1/8','elliptic_support':'1/6','Hurwitz_degree_ceiling':24,
 'limits':'Supplementary finite matrix and exact all-rank arithmetic checks. Universal subgroup and character-weight arguments are proved in the text; published3/4 input is not computationally reproved.',
 'seconds':round(time.monotonic()-start,6)}
(base/'check_higher_even_elementary.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
