"""Exact F_2 Amitsur square-zero comparison in truncated monomial algebras.

For C=F_2[x]/x^N and A the monomial subalgebra with exponents E,
construct C^{tensor_A d}, d=1,2,3, by monomial binomial relations.
For each monomial square-zero ideal I of A, compare the two boundary
subspaces in H^1(I C^bullet). No claim about non-monomial algebras is made.
"""
from itertools import product, combinations
import json,time,sys

def basis_add(b,v):
    while v:
        k=v.bit_length()-1
        if k in b:v^=b[k]
        else:b[k]=v;return True
    return False

def red(b,v):
    while v:
        k=v.bit_length()-1
        if k not in b:return v
        v^=b[k]
    return 0

class Tensor:
    def __init__(self,N,E,d):
        self.N,self.E,self.d=N,E,d
        self.ts=list(product(range(N),repeat=d));self.idx={t:i for i,t in enumerate(self.ts)}
        z=len(self.ts);p=list(range(z+1))
        def root(x):
            while p[x]!=x:p[x]=p[p[x]];x=p[x]
            return x
        def join(a,b):
            a,b=root(a),root(b)
            if a!=b:p[max(a,b)]=min(a,b)
        for t in self.ts:
            for e in E:
                if e==0:continue
                for j in range(1,d):
                    a=list(t);b=list(t);a[0]+=e;b[j]+=e
                    join(self.idx[tuple(a)] if a[0]<N else z,self.idx[tuple(b)] if b[j]<N else z)
        rz=root(z);rs=sorted(set(root(i) for i in range(z))-{rz})
        ri={r:i for i,r in enumerate(rs)}
        self.q=[0 if root(i)==rz else 1<<ri[root(i)] for i in range(z)]
        self.reps=[self.ts[r] for r in rs];self.dim=len(rs)
    def mono(self,t):return self.q[self.idx[tuple(t)]] if all(x<self.N for x in t) else 0
    def mul(self,a,b):
        v=0
        while a:
            i=(a&-a).bit_length()-1;a&=a-1;c=b
            while c:
                j=(c&-c).bit_length()-1;c&=c-1
                v^=self.mono(tuple(x+y for x,y in zip(self.reps[i],self.reps[j])))
        return v
    def face_sum(self,v,target):
        out=0
        while v:
            i=(v&-v).bit_length()-1;v&=v-1;t=self.reps[i]
            for j in range(self.d+1):out^=target.mono(t[:j]+(0,)+t[j:])
        return out
    def ideal(self,I):
        return {self.mono((t[0]+e,)+t[1:]) for t in self.ts for e in I}-{0}

def span(vals):
    b={}
    for v in vals:basis_add(b,v)
    return b

def compare(N,E,I,T):
    C,Q,R=T;j0=C.ideal(I);j1=Q.ideal(I)
    J0=sum(j0);J1=sum(j1)
    bd=span(C.face_sum(v,Q) for v in j0)
    inv=[v for v in range(1<<N) if not (v&J0) and not(C.face_sum(v,Q)&~J1)]
    add=span([*bd.values()]+[C.face_sum(v,Q) for v in inv])
    log=span(bd.values())
    pairs=[]
    for v in inv:
        if not v&1:continue
        a=b=0
        for i in range(N):
            if v>>i&1:a^=Q.mono((i,0));b^=Q.mono((0,i))
        ai=1;term=1
        for _ in range(1,N):term=Q.mul(term,a^1);ai^=term
        w=Q.mul(ai,b)^1
        assert not(w&~J1)
        assert Q.face_sum(w,R)==0
        basis_add(log,w);pairs.append((v,w))
    equal=(len(add)==len(log) and all(red(add,w)==0 for w in log.values()))
    if not equal:
        return {'N':N,'A_exponents':E,'I_exponents':I,'tensor_dimensions':[t.dim for t in T],
                'J_dimensions':[len(j0),len(j1),len(R.ideal(I))],
                'boundary_dim':len(bd),'add_boundary_dim':len(add),'log_boundary_dim':len(log),
                'C0_invariants':inv,'Q_representatives':Q.reps,'J1_bit_basis':sorted(j1),
                'ordinary_boundaries':list(bd.values()),'additive_boundary_basis':list(add.values()),
                'log_boundary_basis':list(log.values()),'log_pairs':pairs}

def main():
    start=time.monotonic();counts={'algebras':0,'ideals':0,'unequal':0};findings=[]
    maxn=int(sys.argv[1]) if len(sys.argv)>1 else 8
    for N in range(2,maxn+1):
        for mask in range(1<<(N-1)):
            E=[0]+[e for e in range(1,N) if mask>>(e-1)&1]
            if any(a+b<N and a+b not in E for a in E for b in E):continue
            Is=[]
            es=[e for e in E if e and 2*e>=N]
            for imask in range(1,1<<len(es)):
                I=[e for i,e in enumerate(es) if imask>>i&1]
                if any(e+a<N and e+a not in I for e in I for a in E):continue
                Is.append(I)
            if not Is:continue
            T=[Tensor(N,E,d) for d in [1,2,3]];counts['algebras']+=1
            for I in Is:
                counts['ideals']+=1;f=compare(N,E,I,T)
                if f:findings.append(f);counts['unequal']+=1
        print(json.dumps({'N_completed':N,'counts':counts,'seconds':time.monotonic()-start}),flush=True)
    print(json.dumps({'summary':counts,'seconds':time.monotonic()-start,'findings':findings},indent=2),flush=True)

if __name__=='__main__':main()
