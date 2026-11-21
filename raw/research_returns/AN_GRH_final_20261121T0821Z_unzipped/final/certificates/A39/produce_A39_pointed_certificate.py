#!/usr/bin/env python3
"""Exact producer for the pointed reflection divisor certificate in A39.

Uses the separately checked Cantor field/polynomial library. This is not
an independent verifier; the companion verifier checks the retained local
identities, reconstructs the matrix and verifies its rank over F2.
"""
from pathlib import Path
import hashlib,json,time
MOD = 0x11B
Q = 256


def slow_mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & Q:
            a ^= MOD
    return out


TABLE = [[slow_mul(a, b) for b in range(Q)] for a in range(Q)]


def mul(a, b):
    return TABLE[a][b]


def power(a, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


INVERSES = [0] + [power(a, Q - 2) for a in range(1, Q)]
assert all(mul(a, INVERSES[a]) == 1 for a in range(1, Q))


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) ^
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def pmul(a, b):
    out = [0] * max(0, len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] ^= mul(ai, bj)
    return trim(out)


def ppow(a, n):
    out = [1]
    for _ in range(n):
        out = pmul(out, a)
    return out


def peval(a, x):
    out = 0
    for ai in reversed(a):
        out = mul(out, x) ^ ai
    return out



inv = lambda a: INVERSES[a]
U=min(a for a in range(Q) if mul(a,a)^a^1==0)
H=[0,0,1]
f=[0,U,0,1,0,U]
ZERO=((1,),())

def scale(a, c):
    return trim([mul(x, c) for x in a])


def divmodp(a, b):
    a, b = trim(a), trim(b)
    assert b
    out = [0] * max(0, len(a) - len(b) + 1)
    bi = inv(b[-1])
    while a and len(a) >= len(b):
        i = len(a) - len(b)
        c = mul(a[-1], bi)
        out[i] = c
        a = add(a, [0]*i + scale(b, c))
    return trim(out), a


def rem(a, b):
    return divmodp(a, b)[1]


def quotient(a, b):
    q, r = divmodp(a, b)
    assert not r
    return q


def xgcd(a, b):
    a, b = trim(a), trim(b)
    s0, s1, t0, t1 = [1], [], [], [1]
    while b:
        q, r = divmodp(a, b)
        a, b = b, r
        s0, s1 = s1, add(s0, pmul(q, s1))
        t0, t1 = t1, add(t0, pmul(q, t1))
    c = inv(a[-1])
    return scale(a, c), scale(s0, c), scale(t0, c)


def check(u, v):
    assert u and u[-1] == 1 and len(v) < len(u)
    assert not rem(add(add(pmul(v, v), pmul(H, v)), f), u)



N=128;u=U;IU=inv(u);mt=TABLE
U=[224,80,1];v=[180,59];A=[188,0,106,39,43,1];B=[80,13,13]

def ppow(a,n):
 r=[1]
 for _ in range(n):r=pmul(r,a)
 return r
assert add(add(pmul(A,A),pmul(pmul(A,B),H)),pmul(pmul(B,B),f))==ppow(U,5)

def sa(a,b,n=N):
 c=list(a[:n])+[0]*max(0,n-len(a))
 for i,x in enumerate(b[:n]):c[i]^=x
 return c

def sm(a,b,n=N):
 c=[0]*n
 aa=[(i,x) for i,x in enumerate(a[:n]) if x]
 bb=[(j,y) for j,y in enumerate(b[:n]) if y]
 for i,x in aa:
  tab=mt[x]
  for j,y in bb:
   if i+j>=n:break
   c[i+j]^=tab[y]
 return c

def ss(a,c,n=N):return [mt[c][x] for x in (list(a[:n])+[0]*max(0,n-len(a)))]

def shift(a,k,n=N):
 assert k>=0
 return ([0]*k+list(a))[:n]+[0]*max(0,n-k-len(a))

def si(a,n=N):
 assert a[0]
 z=[0]*n;z[0]=inv(a[0])
 for i in range(1,n):
  val=0
  for j in range(1,min(i+1,len(a))):val^=mt[a[j]][z[i-j]]
  z[i]=mt[z[0]][val]
 return z

def sp(a,k,n=N):
 if k<0:return sp(si(a,n),-k,n)
 z=[1]+[0]*(n-1)
 for _ in range(k):z=sm(z,a,n)
 return z

def seval(p,x,n=N):
 z=[0]*n
 for c in reversed(p):z=sm(z,x,n);z[0]^=c
 return z

def root5(rhs,constant,n=N):
 z=[0]*n;z[0]=constant;four=lambda x:mt[mt[x][x]][mt[x][x]]
 assert mt[constant][four(constant)]==rhs[0]
 root_scale=inv(four(constant))
 for k in range(1,n):
  val=rhs[k]
  for j in range(1,k//4+1):val^=mt[z[k-4*j]][four(z[j])]
  z[k]=mt[root_scale][val]
 assert sp(z,5,n)==rhs[:n]
 return z

def power_coeff(a,k,e):
 # Needed only for e=3,5 in characteristic2.
 stride=e-1;val=0
 for j in range(k//stride+1):
  x=a[j]
  for _ in range((stride.bit_length()-1)):x=mt[x][x]
  val^=mt[a[k-stride*j]][x]
 return val

start=time.monotonic()
# At W, t=Y/X^3 and S=1/X=t^2*a(t).
a=[0]*N;a[0]=IU
for k in range(1,N):
 val=a[k-1]
 if k>=4:val^=power_coeff(a,k-4,3)
 if k>=8:val^=mt[u][power_coeff(a,k-8,5)]
 a[k]=mt[IU][val]
S=shift(a,2)
one=[1]+[0]*(N-1)
assert sa(sa(sa(one,ss(a,u)),shift(a,1)),sa(shift(sp(a,3),4),ss(shift(sp(a,5),8),u)))==[0]*N
G=[0]*N
for j,c in enumerate(A):G=sa(G,ss(sp(S,5-j),c))
for j,c in enumerate(B):G=sa(G,ss(shift(sp(S,2-j),1),c))
Z=root5(G,1)
Ubar=sa(sa(one,ss(S,80)),ss(sp(S,2),224))
# At Q, local parameter t=Y; X has order2.
Xq=[0]*N
for k in range(1,N):
 val=int(k==2)
 if k>=1 and (k-1)%2==0:val^=mt[Xq[(k-1)//2]][Xq[(k-1)//2]]
 val^=power_coeff(Xq,k,3)
 val^=mt[u][power_coeff(Xq,k,5)]
 Xq[k]=mt[IU][val]
assert sa(sa(shift(one,2),shift(sp(Xq,2),1)),sa(ss(Xq,u),sa(sp(Xq,3),ss(sp(Xq,5),u))))==[0]*N
Fq=sa(seval(A,Xq),shift(seval(B,Xq),1))
z0=power(224,128)
zq=root5(Fq,z0)
Uq=seval(U,Xq)

# Hensel-lift Y on the Delta branch, then invert to the opposite branch.
U4=ppow(U,4);g,hi,_=xgcd(H,U4);assert g==[1]
ylift=v
for unused in range(4):
 err=add(add(pmul(ylift,ylift),pmul(H,ylift)),f)
 ylift=rem(add(ylift,pmul(hi,err)),U4)
assert not rem(add(add(pmul(ylift,ylift),pmul(H,ylift)),f),U4)
ybar=add(ylift,H)


def evaluate(i,aa,bb,m):
 cw=sm(sp(Z,i),sp(Ubar,-i));cq=sm(sp(zq,i),sp(Uq,-i))
 w=[0]*N;q=[0]*N
 for j,c in enumerate(aa):
  w=sa(w,ss(sm(cw,shift(sp(a,i-j),m+2*(i-j))),c))
  q=sa(q,ss(sm(cq,sp(Xq,j)),c))
 for j,c in enumerate(bb):
  w=sa(w,ss(sm(cw,shift(sp(a,i-j-3),m-5+2*i-2*j)),c))
  q=sa(q,ss(shift(sm(cq,sp(Xq,j)),1),c))
 return w,q

basis=[];cols=[]
for i in range(5):
 Ui=ppow(U,i);yb=rem(ybar,Ui)
 specs=[]
 for j in range(17-i):specs.append(([0]*j+Ui,[]))
 for j in range(14+i):specs.append((rem([0]*j+yb,Ui),[0]*j+[1]))
 assert len(specs)==31
 for aa,bb in specs:
  assert not rem(add(aa,pmul(bb,ybar)),Ui)
  w,q=evaluate(i,aa,bb,32)
  cols.append(w[:32]+q[:128]);basis.append({'i':i,'A':aa,'B':bb})
matrix=[[col[j] for col in cols] for j in range(160)]
work=[row[:] for row in matrix];rank=0;pivots=[]
for column in range(155):
 pivot=next((j for j in range(rank,160) if work[j][column]),None)
 if pivot is None:continue
 work[rank],work[pivot]=work[pivot],work[rank]
 tab=mt[inv(work[rank][column])];work[rank]=[tab[x] for x in work[rank]]
 for j in range(rank+1,160):
  if work[j][column]:
   tab=mt[work[j][column]];work[j]=[x^tab[y] for x,y in zip(work[j],work[rank])]
 pivots.append(column);rank+=1
assert rank==155
fs=[{'i':1,'scalar':225,'A':U,'B':[]},
    {'i':2,'scalar':1,'A':[225,12,162,224],'B':[1]},
    {'i':3,'scalar':13,'A':[224,189,202,174,189],'B':[13,1]},
    {'i':4,'scalar':1,'A':[177,0,61,175,79,225],'B':[236,1,1]}]
ws=[0]*N;qs=[0]*N
for term in fs:
 i=term['i'];aa=term['A'];bb=term['B'];c=term['scalar']
 assert not rem(add(aa,pmul(bb,ybar)),ppow(U,i))
 w,q=evaluate(i,aa,bb,2);ws=sa(ws,ss(w,c));qs=sa(qs,ss(q,c))
assert not any(ws[:6]) and ws[6] and not any(qs[:4]) and qs[4]
zeta=next(x for x in range(2,256) if power(x,5)==1)
out={'field_modulus':MOD,'field_size':256,'u':u,'zeta5':zeta,
     'h':H,'f':f,'Delta_U':U,'Delta_V':v,'Kummer_A':A,'Kummer_B':B,
     'norm':ppow(U,5),'series_precision':N,'series_a_W':a,'series_Z_W':Z,
     'series_X_Q':Xq,'series_z_Q':zq,'z_at_Q':z0,'Y_lift_Delta_mod_U4':ylift,
     'basis_L_32_piW':basis,'constraint_matrix_Rt':matrix,'rank_F256':rank,
     'Rs_function':fs,'Rs_function_t2_times_at_P':ws[:10],'Rs_function_at_Q':qs[:8],
     'matrix_rows':'first32 coefficients of t^32 f at P; then first128 coefficients at Q',
     'matrix_columns':155,'matrix_row_count':160,
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exact producer data for independent residual/matrix/bit-rank verification; geometric divisor interpretation is in the accompanying proof.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:out[k] for k in ['rank_F256','matrix_columns','matrix_row_count','z_at_Q','zeta5','Rs_function_t2_times_at_P','Rs_function_at_Q','source_sha256']},indent=2))
