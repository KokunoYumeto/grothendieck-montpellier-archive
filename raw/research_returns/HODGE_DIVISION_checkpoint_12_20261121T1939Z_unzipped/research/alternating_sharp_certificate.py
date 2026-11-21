#!/usr/bin/env python3
"""Exact checks for HD-ALT03; all-degree conclusions use its written proof."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from math import factorial,prod
import hashlib,json,time
P=Path(__file__).resolve().parent

def parts(n,cap=None):
    if not n:
        yield ()
        return
    for k in range(min(n,cap or n),0,-1):
        for tail in parts(n-k,k):yield (k,)+tail

def contents(lam):return [j-i for i,w in enumerate(lam) for j in range(w)]
def degree(lam):
    cols=[sum(w>j for w in lam) for j in range(lam[0])]
    return factorial(sum(lam))//prod(w-j+cols[j]-i-1 for i,w in enumerate(lam) for j in range(w))
def ratios(lam):
    n=sum(lam); c=contents(lam); t=sum(c); S=sum(z*z for z in c)
    return F(3*(S-n*(n-1)//2),n*(n-1)*(n-2)),F(4*(t*t+n*(n-1)-3*S),n*(n-1)*(n-2)*(n-3))
start=time.monotonic()
inputs=(P/'alternating_small_inputs.json').read_bytes(); data=json.loads(inputs)
matched=0
for tab in data['tables']:
    if not tab['name'].startswith('Sym'):continue
    n=tab['n'];pars=[p[1] for p in tab['class_parameters']]
    j3=pars.index([3]+[1]*(n-3));j22=pars.index([2,2]+[1]*(n-4))
    for par,chi in zip(tab['character_parameters'],tab['characters']):
        lam=par[1]; u,v=ratios(lam);a=chi[0]
        assert degree(lam)==a
        assert u==F(chi[j3],a) and v==F(chi[j22],a)
        matched+=1
all_count=balanced_count=0;rows=[]
for n in range(15,33):
    k=(n+1)//2;mn=None;maxu=F(-100);maxv=F(-100);num=0
    for lam in parts(n):
        all_count+=1
        if max(lam[0],len(lam))>k:continue
        balanced_count+=1;num+=1
        c=contents(lam); t=sum(c); S=sum(z*z for z in c);u,v=ratios(lam)
        assert abs(t)<=F(n*(k-1),2)-(n-k)<=F((n-1)*(n-2),4)
        assert u<=F(n-5,4*(n-2))<F(1,4)
        vb=F((n-1)*(n-2)**2+16*n,4*n*(n-2)*(n-3))
        assert v<=vb<F(3,10)
        assert min((1-u)/3,(1-v)/4)>=F(7,40)
        a=F(degree(lam),2)
        assert a>=F(n**3,27)>60
        mn=min(mn or a,a);maxu=max(maxu,u);maxv=max(maxv,v)
    rows.append(dict(n=n,balanced_partitions=num,min_half_specht_degree=str(mn),max_three_cycle_ratio=str(maxu),max_double_transposition_ratio=str(maxv)))
# Exact polynomial positivity: p(15)=1010, forward difference3n²-7n-88.
p=lambda n:n**3-5*n*n-84*n+20
assert p(15)==1010
for n in range(15,1001):
    assert p(n+1)-p(n)==3*n*n-7*n-88>0
    assert F(21,10)*61>2*61+6

def perm(lam):
    n=sum(lam);g=list(range(n));cycles=[];start=0
    for w in lam:
        cy=list(range(start,start+w));cycles.append(cy)
        for i in range(w):g[cy[i]]=cy[(i+1)%w]
        start+=w
    return tuple(g),cycles
def cyc(n,ls):
    q=list(range(n))
    for i,x in enumerate(ls):q[x]=ls[(i+1)%len(ls)]
    return tuple(q)
def mul(p,q):return tuple(p[q[i]] for i in range(len(p)))
def inv(p):
    q=list(p)
    for i,z in enumerate(p):q[z]=i
    return tuple(q)
def comm(g,x):return mul(mul(mul(g,x),inv(g)),inv(x))
def cycle_type(g):
    seen=set();ls=[]
    for i in range(len(g)):
        if i in seen:continue
        j=i;m=0
        while j not in seen:seen.add(j);m+=1;j=g[j]
        if m>1:ls.append(m)
    return sorted(ls)
comm_count=split_count=0
for n in range(15,26):
    for lam in parts(n):
        if lam[0]==1:continue
        g,cs=perm(lam);long=next((c for c in cs if len(c)>=3),None)
        if long:x=cyc(n,long[:2]);expected=[3]
        elif 1 in lam:
            two=next(c for c in cs if len(c)==2);fixed=next(c for c in cs if len(c)==1)
            x=cyc(n,[two[0],fixed[0]]);expected=[3]
        else:x=cyc(n,[cs[0][0],cs[1][0]]);expected=[2,2]
        assert cycle_type(comm(g,x))==expected;comm_count+=1
        if all(w%2 for w in lam) and len(lam)==len(set(lam)):
            long=next(c for c in cs if len(c)>=5)
            assert cycle_type(comm(g,cyc(n,long[:3])))==[3];split_count+=1
out={'status':'PASS','input_sha256':hashlib.sha256(inputs).hexdigest(),'complete_symmetric_rows_matched':matched,
 'all_partitions_15_to_32':all_count,'balanced_partitions_15_to_32':balanced_count,
 'commutator_cycle_types_15_to_25':comm_count,'even_conjugator_distinct_odd_cycle_types':split_count,
 'cases':rows,'polynomial_base':1010,'polynomial_forward_difference':'3n^2-7n-88',
 'scope':'Exact finite content, hook, ratio, group commutator and endpoint checks. All-n inequalities and full normalizer/split/tensor arguments are in the written proof; no finite extrapolation.',
 'proof_sha256':hashlib.sha256((P/'ordinary_alternating_sharp_obstruction.tex').read_bytes()).hexdigest(),
 'seconds':round(time.monotonic()-start,3)}
(P/'alternating_sharp_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
