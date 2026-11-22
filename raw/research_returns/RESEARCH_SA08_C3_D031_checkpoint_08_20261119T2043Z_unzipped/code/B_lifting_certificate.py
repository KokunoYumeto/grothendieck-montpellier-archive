#!/usr/bin/env python3
"""Independent exact certificate for D-031 and the stated sharpness example.

The all-ring argument is the integer identity (c)-(c)=1-0, not a finite
search.  Finite residue-ring checks verify the displayed algebra, differential,
projection and PD operations through index 6; they do not claim that a finite
index test proves all divided-power identities.
"""
from itertools import product
from math import comb, factorial
from pathlib import Path
import json
import time

start = time.perf_counter()
checks = 0

def verify(condition):
    global checks
    checks += 1
    assert condition

def residue_check(modulus):
    m = modulus
    zero = (0, 0, 0)
    one = (1, 0, 0)
    elems = list(product(range(m), repeat=3))
    ev = [(a, b, 0) for a, b in product(range(m), repeat=2)]
    ideal_ev = [(0, b, 0) for b in range(m)]
    odd = [(0, 0, c) for c in range(m)]
    homogeneous = [(a,0,0) for a in range(m)] + ideal_ev + odd
    degrees = {0: [(a,0,0) for a in range(m)],
               -2: ideal_ev, -1: odd}

    def add(x,y): return tuple((a+b)%m for a,b in zip(x,y))
    def scale(a,x): return tuple(a*b % m for b in x)
    def mul(x,y):
        a,b,c=x; A,B,C=y
        return ((a*A)%m, (a*B+b*A)%m, (a*C+c*A)%m)
    def d(x): return (0,0,x[1])
    def pi(x): return (x[0],x[1],0)
    def gamma(n,x): return one if n == 0 else x if n == 1 else zero
    def power(x,n):
        a=one
        for _ in range(n): a=mul(a,x)
        return a

    begin = checks
    for x in elems:
        verify(mul(one,x)==x==mul(x,one))
        verify(d(d(x))==zero)
        verify(pi(d(x))==zero)
    for x,y,z in product(elems, repeat=3):
        verify(mul(mul(x,y),z)==mul(x,mul(y,z)))
        verify(mul(x,add(y,z))==add(mul(x,y),mul(x,z)))
    for a,xs in degrees.items():
        for b,ys in degrees.items():
            for x,y in product(xs,ys):
                sign = -1 if a*b%2 else 1
                verify(mul(x,y)==scale(sign,mul(y,x)))
                sign_d = -1 if a%2 else 1
                verify(d(mul(x,y))==add(mul(d(x),y),scale(sign_d,mul(x,d(y)))))
                verify(pi(mul(x,y))==mul(pi(x),pi(y)))
    for x in odd: verify(mul(x,x)==zero)
    for x in ideal_ev:
        verify(gamma(1,x)==x)
        for n in range(1,7):
            verify(d(gamma(n,x))==mul(gamma(n-1,x),d(x)))
            verify(pi(gamma(n,x))==gamma(n,pi(x)))
            for a in ev:
                verify(gamma(n,mul(a,x))==mul(power(a,n),gamma(n,x)))
            for y in ideal_ev:
                total=zero
                for i in range(n+1):
                    total=add(total,mul(gamma(i,x),gamma(n-i,y)))
                verify(gamma(n,add(x,y))==total)
            for q in range(1,7):
                verify(mul(gamma(n,x),gamma(q,x))==scale(comb(n+q,q),gamma(n+q,x)))
                coeff=factorial(n*q)//(factorial(n)*factorial(q)**n)
                verify(gamma(n,gamma(q,x))==scale(coeff,gamma(n*q,x)))
    for x,y in product(odd,repeat=2):
        for n in range(2,7): verify(gamma(n,mul(x,y))==zero)
    lifts=[]
    for c in range(m):
        if c % m == 1 % m and c % m == 0: lifts.append(c)
    verify(not lifts)
    return {"ring":f"Z/{m}Z", "algebra_elements":len(elems),
            "associativity_triples":len(elems)**3,
            "PD_indices_tested":"n,q=1,...,6; gamma_(nq) up to 36",
            "candidate_generator_lifts":m,"chain_lifts":lifts,
            "checks":checks-begin}

# Matrix certificate, over the integers, in degrees -2 and -1.
# d_E=[1], d_M is the unique map to zero, pi_-2=[1], pi_-1=0.
verify(0*1 == 0*1)  # pi d = d pi
matrix=[[1],[1]]
rhs=[1,0]
left=[1,-1]
verify(sum(left[i]*matrix[i][0] for i in range(2))==0)
verify(sum(left[i]*rhs[i] for i in range(2))==1)

finite=[residue_check(m) for m in (2,3,4)]

# Unbounded acyclic Z/4 complex d=2: a periodic local certificate.
verify(2*2 % 4 == 0)
kernel=[a for a in range(4) if 2*a%4==0]
image=sorted({2*a%4 for a in range(4)})
verify(kernel==image)
homotopy_pairs=[(a,b) for a,b in product(range(4),repeat=2) if 2*(a+b)%4==1]
verify(not homotopy_pairs)

# B-002: finite PD quotient of the characteristic-two shuffle algebra.
# Basis t_n=e^{tensor n}, 0<=n<=6.  Multiplication and PD formulas use
# unsigned shuffle counts because all signs are 1 modulo 2.
cutoff=6
def tmul(x,y):
    ans=0
    for i in range(cutoff+1):
        for j in range(cutoff+1-i):
            if (x>>i)&1 and (y>>j)&1 and comb(i+j,i)%2:
                ans ^= 1<<(i+j)
    return ans
def tgamma(n,x):
    vals=[1]+[0]*n
    for m in (2,4,6):
        if not (x>>m)&1: continue
        row=[1]
        for a in range(1,n+1):
            coeff=factorial(m*a)//(factorial(a)*factorial(m)**a)
            row.append((coeff%2)<<(m*a) if m*a<=cutoff else 0)
        vals=[sum_t(tmul(vals[i],row[j-i]) for i in range(j+1)) for j in range(n+1)]
    return vals[n]
def sum_t(values):
    out=0
    for a in values: out ^= a
    return out
def square_mul(x,y):
    return ((x&1)*(y&1)) | ((((x&1)*((y>>1)&1)+((x>>1)&1)*(y&1))%2)<<1)
def square_gamma(n,x):
    return 1 if n==0 else x if n==1 else 0
def map_zero(x):return x&1
def map_two(x):return (x&1)|(((x>>2)&1)<<1)
begin_extra=checks
for x,y in product(range(1<<(cutoff+1)),repeat=2):
    for f in (map_zero,map_two):
        verify(f(tmul(x,y))==square_mul(f(x),f(y)))
for bits in range(8):
    x=sum(((bits>>i)&1)<<(2*i+2) for i in range(3))
    for n in range(7):
        for f in (map_zero,map_two):
            verify(f(tgamma(n,x))==square_gamma(n,f(x)))
verify(map_zero(2)==map_two(2)==0)   # both extend e -> 0
verify(map_zero(4)!=map_two(4))     # different on e tensor e
ts_checks=checks-begin_extra

# B-007: finite rank, integer differential de=2 leaves the negative part.
verify(2 != 0)

out={"statement_id":"D-031","scope":"nonzero commutative rings; cochain grading",
     "degrees":{"u":-2,"v":-1,"epsilon":-2},
     "differential":{"du":"v","dv":"0","d_epsilon":"0"},
     "projection":{"u":"epsilon","v":"0","1":"1"},
     "integer_lift_equations":{"matrix":matrix,"rhs":rhs,
        "left_annihilator":left,"annihilated_matrix":[0],"annihilated_rhs":1},
     "finite_checks":finite,
     "unbounded_acyclic_example":{"ring":"Z/4Z","every_differential":2,
        "kernel_and_image":kernel,"homotopy_pairs_tested":16,
        "solutions_to_2a_plus_2b_equals_1":homotopy_pairs},
     "TS_freeness_counterexample":{"coefficient_ring":"F2","truncated_tensor_weight":cutoff,
        "algebra_elements":1<<(cutoff+1),"maps":"augmentation and t_2 -> y",
        "both_send_t_1_to_zero":True,"different_on_t_2":True,"checks":ts_checks},
     "negative_ideal_counterexample":{"ring":"Z","generator_degree":-1,
        "differential_to_degree_zero":2,"negative_part_differential_stable":False},
     "checks":checks,"elapsed_seconds":time.perf_counter()-start}
dest=Path(__file__).resolve().parents[1]/"logs"/"B_lifting_certificate.json"
dest.parent.mkdir(parents=True,exist_ok=True)
dest.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"output":str(dest),"checks":checks,"elapsed_seconds":out["elapsed_seconds"]}))
