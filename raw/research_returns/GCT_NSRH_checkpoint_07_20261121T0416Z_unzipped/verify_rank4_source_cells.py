#!/usr/bin/env python3
"""Exact finite checks of GCT IV Figures 21/22 (Example 19.3).

Right-action convention: row r, column s is the coefficient of state s
in state r acted on by Q_i.  P_i = delta^2 I - Q_i.
All arithmetic is over ZZ[delta], followed by the exact substitution
delta = v + v^-1.  No numerical positivity inference is used.
This is a finite search certificate, not a positivity theorem.
"""
import argparse
import itertools
import json
import math
import random
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.domains import ZZ

R, delta = ring('delta', ZZ)
D, a, c = delta**2, delta**2-2, delta**2-4

def zero(n):
    return [[R.zero for _ in range(n)] for _ in range(n)]

def identity(n):
    m=zero(n)
    for i in range(n): m[i][i]=R.one
    return m

def add(A,B,scale=1):
    return [[x+scale*y for x,y in zip(ar,br)] for ar,br in zip(A,B)]

def mul(A,B):
    n=len(A); out=zero(n)
    for r in range(n):
        for h,x in enumerate(A[r]):
            if x:
                for s,y in enumerate(B[h]):
                    if y: out[r][s] += x*y
    return out

def scale(A,s):
    return [[x*s for x in row] for row in A]

def prod(seq,n):
    out=identity(n)
    for A in seq: out=mul(out,A)
    return out

def trace(A):
    return sum((A[i][i] for i in range(len(A))),R.zero)

def laurent(p):
    """Exact coefficients in v; exponents can be negative."""
    ans={}
    for (k,),coef in p.items():
        for j in range(k+1):
            e=k-2*j
            ans[e]=ans.get(e,0)+int(coef)*math.comb(k,j)
    return {e:n for e,n in sorted(ans.items()) if n}

def build(n,des,edges):
    Q=[zero(n) for _ in range(3)]
    for r,items in enumerate(des):
        for i in items: Q[i-1][r][r]=D
    for r,s,i,t in edges:
        assert Q[i-1][r][s] == 0
        Q[i-1][r][s]=R(t)
    P=[add(scale(identity(n),D),A,-1) for A in Q]
    return Q,P

# Figure 21: v12,v13,v23,v3,v2,v1 in the source's displayed notation.
Q6,P6=build(6,[{1,2},{1,3},{2,3},{3},{2},{1}],[
    (0,1,3,D),(1,0,2,1),(1,2,2,1),(2,1,1,D),
    (3,0,2,-1),(4,1,1,a),(4,1,3,a),(1,4,2,c),
    (5,2,2,-1),(4,0,1,1),(4,2,3,1),(3,4,2,2),
    (4,3,3,a),(4,5,1,a),(5,4,2,2)])

# Figure 22: v2,v13,v1,v22,v3 in the source's displayed notation.
Q5,P5=build(5,[{2},{1,3},{1},{2},{3}],[
    (0,1,1,-delta),(0,1,3,-delta),(1,0,2,-delta),
    (0,2,1,c),(2,3,2,a),(3,2,1,a),(2,1,3,-delta),
    (3,1,3,-delta),(3,4,3,-2),(4,3,2,-a),
    (0,4,3,c),(4,0,2,a),(4,1,1,-delta)])

def relations(gens):
    n=len(gens[0]); Z=zero(n)
    for A in gens: assert add(mul(A,A),scale(A,D),-1)==Z
    assert mul(gens[0],gens[2])==mul(gens[2],gens[0])
    for i,j in [(0,1),(1,2)]:
        A,B=gens[i],gens[j]
        rel=add(prod([A,B,A,B,A],n),prod([B,A,B,A,B],n),-1)
        rel=add(rel,scale(add(prod([A,B,A],n),prod([B,A,B],n),-1),D+a*a),-1)
        rel=add(rel,scale(add(A,B,-1),D*a*a))
        assert rel==Z

def all_norepeat(length):
    if length==0:
        yield (); return
    for w in all_norepeat(length-1):
        for i in range(3):
            if not w or i!=w[-1]: yield w+(i,)

def finite_search(gens,max_length):
    n=len(gens[0]); checked=0
    for length in range(1,max_length+1):
        total=0
        for word in all_norepeat(length):
            p=trace(prod([gens[i] for i in word],n)); coeff=laurent(p)
            total+=1; checked+=1
            if any(t<0 for t in coeff.values()):
                return {'status':'NEGATIVE','word':[i+1 for i in word],
                        'trace_delta':str(p),'laurent':coeff,'checked':checked}
        print(json.dumps({'length':length,'checked_this_length':total}),flush=True)
    return {'status':'NO_NEGATIVE_IN_FINITE_SEARCH','checked':checked}

def random_search(gens,count,max_length,seed):
    rng=random.Random(seed); n=len(gens[0])
    for k in range(count):
        length=rng.randint(1,max_length); word=[]
        for _ in range(length):
            choices=[i for i in range(3) if not word or i!=word[-1]]
            word.append(rng.choice(choices))
        p=trace(prod([gens[i] for i in word],n)); coeff=laurent(p)
        if any(t<0 for t in coeff.values()):
            return {'status':'NEGATIVE','word':[i+1 for i in word],
                    'trace_delta':str(p),'laurent':coeff,'checked':k+1,'seed':seed}
    return {'status':'NO_NEGATIVE_IN_SEEDED_SEARCH','checked':count,
            'max_length':max_length,'seed':seed}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-length',type=int,default=9)
    ap.add_argument('--random-count',type=int,default=0)
    ap.add_argument('--random-max-length',type=int,default=30)
    ap.add_argument('--seed',type=int,default=562104)
    ap.add_argument('--blocks',default='6P,6Q,5P,5Q')
    args=ap.parse_args()
    systems={'6P':P6,'6Q':Q6,'5P':P5,'5Q':Q5}
    for name,gens in systems.items():
        relations(gens)
        print(name+' quadratic/far/degree-five relations: PASS',flush=True)
    cyc=Q6[1][3][0]*Q6[2][0][1]*Q6[1][1][4]*Q6[2][4][3]
    assert cyc == -D*c*a
    pcyc=P6[1][3][0]*P6[2][0][1]*P6[1][1][4]*P6[2][4][3]
    assert pcyc==cyc
    print('Figure21 four-cycle coefficient product = -D(D-4)(D-2): PASS')
    for name in args.blocks.split(','):
        print('BEGIN '+name,flush=True)
        print(json.dumps(finite_search(systems[name],args.max_length)),flush=True)
        if args.random_count:
            print(json.dumps(random_search(systems[name],args.random_count,
                    args.random_max_length,args.seed)),flush=True)

if __name__=='__main__': main()
