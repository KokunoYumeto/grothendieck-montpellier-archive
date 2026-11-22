"""Exact characteristic-two Amitsur boundary search for finite closed covers.

A = F2[x_1,...,x_r]/(x_1,...,x_r)^d; A' = product A/K_i.
Tensor factors are A/(sum K_i), so the alternating Cech complex computes
degrees zero and one of the Amitsur complex. The square-zero base ideal is
m^ceil(d/2). Every quotient and every linear operation is exact bit arithmetic.
"""
from itertools import product, combinations
from A4_amitsur_search import basis_add, span, red
from A4_amitsur_random import normal
import random, json, sys, time

class Ring:
    def __init__(self,r,d):
        self.r,self.d=r,d
        self.ms=sorted([t for t in product(range(d),repeat=r) if sum(t)<d],key=lambda t:(sum(t),t))
        self.n=len(self.ms);self.idx={t:i for i,t in enumerate(self.ms)}
        self.mt=[]
        for t in self.ms:
            row=[]
            for u in self.ms:
                v=tuple(a+b for a,b in zip(t,u))
                row.append(1<<self.idx[v] if sum(v)<d else 0)
            self.mt.append(row)
    def mul(self,a,b):
        w=0
        while a:
            i=(a&-a).bit_length()-1;a&=a-1;c=b
            while c:
                j=(c&-c).bit_length()-1;c&=c-1;w^=self.mt[i][j]
        return w
    def ideal(self,gs):return span(self.mul(1<<i,g) for i in range(self.n) for g in gs)

class Quot:
    def __init__(self,A,K):
        self.A,self.K=A,K;self.bs=[1<<i for i in range(A.n) if i not in K]
        self.n=len(self.bs)
    def nf(self,a):return normal(self.K,a)

class Cover:
    def __init__(self,A,Ks,I):
        self.A,self.Ks,self.I=A,Ks,I;self.q=[];self.ts=[];self.off=[];self.masks=[];self.J=[];self.bs=[]
        for degree in range(3):
            ts=list(combinations(range(len(Ks)),degree+1));qs=[];offs=[];n=0;jj=[];bs=[]
            for t in ts:
                K=span(g for i in t for g in Ks[i].values());Q=Quot(A,K)
                qs.append(Q);offs.append(n)
                jj.extend(Q.nf(g)<<n for g in I.values())
                bs.extend(b<<n for b in Q.bs)
                n+=A.n
            self.ts.append(ts);self.q.append(qs);self.off.append(offs)
            self.masks.append((1<<A.n)-1);self.J.append(span(jj));self.bs.append(bs)
        self.one=sum(1<<o for o in self.off[0])
    def diff(self,deg,x):
        out=0;src={t:i for i,t in enumerate(self.ts[deg])}
        for j,t in enumerate(self.ts[deg+1]):
            a=0
            for u in combinations(t,len(t)-1):
                i=src[u];a^=(x>>self.off[deg][i])&self.masks[deg]
            out^=self.q[deg+1][j].nf(a)<<self.off[deg+1][j]
        return out
    def invariant_basis(self):
        piv={};ker=[]
        for b in self.bs[0]:
            v=normal(self.J[1],self.diff(0,b));w=b
            while v:
                p=v.bit_length()-1
                if p not in piv:piv[p]=(v,w);break
                v^=piv[p][0];w^=piv[p][1]
            if not v:ker.append(normal(self.J[0],w))
        return list(span(ker).values())
    def log_boundary(self,u):
        out=0;A=self.A
        for j,(a,b) in enumerate(self.ts[1]):
            Q=self.q[1][j]
            x=Q.nf((u>>self.off[0][a])&self.masks[0]);y=Q.nf((u>>self.off[0][b])&self.masks[0])
            assert x&1 and y&1
            inv=term=1
            for _ in range(1,A.d):term=Q.nf(A.mul(term,x^1));inv^=term
            out^=(Q.nf(A.mul(inv,y))^1)<<self.off[1][j]
        return out
    def inspect(self,maxdim=18):
        ib=self.invariant_basis();bd=span(self.diff(0,v)for v in self.J[0].values())
        add=span([*bd.values()]+[self.diff(0,v)for v in ib])
        logs=span(bd.values());witness=None
        if len(add)==len(bd):return {'dimension':len(ib),'add_rank':0,'log_rank':0,'found':False}
        if len(ib)>maxdim:return {'dimension':len(ib),'add_rank':len(add)-len(bd),'skipped':True}
        # Enumerate all invariant units; they are exactly those with residue 1.
        vals=[0]
        for b in ib:vals += [v^b for v in vals]
        for u in vals:
            if not u&1:continue
            z=self.log_boundary(u)
            assert not red(self.J[1],z) and self.diff(1,z)==0
            if red(add,z) and witness is None:witness=(u,z)
            basis_add(logs,z)
        found=len(add)!=len(logs) or any(red(add,v) for v in logs.values())
        result={'dimension':len(ib),'add_rank':len(add)-len(bd),'log_rank':len(logs)-len(bd),'found':found}
        if found:
            result.update({'ring_monomials':self.A.ms,'ideals':[list(K.values()) for K in self.Ks],
                'I':list(self.I.values()),'invariant_basis':ib,'ordinary_boundaries':list(bd.values()),
                'additive_boundaries':list(add.values()),'logarithmic_boundaries':list(logs.values()),'witness':witness})
        return result

def main():
    seed=29019;rng=random.Random(seed);start=time.monotonic()
    r=int(sys.argv[1])if len(sys.argv)>1 else 3
    d=int(sys.argv[2])if len(sys.argv)>2 else 4
    attempts=int(sys.argv[3])if len(sys.argv)>3 else 2000
    A=Ring(r,d);I=span(1<<i for i,t in enumerate(A.ms)if sum(t)>=(d+1)//2)
    deg1=[i for i,t in enumerate(A.ms)if sum(t)==1];higher=[i for i,t in enumerate(A.ms)if sum(t)>=2]
    found=[];nonzero=0;skipped=0;hist={};seen=set()
    for it in range(attempts):
        gs=[]
        for _ in range(rng.choice([3,3,4])):
            g=0
            for i in deg1:
                if rng.randrange(2):g^=1<<i
            if not g:g=1<<rng.choice(deg1)
            for _ in range(rng.randrange(4)):
                g^=1<<rng.choice(higher)
            gs.append(g)
        Ks=[A.ideal([g])for g in gs]
        key=tuple(sorted(tuple(normal(K,1<<i)for i in range(A.n))for K in Ks))
        if key in seen:continue
        seen.add(key);C=Cover(A,Ks,I);res=C.inspect()
        skipped+=res.get('skipped',False)
        if res['add_rank']:nonzero+=1
        if res.get('found'):
            res['generators']=gs;found.append(res);print(json.dumps({'witness':res}),flush=True);break
        k=(res['add_rank'],res.get('log_rank'));hist[str(k)]=hist.get(str(k),0)+1
        if it%200==0:print(json.dumps({'attempt':it,'distinct_tests':len(seen),'nonzero':nonzero,'seconds':time.monotonic()-start}),flush=True)
    print(json.dumps({'seed':seed,'variables':r,'nilpotence_order':d,'attempts':attempts,'distinct_tests':len(seen),'nonzero_additive_boundaries':nonzero,'skipped':skipped,'ranks':hist,'findings':found,'seconds':time.monotonic()-start},indent=2))

if __name__=='__main__':main()
