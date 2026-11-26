# Independent check of the explicit fibre after thm:odd-plane-char2-obstruction (RESEARCH_SA15):
# Hasse-Witt matrix H_{u,v} = coeff of x^(2v-u) in f (p=2), universal identity H^t w = w^[2],
# rank, smoothness (no singular point over F_{2^m}, m<=6, and Jacobian check), point counts, traces.
import itertools
mons={(5,0,0),(4,1,0),(3,2,0),(2,3,0),(2,2,1),(1,4,0),(1,1,3),(1,0,4),(0,4,1),(0,3,2),(0,1,4)}
d=5
I=[u for u in itertools.product(range(1,d),repeat=3) if sum(u)==d]
I.sort()
print('basis',I)
def c(e): return 1 if tuple(e) in mons else 0
H=[[ (c([2*v[i]-u[i] for i in range(3)]) if all(2*v[i]-u[i]>=0 for i in range(3)) else 0) for v in I] for u in I]
for r in H: print(r)
w=[1 if all(x%2 for x in u) else 0 for u in I]
w=[ (c(u) if all(x%2 for x in u) else 0) for u in I]
Ht_w=[sum(H[a][b]*w[a] for a in range(len(I)))%2 for b in range(len(I))]
print('w',w,'H^t w',Ht_w,'identity holds',Ht_w==[x*x%2 for x in w])
def rank2(M):
    M=[r[:] for r in M]; rk=0; n=len(M[0])
    for col in range(n):
        piv=next((i for i in range(rk,len(M)) if M[i][col]),None)
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][col]: M[i]=[(a+b)%2 for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk
print('rank H over F2:',rank2(H))
# GF(2^m) arithmetic
polys={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}
def mul(a,b,m,mod):
    r=0
    while b:
        if b&1: r^=a
        b>>=1; a<<=1
        if a>>m &1: a^=mod
    return r
def pw(a,e,m,mod):
    r=1
    while e:
        if e&1: r=mul(r,a,m,mod)
        a=mul(a,a,m,mod); e>>=1
    return r
def F(P,m,mod,ms=mons):
    s=0
    for (i,j,k) in ms:
        s^=mul(mul(pw(P[0],i,m,mod),pw(P[1],j,m,mod),m,mod),pw(P[2],k,m,mod),m,mod)
    return s
def deriv(ms,idx):
    out=set()
    for mo in ms:
        if mo[idx]%2==1:
            l=list(mo); l[idx]-=1; t=tuple(l)
            out^={t}
    return out
D=[deriv(mons,i) for i in range(3)]
def matpow_trace(H,m):
    n=len(H); P=[[int(i==j) for j in range(n)] for i in range(n)]
    for _ in range(m):
        P=[[sum(P[i][k]*H[k][j] for k in range(n))%2 for j in range(n)] for i in range(n)]
    return sum(P[i][i] for i in range(n))%2
for m in range(1,7):
    mod=polys[m]; q=1<<m
    pts=[]
    for P in [(1,a,b) for a in range(q) for b in range(q)]+[(0,1,b) for b in range(q)]+[(0,0,1)]:
        if F(P,m,mod)==0: pts.append(P)
    sing=[P for P in pts if all(F(P,m,mod,Di)==0 for Di in D)]
    print('m',m,'#C',len(pts),'singular pts',len(sing),'tr(H^m) mod 2',matpow_trace(H,m),'1-#C mod2',(1-len(pts))%2)
