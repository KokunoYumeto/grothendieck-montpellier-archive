"""Independent exact C25 certificate, using different extension-field models.

Counting fields: F_109[u]/(u^2-6), F_109[v]/(v^3-3),
F_109[w]/(w^4-6), distinct from the parent counting program.
All finite-field arithmetic is exact int64; intermediate products stay small.
"""
from pathlib import Path
import json
import time
import numpy as np
import sympy as sp

p = 109
coeff = [63, 1, 65, 35, 40, 3, 45, 30, 27, 62, 1]
out = []

def report(*xs):
    s = " ".join(map(str, xs))
    print(s, flush=True)
    out.append(s)
    Path("work/check_C25_independent_output.txt").write_text("\n".join(out)+"\n")

# These binomials are irreducible: 6 is nonsquare, p=1 mod 4,
# and 3 is noncube with p=1 mod 3.
assert pow(6, (p-1)//2, p) == p-1
assert pow(3, (p-1)//3, p) != 1
leg = np.array([0]+[1 if pow(t, (p-1)//2, p)==1 else -1
                         for t in range(1,p)], dtype=np.int64)

def count(r):
    chi = 0
    for start in range(0, p**r, 250000):
        code = np.arange(start, min(start+250000, p**r), dtype=np.int64)
        x = []
        for _ in range(r):
            x.append(code % p)
            code = code // p
        z = np.zeros_like(x[0])
        f = [z.copy() for _ in range(r)]
        f[0] += coeff[-1]
        for a0 in reversed(coeff[:-1]):
            if r == 1:
                f = [(f[0]*x[0]+a0) % p]
            elif r == 2:
                a,b = f; u,v = x
                f = [(a*u+6*b*v+a0)%p, (a*v+b*u)%p]
            elif r == 3:
                a,b,c = f; u,v,w = x
                f = [(a*u+3*(b*w+c*v)+a0)%p,
                     (a*v+b*u+3*c*w)%p,
                     (a*w+b*v+c*u)%p]
            else:
                a,b,c,d = f; u,v,w,z = x
                f = [(a*u+6*(b*z+c*w+d*v)+a0)%p,
                     (a*v+b*u+6*(c*z+d*w))%p,
                     (a*w+b*v+c*u+6*d*z)%p,
                     (a*z+b*w+c*v+d*u)%p]
        if r == 1:
            norm = f[0]
        elif r == 2:
            a,b = f
            norm = (a*a-6*b*b)%p
        elif r == 3:
            a,b,c = f
            norm = (a*a*a+3*b*b*b+9*c*c*c-9*a*b*c)%p
        else:
            a,b,c,d = f
            u = (a*a+6*c*c-12*b*d)%p
            v = (2*a*c-b*b-6*d*d)%p
            norm = (u*u-6*v*v)%p
        chi += int(leg[norm].sum())
    return p**r+2+chi

T = sp.symbols("T")
F = sp.Poly(sum(coeff[j]*T**j for j in range(len(coeff))), T, modulus=p)
assert sp.gcd(F, F.diff()).degree()==0
report("Squarefree degree", F.degree(), "with two rational points at infinity")
counts=[]
for r in range(1,5):
    began=time.time()
    counts.append(count(r))
    report("r",r,"count",counts[-1],"seconds",round(time.time()-began,3))
assert counts == [134,11794,1294958,141166026]

power = [None]+[p**r+1-counts[r-1] for r in range(1,5)]
frob=[1]
for k in range(1,5):
    num = -sum(frob[k-j]*power[j] for j in range(1,k+1))
    assert num%k==0
    frob.append(num//k)
frob += [p*frob[3],p*p*frob[2],p**3*frob[1],p**4]
assert frob == [1,24,244,1224,3510,133416,2898964,31080696,141158161]
report("Frobenius descending",frob,"ordinary",frob[4]%p!=0)
f = sp.Poly.from_list(frob,T)
I=sp.I
g=T**4+(12+10*I)*T**3+192*I*T**2+(-1308+1090*I)*T-11881
assert sp.expand(g*sp.conjugate(g).subs(sp.conjugate(T),T)-f.as_expr())==0
g61=sp.Poly(T**4-23*T**2+7*T+14,T,modulus=61)
assert g61.is_irreducible
report("Gaussian quartic product and irreducibility mod61", g61.as_expr())

# Direct power-basis rank, computed by modular multiplication/reduction.
f37 = [v%37 for v in reversed(frob)]
def mul(a,b):
    c=[0]*15
    for j in range(8):
        for k in range(8):c[j+k]=(c[j+k]+a[j]*b[k])%37
    for j in range(14,7,-1):
        for k in range(8):c[j-8+k]=(c[j-8+k]-c[j]*f37[k])%37
    return c[:8]
def power_x(e):
    a=[1]+[0]*7;b=[0,1]+[0]*6
    while e:
        if e&1:a=mul(a,b)
        b=mul(b,b);e//=2
    return a
def det_mod(A):
    A=[row[:] for row in A];d=1
    for i in range(8):
        j=next(j for j in range(i,8) if A[j][i]%37)
        if j!=i:A[i],A[j]=A[j],A[i];d=-d
        pivot=A[i][i]%37;d=d*pivot%37;inv=pow(pivot,-1,37)
        for j in range(i+1,8):
            q=A[j][i]*inv%37
            for k in range(i,8):A[j][k]=(A[j][k]-q*A[i][k])%37
    return d%37
degrees=[2,3,4,5,6,8,10,12,15,16,20,24,30]
dets=[]
for d in degrees:
    cols=[power_x(d*j) for j in range(8)]
    dets.append(det_mod([[cols[j][i] for j in range(8)] for i in range(8)]))
assert dets==[5,11,22,30,9,18,28,14,20,33,7,17,22]
report("Power-basis degrees",degrees,"determinants mod37",dets)

# F_13[alpha], alpha^2-2alpha+7=0; exact Frobenius order.
def mul13(a,b):
    return ((a[0]*b[0]-7*a[1]*b[1])%13,
            (a[0]*b[1]+a[1]*b[0]+2*a[1]*b[1])%13)
def pow13(e):
    a=(1,0);b=(0,1)
    while e:
        if e&1:a=mul13(a,b)
        b=mul13(b,b);e//=2
    return a
assert pow13(168)==(1,0)
assert pow13(84)==(12,0)
assert pow13(56)==(9,0)
assert pow13(24)==(2,2)
report("Order168 powers",[(e,pow13(e)) for e in [24,56,84,168]])
report("ALL EXACT CHECKS PASS")
