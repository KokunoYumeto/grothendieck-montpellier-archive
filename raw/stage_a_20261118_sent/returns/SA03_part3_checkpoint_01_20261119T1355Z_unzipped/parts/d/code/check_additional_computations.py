"""Further exact arithmetic checks prompted by the full transcription."""
from pathlib import Path
from math import comb
import sympy as s
out=[]
def say(*x):out.append(' '.join(map(str,x)))
q=s.symbols('q');N=10
def sigma(n,k):return sum(d**k for d in range(1,n+1) if n%d==0)
E4=1+240*sum(sigma(n,3)*q**n for n in range(1,N+1))
E6=1-504*sum(sigma(n,5)*q**n for n in range(1,N+1))
Delta=q
for n in range(1,N+1):Delta=s.series(Delta*(1-q**n)**24,q,0,N+1).removeO()
res=s.series(E4**3-E6**2-1728*Delta,q,0,N+1).removeO()
assert res==0
say('q-series E4^3-E6^2=1728 q product(1-q^n)^24 through q^10: residual',res)
say('Delta coefficients q^1...q^10:',[Delta.coeff(q,i) for i in range(1,N+1)])
say('This finite check confirms displayed normalizations; it is not a proof of the identity of infinite modular forms.')
# F9=F3[i], i²=-1; automorphisms of y²=x³-x have x=u²X+r,y=u³Y.
def add(a,b):return ((a[0]+b[0])%3,(a[1]+b[1])%3)
def neg(a):return((-a[0])%3,(-a[1])%3)
def mul(a,b):return((a[0]*b[0]-a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
one=(1,0);zero=(0,0)
def pw(a,n):
    r=one
    for _ in range(n):r=mul(r,a)
    return r
els=[(a,b) for a in range(3) for b in range(3)]
us=[u for u in els if pw(u,4)==one]
rs=[r for r in els if pw(r,3)==r]
autos=[(u,r) for u in us for r in rs]
def compose(A,B):
    u,r=A;v,t=B
    return(mul(u,v),add(r,mul(pw(u,2),t)))
assert len(autos)==12
assert all(compose(a,b) in autos for a in autos for b in autos)
say('Characteristic3 y²=x³-x: u^4=1 has',len(us),'solutions; r^3=r has',len(rs),'; automorphisms=',len(autos))
say('Composition (u,r)(v,t)=(uv,r+u²t) closed. Geometric group count, not a verification of the entire formal deformation action.')
# Nilpotence is not vanishing in the exceptional normal form conditions.
say('Dual-number witnesses: char3 a2=epsilon gives c4=a2²=0 with a2!=0; char2 a1=epsilon gives c4=a1⁴=0 with a1!=0.')
say('Boundary sign: outward normals of opposite half-spaces are negatives; normal-first orientations on their common boundary differ by -1.')
path=Path(__file__).resolve().parents[1]/'outputs/additional_computations.txt'
path.write_text('\n'.join(out)+'\n');print(path.read_text())
