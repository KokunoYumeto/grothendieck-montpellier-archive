"""Deterministic randomized exact search in F2[x]/x^N.
Unlike A4_amitsur_search.py, subalgebras and ideals need not be monomial.
All vector-space calculations are exact bit arithmetic over F2.
"""
from A4_amitsur_search import basis_add,span,red
from itertools import product
import random,json,time,sys

def normal(b,v):
    for p in sorted(b,reverse=True):
        if v>>p&1:v^=b[p]
    return v

def cmul(a,b,N):
    w=0
    for i in range(N):
        if a>>i&1:w^=b<<i
    return w&((1<<N)-1)

def algclose(N,gs):
    b=span([1]+gs)
    while True:
        old=len(b)
        for a in list(b.values()):
            for c in list(b.values()):basis_add(b,cmul(a,c,N))
        if len(b)==old:return b

def iclose(N,A,gs):return span(cmul(a,g,N)for a in A.values()for g in gs)

class T:
    def __init__(self,N,A,d):
        self.N,self.d=N,d;self.ts=list(product(range(N),repeat=d));self.idx={t:i for i,t in enumerate(self.ts)}
        self.rel={}
        for t in self.ts:
            for a in A.values():
                for j in range(1,d):
                    v=0
                    for e in range(N):
                        if a>>e&1:
                            for k in [0,j]:
                                u=list(t);u[k]+=e
                                if u[k]<N:v^=1<<self.idx[tuple(u)]
                    basis_add(self.rel,v)
        self.reps=[t for i,t in enumerate(self.ts)if i not in self.rel]
        self.bas=[1<<self.idx[t]for t in self.reps]
        self.dim=len(self.bas)
        self.nf=[normal(self.rel,1<<i)for i in range(len(self.ts))]
    def mono(self,t):return self.nf[self.idx[tuple(t)]]if all(e<self.N for e in t)else 0
    def mul(self,a,b):
        v=0
        while a:
            i=(a&-a).bit_length()-1;a&=a-1;c=b
            while c:
                j=(c&-c).bit_length()-1;c&=c-1
                v^=self.mono(tuple(x+y for x,y in zip(self.ts[i],self.ts[j])))
        return v
    def face(self,a,Q):
        v=0
        while a:
            i=(a&-a).bit_length()-1;a&=a-1;t=self.ts[i]
            for j in range(self.d+1):v^=Q.mono(t[:j]+(0,)+t[j:])
        return v
    def ideal(self,I):
        bs={}
        for a in I.values():
            for t in self.ts:
                v=0
                for e in range(self.N):
                    if a>>e&1:v^=self.mono((t[0]+e,)+t[1:])
                basis_add(bs,v)
        return bs

def check(N,A,I):
    C,Q=T(N,A,1),T(N,A,2)
    J0,J1=C.ideal(I),Q.ideal(I);bd=span(C.face(v,Q)for v in J0.values())
    inv=sorted({normal(J0,v)for v in range(1<<N)if not red(J1,C.face(v,Q))})
    add=span([*bd.values()]+[C.face(v,Q)for v in inv]);lg=span(bd.values());pairs=[]
    for v in inv:
        if not v&1:continue
        a=b=0
        for e in range(N):
            if v>>e&1:a^=Q.mono((e,0));b^=Q.mono((0,e))
        ai=term=1
        for _ in range(1,N):term=Q.mul(term,a^1);ai^=term
        w=Q.mul(ai,b)^1
        assert not red(J1,w)
        basis_add(lg,w);pairs.append((v,w))
    if len(add)!=len(lg)or any(red(add,v)for v in lg.values()):
        R=T(N,A,3)
        assert all(Q.face(w,R)==0 for _,w in pairs)
        return {'N':N,'A_basis':list(A.values()),'I_basis':list(I.values()),'Q_basis':Q.reps,
                'ordinary_boundaries':list(bd.values()),'additive_boundaries':list(add.values()),
                'logarithmic_boundaries':list(lg.values()),'invariants':inv,'log_pairs':pairs,
                'tensor_dimensions':[C.dim,Q.dim,R.dim]}

def main():
    r=random.Random(1729);start=time.monotonic();count=0;seen=set();findings=[]
    Nmax=int(sys.argv[1])if len(sys.argv)>1 else 9
    tries=int(sys.argv[2])if len(sys.argv)>2 else 1000
    for N in range(3,Nmax+1):
        for _ in range(tries):
            gs=[r.randrange(1,1<<(N-1))<<1 for _ in range(r.randrange(1,4))]
            A=algclose(N,gs)
            vals=[]
            av=list(A.values())
            for _ in range(8):
                v=0
                for a in av:
                    if r.randrange(2):v^=a
                if v and cmul(v,v,N)==0:vals.append(v)
            if not vals:continue
            I=iclose(N,A,[r.choice(vals)])
            if any(cmul(a,b,N)for a in I.values()for b in I.values()):continue
            key=(N,tuple(sorted(normal(A,1<<i)for i in range(N))),tuple(sorted(normal(I,1<<i)for i in range(N))))
            if key in seen:continue
            seen.add(key);count+=1;f=check(N,A,I)
            if f:
                findings.append(f);print(json.dumps({'found':f}),flush=True)
        print(json.dumps({'N_completed':N,'distinct_tests':count,'seconds':time.monotonic()-start}),flush=True)
    print(json.dumps({'seed':1729,'distinct_tests':count,'seconds':time.monotonic()-start,'findings':findings},indent=2))

if __name__=='__main__':main()
