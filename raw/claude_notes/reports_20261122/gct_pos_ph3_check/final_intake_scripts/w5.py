import itertools
from collections import defaultdict
def perm_sign(p):
    s=1;p=list(p)
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]: s=-s
    return s
def mult(char,mu,k):
    mu=list(mu)+[0]*(k-len(mu))
    delta=list(range(k-1,-1,-1))
    tot=0
    for p in itertools.permutations(range(k)):
        w=tuple(mu[i]+delta[i]-delta[p[i]] for i in range(k))
        tot+=perm_sign(p)*char.get(w,0)
    return tot
def decompose(char,k):
    # return dict of dominant weights with nonzero mult
    res={}
    for w in char:
        if all(w[i]>=w[i+1] for i in range(k-1)):
            m=mult(char,w,k)
            if m: res[w]=m
    return res
k=5
basis=[tuple(1 if i in c else 0 for i in range(k)) for c in itertools.combinations(range(k),3)]
ok=True
for j in range(11):
    ch=defaultdict(int)
    for S in itertools.combinations(range(10),j):
        w=tuple(sum(basis[s][i] for s in S) for i in range(k)); ch[w]+=1
    print(j,decompose(ch,k))
