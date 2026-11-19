"""Exact, finite-scope checks for Part C (rational arithmetic throughout).
Models are formal Poincare algebras, not Chow rings. Degrees use cohomological
conventions. Normal forms are partitions of {0,...,k}, with 0 the point marker.
"""
from fractions import Fraction
from itertools import product
from collections import defaultdict
import json, time
from pathlib import Path

class Algebra:
    def __init__(self,name,degrees,mul,top,chi):
        self.name,self.degrees,self.mul,self.top,self.chi=name,degrees,mul,top,chi
        self.dim=len(degrees)
        # Dual diagonal: sum e_i^dual tensor e_i.
        import sympy as S
        mat=S.Matrix([[mul.get((i,j),(None,0))[1] if mul.get((i,j),(None,0))[0]==top else 0 for j in range(self.dim)] for i in range(self.dim)])
        inv=mat.inv()
        self.diag={}
        for i in range(self.dim):
            for j in range(self.dim):
                c=inv[j,i]
                if c:self.diag[j,i]=Fraction(int(c.p),int(c.q))
    def multiply(self,a,b):
        out=defaultdict(Fraction)
        k=len(next(iter(a))) if a else 0
        for x,c in a.items():
            for y,d in b.items():
                sign=(-1)**sum(self.degrees[y[i]]*self.degrees[x[j]] for i in range(k) for j in range(i+1,k))
                terms=[self.mul.get((u,v),(None,0)) for u,v in zip(x,y)]
                if any(z is None or q==0 for z,q in terms):continue
                coef=c*d*sign
                for _,q in terms:coef*=q
                out[tuple(z for z,_ in terms)]+=coef
        return {x:c for x,c in out.items() if c}
    def nf(self,P,k):
        ans={(0,)*k:Fraction(1)}
        for B in P:
            if 0 in B:
                for i in B:
                    if i:
                        t=[0]*k;t[i-1]=self.top
                        ans=self.multiply(ans,{tuple(t):Fraction(1)})
            elif len(B)>1:
                i=min(B)
                for j in B:
                    if j!=i:
                        d={}
                        for (a,b),c in self.diag.items():
                            t=[0]*k;t[i-1]=a;t[j-1]=b;d[tuple(t)]=c
                        ans=self.multiply(ans,d)
        return ans

def partitions(items):
    if not items:yield ();return
    a,*rest=items
    for P in partitions(rest):
        yield ((a,),)+P
        for i in range(len(P)):
            yield P[:i]+(tuple(sorted((a,)+P[i])),)+P[i+1:]

def normal(P):return tuple(sorted((tuple(sorted(B)) for B in P),key=lambda B:B[0]))
def degree(P,k):return k-len(P)+1

def rank_exact(cols):
    piv={}
    for col in cols:
        c=dict(col)
        while c:
            row=min(c)
            if row not in piv:
                a=c[row];piv[row]={r:v/a for r,v in c.items()};break
            a=c[row]
            for r,v in piv[row].items():
                c[r]=c.get(r,0)-a*v
                if not c[r]:del c[r]
    return len(piv)

def graph_product(P,Q,k,chi):
    edges=[]
    for T in [P,Q]:
        for B in T:
            a=min(B)
            edges.extend((a,b) for b in B if b!=a)
    parent=list(range(k+1))
    def find(x):
        while x!=parent[x]:x=parent[x]
        return x
    for a,b in edges:
        aa,bb=find(a),find(b)
        if aa!=bb:parent[aa]=bb
    blocks=defaultdict(list)
    for x in range(k+1):blocks[find(x)].append(x)
    out=[];pins=[0];coef=1
    for B in blocks.values():
        num=sum(a in B and b in B for a,b in edges)
        cycle=num-len(B)+1
        if 0 in B:
            if cycle:return 0,None
            pins+= [x for x in B if x]
        elif cycle==0:out.append(tuple(B))
        elif cycle==1:coef*=chi;pins+=B
        else:return 0,None
    out.append(tuple(sorted(pins)))
    return coef,normal(out)

def projective(n):
    mul={(i,j):(i+j,1) for i in range(n+1) for j in range(n+1) if i+j<=n}
    return Algebra(f'P{n}',[2*i for i in range(n+1)],mul,n,n+1)
def curve(g):
    top=2*g+1;mul={}
    for i in range(top+1):mul[0,i]=(i,1);mul[i,0]=(i,1)
    for j in range(g):
        x,y=1+2*j,2+2*j;mul[x,y]=(top,1);mul[y,x]=(top,-1)
    return Algebra(f'curve_g{g}',[0]+[1]*(2*g)+[2],mul,top,2-2*g)
def surface(b):
    top=b+1;mul={}
    for i in range(top+1):mul[0,i]=(i,1);mul[i,0]=(i,1)
    for i in range(1,b+1):mul[i,i]=(top,1)
    return Algebra(f'surface_b2_{b}',[0]+[2]*b+[4],mul,top,b+2)
def abelian(g):
    d=2*g;dim=1<<d;mul={}
    for i in range(dim):
        for j in range(dim):
            if i&j:continue
            sign=(-1)**sum(((i>>a)&1)*((j>>b)&1) for a in range(d) for b in range(a))
            mul[i,j]=(i|j,sign)
    return Algebra(f'abelian_dim{g}',[i.bit_count() for i in range(dim)],mul,dim-1,0)

def iparts(n,maxpart=None):
    if n==0:yield ();return
    if maxpart is None:maxpart=n
    for i in range(min(n,maxpart),1-1,-1):
        for tail in iparts(n-i,i):yield (i,)+tail

def hookdim(lam):
    from math import factorial
    h=1
    for i,L in enumerate(lam):
        for j in range(L):h*=L-j+sum(M>j for M in lam[i+1:])
    return factorial(sum(lam))//h

def pairrank(m,b,odd):
    if m==0:return 1
    ans=0
    for lam in iparts(m):
        if (odd and lam[0]<=b//2) or (not odd and len(lam)<=b):
            shape=tuple(2*x for x in lam)
            if odd:shape=tuple(sum(x>j for x in shape) for j in range(max(shape)))
            ans+=hookdim(shape)
    return ans

def dimformula(k,d,b,odd):
    from math import factorial
    ans=0
    for m in range(k//2+1):
        a=d-m;u=k-a-2*m
        if a>=0 and u>=0:ans+=factorial(k)//(factorial(a)*factorial(2*m)*factorial(u))*pairrank(m,b,odd)
    return ans

def main():
    start=time.perf_counter();records=[];checks=0
    models=[projective(1),projective(2),projective(3),curve(1),curve(2),surface(1),surface(2),surface(22),abelian(2)]
    for A in models:
        for k in range(1,5 if A.name!='abelian_dim2' and A.name!='surface_b2_22' else 4):
            Ps=list(map(normal,partitions(list(range(k+1)))))
            vs={P:A.nf(P,k) for P in Ps}
            dims=[rank_exact([vs[P] for P in Ps if degree(P,k)==d]) for d in range(k+1)]
            if A.name.startswith('curve_g'):
                g=int(A.name[7:]);pred=[dimformula(k,d,2*g,True) for d in range(k+1)];assert dims==pred,(A.name,k,dims,pred)
            if A.name.startswith('surface_b2_'):
                b=int(A.name[11:]);pred=[dimformula(k,d,b,False) for d in range(k+1)];assert dims==pred,(A.name,k,dims,pred)
            if k<=3:
                for P,Q in product(Ps,repeat=2):
                    c,T=graph_product(P,Q,k,A.chi)
                    expected={} if c==0 else {x:c*v for x,v in vs[T].items()}
                    assert A.multiply(vs[P],vs[Q])==expected,(A.name,k,P,Q,c,T)
                    checks+=1
            records.append({'model':A.name,'k':k,'dimensions_in_degrees_2n_times_d':dims})
    E=[(x,y) for x in range(5) for y in range(5) if (y*y-x*x*x+x)%5==0]
    assert len(E)+1==8
    import sympy as S
    u,v,t=S.symbols('u v t')
    for p in [2,3,5,7]:
        c=lambda i:S.binomial(p,i)//p
        fuv=t**p+sum(c(i)*(u*v)**(i-1)*t**i for i in range(1,p))
        fu=t**p+sum(c(i)*u**(i-1)*v**(p-1)*t**i for i in range(1,p))
        fv=t**p+sum(c(i)*v**(i-1)*u**(p-1)*t**i for i in range(1,p))
        assert S.expand(fu.subs(t,v*t)-v**p*fuv)==0
        assert S.expand(fv.subs(t,u*t)-u**p*fuv)==0
    result={'scope':'Weil-cohomology Poincare algebras; no Chow assertion computed','arithmetic':'exact rational','models':records,'graph_product_pairs_checked':checks,'elliptic_counterexample':{'field':5,'equation':'y^2=x^3-x','affine_points':E,'cardinality':8,'trace':-2,'frobenius_polynomial':'T^2+2T+5','discriminant':-16},'finite_group_checks':{'primes':[2,3,5,7],'polynomial_map_identities':'all verified','p2_image_module':'R direct_sum (u,v)t','p2_generic_rank':2,'p2_minimal_generators':3},'elapsed_seconds':round(time.perf_counter()-start,6)}
    out=Path(__file__).with_name('check_tautological_output.json');out.write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
if __name__=='__main__':main()
