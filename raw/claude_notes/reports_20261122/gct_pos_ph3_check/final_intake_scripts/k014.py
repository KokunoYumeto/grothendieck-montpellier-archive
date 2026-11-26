import re,sys,cmath,math,itertools
txt=open(sys.argv[1],encoding='utf-8').read()
rows=[]
for m in re.finditer(r'^\s*(\d+)\s*&\s*\$\(([\d,]+)\)\$\s*&\s*\$\(([\d,]+)\)\$\s*&\s*\$\(([\d,]+)\)\$',txt,re.M):
    rows.append(tuple(tuple(int(x) for x in g.split(',')) for g in m.groups()[1:]))
print('types',len(rows))
M=16; z=cmath.exp(2j*math.pi/M)
def canon(T):
    best=None
    for u in range(M):
        for v in range(M):
            w=(-u-v)%M
            key=(tuple(sorted((a+u)%M for a in T[0])),tuple(sorted((b+v)%M for b in T[1])),tuple(sorted((c+w)%M for c in T[2])))
            if best is None or key<best: best=key
    return best
tot=0; count=0; multdist={}
for A,B,C in rows:
    assert (sum(A)+sum(B)+sum(C))%M==1
    perms=set(canon(P) for P in itertools.permutations((A,B,C)))
    k=len(perms); multdist[k]=multdist.get(k,0)+1; count+=k
    num=1
    for X in (A,B,C):
        for i in range(5):
            for j in range(5):
                if i!=j and (X[i]-X[j])%M: num*=(1-z**(X[i]-X[j]))
    den=1; fixed=0
    for a in A:
        for b in B:
            for c in C:
                if (a+b+c)%M==0: fixed+=1
                else: den*=(1-z**(a+b+c))
    tot+=k*num/den
print('ordered classes',count,'multiplicity distribution',multdist)
claimed=(78+446*z-211*z**2-301*z**3-301*z**4-211*z**5+446*z**6+78*z**7)/32768
print('my total',tot); print('claimed ',claimed)
