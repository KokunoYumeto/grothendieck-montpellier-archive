#!/usr/bin/env python3
"""Independent Fock-matrix check of D-OL19 identities, not a group proof.
F9 uses u^2+u+2, unlike the author's t^2+1 model. No author code imports.
The universal quotient/radical/source arguments are checked in the report.
"""
import hashlib,json,time
from datetime import datetime,timezone
from pathlib import Path

started=datetime.now(timezone.utc).isoformat(); timer=time.perf_counter()
ROOT=Path(__file__).resolve().parent
ADD=[[((x%3+y%3)%3)+3*((x//3+y//3)%3) for y in range(9)] for x in range(9)]
NEG=[((-x%3)%3)+3*((-(x//3))%3) for x in range(9)]
MUL=[[(x%3*y%3+(x//3)*(y//3))%3+3*((x%3*(y//3)+(x//3)*(y%3)+2*(x//3)*(y//3))%3) for y in range(9)] for x in range(9)]
def pw(x,n):
    y=1
    while n:
        if n&1:y=MUL[y][x]
        x=MUL[x][x];n//=2
    return y
INV=[0]+[pw(x,7) for x in range(1,9)]
FROB=[pw(x,3) for x in range(9)]
def ident(n):return tuple(int(i==j) for i in range(n) for j in range(n))
def add(A,B):return tuple(ADD[x][y] for x,y in zip(A,B))
def sc(c,A):return tuple(MUL[c][x] for x in A)
def mm(A,B,n=8):
    C=[0]*(n*n)
    for i in range(n):
        for k in range(n):
            x=A[i*n+k]
            if x:
                for j in range(n):
                    y=B[k*n+j]
                    if y:C[i*n+j]=ADD[C[i*n+j]][MUL[x][y]]
    return tuple(C)
I=ident(8);Z=(0,)*64
G=[]
for k in range(3):
    c=[0]*64;a=[0]*64
    for b in range(8):
        s=1 if (b&((1<<k)-1)).bit_count()%2==0 else 2
        if b&(1<<k):a[(b^(1<<k))*8+b]=s
        else:c[(b|(1<<k))*8+b]=s
    G.extend((add(c,a),add(c,sc(2,a))))
for i in range(6):
    assert mm(G[i],G[i])==sc(1 if i%2==0 else 2,I)
    for j in range(i):assert add(mm(G[i],G[j]),mm(G[j],G[i]))==Z
B=[];REV=[]
for mask in range(64):
    x=I;y=I
    for i in range(6):
        if mask>>i&1:x=mm(x,G[i]);y=mm(G[i],y)
    B.append(x);REV.append(y)
lookup={sc(c,x):(i,c) for i,x in enumerate(B) for c in (1,2)}
products=[]
for i in range(64):
    for j in range(64):products.append(lookup[mm(B[i],B[j])])
def trace(A):
    s=0
    for i in range(8):s=ADD[s][A[9*i]]
    return s
DUAL=[]
for x in B:
    square=mm(x,x);c=square[0]
    assert square==sc(c,I) and c
    inv=sc(INV[c],x)
    DUAL.append(tuple(MUL[2][inv[j*8+i]] for i in range(8) for j in range(8)))
def coeff(A):
    out=[]
    for row in DUAL:
        s=0
        for x,y in zip(row,A):
            if x and y:s=ADD[s][MUL[x][y]]
        out.append(s)
    return out
for i,x in enumerate(B):assert coeff(x)==[int(j==i) for j in range(64)]
def linear(cs,basis):
    out=Z
    for c,x in zip(cs,basis):
        if c:out=add(out,sc(c,x))
    return out
def reverse(A):return linear(coeff(A),REV)
def images(H,mu):
    Hg=[linear([H[j*6+i] for j in range(6)],G) for i in range(6)]
    out=[]
    for mask in range(64):
        x=I
        for i in range(6):
            if mask>>i&1:x=mm(x,Hg[i])
        out.append(sc(pw(INV[mu],mask.bit_count()//2),x))
    return out,Hg
mu=3;assert pw(mu,4)==2 and pw(mu,8)==1
u=MUL[2][ADD[mu][1]];v=MUL[2][ADD[mu][2]]
H=[0]*36
for k in range(3):
    i=2*k;H[i*6+i]=H[(i+1)*6+i+1]=u;H[i*6+i+1]=H[(i+1)*6+i]=v
H=tuple(H);IMG,HG=images(H,mu)
def transform(A):return linear([FROB[c] for c in coeff(A)],IMG)
parity_counts=[0]*4
for i in range(64):
    for j in range(64):
        k,c=products[i*64+j];pi=i.bit_count()%2;pj=j.bit_count()%2
        lhs=sc(c,IMG[k]);rhs=mm(IMG[i],IMG[j])
        if pi and pj:lhs=sc(mu,lhs)
        assert lhs==rhs
        parity_counts[2*pi+pj]+=1
for i in range(64):
    assert transform(REV[i])==reverse(IMG[i])
    for c in range(9):assert transform(sc(c,B[i]))==sc(FROB[c],IMG[i])
H2=mm(H,tuple(FROB[c] for c in H),6);mu2=MUL[mu][FROB[mu]]
IMG2,_=images(H2,mu2)
for i in range(64):
    assert transform(IMG[i])==IMG2[i]
    assert transform(transform(IMG2[i]))==B[i]
for c in range(1,9):
    im,_=images(sc(c,H),MUL[MUL[c][c]][mu])
    for i in range(64):
        assert im[i]==(IMG[i] if i.bit_count()%2==0 else sc(c,IMG[i]))
e=add(G[0],G[1]);w=add(G[2],G[4]);ew=mm(e,w)
samples=[mm(G[0],G[2])]+[add(I,sc(c,ew)) for c in range(9)]
zeta=pw(mu,2);assert pw(zeta,2)==2
central=sc(zeta,B[63]);assert mm(central,central)==sc(2,I)
samples.append(central)
for g in samples:
    inv=reverse(g);assert mm(inv,g)==I
    tg=transform(g);ti=reverse(tg);assert mm(ti,tg)==I
    for j in range(6):
        x=mm(mm(g,G[j]),inv);cs=coeff(x)
        assert all(c==0 or k in [1<<l for l in range(6)] for k,c in enumerate(cs))
        assert mm(mm(tg,HG[j]),ti)==transform(x)
assert transform(central)==sc(2,central)
draft=ROOT.parent.parent/'sixfolds/spin_lifting/spin_even_extension_draft.md'
canonical=draft.with_name('spin_even_extension_section.tex')
result={'status':'PASS','started_utc':started,'completed_utc':datetime.now(timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-timer,'field':'F3[u]/(u^2+u+2)','matrix_dimension':8,
 'natural_dimension':6,'clifford_basis_dimension':64,'matrix_basis_products':4096,
 'parity_product_counts':parity_counts,'trace_dual_basis_pairs':4096,'reversal_checks':64,
 'coefficient_semilinearity_checks':576,'composition_and_fourth_power_checks':128,
 'scalar_rescaling_checks':512,'spin_samples':len(samples),'vector_covariance_checks':6*len(samples),
 'central_order_four_inverted':True,'draft_sha256':hashlib.sha256(draft.read_bytes()).hexdigest(),
 'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
 'scope':'Finite six-dimensional identity reconstruction only; no universal radical, group generation, normalizer, or source theorem is computationally certified.'}
(ROOT/'audit_spin_even_clifford.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
