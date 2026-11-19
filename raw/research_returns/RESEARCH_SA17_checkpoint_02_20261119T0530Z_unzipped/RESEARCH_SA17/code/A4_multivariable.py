"""Exact random search in multivariable local F2 algebras.

The ambient algebra C is F2[x_1,...,x_r]/m^d. We generate subalgebras A
and principal square-zero ideals I of A, then compute C tensor_A C by its
full linear relation space. We compare additive and logarithmic boundary
subgroups, without assuming H1(Ga)=0. On a witness, the cocycle identity
is additionally checked in the threefold tensor product.
"""
from itertools import product
from A4_amitsur_search import basis_add,span,red
from A4_amitsur_random import normal
from A4_closed_covers import Ring
import random,time,json,sys

def closure(C,gs):
    A=span([1]+gs)
    while True:
        old=len(A)
        for a in list(A.values()):
            for b in list(A.values()):basis_add(A,C.mul(a,b))
        if len(A)==old:return A

class Tensor:
    def __init__(self,C,A,d):
        self.C,self.d=C,d;self.ts=list(product(range(C.n),repeat=d));self.idx={t:i for i,t in enumerate(self.ts)}
        self.rel={}
        for t in self.ts:
            for a in A.values():
                if a==1:continue
                for j in range(1,d):
                    v=0
                    for k in [0,j]:
                        w=C.mul(1<<t[k],a)
                        while w:
                            e=(w&-w).bit_length()-1;w&=w-1
                            u=list(t);u[k]=e;v^=1<<self.idx[tuple(u)]
                    basis_add(self.rel,v)
        self.bs=[1<<i for i in range(len(self.ts))if i not in self.rel]
        self.n=len(self.bs);self.nf=[normal(self.rel,1<<i)for i in range(len(self.ts))]
    def mul(self,a,b):
        out=0
        while a:
            i=(a&-a).bit_length()-1;a&=a-1;bb=b
            while bb:
                j=(bb&-bb).bit_length()-1;bb&=bb-1
                possibilities=[0]
                choices=[]
                for u,v in zip(self.ts[i],self.ts[j]):
                    p=self.C.mt[u][v]
                    if not p:break
                    choices.append((p&-p).bit_length()-1)
                if len(choices)==self.d:out^=self.nf[self.idx[tuple(choices)]]
        return out
    def place(self,a,k):
        v=0
        while a:
            i=(a&-a).bit_length()-1;a&=a-1
            t=[0]*self.d;t[k]=i;v^=self.nf[self.idx[tuple(t)]]
        return v
    def diff(self,a,Q):
        out=0
        while a:
            i=(a&-a).bit_length()-1;a&=a-1;t=self.ts[i]
            for j in range(self.d+1):out^=Q.nf[Q.idx[t[:j]+(0,)+t[j:]]]
        return out
    def ideal(self,I):
        gs=[self.place(a,0)for a in I.values()]
        return span(self.mul(g,b)for g in gs for b in self.bs)

def check(C,A,I):
    Q=Tensor(C,A,2);J0=span(C.mul(a,1<<i)for a in I.values()for i in range(C.n));J1=Q.ideal(I)
    diff=lambda c:Q.place(c,0)^Q.place(c,1)
    bd=span(diff(c)for c in J0.values())
    piv={};inv={}
    for i in range(C.n):
        v=normal(J1,diff(1<<i));w=1<<i
        while v:
            p=v.bit_length()-1
            if p not in piv:piv[p]=(v,w);break
            v^=piv[p][0];w^=piv[p][1]
        if not v:basis_add(inv,normal(J0,w))
    add=span([*bd.values()]+[diff(c)for c in inv.values()]);lg=span(bd.values())
    if len(add)==len(bd):return {'nonzero':False,'found':False}
    vals=[0]
    for b in inv.values():vals += [v^b for v in vals]
    witness=None
    for v in vals:
        if not v&1:continue
        x=Q.place(v,0);y=Q.place(v,1);vi=term=1
        for _ in range(1,C.d):term=Q.mul(term,x^1);vi^=term
        w=Q.mul(vi,y)^1
        assert not red(J1,w)
        if red(add,w)and witness is None:witness=(v,w)
        basis_add(lg,w)
    found=len(add)!=len(lg)or any(red(add,w)for w in lg.values())
    result={'nonzero':True,'found':found,'boundary_ranks':[len(add)-len(bd),len(lg)-len(bd)],'invariant_dim':len(inv)}
    if found:
        R=Tensor(C,A,3)
        assert all(Q.diff(w,R)==0 for w in lg.values())
        result.update({'ambient_monomials':C.ms,'A_basis':list(A.values()),'I_basis':list(I.values()),'J0_basis':list(J0.values()),'J1_basis':list(J1.values()),'ordinary_boundaries':list(bd.values()),'additive_boundaries':list(add.values()),'logarithmic_boundaries':list(lg.values()),'invariant_basis':list(inv.values()),'witness':witness,'tensor_dimensions':[C.n,Q.n,R.n]})
    return result

def main():
    rng=random.Random(92019);start=time.monotonic()
    r=int(sys.argv[1])if len(sys.argv)>1 else 2;d=int(sys.argv[2])if len(sys.argv)>2 else 4
    attempts=int(sys.argv[3])if len(sys.argv)>3 else 3000
    ideal_mode=sys.argv[4]if len(sys.argv)>4 else 'principal'
    C=Ring(r,d);seen=set();nz=0;found=[];hist={}
    for it in range(attempts):
        gs=[rng.randrange(1,1<<(C.n-1))<<1 for _ in range(rng.randrange(1,5))]
        A=closure(C,gs);av=list(A.values());v=0
        for _ in range(10):
            v=0
            for a in av:
                if rng.randrange(2):v^=a
            if v and C.mul(v,v)==0:break
        if not v or C.mul(v,v):continue
        I=span(C.mul(v,a)for a in av)
        if ideal_mode=='maximal':
            low=sum(1<<i for i,t in enumerate(C.ms)if sum(t)<(d+1)//2)
            piv={};kernel=[]
            for a in av:
                w=a;v=a&low
                while v:
                    j=v.bit_length()-1
                    if j not in piv:piv[j]=(v,w);break
                    v^=piv[j][0];w^=piv[j][1]
                if not v:kernel.append(w)
            I=span(kernel)
        elif ideal_mode=='double':
            for _ in range(10):
                w=0
                for a in av:
                    if rng.randrange(2):w^=a
                if w and not C.mul(w,w):
                    I=span([*I.values()]+[C.mul(w,a)for a in av]);break
        assert all(not C.mul(a,b)for a in I.values()for b in I.values())
        key=(tuple(normal(A,1<<i)for i in range(C.n)),tuple(normal(I,1<<i)for i in range(C.n)))
        if key in seen:continue
        seen.add(key);z=check(C,A,I);nz+=z['nonzero']
        if z['found']:found.append(z);print(json.dumps({'found':z}),flush=True);break
        k=str(z.get('boundary_ranks',[0,0]));hist[k]=hist.get(k,0)+1
        if it%200==0:print(json.dumps({'attempt':it,'tests':len(seen),'nonzero':nz,'seconds':time.monotonic()-start}),flush=True)
    print(json.dumps({'seed':92019,'variables':r,'nilpotence_order':d,'ideal_mode':ideal_mode,'attempts':attempts,'distinct_tests':len(seen),'nonzero_additive_boundaries':nz,'ranks':hist,'findings':found,'seconds':time.monotonic()-start},indent=2))

if __name__=='__main__':main()
