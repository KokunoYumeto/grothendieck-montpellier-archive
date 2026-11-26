import sympy as sp
from fractions import Fraction as Fr
N=120*8
# series coefficients
den=[2,4,6,8,10]
c=[0]*(N+1); c[0]=1
for a in den:
    for i in range(a,N+1): c[i]+=c[i-a]
f=[c[i]+(c[i-25] if i>=25 else 0) for i in range(N+1)]
s=sp.symbols('s')
P={}
for r in range(120):
    pts=[(r+120*k, f[r+120*k]) for k in range(1,7)]
    P[r]=sp.expand(sp.interpolate(pts,s))
    assert all(P[r].subs(s,x)==fx for x,fx in [(r+120*k,f[r+120*k]) for k in range(0,8) if r+120*k<=N])
def ok_pos(p):
    for r in range(120):
        Q=sp.Poly(sp.expand(P[(r+p)%120].subs(s,s+p)),s)
        if any(co<0 for co in Q.all_coeffs()): return False
    return True
def ok_sat(p):
    for r in range(120):
        Q=sp.expand(P[(r+p)%120].subs(s,s+p))
        if Q==0: continue
        if any(Q.subs(s,x)<=0 for x in range(1,200)): return False
    return True
pp=next(p for p in range(0,200) if ok_pos(p)); ss=next(p for p in range(0,200) if ok_sat(p))
print('positivity index',pp,'saturation index',ss)
