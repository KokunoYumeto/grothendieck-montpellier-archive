import cmath, math, itertools
def S(n):
    w=[(-2)**i for i in range(n-1)]+[0]
    E=[{0,1,k} for k in range(2,n)]+[{0,2,3}]
    ms=[w[i] for i in range(n-1)]
    for t in itertools.combinations(range(n),3):
        if set(t) in E: continue
        ms.append(sum(w[i] for i in t))
    assert len(ms)==math.comb(n,3)
    return ms
# n=4 check of (P-F56v) vs Salmon series
z=cmath.exp(2j*math.pi/8)
lhs=(1+z**25)/((1-z**2)*(1-z**4)*(1-z**6)*(1-z**10))
rhs=1
for b in S(4): rhs/= (1-z**b)
print('n=4 C(zeta): Salmon',lhs,' product',rhs)
for n in range(5,17):
    M=2**(n-1); g=math.gcd(n,3); ms=S(n)
    def logP(a):
        s=0.0
        for b in ms:
            x=(a*b)%M
            s-=math.log2(abs(2*math.sin(math.pi*x/M)))
        return s
    bn=pow(3,-1,M)
    lb=logP(bn)
    Q=0.0; mx=-1e9
    for a in range(1,M,2):
        if a in (bn,M-bn): continue
        v=logP(a)-lb; Q+=2**v; mx=max(mx,v)
    print(n,'log2|P(b_n)|=%.1f'%lb,'Q_n=%.3e'%Q,'max log2 ratio=%.1f'%mx, 'n^4/24=%.1f'%(n**4/24))
