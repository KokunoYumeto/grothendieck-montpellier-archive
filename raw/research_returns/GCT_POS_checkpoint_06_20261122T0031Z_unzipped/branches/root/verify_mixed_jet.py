#!/usr/bin/env python3
"""Independent mixed-jet certificate replay using local Smith elimination.

Imports no nonstandard-branch code. Implements normalized standard Hecke
multiplication directly, reconstructs the supplied P-words, verifies their
full algebra closure, and counts additive subgroup sizes by unit pivoting.
All arithmetic is exact modulo p**k. NumPy int64 products are bounded here
by (p**k-1)**2; the default modulus is 1024.
"""
import argparse, itertools, json, math, pathlib, time
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument('certificate',type=pathlib.Path)
ap.add_argument('--output',type=pathlib.Path)
args=ap.parse_args()
cert=json.loads(args.certificate.read_text())
p,k,L=cert['p'],cert['k'],cert['jet_length']
q=p**k
assert q*q < 2**60
perms=list(itertools.permutations(range(4)))
pi={w:i for i,w in enumerate(perms)}
pairs=[(i,j) for i in range(24) for j in range(i,24)]
ix={u:i for i,u in enumerate(pairs)}
W=len(pairs); D=W*L
assert W==300

def poly_add(a,b,scale=1):
    return [(x+scale*y)%q for x,y in zip(a,b)]

def poly_mul(a,b):
    return [sum(a[j]*b[h-j] for j in range(h+1))%q for h in range(L)]

one=[1]+[0]*(L-1)
v=[1,1]+[0]*(L-2)
vi=[(-1)**i%q for i in range(L)]
r=poly_add(v,vi,-1)
minus_r=[-x%q for x in r]
vv=poly_add(poly_mul(v,v),poly_mul(vi,vi))

def ts(w,s):
    z=list(perms[w]); z[s],z[s+1]=z[s+1],z[s]
    ans=[(pi[tuple(z)],one)]
    if perms[w][s]>perms[w][s+1]: ans.append((w,r))
    return ans

# P_s = 2 T_s tensor T_s - r(T_s tensor 1 + 1 tensor T_s)
#       + (v^2+v^-2) 1 tensor 1.
operators=[]
for s in range(3):
    base=[]
    for i,j in pairs:
        temp={}
        def accum(a,b,pol,scale=1):
            if a>b: return  # symmetric coefficients are read in one half
            t=ix[a,b]
            temp[t]=poly_add(temp.get(t,[0]*L),pol,scale)
        for a,b in ([(i,j)] if i==j else [(i,j),(j,i)]):
            for u,pc in ts(a,s):
                for z,pd in ts(b,s):accum(u,z,poly_mul(pc,pd),2)
                accum(u,b,poly_mul(pc,minus_r))
            for z,pd in ts(b,s):accum(a,z,poly_mul(pd,minus_r))
            accum(a,b,vv)
        base.append([(t,h,c) for t,pol in temp.items() for h,c in enumerate(pol) if c])
    operators.append([[(t+(e+h)*W,c) for t,h,c in base[j] if e+h<L]
                      for e in range(L) for j in range(W)])

def multiply(x,s):
    out=np.zeros(D,dtype=np.int64)
    for j in np.flatnonzero(x):
        c=int(x[j])
        for target,b in operators[s][int(j)]:out[target]=(out[target]+c*b)%q
    return out

def shift(x,h=1):
    z=np.zeros(D,dtype=np.int64)
    if h<L:z[h*W:]=x[:D-h*W]
    return z

word_cache={():np.eye(1,D,ix[0,0],dtype=np.int64)[0]}
def word(w):
    w=tuple(w)
    if w not in word_cache:word_cache[w]=multiply(word(w[:-1]),w[-1]-1)
    return word_cache[w]

class LocalSmith:
    """Invertible row operations over Z/q; choose a globally least-valued pivot.

    A pivot row with pivot p**b has all its coordinates divisible by p**b,
    so its additive order is exactly p**(k-b), and its annihilator creates
    no residual row. Projection to successive pivot coordinates therefore
    proves that the row-span cardinality is the product of these orders.
    The chosen pivot columns need not be in their original order.
    """
    def __init__(self,rows,label):
        a=np.asarray(rows,dtype=np.int64).copy()%q
        pivots=[]; at=0; valuation=0
        while at<len(a) and valuation<k:
            block=a[at:]
            divisor=p**valuation
            positions=np.argwhere(block%(divisor*p)!=0)
            if not len(positions):valuation+=1;continue
            rr,cc=map(int,positions[0]);rr+=at
            if rr!=at:a[[at,rr]]=a[[rr,at]]
            assert int(a[at,cc])%divisor==0
            unit=int(a[at,cc])//divisor
            a[at]=(a[at]*pow(unit,-1,q))%q
            assert a[at,cc]==divisor and np.all(a[at]%divisor==0)
            active=np.flatnonzero(a[at+1:,cc])+at+1
            for start in range(0,len(active),32):
                ids=active[start:start+32]
                coeff=(a[ids,cc]//divisor).reshape(-1,1)
                a[ids]=(a[ids]-coeff*a[at])%q
            assert np.all(a[at+1:,cc]==0)
            pivots.append((cc,valuation));at+=1
            if at%100==0:print(label,at,'pivots',flush=True)
        assert not np.any(a[at:])
        self.rows=a[:at];self.pivots=pivots
        self.logsize=sum(k-b for _,b in pivots)
        self.cyclic_counts={str(b):sum(bb==b for _,bb in pivots) for b in range(k)}
        print(label,'log size',self.logsize,'cyclic factors',self.cyclic_counts,flush=True)
    def contains(self,x):
        x=x.copy()%q
        for row,(j,b) in zip(self.rows,self.pivots):
            d=p**b
            if int(x[j])%d:return False
            if x[j]:x=(x-(int(x[j])//d)*row)%q
        return not np.any(x)

started=time.time()
vectors=[word(w) for w in cert['accepted_words']]
assert np.count_nonzero(vectors[0])==1 and vectors[0][ix[0,0]]==1
M=LocalSmith([shift(x,h) for x in vectors for h in range(L)],'M')
# Algebra closure proves that this finite list spans the full P-generated
# image: the span contains 1, is an R-module, and is stable under each P_i.
for x in vectors:
    assert M.contains(shift(x))
    for s in range(3):assert M.contains(multiply(x,s))
N=LocalSmith([p*x%q for x in vectors]+[shift(x,h) for x in vectors for h in range(1,L)],'mM')
for row in M.rows:
    assert N.contains(p*row%q)
    assert N.contains(shift(row))
assert M.logsize==cert['log_p_size_M']
assert N.logsize==cert['log_p_size_mM']
mu=M.logsize-N.logsize
assert mu==cert['minimal_generators_image']
result={'status':'PASS','method':'Independent standard-Hecke formula and global-valuation local Smith row elimination',
        'p':p,'k':k,'jet_length':L,'accepted_words':len(vectors),'closure_verified':True,
        'log_p_size_M':M.logsize,'log_p_size_mM':N.logsize,'minimal_generators_image':mu,
        'cyclic_valuation_counts_M':M.cyclic_counts,'cyclic_valuation_counts_mM':N.cyclic_counts,
        'generic_rank':114,'nonfreeness_obstruction':mu>114,'seconds':time.time()-started}
dest=args.output or args.certificate.with_name(args.certificate.stem+'_independent_verification.json')
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
