#!/usr/bin/env python3
"""Finite sanity checks for new deductions. This is not a replay of E.

Exhaustive small truth tables test the new Boolean algebra identities,
parsimonious gate encoding, greedy-survivor invariant, and coefficientwise
energy recovery. The full asymptotic proofs are in consequences.json.
"""
import itertools, json, math, pathlib, random
from collections import Counter
import sympy as sp

rng=random.Random(20261121)
results=[]

def plus(p,q): return p.symmetric_difference(q)
def times(p,q):
    ans=set()
    for a in p:
        for b in q:
            z=a|b
            if z in ans: ans.remove(z)
            else: ans.add(z)
    return ans
def val(p,x): return sum((a&x)==a for a in p)%2
def random_system(n,m):
    monos=[a for a in range(1<<n) if a.bit_count()<=2]
    return [set(rng.sample(monos,rng.randrange(min(4,len(monos))+1))) for _ in range(m)]

cases=0
for n in range(1,7):
    for _ in range(30):
        fs=random_system(n,rng.randrange(n+3))
        p={0}
        for f in fs: p=times(p,plus({0},f))
        count=sum(all(val(f,x)==0 for f in fs) for x in range(1<<n))
        assert count%2==int((1<<n)-1 in p)
        pref={0}; telesc=set()
        for f in fs:
            telesc=plus(telesc,times(f,pref))
            pref=times(pref,plus({0},f))
        assert telesc==plus({0},p)
        if count==0: assert telesc=={0}
        cases+=1
results.append({'finding_ids':['NN-C005','NN-C009'],'check':'top coefficient and telescoping identities in Boolean quotient','cases':cases,'result':'pass'})

cases=0
for inputs in range(1,4):
    for _ in range(25):
        gates=[]
        for j in range(4):
            a=rng.randrange(inputs+j)
            if rng.randrange(2): gates.append(('not',a))
            else: gates.append(('and',a,rng.randrange(inputs+j)))
        fs=[]
        for j,g in enumerate(gates):
            z=1<<(inputs+j)
            if g[0]=='not': fs.append(plus(plus({z},{1<<g[1]}),{0}))
            else: fs.append(plus({z},{(1<<g[1])|(1<<g[2])}))
        fs.append({1<<(inputs+len(gates)-1),0})
        true=0
        for x in range(1<<inputs):
            vals=[(x>>i)&1 for i in range(inputs)]
            for g in gates:
                vals.append(1-vals[g[1]] if g[0]=='not' else vals[g[1]]*vals[g[2]])
            true+=vals[-1]
        got=sum(all(val(f,x)==0 for f in fs) for x in range(1<<(inputs+len(gates))))
        assert true==got
        assert all(len(f)<=3 and all(a.bit_count()<=2 for a in f) for f in fs)
        cases+=1
results.append({'finding_ids':['NN-C005','NN-C006'],'check':'AND/NOT gate equations preserve exact counts with unique extension','cases':cases,'result':'pass'})

cases=0
for n in range(1,5):
    m=6
    for _ in range(20):
        vectors=[rng.randrange(1<<m) for _ in range(1<<n)]
        # Include actual zeros in many cases; other vectors need not arise from clauses.
        for j in range(len(vectors)):
            if rng.randrange(5)==0: vectors[j]=0
        survivors=list(range(1<<n)); true=sum(z==0 for z in vectors)
        for step in range(3*n):
            oldfalse=len(survivors)-true
            h=min(range(1<<m), key=lambda h:sum((vectors[x]&h).bit_count()%2==0 for x in survivors))
            survivors=[x for x in survivors if (vectors[x]&h).bit_count()%2==0]
            assert len(survivors)-true <= 0.75*oldfalse
        assert all(vectors[x]==0 for x in survivors)
        assert len(survivors)==true
        cases+=1
results.append({'finding_ids':['NN-C001'],'check':'abstract greedy invariant on arbitrary violation maps using exhaustive row family; not E Tanner-code construction','cases':cases,'result':'pass'})

y=sp.Symbol('y')
cases=0
for n in range(1,5):
    ell=n+1
    p=sp.Poly((1-y)**ell*sum(sp.binomial(ell+j-1,j)*y**j for j in range(ell)),y)
    h=sp.Poly(y*(y-1),y)
    es=[]
    for j in range(ell):
        p,rem=sp.div(p,h);es.append(rem)
    assert p.is_zero
    for _ in range(8):
        fs=random_system(n,n+2)
        histogram=Counter(); lifted=Counter()
        for x in range(1<<n):
            energy=sum((2*i+1)*((x>>i)&1) for i in range(n))
            energy+=2*int(n>=2 and (x&3)==3)
            if all(val(f,x)==0 for f in fs): histogram[energy]+=1
            coeff=[1]+[0]*(ell-1)
            for f in fs:
                L=sum((a&x)==a for a in f)
                factor=[int(es[j].eval(L))*(L*(L-1))**j for j in range(ell)]
                coeff=[sum(coeff[i]*factor[s-i] for i in range(s+1)) for s in range(ell)]
            lifted[energy]+=sum(coeff)
        recovered={a:b%(1<<ell) for a,b in lifted.items() if b%(1<<ell)}
        assert recovered==dict(histogram)
        cases+=1
results.append({'finding_ids':['NN-C013'],'check':'global V-truncation and coefficientwise 2^(n+1) recovery of weighted energy histogram','cases':cases,'result':'pass'})

# Gate builder verifies the linear-size Hamming addition-tree construction.
class Circuit:
    def __init__(self,n): self.n=n;self.gates=[]
    def gate(self,op,*args):
        self.gates.append((op,args));return self.n+len(self.gates)-1
    def xor(self,a,b): return self.gate('xor',a,b)
    def land(self,a,b): return self.gate('and',a,b)
    def lor(self,a,b): return self.gate('or',a,b)
    def add(self,a,b):
        out=[];carry=None
        for j in range(max(len(a),len(b))):
            z=[x for x in [a[j] if j<len(a) else None,b[j] if j<len(b) else None,carry] if x is not None]
            if len(z)==1: out.append(z[0]);carry=None
            elif len(z)==2: out.append(self.xor(*z));carry=self.land(*z)
            else:
                x=self.xor(z[0],z[1]);out.append(self.xor(x,z[2]))
                carry=self.lor(self.land(z[0],z[1]),self.land(x,z[2]))
        if carry is not None: out.append(carry)
        return out
    def evaluate(self,bits,out):
        vals=list(bits)
        for op,args in self.gates:
            a,b=(vals[t] for t in args)
            vals.append(a^b if op=='xor' else a*b if op=='and' else int(a or b))
        return sum(vals[j]<<i for i,j in enumerate(out))
cases=0;ratios=[]
for n in range(1,11):
    c=Circuit(n);level=[[i] for i in range(n)]
    while len(level)>1:
        level=[c.add(level[i],level[i+1]) if i+1<len(level) else level[i] for i in range(0,len(level),2)]
    for x in range(1<<n):
        assert c.evaluate([(x>>i)&1 for i in range(n)],level[0])==x.bit_count();cases+=1
    ratios.append((n,len(c.gates)/n))
results.append({'finding_ids':['NN-C013'],'check':'balanced Hamming addition tree on all inputs n<=10; asymptotic linear bound proved separately','cases':cases,'observed_gate_count_per_input':ratios,'result':'pass'})

out=pathlib.Path(__file__).with_name('FINITE_CHECK_RESULTS.json')
out.write_text(json.dumps({'scope':'Finite examples check derived identities; not full proof of E or asymptotic runtime.','checks':results},indent=2)+'\n')
print(json.dumps({'checks':len(results),'cases':sum(x['cases'] for x in results),'result':'all pass'}))
