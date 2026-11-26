import itertools, math
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp
mp.mp.dps=60
def S(n):
    w=[(-2)**i for i in range(n-1)]+[0]
    E=[{0,1,k} for k in range(2,n)]+[{0,2,3}]
    ms=[w[i] for i in range(n-1)]
    for t in itertools.combinations(range(n),3):
        if set(t) in E: continue
        ms.append(sum(w[i] for i in t))
    return ms
def W(n,r):
    M=2**(n-1); g=math.gcd(n,3); ms=S(n); tot=mp.mpc(0)
    for a in range(1,M,2):
        C=mp.mpc(1)
        for b in ms: C/= (1-mp.expjpi(2*mp.mpf(a*g*b)/M))
        tot+= C/M*mp.expjpi(-2*mp.mpf(a*r)/M)
    return tot
print('n=4: 2W_4(19) via product =',mp.nstr(2*W(4,19),15))
# via Salmon series constituents
s=sp.symbols('s'); N=120*8
c=[0]*(N+1); c[0]=1
for a in (2,4,6,8,10):
    for i in range(a,N+1): c[i]+=c[i-a]
f=[c[i]+(c[i-25] if i>=25 else 0) for i in range(N+1)]
def q(r,x):
    pts=[(r+120*k, f[r+120*k]) for k in range(1,7)]
    return sp.interpolate(pts,s).subs(s,x)
print('n=4: f(19)=',f[19],' q_79(19)=',q(79,19),' f(19)-q_79(19)=',f[19]-q(79,19))
for (n,x,claim) in ((9,6,Fr(1819142906755,64)),(9,7,Fr(782264335828,64))):
    v=2*W(n,x)
    print('n=%d x=%d: 2W ='%(n,x),mp.nstr(v,20),' claimed',float(claim))
