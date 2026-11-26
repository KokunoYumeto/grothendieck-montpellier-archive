# DP_MULT DP1 / DP3 on the height-2 Honda group over Z_3: log l(x)=sum_k x^(9^k)/3^k.
# D = d/dz in the coordinate z=l(t); D^n f(0) = n! [z^n] f(E(z)), E = l^{-1}.
from fractions import Fraction as F
from math import factorial, ceil, floor
p,h=3,2; N=170
def v(x):
    if x==0: return 10**9
    a,b=x.numerator,x.denominator; c=0
    while a%p==0: a//=p; c+=1
    while b%p==0: b//=p; c-=1
    return c
l=[F(0)]*(N+1)
k=0
while p**(h*k)<=N:
    l[p**(h*k)]+=F(1,p**k); k+=1
def mul(a,b):
    c=[F(0)]*(N+1)
    for i,x in enumerate(a):
        if x==0: continue
        for j in range(0,N+1-i):
            if b[j]!=0: c[i+j]+=x*b[j]
    return c
def compose(f,g):  # f(g(z)), g(0)=0
    res=[F(0)]*(N+1); pw=[F(0)]*(N+1); pw[0]=F(1)
    for i in range(N+1):
        if f[i]!=0:
            for j in range(N+1): res[j]+=f[i]*pw[j]
        pw=mul(pw,g)
    return res
# inverse series E with l(E(z))=z: since l(x)=x+x^9/3+x^81/9, iterate E = z - (l(E)-E)
E=[F(0)]*(N+1); E[1]=F(1)
for it in range(25):
    lE=compose(l,E)
    newE=[F(0)]*(N+1); newE[1]=F(1)
    for j in range(2,N+1): newE[j]=-(lE[j]-E[j]) if j!=1 else 0
    if newE==E: break
    E=newE
assert compose(l,E)[:N+1]==[F(0),F(1)]+[F(0)]*(N-1)
c=F(1,p-1)-F(1,p**h-1)
def Eh(n): return sum(n//p**j for j in range(1,10) if j%h!=0)
bad=[];eqfloor=[]
for n in range(1,N+1):
    val=v(factorial(n)*E[n])
    b1=max(0,ceil(c*n-(h-1)))
    if val<b1: bad.append(('DP1',n,val,b1))
    if val<Eh(n): bad.append(('DP3',n,val,Eh(n)))
for r in (1,2):
    n=p**(h*r)
    if n<=N: print(f"n=q^{r}={n}: v(D^n t(0))={v(factorial(n)*E[n])}, c_h(q^r-1)={c*(n-1)}, E_h(n)={Eh(n)}")
# witness t^(p^h-1)=t^8: D^n(t^8)(0) = n! [z^n] E^8
E8=[F(0)]*(N+1); E8[0]=F(1)
for _ in range(p**h-1): E8=mul(E8,E)
att=[n for n in range(1,N+1) if E8[n]!=0 and v(factorial(n)*E8[n])==max(0,ceil(c*n-(h-1))) and ceil(c*n-(h-1))>ceil(c*n)-1]
viol=[n for n in range(1,N+1) if E8[n]!=0 and v(factorial(n)*E8[n])<max(0,ceil(c*n-(h-1)))]
nz=[n for n in range(1,N+1) if E8[n]!=0]
print("violations of DP1/DP3 for f=t, n<=%d:"%N,bad)
print("f=t^8: violations",viol,"; n where v equals ceil(c n-1) and is below ceil(c n):",att[:12])
print("f=t^8 values (n, v, ceil(cn-1), ceil(cn)):",[(n,v(factorial(n)*E8[n]),ceil(c*n-1),ceil(c*n)) for n in nz[:6]])
